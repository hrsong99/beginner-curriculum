#!/usr/bin/env python3
"""Compare `runtime/` against the shared runtime production actually serves.

    python3 korean/tools/check_runtime_drift.py

Why this exists: a lesson is verified by rendering it locally, and locally it
loads `runtime/`. Deployed, it loads a **pinned CDN tag**. When the two differ,
the render you approved is not the page the learner gets — and the failure is
silent, because nothing 404s. A component you relied on simply has no styles.

That is the same class of bug podo-curriculum's static-control problem is: it
works for whoever authored it and breaks somewhere nobody is looking.

podo-curriculum's `validate.py` cannot catch this. Its layer 5 compares the CDN
against that repo's own `shared/`, which is a copy of this tree — so it verifies
publish integrity, not whether authoring has run ahead of the last publish.

Exit codes: 0 in step, 1 drifted, 2 could not check (no network, no pin found).
Drift is not automatically wrong — being ahead is the normal state between a
change here and a release there. It is wrong to *verify a lesson* against it
without knowing.
"""

from __future__ import annotations

import pathlib
import re
import sys
import urllib.error
import urllib.request

KOREAN = pathlib.Path(__file__).resolve().parent.parent
RUNTIME = KOREAN / "runtime"

# Where the production repo usually sits, so the pin can be read rather than
# typed. Falls back to asking, because a wrong pin is worse than no answer.
SIBLINGS = [
    pathlib.Path.home() / "Documents/podo_repository/podo-curriculum",
    KOREAN.parent.parent / "podo-curriculum",
]
PIN_RE = re.compile(r"baseUrl:\s*(\S+).*?version:\s*(v\d+\.\d+\.\d+)", re.S)


def find_pin() -> tuple[str, str, pathlib.Path] | None:
    for repo in SIBLINGS:
        yaml = repo / "curriculum.yaml"
        if not yaml.is_file():
            continue
        text = yaml.read_text(encoding="utf-8")
        block = text.split("sharedRuntime:", 1)
        if len(block) < 2:
            continue
        m = PIN_RE.search(block[1][:400])
        if m:
            return m.group(1).rstrip("/"), m.group(2), yaml
    return None


def fetch(url: str) -> bytes | None:
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        return b"" if e.code == 404 else None
    except Exception:
        return None


def main() -> int:
    pin = find_pin()
    if pin is None:
        print("✗ could not find spec.sharedRuntime in a podo-curriculum checkout.")
        print("  Looked in:", *(f"\n    {p}" for p in SIBLINGS))
        return 2
    base, version, yaml = pin
    print(f"pinned  : {version}   (from {yaml})")
    print(f"base    : {base}\n")

    local = sorted(
        p for sub in ("css", "js") for p in (RUNTIME / sub).iterdir() if p.is_file()
    )
    ahead, missing, same, unreachable = [], [], [], []

    for path in local:
        rel = f"{path.parent.name}/{path.name}"
        body = fetch(f"{base}@{version}/{rel}")
        if body is None:
            unreachable.append(rel)
            continue
        if body == b"":
            missing.append(rel)
            continue
        mine = path.read_bytes()
        if mine == body:
            same.append(rel)
        else:
            ahead.append((rel, len(mine) - len(body)))

    for rel in same:
        print(f"  ✓ {rel}")
    for rel, delta in ahead:
        print(f"  ✗ {rel}  local differs ({delta:+d} bytes vs {version})")
    for rel in missing:
        print(f"  ✗ {rel}  not in {version} — never published")
    for rel in unreachable:
        print(f"  ? {rel}  could not reach the CDN")

    print()
    if unreachable and not (ahead or missing):
        print("? could not check every file — network. Nothing conclusive.")
        return 2
    if not ahead and not missing:
        print(f"✓ runtime/ is exactly {version}. A local render is what ships.")
        return 0

    print(f"✗ runtime/ has drifted from {version}.")
    print("  Local renders of anything touching these files are not what ships.")
    print("  Publish from podo-curriculum when the change is ready:")
    print("    python3 tools/sync-from-authoring.py --runtime-only")
    print("    python3 tools/publish-shared.py <next-version>")
    print("    python3 tools/repoint-shared.py && python3 tools/validate.py")
    return 1


if __name__ == "__main__":
    sys.exit(main())
