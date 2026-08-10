# Deck conventions — read before writing any lesson

The briefs (`toc/lesson-NNN.md`) fix the **grammar**: what this lesson teaches, what the
learner already has, what a later lesson owns and must not be borrowed. That part is airtight.

This file fixes everything the briefs do not: **who appears, what things are called, which
scenes are spent, and what art exists.** Lessons get written in parallel, and without a shared
answer to those, ten lessons independently set their bonus scene in a café and introduce ten
different words for the same object. That reads as ten samples, not one course.

**Append to this file when you spend something.** Using a scene, a name, or a payoff word
marks it used. This is the one file a lesson-writer is expected to edit.

---

## Cast

**Story dialogues** — photo avatars, two named people:

| Name | Who | Avatar |
| --- | --- | --- |
| ハナ (하나) | Korean, the one who asks first | `…/test/hana-avatar.jpg` |
| ハルカ (하루카) | Japanese, the learner's stand-in | `…/test/haruka-avatar.jpg` |

**Practice dialogues** — icon avatars, no photos: `先生` (the tutor) and `私` (the learner).
**Bonus scenes** — the stranger is `相手`, never a named character.
**Named third parties in example sentences**: 다나카 (the learner's stand-in in core), 소희
(the contextual track's love interest — do not reuse her outside 3-contextual-korean).

`1-hangul` has **no cast at all.** It is decoding practice; there are no dialogue pages.

---

## Scenes already spent

Do not set a new bonus scene in one of these. The point of `korea-trip` is that the learner
meets today's pattern somewhere they have not been yet.

| Scene | Where | Track |
| --- | --- | --- |
| Guesthouse, first meeting | `trial-2-patterns` | trial |
| Korean café, book on the table | 과 7 `korea-trip` | core |
| Seoul subway, asking the way | 과 8 `korea-trip` | core |
| Convenience store, rainy night | `trial-3` / 설렘 & 고백 1화 | contextual |

Unspent and worth using: 시장, 병원 접수, 미용실, 택시, 편의점 계산대, 학교 첫날,
회사 점심시간, 공항 입국심사, 우체국, 헬스장.

---

## Art

**Everything referenced must already exist under `trial/assets/`.** A deck that names a file
nobody drew fails packaging, and the packager only bundles paths written in the markup — so an
invented filename 404s on the board while looking fine locally.

| Asset | Covers | Path |
| --- | --- | --- |
| Mouth shapes | **ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ only** — front + side | `trial/assets/mouth/{a,eo,o,u,eu,i}-{front,side}-illustration.png` |
| Stamp | 참 잘했어요 | `trial/assets/well-done.svg` |
| Mascot | brand pages | `trial/assets/podo-character{,-point}.png` |

**There is no art for consonants, y-vowels, w-vowels or 받침.** That is not an oversight to
work around — those letters are taught by *composition*, not by sound:

- y-vowels are a stroke added to a vowel already known (ㅏ→ㅑ), so they want `.build`
- w-vowels are two known vowels joined (ㅗ+ㅏ→ㅘ), so they want `.build`
- consonants are taught by the pair they contrast with, so they want `.pair-side`

Reach for a mouth image only for the six basic vowels. Anywhere else it is the wrong teaching.

---

## Words

**A hangul lesson may only use letters already taught.** The TOC's 「읽을 수 있는 것」 column is
the authoritative word list for each lesson — use those words, and only add others built from
letters that lesson or an earlier one has covered. A single unknown letter turns a decoding
drill into guessing.

**A payoff word is spent once *within a track*.** The word a lesson ends on (`sign-reading`,
`word-card`) should not be another lesson's payoff in the same track. The trial decks are a
separate product and do not spend anything — and **where the TOC assigns a word to a lesson,
the TOC wins over this list.**

| Track | Spent | By |
| --- | --- | --- |
| 1-hangul | 나무 · 어머니 · 오이 | 과 1 |
| 1-hangul | 고기 · 구두 · 다리 · 바다 · 사자 · 모자 · 주스 · 아버지 | 과 2 |
| 1-hangul | 가구 · 거리 · 부모 · 소리 · 도시 · 가지 | 과 3 |
| 1-hangul | 코 · 차 · 하마 · 토마토 · 커피 · 포도 | 과 4 |

**Everyday nouns already in circulation** — reuse these rather than inventing synonyms:

```
집 · 학교 · 회사 · 도서관 · 카페 · 시장
밥 · 커피 · 물 · 김치 · 책 · 음악 · 영화 · 드라마
매일 · 자주 · 보통 · 아침 · 저녁 · 주말 · 내일 · 지금
운동하다 · 요리하다 · 청소하다 · 공부하다 · 노래하다
가다 · 오다 · 먹다 · 마시다 · 읽다 · 보다 · 놀다 · 좋아하다
```

---

## Touching `runtime/` is not a deck decision

"No inline CSS or JS" means the deck ships none of its own. It does **not** mean the shared
runtime is yours to change — and two lesson-writers read it that way in the same batch:

| Deck | Changed | Why it was needed |
| --- | --- | --- |
| 과 7 | `js/hangul-activities.js` — `TALL` lacked ㅑㅕㅐㅔㅒㅖ | the builder drew a tall vowel into the bottom seat |
| 과 10 | `css/trial.css` — `.seat-b` · `.seat-lrb` · `.seat-tbb` · `.blk.lrb/.tbb` | there was no 받침 seat at all |

**Both fixes are correct.** That is the problem: a correct fix to a shared file, made by one of
ten parallel writers, lands with no review, no coordination with the nine others, and no way
for a reader to tell it apart from the file's existing uncommitted work.

Worse, it does not reach a learner. Decks load a **pinned CDN tag**, not this folder, so a deck
that depends on a local runtime change renders right for its author and **unstyled in class** —
과 10's bottom seat would deploy unpainted today.

So: if a lesson needs something the runtime cannot do, **stop and report it — do not fix it.**
Note what is missing, build the page with what exists, and say so. The change then gets made
once, reviewed, and published as a version, instead of ten times in ten directions.

## The seat-colour system only covers the 과 1 case

Three writers hit this independently, so it is a gap in the design system, not three mistakes.
Seat colour (`.seat-c` consonant, `.seat-v` vowel) was built for a block of **one simple
consonant + one simple vowel**, and has no answer for anything else:

| Shape | Problem | Where |
| --- | --- | --- |
| combined vowel (ㅘ ㅝ ㅢ) | uses *both* seats, so neither fill describes it | 과 8 |
| 받침 | there is no third seat | 과 10–14 |
| y/e vowels in `.builder` | `TALL = ["ㅏ","ㅓ","ㅣ"]` draws ㅑㅕㅐㅔㅒㅖ as top/bottom | 과 7–9 |

The workaround the decks converged on: **a block that seat colour cannot describe runs
un-tinted, and only the bare letter takes a seat.** Do that rather than tinting something
half-true — a wrong seat teaches a wrong structure, which is worse than no colour at all.

## Unresolved — 받침 자리 색 (decide before 과 10–14 ship)

**Two decks in the same track draw the bottom slot two different ways.** The design system had
no 받침 seat at all — every block until 과 10 is consonant-seat + vowel-seat — and two agents
hit that gap independently and answered it differently:

| Deck | Answer |
| --- | --- |
| 과 10 | **added** `.seat-b` · `.seat-lrb` · `.seat-tbb` · `.blk.lrb/.tbb` to `runtime/css/trial.css`, uses them 64× |
| 과 11 | uses them, 40× — read "match your neighbour" as decisive and followed 과 10 |
| 과 14 | uses them, 2× |
| 과 12 · 13 | every 받침 tile **plain** — 과 12 looked for a seat colour, found none, worked around it |

A learner going 과 11 → 12 sees the bottom slot change appearance. **과 10's answer should win**
— this track draws structure with seat colour and the third position deserves one, the floor
was measured (62%, because glyph ink runs ~22–75% and the obvious 68% cuts through the 받침),
and three of five decks already use it. The sweep is 과 12 and 13.

Two things block just doing it. It is a **shared stylesheet** change made by one of ten
parallel writers, tangled with pre-existing uncommitted work in the same file; and it does not
exist on the published CDN tag, so **과 10 · 11 · 14 deploy with an unpainted bottom seat until
`runtime/` is republished.** Both need a human, not another agent.

**Until it is settled: do not add new 받침 seat markup.** Match the deck next to yours and say
which in your report.

## Things that have already gone wrong

Each of these cost a rewrite. They are not style preferences.

- **ㅗ examples must not contract.** 보다 and 오다 become 봐요/와요 and break any rule you are
  drawing about ㅗ. Use 놀다. (`AUTHORING.md` § 설명용 도식 says so and it is easy to miss.)
- **Colour is a category, not a word.** `.topic` violet = 조사 (은/는, 을/를, 에/에서),
  `.ending` orange = 어미 (이에요, -아/어요). The CSS comments name the trial deck's specific
  instances; the category is what the colour means.
- **`아직 아님` binds the learner, not the tutor.** The tutor's spoken `.section-subtitle` is
  natural Korean and may run ahead of the syllabus — the trial deck uses `-거든요` in 과 1.
  Forcing the constraint into tutor speech makes the Korean stilted, which is worse.
- **`.batchim` is not only for 받침.** When a rule is decided by something other than sound
  (에 vs 에서 is decided by the verb), drop the letter tile and arrow and keep `.bt-out` alone.
  A letter tile on a non-phonological rule sends learners hunting for a sound rule.
- **No yomi inside a two-way `.opt` pill** — it turns four one-line rows into a paragraph.
  The `.choose-word` beside it does take one.
- **`1-hangul` carries no `.yomi` at all and does not load `yomi.js`.** Printing the kana over
  a word the learner is being asked to decode hands them the answer and cancels the drill.
  The track's kana surfaces are `.kana-eq` (the letter↔kana anchor, while a letter is being
  taught), `.word-card` and `.known-row small`. Decode drills carry nothing. Every other track
  follows the level rule in `CLAUDE.md` instead. *(Three lesson-writers were told the opposite
  by their brief and all three followed the sample deck over the brief — which is the reason
  the deck is read in full.)*
- **A mouth photo on a listening tile is noise unless the two options differ in vowel.** Both
  agents who hit this arrived at it independently: on a 가/카 row the mouth is identical, so
  the image tells the learner nothing and competes with the letter for attention.

---

## Before you call a lesson done

1. Every `href`/`src` resolves — run the deck's own relative paths, do not eyeball them.
2. Nothing from the brief's `아직 아님` appears in learner-produced Korean.
3. Render at 480px and look at it. These are visual documents; a page that reads fine as
   markup can be unusable as a page.
4. **Check every page for clipping, not just for looking right.** The pager floats over the
   bottom ~60px, so a page taller than the window loses its last element with no scrollbar and
   no error. Opening the deck and paging through will not show it — the clipped part is simply
   not there. Measure it:

   ```js
   [...document.querySelectorAll('.phone > [data-page-id]')]
     .filter(p => { const d = p.style.display; p.style.display = '';
                    const h = p.scrollHeight; p.style.display = d;
                    return h > innerHeight - 60; })
     .map(p => p.dataset.pageId)
   ```

   A goal page carries **three or four rows, not six** — six overflowed and hid the last word
   while the tutor line still promised it.
4. Append whatever you spent — scene, payoff word, new noun — to this file.
