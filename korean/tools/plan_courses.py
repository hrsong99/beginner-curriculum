#!/usr/bin/env python3
"""Lay a track out as courses, in the shape podo-curriculum deploys.

    python3 korean/tools/plan_courses.py korean/tracks/3-contextual-korean
    python3 korean/tools/plan_courses.py --all

A track is not a course. A deployable course is one `classLevel` with weeks
running 1..N and no gaps, so every track has to be cut into courses before any of
it can ship. Doing that cut here, against the table of contents, means the
production importer copies a plan instead of inventing one.

Most tracks already say where the cuts go — `3-contextual-korean` is named shows
of ten episodes, `4-freetalking` is themes of ten sessions, `1-hangul` and
`5-pronunciation` are one course each. Only `2-core-patterns` has to be packed,
because 116 numbered 과 have no course boundaries of their own; there the packer
groups units into roughly twelve lessons without ever splitting a unit, so a
course always ends on its 체크포인트.

Reading each TOC is `track_parsers.py`'s job. This file only turns courses into
YAML.

Layout written under the track:

    courses/<course-slug>/course.yaml
    courses/<course-slug>/lessons/<lesson-slug>/lesson.yaml
    courses/<course-slug>/lessons/<lesson-slug>/lesson.html   <- the deck, if written

Both validate against podo-curriculum's `schemas/`.

**`course.yaml` for every course; `lesson.yaml` only where a deck exists.** The
lesson schema wants a slug of `NN-english-words`, and the English name is a
writing decision that does not exist before the lesson does — scaffolding 350 of
them would be 350 renames later. The plan still shows up: each course lists its
lessons as comments, so a diff shows what is coming without pretending it is here.

**Weeks are provisional until a course is complete**, because `_check_weeks`
demands 1..N with no gaps, so week is the position among lessons that exist. Safe
only because an incomplete course is `enabled: false` and never applied.

**This tool never deletes a directory holding a deck.** It owns the YAML; a
`lesson.html` is handwritten work, so a lesson orphaned by a re-plan is reported,
not removed.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

import track_parsers

# --- 2-core-patterns packing ------------------------------------------------
TARGET = 12            # a course should look like the ones already shipping
MAX_AFTER_MERGE = 15   # a trailing stub may join the previous course up to this
MERGE_IF_UNDER = 5

# classLevel is part of grape's natural key, so two courses sharing one are the
# same row.
#
# **The integer part of CLASS_LEVEL is the section.** This is not written down
# anywhere in either repo — it is the convention the live data follows, and it is
# how Breaking News and 프리토킹 are separate sections of the app while both being
# CURRICULUM_TYPE=BASIC:
#
#     1–2          the graded ladder (level 1, level 2)
#     1000         Breaking News          (15 courses, monthly × level)
#     1001, 1002   single topic courses
#     2001–2006    the Business series
#     3500         가벼운 프리토킹          (12 courses)
#     999          test junk — 'html test (john)' lives here
#
# So a track becomes a section by taking its own integer band, and each course in
# it takes a decimal slot. 999.x was the wrong home: it is where throwaway rows go.
#
# LANG_TYPE already separates KR from EN/JP, so these bands cannot collide with
# the English or Japanese curricula even where the numbers coincide. Audience
# ("Korean for Japanese speakers" vs anything later) is GT_CLASS_COURSE.
# COUNTRY_CODE, not this number — see CLAUDE.md § Getting a lesson to production.
# curriculumType is the product line, and it is part of the course's identity —
# grape refuses a second course with the same (LANG_TYPE, CURRICULUM_TYPE,
# LESSON_TIME, CLASS_LEVEL) outright ("동일한 조건의 코스가 이미 존재합니다",
# class_course_ps.php:656). BASIC_V2 therefore gives the interactive curriculum a
# namespace of its own: it can reuse any level band without colliding with the
# legacy PDF BASIC courses, which is what lets it roll out to existing users.
#
# It also forks tutor assignment — le_tutor_curriculum keys on
# PODO_{LANG}_{TYPE}, so a tutor opts into PODO_KR_BASIC_V2 specifically. That is
# wanted (driving an interactive board is a different skill from a PDF), but it
# means **no tutor can be matched until those rows exist**. There are currently
# zero PODO_KR_* rows of any type.
#
# The column is COLLATE utf8mb3_bin, so this string is CASE-SENSITIVE. 'BASIC_v2'
# would be a separate curriculum with no tutors, and nothing would report it.
TRACKS = {
    "1-hangul":            {"band": 1000, "type": "BASIC_V2"},
    "2-core-patterns":     {"band": 2000, "type": "BASIC_V2"},
    "3-contextual-korean": {"band": 3000, "type": "BASIC_V2"},
    "4-freetalking":       {"band": 4000, "type": "BASIC_V2"},
    "5-pronunciation":     {"band": 5000, "type": "BASIC_V2"},
}

DIFFICULTY = {"왕초급": "BEGINNER", "초급": "BEGINNER", "초중급": "BEGINNER",
              "중급": "INTERMEDIATE", "중고급": "INTERMEDIATE", "고급": "ADVANCED"}
LEVEL_SLUG = {"왕초급": "starter", "초급": "beginner", "초중급": "upper-beginner",
              "중급": "intermediate", "중고급": "upper-intermediate", "고급": "advanced"}
LEVEL_JA = {"왕초급": "超入門", "초급": "初級", "초중급": "初中級",
            "중급": "中級", "중고급": "中上級", "고급": "上級"}
LEVEL_EN = {"왕초급": "Starter", "초급": "Beginner", "초중급": "Upper beginner",
            "중급": "Intermediate", "중고급": "Upper intermediate", "고급": "Advanced"}

CORE_TITLE = {"ko": "핵심 문법 패턴", "en": "Core grammar patterns",
              "ja": "コア文法パターン"}

ID_META = re.compile(r'<meta name="podo:lesson-id" content="([^"]*)">')
TITLE_META = re.compile(r'<meta name="podo:title-(ko|en|ja)" content="([^"]*)">')
# schemas/lesson.schema.json — metadata.slug. Kept verbatim so a mismatch shows
# up while writing rather than at the merge gate.
SLUG_RE = re.compile(r"^[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*$")


def pack_core(units: list) -> list[dict]:
    """2-core-patterns only: units -> ~12-lesson courses, never splitting a unit."""
    groups: list[list] = []
    for level in dict.fromkeys(u["level"] for u in units):      # keep TOC order
        band = [u for u in units if u["level"] == level]
        cur: list = []
        for unit in band:
            n = len(unit["lessons"])
            if cur and sum(len(u["lessons"]) for u in cur) + n > TARGET:
                groups.append(cur)
                cur = []
            cur.append(unit)
        if cur:
            size = sum(len(u["lessons"]) for u in cur)
            prev = groups[-1] if groups else None
            if (prev and prev[0]["level"] == level and size < MERGE_IF_UNDER
                    and sum(len(u["lessons"]) for u in prev) + size <= MAX_AFTER_MERGE):
                prev.extend(cur)
            else:
                groups.append(cur)

    courses, nth = [], {}
    for g in groups:
        level = g[0]["level"]
        nth[level] = nth.get(level, 0) + 1
        lessons = [l for u in g for l in u["lessons"]]
        span = f"Unit {g[0]['no']}" + (f"–{g[-1]['no']}" if len(g) > 1 else "")
        courses.append({
            "slug": f"core-{LEVEL_SLUG[level]}-{nth[level]}",
            "level": level,
            "title": {k: f"{CORE_TITLE[k]} · "
                         f"{ {'ko': level, 'ja': LEVEL_JA[level], 'en': LEVEL_EN[level]}[k] } "
                         f"{nth[level]}" for k in ("ko", "en", "ja")},
            "note": f"{span} · " + " · ".join(u["title"].split(" — ")[0] for u in g),
            "lessons": [{"no": l["no"], "title": l["title"], "canDo": l["can_do"],
                         "patterns": [p["form"] for p in l["patterns"]], "scene": None}
                        for l in lessons],
        })
    return courses


def yaml_str(value: str) -> str:
    """Quote only where YAML would otherwise misread the scalar."""
    value = value.replace("\n", " ").strip()
    if value == "" or value[0] in "!&*[]{}>|%@`'\"#-?:," or ": " in value or " #" in value:
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return value


def deck_meta(deck: pathlib.Path) -> tuple[dict, str | None]:
    raw = deck.read_text(encoding="utf-8")
    m = ID_META.search(raw)
    return dict(TITLE_META.findall(raw)), (m.group(1) if m else None)


def course_yaml(course, cfg, class_level, track, written) -> str:
    plan = "\n".join(
        f"#   {l['no']:>3}  {'✓ ' + written[l['no']] if l['no'] in written else '·  '}"
        f"{l['title']}"
        for l in course["lessons"])
    t = course["title"]
    return f"""\
apiVersion: podo.curriculum/v1
kind: Course
metadata:
  # beginner-curriculum {track} · {len(course['lessons'])}과.
  # tools/plan_courses.py 가 목차에서 끊었다.
  slug: {course['slug']}

spec:
  curriculumType: {cfg['type']}
  # 자연키의 일부다 — 바꾸면 같은 코스의 수정이 아니라 다른 코스가 된다.
  classLevel: "{class_level}"
  lessonTime: 25
  # 검수 전까지는 false. true 로 바꾸는 순간 apply 가 학습자에게 노출시킨다.
  enabled: false
  difficulty: {DIFFICULTY[course['level']]}

  title:
    ko: {yaml_str(t['ko'])}
    en: {yaml_str(t['en'])}
    ja: {yaml_str(t['ja'])}

  description:
    ko: {yaml_str(course['note'] or t['ko'])}
    ja: {yaml_str(f"{LEVEL_JA[course['level']]}。{len(course['lessons'])}課。")}

  tutorGroups:
    allowRandom: []
    assignedOnly: []

# 이 코스가 담을 과 — 덱을 쓰면 lessons/ 밑에 디렉터리가 생긴다.
# 슬러그는 스키마가 NN-english-words 를 요구하므로 덱을 쓸 때 정해진다.
{plan}
# Generated by korean/tools/plan_courses.py — 목차를 고치고 다시 돌린다.
"""


def lesson_yaml(lesson, week, slug, titles, track, course_slug) -> str:
    extra = "".join(f"    {k}: {yaml_str(titles[k])}\n"
                    for k in ("en", "ja") if titles.get(k))
    pats = "\n".join(f"      - {yaml_str(p)}" for p in lesson["patterns"])
    scene = f"  scene: {yaml_str(lesson['scene'])}\n" if lesson.get("scene") else ""
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
{pats or "      []"}
    canDo: {yaml_str(lesson['canDo'] or '')}
{scene}\
  prerequisites: []
  source: beginner-curriculum {track}/{course_slug} · {lesson['no']}

# Generated by korean/tools/plan_courses.py — 내용은 목차와 덱이 원본이다.
"""


def plan_track(track: pathlib.Path, dry: bool) -> int:
    cfg = TRACKS.get(track.name)
    parser = track_parsers.PARSERS.get(track.name)
    if cfg is None or parser is None:
        print(f"✗ no plan for track '{track.name}'")
        return 0

    parsed = parser(track)
    courses = pack_core(parsed) if track.name == "2-core-patterns" else parsed

    root, seen, written_n = track / "courses", set(), 0
    print(f"\n{track.name}")

    for i, course in enumerate(courses, start=1):
        # <band>.<slot> — the band is the section, the decimal is this course.
        # decimal(10,3) in the DB, so three decimals is the whole slot space.
        if i > 999:
            print(f"    ! {track.name} has more than 999 courses — the band is full")
            return 0
        class_level = f"{cfg['band']}.{i:03d}"
        cdir = root / course["slug"]
        seen.add(cdir)

        decks: dict[int, pathlib.Path] = {}
        if (cdir / "lessons").is_dir():
            for deck in sorted((cdir / "lessons").glob("*/lesson.html")):
                m = re.match(r"(\d{2})-", deck.parent.name)
                if m:
                    decks[int(m.group(1))] = deck
                else:
                    print(f"    ! {deck.parent.name}: cannot read a lesson number "
                          f"from the directory name — skipped")

        week = 0
        for lesson in course["lessons"]:
            deck = decks.get(lesson["no"])
            if deck is None:
                continue
            week += 1
            slug = deck.parent.name
            titles, ident = deck_meta(deck)
            if ident and ident != slug:
                print(f"    ! {slug}: podo:lesson-id is '{ident}' — deck and "
                      f"directory must agree")
            if not SLUG_RE.match(slug):
                print(f"    ! {slug}: not NN-english-words — will fail validation")
            seen.add(deck.parent)
            if not dry:
                (deck.parent / "lesson.yaml").write_text(
                    lesson_yaml(lesson, week, slug, titles, track.name,
                                course["slug"]), encoding="utf-8")
            written_n += 1

        if not dry:
            (cdir / "lessons").mkdir(parents=True, exist_ok=True)
            (cdir / "course.yaml").write_text(
                course_yaml(course, cfg, class_level,
                            track.name, {n: d.parent.name for n, d in decks.items()}),
                encoding="utf-8")

        print(f"  {course['slug']:<30} {course['level']:<6} {class_level:<8} "
              f"{len(course['lessons']):>3} planned, {len(decks)} written")

    if root.is_dir():
        for p in sorted(root.rglob("lesson.yaml")):
            if p.parent not in seen:
                keep = "  (has a deck — move it, do not delete)" if \
                    (p.parent / "lesson.html").is_file() else ""
                print(f"  ! orphaned by the current plan: {p.parent}{keep}")

    print(f"  → {len(courses)} course(s), "
          f"{sum(len(c['lessons']) for c in courses)} planned, {written_n} written")
    return len(courses)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("track", nargs="?", help="e.g. korean/tracks/1-hangul")
    ap.add_argument("--all", action="store_true", help="every track with a parser")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    here = pathlib.Path(__file__).resolve().parent.parent
    if args.all:
        targets = [here / "tracks" / n for n in sorted(TRACKS)]
    elif args.track:
        targets = [pathlib.Path(args.track)]
    else:
        return ap.error("give a track path or --all")

    total = sum(plan_track(t, args.dry_run) for t in targets)
    print(f"\n{total} course(s) across {len(targets)} track(s)"
          f"{' — dry run, nothing written' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
