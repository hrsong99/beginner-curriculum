# Lesson 4: あります・います — Is There...?

## Design Notes

**Changes from Lesson 3 (extending 15 min → 25 min):**

- Cumulative review now covers L1 (です) + L2 (これ/それ/あれ) + L3 (どこ), not just the previous lesson
- NEW: Dedicated **Pronunciation Practice** page (Page 4) — light, short, "speak slowly and copy the tutor"
- NEW: **Vocab Recall** page moved from bonus to CORE (production, not recognition)
- Pattern drills now have **5 items per sub-activity** (was 3)
- Short Dialogues extended from 3 → 4
- Free Discussion extended from 2 → 3 rounds
- Roleplay now includes one animate target (a person) to force います
- Travel-in-Japan context: convenience store / restaurant (natural あります / います use)

**Two focused patterns:**

- Pattern A: `[place]に [thing]が あります` — for inanimate things
- Pattern B: `[place]に [person/animal]が います` — for living beings

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

## Lesson Flow (13 Core + 2 Bonus + Mission Complete)


| Page | Activity                          | Time  | Notes                                   |
| ---- | --------------------------------- | ----- | --------------------------------------- |
| 1    | Greeting & Intro                  | 1 min | Hello, let's start                      |
| 2    | Review: L1 + L2 + L3              | 4 min | Cumulative check                        |
| 3    | Today's Patterns                  | 2 min | あります / います                         |
| 4    | Pronunciation Practice            | 2 min | Light — slow & copy                     |
| 5    | Pattern Drill A (あります)          | 3 min | Things — 5 items per sub                |
| 6    | Pattern Drill B (います)            | 3 min | People/animals — 5 items per sub        |
| 7    | Vocab Recall                      | 2 min | Production (EN → JP)                    |
| 8    | Short Dialogues                   | 2 min | 4 dialogues                             |
| 9    | Guided Conversation               | 2 min | Classroom / cafe scene                  |
| 10   | Memory Conversation               | 2 min | Fill-in of Page 9                       |
| 11   | Free Discussion                   | 2 min | 3 rounds                                |
| 12   | Roleplay                          | 2 min | Find 3 things + 1 person                |
| 13   | Travel in Japan                   | 2 min | Convenience store / restaurant          |
| 14   | BONUS 1: Translate (no hints)     | 2 min | Skip if short on time                   |
| 15   | BONUS 2: Today's Character の/ノ    | 2 min | Trace, find, match                      |
| 16   | Mission Complete                  | 1 min |                                         |

Travel conversation also appears in prestudy (plain, no highlights).

**Core: ~29 min / With bonus: ~33 min** (planning for 25 min actual class time)

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
|  ▸ "First, let's review everything we've learned so far."               |
|    「まず、これまでならったことをふくしゅうしましょう。」                |
|                                                                         |
|  REVIEW: LESSONS 1, 2 & 3                                               |
|  ──────────────────────                                                 |
|                                                                         |
|  1. LESSON 1 — です (I am / he is)                                       |
|                                                                         |
|  Tutor:    おしごとはなんですか？                                         |
|            What's your job?                                             |
|                                                                         |
|  Student:  わたしは[_________]です。                                      |
|            I am a ______.                                               |
|                                                                         |
|     ┌────────────────────────────────────┐                              |
|     │  がくせい(student)  せんせい(teacher) │                              |
|     │  いしゃ(doctor)  かいしゃいん(worker) │                              |
|     └────────────────────────────────────┘                              |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  2. LESSON 2 — これ・それ・あれ (this / that / that over there)           |
|                                                                         |
|  Tutor:    これはなんですか？                                              |
|            What is this?                                                |
|                                                                         |
|  Student:  [_______]はわたしのかばんです。                                 |
|            That is my bag.                                              |
|                                                                         |
|     ┌──────────────────────────────────┐                                |
|     │  これ = this    それ = that       │                                |
|     │  あれ = that over there          │                                |
|     └──────────────────────────────────┘                                |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  3. LESSON 3 — どこ (where)                                               |
|                                                                         |
|  Tutor:    ペンはどこですか？                                              |
|            Where is the pen?                                            |
|                                                                         |
|  Student:  ペンは[_______]です。                                          |
|            The pen is _______.                                          |
|                                                                         |
|     ┌──────────────────────────────────┐                                |
|     │  ここ(here) そこ(there)           │                                |
|     │  あそこ(over there)               │                                |
|     └──────────────────────────────────┘                                |
|                                                                         |
|                                                                  PAGE 2 |
+-------------------------------------------------------------------------+
```

### PAGE 3 — Today's Patterns

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's read today's patterns together! Repeat after me."             |
|    「きょうのパターンをいっしょによみましょう！                          |
|     わたしのあとにリピートしてください。」                              |
|                                                                         |
|  TODAY'S PATTERNS                                                       |
|  ================                                                       |
|                                                                         |
|  1. There IS a [thing]  —  あります                                      |
|                                                                         |
|     • つくえのうえに ほんが あります。                                    |
|       There is a book on the desk.                                      |
|                                                                         |
|     • かばんのなかに ペンが あります。                                    |
|       There is a pen in the bag.                                        |
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

### PAGE 4 — Pronunciation Practice

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PRONUNCIATION PRACTICE                                                 |
|  ──────────────────────                                                 |
|                                                                         |
|  ▸ "Let's practice saying today's patterns clearly.                     |
|     Speak slowly — copy my pronunciation as closely as you can.         |
|     Don't rush! Smooth is fast."                                        |
|    「きょうのパターンをきれいにいってみましょう。                         |
|     ゆっくりはなしてください。                                           |
|     わたしのはつおんをよくきいて、まねしてみてね！」                    |
|                                                                         |
|                                                                         |
|  Listen first. Then say it slowly with me.                              |
|                                                                         |
|                                                                         |
|  1.  あ・り・ま・す                                                      |
|      a - ri - ma - su                                                   |
|                                                                         |
|  2.  い・ま・す                                                          |
|      i - ma - su                                                        |
|                                                                         |
|  3.  つくえのうえに ほんが あります。                                     |
|      tsukue no ue ni, hon ga arimasu.                                   |
|                                                                         |
|  4.  きょうしつに せんせいが います。                                     |
|      kyoushitsu ni, sensei ga imasu.                                    |
|                                                                         |
|                                                                         |
|     ┌─── TIPS ──────────────────────────────────────────────┐           |
|     │  • Every syllable takes the same amount of time        │           |
|     │  • The "u" in ます is very soft (almost "mas")          │           |
|     │  • Don't stress any syllable — stay flat                │           |
|     └────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                  PAGE 4 |
+-------------------------------------------------------------------------+
```

### PAGE 5 — Pattern Drill A (あります — Things)

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
|  ▸ "Let's read together. Repeat after me."                              |
|    「いっしょによみましょう。わたしのあとにリピートしてください。」      |
|                                                                         |
|  1. Read Together:                                                      |
|     * つくえのうえに ほんが あります。    A book is on the desk.         |
|     * かばんのなかに ペンが あります。    A pen is in the bag.           |
|     * へやに テレビが あります。          A TV is in the room.            |
|     * つくえのうえに とけいが あります。  A clock is on the desk.        |
|     * いすのしたに かばんが あります。    A bag is under the chair.       |
|                                                                         |
|                                                                         |
|  ▸ "Fill in the blank and read the whole thing!"                        |
|    「くうらんにことばをいれて、ぜんぶよんでみましょう！」                |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * つくえのうえに ほん（　　　）あります。       There's a book...    |
|     * かばんのなかに ペンが（　　　）。             There's a pen...     |
|     * へや（　　　）テレビが あります。             There's a TV...      |
|     * いすのしたに（　　　）があります。            There's a bag...     |
|     * つくえのうえ（　　　）とけいがあります。      There's a clock...   |
|                                                                         |
|                                                                         |
|  ▸ "Try turning the English into Japanese. You can look at the hint."   |
|    「えいごをにほんごにしてみてください。ヒントをみてもいいですよ。」    |
|                                                                         |
|  3. Translate:                                                          |
|     * There is a phone on the desk.                                     |
|       _____________________________________________________             |
|       (phone = でんわ / on the desk = つくえのうえ)                       |
|                                                                         |
|     * There is a key in the bag.                                        |
|       _____________________________________________________             |
|       (key = かぎ / in the bag = かばんのなか)                            |
|                                                                         |
|     * There is a notebook on the desk.                                  |
|       _____________________________________________________             |
|       (notebook = ノート)                                                |
|                                                                         |
|     * There is a clock in the room.                                     |
|       _____________________________________________________             |
|       (in the room = へや)                                              |
|                                                                         |
|     * There is a book under the chair.                                  |
|       _____________________________________________________             |
|       (under the chair = いすのした)                                     |
|                                                                         |
|                                                                         |
|  ▸ "Make your own! Say something that exists in your room right now."   |
|    「じぶんのぶんをつくってみましょう！                                  |
|     いまのへやにあるものをいってみてね。」                              |
|                                                                         |
|  4. Make Your Own:                                                      |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 5 |
+-------------------------------------------------------------------------+
```

### PAGE 6 — Pattern Drill B (います — People & Animals)

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
|  ▸ "Next pattern. Let's read together."                                 |
|    「つぎのパターンです。いっしょによみましょう。」                      |
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
|  ▸ "Try turning the English into Japanese."                             |
|    「えいごをにほんごにしてみてください。」                              |
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
|     * There is a cat under the chair.                                   |
|       _____________________________________________________             |
|       (cat = ねこ)                                                       |
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
|                                                                  PAGE 6 |
+-------------------------------------------------------------------------+
```

### PAGE 7 — Vocab Recall

```
+-------------------------------------------------------------------------+
|                                                                         |
|  VOCAB RECALL                                                           |
|  ────────────                                                           |
|                                                                         |
|  ▸ "Can you say these in Japanese? Don't peek at your notes —           |
|     try from memory first!"                                             |
|    「にほんごでいえるかな？                                              |
|     ノートをみないで、おぼえているかためしてみよう！」                  |
|                                                                         |
|                                                                         |
|  PLACES                                                                 |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  on the desk         │  __________           │                        |
|  │  in the bag          │  __________           │                        |
|  │  in the room         │  __________           │                        |
|  │  under the chair     │  __________           │                        |
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
|                                                                  PAGE 7 |
+-------------------------------------------------------------------------+
```

### PAGE 8 — Short Dialogues

```
+-------------------------------------------------------------------------+
|                                                                         |
|  SHORT DIALOGUES                                                        |
|  ────────────────                                                       |
|                                                                         |
|  ▸ "Try asking the question in Japanese."                               |
|    「にほんごでしつもんしてみてください。」                              |
|                                                                         |
|  DIALOGUE 1:                                                            |
|  Student:  [_________________________________]                          |
|            Is there a book on the desk?                                 |
|  Tutor:    はい、つくえのうえにほんがあります。                            |
|            Yes, there is a book on the desk.                            |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  つくえのうえ(on the desk)  ほん(book)    │                         |
|     │  〜がありますか？(is there...?)           │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "I'll ask the question. Answer in Japanese."                         |
|    「わたしがしつもんします。にほんごでこたえてください。」              |
|                                                                         |
|  DIALOGUE 2:                                                            |
|  Tutor:    へやに ねこが いますか？                                       |
|            Is there a cat in the room?                                  |
|  Student:  [_________________________________]                          |
|            Yes, there is a cat in the room.                             |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  へや(room)  ねこ(cat)  います(is)       │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Your turn. Try asking in Japanese."                                 |
|    「あなたのばんです。にほんごできいてみてね。」                        |
|                                                                         |
|  DIALOGUE 3:                                                            |
|  Student:  [_________________________________]                          |
|            Is there a pen in the bag?                                   |
|  Tutor:    はい、かばんのなかにペンがあります。                            |
|            Yes, there is a pen in the bag.                              |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  かばんのなか(in the bag)  ペン(pen)     │                         |
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
|                                                                  PAGE 8 |
+-------------------------------------------------------------------------+
```

### PAGE 9 — Guided Conversation

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
|  ALEX:   わあ、おおきいへやですね！テレビがありますか？                    |
|          Wow, what a big room! Is there a TV?                           |
|                                                                         |
|  YUKI:   はい、あそこにテレビがあります。                                 |
|          Yes, the TV is over there.                                     |
|                                                                         |
|  ALEX:   ねこがいますか？                                                 |
|          Do you have a cat? (lit. Is there a cat?)                      |
|                                                                         |
|  YUKI:   はい、いすのしたにねこがいます。                                 |
|          Yes, there's a cat under the chair.                            |
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
|                                                                  PAGE 9 |
+-------------------------------------------------------------------------+
```

### PAGE 10 — Memory Conversation

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
|  YUKI (you):     はい、あそこに______があります。                         |
|                                                                         |
|  ALEX (tutor):   ねこがいますか？                                         |
|                  Is there a cat?                                        |
|                                                                         |
|  YUKI (you):     はい、いすのしたに______がいます。                       |
|                                                                         |
|  ALEX (tutor):   おかあさんはいますか？                                   |
|                  Is your mom here?                                      |
|                                                                         |
|  YUKI (you):     いいえ、カフェに______。                                 |
|                                                                         |
|  ALEX (tutor):   そうですか。ありがとう！                                 |
|                  I see. Thanks!                                         |
|                                                                         |
|                                                                 PAGE 10 |
+-------------------------------------------------------------------------+
```

### PAGE 11 — Free Discussion

```
+-------------------------------------------------------------------------+
|                                                                         |
|  FREE DISCUSSION                                                        |
|  ────────────────                                                       |
|                                                                         |
|  ▸ "I'll ask you a question. You answer.                                |
|     Then ask me the same question back!"                                |
|    「わたしがしつもんします。こたえてください。                          |
|     そのあと、おなじしつもんをわたしにしてね！」                        |
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
|  ROUND 3: WHAT'S ON YOUR DESK?                                          |
|                                                                         |
|  Tutor:    「つくえのうえに なにが ありますか？」                          |
|            "What's on your desk?"                                       |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「つくえのうえに なにが ありますか？」                          |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  ほん(book) ペン(pen) ノート(notebook)              │               |
|     │  でんわ(phone) とけい(clock)                        │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|                                                                 PAGE 11 |
+-------------------------------------------------------------------------+
```

### PAGE 12 — Roleplay

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
|  │  つくえのうえ / いすのした / あそこ / ここ                  │           |
|  └──────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                 PAGE 12 |
+-------------------------------------------------------------------------+
```

### PAGE 13 — Travel in Japan

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's use what we learned — imagine you're at a Japanese            |
|     convenience store!"                                                 |
|    「きょうならったことをつかってみましょう                              |
|     — にほんのコンビニにいるとおもってね！」                            |
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
|                                                                 PAGE 13 |
+-------------------------------------------------------------------------+
```

### PAGE 14 — Bonus 1: Translate (No Hints)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 1: TRANSLATE — NO HINTS!                                         |
|  ────────────────────────────────                                       |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  ▸ "Can you translate these without any hints? Let's try!"              |
|    「ヒントなしでにほんごにできるかな？やってみよう！」                  |
|                                                                         |
|                                                                         |
|  1. There is a book on the desk.                                        |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  2. There is a cat in the room.                                         |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  3. Is there a pen in the bag?                                          |
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
|                                                                 PAGE 14 |
+-------------------------------------------------------------------------+
```

### PAGE 15 — Bonus 2: Today's Character — の / ノ (no)

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
|  │   "つくえのうえ" — the の connects two things. │                         |
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
|     • つくえのうえ        on the desk                                    |
|     • かばんのなか        in the bag                                     |
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
|     tsukue no ue (on the desk) =  つくえ[   ]うえ                       |
|     kaban no naka (in the bag) =  かばん[   ]なか                       |
|     nomimono (drink)           =  [   ]みもの                           |
|                                                                         |
|     Katakana ノ:                                                        |
|     nooto (notebook)           =  [   ]ート                             |
|     nokku (knock)              =  [   ]ック                             |
|     pasokon (PC)               =  パソコ[   ]                           |
|                                                                         |
|                                                                 PAGE 15 |
+-------------------------------------------------------------------------+
```

### PAGE 16 — Mission Complete

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "You did great today! Amazing! Let's check them off together."       |
|    「きょうはとてもじょうずでした！すごい！                              |
|     いっしょにチェックしましょう。」                                    |
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
|  • つくえのうえにほんがあります。    — There's a book on the desk.       |
|  • かばんのなかにペンがあります。    — There's a pen in the bag.          |
|  • きょうしつにせんせいがいます。    — There's a teacher in the classroom.|
|  • へやにねこがいます。              — There's a cat in the room.         |
|                                                                         |
|                                                                 PAGE 16 |
+-------------------------------------------------------------------------+
```
