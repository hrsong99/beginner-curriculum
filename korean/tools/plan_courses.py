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
# CLASS_LEVEL is also used by hard-coded backend ranges. Existing data follows
# an integer-band convention, but a band does not create a new app section by
# itself — the backend and app still need an explicit label/filter for that range:
#
#     1–2          the graded ladder (level 1, level 2)
#     1000         Breaking News          (15 courses, monthly × level)
#     1001, 1002   single topic courses
#     2001–2006    the Business series
#     3500         가벼운 프리토킹          (12 courses)
#     999          test junk — 'html test (john)' lives here
#
# Give each Korean track its own 100-level band. Primary course positions advance
# by 0.010, leaving nine 0.001 insertion slots between neighbours. When the
# fractional part is exhausted the sequence continues normally (200.990,
# 201.000, 201.010, ...), so one section can hold 9,999 primary positions.
# Keeping the bands below 1000 matters: the current BASIC query treats >=1000 as
# legacy special content (Breaking News / free talking), while <1000 remains in
# the regular BASIC ladder. 999.x is also the wrong home: throwaway rows live there.
#
# LANG_TYPE already separates KR from EN/JP, so these bands cannot collide with
# the English or Japanese curricula even where the numbers coincide. Audience
# ("Korean for Japanese speakers" vs anything later) is GT_CLASS_COURSE.
# COUNTRY_CODE, not this number — see AGENTS.md § Getting a lesson to production.
# curriculumType is a supported product line, not a content-edition number.
# podo-app, podo-backend, and grape all know BASIC; none supports invented
# version-suffixed variants. Using
# BASIC also makes tutor assignment use the supported PODO_KR_BASIC key. A future
# English curriculum generation should likewise stay BASIC and receive unused
# CLASS_LEVEL values; do not invent BASIC_V3.
#
# `prefix` and `name` make every course say which track and level it belongs to.
# A slug is <prefix>-<bare>-<level>, so `drama-crush` — which told you nothing —
# is now `ctx-drama-crush-intermediate`, and a directory listing groups by track
# and then by course, with the level last. Single-course tracks drop the bare part.
TRACKS = {
    "1-hangul":            {"band": 100, "type": "BASIC", "prefix": "hangul",
                            "name": {"ko": "한글 떼기", "en": "Hangul reading",
                                     "ja": "ハングル入門"}},
    # levelFirst: core's bare name is only a counter, so the level *is* its
    # identity and the number just orders within it. Level-last would sort
    # core-1-advanced next to core-1-beginner and hide the progression. Every
    # other track has a real name (a show, a theme), which is what should sort.
    "2-core-patterns":     {"band": 200, "type": "BASIC", "prefix": "core",
                            "levelFirst": True,
                            "name": {"ko": "핵심 문법 패턴", "en": "Core grammar patterns",
                                     "ja": "コア文法パターン"}},
    "3-contextual-korean": {"band": 300, "type": "BASIC", "prefix": "ctx",
                            "name": {"ko": "상황별 한국어", "en": "Korean in context",
                                     "ja": "場面別の韓国語"}},
    "4-freetalking":       {"band": 400, "type": "BASIC", "prefix": "talk",
                            "name": {"ko": "프리토킹", "en": "Free talking",
                                     "ja": "フリートーキング"}},
    "5-pronunciation":     {"band": 500, "type": "BASIC", "prefix": "pron",
                            "name": {"ko": "발음 교정", "en": "Pronunciation repair",
                                     "ja": "発音の矯正"}},
}

DIFFICULTY = {"왕초급": "BEGINNER", "초급": "BEGINNER", "초중급": "BEGINNER",
              "중급": "INTERMEDIATE", "중고급": "INTERMEDIATE", "고급": "ADVANCED"}
LEVEL_SLUG = {"왕초급": "starter", "초급": "beginner", "초중급": "upper-beginner",
              "중급": "intermediate", "중고급": "upper-intermediate", "고급": "advanced"}
LEVEL_JA = {"왕초급": "超入門", "초급": "初級", "초중급": "初中級",
            "중급": "中級", "중고급": "中上級", "고급": "上級"}
LEVEL_EN = {"왕초급": "Starter", "초급": "Beginner", "초중급": "Upper beginner",
            "중급": "Intermediate", "중고급": "Upper intermediate", "고급": "Advanced"}

ID_META = re.compile(r'<meta name="podo:lesson-id" content="([^"]*)">')
TITLE_META = re.compile(r'<meta name="podo:title-(ko|en|ja)" content="([^"]*)">')
# schemas/lesson.schema.json — metadata.slug. Kept verbatim so a mismatch shows
# up while writing rather than at the merge gate.
SLUG_RE = re.compile(r"^[0-9]{2,3}-[a-z0-9]+(-[a-z0-9]+)*$")


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
        # bare name only — compose() adds the track prefix, level and titles, the
        # same way it does for every other track.
        courses.append({
            "slug": str(nth[level]),
            "level": level,
            "title": {k: str(nth[level]) for k in ("ko", "en", "ja")},
            "note": f"{span} · " + " · ".join(u["title"].split(" — ")[0] for u in g),
            "lessons": [{"no": l["no"], "title": l["title"], "canDo": l["can_do"],
                         "patterns": [p["form"] for p in l["patterns"]], "scene": None}
                        for l in lessons],
        })
    return courses


def compose(course: dict, cfg: dict) -> dict:
    """Give a course a slug and titles that name its track and level.

    Parsers return a *bare* name — `drama-crush`, `me-lately`, `1` — because the
    track knows its own prefix and the level comes off the course. Composing here
    means a slug can never disagree with the track it sits in.

        ctx-drama-crush-intermediate     상황별 한국어 · 설렘 & 고백 · 중급
        talk-me-lately-advanced          프리토킹 · 요즘의 나 · 고급
        core-1-beginner                  핵심 문법 패턴 · 1 · 초급
        hangul-starter                   한글 떼기 · 왕초급

    **The level goes last** — it is the least distinguishing part of the name, so
    putting it at the end lets `ctx-drama-*` and `ctx-kpop-*` sort together by
    show instead of being scattered across levels.

    **Except where the bare name is only a counter.** `2-core-patterns` sets
    `levelFirst`, because there the level is the identity and the number merely
    orders within it — level-last would interleave `core-1-advanced` with
    `core-1-beginner` and lose the progression:

        core-beginner-1 … -4      핵심 문법 패턴 · 초급 · 1
        core-upper-beginner-1 … -2
        core-intermediate-1 … -3

    A single-course track drops the bare part rather than repeating itself
    (`hangul-starter`, not `hangul-reading-starter`).
    """
    level = course["level"]
    bare = course["slug"].strip("-")
    lvl = LEVEL_SLUG[level]
    order = (lvl, bare) if cfg.get("levelFirst") else (bare, lvl)
    course["slug"] = "-".join(x for x in (cfg["prefix"], *order) if x)

    label = {"ko": level, "en": LEVEL_EN[level], "ja": LEVEL_JA[level]}
    course["title"] = {
        k: " · ".join(
            x for x in (cfg["name"][k],
                        *((label[k], course["title"].get(k)) if cfg.get("levelFirst")
                          else (course["title"].get(k), label[k])))
            if x)
        for k in ("ko", "en", "ja")
    }
    return course


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
        f"{l['title']}{' [깊게]' if l.get('deep') else ''}"
        for l in course["lessons"])
    t = course["title"]
    return f"""\
apiVersion: podo.curriculum/v1
kind: Course
metadata:
  # podo-curriculum-public {track} · {len(course['lessons'])}과.
  # tools/plan_courses.py 가 목차에서 끊었다.
  #
  # podo:level: {course['level']}
  # 이 코스의 덱이 <meta name="podo:level"> 에 적을 값이다. 스키마가 metadata 에
  # 새 필드를 막아서 주석으로 둔다 — tools/new_lesson.py 가 이 줄을 읽는다.
  # 발음 표기(.yomi)를 다는지가 이 값으로 갈리므로 덱마다 손으로 넣게 두면 안 된다.
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
  source: podo-curriculum-public {track}/{course_slug} · {lesson['no']}

# Generated by korean/tools/plan_courses.py — 내용은 목차와 덱이 원본이다.
"""


def plan_track(track: pathlib.Path, dry: bool, only_course: str | None = None) -> int:
    cfg = TRACKS.get(track.name)
    parser = track_parsers.PARSERS.get(track.name)
    if cfg is None or parser is None:
        print(f"✗ no plan for track '{track.name}'")
        return 0

    parsed = parser(track)
    courses = pack_core(parsed) if track.name == "2-core-patterns" else parsed
    courses = [compose(c, cfg) for c in courses]
    selected_courses = [c for c in courses if only_course is None or c["slug"] == only_course]
    if not selected_courses:
        print(f"✗ no course '{only_course}' in track '{track.name}'")
        return 0

    root, seen, written_n = track / "courses", set(), 0
    print(f"\n{track.name}")

    used_class_levels: set[str] = set()
    for i, course in enumerate(courses, start=1):
        # Most courses advance by .010 across the 100-level section. A parser
        # may reserve an explicit thousandth slot when an existing natural key
        # must stay fixed while a paired course is inserted beside it. Free
        # talking uses .009/.010, .019/.020, ... for Intermediate/Advanced.
        slot = course.get("classLevelSlot", i * 10)
        if not isinstance(slot, int) or not 1 <= slot <= 99_999:
            print(f"    ! {course['slug']}: classLevelSlot must be an integer "
                  "from 1 to 99,999")
            return 0
        class_level_units = cfg["band"] * 1000 + slot
        class_level = f"{class_level_units // 1000}.{class_level_units % 1000:03d}"
        if class_level in used_class_levels:
            print(f"    ! {course['slug']}: duplicate classLevel {class_level}")
            return 0
        used_class_levels.add(class_level)
        if only_course is not None and course["slug"] != only_course:
            continue
        cdir = root / course["slug"]
        seen.add(cdir)

        decks: dict[int, pathlib.Path] = {}
        if (cdir / "lessons").is_dir():
            for deck in sorted((cdir / "lessons").glob("*/lesson.html")):
                m = re.match(r"(\d{2,3})-", deck.parent.name)
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

    if only_course is None and root.is_dir():
        for p in sorted(root.rglob("lesson.yaml")):
            if p.parent not in seen:
                keep = "  (has a deck — move it, do not delete)" if \
                    (p.parent / "lesson.html").is_file() else ""
                print(f"  ! orphaned by the current plan: {p.parent}{keep}")

    print(f"  → {len(selected_courses)} course(s), "
          f"{sum(len(c['lessons']) for c in selected_courses)} planned, {written_n} written")
    return len(selected_courses)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("track", nargs="?", help="e.g. korean/tracks/1-hangul")
    ap.add_argument("--all", action="store_true", help="every track with a parser")
    ap.add_argument("--course", help="regenerate only this course (requires one track)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.all and args.course:
        return ap.error("--course cannot be combined with --all")

    here = pathlib.Path(__file__).resolve().parent.parent
    if args.all:
        targets = [here / "tracks" / n for n in sorted(TRACKS)]
    elif args.track:
        targets = [pathlib.Path(args.track)]
    else:
        return ap.error("give a track path or --all")

    total = sum(plan_track(t, args.dry_run, args.course) for t in targets)
    print(f"\n{total} course(s) across {len(targets)} track(s)"
          f"{' — dry run, nothing written' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
