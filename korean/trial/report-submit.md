# 리포트 저장 — 요청 규격

체험 레슨 리포트([`reports/trial-1-report.html`](./reports/trial-1-report.html)) 맨 끝의
**「리포트 저장」** 버튼이 무엇을 어디로 보내는지 적어 둔 문서입니다.

**남기는 것은 입력뿐입니다.** 리포트가 학생에게 보여 주는 것은 거의 전부 계산해 낸 값이고 —
레벨 문안, 항목별 문장, 좋아요/아쉬워요, 코멘트, 기간, 레슨 수, 코스 순서 — 그 계산은
[`../runtime/js/report.js`](../runtime/js/report.js) 한 곳에 있습니다. **같은 리포트가 앱에서도
열리고 거기서도 같은 계산을 하므로, 계산 결과는 저장하지 않습니다.** 결과까지 넣으면 같은 값이
두 곳에 살게 되고, 둘이 어긋나는 날 어느 쪽이 맞는지 아무도 모릅니다.

그래서 스냅샷은 **열다섯 개 남짓**입니다.

```
학습 동기(복수) · 목표 · 페이스 · 종합 레벨 · 항목별 다섯 · 합의한 주당 횟수
```

저장할 곳은 `le_level_test` 한 행이고, 이 입력들은 그 행의 `report_snapshot`(JSON) 칸에
들어갑니다. 컬럼 대응은 [§4](#4-le_level_test-대응)에 있습니다.

| 무엇 | 어디 |
| --- | --- |
| 버튼 마크업 | `reports/trial-1-report.html` 의 `.rep-send` |
| 스냅샷을 짓는 코드 | [`../runtime/js/report.js`](../runtime/js/report.js) 의 `snapshot()` |
| 보내는 코드 | [`../runtime/js/report-submit.js`](../runtime/js/report-submit.js) |
| **입력 → 리포트 계산** | [`plan-logic.md`](./plan-logic.md) 와 `report.js` |

---

## 1. 언제, 어디로

**튜터만 누릅니다.** 이 칸은 티칭 모드에서만 보이고(`body.teaching`), 학습자 화면에는 아예
없습니다. 저장은 상담이 끝나고 하는 일이지 수업 중의 한 수가 아니라서, 누른 사실도 상대
화면으로 가지 않습니다(`data-sync` 없음).

**다 채우기 전에는 눌리지 않습니다.** 종합 레벨 · 학습 동기 · 목표 · 항목별 다섯 중 하나라도
비어 있으면 버튼이 잠기고, 무엇이 비었는지가 버튼 밑에 이름으로 뜹니다. 입력이 비면 앱에서
리포트를 그릴 수 없습니다 — 비는 것이 결과가 아니라 재료이기 때문입니다.

```
POST  {podo:report-endpoint}
Content-Type: application/json
```

보낼 곳은 덱 머리의 메타 한 줄이 정합니다.

```html
<meta name="podo:report-endpoint" content="https://webhook.example.invalid/api/v2/leveltest/korean-trial-report">
```

지금 들어 있는 값은 **자리만 잡아 둔 웹훅**이라 누르면 실패합니다. 백엔드가 붙으면 이 한 줄만
바꿉니다 — 스크립트에는 주소가 없습니다.

성공 판정은 **HTTP 2xx** 하나뿐이고 응답 본문은 읽지 않습니다. 실패하면 버튼이 다시 풀리고
사유가 뜹니다. 따로 받아 두는 사본은 없습니다 — 되살릴 원본이 화면에 그대로 있으므로 다시
누르면 되고, 숨은 사본을 하나 더 만들면 어느 쪽이 진짜인지가 문제가 됩니다.

### 학생·수업 식별자는 덱 밖에서 옵니다

덱은 어느 수업에나 그대로 실리는 문서라 `studentId` 를 안에 적어 둘 수 없습니다. 보드가
**URL 쿼리스트링**으로 넘겨주고, 스크립트는 그것을 읽습니다.

```
lesson.html?studentId=482913&classId=77120&studentName=%EA%B9%80%ED%8F%AC%EB%8F%84&tutorId=331
```

호스트 쪽에서 전역으로 심어 주는 것도 같은 값으로 받습니다(쿼리스트링보다 우선).

```js
window.PODO_REPORT_CONTEXT = { studentId: 482913, classId: 77120, studentName: "김포도", tutorId: 331 };
```

**없으면 `null` 로 보냅니다.** 지어내지 않습니다 — 잘못 붙은 리포트보다 저장이 실패하는 편이
낫습니다. 백엔드가 `studentId` 없는 요청을 400 으로 막는 것이 맞습니다.

---

## 2. 요청 본문

전부입니다. 실제로 나가는 바이트는 700 정도입니다.

```jsonc
{
  "source": "korean-trial-report",
  "reportVersion": 2,

  // le_level_test 의 이미 있는 평면 칸. 어드민 목록과 집계가 JSON 을 열지 않고
  // 읽는 자리다 — 리포트를 그리는 쪽은 여기가 아니라 reportSnapshot 을 읽는다.
  "levelTest": {
    "studentId": 482913,
    "classId": 77120,
    "studentName": "김포도",
    "language": "KO",
    "level": 3,
    "levelName": "문장 시작",
    "url": null,
    "job": null,
    "reason": ["kpop", "travel"],
    "studyMethod": null,
    "listening": "5",
    "fluency": "3",
    "pronunciation": "1"
  },
  "tutorId": 331,

  // 리포트를 다시 그리는 데 필요한 입력. 이것만 있으면 앱이 같은 리포트를 그린다.
  "reportSnapshot": {
    "kind": "podo-korean-trial-report",
    "schemaVersion": 1,
    "capturedAt": "2026-08-06T04:21:08.412Z",

    "deck": {
      "lessonId": "trial-1-report",
      "contentVersion": "2026-08-06"
    },

    "answers": {
      "why": ["kpop", "travel"],
      "goal": "t7",
      "pace": 3
    },

    "assessment": {
      "level": 3,
      "areas": { "acc": 3, "voc": 5, "flu": 3, "pron": 1, "lis": 5 }
    },

    "plan": { "perWeek": 3 }
  }
}
```

---

## 3. 필드

### 3.1 봉투

| 필드 | 타입 | 뜻 |
| --- | --- | --- |
| `source` | string | 어느 리포트가 보낸 것인가. 지금은 `"korean-trial-report"` 하나 |
| `reportVersion` | int | 스냅샷의 **모양**을 가르는 번호. `le_level_test.report_version` 으로 들어간다([§5](#5-report_version-과-기존-enjp-스냅샷)) |
| `levelTest` | object | 평면 칸([§4](#4-le_level_test-대응)) |
| `tutorId` | int \| null | 판정한 튜터. 지금 테이블에는 담을 칸이 없다 — [§6](#6-정해야-할-것) |
| `reportSnapshot` | object | 리포트를 다시 그리는 입력 |

### 3.2 `reportSnapshot`

| 필드 | 타입 | 값 | 뜻 |
| --- | --- | --- | --- |
| `kind` | string | `"podo-korean-trial-report"` | JSON 만 따로 떼어 봤을 때 무엇인지 알게 하는 표식 |
| `schemaVersion` | int | `1` | 이 문서의 판. 필드가 사라지거나 뜻이 바뀌면 올린다 |
| `capturedAt` | string | ISO 8601 (UTC) | 튜터가 누른 시각. 저장 시각은 `created_at` 이 따로 찍는다 |
| `deck.lessonId` | string | `"trial-1-report"` | 어느 덱이 보냈나 |
| `deck.contentVersion` | string | `"2026-08-06"` | **어느 판으로 그렸나.** [§3.3](#33-contentversion-이-왜-필요한가) |
| `answers.why[]` | string[] | `kpop` `travel` `friend` `work` `topik` `self` `other` | 학습 동기, 복수 선택. **고른 순서가 뜻을 갖는다** — 첫 번째 동기의 코스가 로드맵 맨 뒤에 선다 |
| `answers.goal` | string | `t3` `t5` `t7` `t9` | 목표. 도착 레벨 3 · 5 · 7 · 9 에 대응한다 |
| `answers.pace` | int \| null | 1–5 | 「학습 페이스」 장에서 고른 주당 횟수 |
| `assessment.level` | int | 1–10 | 튜터가 고른 종합 레벨 |
| `assessment.areas` | object | 키 5개, 값 1–10 | 항목별. `acc` 정확성 · `voc` 어휘 · `flu` 유창성 · `pron` 발음 · `lis` 듣기. 실제로 나오는 값은 1 · 3 · 5 · 7 · 9 다섯뿐이다 |
| `plan.perWeek` | int | 1–7 | **상담 중에 합의한 주당 횟수.** 기간이 이 값에서 나온다 |

`answers.pace` 와 `plan.perWeek` 는 같은 것을 가리키지만 갈릴 수 있습니다. 앞엣것은 학습자가
니즈 장에서 고른 희망이고, 뒤엣것은 리포트의 슬라이더로 상담 중에 합의한 값입니다. **기간을
계산할 때 쓰는 것은 `plan.perWeek` 입니다.**

### 3.3 `contentVersion` 이 왜 필요한가

계산의 재료는 고쳐지는 것입니다 — 레벨 문안, 항목별 문장, `DONE` 표, 코스 길이, 5개월 바닥.
그래서 **6개월 뒤에 같은 입력으로 다시 그린 리포트가 그날 학생이 본 것과 다를 수 있습니다.**

결과를 저장하지 않기로 한 이상 이건 없앨 수 없는 성질이고, 없애려 들면 다시 두 벌 저장으로
돌아갑니다. 대신 **어느 판으로 그린 것인지는 알 수 있어야** 합니다. 그게 이 한 칸입니다.

「그날 화면 그대로」가 법적·영업적으로 꼭 필요해지면, 그때 필요한 것은 이 스키마에 필드를
더하는 게 아니라 **렌더된 리포트 자체를 따로 보관하는 것**입니다(EN/JP 가 `url` 에 PDF 를
두는 것처럼).

---

## 4. `le_level_test` 대응

| 컬럼 | 타입 | 무엇이 들어가는가 |
| --- | --- | --- |
| `student_id` | int NOT NULL | `levelTest.studentId` |
| `class_id` | int | `levelTest.classId` |
| `student_name` | varchar(100) | `levelTest.studentName` |
| `language` | varchar(10) NOT NULL | `"KO"` — **새 값**([§6](#6-정해야-할-것)) |
| `level` | int NOT NULL | `reportSnapshot.assessment.level` (1–10) |
| `level_name` | varchar(50) | `levelTest.levelName` |
| `url` | text | `null` — 이 리포트는 PDF 를 만들지 않는다 |
| `report_version` | smallint | 봉투의 `reportVersion` (`2`) |
| **`report_snapshot`** | **json** | **`reportSnapshot` 통째로. 리포트를 그리는 것은 이 칸이다** |
| `job` | text | `null` — 이 리포트는 직업을 묻지 않는다 |
| `reason` | text | `reportSnapshot.answers.why` 를 고른 순서대로 join (`"kpop,travel"`) |
| `study_method` | text | `null` — 이 리포트는 학습 방법을 묻지 않는다 |
| `listening` | varchar(255) | `reportSnapshot.assessment.areas.lis` — 듣기 레벨을 문자열로 |
| `fluency` | varchar(255) | `reportSnapshot.assessment.areas.flu` — 유창성 |
| `pronunciation` | varchar(255) | `reportSnapshot.assessment.areas.pron` — 발음 |
| `created_at` | timestamp | DB 기본값. 튜터가 누른 시각은 `reportSnapshot.capturedAt` 에 따로 있다 |

**평면 칸과 스냅샷의 역할이 다릅니다.** 평면 칸은 어드민 목록·집계가 JSON 을 열지 않고 읽는
자리이고(그래서 `level`·`listening` 같은 값이 두 곳에 있습니다), **리포트를 그리는 쪽은 언제나
`report_snapshot` 을 읽습니다.** 평면 칸을 보고 화면을 그리면 거기 없는 값(동기·목표·페이스·
정확성·어휘)이 통째로 빠집니다.

**겹치는 값은 서버가 스냅샷에서 꺼내 채웁니다.** 봉투의 `levelTest` 에도 `level`·`listening`·
`fluency`·`pronunciation`·`reason` 이 같이 오지만 서버는 그것을 쓰지 않습니다. 같은 값이 한 행
안에서 두 자리에 저장되는 이상, 둘이 어긋날 수 있는 경로를 아예 없애는 편이 낫기 때문입니다.
덱이 이 다섯을 계속 보내는 것은 규격을 읽는 사람이 평면 칸의 내용을 봉투만 보고 알 수 있게 하기
위함이고, 저장의 정본은 언제나 스냅샷입니다.

`level_name` 만은 스냅샷에 없는데도 덱이 따로 보냅니다 — 레벨에서 나오는 이름이지만 그 표가
`report.js` 안에 있어 백엔드가 스스로 채울 수 없고, 어드민 목록이 읽는 칸이라 비워 둘 수도
없기 때문입니다.

`job` · `study_method` 는 EN/JP 레벨테스트의 니즈 문항이고 한국어 체험 리포트에는 없습니다.
없는 칸을 억지로 채우지 않습니다.

---

## 5. `report_version` 과 기존 EN/JP 스냅샷

`report_snapshot` 은 이미 쓰이고 있습니다. EN/JP 레벨테스트가 `report_version = 1` 로 아래
모양을 넣습니다(podo-pdf 가 씁니다).

```json
{ "cefr": "A1+", "variant": "FULL", "chosenLevel": 2, "evaluatedLevel": 2,
  "totalPoints": 90, "skills": { "fluency": 1, "accuracy": 2, "listening": 2,
  "vocabulary": 2, "pronunciation": 2 }, "weakSkills": ["fluency", "accuracy"],
  "scoreInput": { "questions": [ … ], "feedback": { … } } }
```

한국어 체험 리포트는 **모양이 다른 문서**입니다 — 점수 합산이 없고(튜터가 직접 짚습니다),
대신 니즈와 페이스가 들어 있습니다. 그래서 v1 에 끼워 맞추지 않고 `report_version = 2` 로
가릅니다.

```
report_version = 1  →  EN/JP 레벨테스트 (podo-pdf)
report_version = 2  →  한국어 체험 리포트 (kind: "podo-korean-trial-report")
```

---

## 6. 정해야 할 것

붙이기 전에 백엔드·앱과 맞춰야 하는 것들입니다. **아직 아무것도 정해지지 않았고**, 지금
스크립트는 아래의 첫 번째 안대로 보내고 있습니다.

**앱은 무엇으로 리포트를 그리는가.** 이 규격의 전제입니다 — 저장된 것이 입력뿐이므로,
**앱이 `report.js` 와 같은 계산을 해야 합니다.** 셋 중 하나를 골라야 합니다.

1. 앱이 `runtime/` 을 그대로 웹뷰로 띄운다 (계산이 한 벌로 남는다 — 지금 이 규격이 전제하는 쪽)
2. 계산을 백엔드로 옮기고 덱·앱이 둘 다 API 를 부른다
3. 앱이 계산을 다시 구현한다 (**두 벌이 되고, 언젠가 갈라집니다**)

3번을 고를 거라면 결과도 함께 저장하는 편이 낫습니다 — 그때는 이 문서를 되돌려야 합니다.

**`language = "KO"`.** 지금 이 컬럼에는 `EN` · `JP` 둘뿐이고, 둘 다 **배우는 언어**를 뜻합니다.
한국어 코스도 같은 규칙이면 `KO` 가 맞습니다. 다만 이 리포트의 학습자는 일본어 화자라, 이
컬럼을 **화자의 언어**로 읽어 온 조회 코드가 있다면 그쪽이 깨집니다.

**`level` 이 1–10 이 됩니다.** EN/JP 는 1–9(`SubmitLevelTestRequest` 가 `Level [1-9]` 로 막고
있고 실데이터는 1–8)이고 한국어 리포트는 1–10 입니다. 컬럼은 `int` 라 그대로 들어가지만,
레벨을 이름으로 옮기는 코드는 언어별로 갈라야 합니다.

**`listening` · `fluency` · `pronunciation` 의 눈금이 다릅니다.** EN/JP 는 1–5, 한국어는
1–10(실제로는 1·3·5·7·9)입니다. 이 셋을 가로질러 집계하는 화면이 있으면 언어별로 나눠야
합니다. **정확성·어휘는 평면 칸이 없어 `report_snapshot` 에만 있습니다.**

**`tutor_id` 칸이 없습니다.** 누가 판정했는지는 상담 품질을 되짚을 때 가장 먼저 찾게 되는
값인데 테이블에 자리가 없습니다. 지금은 봉투의 `tutorId` 로 보내고만 있고 받는 쪽이 버립니다.
컬럼을 늘릴지, `class_id` 로 튜터를 거슬러 올라갈지 정해야 합니다.

**서버가 스냅샷을 검증할지.** 입력만 들어 있어 검증이 싸졌습니다 — 코드 값 몇 개와 1–10 범위가
전부입니다. 문안이 아니라 코드라서, **덱의 문안이 바뀌어도 스키마는 그대로입니다.**
보기 자체가 늘거나 줄 때만(`why` 에 새 코드, `goal` 에 새 칸) 맞춰야 합니다.

---

## 7. 확인하는 법

붙기 전에도 눌러 볼 수 있습니다.

1. 리포트를 브라우저로 열고 페이저의 **T**(티칭 모드)를 켭니다 — 저장 칸이 나타납니다.
2. 레벨 체크 · 항목별 다섯 · 동기 · 목표를 채웁니다. 다 채우기 전에는 버튼이 잠겨 있고,
   남은 항목이 버튼 밑에 이름으로 뜹니다.
3. 개발자 도구 Network 탭을 열고 버튼을 누릅니다. 지금 엔드포인트는 닿지 않는 주소라
   요청은 실패하지만, 보내려던 본문은 그 요청에 그대로 들어 있습니다.

콘솔에서 본문만 바로 보려면:

```js
JSON.stringify(window.podoReport.snapshot(), null, 2)
```

`window.podoReport` 는 `snapshot()` · `missing()` · `levelName()` 셋만 엽니다. 레벨표·기간
계산·코스 목록은 `report.js` 클로저 안에 그대로 둡니다 — 밖에서 만질 수 있게 열어 두면 계획의
근거가 두 곳이 됩니다. **앱이 리포트를 다시 그릴 때 쓰는 것도 이 파일이어야 합니다.**
