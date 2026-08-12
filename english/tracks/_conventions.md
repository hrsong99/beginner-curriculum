# Deck conventions — read before writing any lesson

The track TOCs fix the **grammar**: what a lesson teaches, what the learner already has, what a
later lesson owns and must not be borrowed. That part is (or will be) airtight.

This file fixes everything the TOCs do not: **who appears, what things are called, which scenes
are spent, and what art exists.** Lessons get written in parallel, and without a shared answer to
those, ten lessons independently set their bonus scene in a café and introduce ten different words
for the same object. That reads as ten samples, not one course.

**Append to this file when you spend something.** Using a scene, a name, or a payoff word marks it
used. This is the one file a lesson-writer is expected to edit — **unless you are one of a parallel
batch**, in which case report it and let the orchestrator write it. Ten writers editing one file is
how the file gets lost.

> **Status: seeded, nothing spent.** No English deck exists yet, so every ledger below is empty by
> fact rather than by oversight. The first pilot deck fills the first rows. Do not treat an empty
> table as permission to skip the ledger — treat it as the reason to start it correctly.

---

## Cast

**Decided:** Contextual English is built as **shows with a named cast and episodes**
(`BUILD-PLAN.md` → D7), not as situation menus. So this table is load-bearing from the first
contextual deck onward, the way `korean/tracks/_conventions.md` is for the drama track.

**Core Patterns** — practice dialogues only, no story cast: `Tutor` and `Me`, icon avatars.

**Contextual English** — one work per course, each with its own cast, photo avatars, and a
relationship state that carries across episodes.

| Course | Work title | Cast | Relationship state |
| --- | --- | --- | --- |
| *(none yet)* | | | |

**The learner is a role, not a spectator.** The speaker of every learner line is `私` — the part
the learner performs. The tutor reads the other role.

Korean's equivalent file carries a warning worth pre-empting here: **the learner may legitimately
have two names across frames** — a role name inside a story dialogue, and a stand-in name in
example sentences and bonus scenes. If that ever becomes true here, write it down at the moment it
is decided. Korean lost two bonus-scene punchlines to a later writer "fixing" the inconsistency.

**Named third parties in example sentences:** *(none yet)*

---

## Scenes already spent

Do not set a new bonus or transfer scene in one already used. The point of a transfer scene is that
the learner meets today's pattern somewhere they have not been yet.

| Scene | Where | Track |
| --- | --- | --- |
| *(none yet)* | | |

**Assign scenes up front for a parallel batch, one per lesson**, and let the assignment travel in
each writer's packet. Korean assigned 과 11–45 in advance precisely so parallel writers could not
collide, and still produced one duplicate — because two scenes were compared *by name* rather than
by situation (`waiting for a late friend` twice, under two different venue names).
**Compare situations, not labels.**

**A venue used for a main dialogue is not available as that lesson's transfer scene either.** A
learner who meets the same room twice in one lesson reads it as a mistake.

---

## Words

**A payoff word is spent once within a track.** The word or phrase a lesson lands on should not be
another lesson's payoff in the same track. Where the TOC assigns a word to a lesson, the TOC wins
over this list.

| Track | Spent | By |
| --- | --- | --- |
| *(none yet)* | | |

### Vocabulary in circulation

`shared/lesson-template.md` caps new content words at **six to eight per lesson**. That cap is
currently unenforceable because no word inventory exists — building one is `BUILD-PLAN.md` → T3.9,
and this is where its per-track working copy lives once it does.

Reuse what is already in circulation rather than inventing synonyms.

**Core Patterns** — *(none yet)*

**Contextual English** — *(none yet)*

### Receptive-only

Words and forms that appear in partner lines but are never asked for in a learner-produced slot go
here, with the reason. Korean's example: a counter that no lesson owns yet, kept receptive until
the TOC assigns it. Keep that restraint rather than quietly promoting a word to productive.

*(none yet)*

---

## Art

**Everything referenced must already exist.** A deck that names a file nobody drew fails packaging,
and the packager only bundles paths written in the markup — so an invented filename 404s on the
board while looking fine locally.

Korean's assets live under `../korean/trial/assets/`. **Which of them English may reference is not
yet decided** — the mascot and the stamp are brand-level and probably shared; the mouth-shape
illustrations are hangul-vowel-specific and are not. Do not reference a Korean asset path from an
English deck until this row is filled in.

| Asset | Covers | Path |
| --- | --- | --- |
| *(not yet decided)* | | |

---

## Touching the runtime is not a deck decision

"No inline CSS or JS" means the deck ships none of its own. It does **not** mean the shared runtime
is yours to change.

Korean learned this the expensive way: two lesson-writers in one batch each made a *correct* fix to
a shared stylesheet, and the correctness was the problem — a shared-file change made by one of ten
parallel writers lands with no review, no coordination, and no way for a reader to tell it apart
from the file's existing uncommitted work. Worse, it does not reach a learner: decks load a pinned
CDN tag, not the working folder, so a deck depending on a local runtime change renders right for
its author and **unstyled in class**.

So: if a lesson needs something the runtime cannot do, **stop and report it — do not fix it.** Note
what is missing, build the page with what exists, and say so.

### Runtime queue — English gaps waiting on a decision

| Needed | State | Why |
| --- | --- | --- |
| *(none recorded yet — the pilot deck will produce the first entries)* | | |

**Expect this table to fill up fast.** The Korean runtime was designed against Korean pedagogy, and
several of its components encode assumptions that do not hold for English — the `.batchim` rule
diagram is built around a phonological branch on the preceding syllable, and English's equivalent
branches (voicing on `-ed`, `-s` allomorphy, article choice) do not have that shape. Record what
does not fit rather than bending a component into a wrong teaching.

---

## Before you call a lesson done

1. Every `href`/`src` resolves — run the deck's own relative paths, do not eyeball them.
2. Nothing the lesson has not taught appears in learner-produced English.
3. **No `.yomi`, no katakana over any English word, and `yomi.js` is not loaded.** See
   `../AGENTS.md` — this is the rule most likely to be broken by an agent that read the Korean
   instructions first.
4. Render at 480px and look at it. These are visual documents; a page that reads fine as markup can
   be unusable as a page.
5. **Check every page for a tail hidden under the pager.** Korean documented three separate wrong
   ways to measure this, each of which passed on all 59 decks while the defect was live. Read
   `../../korean/tracks/_conventions.md` § "Before you call a lesson done" item 4 and use its probe
   — measure the page's own height with the viewport prop removed, against the smallest screen this
   has to work on, not against your monitor.
6. Append whatever you spent — scene, payoff word, new vocabulary — to this file.
