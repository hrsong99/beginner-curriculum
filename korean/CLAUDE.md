# Working in `korean/`

**Read [`ux-philosophy.md`](./shared/ux-philosophy.md) before touching anything in this folder — every
time, including small edits.** It is the contract for every lesson page: one activity per page,
instant clarity, minimal everything, Korean-first titles, one green tutor-script box, one boxed
component that *fills* the page, receptive → productive.

Do not design a page, add a component, or write copy here until you have read it. If a change
you are about to make conflicts with it, say so and ask — don't quietly deviate.

## Also true of this folder

- **Shared design system:** `shared/lesson-card.css` ("Podo Bold"). Per-track additions go in that
  track's own stylesheet, loaded after it (e.g. `trial/trial.css`). Reuse the existing
  component vocabulary before inventing a new one — consistency over novelty.
- **Audience is Japanese speakers learning Korean.** All support text is Japanese; no English.
  Sound anchors are kana, not English words.
- **The green `.section-subtitle` box is the tutor's spoken script** (`.ko` = the line read
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

## Interactive lessons

Anything the learner taps, types, or drags — and anything that has to stay in step with the
tutor's screen — goes through lemonboard's `data-sync` contract.

**Before adding any interaction, read
[`interactive/interaction-protocol.md`](./interactive/interaction-protocol.md).** Getting it
wrong fails silently: the activity works on your screen and never reaches the other person.
Copy from [`interactive/sample-lesson-interactive.html`](./interactive/sample-lesson-interactive.html)
rather than inventing markup, and see
[`interactive/packaging.md`](./interactive/packaging.md) for turning a deck into an uploadable zip.

Two rules that catch most mistakes: an element is shared **only** if it has a `data-sync-id`
(no id = private), and verdicts are never shared — send the choice and let each side derive
`correct`/`wrong` locally. Note that this does *not* hide the answer key: both people load the
same document, so anything in the markup is already on the learner's screen.

## Layout

- **`tracks/`** — the learner-facing curriculum, in learning order: `1-hangul` · `2-core-patterns` ·
  `3-contextual-korean` · `4-freetalking` (pronunciation joins as `5-pronunciation` once it has content).
  Each track holds `table-of-contents.md`, its lesson HTML (`sample-lesson.html` is the canonical
  sample), and an `_archive/` for retired drafts and experiments.
- **`trial/`** — sales trial material, not a learning track. `full-trials/` holds the four complete
  decks (`trial-1..4`), `lessons/` holds the standalone lesson decks cut from them
  (`trial-1-hangul-short.html`, `trial-2-patterns-short.html`, plus its own `_archive/`
  for retired ones), and `onboarding-screens.html` sits at the top. Plus `trial.css`,
  shared `assets/` (art, mouth, characters), and `_experiments/` for variations and capture files.
- **`shared/`** — `lesson-card.css` (the design system) and `ux-philosophy.md` (the contract).
- **`interactive/`** — the `data-sync` contract, reference lesson, and lemonboard packager.
- **`references/`** — source textbook scans (internal reference only).
- `index.html` / `viewer.html` at the root are the navigation; `CLAUDE.md` / `AGENTS.md` stay at
  the root so they auto-load.
