# English Curriculum — Current Build Plan

**Status:** curriculum architecture and authoring infrastructure are ready · native catalog review
is active · further lesson decks are intentionally on hold

**Current as of:** 2026-08-13

This is an operational plan, not a diary. It states what exists now, what remains, and what
unblocks what. Git history preserves the implementation chronology; completed work is summarized
here only when it changes the starting point for future work.

---

## Current snapshot

| Area | Current state |
| --- | --- |
| Audience | Japanese speakers learning English; all support text is Japanese |
| Curriculum | 4 tracks · 315 planned items |
| Production-facing catalog | 303 items: 122 Core · 60 Contextual · 121 Freetalking |
| Planning-only catalog | 12 pronunciation lessons; no pronunciation decks authorized |
| Authored lessons | 1 approved Core pilot: Core 20 |
| Blueprints | Core, Contextual and Freetalking complete |
| Generated author packets | 315 item briefs plus 4 indexes |
| Review surface | generated 303-item catalog; native review in progress |
| Automated quality | 18 regression tests; existing English deck passes with 0 errors and 0 warnings |
| Deployment | not ready: course identity, manifests and external sync path remain open |

The curriculum is no longer waiting for basic architecture or tooling. Its main content risk is
whether the reviewed patterns—especially Core 71–122—survive native and evidence review. Its main
product risk is the still-unassigned level and course identity scheme.

---

## Decisions already fixed

These are constraints, not open tasks.

- **Learner:** Japanese L1.
- **Support language:** Japanese throughout; English is the target language.
- **Pronunciation readings:** no katakana over English, no `.yomi`, and no `yomi.js` at any level.
- **Core reach:** Pre-A1 through working C1, currently 122 lessons.
- **Contextual identity:** scene-first shows with casts, season arcs and episode continuity.
- **Freetalking identity:** 121 shared topics, each designed for accessible and full versions.
- **Pronunciation:** a 12-lesson plan exists, but decks are deferred until Core is substantially
  further along.
- **Decoding:** no separate alphabet/decoding track; the learner already reads Latin script.
- **Product family:** remain `curriculumType: BASIC`; do not invent a version-suffixed family.
- **Audience separation:** country/audience belongs in `GT_CLASS_COURSE.COUNTRY_CODE`, not in a
  new level-number scheme.

### Decisions still required

| Decision | Why it is open | What it blocks |
| --- | --- | --- |
| Native catalog dispositions | The owner is reviewing the generated catalog | final Core/Contextual content, more decks |
| CEFR → product ladder mapping | Trial/report bands do not yet map to Pre-A1–C1 | recommendation logic, trial report |
| Product identity | No English `classLevel`, `LANG_TYPE` confirmation or course-code allocation | manifests, course generator, sync |
| Pronunciation notation | No model-line scaffold has been approved | only future pronunciation/scaffold work; not current Core authoring |

Do not invent answers to the product decisions inside a generator. Prepare evidence and options;
the owner/product system supplies the final values.

---

## What is already done

### 1. Curriculum architecture

- **Core:** 122 ordered two-pattern lessons in 22 units, Pre-A1 through working C1. All lessons
  have can-dos, two patterns, expressions and Japanese-L1 risk notes. Core 1–70 have learner-facing
  grammar support; Core 71–122 deliberately expose 52 missing grammar fields pending review.
- **Contextual:** 4 shows, 10 seasons and 60 episodes. Every episode has a can-do, who/where/what
  scene, two learner lines and two partner reactions. Seven episodes carry an optional
  receptive-only `Understand` target. CTX-54 and CTX-58 are the only missing expression fields.
- **Freetalking:** 11 themes and 121 topics with four explicit formats (`story`, `opinion`,
  `choose`, `両国`), an immediate opening and question ladder. The blueprint defines accessible
  and full language loads, correction loops and format-specific model pages.
- **Pronunciation:** 12 Japanese-L1 contrastive lessons are planned and parsed, but remain
  planning-only.
- Cross-track Core references were re-derived against the 122-lesson spine and mechanically
  range-checked. Generated briefs carry positive prerequisites and explicit “not yet” boundaries.

### 2. Authoring contract and pilot

- `AGENTS.md`, `LESSON-CREATION-WORKFLOW.md`, `PROOFREADING-WORKFLOW.md` and
  `tracks/_conventions.md` define the English-specific production and review rules.
- Core, Contextual and Freetalking each have a production blueprint.
- Core 20 is an approved, visually reviewed 25-page canonical deck.
- `new_lesson.py` copies only an approved English shell, retargets stable identity and paths,
  clears inherited vocabulary, refuses overwrite and keeps non-Core tracks behind their pilot gate.
- The running lexicon classifies new, recycled, assumed-known and receptive-only vocabulary.
  Core 20 currently owns five new content words. Deck validation enforces declarations, hint-chip
  coverage and the normal eight-word Core/Contextual ceiling.

### 3. Generated infrastructure

- One strict parser covers all four TOCs and rejects discontinuous or malformed source structure.
- `build_lesson_briefs.py` generates all 315 briefs and four indexes.
- `build_grammar_map.py` generates the 122-row Core sequence/coverage map and surfaces all 52 gaps.
- `build_catalog.py` generates the 303-item native-review catalog; the catalog holds no curriculum
  facts of its own.
- `parse_catalog_review.py` validates copied feedback against stable ids, titles and first-line
  snapshots, then emits structured JSON without editing a TOC.
- `build_running_lexicon.py` generates the authored vocabulary ledger from lesson metadata.
- `check_deck.py` checks identity, references, duplicate ids, inline code, no-yomi, tutor-script
  parity, reorder chunking and vocabulary ownership/load.
- Eighteen regression tests prove parser contracts, shell retargeting, generated brief/map/lexicon
  freshness and review-intake failure cases.

### 4. Shared foundation

- The language-neutral runtime, UX philosophy and viewer were moved to the repository root and all
  in-repository references were repaired.
- English uses the shared runtime without forking it. Korean trial art remains under `korean/` and
  is not implicitly reusable.
- The external `re-speak/podo-curriculum` sync scripts still need their old `korean/runtime/`
  assumptions updated before deployment; that work is outside this workspace.

---

## Active gate

The owner is reviewing `english/catalog.html`. While that review is open:

- do not author additional Core decks;
- do not invent grammar support for Core 71–122;
- do not fill CTX-54 or CTX-58 underneath the active review surface;
- do not hand-edit the generated catalog, briefs, grammar map or lexicon;
- do not author pronunciation decks;
- do not assign provisional product ids as if they were final.

The hold prevents avoidable content rework. It does not block read-only evidence gathering,
decision preparation, tooling that holds no curriculum facts, or documentation repair.

---

## Remaining work, in execution order

### A. Work that can proceed during native review

#### A1. Build the Core evidence ledger

Create a generated or strictly validated 122-row ledger connecting each Core lesson to:

- the relevant Core Inventory item or equivalent source;
- EGP form-and-meaning evidence where applicable;
- a CEFR descriptor or an explicit “no direct descriptor” result;
- the current working band and an evidence status.

Do not convert a missing citation into invented confidence. This work may flag rows, but it does
not edit the active TOC while native review is open. Until the ledger exists, B1+–C1 remains a
working organization rather than a validated CEFR claim.

#### A2. Run the corpus/naturalness audit

Check Core model sentences and frames against appropriate corpus or primary usage evidence. Record
queries, evidence and verdicts in a review artifact; do not silently rewrite the TOC. Prioritize
Core 71–122, then any row the native reviewer flags.

#### A3. Prepare the product-decision packet

Inspect the consuming product and curriculum repositories and present concrete, collision-checked
options for:

- CEFR-to-trial/report bands;
- English `classLevel` allocation;
- confirmed `LANG_TYPE` behavior;
- course-code conventions and course boundaries;
- the `COUNTRY_CODE` change required by the sync manifest.

This produces a decision packet, not final identifiers. Once the owner chooses, course generation
can proceed without rediscovery.

### B. Land native feedback

1. Export/copy the completed review and parse it with `parse_catalog_review.py`.
2. Triage each item as **keep, rewrite, demote, remove, or needs evidence**.
3. Apply accepted decisions only to authoritative TOCs.
4. On the accepted spine, write the 52 remaining Core grammar fields and the CTX-54/CTX-58
   expression fields. If review removes or demotes rows, recalculate the gap set first.
5. Re-derive every cross-track Core reference affected by a Core move.
6. Regenerate briefs, grammar map and catalog; run all regressions and deck checks.
7. Freeze a reviewed catalog version before lesson production resumes.

Exit condition: no unresolved native-review disposition, no unexplained Core grammar gap, no
missing required expression and no stale generated artifact.

### C. Prove representative lessons before scaling

1. Author three structurally different Core lessons: one narrative, one comparison and one B1+.
2. Review the three together for pedagogy, naturalness, vocabulary load, static correctness and
   rendered behavior at 480px and 360px.
3. Fix the blueprint or shared conventions when a repeated problem is structural; do not patch the
   same defect independently into multiple decks.
4. Stop for explicit approval before any wider Core batch.
5. Author one Contextual pilot from its show/episode blueprint; visually review and obtain explicit
   approval before treating it as canonical.
6. Author one Freetalking topic in both accessible and full versions; visually review and obtain
   explicit approval before treating either structure as canonical.
7. Only after the representative set exists, build the one-way authored-HTML proofreading packet
   projection. One Core pilot is not enough evidence for a universal packet schema.

### D. Create product structure

After the level and identity decisions are approved:

1. Build `plan_courses.py` to cut tracks at authored unit/season/theme boundaries.
2. Generate schema-valid `course.yaml` and `lesson.yaml`; never maintain a second curriculum copy
   inside the generator.
3. Assign final course codes, `classLevel`, `LANG_TYPE` and per-course slots.
4. Build trial materials only from approved representative content: track trials, short cuts,
   report deck and English `plan-logic.md`.
5. Update and verify the external sync path, including the root-runtime move and audience country.
6. Prove the full path through sync, import, shared-reference repointing and validation in the
   consuming repository.

### E. Scale and validate

1. Author by approved course batches, with writers owning disjoint lesson files and an orchestrator
   owning TOCs, generated artifacts, continuity and shared conventions.
2. Run static checks, exact-generation tests, proofreading and rendered QA for every batch.
3. Maintain the running lexicon and Contextual continuity in lesson order.
4. Conduct learner pilots: two lessons per level, recorded task performance, delayed retrieval at
   one week and a transfer task.
5. Revisit pronunciation notation and deck production only after Core evidence, representative
   lessons and the owner gate justify it.

---

## Immediate next action

Unless native feedback arrives first, the next agent-owned action is **A1: build the 122-row Core
evidence ledger without changing the live curriculum**. In parallel, the owner can finish catalog
review. After A1, proceed to corpus/naturalness evidence and then the product-decision packet.

If native feedback arrives at any point, switch to section B before authoring another lesson.

---

## Definition of production readiness

English is ready for scaled production only when all of the following are true:

- native catalog feedback is resolved and regenerated artifacts are current;
- the Core evidence/corpus audits have no untriaged high-risk rows;
- remaining grammar and expression gaps are closed on the accepted spine;
- the three representative Core lessons and both non-Core pilots are explicitly approved;
- course and product identity decisions are fixed and manifests validate;
- the external sync path passes end to end.

It is ready to ship only after batch QA, trial/report material and learner-pilot evidence are also
complete.
