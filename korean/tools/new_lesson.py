#!/usr/bin/env python3
"""Stamp an empty deck skeleton for a new lesson.

    python3 korean/tools/new_lesson.py \
        --track 2-core-patterns --lesson 7 \
        --id core-07-daily-routine \
        --title "저는 매일 운동해요 · 하루 일과" \
        --act "매일 운동해요"

The skeleton is ~70 lines that must be byte-exact every time: the meta block, the
stylesheet links, and sixteen script tags whose *load order is load-bearing*
(pager after activities, highlight after the ja→ko tooltips, stamp outside
.phone, …). Hand-copying that is pure downside — it is not creative work and a
silent reorder breaks the deck in ways that only show up on the other person's
screen.

So this does not hold a copy of the skeleton. It reads the track's canonical
deck and lifts the head and foot off it, which means the skeleton can never
drift from the real one and per-track differences (a hangul deck's extra
hangul-activities.js, a freetalk deck's freetalk-activities.js) come along for
free. Writing the pages is the only thing left to do.
"""

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

KOREAN = Path(__file__).resolve().parent.parent

# the one line at this exact indent is .phone's closing tag — pages are its
# direct children, so everything before the opener and after the closer is frame
PHONE_OPEN = '<div class="phone">'
PHONE_CLOSE_RE = re.compile(r"^  </div>\s*$")

PLACEHOLDER = """
    <!-- ============================================================
         PAGES GO HERE — one .phone child per page, one activity per page.

         Plan the arc from  lesson-blueprint.md
         Take the content from  toc/lesson-{lesson:03d}.md
         Copy component markup and tutor voice from the deck this
         skeleton came from — do not invent components.

         The first page must carry data-act, since the cover that used
         to supply it is a trial-only page and is not here.
         ============================================================ -->
"""


def split_skeleton(deck: Path):
    """Return (head, foot) of a canonical deck — everything that isn't pages."""
    lines = deck.read_text(encoding="utf-8").splitlines(keepends=True)

    open_at = next((i for i, l in enumerate(lines) if PHONE_OPEN in l), None)
    if open_at is None:
        sys.exit(f"{deck}: no {PHONE_OPEN} — is this a lesson deck?")

    closes = [i for i, l in enumerate(lines) if PHONE_CLOSE_RE.match(l)]
    if len(closes) != 1:
        sys.exit(
            f"{deck}: expected exactly one '  </div>' closing .phone, found "
            f"{len(closes)}. The deck's indentation changed — fix this script "
            f"rather than guessing a boundary."
        )

    return "".join(lines[: open_at + 1]), "".join(lines[closes[0] :])


def retarget(head: str, *, lesson_id: str, level: str, titles: dict, version: str) -> str:
    """Swap the canonical deck's identity for the new lesson's.

    The three `podo:title-*` metas exist so the deck is self-describing: the
    production importer builds `lesson.yaml` from them rather than from a table
    it has to keep in step with 116 files. A title that lives in two places is a
    title that will disagree with itself.
    """
    subs = [
        (r'(<meta name="podo:lesson-id" content=")[^"]*(")', lesson_id),
        (r'(<meta name="podo:level" content=")[^"]*(")', level),
        (r'(<meta name="podo:content-version" content=")[^"]*(")', version),
        (r"(<title>).*?(</title>)", f"{titles['ko']} — PODO 韓国語"),
    ]
    for pattern, value in subs:
        head, n = re.subn(pattern, lambda m: m.group(1) + value + m.group(2), head, count=1)
        if not n:
            sys.exit(f"skeleton is missing the field matched by {pattern!r} — deck format changed")

    block = "".join(
        f'  <meta name="podo:title-{lang}" content="{titles[lang]}">\n'
        for lang in ("ko", "en", "ja")
    )
    head, n = re.subn(r"([ \t]*<title>)", block + r"\1", head, count=1)
    if not n:
        sys.exit("skeleton has no <title> to anchor the title metas to")
    return head


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--track", required=True, help="e.g. 2-core-patterns")
    ap.add_argument("--lesson", required=True, type=int, help="과 number, e.g. 7")
    ap.add_argument("--id", required=True, help="podo:lesson-id, e.g. core-07-daily-routine")
    ap.add_argument("--title-ko", required=True, help="Korean title; also becomes <title>")
    ap.add_argument("--title-ja", required=True, help="Japanese title — the learner reads this one")
    ap.add_argument("--title-en", required=True, help="English title, for the admin course list")
    ap.add_argument("--level", default="초급")
    ap.add_argument("--from-deck", help="deck to lift the skeleton from (default: the track's sample-lesson.html)")
    ap.add_argument("--out", help="output path (default: <track>/lesson-NNN.html)")
    args = ap.parse_args()

    track_dir = KOREAN / "tracks" / args.track
    if not track_dir.is_dir():
        sys.exit(f"no such track: {track_dir}")

    source = Path(args.from_deck) if args.from_deck else track_dir / "sample-lesson.html"
    if not source.exists():
        sys.exit(f"no canonical deck at {source} — pass --from-deck")

    out = Path(args.out) if args.out else track_dir / f"lesson-{args.lesson:03d}.html"
    if out.exists():
        sys.exit(f"{out} already exists — delete it or pass a different --out")

    head, foot = split_skeleton(source)
    head = retarget(
        head,
        lesson_id=args.id,
        level=args.level,
        titles={"ko": args.title_ko, "en": args.title_en, "ja": args.title_ja},
        version=dt.date.today().isoformat(),
    )

    out.write_text(head + PLACEHOLDER.format(lesson=args.lesson) + foot, encoding="utf-8")

    def rel(p: Path) -> str:
        """Repo-relative when possible — --out may point anywhere."""
        try:
            return str(p.resolve().relative_to(KOREAN.parent))
        except ValueError:
            return str(p)

    brief = track_dir / "toc" / f"lesson-{args.lesson:03d}.md"
    print(f"wrote {rel(out)}")
    print(f"  skeleton from : {rel(source)}")
    print(f"  now read      : {rel(track_dir / 'lesson-blueprint.md')}")
    print(f"                  {rel(brief)}" + ("" if brief.exists() else "  (missing — run shard_toc.py)"))
    print(f"                  {rel(source)}  ← voice and components")


if __name__ == "__main__":
    main()
