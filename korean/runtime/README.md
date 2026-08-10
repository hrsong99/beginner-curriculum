# runtime — 덱이 불러 쓰는 것 전부

이 폴더에 있는 것이 **레슨 덱이 실행할 때 불러오는 파일의 전부**입니다. 나머지
(마크업·문서·패키저·참고 자료)는 이 폴더 밖에 있고, 덱은 그것들 없이도 돌아갑니다.

```
runtime/
  css/   lesson-card.css   디자인 시스템 — 모든 트랙이 쓴다
         trial.css         체험 레슨 트랙의 시트 (lesson-card.css 다음에 로드)
  js/    activities.js     점선 칸·고르기·문장 만들기 + lessonSync 스텁
         pager.js          페이지 넘김·스크러버·티칭 모드
         hangul-activities.js / freetalk-activities.js / report.js / report-consult.js
                           과 성격별 활동
         report-submit.js  리포트를 백엔드에 남기는 버튼 (report.js 뒤에 로드)
         highlight.js · spotlight.js · stamp.js · tutor-notes.js · script-lines.js
                           모든 덱이 공통으로 얹는 것들
```

## 왜 한 폴더인가

**곧 공개 저장소로 미러링할 대상이 정확히 이 폴더입니다.** 지금은 덱이 상대
경로로 부르지만(`../../runtime/js/pager.js`), 공개 저장소 + CDN 으로 옮기면
절대 URL 하나만 바뀝니다. 무엇이 나가고 무엇이 남는지를 폴더 경계로 못박아
두면, 미러링 규칙이 "이 폴더를 그대로"가 되어 목록을 손으로 관리할 일이 없습니다.

공개해도 되는 것만 둡니다 — 여기 있는 파일에는 교재 스캔도, 가격도, 내부 메모도
없습니다. 그런 것이 이 폴더에 들어가려 하면 그건 런타임이 아닙니다.

## 옮길 때 (아직 아님)

1. 이 폴더를 공개 저장소(`podo-lesson-runtime` 같은)로 미러링하는 액션을 붙입니다.
2. 버전은 **경로로** 끊습니다 — `…/v1/js/pager.js`. 이미 올라간 덱이 조용히
   바뀌지 않도록, 한 번 올린 경로는 덮어쓰지 않습니다.
3. 덱의 `<link>` · `<script src>` 를 그 URL 로 바꿉니다. 패키저는 절대 URL 을
   건드리지 않고 그대로 두므로(`podo-curriculum` 의 `docs/packaging.md`), zip 은 자동으로
   HTML + 이미지만 남습니다.
4. 덱을 새 버전으로 올리는 것은 그때마다 **의도적으로** 합니다. 그게 이 방식의
   요점입니다 — 수업 중인 화면이 배포 때문에 바뀌지 않습니다.

## 규칙

- **덱은 인라인 CSS·JS 를 갖지 않습니다.** 새로 필요한 것이 생기면 여기에
  넣고 공유합니다. 한 덱에만 둔 수정은 그 덱에만 남습니다 — 스크러버와
  스크롤바 자리가 실제로 그렇게 한 덱에만 있었습니다.
- **로드 순서가 있습니다.** `activities` → `pager` → `script-lines` →
  `spotlight` → `tutor-notes` → `highlight` → `stamp`. 이유는 각 파일 머리말에
  적혀 있고, 덱 뼈대는 [`AUTHORING.md`](../AUTHORING.md) 에 있습니다.
- **CSS 는 두 장이 한 벌입니다.** `lesson-card.css` 다음에 트랙 시트. 패키저가
  링크 순서대로 이어 붙이므로 순서가 곧 캐스케이드입니다.
