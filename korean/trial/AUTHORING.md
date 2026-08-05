# 새 덱 만들기 — 컴포넌트와 뼈대

새 과를 만들 때 **CSS 도 자바스크립트도 쓰지 않습니다.** 아래 마크업을 얹으면
배선(입력·채점·공유·페이지 넘김)은 공유 스크립트가 합니다. 새 클래스를 만들기
전에 이 목록에 이미 있는 것을 먼저 찾아보세요 — 어휘가 하나 늘 때마다 덱 사이의
일관성이 한 칸씩 줄어듭니다.

설계 원칙은 [`ux-philosophy.md`](../ux-philosophy.md) 에 있습니다.
이 문서는 **무엇을 쓸 수 있는가**만 적습니다.

---

## 1 · 파일 뼈대

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
  <link rel="stylesheet" href="../runtime/css/lesson-card.css">
  <link rel="stylesheet" href="../runtime/css/trial.css">
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

  <script src="../runtime/js/activities.js"></script>
  <script src="../runtime/js/pager.js"></script>
  <script src="../runtime/js/script-lines.js"></script>
  <script src="../runtime/js/spotlight.js"></script>
  <script src="../runtime/js/tutor-notes.js"></script>
  <script src="../runtime/js/highlight.js"></script>
  <script src="../runtime/js/stamp.js"></script>
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
- `.answer-space` 는 답이 적혀 있으면 채점칸, 비어 있으면 자유 작문칸이 됩니다.
- **힌트는 어휘만**(`JP:KO`), 조사나 어미는 넣지 않습니다. 그리고 **답 칸 안에** 둡니다.

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

### 설명용 도식

| 무엇 | 마크업 |
| --- | --- |
| 받침 규칙 | `.batchim` > `.bt-box` > `.bt-eq`(`.bt-syl` + `.bt-arrow` + `.bt-out`) + `.bt-head` + `.bt-ex` |
| 억양(끝 올리기/내리기) | `.pitch` > `.pi-card` > `.korean` + `.pi-curve`(SVG) + `.translation` |
| 한자 다리 | `.bridge` > `.br-row` > `.br-cn` + `.br-eq` + `.br-ko` |
| 오늘의 성과 | `.combi`(명사 은행 × 어미) + `.payoff`(큰 숫자) |

받침 도식을 어미(주황) 색으로 쓰려면 `.batchim.ending-rule` 을 씁니다.

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
- 자세한 계약은 [`interactive/interaction-protocol.md`](../interactive/interaction-protocol.md).

---

## 6 · 만든 뒤 확인

1. 브라우저 480px 폭에서 **전 페이지를 눈으로** 봅니다(시각 문서입니다).
2. 페이저 스크러버로 끝까지 넘겨 가로 넘침이 없는지 봅니다.
3. 티칭 모드(T)를 켜서 유령 답과 튜터 메모가 뜨는지 봅니다.
4. 레몬보드에 올릴 zip 은 [`interactive/packaging.md`](../interactive/packaging.md).
