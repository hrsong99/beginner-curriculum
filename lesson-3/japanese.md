# Lesson 3: どこですか？ — Where Is It?

## Design Notes

**Changes from Lesson 2 based on tutor feedback (Andrew & Scott):**

- Added Lesson 2 review page at the start (~3 min)
- Pattern drills come BEFORE conversation (conversation felt too intense early)
- Short dialogues come BEFORE roleplay (scaffolding progression)
- Roleplay moved to BONUS page with full script (students didn't know what to do)
- Pages kept smaller for breathing room
- Vocab activity added as BONUS before Mission Complete (skip if short on time)
- Only TWO focused patterns (no あります/います — save for Lesson 4)

**Styling conventions (HTML implementation):**

- Warm romaji color (#c4b8a8) used for furigana `<rt>` text
- JP/EN paired layout uses `.pair` wrappers with `.jp` and `.en` child divs
- Inline fill-in-the-blank inputs use `.blank-input` class (bordered box, auto-sizing)
- Full-width answer inputs use `.blank-input-full` class
- Q:/A: grid layout (`.qa` + `.qa-label`) for review exercises — replaces Tutor:/Student: labels
- Help-word boxes use `.help-box` class (smaller border, indented)
- Dashed separators (`<hr class="separator">`) between sections throughout
- Interactive hanamaru (花丸) drawn on checkbox click via SVG animation — flower petals + spiral drawn with stroke-dashoffset animation
- Page 1 intro lines ①②③ are plain hiragana (no furigana)
- Roleplay HINTS box merges PHRASES and WORDS into one `.help-box`

## Lesson Flow (10 Core + 1 Bonus Page)


| Page | Activity                     | Time  | Notes                       |
| ---- | ---------------------------- | ----- | --------------------------- |
| 1    | Title & Pattern Intro        | 2 min |                             |
| 2    | Review: Lesson 2 Quick Check | 3 min | Review previous lesson      |
| 3    | Pattern Drill A (どこですか？)     | 3 min | Asking "where is ___?"      |
| 4    | Pattern Drill B (ここ/そこ/あそこ)  | 3 min | Answering "it's here/there" |
| 5    | Short Dialogues              | 3 min | Student asks first          |
| 6    | Guided Conversation          | 3 min | Moved AFTER drills          |
| 7    | Memory Conversation          | 3 min | Fill-in-the-blank of Page 6 |
| 8    | Free Discussion              | 3 min | Open practice               |
| 9    | Roleplay                     | 3 min | Constrained scenario        |
| 10   | BONUS: Vocab Challenge       | 2 min | Skip if short on time       |
| 11   | Mission Complete             | 2 min |                             |


**Core: ~28 min / With bonus: ~30 min**

---

### PAGE 1 — Title & Pattern Intro


```
+-------------------------------------------------------------------------+
|                                                                         |
|  どこですか？                                                             |
|  ここ・そこ・あそこ                                                       |
|  Where is it? — here / there / over there                               |
|                                                                         |
|  ① 〜さん、わたしはにほんごのせんせいです。〜ともうします。               |
|       これからよろしくおねがいします。                                    |
|     "~, I'm your Japanese teacher. My name is ~.                        |
|      Nice to meet you, let's have a great time!"                        |
|                                                                         |
|  ② それでは、きょうのじゅぎょうはじめます！                              |
|     "Alright, let's start today's lesson!"                              |
|                                                                         |
|  ③ これをよんでください。                                                 |
|     "Please read this."                                                 |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ┌─── OUTCOME / もくひょう ────────────────────────────────────┐         |
|  │  You can ask where things are and say where they are.       │         |
|  │  ものがどこにあるかきいたり、こたえられるようになります。      │         |
|  └─────────────────────────────────────────────────────────────┘         |
|                                                                         |
|                                                                         |
|  TODAY'S PATTERNS                                                       |
|  ================                                                       |
|                                                                         |
|  1. Asking Where (どこ)                                                  |
|                                                                         |
|     • [ほん]はどこですか？            Where is [the book]?               |
|     • [ペン]はどこですか？            Where is [the pen]?                |
|     • [かばん]はどこですか？          Where is [the bag]?                |
|                                                                         |
|                                                                         |
|  2. Answering Where (ここ・そこ・あそこ)                                  |
|                                                                         |
|     • [ほん]はここです。              [The book] is here. (near me)      |
|     • [ペン]はそこです。              [The pen] is there. (near you)     |
|     • [かばん]はあそこです。          [The bag] is over there.           |
|                                        (far from both)                  |
|                                                                         |
|                                                                  PAGE 1 |
+-------------------------------------------------------------------------+
```

### PAGE 2 — Review: Lesson 2 Quick Check

```
+-------------------------------------------------------------------------+
|                                                                         |
|  REVIEW: LESSON 2                                                       |
|  ────────────────                                                       |
|                                                                         |
|  1. What is this?                                                       |
|                                                                         |
|  Q:  これはなんですか？                                                   |
|      What is this?                                                      |
|                                                                         |
|  A:  これは[_______]です。                                               |
|                                                                         |
|                                                                         |
|     ┌─────────────────────────────────────────────────────┐             |
|     │  ほん(book)  ペン(pen)  ノート(notebook)             │             |
|     └─────────────────────────────────────────────────────┘             |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  2. Whose is that?                                                      |
|                                                                         |
|  Q:  それはだれのですか？                                                 |
|      Whose is that?                                                     |
|                                                                         |
|  A:  それは[_____]の[_______]です。                                      |
|      (two inline input boxes inside the sentence)                       |
|                                                                         |
|     ┌─────────────────────────────────────────────────────┐             |
|     │  わたし(my)  せんせい(teacher)  ともだち(friend)     │             |
|     └─────────────────────────────────────────────────────┘             |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  3. What is that over there?                                            |
|                                                                         |
|  Q:  あれはなんですか？                                                   |
|      What is that over there?                                           |
|                                                                         |
|  A:  あれは[_______]です。                                               |
|                                                                         |
|                                                                         |
|     ┌─────────────────────────────────────────────────────┐             |
|     │  かばん(bag)  とけい(clock)  いす(chair)             │             |
|     └─────────────────────────────────────────────────────┘             |
|                                                                         |
|                                                                  PAGE 2 |
+-------------------------------------------------------------------------+
```

### PAGE 3 — Pattern Drill A (Asking Where)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL: ASKING WHERE (どこ)                                     |
|  ──────────────────────────────────                                     |
|                                                                         |
|  PATTERN:  [noun]はどこですか？                                          |
|                                                                         |
|                                                                         |
|  1. Read Together:                                                      |
|     * 本はどこですか？                Where is the book?                 |
|     * ペンはどこですか？              Where is the pen?                  |
|     * かばんはどこですか？            Where is the bag?                  |
|                                                                         |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * 本は（　　　）ですか？          Where is the book?                 |
|     * （　　　）はどこですか？        Where is the pen?                  |
|     * ノートは（　　　）ですか？      Where is the notebook?             |
|                                                                         |
|                                                                         |
|  3. Translate:                                                          |
|     * Where is the phone?                                               |
|       _____________________________________________________             |
|       (phone = でんわ)                                                   |
|                                                                         |
|     * Where is the clock?                                               |
|       _____________________________________________________             |
|       (clock = とけい)                                                   |
|                                                                         |
|                                                                         |
|  4. Make Your Own:                                                      |
|     Ask where something is!                                             |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 3 |
+-------------------------------------------------------------------------+
```

### PAGE 4 — Pattern Drill B (Answering Where)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL: ANSWERING WHERE (ここ・そこ・あそこ)                     |
|  ───────────────────────────────────────────────────                     |
|                                                                         |
|  PATTERN:  [noun]は ここ/そこ/あそこ です。                               |
|                                                                         |
|     ここ   = here (near me)                                             |
|     そこ   = there (near you)                                           |
|     あそこ = over there (far from both)                                 |
|                                                                         |
|                                                                         |
|  1. Read Together:                                                      |
|     * 本はここです。                  The book is here.                  |
|     * ペンはそこです。                The pen is there.                  |
|     * かばんはあそこです。            The bag is over there.             |
|                                                                         |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * 本は（　　　）です。            The book is here.                  |
|     * ペンは（　　　）です。          The pen is there.                  |
|     * かばんは（　　　）です。        The bag is over there.             |
|                                                                         |
|                                                                         |
|  3. Translate:                                                          |
|     * The phone is here.                                                |
|       _____________________________________________________             |
|       (phone = でんわ / here = ここ)                                     |
|                                                                         |
|     * The clock is over there.                                          |
|       _____________________________________________________             |
|       (clock = とけい / over there = あそこ)                              |
|                                                                         |
|                                                                         |
|  4. Make Your Own:                                                      |
|     Point at something and say where it is!                             |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 4 |
+-------------------------------------------------------------------------+
```

### PAGE 5 — Short Dialogues

```
+-------------------------------------------------------------------------+
|                                                                         |
|  SHORT DIALOGUES                                                        |
|  ────────────────                                                       |
|                                                                         |
|  DIALOGUE 1:                                                            |
|  Student:  [_________________________________]                          |
|            Where is the book?                                           |
|  Tutor:    ほんはここです。                                               |
|            The book is here.                                            |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  ほん(book)  どこ(where)                 │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  DIALOGUE 2:                                                            |
|  Tutor:    ペンはどこですか？                                             |
|            Where is the pen?                                            |
|  Student:  [_________________________________]                          |
|            The pen is there.                                            |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  ペン(pen)  そこ(there)                  │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  DIALOGUE 3:                                                            |
|  Student:  [_________________________________]                          |
|            Where is the notebook?                                       |
|  Tutor:    ノートはあそこです。                                           |
|            The notebook is over there.                                  |
|                                                                         |
|     ┌─────────────────────────────────────────┐                         |
|     │  ノート(notebook)  どこ(where)            │                         |
|     └─────────────────────────────────────────┘                         |
|                                                                         |
|                                                                  PAGE 5 |
+-------------------------------------------------------------------------+
```

### PAGE 6 — Guided Conversation

```
+-------------------------------------------------------------------------+
|                                                                         |
|  CONVERSATION: GUIDED READING                                           |
|  ----------------------------                                           |
|                                                                         |
|  ┌─── CONTEXT / 状況 ─────────────────────────────────────────┐         |
|  │  Yuki can't find things in the classroom. Alex helps.      │         |
|  │  ゆきが教室で物を探しています。アレックスが手伝います。        │         |
|  └────────────────────────────────────────────────────────────┘         |
|                                                                         |
|                                                                         |
|  YUKI:   私のペンはどこですか？                                          |
|          Where is my pen?                                               |
|                                                                         |
|  ALEX:   ペンはそこです。                                                |
|          The pen is there.                                              |
|                                                                         |
|  YUKI:   あ、ありがとう！ノートはどこですか？                             |
|          Oh, thanks! Where is the notebook?                             |
|                                                                         |
|  ALEX:   ノートはここです。                                              |
|          The notebook is here.                                          |
|                                                                         |
|  YUKI:   じゃあ、私のかばんはどこですか？                                 |
|          Then, where is my bag?                                         |
|                                                                         |
|  ALEX:   かばんはあそこです。                                            |
|          The bag is over there.                                         |
|                                                                         |
|  YUKI:   ありがとう、アレックスさん！                                    |
|          Thanks, Alex!                                                  |
|                                                                         |
|                                                                  PAGE 6 |
+-------------------------------------------------------------------------+
```

### PAGE 7 — Memory Conversation

```
+-------------------------------------------------------------------------+
|                                                                         |
|  CONVERSATION: SPEED & MEMORY CHECK                                     |
|  -----------------------------------                                    |
|                                                                         |
|                                                                         |
|  YUKI:   私のペンはどこですか？                                          |
|          Where is my pen?                                               |
|                                                                         |
|  ALEX:   ペンは______です。                                                   |
|          (The pen is there.)                                            |
|                                                                         |
|  YUKI:   あ、ありがとう！ノートはどこですか？                             |
|          Oh, thanks! Where is the notebook?                             |
|                                                                         |
|  ALEX:   ノートは______です。                                                 |
|          (The notebook is here.)                                        |
|                                                                         |
|  YUKI:   じゃあ、私のかばんはどこですか？                                 |
|          Then, where is my bag?                                         |
|                                                                         |
|  ALEX:   かばんは______です。                                                 |
|          (The bag is over there.)                                       |
|                                                                         |
|  YUKI:   ありがとう、アレックスさん！                                    |
|          Thanks, Alex!                                                  |
|                                                                         |
|                                                                  PAGE 7 |
+-------------------------------------------------------------------------+
```

### PAGE 8 — Free Discussion

```
+-------------------------------------------------------------------------+
|                                                                         |
|  FREE DISCUSSION                                                        |
|  ────────────────                                                       |
|                                                                         |
|                                                                         |
|  ROUND 1: WHERE IS IT?                                                  |
|                                                                         |
|  Tutor:    「本はどこですか？」                                           |
|            "Where is the book?"                                         |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「ペンはどこですか？」                                         |
|            "Where is the pen?"                                          |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  本(book) ペン(pen) ノート(notebook)                │               |
|     │  ここ(here) そこ(there) あそこ(over there)         │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─    |
|                                                                         |
|  ROUND 2: POINT AND ANSWER                                              |
|                                                                         |
|  Tutor:    「かばんはどこですか？」                                       |
|            "Where is the bag?"                                          |
|                                                                         |
|  Student:  _____________________________________________                |
|                                                                         |
|  Student:  「とけいはどこですか？」                                       |
|            "Where is the clock?"                                        |
|                                                                         |
|  Tutor:    (answer naturally)                                           |
|                                                                         |
|     ┌─── WORDS ─────────────────────────────────────────┐               |
|     │  かばん(bag) とけい(clock) でんわ(phone) かぎ(key)  │               |
|     │  ここ(here) そこ(there) あそこ(over there)         │               |
|     └────────────────────────────────────────────────────┘               |
|                                                                         |
|                                                                  PAGE 8 |
+-------------------------------------------------------------------------+
```

### PAGE 9 — Roleplay

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ROLEPLAY                                                               |
|  ────────                                                               |
|  "Find Your 3 Lost Items!"                                              |
|                                                                         |
|  SCENARIO                                                               |
|  きょうしつで3つ(mittsu)のものをなくしました！                            |
|  You lost 3 things in the classroom!                                    |
|                                                                         |
|  GOAL                                                                   |
|  せんせいにきいて、3つぜんぶみつけましょう！                              |
|  Ask the tutor where each item is. Find all 3!                          |
|                                                                         |
|  なくしたもの：ペン、ノート、かばん                                       |
|  You lost your: pen, notebook, and bag.                                 |
|                                                                         |
|  HINTS                                                                  |
|  ┌──────────────────────────────────────────────────────────┐           |
|  │  PATTERN                                                  │           |
|  │  ＿＿はどこですか？         Where is ___?                 │           |
|  │  WORDS                                                    │           |
|  │  ペン(pen)  ノート(notebook)  かばん(bag)                 │           |
|  └──────────────────────────────────────────────────────────┘           |
|                                                                         |
|                                                                  PAGE 9 |
+-------------------------------------------------------------------------+
```

### PAGE 10 — Bonus: Vocab Challenge

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS: VOCAB CHALLENGE                                                 |
|  (Skip if you don't have time!)                                         |
|  ───────────────────────                                                |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  Can you match the Japanese to the English?                             |
|  日本語と英語を合わせましょう！                                          |
|                                                                         |
|                                                                         |
|  LOCATION WORDS:                                                        |
|  ここ       ・              ・  over there                              |
|  そこ       ・              ・  here                                    |
|  あそこ     ・              ・  where                                   |
|  どこ       ・              ・  there                                   |
|                                                                         |
|                                                                         |
|  THINGS (from this lesson):                                             |
|  本         ・              ・  pen                                     |
|  ペン       ・              ・  bag                                     |
|  ノート     ・              ・  book                                    |
|  かばん     ・              ・  notebook                                |
|                                                                         |
|                                                                         |
|  MORE THINGS (from drills & discussion):                                |
|  でんわ     ・              ・  key                                     |
|  かぎ       ・              ・  clock                                   |
|  とけい     ・              ・  water                                   |
|  みず       ・              ・  phone                                   |
|  いす       ・              ・  desk                                    |
|  つくえ     ・              ・  chair                                   |
|                                                                         |
|                                                                         |
|  LESSON 2 ←→ LESSON 3 CONNECTION:                                       |
|                                                                         |
|     これ (this thing)    ←→   ここ (this place / here)                  |
|     それ (that thing)    ←→   そこ (that place / there)                 |
|     あれ (that thing     ←→   あそこ (that place /                      |
|           over there)               over there)                         |
|                                                                         |
|                                                                         |
|                                                                 PAGE 10 |
+-------------------------------------------------------------------------+
```

### PAGE 11 — Mission Complete

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ミッションかんりょう！                                                   |
|  Mission Complete!                                                      |
|  ─────────────────                                                      |
|                                                                         |
|  きょうのミッション:                                                      |
|  ┌─────────────────────────────────────────────────────────┐            |
|  │                                                          │            |
|  │  ┌──┐                                                    │            |
|  │  │  │  PATTERN 1: ＿＿はどこですか？                      │            |
|  │  └──┘                                                    │            |
|  │                                                          │            |
|  │  ┌──┐                                                    │            |
|  │  │  │  PATTERN 2: ＿＿はここ/そこ/あそこです。             │            |
|  │  └──┘                                                    │            |
|  │                                                          │            |
|  └─────────────────────────────────────────────────────────┘            |
|                                                                         |
|                                                                         |
|  KEY EXPRESSIONS — もういちどよんでみましょう！                           |
|  • ほんはどこですか？          — Where is the book?                      |
|  • ほんはここです。            — The book is here.                       |
|  • ペンはそこです。            — The pen is there.                       |
|  • かばんはあそこです。        — The bag is over there.                  |
|                                                                         |
|                                                                 PAGE 11 |
+-------------------------------------------------------------------------+
```

