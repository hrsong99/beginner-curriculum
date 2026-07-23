#!/usr/bin/env python3
"""
Package a lesson deck for the lemonboard-html upload slot.

The upload slot takes a zip holding exactly one HTML and one CSS file. On
"생성" the zip is unpacked to S3 under lemonboard-html/{교재ID}/ and the two
files are renamed — lecture.html / lecture.css for 수업용, prestudy.html /
prestudy.css for 예습용.

Three consequences drive everything this script does:

  1. Our decks load two stylesheets (the shared lesson-card.css plus the
     track's own sheet). They have to be merged into one, in link order, so
     the cascade survives.
  2. The platform renames the CSS but does not rewrite the <link> inside the
     HTML. So the link has to point at the *post-rename* name.
  3. The same zip goes into both slots. Whichever slot it lands in decides
     the name, so the HTML carries BOTH links — one resolves, the other 404s
     harmlessly, and one file works as 수업용 and 예습용 alike.

Images can't ride along (the unpack flattens into one S3 prefix, and our art
lives in subfolders), so local <img src> is rewritten to a jsDelivr URL pinned
to a commit SHA. Pinned, not @main, so a later commit can't change a deck that
is already live.

Usage:
    python3 build_lemonboard.py SOURCE.html --out DIR
"""

import argparse
import pathlib
import re
import subprocess
import sys
import zipfile

REPO = "hrsong99/beginner-curriculum"
CDN = "https://cdn.jsdelivr.net/gh"

LINK_RE = re.compile(r'[ \t]*<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"[^>]*>\n?')
SRC_RE = re.compile(r'\bsrc="([^"]+)"')


def repo_root(start: pathlib.Path) -> pathlib.Path:
    out = subprocess.run(
        ["git", "-C", str(start.parent), "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True)
    return pathlib.Path(out.stdout.strip())


def head_sha(root: pathlib.Path) -> str:
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def check_clean(root: pathlib.Path, paths: list) -> list:
    """Return the subset of paths that differ from origin/main.

    Anything listed here would 404 (or serve stale bytes) from the CDN, so the
    caller warns loudly rather than shipping a deck with dead images.
    """
    rel = [str(p.relative_to(root)) for p in paths]
    out = subprocess.run(["git", "-C", str(root), "diff", "--name-only", "origin/main", "--", *rel],
                         capture_output=True, text=True)
    changed = [ln for ln in out.stdout.splitlines() if ln.strip()]
    untracked = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--others", "--exclude-standard", "--", *rel],
        capture_output=True, text=True).stdout.splitlines()
    return sorted(set(changed) | set(ln for ln in untracked if ln.strip()))


def build(source: pathlib.Path, outdir: pathlib.Path, sha: str = None):
    root = repo_root(source)
    sha = sha or head_sha(root)
    html = source.read_text(encoding="utf-8")
    srcdir = source.parent
    base = f"{CDN}/{REPO}@{sha}/{srcdir.relative_to(root).as_posix()}/"

    # ---- 1. merge every local stylesheet, in link order, into one file ----
    links = LINK_RE.findall(html)
    local = [l for l in links if not l.startswith(("http://", "https://", "//"))]
    if not local:
        sys.exit(f"no local stylesheet <link> found in {source.name}")

    merged = []
    for href in local:
        path = (srcdir / href).resolve()
        if not path.is_file():
            sys.exit(f"stylesheet not found: {href} -> {path}")
        merged.append(f"/* ===== {path.name} ===== */\n{path.read_text(encoding='utf-8')}")
    css = "\n\n".join(merged)

    # A merged sheet may hold several @import lines; CSS requires them before
    # any rule, so hoist them to the top in first-seen order.
    imports = []

    def lift(m):
        imports.append(m.group(0).strip())
        return ""

    css_body = re.sub(r'^[ \t]*@import[^;]+;[ \t]*\n?', lift, css, flags=re.M)
    if imports:
        css = "\n".join(dict.fromkeys(imports)) + "\n\n" + css_body

    # ---- 2. collapse the link tags down to the renamed sheet ----
    # Both names are emitted so one zip serves both slots; the slot the file
    # did not land in simply 404s, which browsers ignore.
    first = True

    def swap(m):
        nonlocal first
        if m.group(1).startswith(("http://", "https://", "//")):
            return m.group(0)          # leave remote sheets alone
        if first:
            first = False
            return ('  <link rel="stylesheet" href="lecture.css">\n'
                    '  <link rel="stylesheet" href="prestudy.css">\n')
        return ""

    html = LINK_RE.sub(swap, html)

    # ---- 3. local images -> pinned CDN ----
    used = []

    def to_cdn(m):
        ref = m.group(1)
        if ref.startswith(("http://", "https://", "//", "data:", "#")):
            return m.group(0)
        used.append((srcdir / ref).resolve())
        return f'src="{base}{ref}"'

    html, n_img = SRC_RE.subn(to_cdn, html)

    missing = [p for p in used if not p.is_file()]
    if missing:
        sys.exit("referenced images not on disk:\n  " + "\n  ".join(map(str, missing)))

    dirty = check_clean(root, sorted(set(used))) if used else []

    # ---- 4. write + zip ----
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "lecture.html").write_text(html, encoding="utf-8")
    (outdir / "lecture.css").write_text(css, encoding="utf-8")

    zip_path = outdir / f"{source.stem}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(outdir / "lecture.html", "lecture.html")
        z.write(outdir / "lecture.css", "lecture.css")

    leftover = [r for r in SRC_RE.findall(html)
                if not r.startswith(("http://", "https://", "//", "data:", "#"))]

    print(f"{zip_path.name}")
    print(f"  merged css   : {', '.join(pathlib.Path(l).name for l in local)}  -> lecture.css")
    print(f"  hoisted      : {len(imports)} @import")
    print(f"  images -> cdn: {n_img} ({len(set(used))} unique) @ {sha[:8]}")
    print(f"  local refs   : {len(leftover)} remaining {leftover if leftover else '(clean)'}")
    print(f"  slot links   : lecture.css + prestudy.css (same zip works in both slots)")
    if dirty:
        print("  WARNING - not on origin/main, these will 404 from the CDN:")
        for d in dirty:
            print(f"    {d}")
    return zip_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--sha", help="pin images to this commit (default: HEAD)")
    a = ap.parse_args()
    build(a.source.resolve(), a.out.resolve(), a.sha)
