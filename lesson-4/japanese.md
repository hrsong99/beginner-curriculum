# Lesson 4: あります・います — Is There...?

## Design Notes

**Changes from Lesson 3 (extending 15 min → 25 min):**

- Cumulative review now covers L1 (です) + L2 (これ/それ/あれ) + L3 (どこ), not just the previous lesson
- **Review page is first-timer friendly**: 2 questions per pattern — Q1 is a fill-in-blank where most of the Japanese sentence is shown so a student who never took L1–L3 can still infer the missing piece from the pattern formula above; Q2 is a translate-from-English with vocab hints, which is the production rep for returning students. 6 questions total instead of 9.
- **Pronunciation cues embedded** in the Today's Patterns page and both Pattern Drill "Read Together" steps — "listen closely and repeat closely" phrasing, no dedicated page, no shadowing loops (would get boring fast)
- NEW: **Vocab Recall** page moved from bonus to CORE (production, not recognition)
- Pattern drills now have **5 items per sub-activity** (was 3)
- Short Dialogues extended from 3 → 4
- Free Discussion extended from 2 → 3 rounds
- Roleplay now includes one animate target (a person) to force います
- Travel-in-Japan context: convenience store / restaurant (natural あります / います use)

**Two focused patterns:**

- Pattern A: `[place]に [thing]が あります` — for inanimate things
- Pattern B: `[place]に [person/animal]が います` — for living beings

**Hint principles:**

- Hint boxes contain **vocab only** (nouns, verbs, adjectives, demonstratives, question words). No particles (は, が, に, の, から), no copula (〜です), no pattern templates (〜は 〜ですか, 〜がありますか). Patterns live at the top of each drill page, not inside every hint.
- **Page 13 (Bonus 1 "No Hints Translate") prerequisite:** every vocab word required by Page 13 sentences must already be tested on Page 6 (Vocab Recall). If you add a new word to Page 13, add it to Page 6 first.

**Styling conventions (carried over from Lesson 3):**

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

## Lesson Flow (12 Core + 2 Bonus + Mission Complete)


| Page | Activity                          | Time  | Notes                                   |
| ---- | --------------------------------- | ----- | --------------------------------------- |
| 1    | Greeting & Intro                  | 1 min | Hello, let's start                      |
| 2    | Review: L1 + L2 + L3              | 2 min | 2 Qs/lesson: fill-in-blank + translate  |
| 3    | Today's Patterns                  | 3 min | あります / います (+ pronunciation cue)  |
| 4    | Pattern Drill A (あります)          | 3 min | Things — 5 items per sub                |
| 5    | Pattern Drill B (います)            | 3 min | People/animals — 5 items per sub        |
| 6    | Vocab Recall                      | 2 min | Production (EN → JP)                    |
| 7    | Short Dialogues                   | 2 min | 4 dialogues                             |
| 8    | Guided Conversation               | 2 min | Classroom / cafe scene                  |
| 9    | Memory Conversation               | 2 min | Fill-in of Page 8                       |
| 10   | Free Discussion                   | 2 min | 3 rounds                                |
| 11   | Roleplay                          | 2 min | Find 3 things + 1 person                |
| 12   | Travel in Japan                   | 2 min | Convenience store / restaurant          |
| 13   | BONUS 1: Translate (no hints)     | 2 min | Skip if short on time                   |
| 14   | BONUS 2: Today's Character の/ノ    | 2 min | Trace, find, match                      |
| 15   | Mission Complete                  | 1 min |                                         |

Travel conversation also appears in prestudy (plain, no highlights).

**Core: ~28 min / With bonus: ~32 min** (planning for 25 min actual class time)

---

### PAGE 1 — Greeting & Intro


```
+-------------------------------------------------------------------------+
|                                                                         |
|  あります・います                                                        |
|  Is There...? — There is / There are                                    |
|                                                                         |
|  ① 〜さん、こんにちは！おかえりなさい。                                    |
|     "Hi ~, welcome back!"                                               |
|                                                                         |
|  ② きょうもよろしくおねがいします。                                       |
|     "Let's have a great lesson today."                                  |
|                                                                         |
|  ③ これをよんでください。                                                 |
|     "Please read this."                                                 |
|                                                                         |
|                                                                  PAGE 1 |
+-------------------------------------------------------------------------+
```

### PAGE 2 — Review: L1 + L2 + L3

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's review — translate each sentence into Japanese."              |
|    「ふくしゅうしましょう。にほんごにしてみてね。」                      |
|                                                                         |
|  REVIEW: LESSONS 1, 2 & 3                                               |
|  ──────────────────────                                                 |
|                                                                         |
|  ┌─ LESSON 1: です (I am / he is) ─────────────────────────┐            |
|  │                                                          │            |
|  │  PATTERN:  [person]は [noun / adjective]です。           │            |
|  │                                                          │            |
|  │  1. FILL IN:  わたしはがくせい______。                    │            |
|  │               "I am a student"                            │            |
|  │                                                          │            |
|  │  2. TRANSLATE:  He is kind.                              │            |
|  │     → ____________________________________              │            |
|  │                                                          │            |
|  │  ┌─ Q2 WORDS ─────────────────────────────────────┐     │            |
|  │  │  かれ(he)  しんせつ(kind)                        │     │            |
|  │  └─────────────────────────────────────────────────┘     │            |
|  └──────────────────────────────────────────────────────────┘            |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ┌─ LESSON 2: これ・それ・あれ (this / that / over there) ──┐            |
|  │                                                          │            |
|  │  PATTERN:  これ / それ / あれ は [noun]です。             │            |
|  │                                                          │            |
|  │  1. FILL IN:  ______はほんです。                          │            |
|  │               "This is a book"                            │            |
|  │                                                          │            |
|  │  2. TRANSLATE:  That is my pen.                          │            |
|  │     → ____________________________________              │            |
|  │                                                          │            |
|  │  ┌─ Q2 WORDS ─────────────────────────────────────┐     │            |
|  │  │  それ(that)  わたし(I)  ペン(pen)                │     │            |
|  │  └─────────────────────────────────────────────────┘     │            |
|  └──────────────────────────────────────────────────────────┘            |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ┌─ LESSON 3: どこ (where) ────────────────────────────────┐            |
|  │                                                          │            |
|  │  PATTERN:  [noun]は どこですか？                          │            |
|  │            [noun]は ここ / そこ / あそこです。             │            |
|  │                                                          │            |
|  │  1. FILL IN:  ほんは______ですか？                        │            |
|  │               "Where is the book?"                        │            |
|  │                                                          │            |
|  │  2. TRANSLATE:  The pen is there.                        │            |
|  │     → ____________________________________              │            |
|  │                                                          │            |
|  │  ┌─ Q2 WORDS ─────────────────────────────────────┐     │            |
|  │  │  ペン(pen)  そこ(there)                          │     │            |
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
|  1. There IS a [thing]  —  あります                                      |
|                                                                         |
|     • へやに テレビが あります。                                          |
|       There is a TV in the room.                                        |
|                                                                         |
|     • いえに ほんが あります。                                            |
|       There is a book at home.                                          |
|                                                                         |
|                                                                         |
|  2. There IS a [person/animal]  —  います                                 |
|                                                                         |
|     • きょうしつに せんせいが います。                                    |
|       There is a teacher in the classroom.                              |
|                                                                         |
|     • へやに ねこが います。                                              |
|       There is a cat in the room.                                       |
|                                                                         |
|                                                                         |
|     ┌─── REMEMBER ──────────────────────────────────────────┐           |
|     │  あります → for THINGS (book, pen, desk...)             │           |
|     │  います   → for LIVING things (people, animals)        │           |
|     └────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                  PAGE 3 |
+-------------------------------------------------------------------------+
```

### PAGE 4 — Pattern Drill A (あります — Things)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL A: あります (THINGS)                                      |
|  ──────────────────────────────────                                     |
|                                                                         |
|  PATTERN:  [place]に [thing]が あります。                                 |
|            There is a [thing] at [place].                               |
|                                                                         |
|                                                                         |
|  ▸ "Let's read together. Copy my pronunciation closely — slow is OK."  |
|    「いっしょによみましょう。はつおんをよくまねしてね。                  |
|     ゆっくりでいいですよ。」                                            |
|                                                                         |
|  1. Read Together:                                                      |
|     * へやに テレビが あります。          A TV is in the room.            |
|     * きょうしつに とけいが あります。    A clock is in the classroom.   |
|     * いえに ほんが あります。            A book is at home.             |
|     * カフェに ペンが あります。          A pen is at the cafe.          |
|     * コンビニに ノートが あります。      A notebook is at the store.    |
|                                                                         |
|                                                                         |
|  ▸ "Fill in the blank and read the whole thing!"                        |
|    「くうらんにことばをいれて、ぜんぶよんでみましょう！」                |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * へやに テレビ（　　　）あります。             There's a TV...      |
|     * きょうしつに とけいが（　　　）。             There's a clock...   |
|     * いえ（　　　）ほんが あります。               There's a book...    |
|     * カフェに（　　　）があります。                There's a pen...     |
|     * コンビニ（　　　）ノートがあります。          There's a notebook...|
|                                                                         |
|                                                                         |
|  ▸ "Translate to Japanese — hints are OK."                              |
|    「にほんごにしてみましょう。ヒントをみてもいいですよ。」              |
|                                                                         |
|  3. Translate:                                                          |
|     * There is a phone in the room.                                     |
|       _____________________________________________________             |
|       (phone = でんわ / room = へや)                                      |
|                                                                         |
|     * There is a key at home.                                           |
|       _____________________________________________________             |
|       (key = かぎ / home = いえ)                                          |
|                                                                         |
|     * There is a notebook at the cafe.                                  |
|       _____________________________________________________             |
|       (notebook = ノート / cafe = カフェ)                                 |
|                                                                         |
|     * There is a clock in the classroom.                                |
|       _____________________________________________________             |
|       (clock = とけい / classroom = きょうしつ)                           |
|                                                                         |
|     * There is a book at the convenience store.                         |
|       _____________________________________________________             |
|       (book = ほん / convenience store = コンビニ)                        |
|                                                                         |
|                                                                         |
|  ▸ "Make your own! Say something that exists in your room right now."   |
|    「じぶんのぶんをつくってみましょう！                                  |
|     いまのへやにあるものをいってみてね。」                              |
|                                                                         |
|  4. Make Your Own:                                                      |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 4 |
+-------------------------------------------------------------------------+
```

### PAGE 5 — Pattern Drill B (います — People & Animals)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL B: います (PEOPLE / ANIMALS)                               |
|  ────────────────────────────────────────                                |
|                                                                         |
|  PATTERN:  [place]に [person/animal]が います。                           |
|            There is a [person/animal] at [place].                       |
|                                                                         |
|                                                                         |
|  ▸ "Next pattern. Same idea — copy my pronunciation closely."           |
|    「つぎのパターンです。おなじように、はつおんをまねしてみてね。」      |
|                                                                         |
|  1. Read Together:                                                      |
|     * きょうしつに せんせいが います。    A teacher is in the classroom. |
|     * へやに ねこが います。              A cat is in the room.          |
|     * カフェに ともだちが います。        A friend is in the cafe.        |
|     * いえに いぬが います。              A dog is at home.              |
|     * こうえんに こどもが います。        A child is in the park.        |
|                                                                         |
|                                                                         |
|  ▸ "Fill in the blank and read the whole thing!"                        |
|    「くうらんにことばをいれて、ぜんぶよんでみましょう！」                |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * きょうしつに せんせい（　　　）います。       There's a teacher... |
|     * へやに（　　　）がいます。                    There's a cat...     |
|     * カフェ（　　　）ともだちがいます。            There's a friend...  |
|     * いえにいぬが（　　　）。                      There's a dog...     |
|     * こうえん（　　　）こどもがいます。            There's a child...   |
|                                                                         |
|                                                                         |
|  ▸ "Translate to Japanese."                                             |
|    「にほんごにしてみましょう。」                                        |
|                                                                         |
|  3. Translate:                                                          |
|     * There is a teacher in the room.                                   |
|       _____________________________________________________             |
|       (teacher = せんせい / room = へや)                                  |
|                                                                         |
|     * There is a dog in the park.                                       |
|       _____________________________________________________             |
|       (dog = いぬ / park = こうえん)                                      |
|                                                                         |
|     * There is a friend at home.                                        |
|       _____________________________________________________             |
|       (friend = ともだち / home = いえ)                                   |
|                                                                         |
|     * There is a cat at the cafe.                                       |
|       _____________________________________________________             |
|       (cat = ねこ / cafe = カフェ)                                        |
|                                                                         |
|     * There is a child in the classroom.                                |
|       _____________________________________________________             |
|       (child = こども / classroom = きょうしつ)                           |
|                                                                         |
|                                                                         |
|  ▸ "Make your own! Say who is in the room with you right now."          |
|    「じぶんのぶんをつくってみましょう！                                  |
|     いま、だれがへやにいますか？」                                       |
|                                                                         |
|  4. Make Your Own:                                                      |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 5 |
+-------------------------------------------------------------------------+
```

### PAGE 6 — Vocab Recall

```
+-------------------------------------------------------------------------+
|                                                                         |
|  VOCAB RECALL                                                           |
|  ────────────                                                           |
|                                                                         |
|  ▸ "Say these in Japanese — from memory!"                               |
|    「にほんごでいってみましょう。おぼえているかな？」                    |
|                                                                         |
|                                                                         |
|  PLACES                                                                 |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  room                │  __________           │                        |
|  │  classroom           │  __________           │                        |
|  │  home                │  __________           │                        |
|  │  cafe                │  __________           │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|  THINGS                                                                 |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  TV                  │  __________           │                        |
|  │  pen                 │  __________           │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|  PEOPLE & ANIMALS                                                       |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  teacher             │  __________           │                        |
|  │  friend              │  __________           │                        |
|  │  cat                 │  __________           │                        |
|  │  dog                 │  __________           │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|  KEY VERBS                                                              |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  there is (thing)    │  __________           │                        |
|  │  there is (person)   │  __________           │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|                                                                  PAGE 6 |
+-------------------------------------------------------------------------+
```

### PAGE 7 — Short Dialogues

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
|            Is there a book in the room?                                 |
|  Tutor:    はい、へやにほんがあります。                                    |
|            Yes, there is a book in the room.                            |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  へや(room)  ほん(book)                  │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "I'll ask. Answer in Japanese."                                      |
|    「わたしがききます。にほんごでこたえてね。」                          |
|                                                                         |
|  DIALOGUE 2:                                                            |
|  Tutor:    へやに ねこが いますか？                                       |
|            Is there a cat in the room?                                  |
|  Student:  [_________________________________]                          |
|            Yes, there is a cat in the room.                             |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  へや(room)  ねこ(cat)                   │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Your turn — ask in Japanese."                                       |
|    「あなたのばんです。にほんごできいてみてね。」                        |
|                                                                         |
|  DIALOGUE 3:                                                            |
|  Student:  [_________________________________]                          |
|            Is there a pen at the cafe?                                  |
|  Tutor:    はい、カフェにペンがあります。                                  |
|            Yes, there is a pen at the cafe.                             |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  カフェ(cafe)  ペン(pen)                  │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Last one! I'll ask — answer in Japanese."                           |
|    「さいごです！しつもんします、にほんごでこたえてね。」                |
|                                                                         |
|  DIALOGUE 4:                                                            |
|  Tutor:    きょうしつに せんせいが いますか？                              |
|            Is there a teacher in the classroom?                         |
|  Student:  [_________________________________]                          |
|            Yes, there is a teacher in the classroom.                    |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  きょうしつ(classroom)  せんせい(teacher)│                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|                                                                  PAGE 7 |
+-------------------------------------------------------------------------+
```

### PAGE 8 — Guided Conversation

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
|  │  Alex is visiting Yuki's house for the first time.         │         |
|  │  アレックスがゆきのいえにはじめてきました。                   │         |
|  └────────────────────────────────────────────────────────────┘         |
|                                                                         |
|                                                                         |
|  ALEX:   わあ、おおきいいえですね！テレビがありますか？                    |
|          Wow, what a big house! Is there a TV?                          |
|                                                                         |
|  YUKI:   はい、へやにテレビがあります。                                    |
|          Yes, there is a TV in the room.                                |
|                                                                         |
|  ALEX:   ねこがいますか？                                                 |
|          Do you have a cat? (lit. Is there a cat?)                      |
|                                                                         |
|  YUKI:   はい、へやにねこがいます。                                        |
|          Yes, there's a cat in the room.                                |
|                                                                         |
|  ALEX:   かわいい！おかあさんはいますか？                                  |
|          Cute! Is your mom here?                                        |
|                                                                         |
|  YUKI:   いいえ、いまはいません。カフェにいます。                          |
|          No, she's not here right now. She's at a cafe.                 |
|                                                                         |
|  ALEX:   そうですか。ありがとう、ゆきさん！                                |
|          I see. Thanks, Yuki!                                           |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Great job! Now let's swap. This time I'll be Alex."                 |
|    「じょうずですね！こうたいしましょう。                                |
|     こんどはわたしがアレックスです。」                                  |
|                                                                         |
|                                                                  PAGE 8 |
+-------------------------------------------------------------------------+
```

### PAGE 9 — Memory Conversation

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Same conversation, but now from memory!                             |
|     I'll be Alex. You're Yuki — say the full sentence."                 |
|    「おなじかいわです。こんどはおぼえていってみましょう！                |
|     わたしがアレックスです。あなたはゆき                                |
|     — ぜんぶのぶんをいってください。」                                  |
|                                                                         |
|  CONVERSATION: MEMORY CHECK                                             |
|  --------------------------                                             |
|  Tutor = Alex / Student = Yuki                                          |
|                                                                         |
|                                                                         |
|  ALEX (tutor):   テレビがありますか？                                     |
|                  Is there a TV?                                         |
|                                                                         |
|  YUKI (you):     はい、へやにテレビが______。                              |
|                  Yes, there is a TV in the room.                        |
|                                                                         |
|  ALEX (tutor):   ねこがいますか？                                         |
|                  Is there a cat?                                        |
|                                                                         |
|  YUKI (you):     はい、へやにねこが______。                                |
|                  Yes, there's a cat in the room.                        |
|                                                                         |
|  ALEX (tutor):   おかあさんはいますか？                                   |
|                  Is your mom here?                                      |
|                                                                         |
|  YUKI (you):     いいえ、カフェに______。                                 |
|                  No, she's at a cafe.                                   |
|                                                                         |
|  ALEX (tutor):   そうですか。ありがとう！                                 |
|                  I see. Thanks!                                         |
|                                                                         |
|                                                                  PAGE 9 |
+-------------------------------------------------------------------------+
```

### PAGE 10 — Free Discussion

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
|  ROUND 1: WHAT'S IN YOUR ROOM?                                          |
|                                                                         |
|  Tutor:    「へやに なにが ありますか？」                                  |
|            "What's in your room?"                                       |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「へやに なにが ありますか？」                                  |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  テレビ(TV) つくえ(desk) ベッド(bed)                │               |
|     │  ほん(book) とけい(clock)                           │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─    |
|                                                                         |
|  ROUND 2: WHO'S AT HOME?                                                |
|                                                                         |
|  Tutor:    「いえに だれが いますか？」                                    |
|            "Who's at your home?"                                        |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「いえに だれが いますか？」                                    |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  おかあさん(mom) おとうさん(dad)                    │               |
|     │  ともだち(friend) ねこ(cat) いぬ(dog)                │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─    |
|                                                                         |
|  ROUND 3: WHAT'S AT YOUR FAVORITE CAFE?                                 |
|                                                                         |
|  Tutor:    「カフェに なにが ありますか？」                                |
|            "What's at your favorite cafe?"                              |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「カフェに なにが ありますか？」                                |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  ほん(book) ペン(pen) ノート(notebook)              │               |
|     │  でんわ(phone) とけい(clock)                        │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|                                                                 PAGE 10 |
+-------------------------------------------------------------------------+
```

### PAGE 11 — Roleplay

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ROLEPLAY                                                               |
|  ────────                                                               |
|  "Who and What Is in the Classroom?"                                    |
|                                                                         |
|  SCENARIO                                                               |
|  あなたはきょうしつにきました。                                           |
|  でも、いろいろなものとひとをさがしています！                             |
|  You've arrived at the classroom, but you're looking for things        |
|  AND a person!                                                          |
|                                                                         |
|  GOAL                                                                   |
|  せんせいにきいて、ぜんぶみつけましょう！                                 |
|  Ask the tutor where everything and everyone is!                        |
|                                                                         |
|  さがすもの：ほん、ペン、かばん                                           |
|  さがすひと：ともだち                                                    |
|  You're looking for: a book, a pen, a bag, AND a friend.                |
|                                                                         |
|  HINTS                                                                  |
|  ┌──────────────────────────────────────────────────────────┐           |
|  │  PATTERN                                                  │           |
|  │  ＿＿は ありますか？       Is there a ＿＿ (thing)?        │           |
|  │  ＿＿は いますか？         Is there a ＿＿ (person)?       │           |
|  │  WORDS                                                    │           |
|  │  ほん(book) ペン(pen) かばん(bag) ともだち(friend)          │           |
|  └──────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                 PAGE 11 |
+-------------------------------------------------------------------------+
```

### PAGE 12 — Travel in Japan

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Imagine you're at a Japanese convenience store!"                    |
|    「にほんのコンビニにいるとおもってね！」                              |
|                                                                         |
|  TRAVEL IN JAPAN: AT A CONVENIENCE STORE                                |
|  ────────────────────────────────────────                               |
|  You are a traveler. Fill in the blanks and say them out loud!          |
|                                                                         |
|  ┌─── CONTEXT / 状況 ─────────────────────────────────────────┐         |
|  │  You walk into a Japanese convenience store looking for    │         |
|  │  water, a snack, and a staff member who speaks English.    │         |
|  └────────────────────────────────────────────────────────────┘         |
|                                                                         |
|     ┌─── NEW WORDS ──────────────────────────────────────┐              |
|     │  みず (water)      おにぎり (rice ball)             │              |
|     │  スタッフ (staff)  えいご (English language)        │              |
|     │  すみません (excuse me)                              │              |
|     └─────────────────────────────────────────────────────┘              |
|                                                                         |
|                                                                         |
|  YOU:      すみません、みずは______か？                                   |
|            Excuse me, is there water?                                   |
|                                                                         |
|  STAFF:    はい、あそこにあります。                                       |
|            Yes, it's over there.                                        |
|                                                                         |
|  YOU:      おにぎりも______か？                                           |
|            Are there rice balls too?                                    |
|                                                                         |
|  STAFF:    はい、ここにおにぎりがあります。                                |
|            Yes, the rice balls are here.                                |
|                                                                         |
|  YOU:      えいごのスタッフは______か？                                   |
|            Is there any English-speaking staff?                         |
|                                                                         |
|  STAFF:    はい、あそこにいます！                                         |
|            Yes, they're over there!                                     |
|                                                                         |
|  YOU:      ありがとうございます！                                         |
|            Thank you very much!                                         |
|                                                                         |
|                                                                 PAGE 12 |
+-------------------------------------------------------------------------+
```

### PAGE 13 — Bonus 1: Translate (No Hints)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 1: TRANSLATE — NO HINTS!                                         |
|  ────────────────────────────────                                       |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  ▸ "Translate these — no hints!"                                        |
|    「ヒントなしでにほんごにしてみましょう！」                            |
|                                                                         |
|                                                                         |
|  1. There is a TV in the room.                                          |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  2. There is a cat in the room.                                         |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  3. Is there a pen at the cafe?                                         |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  4. There is a teacher in the classroom.                                |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  5. Is there a dog at home?                                             |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  6. There is a friend at the cafe.                                      |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|                                                                 PAGE 13 |
+-------------------------------------------------------------------------+
```

### PAGE 14 — Bonus 2: Today's Character — の / ノ (no)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 2: TODAY'S CHARACTER                                             |
|  ──────────────────────────                                             |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  ▸ "Let's learn one character today!"                                   |
|    「きょうはひとつ、もじをおぼえましょう！」                             |
|                                                                         |
|                                                                         |
|  ┌────────────────────────────────────────────┐                         |
|  │                                              │                         |
|  │   Hiragana:  の        Katakana:  ノ          │                         |
|  │   Sound:     no                               │                         |
|  │                                              │                         |
|  │   You already know の!                        │                         |
|  │   "わたしのほん" — the の connects two things  │                         |
|  │   (like "my book").                           │                         |
|  │                                              │                         |
|  └────────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  1. RECOGNITION — Which one is `no`?                                     |
|                                                                         |
|  ▸ "Can you find `no`? Point to it!"                                     |
|    「の はどれですか？ゆびでさしてね！」                                  |
|                                                                         |
|     a)  め       b)  の       c)  ぬ                                     |
|                                                                         |
|     Which one is `no`?                                                    |
|                                                                         |
|     a)  ソ       b)  ン       c)  ノ                                     |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  2. READ — Read these words out loud!                                   |
|                                                                         |
|  ▸ "Can you read these without romaji? Find the の!"                     |
|    「よめるかな？ の をみつけてね！」                                     |
|                                                                         |
|     • わたしのほん        my book                                        |
|     • せんせいのかばん    the teacher's bag                              |
|     • のみもの            drink                                          |
|     • ノート              notebook                                       |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  3. DRAW — Fill in the missing の/ノ!                                     |
|                                                                         |
|  ▸ "Draw the missing character to complete the word!"                   |
|    「の をかいて、ことばをかんせいさせてね！」                            |
|                                                                         |
|     Hiragana の:                                                        |
|     watashi no hon (my book)        =  わたし[   ]ほん                  |
|     sensei no kaban (teacher's bag) =  せんせい[   ]かばん              |
|     nomimono (drink)                =  [   ]みもの                      |
|                                                                         |
|     Katakana ノ:                                                        |
|     nooto (notebook)           =  [   ]ート                             |
|     nokku (knock)              =  [   ]ック                             |
|     pasokon (PC)               =  パソコ[   ]                           |
|                                                                         |
|                                                                 PAGE 14 |
+-------------------------------------------------------------------------+
```

### PAGE 15 — Mission Complete

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
|  │  │  │  PATTERN 1: ＿＿に ＿＿が あります。                 │            |
|  │  └──┘              (There is a THING at a PLACE)         │            |
|  │                                                          │            |
|  │  ┌──┐                                                    │            |
|  │  │  │  PATTERN 2: ＿＿に ＿＿が います。                   │            |
|  │  └──┘              (There is a PERSON/ANIMAL at a PLACE) │            |
|  │                                                          │            |
|  └─────────────────────────────────────────────────────────┘            |
|                                                                         |
|                                                                         |
|  ▸ "Let's read one more time. Perfect! See you next lesson!"            |
|    「さいごにもういちどよみましょう。かんぺき！                          |
|     つぎのレッスンであいましょう！」                                    |
|                                                                         |
|  KEY EXPRESSIONS — もういちどよんでみましょう！                           |
|  • へやにテレビがあります。          — There's a TV in the room.          |
|  • いえにほんがあります。            — There's a book at home.            |
|  • きょうしつにせんせいがいます。    — There's a teacher in the classroom.|
|  • へやにねこがいます。              — There's a cat in the room.         |
|                                                                         |
|                                                                 PAGE 15 |
+-------------------------------------------------------------------------+
```
