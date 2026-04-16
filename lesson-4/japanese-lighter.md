# Lesson 4: あります・います — Is There...? (Lighter Class Version)

## Design Notes

**Goal of this duplicate:** keep the same grammar target, but reduce burnout for absolute beginners by replacing some full-sentence production with **recognition, guided writing, multiple choice, and image-supported tasks**.

**What changed from the original Lesson 4:**

- Keep the same two focused patterns:
  - Pattern A: `[place]に [thing]が あります`
  - Pattern B: `[place]に [person/animal]が います`
- Keep the same travel/usefulness payoff: room / classroom / cafe / convenience store
- Reduce the number of pages where the student must create a full sentence from zero
- Add **choice-first tasks**: choose first, then read aloud
- Add **micro-writing**: one blank, one particle, one verb, or short rebuild instead of long translation
- Add **image-supported slides** so the picture carries some of the cognitive load
- Add **classification tasks** (`あります` vs `います`, thing vs living thing)
- Keep one dialogue page, one guided conversation page, one roleplay/travel payoff page
- Preserve a teacher-led classroom feel without depending on free chat for “downtime”

**Pedagogical direction for this version:**

- For absolute beginners, “lighter” should mean **less open production**, not necessarily more casual conversation.
- The class should feel like: **notice → choose → fill → read → small production**.
- Prestudy-style tasks are intentionally brought into class because they are lower-stress but still useful.
- Images should be added on the corresponding HTML slides where marked below with `[IMAGE SUGGESTION]`.

**Hint principles:**

- Hint boxes can include vocab and limited answer choices.
- For lighter pages, multiple choice and one-word completion are preferred over open translation.
- Full open production should appear later in the lesson, after several supported reps.

**Styling conventions (carry over from Lesson 3 / current Lesson 4):**

- Warm romaji color (#c4b8a8) used for furigana `<rt>` text
- JP/EN paired layout uses `.pair` wrappers with `.jp` and `.en` child divs
- Inline fill-in-the-blank inputs use `.blank-input` class
- Full-width answer inputs use `.blank-input-full` class
- Help-word / answer-choice boxes use `.help-box` class
- Dashed separators (`<hr class="separator">`) between sections
- Interactive hanamaru on Mission Complete checkbox click
- Tutor script notation: `▸ "English text" ／ 「にほんご」`

## Lesson Flow (15 Core + 2 Bonus)

| Page | Activity                              | Time  | Notes |
| ---- | ------------------------------------- | ----- | ----- |
| 1    | Greeting & Intro                      | 1 min | Hello, let's start |
| 2    | Review: L1 + L2 + L3                  | 2 min | Keep first-timer-friendly scaffolding |
| 3    | Today's Patterns                      | 3 min | あります / います |
| 4    | Visual Warm-up: Choose the Sentence   | 2 min | image + multiple choice |
| 5    | Pattern Drill A Lite (あります)        | 3 min | guided blanks + fewer open translations |
| 6    | Pattern Drill B Lite (います)          | 3 min | guided blanks + fewer open translations |
| 7    | Quick Check: あります or います?        | 2 min | sort / choose / classify |
| 8    | Image Fill: Look and Complete         | 2 min | image + one blank |
| 9    | Short Dialogues                       | 2 min | still useful, but shorter pressure |
| 10   | Guided Conversation                   | 2 min | supported reading |
| 11   | Picture Hunt                          | 2 min | yes/no + short answer from image |
| 12   | Free Discussion Lite                  | 2 min | choice-first, then personal answer |
| 13   | Roleplay                              | 2 min | find items/person |
| 14   | Travel in Japan                       | 2 min | convenience store payoff |
| 15   | Bonus 1: Translate (No Hints)         | 2 min | skip if short on time |
| 16   | Bonus 2: Today's Character の/ノ       | 2 min | trace, find, match |
| 17   | Mission Complete                      | 1 min | round-up |

**Core: ~28 min / With bonus: ~32 min**

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

### PAGE 4 — Visual Warm-up: Choose the Sentence

```
+-------------------------------------------------------------------------+
|                                                                         |
|  VISUAL WARM-UP: CHOOSE THE SENTENCE                                    |
|  ───────────────────────────────────                                    |
|                                                                         |
|  ▸ "Look at the picture. Choose first, then read it aloud."             |
|    「えをみて、まずえらびましょう。えらんだらよんでみてね。」            |
|                                                                         |
|  [IMAGE SUGGESTION: simple room picture with a TV, book, and cat]       |
|                                                                         |
|  1. Which sentence matches the TV?                                      |
|     a) へやに テレビが あります。                                         |
|     b) へやに テレビが います。                                           |
|     c) へやに ねこが あります。                                           |
|                                                                         |
|  2. Which sentence matches the cat?                                     |
|     a) へやに ねこが あります。                                           |
|     b) へやに ねこが います。                                             |
|     c) へやに ほんが います。                                             |
|                                                                         |
|  3. Which sentence matches the book?                                    |
|     a) へやに ほんが あります。                                           |
|     b) へやに ほんが います。                                             |
|     c) へやに せんせいが あります。                                       |
|                                                                         |
|  ▸ "Good. Now read the correct sentence one more time."                 |
|    「いいですね。せいかいをもういちどよんでみましょう。」                |
|                                                                         |
|                                                                  PAGE 4 |
+-------------------------------------------------------------------------+
```

### PAGE 5 — Pattern Drill A Lite (あります — Things)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL A LITE: あります (THINGS)                                 |
|  ───────────────────────────────                                        |
|                                                                         |
|  PATTERN:  [place]に [thing]が あります。                                 |
|            There is a [thing] at [place].                               |
|                                                                         |
|  ▸ "Let's read together first."                                         |
|    「まず、いっしょによみましょう。」                                    |
|                                                                         |
|  1. Read Together:                                                      |
|     * へやに テレビが あります。                                          |
|     * きょうしつに とけいが あります。                                    |
|     * いえに ほんが あります。                                            |
|                                                                         |
|  ▸ "Now fill just one part."                                            |
|    「こんどは、ひとつだけいれてみましょう。」                            |
|                                                                         |
|  2. One-Blank Fill:                                                     |
|     * へやに テレビが（あります / います）。                              |
|     * きょうしつに とけいが（あります / います）。                        |
|     * いえ（に / が）ほんが あります。                                   |
|     * カフェに（ペン / ねこ）が あります。                               |
|                                                                         |
|  ▸ "Choose first, then read the whole sentence."                        |
|    「まずえらんで、そのあとぜんぶよみましょう。」                        |
|                                                                         |
|  3. Guided Writing:                                                     |
|     * There is a phone in the room.                                     |
|       へやに でんわが ____________________。                              |
|     * There is a key at home.                                           |
|       いえに かぎが ______________________。                              |
|     * There is a notebook at the cafe.                                  |
|       カフェに ノートが __________________。                              |
|                                                                         |
|  4. Tiny Personal Step:                                                 |
|     * へやに ______が あります。                                          |
|                                                                         |
|                                                                  PAGE 5 |
+-------------------------------------------------------------------------+
```

### PAGE 6 — Pattern Drill B Lite (います — People & Animals)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL B LITE: います (PEOPLE / ANIMALS)                         |
|  ─────────────────────────────────────────────                          |
|                                                                         |
|  PATTERN:  [place]に [person/animal]が います。                           |
|            There is a [person/animal] at [place].                       |
|                                                                         |
|  ▸ "Same idea. Read together first."                                    |
|    「おなじかたちです。まず、いっしょによみましょう。」                  |
|                                                                         |
|  1. Read Together:                                                      |
|     * きょうしつに せんせいが います。                                   |
|     * へやに ねこが います。                                             |
|     * いえに いぬが います。                                             |
|                                                                         |
|  ▸ "Now choose the right part."                                         |
|    「こんどは、あうものをえらびましょう。」                              |
|                                                                         |
|  2. One-Blank Fill:                                                     |
|     * きょうしつに せんせいが（います / あります）。                      |
|     * へやに（ねこ / テレビ）が います。                                 |
|     * カフェ（に / が）ともだちが います。                               |
|     * いえに いぬが（います / あります）。                                |
|                                                                         |
|  ▸ "Write just the ending."                                             |
|    「さいごのことばだけかいてみましょう。」                             |
|                                                                         |
|  3. Guided Writing:                                                     |
|     * There is a teacher in the room.                                   |
|       へやに せんせいが __________________。                              |
|     * There is a dog in the park.                                       |
|       こうえんに いぬが __________________。                              |
|     * There is a friend at home.                                        |
|       いえに ともだちが __________________。                              |
|                                                                         |
|  4. Tiny Personal Step:                                                 |
|     * いえに ______が います。                                            |
|                                                                         |
|                                                                  PAGE 6 |
+-------------------------------------------------------------------------+
```

### PAGE 7 — Quick Check: あります or います?

```
+-------------------------------------------------------------------------+
|                                                                         |
|  QUICK CHECK: あります or います?                                        |
|  ──────────────────────────────                                         |
|                                                                         |
|  ▸ "This is a quick check. No long answers."                            |
|    「かんたんなチェックです。ながいこたえはいりません。」                |
|                                                                         |
|  1. Choose the correct verb:                                            |
|     * へやに テレビが (あります / います)                                 |
|     * へやに ねこが (あります / います)                                   |
|     * きょうしつに せんせいが (あります / います)                         |
|     * カフェに ペンが (あります / います)                                 |
|                                                                         |
|  2. Put each word in the correct group:                                 |
|     あります → ほん / テレビ / ペン / ノート                              |
|     います   → ねこ / いぬ / せんせい / ともだち                         |
|                                                                         |
|  3. Mini contrast:                                                      |
|     * thing?   book  → __________________                                |
|     * living?  cat   → __________________                                |
|     * thing?   clock → __________________                                |
|     * living?  dog   → __________________                                |
|                                                                         |
|                                                                  PAGE 7 |
+-------------------------------------------------------------------------+
```

### PAGE 8 — Image Fill: Look and Complete

```
+-------------------------------------------------------------------------+
|                                                                         |
|  IMAGE FILL: LOOK AND COMPLETE                                          |
|  ─────────────────────────────                                          |
|                                                                         |
|  ▸ "Look at the picture and fill one blank."                            |
|    「えをみて、くうらんをひとつうめましょう。」                          |
|                                                                         |
|  [IMAGE SUGGESTION: classroom picture with teacher, clock, bag, cat]    |
|                                                                         |
|  1. きょうしつに せんせいが ______。                                       |
|     a) あります   b) います                                                |
|  2. きょうしつに とけいが ______。                                         |
|     a) あります   b) います                                                |
|  3. きょうしつに かばんが ______。                                         |
|     a) あります   b) います                                                |
|  4. きょうしつに ねこが ______。                                           |
|     a) あります   b) います                                                |
|  5. One short write:                                                    |
|     * Is there a bag in the classroom?                                  |
|       きょうしつに かばんが __________________ か？                        |
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
|            Is there a book in the room?                                 |
|  Tutor:    はい、へやにほんがあります。                                    |
|                                                                         |
|  DIALOGUE 2:                                                            |
|  Tutor:    へやに ねこが いますか？                                       |
|  Student:  [_________________________________]                          |
|            Yes, there is a cat in the room.                             |
|                                                                         |
|  DIALOGUE 3:                                                            |
|  Student:  [_________________________________]                          |
|            Is there a pen at the cafe?                                  |
|  Tutor:    はい、カフェにペンがあります。                                  |
|                                                                         |
|  ▸ "If needed, answer with just the ending first."                      |
|    「むずかしかったら、さいごのことばからでもいいですよ。」              |
|                                                                         |
|                                                                  PAGE 9 |
+-------------------------------------------------------------------------+
```

### PAGE 10 — Guided Conversation

```
+-------------------------------------------------------------------------+
|                                                                         |
|  CONVERSATION: GUIDED READING                                           |
|  ----------------------------                                           |
|                                                                         |
|  ▸ "Let's read together. I'll be Yuki, you be Alex."                    |
|    「いっしょによみましょう。わたしがゆきで、あなたがアレックスです。」  |
|                                                                         |
|  CONTEXT: Alex is visiting Yuki's house for the first time.             |
|                                                                         |
|  ALEX:   わあ、おおきいいえですね！テレビがありますか？                    |
|  YUKI:   はい、へやにテレビがあります。                                    |
|  ALEX:   ねこがいますか？                                                 |
|  YUKI:   はい、へやにねこがいます。                                        |
|  ALEX:   おかあさんはいますか？                                            |
|  YUKI:   いいえ、いまはいません。カフェにいます。                          |
|                                                                         |
|  ▸ "Second round: choose one line and read it again."                   |
|    「こんどは、すきなぶんをひとつえらんでもういちどよみましょう。」      |
|                                                                         |
|                                                                 PAGE 10 |
+-------------------------------------------------------------------------+
```

### PAGE 11 — Picture Hunt

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PICTURE HUNT                                                           |
|  ────────────                                                           |
|                                                                         |
|  ▸ "Look at the picture. Answer yes/no first, then full sentence."      |
|    「えをみて、まずはい・いいえでこたえましょう。できたら、                |
|     そのあとぶんでもいってみましょう。」                                 |
|                                                                         |
|  [IMAGE SUGGESTION: cafe picture with notebook, pen, friend, dog]       |
|                                                                         |
|  1. カフェに ノートが ありますか？                                         |
|     → はい / いいえ                                                      |
|     → Full sentence: _____________________________________              |
|  2. カフェに ともだちが いますか？                                         |
|     → はい / いいえ                                                      |
|     → Full sentence: _____________________________________              |
|  3. カフェに いぬが いますか？                                             |
|     → はい / いいえ                                                      |
|     → Full sentence: _____________________________________              |
|  4. カフェに テレビが ありますか？                                         |
|     → はい / いいえ                                                      |
|     → Full sentence: _____________________________________              |
|                                                                         |
|                                                                 PAGE 11 |
+-------------------------------------------------------------------------+
```

### PAGE 12 — Free Discussion Lite

```
+-------------------------------------------------------------------------+
|                                                                         |
|  FREE DISCUSSION LITE                                                   |
|  ────────────────────                                                   |
|                                                                         |
|  ▸ "First choose. Then say your own answer if you can."                 |
|    「まずえらびましょう。できたら、そのあとじぶんのこたえも               |
|     いってみてね。」                                                     |
|                                                                         |
|  ROUND 1: WHAT'S IN YOUR ROOM?                                          |
|  Choose one first:  テレビ / ベッド / つくえ / ほん                        |
|  Then say:  へやに ______が あります。                                    |
|                                                                         |
|  ROUND 2: WHO'S AT HOME?                                                |
|  Choose one first:  おかあさん / おとうさん / ともだち / ねこ / いぬ      |
|  Then say:  いえに ______が います。                                      |
|                                                                         |
|  ROUND 3: YOUR REAL ANSWER (OK to keep it short)                        |
|  * へやに なにが ありますか？                                              |
|  * いえに だれが いますか？                                                |
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
|  "Who and What Is in the Classroom?"                                    |
|                                                                         |
|  SCENARIO                                                               |
|  あなたはきょうしつにきました。                                           |
|  でも、いろいろなものとひとをさがしています！                             |
|                                                                         |
|  GOAL                                                                   |
|  せんせいにきいて、ぜんぶみつけましょう！                                 |
|                                                                         |
|  さがすもの：ほん、ペン、かばん                                           |
|  さがすひと：ともだち                                                    |
|                                                                         |
|  HINTS                                                                  |
|  ┌──────────────────────────────────────────────────────────┐           |
|  │  ＿＿は ありますか？       Is there a ＿＿ (thing)?        │           |
|  │  ＿＿は いますか？         Is there a ＿＿ (person)?       │           |
|  │  ほん(book) ペン(pen) かばん(bag) ともだち(friend)          │           |
|  └──────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                 PAGE 13 |
+-------------------------------------------------------------------------+
```

### PAGE 14 — Travel in Japan

```
+-------------------------------------------------------------------------+
|                                                                         |
|  TRAVEL IN JAPAN: AT A CONVENIENCE STORE                                |
|  ────────────────────────────────────────                               |
|                                                                         |
|  ▸ "Imagine you're at a Japanese convenience store!"                    |
|    「にほんのコンビニにいるとおもってね！」                              |
|                                                                         |
|  CONTEXT: You want water, a snack, and English-speaking staff.          |
|                                                                         |
|  YOU:      すみません、みずは______か？                                   |
|  STAFF:    はい、あそこにあります。                                       |
|                                                                         |
|  YOU:      おにぎりも______か？                                           |
|  STAFF:    はい、ここにおにぎりがあります。                                |
|                                                                         |
|  YOU:      えいごのスタッフは______か？                                   |
|  STAFF:    はい、あそこにいます！                                         |
|                                                                         |
|                                                                 PAGE 14 |
+-------------------------------------------------------------------------+
```

### PAGE 15 — Bonus 1: Translate (No Hints)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 1: TRANSLATE — NO HINTS!                                         |
|  ────────────────────────────────                                       |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  1. There is a TV in the room.                                          |
|     _____________________________________________________               |
|  2. There is a cat in the room.                                         |
|     _____________________________________________________               |
|  3. Is there a pen at the cafe?                                         |
|     _____________________________________________________               |
|  4. There is a teacher in the classroom.                                |
|     _____________________________________________________               |
|                                                                         |
|                                                                 PAGE 15 |
+-------------------------------------------------------------------------+
```

### PAGE 16 — Bonus 2: Today's Character — の / ノ (no)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 2: TODAY'S CHARACTER                                             |
|  ──────────────────────────                                             |
|                                                                         |
|  1. Which one is `no`?                                                  |
|     a) め   b) の   c) ぬ                                                |
|     a) ソ   b) ン   c) ノ                                                |
|                                                                         |
|  2. Read these words:                                                   |
|     * わたしのほん                                                      |
|     * せんせいのかばん                                                  |
|     * のみもの                                                          |
|     * ノート                                                            |
|                                                                         |
|  3. Fill in the missing の / ノ                                         |
|     * わたし[   ]ほん                                                   |
|     * せんせい[   ]かばん                                               |
|     * [   ]みもの                                                       |
|     * [   ]ート                                                         |
|                                                                         |
|                                                                 PAGE 16 |
+-------------------------------------------------------------------------+
```

### PAGE 17 — Mission Complete

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ミッションかんりょう！                                                   |
|  Mission Complete!                                                      |
|  ─────────────────                                                      |
|                                                                         |
|  きょうのミッション:                                                      |
|  ┌─────────────────────────────────────────────────────────┐            |
|  │  ┌──┐  PATTERN 1: ＿＿に ＿＿が あります。               │            |
|  │  └──┘  (There is a THING at a PLACE)                   │            |
|  │  ┌──┐  PATTERN 2: ＿＿に ＿＿が います。                 │            |
|  │  └──┘  (There is a PERSON/ANIMAL at a PLACE)           │            |
|  └─────────────────────────────────────────────────────────┘            |
|                                                                         |
|  ▸ "Today you did choosing, filling, reading, and some speaking."      |
|    「きょうは、えらぶ・うめる・よむ・はなす、ぜんぶできました！」       |
|                                                                         |
|  • へやにテレビがあります。                                               |
|  • いえにほんがあります。                                                 |
|  • きょうしつにせんせいがいます。                                         |
|  • へやにねこがいます。                                                   |
|                                                                         |
|                                                                 PAGE 17 |
+-------------------------------------------------------------------------+
```
