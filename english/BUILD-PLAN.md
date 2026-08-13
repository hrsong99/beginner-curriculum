# English Curriculum — Build Plan

**Status:** infrastructure ready · native catalog review in progress · further decks on hold
**Written:** 2026-08-12
**Last reconciled:** 2026-08-13

---

## Where we are

| | Korean | English |
|---|---:|---:|
| Tracks | 5 | 4 (pronunciation plan-only) |
| Planned items | 316 written decks | 315 TOC items |
| Process / authoring docs | mature | working contract + three production blueprints |
| Build tools | 8 + tests | parser, briefs, grammar map, catalog, checker, skeleton + tests |
| Written lesson decks | 316 | **1 approved Core pilot** |
| Catalog / review surface | yes | 303-item review catalog; native review active |

English now has the production spine that was missing when this plan was written: guarded
authoring, an approved Core pilot, strict TOC parsing, generated briefs and grammar map, a deck
checker and a review catalog. The main uncertainty has moved from **can this be built?** to **which
reviewed patterns survive, and how does the product identify the resulting courses?**

The plan below is ordered so that **each phase unblocks the next**, and so that the cheapest
work that removes the most uncertainty happens first.

---

## Priority summary

| Phase | What | Blocks | Size | Who |
|---|---|---|---|---|
| **0** | Decisions only the owner can make | everything | — | human |
| **1** | Make `english/` a working folder | all authoring | S | agent |
| **2** | Blueprint + one hand-authored pilot deck | all batches | M | agent + human gate |
| **3** | TOC repair | briefs, decks | M | agent, parallelizable |
| **4** | Tooling | batch production | M | agent |
| **5** | Track rebuilds & new tracks | scale | XL | agent batch |
| **6** | Native / corpus / learner validation | calling it CEFR-aligned | L | human + agent |
| **7** | Product & deploy identity | shipping to app | M | agent + backend |

Phases 1–5 are substantially complete. Phase 6 native review is active. The owner has explicitly
held further deck production until that feedback returns; Phase 7 remains gated on D4–D5.

---

## Phase 0 · Decisions only a human can make

These are not work items; they are answers. Every one of them has downstream files that cannot
be written until the answer exists.

### Decided 2026-08-12

- [x] **D1 — The learner is a Japanese speaker.** Same audience as the Korean curriculum, different
  target language. *Consequences:* the JP-facing half of the shared `runtime/` (Japanese tutor notes,
  kana anchoring, the よみがな switch machinery) is directly reusable; the pronunciation track
  becomes a Japanese-L1 contrastive list; `GT_CLASS_COURSE.COUNTRY_CODE` is the column that will
  eventually separate this from any English-for-Koreans line, exactly as `korean/AGENTS.md`
  anticipated.
- [x] **D2 — Support text is Japanese throughout.** Every gloss, hint, instruction and translated
  tutor line is Japanese; English is reserved for the target language itself. Same contract as
  `korean/AGENTS.md` line 3, with Korean swapped for English.
- [x] **D3 — No katakana readings. Ever. At any level.** This is the sharpest single consequence of
  D1 and it *inverts* the Korean rule rather than copying it.

  Korean's `.yomi` exists because hangul is an unfamiliar script and a beginner genuinely cannot
  decode it; the reading is a crutch that the よみがな switch removes once decoding lands. English
  has no such problem — a Japanese learner already reads the Latin alphabet on day one.

  Worse, a katakana reading over an English word would **teach the single most damaging
  Japanese-L1 pronunciation error in the language**: mora-timed katakana English. Writing
  `マクドナルド` over *McDonald's* does not scaffold the word, it installs the wrong one. This is
  the same reasoning that makes `1-hangul` carry no `.yomi` at all — printing the answer over the
  thing being learned cancels the learning — but here it applies to **every English deck at every
  level**, not just one track.

  *Consequences:* English decks do not load `yomi.js` and carry no `.yomi`. If a pronunciation
  scaffold is ever needed it must be IPA or a stress/rhythm mark, never kana, and it needs its own
  decision. Kana remains fine where it is *not* pronouncing English: a Japanese gloss, a hint chip,
  a tutor note.

### Still open

- [ ] **D3b — Is there any pronunciation scaffold at all?** Given D3, does an English deck mark
  stress, linking or rhythm on model lines — and with what? Deferred until the pilot deck shows
  whether a model line needs one.
- [ ] **D4 — Level ladder and its mapping.** English uses CEFR (Pre-A1 → C1). The product's
  trial report (`korean/trial/plan-logic.md`) runs on 왕초급/초급/초중급/중급/고급. No mapping
  exists between them. *Downstream:* trial report, catalog, course recommendation logic.
- [ ] **D5 — Product identity numbers.** `classLevel` band, `LANG_TYPE`, course-code scheme.
  `korean/AGENTS.md` reserves the shape ("stay `BASIC`, use unused `classLevel` values, do not
  create `BASIC_V3`") but assigns nothing for English. *Downstream:* `course.yaml`, sync, catalog.
- [x] **D6 — DECIDED 2026-08-13. Core runs to C1; pronunciation gets a plan, not decks.**
  Core extended Pre-A1 → C1 (122 lessons), matching Korean's reach. A pronunciation track exists as
  `tracks/4-pronunciation/table-of-contents.md` in **planning state only** — no decks are to be
  written until Core is further along, exactly the state `korean/tracks/5-pronunciation` has sat in
  for the mirror-image learner. No decoding track: the learner already reads Latin script.
- [x] **D7 — Contextual English is rebuilt as shows with a cast and episodes.** Korean's answer,
  adopted. The existing 48 situation lessons stay as the underlying inventory of what must be
  covered; the courses on top of them get a work title, a named cast, a relationship state, an
  episode arc and a `場面:` line per lesson. *Downstream:* T5.1 grows; T3.6–T3.8 fold into it.

---

## Phase 1 · Make `english/` a working folder — **DONE 2026-08-12**

- [x] **T1.1** — `english/AGENTS.md`. Audience, the katakana rule, colour meanings, audio-only,
  the pilot gate, the inputs order, the *English deltas* table, layout, and an honest
  "production is not yet possible" section.
- [x] **T1.2** — `english/CLAUDE.md` — one line, `@./AGENTS.md`, matching Korean.
- [x] **T1.3** — **Resolved by not writing one.** `korean/ux-philosophy.md` is language-neutral in
  substance and is now cited as the shared contract for both folders; the places where English
  genuinely differs are a seven-row *English deltas* table in `AGENTS.md`. A second copy would
  have drifted, and the Korean original is the one that gets maintained.
- [x] **T1.4** — `english/LESSON-CREATION-WORKFLOW.md`. Every step whose tool does not exist yet is
  marked **[not built]** and says what to do instead, so a writer cannot mistake a missing tool for
  a step to improvise past.
- [x] **T1.5** — `english/tracks/_conventions.md`, seeded with empty ledgers and the reasoning
  behind each, including Korean's compare-situations-not-labels warning and the
  don't-fix-shared-runtime rule.
- [x] **T1.6** — Root `index.html` English row updated.
- [x] **T1.7** — `README.md` now states the learner in its first line.

---

## Phase 2 · Blueprint + pilot deck — **size M, the highest-leverage single item**

Zero HTML exists in `english/`. Until one deck exists, the conventions file has nothing to record,
the tooling has nothing to generate against, and no batch can be assigned. The Korean workflow is
explicit that the deck — not the blueprint — carries the tutor's voice, the reason a wrong answer
is wrong, and the rhythm of the examples.

- [x] **T2.1 — DONE 2026-08-12. The shared layer was hoisted to the repo root.**

  Three things moved out of `korean/` because they are not Korean:

  | Moved | To | Why |
  | --- | --- | --- |
  | `korean/runtime/` | `runtime/` | both curricula load the same CSS and JS |
  | `korean/ux-philosophy.md` | `ux-philosophy.md` | the shared page contract, cited by both `AGENTS.md` files |
  | `korean/viewer.html` | `viewer.html` | generic markdown viewer; it had to follow, see below |

  **`trial/assets/` deliberately did not move.** It is Korean sales art plus hangul-specific mouth
  illustrations. The consequence is that a deck's `../` count now differs by one between the two
  targets — seven for the runtime, six for the assets — which `new_lesson.py` now handles and a
  hand-edited path will not.

  What it took: **3,268 refs across 331 decks** rewritten and every one verified to resolve, plus
  five couplings that would each have failed silently —
  - the `Dockerfile` copies `index.html`, `english/`, `korean/`, `_archive/` and nothing else, so a
    root `runtime/` would not have been served at all and the entire site would render unstyled;
  - `viewer.html` rejects any `?doc=` containing `..` as a path-traversal guard, so leaving it in
    `korean/` would have made the hoisted `ux-philosophy.md` unreachable from the nav — hence the
    third move, and `korean/index.html`'s links are now `../viewer.html?doc=korean/<path>`;
  - `check_runtime_drift.py` hard-coded `RUNTIME = KOREAN / "runtime"`;
  - `new_lesson.py`'s `redepth()` applied **one** depth to both `runtime/` and `trial/`, which now
    sit at different levels — it would have 404'd one of them on every generated deck;
  - `AUTHORING.md`'s file-skeleton example, which is what a deck author copies from.

  `_archive/` (22 files) was left untouched by design — it is explicitly not part of the read path.

  **Still needs coordination:** `sync-from-authoring.py` and `repoint-shared.py` live in
  `re-speak/podo-curriculum`, not in this repo, and they expect `korean/runtime/`. **The production
  sync will break until they are updated.** That change is not in this workspace and has to be made
  there before the next deploy.
- [x] **T2.2** — `tracks/1-core-patterns/lesson-blueprint.md`. Done. 26–28 page skeleton, the
  receptive → productive ladder marked unchangeable, the counting rules mirrored in (four questions,
  four chips, one blank one question), and two English-specific findings recorded:
  - `words-you-know` does a second job here — katakana loanwords are real prior knowledge and worth
    using for motivation, but the page must not become a pronunciation drill or print kana beside
    the English.
  - **English will hit Korean's three-branch rule-diagram wall**, and sooner: `do/does/did`,
    `a/an/the`, `-s/-es/-ies` are all three-case rules and `.batchim` is single-column. The
    instruction is Korean's — ship the honest two-box split, keep the third case out of
    learner-produced language, and report it rather than compressing into a misleading tile.
- [x] **T2.3 — DONE.** Core 20 authored end to end at
  `tracks/1-core-patterns/courses/core-first-exchanges-2/lessons/20-asking-for-help/lesson.html`
  — 25 pages, no inline CSS or JS, no `yomi.js`, zero `.yomi` elements.

  The lesson's form rule turned out to be the best thing in it: **`help me with` + a thing vs
  `help me` + an action.** Japanese 「手伝う」 does not make that split, so `help me with carry it`
  and `help me to carry it` are both live L1 errors — and it is an honest two-brancher, which
  dodges the three-case wall. It is taught once from the asking side and once from the answering
  side. The course code `core-first-exchanges-2` is **provisional** until `plan_courses.py` exists.
- [x] **T2.4 — DONE.** Static checks pass (10 local refs resolve, lesson-id equals its directory,
  25/25 unique page ids, 40/40 unique sync ids). Rendered in-browser: both stylesheets applied
  (189 + 1320 rules), 7 scripts loaded, pager live, `.pattern-meaning` and `.nuance-compare` both
  styled. The page-tail probe at 800px reports **no non-`.section` page clipping**.

  One defect found and fixed by looking at it, which is the argument for the rule: the rule diagram
  shipped as bare `.batchim`, which renders **violet — the Korean 조사 colour**, a category English
  does not have. Now `batchim ending-rule`, so orange means "the taught frame" on every page.
- [x] **T2.5 — APPROVED 2026-08-13.** The pilot is the canonical deck for `1-core-patterns`.
- [ ] **T2.6 — ON HOLD by owner decision.** After native review, author three structurally
  different Core lessons (a narrative one, a comparison one and a B1+ one) and review them together
  before any wider batch. The pilot is approved, but no further decks are written while the review
  is open. Correct call: Korean's precedent says a chunk of Part 2 will not survive native review,
  and a deck written from a pattern that gets cut is a deck rewritten.
- [x] ~~**T2.5 (old)** — STOP. Explicit owner approval.~~ Structural checks do not approve a pilot. If
  rejected, rewrite and re-review; do not use a rejected pilot as a template.
- [x] **T2.7 — DONE 2026-08-13.** Contextual and Freetalking now have production blueprints.
  Contextual gives `Understand` a receptive-only lane, defines marked-chunk treatment and owns the
  teaser/continuity contract. Freetalking defines four format-specific model pages, the two load
  versions, the eight-question ladder and the correction contract. Neither creates or approves a
  track pilot.

---

## Phase 3 · TOC repair — **size M, parallelizable with 1–2**

### 3a · Core (122 lessons) — correctness first

- [x] **T3.1 — DONE 2026-08-13.** The 12 Core and 2 Contextual frames that failed the pattern
  standard were rewritten; defensible open frames were retained with reasons.
- [x] **T3.2 — DONE 2026-08-13.** The past-deduction model/frame mismatch was corrected in the
  rebuilt spine (now Core 72).
- [~] **T3.3 — PART 1 DONE; PART 2 WAITS ON REVIEW.** Core 1–70 have learner-facing `Grammar:`
  support. Core 71–122 have none; the generated grammar map and every affected brief expose those
  52 gaps instead of inventing explanations for patterns that native review may demote.
- [~] **T3.4 — 180/182 DONE.** All 122 Core lessons and 58/60 Contextual episodes carry supporting
  expressions. CTX-54 and CTX-58 remain missing; fill them together with accepted catalog feedback
  rather than changing the active review surface underneath the reviewer.
- [x] **T3.5 — DONE 2026-08-13.** All 22 Core units carry framing and checkpoint/review summaries.

### 3b · Contextual (60 episodes)

- [x] **T3.6 — DONE 2026-08-13.** All 60 episodes carry a can-do.
- [x] **T3.7 — DONE 2026-08-13.** All 60 episodes carry a who/where/what scene.
- [x] **T3.8 — DONE 2026-08-13.** Every episode has two learner lines and two partner reactions;
  the strict parser tests the contract, including non-Latin dialogue quotes.

### 3c · Cross-cutting

- [x] **T3.9 — DONE 2026-08-13.** Authored decks now declare new, recycled, assumed-known and
  receptive-only vocabulary in machine-readable metadata. `build_running_lexicon.py` generates the
  working ledger from those declarations; `check_deck.py` rejects undeclared hint-chip vocabulary,
  copied-shell `todo` status and Core/Contextual loads above eight unless a written waiver surfaces
  the exception. The approved Core 20 pilot starts the ledger at five new content words.
- [x] **T3.10 — DONE 2026-08-13.** Contextual defines `Understand` as an optional receptive-only
  field and the blueprint gives it a dedicated recognition page. Seven episodes currently need it;
  absence elsewhere means the episode has no extra receptive target, not a missing required field.
- [x] **T3.11 — DONE 2026-08-13.** Generated briefs now carry the negative sequence constraint.
  Core lists exact already-learned/not-yet ranges and nearby boundaries; Contextual names the
  productive floor and chunk exception; Freetalking is explicitly retrieval-only. These are
  regenerated from the TOCs rather than maintained as a second curriculum.

---

## Phase 4 · Tooling — **size M**

Korean's eight tools all derive their output from files that already exist, so none holds a second
copy of anything. Same rule here.

- [x] **T4.1 — DONE 2026-08-13.** `tools/track_parsers.py` strictly parses all four TOCs into one
  shared shape: 122 Core lessons, 60 Contextual episodes, 121 Freetalking topics and 12 planned
  pronunciation lessons. It raises on missing or discontinuous source structure instead of
  silently dropping items. Regression tests cover counts, two-pattern/reaction contracts, Core
  reference ranges, opening/ladder fields and pronunciation's planning-only state.
- [x] **T4.2 — DONE 2026-08-13.** `build_lesson_briefs.py` generates 315 stable-id briefs plus
  indexes. Core carries explicit already-learned/not-yet ranges; Contextual carries floor, Core
  ownership and chunk rules; Freetalking carries retrieval-only constraints. No course-code scheme
  is invented while D5 remains open.
- [x] **T4.3 — DONE 2026-08-13.** `new_lesson.py` lifts only the shell from an approved canonical
  English deck, removes its pages and identity comments, retargets metadata and paths, verifies
  refs/no-yomi, and refuses overwrite. Non-Core tracks remain gated on their own approved pilots.
- [ ] **T4.4** — `plan_courses.py` — cut tracks into deployable courses on unit boundaries;
  emit `course.yaml` / `lesson.yaml` validating against podo-curriculum's schemas.
- [x] **T4.5 / T7.3 — DONE 2026-08-13.** `english/tools/build_catalog.py` + `catalog_template.html`
  generate `english/catalog.html` from the three TOCs — 303 items, every one with a stable id
  (`CORE-31`, `CTX-12`, `FT-45`) so review feedback is unambiguous. Model sentences are set large
  because they are what a native reviewer judges; frames, Core links and JP notes are context.
  Holds no facts of its own; re-run after any TOC change and never hand-edit.
- [x] **T4.6a — DONE, ahead of the rest of Phase 4.** `english/tools/check_deck.py` — the static
  deck checker. Built early because the pilot shipped two defects that pass markup review and leave
  nothing in the console, and a checklist item only reaches whoever was told to read the checklist.
  Covers metadata, id/directory match, ref resolution, duplicate ids, inline CSS/JS, the English
  no-katakana rule, **tutor-script sentence parity** and **reorder chunk consistency**. Exits
  non-zero, so it can gate a batch.

  Run against the Korean tree it finds **94 pre-existing errors in 318 decks** — 39 parity, 54
  mixed-chip-count pages, 1 deck shipping inline `<style>`. The chip figure independently confirms
  the problem Korean's own `_conventions.md` records ("348문장 중 51문장"), which is still open.
- [x] **T4.6b — CORE GENERATORS COVERED 2026-08-13.** Eighteen regression tests now cover all
  four parsers, canonical-shell extraction/retargeting/path depth, exact generated grammar-map and
  315-brief freshness, catalog-review intake including stale/duplicate/unknown feedback, and the
  vocabulary ownership/cap/ledger contract. New shells clear copied vocabulary and stay `todo`.
  Future `plan_courses.py` and authored-deck packet tooling add their own tests when built.
- [x] **T3.12 — DONE 2026-08-13.** `build_grammar_map.py` regenerates the 122-row function,
  two-pattern, grammar, band, sequence and JP-risk map from the Core TOC. It surfaced rather than
  papered over the remaining curriculum gap: Core 71–122 have no learner-facing `Grammar:` field.
  Those 52 rows are visibly marked and remain catalog/native-review-dependent authorship.
- [x] **T3.13 — DONE 2026-08-13.** All Core references in Contextual (71) and Freetalking (44) re-derived against the 122-lesson spine and mechanically verified in range. Stale banners removed from both. 72 `Core N` references across
  the two tracks now point at the wrong lessons. Folded into the D7 rebuild, which rewrites those
  courses anyway.

---

## Phase 5 · Track rebuilds and new tracks — **size XL**

- [x] **T5.1 — DONE 2026-08-13.** Contextual rebuilt as 4 shows · 10 seasons · 60 episodes, each with a cast, an arc, a `場面:` line and a partner reaction per learner line. Also clears **T3.13** — all 71 Core references re-derived against the 122-lesson spine and verified in range.
- [x] ~~**T5.1 (old)** — Contextual identity (gated on D7).~~ If "show": season bibles, named casts,
  relationship state, episode arcs, a scenes-spent ledger. Korean's stated failure mode is the
  reverse direction — teaching grammar and sprinkling in themed vocabulary.
- [x] **T5.2 — DONE 2026-08-13, then rebuilt again against the full Korean track.** Freetalking is
  now **11 themes · 121 topics × 2 levels**, deliberately mirroring `korean/tracks/4-freetalking`
  so the two curricula share one topic inventory. **103 of Korean's 105 topics ported**; the two
  that did not are named with reasons. 18 originals written here are proposed back in
  [`tracks/3-freetalking/proposals-to-korean.md`](./tracks/3-freetalking/proposals-to-korean.md).
  - Replace the essay-prompt topics. Korean's TOC diagnoses this exactly: 「~란 무엇인가」 titles
    look deep in a contents list but produce no answer within three seconds even in the L1.
    English ships *"What does success mean to you?"* as topic #1, plus *"What makes a job
    meaningful?"* and *"Is convenience worth the environmental cost?"*. Rule: experience over opinion.
  - Per-topic question ladders (one generic 6-rung ladder currently serves all 24).
  - Two versions of each topic (accessible / full), same theme and skeleton, differing only in
    the language load — not two separate idea lists.
  - Session page skeleton.
- [x] **T5.3 — PLANNED, DECKS DEFERRED 2026-08-13.** The 12-lesson Japanese-L1 contrastive
  pronunciation TOC is written and parsed. Per D6, it remains planning-only until Core is further
  along; D3b still controls any scaffold choice.
- [x] **T5.4 — NOT APPLICABLE by D6.** There is no Hangul-style decoding track: the learner already
  reads Latin script. Sound/spelling and connected-speech needs belong in pronunciation planning.
- [x] **T5.5 — WRITTEN, UNDER REVIEW 2026-08-13.** Core Part 2 extends B1+→C1 through lesson 122.
  It is explicitly unvalidated and expected to shrink under native/corpus review.

---

## Phase 6 · Validation — **size L, cannot be skipped**

Korean's native review knocked **28 of 264 patterns** out of the pattern slot as things people do
not actually say. Its TOC names the cause precisely: the parts built *from scenes* survived; the
part built *from a grammar list* did not (28 of 120 in Part 2). English's B1+ bridge and grammar
coverage map are exactly that shape.

- [~] **T6.1 — IN PROGRESS, owner reviewing.** Surface is `english/catalog.html`. Rejected patterns
  get **demoted to the expressions line, not deleted** — the learner still meets them but is no
  longer asked to produce them.
- [ ] **T6.2** — Corpus/naturalness check on model sentences (Step 6 of the proposed method).
- [ ] **T6.3** — Row-level source audit: Core Inventory item + EGP form-and-meaning + CEFR
  descriptor for every grammar-map row. `proposed-authoritative-build-method.md` lists this as
  not done; until it is, `B1+` stays a working band, not a claim.
- [~] **T6.4 — CATALOG INTAKE DONE; DECK PACKETS DEFERRED.** `PROOFREADING-WORKFLOW.md` separates
  catalog, lesson and rendered review. `parse_catalog_review.py` validates copied feedback against
  current stable ids, titles and first-line snapshots and emits structured JSON without editing
  TOCs. Build the one-way authored-HTML packet projection after the representative three-Core-deck
  gate; building it from one pilot would encode one lesson's structure as universal.
- [ ] **T6.5** — Learner pilot: two lessons per level, recorded task performance, delayed retrieval
  at one week, transfer check.

---

## Phase 7 · Product and deploy — **size M**

- [ ] **T7.1** — Assign the `classLevel` band and per-course decimal slots (gated on D5).
- [ ] **T7.2** — Course codes; `course.yaml` / `lesson.yaml` generation.
- [x] **T7.3 — DONE 2026-08-13.** The generated 303-item catalog is the active native-review
  surface. Product publication remains separate from the review artifact.
- [ ] **T7.4** — Trial material: trial decks per track, short cuts, the report deck, and an English
  `plan-logic.md` (level ladder, duration formula, the 5-month sales floor). This is the sales
  front door and currently does not exist in any form.
- [ ] **T7.5** — Sync path into `re-speak/podo-curriculum`; confirm the English tree survives
  `sync-from-authoring.py` → `import-track-lessons.py` → `repoint-shared.py` → `validate.py`.

---

## Sequencing note

The next critical path is now: **native feedback → TOC decisions → regenerate derived artifacts →
three varied Core lessons → batch gate.** In parallel, D4–D5 unblock course planning and product
identity. Do not create lesson volume merely because the infrastructure can now stamp shells.

Phase 1 is a few hours and removes a live risk (agents working in an unguarded folder). Do it
alongside.
