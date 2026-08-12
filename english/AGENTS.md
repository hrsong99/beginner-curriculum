# Working in `english/`

**Read [`../ux-philosophy.md`](../ux-philosophy.md) before touching anything in this
folder — every time, including small edits.** It is the shared contract for every lesson page in
this repo, not a Korean-only document: one activity per page, instant clarity, minimal everything,
one blue tutor-script box, one boxed component that *fills* the page, receptive → productive.
Substitute "English" for "Korean" as the target language and almost all of it applies unchanged.
The places where it does **not** are listed under *English deltas* below — read those too.

Do not design a page, add a component, or write copy here until you have read both. If a change
you are about to make conflicts with either, say so and ask — don't quietly deviate.

**This folder is early.** Korean has 316 written decks, 8 build tools and a review pipeline;
English has a table of contents and this file. [`BUILD-PLAN.md`](./BUILD-PLAN.md) is the ordered
list of what is missing and who unblocks whom. When something below says a tool or file does not
exist yet, that is current fact, not an invitation to invent a local substitute — check the plan
and report the gap.

---

## Audience

**Japanese speakers learning English.** Same learner as the Korean curriculum, different target
language.

- **All support text is Japanese** — glosses, hints, instructions, answer-box labels, the
  translated half of the tutor's script. English is reserved for the target language itself.
  No Korean anywhere in a learner-facing English deck.
- **Tutor notes are written in Japanese here.** In Korean decks the notes are Korean, which
  doubles as a lock on the answers because a beginner cannot read them. That trick does not
  transfer — an English learner reads Latin script fine — so English tutor notes rely on the
  `チューターのみ` badge and the teaching-mode switch alone. Do not write answers into a note that
  the page already reveals.

### **No katakana readings. Ever. At any level.**

This is the one rule that *inverts* rather than copies its Korean counterpart, and it is the
easiest mistake for an agent that has just read `korean/AGENTS.md` to make.

Korean decks put a kana `.yomi` under the hangul through 초중급 because hangul is an unfamiliar
script and a beginner genuinely cannot decode it. **English has no such problem** — a Japanese
learner reads the Latin alphabet on day one, so the crutch scaffolds nothing.

Worse, it would actively teach the error. Writing `マクドナルド` over *McDonald's* does not support
the word; it installs mora-timed katakana English, which is the single most damaging Japanese-L1
pronunciation habit in the language and the thing a speaking course exists to undo. This is the
same reasoning that makes `1-hangul` carry no `.yomi` at all — printing the answer over the thing
being learned cancels the learning — except that here it applies to **every English deck at every
level**, not to one track.

So:

- English decks **do not load `yomi.js`** and carry no `.yomi`.
- `<meta name="podo:level">` still declares the deck's level for other purposes; it does not gate a
  reading, because there is no reading to gate.
- Kana is fine wherever it is *not* pronouncing English: a Japanese gloss, a hint chip
  (`JP:EN` vocabulary), a tutor note, a page title's parenthetical.
- If a model line ever genuinely needs a pronunciation scaffold, it must be IPA or a stress/rhythm
  mark, and it needs its own decision first (`BUILD-PLAN.md` → D3b). Do not reach for kana.

---

## Also true of this folder

- **Shared design system:** `../runtime/css/lesson-card.css`. White cards on a 1px grey
  outline; the palette lives in `:root` there — **use the tokens, never the hex**. Reuse the
  existing component vocabulary before inventing a new one — consistency over novelty.

  **The runtime lives at the repo root and is shared with the Korean curriculum.** There is exactly
  one copy; do not fork it, and do not change it from inside a lesson assignment. If an English
  deck needs something the runtime cannot do, **report the gap** — record it in
  `tracks/_conventions.md` § runtime queue, build the page with what exists, and say so. A shared
  file changed by one of several parallel writers lands with no review, and worse, does not reach a
  learner: decks load a pinned CDN tag, so a deck depending on a local runtime change renders right
  for its author and **unstyled in class**.

  Two path facts that will bite a hand-edited deck:

  | Target | Where | From a lesson deck |
  | --- | --- | --- |
  | the runtime | repo root, shared | seven `../` |
  | `trial/assets/` | still inside `korean/` — **did not move** | six `../` |
- **Every colour means one thing.** `green-500`/`green-100` = state (chosen, correct, active).
  `blue-100` = the tutor's spoken script. `blue-200` = the tutor-only band fused under it.
  `lime` = brand chrome only, never state. `gray-200` = ordinary outlines. Dashed grey = "write
  here". Adding a second meaning to any of these is the single easiest way to make a page
  unreadable — see the table in `ux-philosophy.md`.
- **The blue `.section-subtitle` box is the tutor's spoken script.** Natural spoken English, no
  grammar jargon, written in the first person (`I'll read it first` — never `the teacher will`).
  Its Japanese line is a direct translation of the English, not extra teaching content.
- **Lessons are audio-only.** The learner hears the tutor but never sees them, so no instruction
  may depend on watching the tutor — no "watch my mouth", no gestures, no "look at me". Model a
  sound by *saying* it. Describing the learner's **own** mouth is fine and matters more here than
  it does in Korean, because several of the target contrasts are articulatory
  (`Put your tongue between your teeth` for /θ/).
- **Max two levels of boxes:** the page card plus ONE boxed component inside it. Never wrap
  bordered components in another bordered card.
- Every lesson page needs `<meta name="google" content="notranslate">` or Chrome auto-translate
  mangles the mixed ja/en content. **This matters more for English than it did for Korean** —
  Chrome is far likelier to offer to translate a page that is half English.
- **Verify visually.** These are visual documents; render them in a browser at 480px width and
  look at the screenshots before claiming a change works.

---

## Writing a new lesson

**If the request says create/generate a curriculum, course, lesson, or batch of lessons, read
[`LESSON-CREATION-WORKFLOW.md`](./LESSON-CREATION-WORKFLOW.md) before planning or delegating.**

### Mandatory pilot gate

Treat the workflow's pilot sequence as a stop gate, not advice. **No English lesson deck exists
yet**, so the very first one is a pilot by definition: author it by hand, verify its complete
narrative, pedagogy, component markup and every page at 480px, then **stop for explicit user
approval**. Do not use a generic content generator, assign a lesson batch, or present additional
decks as finished before that approval. Structural checks alone never approve a pilot. If the
pilot is rejected, rewrite and re-review it; do not use it as a template. After approval, draft
three structurally different lessons, review those, and only then expand.

### The inputs, in order

1. **A deck skeleton.** Korean has `tools/new_lesson.py`, which lifts the meta block, stylesheet
   links and the load-order-bearing script tags off the track's canonical deck so they cannot
   drift. **English has no such tool yet** (`BUILD-PLAN.md` → T4.3). Until it exists, copy the
   skeleton from the approved English pilot deck — not from a Korean deck, whose script list
   includes `yomi.js`.
2. **The lesson brief.** Korean generates course-scoped briefs from its TOC. **English has no
   brief generator yet** (`BUILD-PLAN.md` → T4.2), so read the entry in the track's
   `table-of-contents.md` directly — and read the entries on either side of it, which is what a
   brief would have given you for free.
3. **`tracks/<track>/lesson-blueprint.md`** — which pages, in what order, doing what. Plan the arc
   from here. *(Written per track as each track's pilot lands.)*
4. **The canonical deck the blueprint names**, in full. This is the expensive read and it is the
   one worth paying for: the blueprint carries structure, but the tutor's voice, the way a wrong
   answer is made wrong for a reason, and the rhythm of the example sentences live only in the
   deck itself. A lesson written from the blueprint alone comes out correctly shaped and lifeless.

### Two constraints that are easy to lose

- **The "not yet" constraint binds the learner, not the tutor.** The tutor's spoken
  `.section-subtitle` is natural English and may run ahead of the syllabus. Forcing the syllabus
  into tutor speech makes the English stilted, which is worse.
- **Scaffold every non-target word.** Blanks target only the pattern being practiced. Hint chips
  list vocabulary only (`JP:EN`) — never articles, auxiliaries or inflections, which are the
  English analogue of the particles-and-endings rule in `ux-philosophy.md`.

---

## English deltas from `ux-philosophy.md`

Everything in that file holds except these. Each is a consequence of the target language changing,
not a matter of taste.

| `ux-philosophy.md` says | For English |
| --- | --- |
| Korean-first title, Japanese gloss in parentheses | **English-first** title, Japanese gloss in parentheses. Same shape. |
| Tutor notes in Korean; the language locks the answers | Tutor notes in **Japanese**. The lock is gone — rely on the badge and the switch, and never restate a revealed answer. |
| A `.yomi` reading through 초중급; the よみがな switch | **None, at any level.** See the audience section. English decks do not load `yomi.js`. |
| "Romanize the parts" — Latin letters as phonetic labels | Not applicable; the target language *is* Latin letters. If a page needs to show a sound apart from its spelling, that is IPA and it needs a decision first. |
| Decoding arc: Listen and pick → Read aloud → Build from the parts | No decoding track exists yet (`BUILD-PLAN.md` → D6/T5.4). The sentence arc below is the only one in use. |
| Sentence arc: Read → Choose → Reorder → Fill → Translate → Write | Unchanged, and it is the spine of every English lesson. |
| Cream/pink seat colours = consonant/vowel | Hangul-specific. Those tokens are unused in English decks; do not repurpose them for something else. |

---

## Layout

- **`tracks/`** — the learner-facing curriculum, in learning order: `1-core-patterns` ·
  `2-contextual-english` · `3-freetalking`. Each track holds `table-of-contents.md`, and will hold
  `lesson-blueprint.md` and its lesson HTML as those land.
- **`reference/`** — the author-only source trail: teaching philosophy and the pattern standard,
  the source hierarchy and provenance policy, the proposed evidence-first build method, the
  grammar coverage map, the rationale, and the transformation map from the linked Podolingo doc.
  **This is the strongest part of the English folder** and it is more rigorous than anything on the
  Korean side; it should eventually be back-ported rather than diluted.
- **`shared/`** — `lesson-template.md`, the two-pattern lesson spec. Note it is a *prose* spec: it
  does not yet correspond to any page structure or component. Reconciling it with a real blueprint
  is part of the pilot.
- **`BUILD-PLAN.md`** — the ordered gap list and its decisions. Read it before proposing work.
- **Archive — deliberately not here.** Retired drafts live in `_archive/` at the *repo* root. They
  are **not part of the read path**: never cite one as precedent, never copy markup out of one.
  If a grep turns up an `_archive/` hit, the live answer is elsewhere.

## Getting a lesson to production

**Not yet possible, and nothing here should pretend otherwise.** English has no course codes, no
`classLevel` band, no `course.yaml`, no catalog and no sync path (`BUILD-PLAN.md` → Phase 7).

Two constraints are already fixed and worth knowing before anyone designs around them, both from
`../korean/AGENTS.md`:

- **Stay `curriculumType: BASIC`.** It is a supported product line recognized by `podo-app`,
  `podo-backend` and `grape`. Do not create a version-suffixed variant.
- **Audience is `GT_CLASS_COURSE.COUNTRY_CODE`, not the level.** That column is what would
  separate this curriculum from an English-for-Korean-speakers line later. The sync manifest does
  not send it yet, so it needs a grape-side change rather than a new number scheme.

`LANG_TYPE` separates English from the Korean and Japanese curricula, so band numbers cannot
collide across languages even where they coincide.
