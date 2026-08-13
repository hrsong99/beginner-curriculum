#!/usr/bin/env python3
"""Stamp an empty English lesson from an approved canonical deck.

The tool copies only the deck shell: metadata, shared styles, ``.phone`` frame,
pager and load-order-bearing scripts. It never copies lesson pages and never
overwrites an existing file.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import pathlib
import re


ENGLISH = pathlib.Path(__file__).resolve().parent.parent
REPO = ENGLISH.parent
PHONE_OPEN = '<div class="phone">'
PHONE_CLOSE = re.compile(r"^  </div>\s*$")
SLUG = re.compile(r"^(\d{2,3})-[a-z0-9]+(?:-[a-z0-9]+)*$")
REL_SHARED = re.compile(r'((?:href|src)=")(?:(?:\.\./)+)(runtime|korean)/')
PLACEHOLDER = """

    <!-- ============================================================
         PAGES GO HERE — one .phone child per page, one activity per page.

         Plan the arc from lesson-blueprint.md.
         Take curriculum content and sequence guardrails from {brief}.
         Copy component composition and tutor voice from the canonical deck;
         never invent a new shared component inside a lesson assignment.
         ============================================================ -->

"""


def split_shell(text: str) -> tuple[str, str]:
    lines = text.splitlines(keepends=True)
    body = next((i for i, line in enumerate(lines) if re.match(r"^<body>\s*$", line)), None)
    opened = next((i for i, line in enumerate(lines) if PHONE_OPEN in line), None)
    closes = [i for i, line in enumerate(lines) if PHONE_CLOSE.match(line)]
    if body is None or opened is None or len(closes) != 1 or closes[0] <= opened:
        raise ValueError("canonical deck no longer has one recognisable <body> / .phone shell")
    # Deliberately omit canonical lesson comments between <body> and .phone.
    head = "".join(lines[:body + 1]) + "  " + PHONE_OPEN + "\n"
    foot = "".join(lines[closes[0]:])
    return head, foot


def retarget(head: str, *, lesson_id: str, level: str, title: str, version: str) -> str:
    substitutions = [
        (r'(<meta name="podo:lesson-id" content=")[^"]*(")', lesson_id),
        (r'(<meta name="podo:level" content=")[^"]*(")', level),
        (r'(<meta name="podo:content-version" content=")[^"]*(")', version),
        (r"(<title>).*?(</title>)", title + " — PODO English"),
    ]
    for pattern, value in substitutions:
        head, count = re.subn(pattern, lambda m: m.group(1) + value + m.group(2), head, count=1)
        if count != 1:
            raise ValueError(f"canonical deck is missing required identity field {pattern!r}")
    return head


def redepth(page: str, out: pathlib.Path) -> str:
    def replace(match: re.Match) -> str:
        target = REPO / match.group(2)
        relative = pathlib.Path(os.path.relpath(target, out.parent)).as_posix()
        return match.group(1) + relative + "/"
    return REL_SHARED.sub(replace, page)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track", required=True, choices=("1-core-patterns", "2-contextual-english", "3-freetalking"))
    parser.add_argument("--review-id", required=True, help="stable TOC id, e.g. CORE-31")
    parser.add_argument("--course", required=True, help="provisional course directory")
    parser.add_argument("--lesson", required=True, type=int)
    parser.add_argument("--id", required=True, help="directory and podo:lesson-id, e.g. 31-past-action")
    parser.add_argument("--title", required=True, help="English deck title")
    parser.add_argument("--level", required=True, help="podo:level value")
    parser.add_argument("--from-deck", help="approved canonical lesson.html; Core defaults to its approved pilot")
    parser.add_argument("--out", help="override output lesson.html")
    args = parser.parse_args()

    match = SLUG.fullmatch(args.id)
    if not match or int(match.group(1)) != args.lesson:
        parser.error(f"--id must start with lesson {args.lesson:02d} (for example {args.lesson:02d}-useful-name)")
    expected_prefix = {"1-core-patterns": "CORE", "2-contextual-english": "CTX", "3-freetalking": "FT"}[args.track]
    if args.review_id != f"{expected_prefix}-{args.lesson}":
        parser.error(f"--review-id must be {expected_prefix}-{args.lesson} for this track and lesson")

    track = ENGLISH / "tracks" / args.track
    brief = track / "toc" / f"{args.review_id}.md"
    if not brief.is_file():
        parser.error(f"missing generated brief {brief}; run build_lesson_briefs.py first")
    if args.from_deck:
        source = pathlib.Path(args.from_deck)
    elif args.track == "1-core-patterns":
        source = track / "courses" / "core-first-exchanges-2" / "lessons" / "20-asking-for-help" / "lesson.html"
    else:
        parser.error("this track has no approved canonical deck; pass --from-deck only after its pilot is approved")
    if not source.is_file():
        parser.error(f"canonical deck not found: {source}")

    out = pathlib.Path(args.out) if args.out else track / "courses" / args.course / "lessons" / args.id / "lesson.html"
    if out.exists():
        parser.error(f"refusing to overwrite existing deck: {out}")

    head, foot = split_shell(source.read_text(encoding="utf-8"))
    head = retarget(head, lesson_id=args.id, level=args.level, title=args.title, version=dt.date.today().isoformat())
    page = redepth(head + PLACEHOLDER.format(brief=brief.relative_to(track)) + foot, out)
    if "yomi.js" in page or 'class="yomi"' in page:
        parser.error("canonical shell contains forbidden English yomi support")
    refs = re.findall(r'(?:href|src)="((?:\.\./)+[^"#]+)"', page)
    broken = [ref for ref in refs if not (out.parent / ref).resolve().is_file()]
    if broken:
        parser.error(f"generated shell has {len(broken)} broken reference(s), first: {broken[0]}")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out.relative_to(REPO) if out.is_relative_to(REPO) else out}")
    print(f"  shell: {source.relative_to(REPO) if source.is_relative_to(REPO) else source}")
    print(f"  brief: {brief.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
