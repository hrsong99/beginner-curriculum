# English Curriculum — Build Plan

**Status:** Phase 0 decided · Phase 1 in progress
**Written:** 2026-08-12
**Basis:** full read-through of `english/` (11 files) against `korean/` (316 written decks, 5 tracks, 8 build tools, 7 process docs)

---

## Where we are

| | Korean | English |
|---|---:|---:|
| Tracks | 5 | 3 |
| TOC lines | 3,650 | 953 |
| Process / authoring docs | 7 (1,464 lines) | 0 |
| Build tools | 8 + tests | 0 |
| Written lesson decks | 316 | **0** |
| Trial decks · catalog · review pipeline | yes | none |

English has a **curriculum specification**. Korean has a **production system**. The spec is good
— `curriculum-source-hierarchy.md` and `proposed-authoritative-build-method.md` are more rigorous
than anything on the Korean side and should eventually be back-ported. But almost everything
between "we know what to teach" and "a lesson exists" is missing.

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

Phases 1–3 can run concurrently. Phase 2 has a **hard stop gate** before any batch work.

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
- [ ] **D4 — Level ladder and its mapping.** English uses CEFR (Pre-A1 → B1+). The product's
  trial report (`korean/trial/plan-logic.md`) runs on 왕초급/초급/초중급/중급/고급. No mapping
  exists between them. *Downstream:* trial report, catalog, course recommendation logic.
- [ ] **D5 — Product identity numbers.** `classLevel` band, `LANG_TYPE`, course-code scheme.
  `korean/AGENTS.md` reserves the shape ("stay `BASIC`, use unused `classLevel` values, do not
  create `BASIC_V3`") but assigns nothing for English. *Downstream:* `course.yaml`, sync, catalog.
- [ ] **D6 — Track scope.** Does English get a decoding track, a pronunciation track, a Part 2
  (B2/C1)? *Downstream:* Phase 5 size. Note D1 makes the pronunciation track's contents knowable
  today — the Japanese-L1 collision list for English is closed and short.
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
- [x] **T2.3 — DONE.** Core 22 authored end to end at
  `tracks/1-core-patterns/courses/core-first-exchanges-2/lessons/22-asking-for-help/lesson.html`
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
- [ ] **T2.5** — **STOP. Explicit owner approval.** Structural checks do not approve a pilot. If
  rejected, rewrite and re-review; do not use a rejected pilot as a template.
- [ ] **T2.6** — After approval: three structurally different lessons (e.g. a narrative one, a
  comparison one, a B1+ one), reviewed together, before any wider batch.
- [ ] **T2.7** — Blueprints for tracks 2 and 3, written after the Core pilot holds up.

---

## Phase 3 · TOC repair — **size M, parallelizable with 1–2**

### 3a · Core (72 lessons) — correctness first

- [ ] **T3.1** — Fix six frames that violate the curriculum's own pattern standard.
  `teaching-philosophy.md` §4 rejects `We ___ed ___ last night` as "a past-tense formula, not a
  retrievable frame"; `lesson-template.md` bans grammar formulas as patterns. Currently shipping:
  - L59 `My ___ was ___ yesterday.` — literally the rejected shape
  - L42 `I'm ___ed because it's ___ing.` — two inflected slots, almost no fixed language
  - L30 `I was ___ing when you ___ed.`
  - L41 `It's the ___est option.` · L40 `This one is ___er than that one.`
- [ ] **T3.2** — L65: model line says "The traffic must have been bad," frame reads `It must have ___`.
- [ ] **T3.3** — Add the learner-facing grammar line to all 72 entries. `teaching-philosophy.md` §3
  promises it exists; `grammar-coverage-map.md` is explicitly author-only; so today it exists nowhere.
- [ ] **T3.4** — Normalize supporting expressions. Core carries them on ~10 of 72 lessons;
  Contextual carries 2 on every lesson. One standard, applied to both.
- [ ] **T3.5** — Unit framing lines (what this unit does, where the load is) and checkpoint form
  summaries.

### 3b · Contextual (48 lessons)

- [ ] **T3.6** — Add a can-do line to all 48. Core has one per lesson; Contextual has none.
- [ ] **T3.7** — Add a scene line (who · where · what's happening) per lesson. Without it the deck
  writer invents the situation on the spot.
- [ ] **T3.8** — Add partner reactions to model lines. Korean's finding: two lines with no reply
  are examples, not a script.

### 3c · Cross-cutting

- [ ] **T3.9** — Build the **running lexicon**. `lesson-template.md` caps new content words at
  6–8 per lesson; there is no word inventory anywhere, so the rule is unenforceable today.
- [ ] **T3.10** — Add a receptive-only tier (Korean's `이해`) for language the learner must
  recognize but not produce — announcements, clerk speech, signage.
- [ ] **T3.11** — Define the per-lesson **"not yet" list**. The `Depends on` column is a forward
  dependency; the negative constraint is what actually stops a writer using untaught grammar.
  This should be *generated* from the TOC in Phase 4, not hand-maintained.

---

## Phase 4 · Tooling — **size M**

Korean's eight tools all derive their output from files that already exist, so none holds a second
copy of anything. Same rule here.

- [ ] **T4.1** — English TOC parser (`tools/track_parsers.py` equivalent). Must represent
  can-do, patterns, expressions, grammar line, prerequisites and scene without guessing.
- [ ] **T4.2** — `build_lesson_briefs.py` — course-scoped briefs, including the generated
  "already learned / not yet" ledger (T3.11).
- [ ] **T4.3** — `new_lesson.py` — deck skeleton, so the meta block, stylesheet links and
  load-order-bearing script tags are never retyped.
- [ ] **T4.4** — `plan_courses.py` — cut tracks into deployable courses on unit boundaries;
  emit `course.yaml` / `lesson.yaml` validating against podo-curriculum's schemas.
- [ ] **T4.5** — `build_catalog.py` — English catalog gateway + per-track pages.
- [x] **T4.6a — DONE, ahead of the rest of Phase 4.** `english/tools/check_deck.py` — the static
  deck checker. Built early because the pilot shipped two defects that pass markup review and leave
  nothing in the console, and a checklist item only reaches whoever was told to read the checklist.
  Covers metadata, id/directory match, ref resolution, duplicate ids, inline CSS/JS, the English
  no-katakana rule, **tutor-script sentence parity** and **reorder chunk consistency**. Exits
  non-zero, so it can gate a batch.

  Run against the Korean tree it finds **94 pre-existing errors in 318 decks** — 39 parity, 54
  mixed-chip-count pages, 1 deck shipping inline `<style>`. The chip figure independently confirms
  the problem Korean's own `_conventions.md` records ("348문장 중 51문장"), which is still open.
- [ ] **T4.6b** — Tests for the tools, matching `test_track_parsers.py`.

---

## Phase 5 · Track rebuilds and new tracks — **size XL**

- [ ] **T5.1** — **Contextual identity** (gated on D7). If "show": season bibles, named casts,
  relationship state, episode arcs, a scenes-spent ledger. Korean's stated failure mode is the
  reverse direction — teaching grammar and sprinkling in themed vocabulary.
- [ ] **T5.2** — **Freetalking repair.** Currently 24 topics vs Korean's 105 × 2 levels = 210.
  - Replace the essay-prompt topics. Korean's TOC diagnoses this exactly: 「~란 무엇인가」 titles
    look deep in a contents list but produce no answer within three seconds even in the L1.
    English ships *"What does success mean to you?"* as topic #1, plus *"What makes a job
    meaningful?"* and *"Is convenience worth the environmental cost?"*. Rule: experience over opinion.
  - Per-topic question ladders (one generic 6-rung ladder currently serves all 24).
  - Two versions of each topic (accessible / full), same theme and skeleton, differing only in
    the language load — not two separate idea lists.
  - Session page skeleton.
- [ ] **T5.3** — **Pronunciation track** (gated on D1 + D6). Korean's is not generic phonetics: it
  is a *closed, predictable, L1-contrastive* list. The Korean-L1-for-English list is equally
  closed — /r/–/l/, /f/–/p/, /v/–/b/, /θ/, /z/, final-consonant vowel epenthesis, consonant
  clusters, syllable- vs stress-timing, /æ/–/e/. Note `curriculum-rationale.md` §5 declined a
  pronunciation syllabus on *generic* grounds, before the L1 was ever named — worth re-taking.
- [ ] **T5.4** — **Decoding track** (gated on D6) — the `1-hangul` analogue: sound↔spelling,
  connected speech, and the loanword interference that makes written English unrecoverable in speech.
- [ ] **T5.5** — **Part 2 / B2–C1** (gated on D6). English currently stops at B1+ with an explicit
  scope boundary; Korean Core runs to 고급 in one file.

---

## Phase 6 · Validation — **size L, cannot be skipped**

Korean's native review knocked **28 of 264 patterns** out of the pattern slot as things people do
not actually say. Its TOC names the cause precisely: the parts built *from scenes* survived; the
part built *from a grammar list* did not (28 of 120 in Part 2). English's B1+ bridge and grammar
coverage map are exactly that shape.

- [ ] **T6.1** — Native-speaker pass over all 144 Core patterns + 96 Contextual patterns. Demote
  rather than delete — Korean moved rejects to the expression/grammar line so learners still meet
  them but are not asked to produce them.
- [ ] **T6.2** — Corpus/naturalness check on model sentences (Step 6 of the proposed method).
- [ ] **T6.3** — Row-level source audit: Core Inventory item + EGP form-and-meaning + CEFR
  descriptor for every grammar-map row. `proposed-authoritative-build-method.md` lists this as
  not done; until it is, `B1+` stays a working band, not a claim.
- [ ] **T6.4** — `english/PROOFREADING-WORKFLOW.md` + packet builder, mirroring Korean's
  reviewer-tree pipeline.
- [ ] **T6.5** — Learner pilot: two lessons per level, recorded task performance, delayed retrieval
  at one week, transfer check.

---

## Phase 7 · Product and deploy — **size M**

- [ ] **T7.1** — Assign the `classLevel` band and per-course decimal slots (gated on D5).
- [ ] **T7.2** — Course codes; `course.yaml` / `lesson.yaml` generation.
- [ ] **T7.3** — English catalog (gateway + per-track pages), generated, never hand-edited.
- [ ] **T7.4** — Trial material: trial decks per track, short cuts, the report deck, and an English
  `plan-logic.md` (level ladder, duration formula, the 5-month sales floor). This is the sales
  front door and currently does not exist in any form.
- [ ] **T7.5** — Sync path into `re-speak/podo-curriculum`; confirm the English tree survives
  `sync-from-authoring.py` → `import-track-lessons.py` → `repoint-shared.py` → `validate.py`.

---

## Sequencing note

The temptation is to start with Phase 3 because the TOC is the thing that exists and editing it
feels productive. Resist it. Phase 3 is real work but it does not reduce uncertainty — we already
know what those edits are. **Phase 2 is where the unknowns live**: nobody has yet proved that an
English lesson can be built out of this component vocabulary at all, and every estimate in
Phases 4–7 is a guess until one deck exists.

Phase 1 is a few hours and removes a live risk (agents working in an unguarded folder). Do it
alongside.
