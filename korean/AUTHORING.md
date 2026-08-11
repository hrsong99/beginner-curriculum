# 새 덱 만들기 — 컴포넌트와 뼈대

새 과를 만들 때 **CSS 도 자바스크립트도 쓰지 않습니다.** 아래 마크업을 얹으면
배선(입력·채점·공유·페이지 넘김)은 공유 스크립트가 합니다. 새 클래스를 만들기
전에 이 목록에 이미 있는 것을 먼저 찾아보세요 — 어휘가 하나 늘 때마다 덱 사이의
일관성이 한 칸씩 줄어듭니다.

설계 원칙은 [`ux-philosophy.md`](./ux-philosophy.md) 에 있습니다.
이 문서는 **무엇을 쓸 수 있는가**만 적습니다.

> **그래도 새 컴포넌트를 만들었다면, 이름을 `runtime/js/spotlight.js` 의 `SPOT`
> 목록에 넣으세요.** 그 목록에 있는 것만 튜터가 빨간 링으로 짚을 수 있고, 빠뜨려도
> 아무 에러가 나지 않습니다 — 그 블록만 조용히 안 켜집니다. 블록 안에서 따로 짚을
> 이름이 있는 부품(예: 규칙 카드 안의 글자 하나)도 같이 넣으면 됩니다. 한 겹씩
> 들어가는 방식이라 부품을 넣는다고 블록을 못 짚게 되지는 않습니다.
> 이유는 [`ux-philosophy.md` § The shared pointer](./ux-philosophy.md) 에 있습니다.

---

## 1 · 파일 뼈대

경로는 `trial/lessons/deck.html` 처럼 **두 단계 아래**에 있는 덱 기준입니다.
한 단계(`tracks/2-core-patterns/`)에 두면 `../` 하나를 빼세요.

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google" content="notranslate">        <!-- 없으면 크롬이 ja/ko 를 섞어 망가뜨린다 -->
  <meta name="podo:lesson-id" content="trial-2-selfintro">
  <meta name="podo:content-version" content="2026-08-05">
  <title>…</title>
  <link rel="stylesheet" href="../../runtime/css/lesson-card.css">
  <link rel="stylesheet" href="../../runtime/css/trial.css">
</head>
<body>
  <div class="phone">
    … 페이지들 …
  </div>

  <!-- 페이저 (스크러버 포함) -->
  <nav class="pager" data-sync-id="deck-page" data-sync-kind="page">
    <input class="pg-scrub" type="range" min="0" max="0" step="1" value="0" aria-label="페이지 이동">
    <button class="pg-btn pg-prev" type="button" aria-label="이전 페이지">←</button>
    <div class="pg-mid"><span class="pg-label"><b class="pg-act">—</b><span class="pg-n">—</span></span></div>
    <button class="pg-btn pg-teach" type="button" aria-label="티칭 모드">T</button>
    <button class="pg-btn pg-next" type="button" aria-label="다음 페이지">→</button>
  </nav>

  <img class="stamp-art" src="../assets/well-done.svg" alt="">   <!-- .phone 바깥! -->

  <script src="../../runtime/js/activities.js"></script>
  <script src="../../runtime/js/pager.js"></script>
  <script src="../../runtime/js/script-lines.js"></script>
  <script src="../../runtime/js/spotlight.js"></script>
  <script src="../../runtime/js/tutor-notes.js"></script>
  <script src="../../runtime/js/highlight.js"></script>
  <script src="../../runtime/js/stamp.js"></script>
  <script src="../../runtime/js/yomi.js"></script>          <!-- 발음 표기를 쓰는 덱만 -->
</body>
</html>
```

**로드 순서는 지켜야 합니다.** `activities` → `pager`(티칭 모드가 activities 가 만든
유령 답을 부른다) → `script-lines` → `tutor-notes`(페이지를 다 센 뒤에 칸을 끼운다) →
`highlight`(글자에 긋는 형광펜 — 마크업이 다 선 뒤에 `<mark>` 를 끼운다) → `stamp`.

과의 성격에 따라 `activities.js` 바로 뒤에 한 줄을 더합니다:

| 과 | 추가 |
| --- | --- |
| 한글(자모·음절) | `runtime/js/hangul-activities.js` |
| 자유 대화(피드백·고르기) | `runtime/js/freetalk-activities.js` |
| 문장 패턴 | 없음 — `activities.js` 만으로 충분 |

---

## 1-2 · 체험 레슨 풀덱 (`full-trials/`)

풀덱은 **레슨 덱에 앞뒤 열다섯 장을 두른 것**입니다. 레슨은 `lessons/` 의 것을
그대로 쓰고, 감싸는 페이지는 네 덱이 모두 같은 것을 씁니다.

```
cover · greeting
  needs-intro · needs-why · needs-goal · needs-pace          ← 니즈 파악 4장
  … 레슨 전체(trial-intro … todays-result) …
  report-intro · report                                       ← 리포트 2장
  info-intro · info-podo · info-about · plan-curriculum ·
  info-tutors · plan-price · plan-switch · info-price-all ·
  info-faq                                                    ← 안내(판매) 9장
closing
```

- 감싸는 페이지의 CSS 는 `runtime/css/trial.css` 의 「FULL TRIAL」 절에 있습니다.
- 리포트의 레벨 체크·항목별 진단·로드맵 배선은 `runtime/js/report.js` 입니다.
  풀덱은 `activities.js` 다음에 이 줄을 하나 더 답니다.
- 감싸는 페이지는 레슨과 무관한 판매 자료라, 새 풀덱을 만들 때는 다른 풀덱에서
  이 열다섯 장을 그대로 복사해 오면 됩니다.

---

## 2 · 페이지 (`.phone` 의 자식 하나 = 한 장)

모든 페이지에 **`data-page-id`** 를 답니다. 공유되는 것은 순서가 아니라 이 id 라서,
나중에 페이지를 끼워 넣어도 상대 화면이 어긋나지 않습니다.

| 무엇 | 마크업 |
| --- | --- |
| 표지 | `<div class="brand-page" data-page-id="cover">` + `.podo-badge` + `.brand-title` |
| 파트 구분(라임) | `<div class="brand-page divider">` + `.brand-mascot` + `.brand-title` + `.brand-sub` |
| 파트 전환(어두운) | `<div class="transition-page" data-act="N이에요 / 예요">` + `.transition-kicker` + `.transition-title` + `.transition-copy` |
| 학습 페이지 | `<div class="section" data-page-id="p1-teach">` |
| 마무리 | `<div class="brand-page end">` |

`data-act` 는 페이저 왼쪽에 뜨는 장 이름입니다. 붙인 페이지에서 새 장이 시작됩니다.

### 학습 페이지 한 장의 구조

```html
<div class="section" data-page-id="p1-fill">
  <h2 class="section-title">빈칸을 채워요 <span class="title-ja">(空欄をうめよう)</span></h2>
  <p class="section-subtitle"><span class="ko">…</span><span class="ja">…</span></p>
  <div class="tutor-note">학생이 말한 대로 빈칸에 적어 주세요.</div>   <!-- 튜터만, 선택 -->
  … 활동 하나 …
</div>
```

- 제목은 **한국어 먼저**, 일본어는 괄호 안 `.title-ja`.
- `.section-subtitle` 은 **튜터가 소리 내어 읽는 줄**입니다(`blue-100` 은 이 뜻 하나뿐).
  `.ko` 가 읽는 말, `.ja` 는 그 번역 — 둘은 **같은 문장**이어야 합니다.
- `.tutor-note` 는 스크립트 바로 밑에 붙는 튜터 전용 띠입니다. 한국어로 씁니다.
- **활동은 한 장에 하나.** 두 종류를 한 화면에 섞지 않습니다.

---

## 3 · 활동 컴포넌트

### 읽기 (받아들이기)

```html
<div class="model-list">
  <div class="model-line"><span class="korean">저는 학생<span class="ending">이에요</span>.</span><span class="translation">私は学生<span class="ending">です</span>。</span></div>
</div>
```

### 패턴 카드 + 변형

```html
<div class="sent-hero">                       <!-- .topic 을 더하면 보라(은/는) 카드 -->
  <span class="korean">저는 다나카<span class="ending">예요</span>.</span>
  <span class="translation">私は田中<span class="ending">です</span>。</span>
</div>
<div class="sent-more">                       <!-- 카드 밑에 붙는 회색 트레이 -->
  <div><span class="korean">…</span><span class="translation">…</span></div>
</div>
```

### 고르기 (둘 중 하나)

```html
<div class="choose-list">
  <div class="choose-row sentence" data-sync-id="p1-choice-student" data-sync-kind="selection" data-sync-state="chosen">
    <span class="translation">私は学生です。</span>
    <span class="choose-sentence">저는 학생<span class="opt" data-sync-option="ieyo" data-correct>이에요.</span><span class="sep">/</span><span class="opt" data-sync-option="yeyo">예요.</span></span>
  </div>
</div>
```

정답은 오가지 않습니다 — 고른 쪽만 공유하고 `data-correct` 로 각자 채점합니다.
고른 것을 다시 누르면 아무것도 안 고른 상태로 돌아갑니다(맞혔든 틀렸든).
되돌리기는 곧 "빈 집합"이라 상대 화면에서도 같이 풀립니다.

### 빈칸 채우기 / 번역 / 자유 작문

```html
<div class="task-block">
  <div class="answer-box">                     <!-- .tall 이면 자유 작문 높이 -->
    <span class="answer-label">私は学生<span class="target ending">です</span>。</span>
    <span class="answer-fill"><span class="korean">저는 학생<span class="slot" data-sync-id="p1-fill-student">이에요</span>.</span></span>
    <span class="hint"><span class="hint-chip">学生:학생</span></span>   <!-- 칸 안에 넣으면 아래 띠가 된다 -->
  </div>
</div>
```

- `.slot` 안에 적은 글자가 **정답**입니다. 로드될 때 점선 입력칸으로 바뀝니다.
- 빈칸이 **문장 한 토막**이어도(대화 채우기처럼 서술어 전체를 말하게 하는 자리) 그냥
  `.slot` 입니다. 크기를 지정하는 클래스는 없습니다 — 로드될 때 답을 실제로 그려 보고
  그 너비로 칸을 잡으므로, 앞말이 짧으면 한 줄에 들어가고 길면 알아서 아랫줄로
  넘어갑니다. 넘어간 칸이 윗글에 붙어 보이지 않도록 `.dialogue .answer-fill` 의 줄
  간격이 넉넉하게 잡혀 있으니, 여백을 따로 손대지 마세요.
- `.answer-space` 는 답이 적혀 있으면 채점칸, 비어 있으면 자유 작문칸이 됩니다.
- **머리띠(`.answer-label`)는 아래 한국어의 일본어 번역입니다.** 세 장만 지나면 학습자는
  이 자리를 그렇게 읽습니다. 번역할 것이 없어(아직 한국어가 없고 학습자가 지어냅니다)
  **할 일**을 적어야 하면 `.task` 를 답니다 — 「やること」 배지가 CSS 에서 붙고 글자 무게가
  한 단 내려갑니다. 띠 전체가 지시면 `<span class="answer-label task">`, 번역 뒤에 지시가
  덧붙는 형태면 번역은 그대로 두고 지시만 `<span class="task">` 로 감쌉니다.
  괄호로만 구분하지 마세요 — 괄호는 번역문 안에도 나옵니다.
- **힌트는 어휘만**(`JP:KO`), 조사나 어미는 넣지 않습니다. 그리고 **답 칸 안에** 둡니다.
- **힌트 칩은 그 빈칸의 답에 실제로 쓰이는 낱말만** 답니다. 화면에 이미 찍혀 있는 말
  (`네! 일본에 ▁?` 의 일본)은 힌트가 아니라 소음이고, 있어야 할 낱말을 밀어냅니다.
  자유 작문 칸은 답이 정해져 있지 않으므로, 고를 수 있는 어휘를 그대로 늘어놓습니다.

### 문장 만들기 (칩 배열)

```html
<div class="task-block">
  <div class="answer-box small">
    <span class="answer-label">私は日本人です。</span>
    <span class="answer-space" data-sync-id="p2-order-japanese">저는 일본 사람이에요</span>
  </div>
  <span class="choice" data-item-id="japanese">일본 사람</span>
  <span class="choice" data-item-id="me">저는</span>
  <span class="choice" data-item-id="ieyo">이에요</span>
</div>
```

### 대화

```html
<div class="dialogue">
  <div class="turn other"><span class="who"><img class="avatar" src="…" alt=""><span class="who-name">ハナ</span></span>
    <div class="bubble"><span class="korean">…</span><span class="translation">…</span></div></div>
  <div class="turn me">… <div class="bubble me">…</div></div>
</div>
```

이야기 인물은 사진 아바타, 튜터/학생 연습은 기본 아이콘 아바타를 씁니다.
학생 말풍선(`.bubble.me`)은 초록 틴트만 받고 초록 테두리는 받지 않습니다.

말풍선이 **적는 칸**이면 `.bubble` 안에 `.answer-box` 하나만 넣습니다 — 말풍선 껍데기는
스스로 사라지고 답 상자가 곧 말풍선이 됩니다(상자 안에 상자를 만들지 마세요). 어느 쪽이든
쓸 수 있습니다: 학생 차례면 머리띠가 초록(`.bubble.me`), 튜터가 직접 답을 적는 자리면
회색입니다.

```html
<div class="turn other"><span class="who">…<span class="who-name">선생님</span></span>
  <div class="bubble"><div class="answer-box small">
    <span class="answer-label">先生の答え</span>
    <span class="answer-space" data-sync-id="p3-freetalk-tutor"></span>
  </div></div></div>
```

### 설명용 도식

| 무엇 | 마크업 |
| --- | --- |
| 받침 규칙 | `.batchim` > `.bt-box` > `.bt-eq`(`.bt-syl` 또는 `.bt-syls` + `.bt-arrow` + `.bt-out`) + `.bt-head` + `.bt-ex` |
| 억양(끝 올리기/내리기) | `.pitch` > `.pi-card` > `.korean` + `.pi-curve`(SVG) + `.translation` |
| 한자 다리 | `.bridge` > `.br-row` > `.br-cn` + `.br-eq` + `.br-ko` |
| 바꿔 말하기(원어민 팁) | `.swap` > `.swap-row` > `.translation` + `.sw-from` + `.sw-to` |
| 오늘의 성과 | `.combi`(명사 은행 × 어미) + `.payoff`(큰 숫자) |

받침 도식을 어미(주황) 색으로 쓰려면 `.batchim.ending-rule` 을 씁니다.

**글자 도식에서 색이 앉는 자리는 규칙이 정해집니다.** `.bt-syl` 의 자리(seat)는 글자 뒤에
깔리는 것이지 글자를 칠하는 것이 아니고, 무엇으로 갈리는 규칙이냐에 따라 위치가 다릅니다.

| 규칙이 갈리는 것 | 클래스 | 자리 | 예 |
| --- | --- | --- | --- |
| 받침 | `.on` / `.off` | 바닥 | 먹 · 보 |
| 모음 (ㅏ ㅓ ㅣ …) | `.vowel` | 오른쪽 세로획 | 앉 · 먹 |
| 모음 (ㅗ ㅜ ㅡ ㅛ ㅠ) | `.vowel.under` | 가운데 가로띠 | 놀 |

글자를 그대로 두고 캡션에만 「ㅏ · ㅗ」라고 적으면, 정작 어디를 보라는 건지가 화면에
없습니다. 바닥 자리를 모음에 쓰지 마세요 — 같은 덱 앞쪽에서 이미 받침을 뜻합니다
(그리고 `.under` 를 쓰는 글자는 그 바닥에 자기 받침을 깔고 있습니다).

**규칙이 모음 두 개를 덮으면 둘 다 그립니다.** `.bt-eq` 안에 `.bt-syls` 로 어간 타일을
나란히 놓으면 화살표 하나가 둘을 동시에 받습니다 — 「ㅏ · ㅗ」인데 앉만 보이면 ㅗ 는
각주가 됩니다. **두 타일 사이에는 고르기 줄과 같은 `.sep`(`/`) 를 넣으세요** — 붙여 놓으면
한 낱말로 읽힙니다(앉 놀 → 앉놀). 타일은 두 장이 되면서 한 단 작아지고, 480px 아래에서
한 번 더 작아집니다.
가로 폭이 이 컴포넌트에서 가장 빠듯한 자리이니 예를 바꾸면 360px 폭에서 다시 재세요.
ㅗ 예는 축약되지 않는 어간으로 고릅니다 — 보다·오다는 봐도·와도가 되어 규칙을 깹니다.

**`.swap` 은 "같은 문장을 원어민은 이렇게 말한다"를 그립니다.** 위 줄(`.sw-from`)이 평범한
쪽, 아래 줄(`.sw-to`)이 학습자가 가져갈 쪽이고, 바뀐 조각만 `.ending`/`.topic` 으로
표시합니다. 화살표는 CSS 가 붙이므로 마크업에 적지 않습니다. 결과만 두 개 보여주고
설명은 글로 쓰는 카드(옛 `.card` + `.tip` + `.example-card`)로 돌아가지 마세요 — 상자가
세 겹이 되고, 정작 무엇이 바뀌었는지는 학습자가 되짚어야 합니다.

### 발음 표기 (`.yomi`)

**발음 표기는 초중급까지입니다.** 가나 읽기는 한글을 아직 못 읽는 사람을 위한 받침대라,
**왕초급 · 초급 · 초중급** 덱에만 답니다. **중급부터는 달지 않습니다** — 거기서부터 한글 읽기는
학습자가 이미 가진 기술이고, 덱이 대신 읽어 주면 그 연습을 빼앗습니다. 덱의 레벨은 파일 안
`<meta name="podo:level">` 에 적혀 있으니, 읽기를 달기 전에 그것부터 확인하세요
(레벨 표는 [`AGENTS.md`](./AGENTS.md) 에 있습니다).

레벨이 맞는 덱에서는 **학습자가 소리 내어 말하는 한국어** 밑에 가나 읽기를 답니다.
클래스 하나뿐이고, 자리는 그 한국어 **바로 뒤**입니다.

```html
<span class="korean">저는 학생<span class="ending">이에요</span>.</span>
<span class="yomi">チョヌン ハクセンイエヨ</span>
```

- 붙는 곳: `.model-line` · `.sent-hero`/`.sent-more` · `.bubble` · `.pi-card` ·
  `.bt-out`/`.bt-ex` · `.choice`/`.choose-word` · `.answer-fill` ·
  `.example-card` · `.combi` 타일 · `.brand-title`/`.transition-title`.
- **안 붙는 곳**: `.section-title`(옆의 `.title-ja` 가 이미 무슨 장인지 말한다),
  `.section-subtitle`(튜터가 읽는 줄), `.tutor-note`, `.slot`·`.answer-space`(정답).
- **둘 중 하나를 고르는 알약(`.opt`)에는 넣지 않습니다.** 거기 들어가는 것은 그 장이
  방금 가르친 패턴뿐이라(이에요/예요, 은/는) 고를 때쯤엔 도움이 아니라 2em 짜리
  과녁 안의 두 번째 줄이 되고, 네 줄이면 한눈에 보던 것이 문단이 됩니다. 옆의 **낱말**
  (`.choose-word`)은 그대로 답니다. 칩 배열(`.choice`)은 넓어서 둘 다 들어갑니다.
- 힌트 칩 안에서는 줄이 바뀌지 않고 뒤에 붙습니다 —
  `<span class="hint-chip">学生:학생<span class="yomi">ハクセン</span></span>`.
- 빈칸이 있는 문장은 보이는 부분만 읽고 빈칸은 `＿＿＿` 로 둡니다 —
  `チョヌン ハクセン ＿＿＿`.
- 표기는 **철자가 아니라 소리**입니다: 회사원이에요 → `フェサウォニエヨ`(연음),
  시작할게요 → `シジャカルケヨ`. 어절 사이는 반각 공백으로 띕니다.
- 스위치는 `runtime/js/yomi.js` 가 **읽기가 있는 페이지마다** 하나씩 놓습니다
  (마크업에 쓸 것은 없습니다 — `<script src>` 한 줄이면 됩니다). 이름은
  「よみがな」, 학습자의 말입니다: 페이저 안의 기호였을 때는 덱의 장치로 읽혀서
  자기가 끌 수 있는 줄 몰랐습니다.
- 자리는 **제목과 같은 줄**입니다. `.section-title` 을 `.page-head` 로 감싸고 그
  오른쪽 끝에 붙이므로, 제목이 길어지면 스위치 앞에서 줄이 바뀔 뿐 밑으로 파고들지
  않습니다(모서리에 띄우는 방식은 언젠가 긴 제목에 깔립니다). 맞출 제목이 없는
  표지·전환 페이지에서만 `.corner` 로 오른쪽 위 모서리에 띄웁니다.
- 상태는 `body.no-yomi` 하나라 한 장에서 끄면 전부 꺼지고, **티칭 모드와 달리
  공유합니다**(`data-sync-kind="yomi"`). 읽기를 끄는 것은 답을 여는 일이 아니라
  수업의 합의라서, 튜터가 껐는데 학습자 화면이 그대로면 그 말이 성립하지 않습니다.
- 채점은 `.yomi` 를 빼고 한국어만 봅니다(`activities.js` 의 `koText`). 새 활동을 만들 때
  칩·칸의 글자를 읽어야 하면 `textContent` 가 아니라 그 함수를 쓰세요.
- **읽기에 자리를 내주는 규칙은 반드시 `body:not(.no-yomi)` 로 묶습니다.** `:has()` 와
  `+` 는 구조를 보는 선택자라 스위치가 읽기를 숨겨도 계속 맞고, 그러면 카드가 바닥
  여백을 잃습니다(`.model-line`·`.bubble` 의 `padding-bottom: 0` 이 그랬습니다).
  끈 상태는 읽기를 넣기 전의 화면과 **픽셀 단위로 같아야** 합니다 — 두 상태를 모두
  렌더해서 확인하세요.

---

## 4 · 색과 간격

색은 **하나에 하나의 뜻**입니다. 새 뜻을 얹는 순간 페이지가 안 읽힙니다.

| 색 | 뜻 |
| --- | --- |
| `green-500` / `green-100` | 상태 — 고름·정답·활성 |
| `blue-100` | 튜터가 소리 내어 읽는 줄 |
| `blue-200` | 그 밑에 붙는 튜터 전용 메모 |
| `lime` | 브랜드 크롬(브랜드 페이지·페이저) — 상태로 쓰지 않는다 |
| `gray-200` | 보통의 테두리 |
| 점선 회색 | "여기에 쓴다" |
| 주황(`--ending-*`) / 보라(`--topic-*`) | 어미 / 조사 — 지금 가르치는 조각 |

간격은 토큰 하나가 정합니다: **`--item-gap`(16px)** — 한 활동 안에서 반복되는
항목 사이의 거리. 스크립트 상자와 활동 사이는 26px 로 모든 페이지가 같습니다.
새 컴포넌트의 CSS 는 `runtime/css/` 안에서 삽니다 — 덱 안에 `<style>` 을 두지 않습니다.
컴포넌트를 새로 만들 때 `gap` 을 직접 적지 말고 `var(--item-gap)` 을 쓰세요.

---

## 5 · 공유(레몬보드)

- **`data-sync-id` 가 있는 요소만 공유됩니다.** id 가 없으면 그 칸은 각자의 것입니다.
- 정답/오답은 절대 공유하지 않습니다 — 고른 값만 보내고 판정은 양쪽이 각자 합니다.
- 티칭 모드(답 보기)는 공유하지 않습니다.
- 자세한 계약은 [`interaction-protocol.md`](./interaction-protocol.md).

---

## 6 · 만든 뒤 확인

1. 브라우저 480px 폭에서 **전 페이지를 눈으로** 봅니다(시각 문서입니다).
2. 페이저 스크러버로 끝까지 넘겨 가로 넘침이 없는지 봅니다.
3. 티칭 모드(T)를 켜서 유령 답과 튜터 메모가 뜨는지 봅니다.
4. 레몬보드에 올릴 zip 은 이 레포에서 만들지 않습니다 — `podo-curriculum` 의
   `tools/build.py` 가 배포 파이프라인의 일부로 처리합니다(`docs/packaging.md`).
