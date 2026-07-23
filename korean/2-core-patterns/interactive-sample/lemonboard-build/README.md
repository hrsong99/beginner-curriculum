# lemonboard-html upload build — interactive sample

Packaged output of `sample-lesson-interactive.html` for the lemonboard upload slot
(html 1개 + css 1개 → `lecture.html`/`lecture.css` or `prestudy.html`/`prestudy.css`).

The generator and a full explanation of the upload contract live in
[`../../0-trial-class/lemonboard-build/`](../../0-trial-class/lemonboard-build/README.md).

```sh
python3 ../../0-trial-class/lemonboard-build/build_lemonboard.py \
    sample-lesson-interactive.html --out lemonboard-build
```

## What packaging did to this deck

Only one stylesheet to merge (`lesson-card.css`) — this deck's own rules are an inline
`<style>`, which rides along in the HTML. The two avatar images are already absolute S3
URLs, so nothing needed rewriting to a CDN and the deck has no image pin to keep fresh.

| | |
|---|---|
| `sample-lesson-interactive.zip` | the upload — use it for both slots |
| `lecture.html`, `lecture.css` | unzipped, for inspection |

The HTML links both `lecture.css` and `prestudy.css`, so one zip works in either slot
whichever way the platform renames it.

## Verified after packaging

Extracted flat the way S3 unpacks it, then loaded: single sheet applied, Pretendard loaded,
0/12 images broken, 30 pages, pager turning and emitting `set-page`, remote `set-page` and
`set-value` applying, snapshot covering 50 shared targets.

## Caveat

Uploading this deck ships the *markup and runtime* half of the sync protocol. Nothing
synchronises until the host app attaches a transport:

```js
PodoLessonSync.configure({ senderId: 'peer-a' });
PodoLessonSync.onOutbound(msg => channel.send(JSON.stringify(msg)));
channel.onmessage = e => PodoLessonSync.receive(JSON.parse(e.data));
PodoLessonSync.requestSnapshot();
```

Without it the deck behaves exactly as it did before — a normal single-player lesson.
