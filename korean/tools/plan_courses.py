#!/usr/bin/env python3
"""Lay a track out as courses, in the shape podo-curriculum deploys.

    python3 korean/tools/plan_courses.py korean/tracks/2-core-patterns

A track is not a course. `2-core-patterns` is 116 lessons across 23 units, while
a deployable course is one `classLevel` with weeks running 1..N and no gaps — so
the track has to be cut into courses before any of it can ship. Doing that cut
here, against the table of contents, means the production importer copies a plan
instead of inventing one.

Layout written under the track:

    courses/<course-slug>/course.yaml
    courses/<course-slug>/lessons/<lesson-slug>/lesson.yaml
    courses/<course-slug>/lessons/<lesson-slug>/lesson.html   <- the deck, if written

Both YAML files validate against `schemas/{course,lesson}.schema.json` over
there. Only `title.ko` is required, so a lesson that has no deck yet is still a
valid, reviewable row — its Korean title comes from the TOC, and `en`/`ja` arrive
with the deck (which carries `podo:title-*`).

**`course.yaml` is written for all 12 courses; `lesson.yaml` only for lessons
that have a deck.** The lesson schema requires a slug matching
`^[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*$` — two digits and an English name — and the
English name is a writing decision that does not exist before the lesson does.
Scaffolding 108 `07-tbd` directories would just be 108 renames later. The full
plan still shows up: every course lists its unwritten lessons as comments, so
the diff shows what is coming without pretending it is here.

The slug comes from the deck's own `podo:lesson-id`, so the authoring id and the
deployed directory are the same string and neither can drift.

**Weeks are provisional until a course is complete.** Week is the position among
lessons that exist, because `model._check_weeks` demands 1..N with no gaps. Add
과 1–6 to a course that only had 과 7 and 과 7 moves from week 1 to week 7. That is
safe precisely because an incomplete course is `enabled: false` and never applied.

**This tool never deletes a directory holding a deck.** It owns the YAML and will
rewrite it freely, but a `lesson.html` is handwritten work — if the plan moves a
lesson to a different course, the old directory is reported, not removed.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

import shard_toc

# A course wants to look like the ones already shipping (hangul-lv1 is 11).
# Units are never split — each ends on its 체크포인트, which is the course's exit
# test — so these are targets the packer respects rather than hard sizes.
TARGET = 12
# A trailing stub gets folded back rather than shipped as a 3-lesson course,
# provided the course it joins stays inside this.
MAX_AFTER_MERGE = 15
MERGE_IF_UNDER = 5

# Per-track identity. classLevel is part of grape's natural key, so changing one
# creates a course rather than editing it; 999.x is the test band.
TRACKS = {
    "2-core-patterns": {
        "prefix": "core",
        "curriculumType": "BASIC",
        "levelBase": {"초급": "999.31", "초중급": "999.32", "중급": "999.33",
                      "중고급": "999.34", "고급": "999.35"},
        "difficulty": {"초급": "BEGINNER", "초중급": "BEGINNER", "중급": "INTERMEDIATE",
                       "중고급": "INTERMEDIATE", "고급": "ADVANCED"},
        "levelSlug": {"초급": "beginner", "초중급": "upper-beginner", "중급": "intermediate",
                      "중고급": "upper-intermediate", "고급": "advanced"},
        "titleJa": {"초급": "初級", "초중급": "初中級", "중급": "中級",
                    "중고급": "中上級", "고급": "上級"},
        "titleEn": {"초급": "Beginner", "초중급": "Upper beginner", "중급": "Intermediate",
                    "중고급": "Upper intermediate", "고급": "Advanced"},
        "courseTitle": {"ko": "핵심 문법 패턴", "en": "Core grammar patterns",
                        "ja": "コア文法パターン"},
    },
}

TITLE_META = re.compile(r'<meta name="podo:title-(ko|en|ja)" content="([^"]*)">')
ID_META = re.compile(r'<meta name="podo:lesson-id" content="([^"]*)">')
# schemas/lesson.schema.json — metadata.slug. Kept here verbatim so a mismatch
# surfaces while writing rather than at the merge gate.
SLUG_RE = re.compile(r"^[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*$")


def pack(units: list) -> list[list]:
    """Group units into courses of ~TARGET lessons without splitting a unit."""
    courses: list[list] = []
    for level in dict.fromkeys(u["level"] for u in units):     # keep TOC order
        band = [u for u in units if u["level"] == level]
        cur: list = []
        for unit in band:
            n = len(unit["lessons"])
            if cur and sum(len(u["lessons"]) for u in cur) + n > TARGET:
                courses.append(cur)
                cur = []
            cur.append(unit)
        if cur:
            size = sum(len(u["lessons"]) for u in cur)
            prev = courses[-1] if courses else None
            if (prev and prev[0]["level"] == level and size < MERGE_IF_UNDER
                    and sum(len(u["lessons"]) for u in prev) + size <= MAX_AFTER_MERGE):
                prev.extend(cur)
            else:
                courses.append(cur)
    return courses


def yaml_str(value: str) -> str:
    """Quote only when YAML would otherwise misread it."""
    if value == "" or value[0] in "!&*[]{}>|%@`'\"#-?:," or ": " in value or " #" in value:
        return '"' + value.replace('"', '\\"') + '"'
    return value


def deck_titles(deck: pathlib.Path | None) -> dict[str, str]:
    if deck is None or not deck.is_file():
        return {}
    return dict(TITLE_META.findall(deck.read_text(encoding="utf-8")))


def course_yaml(cfg, slug, level, units, lessons, track, nth, written) -> str:
    first, last = lessons[0]["no"], lessons[-1]["no"]
    plan = "\n".join(
        f"#   과 {l['no']:>3}  {'✓ ' + written[l['no']] if l['no'] in written else '· '}"
        f"{l['title']}"
        for l in lessons)
    unit_span = f"Unit {units[0]['no']}" + (
        f"–{units[-1]['no']}" if len(units) > 1 else "")
    return f"""\
apiVersion: podo.curriculum/v1
kind: Course
metadata:
  # beginner-curriculum {track} · {unit_span} · 과 {first}–{last}.
  # tools/plan_courses.py 가 목차에서 끊었다 — 단원을 쪼개지 않고 12과 안팎으로
  # 묶으므로, 코스의 마지막 과는 언제나 그 단원의 체크포인트다.
  slug: {slug}

spec:
  curriculumType: {cfg['curriculumType']}
  # 자연키의 일부다 — 바꾸면 같은 코스의 수정이 아니라 다른 코스가 된다.
  # 레벨 대역 + 그 안에서의 순번이라 같은 (KR, BASIC, 25) 안에서 겹치지 않는다.
  classLevel: "{cfg['levelBase'][level]}{nth}"
  lessonTime: 25
  # 검수 전까지는 false. true 로 바꾸는 순간 apply 가 학습자에게 노출시킨다.
  enabled: false
  difficulty: {cfg['difficulty'][level]}

  title:
    ko: {yaml_str(f"{cfg['courseTitle']['ko']} · {level} {slug.rsplit('-', 1)[-1]}")}
    en: {yaml_str(f"{cfg['courseTitle']['en']} · {cfg['titleEn'][level]} {slug.rsplit('-', 1)[-1]}")}
    ja: {yaml_str(f"{cfg['courseTitle']['ja']} · {cfg['titleJa'][level]} {slug.rsplit('-', 1)[-1]}")}

  description:
    ko: {yaml_str(' · '.join(u['title'].split(' — ')[0] for u in units))}
    ja: {yaml_str(f"{cfg['titleJa'][level]}。{len(lessons)}課。")}

  tutorGroups:
    allowRandom: []
    assignedOnly: []

# 이 코스가 담을 과 — 덱을 쓰면 lessons/ 밑에 디렉터리가 생긴다.
# 슬러그는 스키마가 NN-english-words 를 요구하므로 덱을 쓸 때 정해진다.
{plan}
# Generated by korean/tools/plan_courses.py — 목차를 고치고 다시 돌린다.
# enabled · tutorGroups 는 배포 쪽 검수에서 정하므로 저쪽에서 덮어쓰지 않는다.
"""


def lesson_yaml(lesson, week, slug, titles, track, brief) -> str:
    u = lesson["unit"]
    patterns = "\n".join(f"      - {yaml_str(p['form'])}" for p in lesson["patterns"])
    extra = ""
    for lang in ("en", "ja"):
        if titles.get(lang):
            extra += f"    {lang}: {yaml_str(titles[lang])}\n"
    return f"""\
apiVersion: podo.curriculum/v1
kind: Lesson
metadata:
  slug: {slug}

spec:
  week: {week}                      # → CLASS_WEEK. 코스 안에서 1..N 연속이어야 한다.

  title:
    ko: {yaml_str(titles.get('ko') or lesson['title'])}
{extra}\
  decks:
    lecture:  {{ entry: lecture/index.html }}    # 수업용  → CLASS_LEMONBOARD_KEY
    prestudy: {{ entry: prestudy/index.html }}   # 예습용  → PRESTUDY_LEMONBOARD_KEY

  # ---- 아래는 레포에만 남는다. DB 로 가지 않는다 ----
  teaches:
    patterns:
{patterns or "      []"}
    canDo: {yaml_str(lesson['can_do'] or '')}
  prerequisites: []
  source: beginner-curriculum {track}/toc/{brief}

# Generated by korean/tools/plan_courses.py — 내용은 목차와 덱이 원본이다.
"""


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("track", help="e.g. korean/tracks/2-core-patterns")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    track = pathlib.Path(args.track)
    cfg = TRACKS.get(track.name)
    if cfg is None:
        sys.exit(f"no course plan for track '{track.name}' — add it to TRACKS "
                 f"(each track's TOC has its own shape; see shard_toc.py)")

    units = shard_toc.parse(track / "table-of-contents.md")
    if not units:
        sys.exit(f"parsed 0 units from {track}/table-of-contents.md")

    groups = pack(units)
    root = track / "courses"
    seen: set[pathlib.Path] = set()
    counter: dict[str, int] = {}
    written = 0

    for units_in in groups:
        level = units_in[0]["level"]
        counter[level] = counter.get(level, 0) + 1
        slug = f"{cfg['prefix']}-{cfg['levelSlug'][level]}-{counter[level]}"
        lessons = [l for u in units_in for l in u["lessons"]]

        cdir = root / slug
        seen.add(cdir)

        # A lesson exists here iff someone wrote a deck for it. Find them by
        # their 과 number, which lives in the brief the deck was written from.
        decks: dict[int, pathlib.Path] = {}
        for deck in sorted((cdir / "lessons").rglob("lesson.html")) \
                if (cdir / "lessons").is_dir() else []:
            m = re.search(r"toc/lesson-(\d+)\.md", deck.read_text(encoding="utf-8")) \
                or re.match(r"(\d{2})-", deck.parent.name)
            n = int(m.group(1)) if m else None
            if n is None:
                print(f"  ! cannot tell which 과 {deck} is — skipped")
                continue
            decks[n] = deck

        week = 0
        for lesson in lessons:
            deck = decks.get(lesson["no"])
            if deck is None:
                continue
            week += 1
            lslug = deck.parent.name
            m = ID_META.search(deck.read_text(encoding="utf-8"))
            if m and m.group(1) != lslug:
                print(f"  ! {lslug}: podo:lesson-id is '{m.group(1)}' — "
                      f"the deck and its directory must agree")
            if not SLUG_RE.match(lslug):
                print(f"  ! {lslug}: not a valid lesson slug "
                      f"(needs NN-english-words) — will fail schema validation")
            seen.add(deck.parent)
            text = lesson_yaml(lesson, week, lslug, deck_titles(deck), track.name,
                               f"lesson-{lesson['no']:03d}.md")
            if not args.dry_run:
                (deck.parent / "lesson.yaml").write_text(text, encoding="utf-8")
            written += 1

        body = course_yaml(cfg, slug, level, units_in, lessons, track.name,
                           counter[level],
                           {n: d.parent.name for n, d in decks.items()})
        if not args.dry_run:
            (cdir / "lessons").mkdir(parents=True, exist_ok=True)
            (cdir / "course.yaml").write_text(body, encoding="utf-8")

        print(f"  {slug:<28} {level:<5} 과 {lessons[0]['no']:>3}–{lessons[-1]['no']:<3} "
              f"{len(lessons):>2} planned, {len(decks)} written")

    # Never delete handwritten work; say what no longer fits the plan.
    if root.is_dir():
        orphans = [p for p in sorted(root.rglob("lesson.yaml"))
                   if p.parent not in seen]
        for p in orphans:
            keep = "  (has a deck — move it, do not delete)" if \
                (p.parent / "lesson.html").is_file() else ""
            print(f"  ! orphaned by the current plan: {p.parent}{keep}")

    print(f"\n{len(groups)} course(s), {written} lesson(s)"
          f"{' — dry run, nothing written' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
