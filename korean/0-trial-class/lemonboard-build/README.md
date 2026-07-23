# lemonboard-html upload build

Packaged output for the lemonboard upload slot, plus the script that produces it.

## The upload contract

> zip 안에 html 1개 + css 1개(선택: 이미지 등 부속 파일)를 넣어 업로드하세요. 생성 시 S3
> `lemonboard-html/{교재ID}/` 아래에 수업용은 `lecture.html`·`lecture.css`, 예습용은
> `prestudy.html`·`prestudy.css` 로 풀어서 업로드됩니다.

Three things follow from that, and all three are handled by `build_lemonboard.py`:

**One CSS, not two.** Our decks load `lesson-card.css` (shared design system) and the track's
own sheet (`trial.css`). The script concatenates them *in link order* so the cascade is
unchanged, and hoists any `@import` to line 1 where CSS requires it.

**The `<link>` has to anticipate the rename, twice.** The platform renames the stylesheet on
unpack but does not rewrite the `href` inside the HTML — and the same zip goes into both the
수업용 and 예습용 slots, which rename it differently. So the HTML carries **both** links:

```html
<link rel="stylesheet" href="lecture.css">
<link rel="stylesheet" href="prestudy.css">
```

Whichever slot the zip lands in, one resolves and the other 404s, which browsers ignore. One
file, both slots.

**Images go over the network.** They can't ride in the zip: our art lives in `mouth/` and
`art/` subfolders, and the unpack flattens into a single S3 prefix. Local `<img src>` is
rewritten to jsDelivr, pinned to a commit SHA:

```
https://cdn.jsdelivr.net/gh/hrsong99/beginner-curriculum@<sha>/korean/0-trial-class/...
```

Pinned rather than `@main` so a later commit cannot change a deck that is already live.
`raw.githubusercontent.com` is avoided — it is not meant for hotlinking, and it serves CSS as
`text/plain` with `nosniff`, which browsers refuse to apply as a stylesheet.

## Rebuilding

```sh
python3 lemonboard-build/build_lemonboard.py trial-1-hangul.html --out lemonboard-build
```

The script warns if any referenced image is not yet on `origin/main` — those would 404 from
the CDN. **Push image changes before building**, and rebuild whenever artwork changes, since
the pin freezes images at the SHA it was built with.

## Files here

| File | What it is |
|---|---|
| `trial-1-hangul.zip` | the upload — `lecture.html` + `lecture.css`; use it for both slots |
| `lecture.html`, `lecture.css` | unzipped, for inspection |
| `build_lemonboard.py` | the generator; works on any deck in this repo |

The deck is trimmed to the lesson itself (the needs section and the plan/price/FAQ block are
gone) and syncs over `podo.lesson-sync` v3 — page turns, tap tiles and the syllable keypad.
Teaching mode is deliberately local: the tutor reveals answers without revealing them to the
learner.

## Caveat

The page needs internet for images and the Pretendard webfont. If a classroom might be on a
locked-down network, the alternative is inlining images as `data:` URIs — still exactly two
files, fully offline, at the cost of a much larger HTML.
