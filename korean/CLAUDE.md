# Working in `korean/`

**Read [`ux-philosophy.md`](./ux-philosophy.md) before touching anything in this folder — every
time, including small edits.** It is the contract for every lesson page: one activity per page,
instant clarity, minimal everything, Korean-first titles, one blue tutor-script box, one boxed
component that *fills* the page, receptive → productive.

Do not design a page, add a component, or write copy here until you have read it. If a change
you are about to make conflicts with it, say so and ask — don't quietly deviate.

## Also true of this folder

- **Shared design system:** `runtime/css/lesson-card.css`. White cards on a 1px grey outline; the
  palette lives in `:root` there — **use the tokens, never the hex**. Per-track additions go in
  that track's own stylesheet, loaded after it (e.g. `runtime/css/trial.css`). Reuse the existing
  component vocabulary before inventing a new one — consistency over novelty.
- **Every colour means one thing.** `green-500`/`green-100` = state (chosen, correct, active).
  `blue-100` = the tutor's spoken script. `lime` = brand chrome only, never state.
  `gray-200` = ordinary outlines. Dashed grey = "write here". The cream/pink seat colours are
  pedagogy and outrank everything. Adding a second meaning to any of these is the single
  easiest way to make a page unreadable — see the table in `ux-philosophy.md`.
- **Audience is Japanese speakers learning Korean.** All support text is Japanese; no English.
  Sound anchors are kana, not English words.
- **Pronunciation stops at 초중급. This is a level rule, not a per-deck taste.**
  A kana reading (`.yomi`) under the Korean is a decoding crutch, so it belongs only where the
  learner may not yet decode hangul — **왕초급 · 초급 · 초중급 and no further**. From 중급 up,
  reading hangul is a skill the learner already has and the deck must not do it for them.
  Every deck declares its own level in `<meta name="podo:level">`; check it before adding a
  reading to anything.

  | Trial deck | Level | Readings |
  |---|---|---|
  | `trial-1-hangul` | 왕초급 | yes |
  | `trial-2-patterns` | 초급 | yes — the reference implementation |
  | `trial-3-contextual` | 중급 | **no** |
  | `trial-4-freetalking` | 고급 | **no** |

  Where readings do apply, `runtime/js/yomi.js` puts a named **よみがな** switch on the title
  line of every page that has them; it hides them deck-wide and the state is shared with the
  other screen. See `AUTHORING.md` § 발음 표기 for where a reading goes and where it must not
  (never inside a two-way `.opt` pill).
- **The blue `.section-subtitle` box is the tutor's spoken script** (`.ko` = the line read
  aloud, `.ja` = its Japanese translation). Natural spoken Korean, no grammar jargon.
- **Lessons are audio-only.** The learner hears the tutor but never sees them, so no
  instruction may depend on watching the tutor (口の形をまねして, gestures, "look at me").
  Model sounds by saying them — 제가 먼저 읽을게요. 잘 듣고 따라 읽어 보세요.
- **Max two levels of boxes:** the page card plus ONE boxed component inside it. Never wrap
  bordered components in another bordered card.
- Every lesson page needs `<meta name="google" content="notranslate">` or Chrome auto-translate
  mangles the mixed ja/ko content.
- **Verify visually.** These are visual documents; render them in a browser at 480px width and
  look at the screenshots before claiming a change works.

## Writing a new lesson

Four inputs, in this order. Read them all — the budget saved by the first two is there to be
spent on the last one.

1. **`tools/new_lesson.py`** stamps the deck skeleton. The meta block, the stylesheet links and
   the sixteen script tags whose load order is load-bearing are not yours to retype — the script
   lifts them off the track's canonical deck so they cannot drift.
   `python3 korean/tools/new_lesson.py --track 2-core-patterns --lesson 7 --id core-07-… --title "…"`
2. **`tracks/<track>/toc/lesson-NNN.md`** — what this lesson teaches, what the learner already
   knows, and what must not be used yet because a later lesson teaches it. This is generated
   from `table-of-contents.md` by `tools/shard_toc.py`; **never hand-edit a brief**, edit the
   TOC and re-run. Read the brief, not the 93KB TOC.
3. **`tracks/<track>/lesson-blueprint.md`** — which pages, in what order, doing what. Plan the
   arc from here.
4. **The trial deck the blueprint names** (`trial/lessons/trial-N-*.html`), in full. This is the
   expensive read and it is the one worth paying for: the blueprint carries structure, but the
   tutor's spoken voice, the way a wrong answer is made wrong for a reason, and the rhythm of
   the example sentences live only in the deck itself. A lesson written from the blueprint alone
   comes out correctly shaped and lifeless.

Regenerate the briefs after any TOC change:
`python3 korean/tools/shard_toc.py korean/tracks/<track>`

**Before trusting a local render, check the runtime you rendered against.**
`python3 korean/tools/check_runtime_drift.py` compares `runtime/` with the CDN tag
production actually serves. Deployed decks load that tag, not this folder — so when
the two differ, the page you approved at 480px is not the page the learner gets, and
nothing errors to tell you. A component that only exists locally just renders unstyled.

## Getting a lesson to production

This folder is the authoring tree; `re-speak/podo-curriculum` is what deploys. **Keep
writing relative `../../runtime/…` refs** — that is the input format the production
tools expect. `sync-from-authoring.py` rewrites them to `shared/`, and
`repoint-shared.py` then pins them to the CDN tag declared in one place
(`curriculum.yaml` → `spec.sharedRuntime`). Writing a CDN URL here by hand would
hand-pin a version in every file and break local verification.

**A track is not a course.** 2-core-patterns is 116 lessons; a deployable course is one
`classLevel` with weeks 1..N and no gaps. `tools/plan_courses.py` cuts the track against
its TOC into ~12-lesson courses on unit boundaries, and writes `course.yaml` /
`lesson.yaml` that already validate against podo-curriculum's `schemas/` — so the sync is
a copy, not a translation. Decks live at
`tracks/<track>/courses/<course>/lessons/<slug>/lesson.html`.

Lesson slugs are `NN-english-words` (`07-daily-routine`) because the schema demands it, and
the deck's `podo:lesson-id` must equal its directory name. `lesson.yaml` is written only for
lessons that have a deck; the rest of the plan lives as comments in `course.yaml`.

Over there, in order: `sync-from-authoring.py` → `import-track-lessons.py <track>`
→ `repoint-shared.py` → `validate.py`. `podo:lesson-id` and `podo:title-{ko,en,ja}` are
load-bearing — `new_lesson.py` writes them and they must not be removed.

**Never edit `shared/` or `sandbox/` in podo-curriculum.** Both are sync destinations
and get replaced wholesale; a fix made there disappears on the next sync with no error.
Fix it here instead.

## Interactive lessons

Anything the learner taps, types, or drags — and anything that has to stay in step with the
tutor's screen — goes through lemonboard's `data-sync` contract.

**Reuse an existing activity and the contract comes with it** — copy the markup from
[`AUTHORING.md`](./AUTHORING.md) or from a live deck in `trial/lessons/`, `data-sync`
attributes and all, and there is nothing further to read. This is the normal case, and it is
why building a lesson out of the existing component vocabulary is cheaper *and* safer than
inventing markup.

**Read [`interaction-protocol.md`](./interaction-protocol.md) only when
you are inventing a new interaction type** — a new `data-sync-kind`, a new way of sharing state,
anything not already in the vocabulary. Getting it wrong there fails silently: the activity
works on your screen and never reaches the other person. Packaging a deck into an uploadable
zip is not this repo's job — `podo-curriculum` does it in `tools/build.py`.

Two rules that catch most mistakes: an element is shared **only** if it has a `data-sync-id`
(no id = private), and verdicts are never shared — send the choice and let each side derive
`correct`/`wrong` locally. Note that this does *not* hide the answer key: both people load the
same document, so anything in the markup is already on the learner's screen.

## Layout

- **`tracks/`** — the learner-facing curriculum, in learning order: `1-hangul` · `2-core-patterns` ·
  `3-contextual-korean` · `4-freetalking` (pronunciation joins as `5-pronunciation` once it has content).
  Each track holds `table-of-contents.md`, the generated `toc/` briefs, `lesson-blueprint.md`,
  and its lesson HTML. Nothing else — retired drafts live outside this folder, see **Archive**.

  **The trial deck is the source of truth, not the sample.** `trial/lessons/trial-N-*.html` is
  the deck that gets maintained; each track's `sample-lesson.html` is that deck **with the sales
  pages cut** — cover, greeting, trial-intro, todays-result and closing come off, everything
  pedagogical stays. So the samples are full paged decks, not scrolling documents: same
  skeleton, same stylesheets, same scripts, and the shared art still comes from
  `../../trial/assets/`. When a trial lesson changes, re-cut its sample rather than editing both
  by hand — and when the two disagree, **the trial deck wins.** The first surviving page needs
  its own `data-act`; the act name used to come from the cover's `.brand-title`.
- **`trial/`** — sales trial material, not a learning track. `full-trials/` holds the four complete
  decks (`trial-1..4`), `lessons/` holds the standalone lesson decks cut from them
  (`trial-1-hangul-short.html`, `trial-2-patterns-short.html`, `trial-3-contextual-short.html`),
  and `reports/` holds the trial report deck. Plus shared `assets/` (art, mouth, characters).

  **A deck is markup plus shared scripts — no per-deck CSS or JS.** Load them in this
  order: `activities` → `pager` → `script-lines` → `spotlight` → `tutor-notes`
  → `highlight` → `stamp`. The order is load-bearing (see the comments at each tag).
  A hangul deck adds `hangul-activities`, a freetalk deck adds `freetalk-activities`,
  both directly after `activities`. A deck ships **no inline script and no inline CSS**
  of its own — if you are writing either, the thing you need probably belongs in a
  shared module or in `trial.css`.

  **The report's recommendation is a spec, not a guess.** How the trial report gets to
  「N개월 · 이 코스들」 — the lesson counts it draws on, the level ladder, the duration
  formula and its **5-month floor** (a sales policy, not a calculation), and how level ×
  goal × reason pick the courses — lives in [`trial/plan-logic.md`](./trial/plan-logic.md).
  The code for all of it is `runtime/js/report.js`; when the two disagree, the doc wins.
  Read it before touching any number in that file.

  **Read [`AUTHORING.md`](./AUTHORING.md) before building a new deck.** It is
  the component vocabulary — page types, every activity's markup, the colour and spacing
  tokens, and the file skeleton. Reach for an existing component before inventing one.
- **`runtime/`** — everything a deck loads at run time: `css/` (the design system plus each
  track's sheet) and `js/` (the shared modules). This folder is the publish set — it is what
  gets mirrored to a public repo and served from a CDN, so nothing private may live in it.
  See [`runtime/README.md`](./runtime/README.md).
- **`interaction-protocol.md`** — the `data-sync` contract. Documentation only; the code
  decks load lives in `runtime/`. Packaging a deck for upload is not done here at all —
  `podo-curriculum` owns it (`tools/build.py`), because the zip is a deploy artefact and
  building one by hand is how a stale deck reaches a classroom.
- **`tools/`** — authoring scripts. `shard_toc.py` (TOC → per-lesson briefs), `new_lesson.py`
  (deck skeleton) and `build_catalog.py` (five TOCs → `catalog.html`). All three derive their
  output from files that already exist, so none holds a second copy of anything.
- **`references/`** — source textbook scans (internal reference only).
- **Archive — deliberately not here.** Retired drafts, design variations and capture files live in
  `_archive/` at the *repo* root, under their original paths. They are kept for history and are
  **not part of the read path**: never cite one as precedent, never copy markup out of one, and
  don't search them when looking for how something is done. If a grep turns up an `_archive/`
  hit, the live answer is elsewhere in `korean/`.
- `index.html` / `viewer.html` at the root are the navigation; `CLAUDE.md` / `AGENTS.md` stay at
  the root so they auto-load.
- **`catalog.html` + `catalog/` are generated — never hand-edit them.** `catalog.html` is the
  gateway (hero, five track cards, level ladder); `catalog/<track>.html` is that track's full
  contents — every 과, what it teaches, and the pattern marked inside its own example sentence.
  All six pages are built from the five `table-of-contents.md` files by `tools/build_catalog.py`,
  out of `tools/gateway_template.html` and `tools/track_template.html`. They hold no facts of
  their own, so a wrong number there is a wrong number in a TOC. Re-run
  `python3 korean/tools/build_catalog.py` after any TOC change, alongside `shard_toc.py`.

  **The colour rules are the point, not decoration.** Each track owns one accent, validated as a
  categorical palette (`dataviz` skill's `validate_palette.js`), and that accent appears only in
  the top three levels of the hierarchy — track title, band heading, unit chip. Below that
  everything is ink and hairlines, because the one saturated thing inside an open 과 has to be
  the peach `mark` on the taught pattern (`--pat-mark`/`--pat-ink`, lifted from the decks'
  `--ending-*`). Paint the fourth level too and that mark stops reading.
