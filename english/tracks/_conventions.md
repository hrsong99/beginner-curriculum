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

> **Status: one deck written.** Core 22 (`Could you help me with ___?`) is the pilot and the
> canonical deck for `1-core-patterns`. The ledgers below carry what it spent. Contextual and
> Freetalking have no decks yet, so their rows are empty by fact rather than by oversight.

---

## The inline mark vocabulary in English

**`.ending` means "the taught frame words" — the fixed language the learner has to retrieve.**
It is the only inline accent an English deck uses, and it has exactly one meaning.

This is a decision, not an inheritance. Korean's two accents are grammatical categories —
`.topic` violet = 조사, `.ending` orange = 어미 — and English has neither. Rather than pick a
second category arbitrarily, English spends one accent on one idea and leaves violet unused.

Consequences a writer has to honour:

- A rule diagram about the taught frame takes **`class="batchim ending-rule"`**, not bare
  `.batchim`. Bare `.batchim` renders violet, which in this repo means 조사 — a category English
  does not have and must not borrow. The pilot shipped violet first and it was wrong.
- **`.topic` is unspent.** Do not reach for it as a spare slot. If a lesson genuinely teaches two
  distinct pieces, report it — a second accent needs one human decision about what it *means*,
  the same way Korean's third-accent gap does.

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
| Airport check-in counter, too much luggage | Core 22 `in-the-wild` | core |
| New office, moving boxes in | Core 22 `p3-model` (main dialogue, **not** available as a transfer scene) | core |

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
| 1-core-patterns | `I can carry the small one.` — the line the transfer scene lands on | Core 22 |

### Vocabulary in circulation

`shared/lesson-template.md` caps new content words at **six to eight per lesson**. That cap is
currently unenforceable because no word inventory exists — building one is `BUILD-PLAN.md` → T3.9,
and this is where its per-track working copy lives once it does.

Reuse what is already in circulation rather than inventing synonyms.

**Core Patterns** — in circulation after Core 22. Reuse these rather than inventing synonyms:

```
box · suitcase · bag · menu · Wi-Fi · station · counter
carry · find · help
big · small · one (the big one / the small one — substitution, Core 20)
```

Supporting expressions heard but never asked for in a learner slot:
`What do you need?` (Core 22) · `Anything else?` (Core 16) · `Do you need help?` (receptive)

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

Korean's assets live under `korean/trial/assets/`. **Whether English may reference one is decided
per asset, in the table below** — the test is whether the art carries anything Korean in it, not
whether it happens to sit in the Korean folder. Check the file before adding a row; do not assume.

| Asset | Covers | Path | Shared? |
| --- | --- | --- | --- |
| Well-done stamp | the `stamp.js` mark | `korean/trial/assets/well-done.svg` | **yes** — checked, it is pure paths with no text in it, so nothing about it is Korean |
| Mascot | brand pages | `korean/trial/assets/podo-character{,-point}.png` | untested — no English deck uses a brand page yet |
| Mouth shapes | six Korean vowels | `korean/trial/assets/mouth/…` | **no** — hangul-specific. If an English pronunciation track ever needs mouth art it needs its own, drawn for English contrasts |

Note the path: `trial/assets/` stayed inside `korean/` when the runtime was hoisted to the repo
root, so from a lesson deck the assets are **one `../` shorter** than the runtime.

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
| **Republish the runtime** | **blocking for class use** | `.pattern-meaning`, `.meaning-kicker` and `.nuance-compare` exist locally but are **not in the published CDN tag** (Korean's own queue says so). Core 22 uses all three. Until the runtime is republished the deck renders correctly for its author and **unstyled in class** — the exact failure this repo keeps warning about |
| `.br-cn` sizing for loanwords | not written | 33px fits Korean's 2–3-character kanji. Katakana loanwords are longer: `スーツケース` wraps to two lines and makes its row taller than its neighbours. English will hit this constantly, because long loanwords are exactly the ones worth showing. Core 22 keeps `スーツケース` — dropping the lesson's best example to satisfy a layout constraint is the wrong trade |
| A three-branch rule diagram | not written | inherited from Korean and **worse here**: `do/does/did`, `a/an/the` and `-s/-es/-ies` are all three-case, and `.batchim` is single-column. Core 22 dodged it (its rule is an honest two-brancher). The next lesson that does not, ships two boxes and reports it |
| `.ko` / `.korean` class names | naming only, not a defect | they mean "the line the tutor reads" and "the target-language span". English decks reuse them as-is, because renaming is a runtime change touching 316 Korean decks. Worth knowing before someone reads an English deck and thinks it is mislabelled |
| A second inline accent for English | not written | see the mark-vocabulary section above. Not needed yet |

**Expect this table to fill up fast.** The Korean runtime was designed against Korean pedagogy, and
several of its components encode assumptions that do not hold for English — the `.batchim` rule
diagram is built around a phonological branch on the preceding syllable, and English's equivalent
branches (voicing on `-ed`, `-s` allomorphy, article choice) do not have that shape. Record what
does not fit rather than bending a component into a wrong teaching.

---

## Before you call a lesson done

0. **`python3 english/tools/check_deck.py <your deck>` — run this first.** It mechanises items
   1, 3, 4 and 5 below and exits non-zero on any error. It does not replace looking at the page.
1. Every `href`/`src` resolves — run the deck's own relative paths, do not eyeball them.
2. Nothing the lesson has not taught appears in learner-produced English.
3. **No `.yomi`, no katakana over any English word, and `yomi.js` is not loaded.** See
   `../AGENTS.md` — this is the rule most likely to be broken by an agent that read the Korean
   instructions first.
4. **Tutor script sentence parity** — same sentence count on both sides of every `.section-subtitle`
   (`.pattern-meaning` exempt). Mismatched counts make `script-lines.js` give up silently and the
   box renders as bunched text. Script in `../LESSON-CREATION-WORKFLOW.md` §6.
5. **Reorder chunking** — one criterion per page, written into a comment above it, and every row
   checked against that one sentence. Mixed criteria are the defect; the count is only the symptom.
6. Render at 480px and look at it. These are visual documents; a page that reads fine as markup can
   be unusable as a page. Both of the checks above were added *because the pilot passed every other
   check and still shipped them* — markup review does not catch either.
7. **Check every page for a tail hidden under the pager.** Korean documented three separate wrong
   ways to measure this, each of which passed on all 59 decks while the defect was live. Read
   `../../korean/tracks/_conventions.md` § "Before you call a lesson done" item 4 and use its probe
   — measure the page's own height with the viewport prop removed, against the smallest screen this
   has to work on, not against your monitor.
8. Append whatever you spent — scene, payoff word, new vocabulary — to this file.
