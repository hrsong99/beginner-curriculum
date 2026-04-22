# Lesson 5: 〜を 〜ます — What Do You Eat, Drink, Read?

## Design Notes

**Changes from Lesson 4:**

- Cumulative review now spans L1 (です) + L2 (これ/それ/あれ) + L3 (どこ) + L4 (あります/います). Same first-timer-friendly format: fill-in (Q1) + translate-with-vocab-hint (Q2), 2 Qs per lesson.
- **Vocab page simplified to a Connect-the-Dots matching activity** (recognition, not production). It mixes L5 new words with a small number of L1/L2 review words so returning students get cumulative reinforcement without fresh cognitive load. Replaces L4's full EN→JP recall table.
- **Dropped the Today's Character (hiragana/katakana) bonus page** — tested poorly as a class activity; the isolated character drill interrupted lesson flow without reinforcing the target pattern.
- **NEW: Quick Practice page** — multiple choice (two inline options separated by `/` inside the blank) + word-reorder, modeled on the prestudy interaction style. Acts as low-stress downtime between heavier drill pages. No open production required.
- **NEW: Listening Activity page** — a short **first-person monologue** delivered via **mp3** (not tutor-read): "Yuki's Daily Routine," ~20 seconds, uses only Pattern A (affirmative) naturally; the question-form isn't forced in since it doesn't fit a self-introduction. Student answers multiple-choice comprehension — each question and each option is bilingual (EN + JP). A "Show Full Transcript" button reveals the complete JP/EN script after students finish the MCs (replaces the second-pass fill-in activity).
- Pattern drills and conversation structure carried over from Lesson 4.

**Two focused patterns:**

- Pattern A: `[noun]を [verb]ます。` — affirmative daily action (I drink coffee.)
- Pattern B: `[noun]を [verb]ますか？` → `はい、〜ます。／ いいえ、〜ません。` — question & negative answer

**Target verbs (5):** たべます, のみます, よみます, みます, ききます
**Target objects:** ごはん, パン, みず, コーヒー, ほん, テレビ, えいが, おんがく

**Hint principles:**

- Hint boxes contain **vocab only** (nouns, verbs, adjectives, question words). No particles (は, が, に, を, の), no conjugated forms (〜ます/〜ません/〜ますか), no pattern templates. Patterns live at the top of each drill page only.
- **Bonus "No Hints Translate" prerequisite:** every vocab word required by that page must already appear on Page 6 (Vocab Connect) or in the pattern drills.

**Styling conventions (carry over from Lesson 4):**

- Warm romaji color (#c4b8a8) used for furigana `<rt>` text
- JP/EN paired layout uses `.pair` wrappers with `.jp` and `.en` child divs
- Inline fill-in-the-blank inputs use `.blank-input` class
- Full-width answer inputs use `.blank-input-full` class
- Q:/A: grid layout (`.qa` + `.qa-label`) for review exercises
- Help-word boxes use `.help-box` class
- Dashed separators (`<hr class="separator">`) between sections
- Interactive hanamaru (花丸) on Mission Complete checkbox click
- Tutor script notation: `▸ "English text" ／ 「にほんご」` — embedded at point of use
- Roleplay HINTS box merges PHRASES and WORDS into one `.help-box`
- Multiple choice: on Page 7, render the two inline options as a single tappable pair separated by `/` inside the blank (e.g. `（ たべます / のみます ）`); each option is independently clickable with green/red feedback. On Page 8, render as stacked buttons with EN label and JP translation on one line.
- Word reorder: word-bank buttons + answer tray + Check/Reset/Show Answer (like prestudy `.reorder-item`)
- Listening activity: embed an mp3 audio player at the top of the page; audio file covers the full monologue. The "Show Full Transcript" button toggles a hidden `.transcript-reveal` block containing the JP script with furigana + EN translation. No tutor-read path.

## Lesson Flow (14 Core + 1 Bonus + Mission Complete)


| Page | Activity                          | Time  | Notes                                   |
| ---- | --------------------------------- | ----- | --------------------------------------- |
| 1    | Greeting & Intro                  | 1 min | Hello, let's start                      |
| 2    | Review: L1 + L2 + L3 + L4         | 2 min | 2 Qs/lesson: fill-in + translate        |
| 3    | Today's Patterns                  | 2 min | 〜を〜ます / 〜ますか (+ pronunciation cue) |
| 4    | Pattern Drill A (affirmative)     | 3 min | I eat / drink / read / watch            |
| 5    | Pattern Drill B (question + neg)  | 3 min | Do you…? Yes/No                         |
| 6    | Vocab Connect (matching)          | 2 min | EN ↔ JP — incl. L1/L2 review words      |
| 7    | Quick Practice (MC + Reorder)     | 2 min | Low-stress downtime                     |
| 8    | Listening Activity                | 3 min | mp3 monologue → MC (bilingual) + reveal |
| 9    | Short Dialogues                   | 2 min | 4 dialogues                             |
| 10   | Guided Conversation               | 2 min | Cafe scene                              |
| 11   | Memory Conversation               | 2 min | Fill-in of Page 10                      |
| 12   | Free Discussion                   | 2 min | 3 rounds                                |
| 13   | Roleplay                          | 2 min | Order at a cafe                         |
| 14   | Travel in Japan                   | 2 min | Restaurant / ordering                   |
| 15   | BONUS: Translate (no hints)       | 2 min | Skip if short on time                   |
| 16   | Mission Complete                  | 1 min |                                         |

Travel conversation also appears in prestudy (plain, no highlights).

**Core: ~28 min / With bonus: ~30 min** (planning for 25 min actual class time)

---

### PAGE 1 — Greeting & Intro


```
+-------------------------------------------------------------------------+
|                                                                         |
|  〜を 〜ます                                                             |
|  What Do You Eat, Drink, Read?                                          |
|                                                                         |
|  ① 〜さん、こんにちは！また あいましたね。                                 |
|     "Hi ~, good to see you again!"                                      |
|                                                                         |
|  ② きょうも よろしく おねがいします。                                      |
|     "Let's have a great lesson today."                                  |
|                                                                         |
|  ③ これを よんで ください。                                                |
|     "Please read this."                                                 |
|                                                                         |
|                                                                  PAGE 1 |
+-------------------------------------------------------------------------+
```

### PAGE 2 — Review: L1 + L2 + L3 + L4

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Quick review — translate each sentence into Japanese."              |
|    「ふくしゅうしましょう。にほんごにしてみてね。」                      |
|                                                                         |
|  REVIEW: LESSONS 1–4                                                    |
|  ────────────────────                                                   |
|                                                                         |
|  ┌─ LESSON 1: です (I am / he is) ─────────────────────────┐            |
|  │                                                          │            |
|  │  PATTERN:  [person]は [noun]です。                        │            |
|  │                                                          │            |
|  │  1. FILL IN:  わたしは がくせい______。                    │            |
|  │               "I am a student"                            │            |
|  │                                                          │            |
|  │  2. TRANSLATE:  She is a teacher.                        │            |
|  │     → ____________________________________              │            |
|  │                                                          │            |
|  │  ┌─ Q2 WORDS ─────────────────────────────────────┐     │            |
|  │  │  かのじょ(she)  せんせい(teacher)                │     │            |
|  │  └─────────────────────────────────────────────────┘     │            |
|  └──────────────────────────────────────────────────────────┘            |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ┌─ LESSON 2: これ・それ・あれ ─────────────────────────────┐            |
|  │                                                          │            |
|  │  PATTERN:  これ / それ / あれ は [noun]です。             │            |
|  │                                                          │            |
|  │  1. FILL IN:  ______は ほんです。                         │            |
|  │               "This is a book"                            │            |
|  │                                                          │            |
|  │  2. TRANSLATE:  That over there is a bag.                │            |
|  │     → ____________________________________              │            |
|  │                                                          │            |
|  │  ┌─ Q2 WORDS ─────────────────────────────────────┐     │            |
|  │  │  あれ(that over there)  かばん(bag)              │     │            |
|  │  └─────────────────────────────────────────────────┘     │            |
|  └──────────────────────────────────────────────────────────┘            |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ┌─ LESSON 3: どこ (where) ────────────────────────────────┐            |
|  │                                                          │            |
|  │  PATTERN:  [noun]は どこですか？                          │            |
|  │                                                          │            |
|  │  1. FILL IN:  カフェは______です。                        │            |
|  │               "The cafe is there"                         │            |
|  │                                                          │            |
|  │  2. TRANSLATE:  The book is here.                        │            |
|  │     → ____________________________________              │            |
|  │                                                          │            |
|  │  ┌─ Q2 WORDS ─────────────────────────────────────┐     │            |
|  │  │  ほん(book)  ここ(here)                          │     │            |
|  │  └─────────────────────────────────────────────────┘     │            |
|  └──────────────────────────────────────────────────────────┘            |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ┌─ LESSON 4: あります・います (is there) ──────────────────┐            |
|  │                                                          │            |
|  │  PATTERN:  [place]に [thing]が あります。                 │            |
|  │            [place]に [person/animal]が います。           │            |
|  │                                                          │            |
|  │  1. FILL IN:  へやに テレビが______。                     │            |
|  │               "There is a TV in the room"                 │            |
|  │                                                          │            |
|  │  2. TRANSLATE:  There is a cat at home.                  │            |
|  │     → ____________________________________              │            |
|  │                                                          │            |
|  │  ┌─ Q2 WORDS ─────────────────────────────────────┐     │            |
|  │  │  いえ(home)  ねこ(cat)                           │     │            |
|  │  └─────────────────────────────────────────────────┘     │            |
|  └──────────────────────────────────────────────────────────┘            |
|                                                                         |
|                                                                  PAGE 2 |
+-------------------------------------------------------------------------+
```

### PAGE 3 — Today's Patterns

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's read together. Copy my pronunciation closely — slow is OK."  |
|    「いっしょによみましょう。はつおんをよくまねしてね。                  |
|     ゆっくりでいいですよ。」                                            |
|                                                                         |
|  TODAY'S PATTERNS                                                       |
|  ================                                                       |
|                                                                         |
|  1. I DO something  —  [noun]を [verb]ます                               |
|                                                                         |
|     • わたしは ごはんを たべます。                                       |
|       I eat rice.                                                       |
|                                                                         |
|     • わたしは コーヒーを のみます。                                     |
|       I drink coffee.                                                   |
|                                                                         |
|                                                                         |
|  2. Do you…?  —  [noun]を [verb]ますか？                                 |
|     Answer:    はい、〜ます。／ いいえ、〜ません。                        |
|                                                                         |
|     • ほんを よみますか？                                                |
|       Do you read books?                                                |
|       → はい、よみます。／ いいえ、よみません。                          |
|                                                                         |
|     • テレビを みますか？                                                |
|       Do you watch TV?                                                  |
|       → はい、みます。／ いいえ、みません。                              |
|                                                                         |
|                                                                         |
|     ┌─── REMEMBER ──────────────────────────────────────────┐           |
|     │  を  → the thing you act on (rice, coffee, book...)    │           |
|     │  〜ます   → I do it  (positive)                         │           |
|     │  〜ますか → Do you…?  (question)                        │           |
|     │  〜ません → I don't   (negative)                        │           |
|     └────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                  PAGE 3 |
+-------------------------------------------------------------------------+
```

### PAGE 4 — Pattern Drill A (〜を 〜ます — Affirmative)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL A: 〜を 〜ます (I DO something)                           |
|  ────────────────────────────────────────────                           |
|                                                                         |
|  PATTERN:  [noun]を [verb]ます。                                         |
|            I [verb] [noun].                                             |
|                                                                         |
|                                                                         |
|  ▸ "Let's read together. Copy my pronunciation closely — slow is OK."  |
|    「いっしょによみましょう。はつおんをよくまねしてね。                  |
|     ゆっくりでいいですよ。」                                            |
|                                                                         |
|  1. Read Together:                                                      |
|     * ごはんを たべます。            I eat rice.                         |
|     * みずを のみます。              I drink water.                      |
|     * ほんを よみます。              I read a book.                      |
|     * テレビを みます。              I watch TV.                         |
|     * おんがくを ききます。          I listen to music.                  |
|                                                                         |
|                                                                         |
|  ▸ "Fill in the blank and read the whole thing!"                        |
|    「くうらんにことばをいれて、ぜんぶよんでみましょう！」                |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * ごはん（　　　）たべます。           I eat rice.                   |
|     * みずを（　　　）。                   I drink water.                |
|     * ほん（　　　）よみます。             I read a book.                |
|     * （　　　）を みます。                I watch TV.                   |
|     * おんがくを（　　　）。               I listen to music.            |
|                                                                         |
|                                                                         |
|  ▸ "Translate to Japanese — hints are OK."                              |
|    「にほんごにしてみましょう。ヒントをみてもいいですよ。」              |
|                                                                         |
|  3. Translate:                                                          |
|     * I drink coffee.                                                   |
|       _____________________________________________________             |
|       (coffee = コーヒー)                                                |
|                                                                         |
|     * I eat bread.                                                      |
|       _____________________________________________________             |
|       (bread = パン)                                                     |
|                                                                         |
|     * I read a book.                                                    |
|       _____________________________________________________             |
|       (book = ほん)                                                      |
|                                                                         |
|     * I watch a movie.                                                  |
|       _____________________________________________________             |
|       (movie = えいが)                                                   |
|                                                                         |
|     * I listen to music.                                                |
|       _____________________________________________________             |
|       (music = おんがく)                                                 |
|                                                                         |
|                                                                         |
|  ▸ "Make your own! What do you eat or drink every day?"                 |
|    「じぶんのぶんをつくってみましょう！                                  |
|     まいにち なにを たべますか？ なにを のみますか？」                  |
|                                                                         |
|  4. Make Your Own:                                                      |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 4 |
+-------------------------------------------------------------------------+
```

### PAGE 5 — Pattern Drill B (〜を 〜ますか — Question & Negative)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL B: 〜ますか？ / 〜ません (DO YOU…? / I DON'T)             |
|  ───────────────────────────────────────────────────                    |
|                                                                         |
|  PATTERN:  [noun]を [verb]ますか？                                       |
|            → はい、〜ます。／ いいえ、〜ません。                          |
|                                                                         |
|                                                                         |
|  ▸ "Next pattern. Let's ask and answer together."                       |
|    「つぎのパターンです。しつもんとこたえ、いっしょにやってみましょう。」|
|                                                                         |
|  1. Read Together:                                                      |
|     * コーヒーを のみますか？          Do you drink coffee?              |
|       → はい、のみます。                Yes, I do.                       |
|                                                                         |
|     * テレビを みますか？              Do you watch TV?                  |
|       → いいえ、みません。              No, I don't.                      |
|                                                                         |
|     * ほんを よみますか？              Do you read books?                |
|       → はい、よみます。                Yes, I do.                       |
|                                                                         |
|     * パンを たべますか？              Do you eat bread?                 |
|       → いいえ、たべません。            No, I don't.                      |
|                                                                         |
|     * おんがくを ききますか？          Do you listen to music?           |
|       → はい、ききます。                Yes, I do.                       |
|                                                                         |
|                                                                         |
|  ▸ "Fill in the blank and read the whole thing!"                        |
|    「くうらんにことばをいれて、ぜんぶよんでみましょう！」                |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * コーヒーを のみ（　　　）？        Do you drink coffee?            |
|       → はい、のみ（　　　）。            Yes, I do.                      |
|                                                                         |
|     * テレビを み（　　　）？            Do you watch TV?                |
|       → いいえ、み（　　　）。            No, I don't.                     |
|                                                                         |
|     * ほん（　　　）よみますか？          Do you read books?             |
|       → はい、よみます。                                                 |
|                                                                         |
|                                                                         |
|  ▸ "Translate to Japanese."                                             |
|    「にほんごにしてみましょう。」                                        |
|                                                                         |
|  3. Translate:                                                          |
|     * Do you drink water?                                               |
|       _____________________________________________________             |
|       (water = みず)                                                     |
|                                                                         |
|     * Do you eat rice?                                                  |
|       _____________________________________________________             |
|       (rice = ごはん)                                                    |
|                                                                         |
|     * No, I don't watch movies.                                         |
|       _____________________________________________________             |
|       (movie = えいが)                                                   |
|                                                                         |
|     * Yes, I listen to music.                                           |
|       _____________________________________________________             |
|       (music = おんがく)                                                 |
|                                                                         |
|                                                                         |
|  ▸ "Now you ask ME a question!"                                         |
|    「こんどは、あなたがわたしにしつもんしてね！」                        |
|                                                                         |
|  4. Ask the Tutor:                                                      |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 5 |
+-------------------------------------------------------------------------+
```

### PAGE 6 — Vocab Connect (Matching)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  VOCAB CONNECT                                                          |
|  ──────────────                                                         |
|                                                                         |
|  ▸ "Draw a line from English to Japanese. Say each pair out loud!"      |
|    「えいごとにほんごを せんで つないでね。                              |
|     そして こえに だして よみましょう！」                               |
|                                                                         |
|                                                                         |
|  TODAY'S VERBS                                                          |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  eat            •    │    •  のみます         │                        |
|  │  drink          •    │    •  みます           │                        |
|  │  read           •    │    •  たべます         │                        |
|  │  watch          •    │    •  ききます         │                        |
|  │  listen         •    │    •  よみます         │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  TODAY'S OBJECTS                                                        |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  rice           •    │    •  コーヒー         │                        |
|  │  water          •    │    •  ごはん           │                        |
|  │  coffee         •    │    •  おんがく         │                        |
|  │  movie          •    │    •  みず             │                        |
|  │  music          •    │    •  えいが           │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  REVIEW FROM BEFORE  (L1 · L2 · L4)                                     |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  student        •    │    •  ねこ             │                        |
|  │  teacher        •    │    •  がくせい         │                        |
|  │  book           •    │    •  ほん             │                        |
|  │  cat            •    │    •  せんせい         │                        |
|  │  this           •    │    •  これ             │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|                                                                  PAGE 6 |
+-------------------------------------------------------------------------+
```

### PAGE 7 — Quick Practice (Multiple Choice + Word Reorder)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  QUICK PRACTICE                                                         |
|  ──────────────                                                         |
|                                                                         |
|  ▸ "Easy round! Just tap and check."                                    |
|    「かんたんなラウンドです。タップしてたしかめてみましょう！」          |
|                                                                         |
|                                                                         |
|  A. MULTIPLE CHOICE — Pick the right word (tap one).                    |
|                                                                         |
|     1. ごはんを（ たべます / のみます ）。       I eat rice.             |
|                                                                         |
|     2. みずを（ みます / のみます ）。           I drink water.          |
|                                                                         |
|     3. ほんを（ よみます / ききます ）。         I read a book.          |
|                                                                         |
|     4. テレビ（ を / に ）みます。               I watch TV.             |
|                                                                         |
|     5. コーヒーを のみ（ ます / ますか ）？      Do you drink coffee?    |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Now drag the words into the right order."                           |
|    「ことばをただしいじゅんばんにならべてみましょう。」                  |
|                                                                         |
|  B. WORD REORDER — Put the words in the correct order.                  |
|                                                                         |
|     1. I eat rice.                                                      |
|        [ たべます ] [ を ] [ ごはん ]                                    |
|        → _____________________________________                          |
|                                                                         |
|     2. I drink coffee.                                                  |
|        [ のみます ] [ コーヒー ] [ を ]                                  |
|        → _____________________________________                          |
|                                                                         |
|     3. I read a book.                                                   |
|        [ を ] [ よみます ] [ ほん ]                                      |
|        → _____________________________________                          |
|                                                                         |
|     4. Do you watch TV?                                                 |
|        [ か ] [ みます ] [ テレビ ] [ を ]                               |
|        → _____________________________________                          |
|                                                                         |
|     5. I don't listen to music.                                         |
|        [ ききません ] [ おんがく ] [ を ]                                |
|        → _____________________________________                          |
|                                                                         |
|                                                                  PAGE 7 |
+-------------------------------------------------------------------------+
```

### PAGE 8 — Listening Activity

```
+-------------------------------------------------------------------------+
|                                                                         |
|  LISTENING                                                              |
|  ──────────                                                             |
|                                                                         |
|  ▸ "Press play and listen. Don't peek at the transcript yet!"           |
|    「さいせいボタンをおして、きいてみましょう。                          |
|     まだ スクリプトは みないでね！」                                    |
|                                                                         |
|                                                                         |
|  ┌─── AUDIO PLAYER ──────────────────────────────────────────┐          |
|  │                                                            │          |
|  │   ▶  [  ━━━━━━━━━━━━━━━━━━━━━━━━━  ]  0:00 / 0:22        │          |
|  │                                                            │          |
|  │   Yuki's Daily Routine  (ゆきの いちにち)                   │          |
|  │                                                            │          |
|  └────────────────────────────────────────────────────────────┘          |
|                                                                         |
|  ┌─── AUDIO SCRIPT (hidden from student — for tutor/dev ref) ┐          |
|  │                                                            │          |
|  │  こんにちは、ゆきです。                                      │          |
|  │  まいあさ コーヒーを のみます。                              │          |
|  │  ごはんも たべます。                                         │          |
|  │  よる、うちで ほんを よみます。                              │          |
|  │  そして、ねるまえに おんがくを ききます。                    │          |
|  │                                                            │          |
|  │  (Hi, I'm Yuki. Every morning I drink coffee.              │          |
|  │   I also eat rice. At night, I read books at home.         │          |
|  │   And before bed, I listen to music.)                      │          |
|  └────────────────────────────────────────────────────────────┘          |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  COMPREHENSION — Multiple Choice                                        |
|  ▸ "Answer the questions. Listen again if you need to!"                 |
|    「しつもんにこたえましょう。もういちどきいてもいいですよ！」          |
|                                                                         |
|                                                                         |
|  1. What does Yuki drink in the morning?                                |
|     ゆきさんは あさ なにを のみますか？                                   |
|        a)  water / みず                                                  |
|        b)  coffee / コーヒー                                             |
|                                                                         |
|                                                                         |
|  2. Does Yuki eat rice?                                                 |
|     ゆきさんは ごはんを たべますか？                                      |
|        a)  Yes / はい、たべます                                          |
|        b)  No  / いいえ、たべません                                      |
|                                                                         |
|                                                                         |
|  3. What does Yuki do at night?                                         |
|     よる、ゆきさんは なにを しますか？                                    |
|        a)  watches TV / テレビを みます                                  |
|        b)  reads a book / ほんを よみます                                |
|                                                                         |
|                                                                         |
|  4. What does Yuki listen to before bed?                                |
|     ねるまえに ゆきさんは なにを ききますか？                             |
|        a)  music / おんがく                                              |
|        b)  the news / ニュース                                           |
|                                                                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "All done? Click to see the full script and read along!"             |
|    「ぜんぶ できたら、ボタンをおして スクリプトをみてみましょう！」      |
|                                                                         |
|     ┌──────────────────────────────────────┐                            |
|     │   ▶  SHOW FULL TRANSCRIPT            │                            |
|     │      (スクリプトを みる)              │                            |
|     └──────────────────────────────────────┘                            |
|                                                                         |
|                                                                  PAGE 8 |
+-------------------------------------------------------------------------+
```

### PAGE 9 — Short Dialogues

```
+-------------------------------------------------------------------------+
|                                                                         |
|  SHORT DIALOGUES                                                        |
|  ────────────────                                                       |
|                                                                         |
|  ▸ "Ask this in Japanese."                                              |
|    「にほんごできいてみましょう。」                                      |
|                                                                         |
|  DIALOGUE 1:                                                            |
|  Student:  [_________________________________]                          |
|            Do you drink coffee?                                         |
|  Tutor:    はい、コーヒーを のみます。                                    |
|            Yes, I drink coffee.                                         |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  コーヒー(coffee)                          │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "I'll ask. Answer in Japanese."                                      |
|    「わたしがききます。にほんごでこたえてね。」                          |
|                                                                         |
|  DIALOGUE 2:                                                            |
|  Tutor:    ほんを よみますか？                                           |
|            Do you read books?                                           |
|  Student:  [_________________________________]                          |
|            Yes, I read books.                                           |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  ほん(book)                               │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Your turn — ask in Japanese."                                       |
|    「あなたのばんです。にほんごできいてみてね。」                        |
|                                                                         |
|  DIALOGUE 3:                                                            |
|  Student:  [_________________________________]                          |
|            Do you watch movies?                                         |
|  Tutor:    いいえ、みません。                                             |
|            No, I don't.                                                 |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  えいが(movie)                             │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Last one! I'll ask — answer in Japanese."                           |
|    「さいごです！しつもんします、にほんごでこたえてね。」                |
|                                                                         |
|  DIALOGUE 4:                                                            |
|  Tutor:    おんがくを ききますか？                                        |
|            Do you listen to music?                                      |
|  Student:  [_________________________________]                          |
|            Yes, I listen to music.                                      |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  おんがく(music)                           │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|                                                                  PAGE 9 |
+-------------------------------------------------------------------------+
```

### PAGE 10 — Guided Conversation

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's read together. I'll be Yuki, you be Alex."                    |
|    「いっしょによみましょう。わたしがゆきで、あなたがアレックスです。」  |
|                                                                         |
|  CONVERSATION: GUIDED READING                                           |
|  ----------------------------                                           |
|                                                                         |
|  ┌─── CONTEXT / 状況 ─────────────────────────────────────────┐         |
|  │  Alex and Yuki are at a cafe ordering lunch.               │         |
|  │  アレックスとゆきが カフェで ひるごはんを ちゅうもんします。     │         |
|  └────────────────────────────────────────────────────────────┘         |
|                                                                         |
|                                                                         |
|  YUKI:   アレックスさん、なにを のみますか？                               |
|          Alex, what will you drink?                                     |
|                                                                         |
|  ALEX:   わたしは コーヒーを のみます。                                    |
|          I'll drink coffee.                                             |
|                                                                         |
|  YUKI:   ごはんは？ パンを たべますか？                                    |
|          How about food? Do you eat bread?                              |
|                                                                         |
|  ALEX:   はい、パンを たべます。ゆきさんは？                               |
|          Yes, I'll eat bread. How about you, Yuki?                      |
|                                                                         |
|  YUKI:   わたしは ごはんを たべます。みずも のみます。                     |
|          I'll eat rice. I'll drink water too.                           |
|                                                                         |
|  ALEX:   いいですね！                                                    |
|          Sounds good!                                                   |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Great job! Now let's swap. This time I'll be Alex."                 |
|    「じょうずですね！こうたいしましょう。                                |
|     こんどはわたしがアレックスです。」                                  |
|                                                                         |
|                                                                 PAGE 10 |
+-------------------------------------------------------------------------+
```

### PAGE 11 — Memory Conversation

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Same conversation, but now from memory!                             |
|     I'll be Yuki. You're Alex — say the full sentence."                 |
|    「おなじかいわです。こんどはおぼえていってみましょう！                |
|     わたしがゆきです。あなたはアレックス                                |
|     — ぜんぶのぶんをいってください。」                                  |
|                                                                         |
|  CONVERSATION: MEMORY CHECK                                             |
|  --------------------------                                             |
|  Tutor = Yuki / Student = Alex                                          |
|                                                                         |
|                                                                         |
|  YUKI (tutor):   なにを のみますか？                                     |
|                  What will you drink?                                   |
|                                                                         |
|  ALEX (you):     わたしは コーヒーを______。                              |
|                  I'll drink coffee.                                     |
|                                                                         |
|  YUKI (tutor):   パンを たべますか？                                     |
|                  Do you eat bread?                                      |
|                                                                         |
|  ALEX (you):     はい、パンを______。                                    |
|                  Yes, I'll eat bread.                                   |
|                                                                         |
|  YUKI (tutor):   わたしは ごはんを たべます。みずも のみます。            |
|                  I'll eat rice. I'll drink water too.                   |
|                                                                         |
|  ALEX (you):     ______ですね！                                          |
|                  Sounds good!                                           |
|                                                                         |
|                                                                 PAGE 11 |
+-------------------------------------------------------------------------+
```

### PAGE 12 — Free Discussion

```
+-------------------------------------------------------------------------+
|                                                                         |
|  FREE DISCUSSION                                                        |
|  ────────────────                                                       |
|                                                                         |
|  ▸ "I'll ask — you answer. Then ask me the same question back!"         |
|    「わたしがききます、こたえてください。                                |
|     そのあと、おなじしつもんをしてね！」                                |
|                                                                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ROUND 1: WHAT DO YOU DRINK?                                            |
|                                                                         |
|  Tutor:    「まいあさ なにを のみますか？」                               |
|            "What do you drink every morning?"                           |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「まいあさ なにを のみますか？」                               |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  コーヒー(coffee)  みず(water)                      │               |
|     │  おちゃ(tea)       ぎゅうにゅう(milk)                │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─    |
|                                                                         |
|  ROUND 2: WHAT DO YOU READ / WATCH?                                     |
|                                                                         |
|  Tutor:    「よる なにを みますか？ なにを よみますか？」                 |
|            "What do you watch / read at night?"                         |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「よる なにを みますか？」                                    |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  テレビ(TV) えいが(movie) ほん(book)                │               |
|     │  まんが(comic) ニュース(news)                       │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─    |
|                                                                         |
|  ROUND 3: WHAT DO YOU NOT DO?                                           |
|                                                                         |
|  Tutor:    「なにを たべませんか？ なにを のみませんか？」                |
|            "What don't you eat or drink?"                               |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「なにを たべませんか？」                                     |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  ごはん(rice) パン(bread) にく(meat)                │               |
|     │  さかな(fish) やさい(vegetables)                    │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|                                                                 PAGE 12 |
+-------------------------------------------------------------------------+
```

### PAGE 13 — Roleplay

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ROLEPLAY                                                               |
|  ────────                                                               |
|  "At the Cafe"                                                          |
|                                                                         |
|  SCENARIO                                                               |
|  あなたは カフェに きました。                                             |
|  メニューを みて、ちゅうもんしましょう！                                   |
|  You've arrived at a cafe. Look at the menu and order!                  |
|                                                                         |
|  GOAL                                                                   |
|  ともだち（＝チューター）に なにを たべるか、なにを のむか                 |
|  きいてから、じぶんも ちゅうもんしましょう！                               |
|  Ask your friend (the tutor) what they'll eat and drink,                |
|  then order for yourself!                                               |
|                                                                         |
|  やること:                                                                |
|    ① ともだちに「なにを のみますか？」ときく                              |
|    ② ともだちに「なにを たべますか？」ときく                              |
|    ③ じぶんも ちゅうもんする                                             |
|  To do:                                                                 |
|    ① Ask the friend what they'll drink                                  |
|    ② Ask the friend what they'll eat                                    |
|    ③ Order something for yourself                                       |
|                                                                         |
|  HINTS                                                                  |
|  ┌──────────────────────────────────────────────────────────┐           |
|  │  PATTERN                                                  │           |
|  │  なにを ＿＿ますか？          What will you ＿＿?           │           |
|  │  わたしは ＿＿を ＿＿ます。    I'll ＿＿ ＿＿.               │           |
|  │  WORDS                                                    │           |
|  │  コーヒー(coffee) みず(water) おちゃ(tea)                  │           |
|  │  ごはん(rice) パン(bread) ケーキ(cake)                      │           |
|  └──────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                 PAGE 13 |
+-------------------------------------------------------------------------+
```

### PAGE 14 — Travel in Japan

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Imagine you're at a small Japanese restaurant!"                     |
|    「にほんの ちいさな レストランに いるとおもってね！」                 |
|                                                                         |
|  TRAVEL IN JAPAN: AT A RESTAURANT                                       |
|  ─────────────────────────────────                                      |
|  You are a traveler. Fill in the blanks and say them out loud!          |
|                                                                         |
|  ┌─── CONTEXT / 状況 ─────────────────────────────────────────┐         |
|  │  The waiter is taking your order at a small Japanese       │         |
|  │  restaurant. Tell them what you'll eat and drink.          │         |
|  └────────────────────────────────────────────────────────────┘         |
|                                                                         |
|     ┌─── NEW WORDS ──────────────────────────────────────┐              |
|     │  すし (sushi)      おちゃ (green tea)                │              |
|     │  おねがいします (please)                              │              |
|     │  メニュー (menu)                                      │              |
|     └─────────────────────────────────────────────────────┘              |
|                                                                         |
|                                                                         |
|  WAITER:   いらっしゃいませ！なにを ______か？                            |
|            Welcome! What will you eat?                                  |
|                                                                         |
|  YOU:      わたしは すしを ______。                                      |
|            I'll have sushi.                                             |
|                                                                         |
|  WAITER:   なにを のみますか？                                           |
|            What would you like to drink?                                |
|                                                                         |
|  YOU:      おちゃを ______。                                             |
|            I'll have green tea.                                         |
|                                                                         |
|  WAITER:   パンも ______か？                                             |
|            Will you also eat bread?                                     |
|                                                                         |
|  YOU:      いいえ、パンは ______。                                        |
|            No, I won't eat bread.                                       |
|                                                                         |
|  YOU:      おねがいします！                                               |
|            Please (please bring it)!                                    |
|                                                                         |
|                                                                 PAGE 14 |
+-------------------------------------------------------------------------+
```

### PAGE 15 — Bonus: Translate (No Hints)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS: TRANSLATE — NO HINTS!                                           |
|  ──────────────────────────────                                         |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  ▸ "Translate these — no hints!"                                        |
|    「ヒントなしでにほんごにしてみましょう！」                            |
|                                                                         |
|                                                                         |
|  1. I eat rice.                                                         |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  2. I drink coffee.                                                     |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  3. Do you read books?                                                  |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  4. I don't watch TV.                                                   |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  5. Do you listen to music?                                             |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  6. I eat bread and drink water.                                        |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|                                                                 PAGE 15 |
+-------------------------------------------------------------------------+
```

### PAGE 16 — Mission Complete

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Great job today! Let's check them off."                             |
|    「きょうはじょうずでしたね！いっしょにチェックしましょう。」          |
|                                                                         |
|  ミッションかんりょう！                                                   |
|  Mission Complete!                                                      |
|  ─────────────────                                                      |
|                                                                         |
|  きょうのミッション:                                                      |
|  ┌─────────────────────────────────────────────────────────┐            |
|  │                                                          │            |
|  │  ┌──┐                                                    │            |
|  │  │  │  PATTERN 1: ＿＿を ＿＿ます。                       │            |
|  │  └──┘              (I do something)                      │            |
|  │                                                          │            |
|  │  ┌──┐                                                    │            |
|  │  │  │  PATTERN 2: ＿＿を ＿＿ますか？                      │            |
|  │  └──┘              (Do you…? Yes/No)                      │            |
|  │                                                          │            |
|  └─────────────────────────────────────────────────────────┘            |
|                                                                         |
|                                                                         |
|  ▸ "Let's read one more time. Perfect! See you next lesson!"            |
|    「さいごにもういちどよみましょう。かんぺき！                          |
|     つぎのレッスンであいましょう！」                                    |
|                                                                         |
|  KEY EXPRESSIONS — もういちどよんでみましょう！                           |
|  • ごはんを たべます。               — I eat rice.                        |
|  • コーヒーを のみます。             — I drink coffee.                    |
|  • ほんを よみますか？               — Do you read books?                 |
|  • テレビを みません。               — I don't watch TV.                  |
|                                                                         |
|                                                                 PAGE 16 |
+-------------------------------------------------------------------------+
```
