# Working in `korean/`

**Read [`ux-philosophy.md`](./ux-philosophy.md) before touching anything in this folder — every
time, including small edits.** It is the contract for every lesson page: one activity per page,
instant clarity, minimal everything, Korean-first titles, one green tutor-script box, one boxed
component that *fills* the page, receptive → productive.

Do not design a page, add a component, or write copy here until you have read it. If a change
you are about to make conflicts with it, say so and ask — don't quietly deviate.

## Also true of this folder

- **Shared design system:** `lesson-card.css` ("Podo Bold"). Per-track additions go in that
  track's own stylesheet, loaded after it (e.g. `0-trial-class/trial.css`). Reuse the existing
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

## Tracks

`0-trial-class` (sales trial decks) · `1-hangul` · `2-core-patterns` · `3-contextual-korean` ·
`4-freetalking` · `?-pronunciation-class` · `textbooks-references` (source scans)
