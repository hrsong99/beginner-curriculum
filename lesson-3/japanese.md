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

**Page restructure (v2):**

- Page 1 is greeting only — jump straight to review after hello
- Outcome + Today's Patterns moved to Page 3 (after review, before drills)
- Tutor scripts embedded inline with each activity (English first, Japanese below)

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
- Tutor script notation: `▸ "English text" ／ 「にほんご」` — embedded at point of use

## Lesson Flow (11 Core + 4 Bonus Pages)


| Page | Activity                     | Time  | Notes                          |
| ---- | ---------------------------- | ----- | ------------------------------ |
| 1    | Greeting & Intro             | 1 min | Hello, let's start             |
| 2    | Review: Lesson 2 Quick Check | 3 min | Reading exercise w/ blanks     |
| 3    | Today's Patterns             | 2 min | Patterns only (no goal box)    |
| 4    | Pattern Drill A (どこですか？)     | 3 min | Asking "where is ___?"         |
| 5    | Pattern Drill B (ここ/そこ/あそこ)  | 3 min | Answering "it's here/there"    |
| 6    | Short Dialogues              | 3 min | Student asks first             |
| 7    | Guided Conversation          | 3 min | Moved AFTER drills             |
| 8    | Memory Conversation          | 3 min | Fill-in-the-blank of Page 7    |
| 9    | Free Discussion              | 3 min | Open practice                  |
| 10   | Roleplay                     | 3 min | Constrained scenario           |
| 11   | Travel in Japan              | 3 min | Real-world application         |
| 12   | BONUS 1: Vocab Quiz          | 2 min | Skip if short on time          |
| 13   | BONUS 2: Translate (no hints)| 2 min | Skip if short on time          |
| 14   | BONUS 3: Today's Character   | 2 min | か/カ (ka) — trace, find, match |
| 15   | Mission Complete             | 2 min |                                |

Travel conversation also appears in prestudy (plain, no highlights).

**Core: ~30 min / With bonus: ~36 min**

---

### PAGE 1 — Greeting & Intro


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
|                                                                  PAGE 1 |
+-------------------------------------------------------------------------+
```

### PAGE 2 — Review: Lesson 2 Quick Check

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "First, let's review the previous lesson."                           |
|    「まず、まえのレッスンのふくしゅうをしましょう。」                    |
|                                                                         |
|  REVIEW: LESSON 2                                                       |
|  ────────────────                                                       |
|  Let's make sure we remember what we learned last time!                 |
|                                                                         |
|  1. What is this?                                                       |
|                                                                         |
|  Tutor:    これはなんですか？                                              |
|            What is this?                                                |
|                                                                         |
|  Student:  [_______]はほんです。                                          |
|            This is a book.                                              |
|                                                                         |
|     ┌──────────────────────┐                                            |
|     │  これ = this          │                                            |
|     └──────────────────────┘                                            |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  2. Whose is that?                                                      |
|                                                                         |
|  Tutor:    それはだれのですか？                                            |
|            Whose is that?                                               |
|                                                                         |
|  Student:  [_______]はわたしのペンです。                                   |
|            That is my pen.                                              |
|                                                                         |
|     ┌──────────────────────┐                                            |
|     │  それ = that          │                                            |
|     └──────────────────────┘                                            |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  3. What is that over there?                                            |
|                                                                         |
|  Tutor:    あれはなんですか？                                              |
|            What is that over there?                                     |
|                                                                         |
|  Student:  [_______]はかばんです。                                        |
|            That is a bag.                                               |
|                                                                         |
|     ┌──────────────────────────────┐                                    |
|     │  あれ = that over there      │                                    |
|     └──────────────────────────────┘                                    |
|                                                                         |
|                                                                  PAGE 2 |
+-------------------------------------------------------------------------+
```

### PAGE 3 — Today's Patterns

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's read together! Repeat after me."                              |
|    「いっしょによんでみましょう！わたしのあとにリピートしてください。」  |
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
|                                                                  PAGE 3 |
+-------------------------------------------------------------------------+
```

### PAGE 4 — Pattern Drill A (Asking Where)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  PATTERN DRILL: ASKING WHERE (どこ)                                     |
|  ──────────────────────────────────                                     |
|                                                                         |
|  PATTERN:  [noun]はどこですか？                                          |
|                                                                         |
|                                                                         |
|  ▸ "Let's read together. Repeat after me."                              |
|    「いっしょによみましょう。わたしのあとにリピートしてください。」      |
|                                                                         |
|  1. Read Together:                                                      |
|     * 本はどこですか？                Where is the book?                 |
|     * ペンはどこですか？              Where is the pen?                  |
|     * かばんはどこですか？            Where is the bag?                  |
|                                                                         |
|                                                                         |
|  ▸ "Fill in the blank and read the whole thing!"                        |
|    「くうらんにことばをいれて、ぜんぶよんでみましょう！」                |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * 本は（　　　）ですか？          Where is the book?                 |
|     * （　　　）はどこですか？        Where is the pen?                  |
|     * ノートは（　　　）ですか？      Where is the notebook?             |
|                                                                         |
|                                                                         |
|  ▸ "Try turning the English into Japanese. You can look at the hint."   |
|    「えいごをにほんごにしてみてください。ヒントをみてもいいですよ。」    |
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
|  ▸ "Try making your own sentence! Ask where something is."              |
|    「じぶんのぶんをつくってみましょう！なにかについてきいてみてね。」    |
|                                                                         |
|  4. Make Your Own:                                                      |
|     Ask where something is!                                             |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 4 |
+-------------------------------------------------------------------------+
```

### PAGE 5 — Pattern Drill B (Answering Where)

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
|  ▸ "Next pattern. Let's read together."                                 |
|    「つぎのパターンです。いっしょによみましょう。」                      |
|                                                                         |
|  1. Read Together:                                                      |
|     * 本はここです。                  The book is here.                  |
|     * ペンはそこです。                The pen is there.                  |
|     * かばんはあそこです。            The bag is over there.             |
|                                                                         |
|                                                                         |
|  ▸ "Fill in the blank and read the whole thing!"                        |
|    「くうらんにことばをいれて、ぜんぶよんでみましょう！」                |
|                                                                         |
|  2. Fill in the Blanks:                                                 |
|     * 本は（　　　）です。            The book is here.                  |
|     * ペンは（　　　）です。          The pen is there.                  |
|     * かばんは（　　　）です。        The bag is over there.             |
|                                                                         |
|                                                                         |
|  ▸ "Try turning the English into Japanese."                             |
|    「えいごをにほんごにしてみてください。」                              |
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
|  ▸ "Try making your own! Point at something and say where it is."       |
|    「じぶんのぶんをつくってみましょう！なにかをさしてこたえてね。」      |
|                                                                         |
|  4. Make Your Own:                                                      |
|     Point at something and say where it is!                             |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|                                                                  PAGE 5 |
+-------------------------------------------------------------------------+
```

### PAGE 6 — Short Dialogues

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
|  ▸ "I'll ask the question. Answer in Japanese."                         |
|    「わたしがしつもんします。にほんごでこたえてください。」              |
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
|  ▸ "Last one! Try asking in Japanese."                                  |
|    「さいごです！にほんごでしつもんしてみてください。」                  |
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
|                                                                  PAGE 6 |
+-------------------------------------------------------------------------+
```

### PAGE 7 — Guided Conversation

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's read together. I'll be Alex, you be Yuki."                    |
|    「いっしょによみましょう。わたしがアレックスで、あなたがゆきです。」  |
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
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  ▸ "Great job! Now let's swap. This time I'll be Yuki."                 |
|    「じょうずですね！じゃあ、こうたいしましょう。                        |
|     こんどはわたしがゆきです。」                                        |
|                                                                         |
|                                                                  PAGE 7 |
+-------------------------------------------------------------------------+
```

### PAGE 8 — Memory Conversation

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
|  YUKI (tutor):   私のペンはどこですか？                                  |
|                  Where is my pen?                                       |
|                                                                         |
|  ALEX (you):     ペンは______です。                                      |
|                                                                         |
|  YUKI (tutor):   あ、ありがとう！ノートはどこですか？                     |
|                  Oh, thanks! Where is the notebook?                     |
|                                                                         |
|  ALEX (you):     ノートは______です。                                    |
|                                                                         |
|  YUKI (tutor):   じゃあ、私のかばんはどこですか？                         |
|                  Then, where is my bag?                                 |
|                                                                         |
|  ALEX (you):     かばんは______です。                                    |
|                                                                         |
|  YUKI (tutor):   ありがとう、アレックスさん！                            |
|                  Thanks, Alex!                                          |
|                                                                         |
|                                                                  PAGE 8 |
+-------------------------------------------------------------------------+
```

### PAGE 9 — Free Discussion

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
|                                                                  PAGE 9 |
+-------------------------------------------------------------------------+
```

### PAGE 10 — Roleplay

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
|                                                                 PAGE 10 |
+-------------------------------------------------------------------------+
```

### PAGE 11 — Travel in Japan

```
+-------------------------------------------------------------------------+
|                                                                         |
|  ▸ "Let's try using what we learned — imagine you're traveling           |
|     in Japan!"                                                          |
|    「きょうならったことをつかってみましょう                              |
|     — にほんをりょこうしているとおもってね！」                          |
|                                                                         |
|  TRAVEL IN JAPAN: ASKING FOR DIRECTIONS                                 |
|  ──────────────────────────────────────                                 |
|  You are a traveler. Fill in the blanks and say them out loud!          |
|                                                                         |
|  ┌─── CONTEXT / 状況 ─────────────────────────────────────────┐         |
|  │  You just arrived at a train station in Tokyo.              │         |
|  │  Ask the staff where things are!                            │         |
|  └────────────────────────────────────────────────────────────┘         |
|                                                                         |
|     ┌─── NEW WORDS ──────────────────────────────────────┐              |
|     │  すみません (excuse me)   トイレ (toilet/restroom)    │              |
|     │  コンビニ (convenience store)  でぐち (exit)          │              |
|     │  ありがとうございます (thank you)                      │              |
|     └─────────────────────────────────────────────────────┘              |
|                                                                         |
|                                                                         |
|  YOU:      すみません、トイレは______ですか？                             |
|            Excuse me, where is the restroom?                            |
|                                                                         |
|  STAFF:    トイレはあそこです。                                           |
|            The restroom is over there.                                  |
|                                                                         |
|  YOU:      ありがとうございます！でぐちは______ですか？                   |
|            Thank you! Where is the exit?                                |
|                                                                         |
|  STAFF:    でぐちはそこです。                                             |
|            The exit is there.                                           |
|                                                                         |
|  YOU:      コンビニは______ですか？                                       |
|            Where is the convenience store?                              |
|                                                                         |
|  STAFF:    コンビニはここです。                                           |
|            The convenience store is right here.                         |
|                                                                         |
|  YOU:      ______ございます！                                             |
|            Thank you very much!                                         |
|                                                                         |
|                                                                 PAGE 11 |
+-------------------------------------------------------------------------+
```

### PAGE 12 — Bonus 1: Vocab Quiz

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 1: VOCAB QUIZ                                                    |
|  ─────────────────────                                                  |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  ▸ "Can you say these words in Japanese?"                               |
|    「にほんごでいえるかな？」                                            |
|                                                                         |
|                                                                         |
|  ┌──────────────────────┬──────────────────────┐                        |
|  │  English              │  Say in Japanese      │                        |
|  ├──────────────────────┼──────────────────────┤                        |
|  │  where                │  __________           │                        |
|  │  here                 │  __________           │                        |
|  │  there                │  __________           │                        |
|  │  over there           │  __________           │                        |
|  ├──────────────────────┼──────────────────────┤                        |
|  │  book                 │  __________           │                        |
|  │  pen                  │  __________           │                        |
|  │  notebook             │  __________           │                        |
|  │  bag                  │  __________           │                        |
|  │  phone                │  __________           │                        |
|  │  clock                │  __________           │                        |
|  │  key                  │  __________           │                        |
|  └──────────────────────┴──────────────────────┘                        |
|                                                                         |
|                                                                         |
|  LESSON 2 ←→ LESSON 3 CONNECTION:                                       |
|                                                                         |
|     これ (this thing)    ←→   ここ (this place / here)                  |
|     それ (that thing)    ←→   そこ (that place / there)                 |
|     あれ (that thing     ←→   あそこ (that place /                      |
|           over there)               over there)                         |
|                                                                         |
|                                                                 PAGE 12 |
+-------------------------------------------------------------------------+
```

### PAGE 13 — Bonus 2: Translate (No Hints)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 2: TRANSLATE — NO HINTS!                                         |
|  ────────────────────────────────                                       |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  ▸ "Can you translate these without any hints? Let's try!"              |
|    「ヒントなしでにほんごにできるかな？やってみよう！」                  |
|                                                                         |
|                                                                         |
|  1. Where is the pen?                                                   |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  2. The book is here.                                                   |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  3. Where is the bag?                                                   |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  4. The clock is over there.                                            |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  5. Where is the phone?                                                 |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|  6. The notebook is there.                                              |
|                                                                         |
|     _____________________________________________________               |
|                                                                         |
|                                                                 PAGE 13 |
+-------------------------------------------------------------------------+
```

### PAGE 14 — Bonus 3: Today's Character — か / カ (ka)

```
+-------------------------------------------------------------------------+
|                                                                         |
|  BONUS 3: TODAY'S CHARACTER                                             |
|  ──────────────────────────                                             |
|  (Skip if you don't have time!)                                         |
|                                                                         |
|  ▸ "Let's learn one character today!"                                   |
|    「きょうはひとつ、もじをおぼえましょう！」                                         |
|                                                                         |
|                                                                         |
|  ┌────────────────────────────────────────────┐                         |
|  │                                              │                         |
|  │   Hiragana:  か        Katakana:  カ          │                         |
|  │   Sound:     ka                               │                         |
|  │                                              │                         |
|  └────────────────────────────────────────────┘                         |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  1. RECOGNITION — Which one is `ka`?                                      |
|                                                                         |
|  ▸ "Can you find `ka`? Point to it!"                                      |
|    「か はどれですか？ゆびでさしてね！」                                  |
|                                                                         |
|     a)  き       b)  か       c)  さ                                    |
|                                                                         |
|     Which one is `ka`?                                                     |
|                                                                         |
|     a)  ク       b)  キ       c)  カ                                    |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  2. READ — Read these words out loud!                                   |
|                                                                         |
|  ▸ "Can you read these words without romaji?                            |
|    「よめるかな？か をみつけてね！」                                               |
|                                                                         |
|     • かばん           bag                                              |
|     • かぎ             key                                              |
|     • どこですか ？      Where is ___?                                     |
|                                                                         |
|  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
|                                                                         |
|  3. WRITE — Fill in the missing か!                                     |
|                                                                         |
|  ▸ "Write the missing か to complete the word!"                         |
|    「か をかいて、ことばをかんせいさせてね！」                           |
|                                                                         |
|     Hiragana か:                                                        |
|     kagi (key)          =  [   ]ぎ                                      |
|     kaban (bag)         =  [   ]ばん                                    |
|     doko desu ka?       =  どこです[   ]？                              |
|                                                                         |
|     Katakana カ:                                                        |
|     kamera (camera)     =  [   ]メラ                                    |
|     karee (curry)       =  [   ]レー                                    |
|     kaado (card)        =  [   ]ード                                    |
|                                                                         |
|                                                                 PAGE 14 |
+-------------------------------------------------------------------------+
```

### PAGE 15 — Mission Complete

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
|  ▸ "Let's read one more time. Perfect! See you next lesson!"            |
|    「さいごにもういちどよみましょう。かんぺき！                          |
|     つぎのレッスンであいましょう！」                                    |
|                                                                         |
|  KEY EXPRESSIONS — もういちどよんでみましょう！                           |
|  • ほんはどこですか？          — Where is the book?                      |
|  • ほんはここです。            — The book is here.                       |
|  • ペンはそこです。            — The pen is there.                       |
|  • かばんはあそこです。        — The bag is over there.                  |
|                                                                         |
|                                                                 PAGE 15 |
+-------------------------------------------------------------------------+
```
