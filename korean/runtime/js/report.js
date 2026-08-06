/* ================================================================
   REPORT · 체험 레슨 리포트와 안내 페이지의 배선 (공유 스크립트)

     .lvcheck      10단계 레벨 체크 — 고르면 접힌다
     .axsteps      항목별 진단 다섯 줄 + 레이더
     .tcon         목표 레벨까지 · 커리큘럼 로드맵
     .fold         길어지는 카드의 더 보기

   튜터가 수업 중에 채우고, 그 결과가 학습자 화면에도 그대로 간다.
   레슨 활동(activities.js)과 겹치는 마크업이 없으므로 둘을 같이 불러도
   서로를 건드리지 않는다.
   ================================================================ */

(function () {
  // 로드맵의 칸은 클로저에 있어 DOM 만으로는 읽을 수 없다 — register 로 넘긴다
  var sync = window.lessonSync;

  /* ---------- 10단계 레벨 ----------
     사내 레벨표(CEFR·JLPT 대응)를 한국어 학습으로 옮긴 것이다. 눈금 10칸이
     곧 레벨 1~10 이고, 튜터가 고른 이 값이 리포트 전체의 기준점이 된다.
     출처: Figma「❤️ PODO JP」> 일본어 리포트 > 레벨표.
     한 레벨에 그림 한 장(assets/levels/lv-N.png) — 열 장이 한 줄로 이어지는
     성장 그림이라, 번호가 아니라 그림만 봐도 어디쯤인지 읽힌다. */
  var LADDER_STEPS = 10;
  var LV = {
    "1":  { name: "첫걸음",
            line: '한글을 <b>하나씩 읽어요</b>',
            diag: '간단한 인사와 자기소개는 <b>따라 말할 수 있어요.</b> 아직 글자를 붙여 읽는 게 느리고, 문장은 한 번에 하나씩 나와요. 지금은 소리와 글자를 손에 익히는 단계예요.',
            cert: ["1급", "준비 단계 · 아직 응시 전"] },
    "2":  { name: "글자 떼기",
            line: '한글을 <b>막힘 없이 읽어요</b>',
            diag: '받침이 있는 글자까지 <b>소리 내어 읽어요.</b> 일상적인 주제로 짧은 대화가 오가고, 가게에서 메뉴를 물어보는 정도는 돼요. 아직 아는 단어가 적어서, 읽어도 뜻이 바로 붙지는 않아요.',
            cert: ["1급", "기본 인사와 소개 가능"] },
    "3":  { name: "문장 시작",
            line: '원하는 대로 <b>주문할 수 있어요</b>',
            diag: '배운 패턴으로 <b>짧은 문장을 스스로 만들어요.</b> 가게에서 원하는 대로 주문하고, 가족·친구·취미처럼 익숙한 주제로 간단히 이야기해요. 조사와 말끝은 아직 자주 흔들려요.',
            cert: ["2급", "한국어로 일상 회화 가능"] },
    "4":  { name: "일상 회화",
            line: '여행에서 <b>혼자서도 괜찮아요</b>',
            diag: '익숙한 주제라면 <b>주고받는 대화가 이어져요.</b> 여행지에서 만난 한국인과 가벼운 수다도 가능해요. 낯선 화제로 넘어가면 말이 끊기고, 문법도 말할 때는 자주 흔들려요.',
            cert: ["2급", "익숙한 주제로 대화 가능"] },
    "5":  { name: "대화의 폭",
            line: '익숙한 주제를 <b>구체적으로 말해요</b>',
            diag: '익숙한 주제를 <b>더 구체적이고 분명하게 말해요.</b> 일 이야기도 가벼운 스몰톡 정도는 오가요. 아직 표현의 폭이 좁아 같은 말이 반복돼요.',
            cert: ["3급", "일상 · 업무 대화 가능"] },
    "6":  { name: "내 생각",
            line: '이유를 붙여 <b>내 의견을 말해요</b>',
            diag: '자기 생각에 <b>이유를 붙여 말할 수 있어요.</b> 가벼운 사회 이슈로도 의견을 주고받아요. 긴 이야기는 아직 앞뒤가 느슨해져요.',
            cert: ["3~4급", "이유를 붙여 의견 전달 가능"] },
    "7":  { name: "논리",
            line: '추상적인 주제도 <b>논리적으로 말해요</b>',
            diag: '추상적인 주제로도 <b>깊은 대화가 이어져요.</b> 사회 이슈를 두고 원어민과 논리적으로 설명하고 되받을 수 있어요. 어휘 선택은 아직 무난한 쪽으로 몰려요.',
            cert: ["4급", "사회 주제도 설명 가능"] },
    "8":  { name: "자연스러움",
            line: '다양한 표현으로 <b>흐름을 이어가요</b>',
            diag: '다양한 어휘와 표현을 쓰며 <b>대화의 흐름이 자연스러워요.</b> 한국에서 일하게 되어도 빠르게 적응할 수 있는 수준이에요.',
            cert: ["4~5급", "자연스러운 흐름으로 대화 가능"] },
    "9":  { name: "유학파",
            line: '복잡한 이야기도 <b>바로 알아들어요</b>',
            diag: '복잡한 내용으로 <b>심층적인 논의가 가능해요.</b> 전문적인 어휘를 쓰고, 어려운 글의 함축적인 의미까지 읽어내요.',
            cert: ["5급", "전문적인 내용도 이해 가능"] },
    "10": { name: "전문가",
            line: '어떤 자리에서도 <b>막힘이 없어요</b>',
            diag: '까다로운 주제로 <b>깊이 있는 토론이 가능해요.</b> 전문 분야에서도 자유롭게 소통하고, 전문 지식이 필요한 글도 서슴없이 읽고 말해요.',
            cert: ["6급", "어떤 자리에서도 자유롭게 소통"] }
  };

  /* ---------- 항목별 문안 ----------
     출처: 같은 Figma 파일의 항목 × 레벨대 표(1~2 / 3~4 / 5~6 / 7~8 / 9~10).
     문장은 그대로 두고 대상 언어만 한국어로 옮겼다. 한 칸이 두 레벨을
     덮으므로 색인은 ceil(lv / 2) 다.
     HINT 는 같은 표의 "OO을 보완하려면?" 문단을 한 줄로 줄인 것. */
  var AREAS = [
    { k: "acc",  n: "정확성" },
    { k: "voc",  n: "어휘" },
    { k: "flu",  n: "유창성" },
    { k: "pron", n: "발음" },
    { k: "lis",  n: "듣기" }
  ];
  /* 항목별 문안은 아래 항목별 체크의 보기 다섯 줄이 원본이다. 보기 하나가
     두 문장을 든다: 버튼에 보이는 짧은 말은 튜터가 수업 직후에 고르는
     관찰("가끔 틀렸어요")이고, data-say 는 그 관찰을 학습자가 읽을 문장으로
     옮긴 것이다. 리포트는 뒤엣것을 쓴다 — 표를 여기 또 적지 않고 DOM 에서
     읽으므로, 튜터가 고른 칸과 리포트에 실리는 문장이 어긋날 수 없다. 한 칸이 두 레벨(1–2 · 3–4 …)을 덮으므로 색인은
     (lv - 1) / 2 이고, band() 가 짝수 값이 들어와도 같은 칸으로 접는다. */
  var BAND = {};
  document.querySelectorAll(".axq").forEach(function (q) {
    BAND[q.getAttribute("data-ax")] = [].map.call(
      q.querySelectorAll(".axq-opts button"),
      function (b) { return b.getAttribute("data-say"); });
  });

  /* 코멘트에 들어갈 「무엇을 하면 느는가」. HINT 와 따로 두는 이유는 꼴이
     달라서다 — HINT 는 목록에 놓이는 「…하기」 이고, 이쪽은 문장 가운데에
     들어가 「…것이 중요해요」 로 닫힌다. */
  var GROW = {
    acc: "단어와 문법의 뜻·쓰임을 정확히 알고, 맞는 상황에서 직접 써 보는 것",
    voc: "많이 읽어 단어를 알고, 그 단어를 대화에서 실제로 써 보는 것",
    flu: "여러 사람과 자주 주고받으며 말하는 양을 늘리는 것",
    pron: "원어민의 발음과 억양을 많이 듣고 그대로 따라 해 보는 것",
    lis: "여러 속도와 억양에 익숙해질 때까지 자주 들어 보는 것"
  };
  /* 받침이 있으면 과/이, 없으면 와/가. 항목 이름이 다섯뿐이라 표로 둘 수도
     있지만, 코멘트가 이름을 조합해 문장을 만들므로 규칙으로 두는 편이 안전하다. */
  function hasBatchim(word) {
    var c = word.charCodeAt(word.length - 1) - 0xac00;
    return c >= 0 && c <= 11171 && c % 28 !== 0;
  }
  function josa(word, withT, withoutT) { return word + (hasBatchim(word) ? withT : withoutT); }

  var HINT = {
    flu: "다양한 상황에서 소통하는 경험을 늘리기 — 사람과 한국어로 주고받은 양이 그대로 유창성이 돼요.",
    acc: "단어와 문법의 정확한 뜻·쓰임을 이해하고, 맞는 상황에서 직접 써 보며 충분히 연습하기.",
    pron: "정확한 발음·억양·리듬을 쓰는 원어민의 한국어를 많이 듣고, 그대로 따라 하며 내 것으로 만들기.",
    lis: "한국어의 다양한 억양과 속도에 친숙해지기 — 빠르게 말해도 들릴 때까지 여러 사람과 대화해 보기.",
    voc: "많이 읽어 단어를 알고, 그 단어가 어떤 맥락에서 쓰이는지 원어민과 대화하며 계속 익히기."
  };

  /* ---------- 견줄 자리 ----------
     포도 수강생 전체의 항목별 평균. 목표선 대신 이걸 옆에 두는 이유는, 처음
     온 사람에게 "Lv.3" 은 아무 크기도 아니어서다 — 옆에 사람이 서 있어야
     비로소 높이가 보인다.

     다섯 값이 고르지 않은 건 일본어 화자가 한국어를 배울 때 실제로 그렇게
     기울기 때문이다. 어휘가 가장 높다(한자어가 그대로 겹친다: 約束-약속,
     無理-무리). 정확성이 그다음 — 어순도 조사도 경어도 거의 같은 자리에
     있어서 문장 구조가 일찍 잡힌다. 듣기는 겹치는 어휘 덕에 중간.
     유창성은 알아듣는 것보다 늘 늦게 오고, 발음이 가장 낮다: 모음이 5개뿐이라
     ㅓ/ㅗ·ㅜ/ㅡ가 붙고, 평음·경음·격음 3항 대립이 없으며, 받침이 없다.
     TODO(데이터): 실제 코호트 수치가 나오면 숫자만 갈아끼운다 —
     레이더와 막대가 함께 따라간다. */
  var AVG = { voc: 4.4, acc: 3.8, lis: 3.4, flu: 2.9, pron: 2.3 };

  /* ---------- 목표 ----------
     학습 동기 하나가 사다리 하나고, 그 사다리의 세 칸이 여기 세 줄이다.
     lv 는 그 목표가 도착하는 레벨이고, 걸리는 레슨 수는 따로 두지 않고
     DONE[lv] 에서 읽는다 — 같은 레벨인데 어느 줄을 눌렀느냐로 기간이
     달라지면 튜터가 설명할 수 없다. */
  var GOALS = {
    t3: { lv: 3, t: "짧은 문장으로 전하기" },
    t5: { lv: 5, t: "익숙한 주제로 대화 이어가기" },
    t7: { lv: 7, t: "의견도 이유도 말하기" },
    t9: { lv: 9, t: "어떤 주제든 자유롭게 말하기" }
  };
  // 이유 -> 그 이유를 실제로 채워 주는 상황별 코스. 목표 카드는 거리만
  // 정하고, 길에 무엇을 깔지는 이유가 정한다.
  var WHY_COURSE = { travel: "travel", kpop: "drama", friend: "banmal",
                     self: "travel", work: "free", topik: "free" };
  // the tutor's level call -> lessons already effectively covered.
  var DONE = { "1": 0, "2": 11, "3": 25, "4": 45, "5": 70,
               "6": 90, "7": 110, "8": 130, "9": 150, "10": 170 };

  // 이름과 순서는 뒤의 「커리큘럼」 장과 같다 — 리포트가 추천한 코스를
  // 그 장에서 그대로 짚어 설명할 수 있어야 한다.
  // s   = 그 코스가 뭘 하는 곳인지 한 줄
  // can = 그 코스를 마치면 할 수 있게 되는 말
  // ex  = 그 말을 예문 하나로 푼 것
  var COURSE = {
    hangul: { w: 1, t: "한글 읽기",   s: "글자를 소리 내어 읽는 법",
              can: "간판이 읽혀요",
              ex: "카페 · 김밥 · 화장실 — 거리에서 보이는 글자를 소리 내어 읽어요" },
    core:   { w: 3, t: "핵심 패턴",   s: "하고 싶은 말을 스스로 만드는 법",
              can: "내 이야기를 말해요",
              ex: "「저는 일본 사람입니다」처럼, 배운 틀에 내 단어를 넣어 문장을 만들어요" },
    travel: { w: 2, t: "상황별 · 여행",   s: "가게에서 · 길에서 진짜 쓰는 말",
              can: "가게에서 말해요",
              ex: "「혹시 명동역이 어딘지 아세요?」 길을 묻고, 주문하고, 되물어요" },
    drama:  { w: 2.4, t: "상황별 · 드라마", s: "좋아하는 드라마의 진짜 대사",
              can: "자막 없이 들려요",
              ex: "「우리 어디서 본 적 있지 않아요?」 드라마에 나오는 말이 그대로 들려요" },
    banmal: { w: 2, t: "상황별 · 반말 수다",   s: "친구에게 쓰는 편한 반말",
              can: "반말로 수다 떨어요",
              ex: "「너 지금 어디 가는 거야?」 친구에게 말을 놓고 편하게 이야기해요" },
    free:   { w: 2.4, t: "프리토킹", s: "문법이 아니라 생각을 말하기",
              can: "이유까지 말해요",
              ex: "「돈 vs 시간, 하나만 가질 수 있다면?」 생각과 그 이유를 이어서 말해요" }
  };
  var pick = { why: [], goal: null, pace: null, level: null };

  /* ---- the answer groups remember what was chosen ---- */
  document.querySelectorAll("[data-group]").forEach(function (group) {
    var key = group.getAttribute("data-group");
    var multi = group.getAttribute("data-pick") === "multi";
    group.querySelectorAll("button[data-val]").forEach(function (b) {
      b.addEventListener("click", function () {
        var v = b.getAttribute("data-val");
        if (multi) {
          b.classList.toggle("on");
          pick[key] = [].slice.call(group.querySelectorAll("button.on"))
                        .map(function (x) { return x.getAttribute("data-val"); });
        } else {
          var was = b.classList.contains("on");
          group.querySelectorAll("button").forEach(function (x) { x.classList.remove("on"); });
          if (!was) b.classList.add("on");
          pick[key] = was ? null : v;
        }
        // 항목 하나를 고르면 「고치는 중」 은 끝난다 — 다음 항목이 열린다
        if (key.indexOf("ax-") === 0) editing = null;
        if (key === "level") lvEditing = false;
        render();
      });
    });
  });

  /* ---- 지금 서 있는 레벨들 ----
     종합은 아직 안 골랐으면 1 — 레벨 체크의 "대부분 1이에요" 가 말하는 그
     기본값이다. 항목별은 손대지 않았으면 종합을 그대로 따라간다. */
  function overall() { return clamp(Number(pick.level || 1)); }
  /* 아직 안 고른 항목은 0 이다 — 종합 레벨로 대신 채우지 않는다. 채워 두면
     레벨을 고르는 순간 오각형이 이미 완성돼 버려서, 튜터가 다섯 항목을
     고르는 동안 학습자 화면에서는 아무 일도 일어나지 않는다. 종합 레벨은
     이제 보기 옆의 「추천」 으로만 남는다: 제안이지 값이 아니다. */
  function areaLv(k) { var v = Number(pick["ax-" + k]); return v ? clamp(v) : 0; }
  function rated(k) { return !!pick["ax-" + k]; }
  function allRated() { return AREAS.every(function (a) { return rated(a.k); }); }
  function clamp(n) { return Math.max(1, Math.min(LADDER_STEPS, n || 1)); }
  // 한 칸이 두 레벨을 덮는다: 1–2 → 0, 3–4 → 1 … 9–10 → 4
  function band(lv) { return Math.max(0, Math.ceil(clamp(lv) / 2) - 1); }
  // 10칸 사다리 위의 자리. 평균은 2.6 처럼 칸 사이에 서므로 칸 중앙이 아니라
  // 눈금값 그대로 재야 레이더(반지름 = lv/10)와 같은 곳을 가리킨다.
  function pct(lv) { return lv ? clamp(lv) * 10 : 0; }
  // 항목을 잘하는 순으로. 「좋아요/아쉬운 점」·막대 색·추천이 모두 이 한
  // 줄에서 나오므로, 세 곳이 서로 다른 항목을 가리키는 일이 없다.
  function ranked() {
    return AREAS.filter(function (a) { return rated(a.k); })
                .sort(function (a, b) { return areaLv(b.k) - areaLv(a.k); });
  }

  /* ---- 날짜 ----
     리포트 머리글의 날짜와 수강료 쿠폰의 마감일은 같은 "오늘" 에서 나온다.
     상담은 오늘 하는 것이라, 문서에 날짜를 적어 두면 반드시 어긋난다. */
  var DOW = ["일", "월", "화", "수", "목", "금", "토"];
  function stampDates() {
    var d = new Date(), el = document.querySelector(".rm-date");
    if (el) {
      el.textContent = d.getFullYear() + "." +
        String(d.getMonth() + 1).padStart(2, "0") + "." +
        String(d.getDate()).padStart(2, "0");
    }
    // 쿠폰은 오늘 포함 나흘째 자정에 닫힌다(D+3)
    var end = new Date(d.getTime() + 3 * 86400000);
    var big = document.querySelector(".dl-date");
    if (big) big.textContent = (end.getMonth() + 1) + "월 " + end.getDate() + "일(" +
      DOW[end.getDay()] + ") 23:59";
    var cells = document.querySelectorAll(".dl-days > div");
    for (var i = 0; i < cells.length; i++) {
      var x = new Date(d.getTime() + i * 86400000);
      cells[i].querySelector(".d").textContent = (x.getMonth() + 1) + "/" + x.getDate();
      if (i > 0 && i < cells.length - 1) cells[i].querySelector(".w").textContent = DOW[x.getDay()];
    }
  }

  /* ---- 레벨 체크는 고르고 나면 접힌다 ----
     고른 뒤에도 다섯 줄이 펼쳐져 있으면, 카드에서 정작 봐야 할 것(레벨과
     근거)보다 고르는 칸이 더 길다. 접으면 고른 한 줄만 남는다.
     「다시 고르기」 는 이 화면만의 상태라 공유하지 않는다 — 튜터가 무엇을
     열어 두었는지는 학습자와 아무 상관이 없다. */
  var lvEditing = false;
  var lvcheck = document.querySelector(".lvcheck");
  if (lvcheck) {
    lvcheck.querySelector(".lvcheck-redo").addEventListener("click", function () {
      lvEditing = true;
      render();
    });
  }

  function renderLevelPick() {
    if (!lvcheck) return;
    lvcheck.classList.toggle("folded", !!pick.level && !lvEditing);
  }

  /* ---- 항목별 체크 · 한 번에 한 항목 ----
     다음 차례는 「아직 안 고른 첫 항목」 이다 — 어디까지 했는지를 따로 세지
     않으니 되돌아가 고쳐도 순서가 꼬이지 않는다. 칩을 누르면 그 항목을 다시
     열고(editing), 고르는 순간 다시 자동 진행으로 돌아간다.
     editing 은 공유하지 않는다: 튜터가 지금 어느 칸을 보고 있는지는 튜터의
     화면 사정이고, 학습자에게는 이 블록 자체가 없다. */
  var editing = null;
  var steps = document.querySelector(".axsteps");
  var chips = steps && steps.querySelector(".axst-chips");

  if (chips) {
    chips.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-ax]");
      if (!b) return;
      editing = b.getAttribute("data-ax");
      render();
    });
  }

  function renderAxSteps() {
    if (!steps) return;
    var nextUp = null;
    AREAS.forEach(function (a) { if (!nextUp && !pick["ax-" + a.k]) nextUp = a.k; });
    var open = editing || nextUp;

    chips.innerHTML = "";
    AREAS.forEach(function (a) {
      var own = pick["ax-" + a.k];
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("data-ax", a.k);
      b.className = (own ? "done" : "") + (a.k === open ? " now" : "");
      b.textContent = a.n;
      chips.appendChild(b);
    });

    steps.querySelectorAll(".axq").forEach(function (q) {
      var k = q.getAttribute("data-ax");
      q.classList.toggle("now", k === open);
      /* 종합 레벨과 같은 칸을 「추천」 으로 짚어 준다. 값을 넣지는 않는다 —
         튜터가 눌러야 값이 된다. 이미 고른 항목에는 표시하지 않는다:
         고른 뒤에도 남으면 자기가 고른 것과 제안이 헷갈린다. */
      q.querySelectorAll(".rung-row").forEach(function (b) {
        b.classList.toggle("sug",
          !rated(k) && Number(b.getAttribute("data-val")) === overall());
      });
    });
    steps.classList.toggle("all", !nextUp && !editing);
  }

  /* ---- ① 내 레벨 카드 ---- */
  var card = document.querySelector(".lvcard");

  function renderLevel() {
    if (!card) return;
    var n = overall(), d = LV[String(n)];
    card.querySelector(".lvbig-n b").textContent = "Lv." + n;
    card.querySelector(".lvbig-l").innerHTML = d.line;
    card.querySelector(".lvbig-img").src = "../assets/levels/lv-" + n + ".png";
    card.querySelector(".lvbig-img").alt = "Lv." + n + " · " + d.name;
    card.querySelector(".topikrow i").textContent = "TOPIK " + d.cert[0];
    card.querySelector(".topikrow span").textContent = d.cert[1];

    /* 근거는 실제로 체크한 항목에서만 나온다 — 가장 잘 되는 둘. 아직 하나도
       체크하지 않았으면 근거 칸 자체를 비워 둔다: 없는 근거를 지어내느니
       레벨과 한 줄 설명만 보이는 편이 낫다. */
    var top2 = ranked().slice(0, 2), ul = card.querySelector(".lv-ev");
    ul.innerHTML = "";
    ul.classList.toggle("hide", !top2.length);
    top2.forEach(function (a) {
      var li = document.createElement("li");
      li.innerHTML = '<i>✓</i><span>' + a.n + " · " + BAND[a.k][band(areaLv(a.k))] + '</span>';
      ul.appendChild(li);
    });
  }

  /* ---- ② 항목별 진단 · 레이더 + 다섯 줄 ---- */
  var bars = document.querySelector(".axbars");

  function renderAspects() {
    growRadar();
    if (!bars) return;
    var order = ranked();

    // 다섯 줄은 언제나 같은 순서(정확성→듣기)로 선다. 순위대로 세우면
    // 튜터가 값을 고칠 때마다 줄이 자리를 바꿔, 어디를 보는지 놓친다.
    bars.innerHTML = "";
    AREAS.forEach(function (a) {
      var row = document.createElement("div");
      row.className = "axb";
      // 평균은 두 번째 막대가 아니라 눈금 하나다 — 막대 둘을 겹쳐 놓으면
      // 어느 쪽이 내 것인지 매번 범례를 봐야 한다.
      row.innerHTML = '<span class="axb-n">' + a.n + '</span>' +
        '<span class="axb-t"><i class="axb-f" style="width:' + pct(areaLv(a.k)) + '%"></i>' +
        '<b class="axb-avg" style="left:' + pct(AVG[a.k]) + '%"></b></span>';
      bars.appendChild(row);
    });

    /* 다섯을 다 보기 전에는 잘하는 쪽도 아쉬운 쪽도 말할 수 없고, 다섯이
       모두 같으면 말할 것이 없다. 둘 중 하나라도 걸리면 두 상자를 접는다 —
       아직 안 본 항목을 약점이라고 말해 버리는 것이 가장 나쁜 결과다. */
    var flat = !order.length || !allRated() ||
               areaLv(order[0].k) === areaLv(order[order.length - 1].k);
    document.querySelector(".axsum").classList.toggle("hide", flat);
    document.querySelector(".axtip").classList.toggle("hide", flat);
    if (flat) return;

    var good = document.querySelector(".axs:not(.weak) ul");
    var weak = document.querySelector(".axs.weak ul");
    good.innerHTML = ""; weak.innerHTML = "";
    order.slice(0, 2).forEach(function (a) { good.innerHTML += "<li>" + a.n + "</li>"; });
    order.slice(-2).forEach(function (a) { weak.innerHTML += "<li>" + a.n + "</li>"; });

    /* 코멘트는 위 두 상자를 한 문장으로 잇는다: 잘하는 둘을 이름으로 부르고,
       아쉬운 둘을 기르는 방법을 붙인다. 방법은 가장 처지는 항목의 HINT 다 —
       둘 다 적으면 문단이 길어지고, 튜터가 읽어 줄 말이 아니게 된다. */
    var good2 = order.slice(0, 2), weak2 = order.slice(-2);
    // 이름을 이을 때도 문장을 닫을 때도 앞말의 받침을 따라간다
    var nm = function (xs) {
      return xs.map(function (a, i) {
        var b = "<b>" + a.n + "</b>";
        return i < xs.length - 1 ? b + (hasBatchim(a.n) ? "과 " : "와 ") : b;
      }).join("");
    };
    var lastOf = function (xs) { return xs[xs.length - 1].n; };
    document.querySelector(".axtip p").innerHTML =
      "포도님은 " + nm(good2) + (hasBatchim(lastOf(good2)) ? "이" : "가") + " 좋은 편이에요.<br>" +
      nm(weak2) + (hasBatchim(lastOf(weak2)) ? "을" : "를") + " 키우려면 " +
      GROW[order[order.length - 1].k] + "이 중요해요.";
  }

  /* 오각형. 지금(초록 채움)은 튜터가 고른 항목별 레벨, 점선 외곽은 체험
     수업을 받은 분들의 평균이다. 평균은 배경 쪽 정보라 점만 찍지 않고
     윤곽선으로만 두고, 초록 면을 그 위에 얹는다. */
  var svg = document.getElementById("radar");

  /* 지금 화면에 그려져 있는 값. 목표값(areaLv)과 따로 두는 이유는 항목을
     하나 고를 때마다 그 축이 자라나는 게 보여야 해서다 — 튜터는 고르고,
     학습자는 자기 오각형이 커지는 걸 본다. 0 에서 시작하므로 첫 그림도
     가운데에서 피어난다. */
  var shown = {};
  AREAS.forEach(function (a) { shown[a.k] = 0; });
  var raf = null;
  var still = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function growRadar() {
    var from = {}, to = {}, moved = false;
    AREAS.forEach(function (a) {
      from[a.k] = shown[a.k];
      to[a.k] = areaLv(a.k);
      if (Math.abs(to[a.k] - from[a.k]) > 0.01) moved = true;
    });
    if (!moved) { drawRadar(); return; }
    if (still) {
      AREAS.forEach(function (a) { shown[a.k] = to[a.k]; });
      drawRadar();
      return;
    }
    if (raf) cancelAnimationFrame(raf);
    var t0 = null, DUR = 420;
    raf = requestAnimationFrame(function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min(1, (ts - t0) / DUR);
      var e = 1 - Math.pow(1 - p, 3);          // 빠르게 나갔다 부드럽게 멎는다
      AREAS.forEach(function (a) { shown[a.k] = from[a.k] + (to[a.k] - from[a.k]) * e; });
      drawRadar();
      raf = p < 1 ? requestAnimationFrame(step) : null;
    });
  }

  function drawRadar() {
    if (!svg) return;
    var cx = 100, cy = 100, R = 82, N = AREAS.length, NS = "http://www.w3.org/2000/svg";
    svg.innerHTML = "";
    var el = function (t, at) {
      var e = document.createElementNS(NS, t);
      for (var k in at) e.setAttribute(k, at[k]);
      return e;
    };
    var P = function (i, f) {
      var a = -Math.PI / 2 + i * 2 * Math.PI / N;
      return [cx + Math.cos(a) * R * f, cy + Math.sin(a) * R * f];
    };
    var poly = function (pts) {
      return pts.map(function (p) { return p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ");
    };
    var i, p, e, lp, t, d;
    [0.25, 0.5, 0.75, 1].forEach(function (f) {
      p = [];
      for (i = 0; i < N; i++) p.push(P(i, f));
      svg.appendChild(el("polygon", { points: poly(p), fill: "none", stroke: "#f0efec", "stroke-width": "1" }));
    });
    for (i = 0; i < N; i++) {
      e = P(i, 1);
      svg.appendChild(el("line", { x1: cx, y1: cy, x2: e[0], y2: e[1], stroke: "#f0efec", "stroke-width": "1" }));
      lp = P(i, 1.18);
      t = el("text", { x: lp[0].toFixed(1), y: (lp[1] + 4).toFixed(1), "font-size": "11.5",
                       "font-weight": "700", fill: "#2b2b2b",
                       "text-anchor": lp[0] > cx + 4 ? "start" : (lp[0] < cx - 4 ? "end" : "middle") });
      t.textContent = AREAS[i].n;
      svg.appendChild(t);
    }
    var ap = [];
    for (i = 0; i < N; i++) ap.push(P(i, AVG[AREAS[i].k] / LADDER_STEPS));
    svg.appendChild(el("polygon", { points: poly(ap), fill: "none", stroke: "#b4b4b0",
                                    "stroke-width": "1.5", "stroke-dasharray": "4 3",
                                    "stroke-linejoin": "round" }));
    var np = [];
    for (i = 0; i < N; i++) np.push(P(i, shown[AREAS[i].k] / LADDER_STEPS));
    svg.appendChild(el("polygon", { points: poly(np), fill: "rgba(106,190,54,.20)", stroke: "#6abe36",
                                    "stroke-width": "1.75", "stroke-linejoin": "round" }));
    for (i = 0; i < N; i++) {
      d = P(i, shown[AREAS[i].k] / LADDER_STEPS);
      svg.appendChild(el("circle", { cx: d[0].toFixed(1), cy: d[1].toFixed(1), r: "2.6",
                                     fill: "#6abe36", stroke: "#fff", "stroke-width": "1" }));
    }
  }

  /* ---- 학습 순서는 한 곳에서만 정해진다 ----
     ④-A 시작 커리큘럼 카드, 그래프의 마디, 아래 학습 순서 카드가 모두 이
     목록을 읽는다. 세 곳이 각자 고르면 언젠가 서로 다른 코스를 말한다.
     무엇을 배우는지는 이유가, 어디까지 가는지는 목표가 정한다. 상황별은
     둘까지만 얹는다 — 마디가 다섯이 되면 그래프 라벨이 서로 겹치고,
     학습 순서라기보다 목록이 된다. */
  function courseList(goalLv) {
    var lv = overall();
    var extras = [], why0 = pick.why && pick.why.length ? pick.why[0] : null;
    (pick.why || []).forEach(function (w) {
      var k = WHY_COURSE[w];
      if (k && extras.indexOf(k) < 0) extras.push(k);
    });
    // Lv.8 위는 프리토킹 없이 설명이 안 되는 높이라, 그 자리를 비워 둔다
    extras = goalLv >= 8
      ? extras.filter(function (k) { return k !== "free"; }).slice(0, 1).concat("free")
      : extras.slice(0, 2);
    // 첫 번째 이유의 코스는 맨 뒤로. 마지막 마디가 곧 「목표」 라서, 리포트가
    // 부르는 목표 이름과 다른 코스가 끝에 서면 도착점이 두 개로 읽힌다.
    var mainC = why0 && WHY_COURSE[why0];
    if (mainC && extras.length > 1 && extras.indexOf(mainC) >= 0 && extras[extras.length - 1] !== "free") {
      extras = extras.filter(function (k) { return k !== mainC; }).concat(mainC);
    }
    // never recommend a course the learner has already passed
    var all = ["hangul", "core"].concat(extras);
    var out = all.filter(function (k) {
      if (k === "hangul") return lv < 2;
      if (k === "core") return lv < 5;
      return true;
    });
    return out.length ? out : [all[all.length - 1]];
  }

  /* ---- ③ 원하는 레벨까지 ----
     주당 횟수는 앞의 「학습 페이스」 장에서 한 번 정해지고, 여기 슬라이더가
     그 값을 이어받아 실제로 굴린다. 둘은 같은 것을 가리키므로 한쪽을 움직이면
     다른 쪽도 따라간다 — 상담 중에 「그럼 주 6회면요?」 를 손으로 답하는 자리다. */
  var freq = document.querySelector(".freq-range");
  if (freq) {
    freq.addEventListener("input", function () {
      pick.pace = freq.value;
      render();
    });
  }
  function perWeek() { return Number((freq && freq.value) || pick.pace || 3); }

  var rcourse = document.querySelector(".freq");
  var rjCourse = document.querySelector(".rj-course");

  function renderCourseCard() {
    if (!rcourse) return;
    var g = GOALS[pick.goal];
    // 페이스는 슬라이더가 늘 값을 들고 있으므로, 비어 있을 수 있는 건 목표뿐이다
    if (!g) {
      rcourse.classList.add("hide");
      document.querySelector(".tiles").classList.add("hide");
      if (rjCourse) {
        rjCourse.classList.remove("hide");
        rjCourse.href = "#p-goal";
        rjCourse.querySelector(".rj-t").textContent = "목표를 아직 안 골랐어요";
      }
      return;
    }
    rcourse.classList.remove("hide");
    document.querySelector(".tiles").classList.remove("hide");
    if (rjCourse) rjCourse.classList.add("hide");

    var per = perWeek();
    var need = Math.max(6, DONE[String(g.lv)] - DONE[String(overall())]);
    var mo = months(need, per);
    if (freq) freq.value = per;
    rcourse.querySelector(".freq-n").textContent = per;
    var bub = rcourse.querySelector(".freq-bub");
    bub.textContent = per + "회";
    // 말풍선이 손잡이를 따라간다. 양 끝에서는 손잡이 반지름만큼 안으로 당겨
    // 카드 밖으로 새지 않게 한다.
    bub.style.left = "calc(" + ((per - 1) / 6 * 100) + "% + " + (8 - (per - 1) / 6 * 16) + "px)";
    document.querySelector(".eta").textContent = mo + "개월";
  }

  /* ---- ④ 커리큘럼 로드맵 ----
     길은 Figma 삽화 그대로 고정된 뱀 모양이고 점이 일곱이다. 다음/이전은 그
     점을 하나씩 밟는다 — 칸을 코스 수로 나누면 추천이 두 코스일 때 점 일곱 중
     다섯이 아무도 서지 않는 자리가 된다. 그림에 점이 일곱이면 걸음도 여섯이다.
     칸 i 는 여정의 i/6 지점이라 모퉁이 점(2·4·6)이 정확히 ⅓·⅔·끝에 떨어지고,
     그림에 박힌 「1개월·2개월·3개월」 라벨이 바로 그 세 자리다. */
  var roadCard = document.querySelector(".road-card");
  var road = roadCard && roadCard.querySelector(".road-svg");
  var roadStep = 0;
  var STEPS = 6;                                    // 점 일곱 = 걸음 여섯

  function roadStops() {
    var g = GOALS[pick.goal];
    return courseList(g ? g.lv : overall() + 2);
  }
  /* 칸 i 에서 하고 있는 코스. 코스 길이(w)의 누적으로 가른다 — 균등하게
     나누면 11레슨짜리 한글 읽기가 112과짜리 핵심 패턴과 같은 폭을 먹는다.
     한 코스가 여러 칸에 걸치는 것이 정상이다: 핵심 패턴만 넉 달인 사람도 있다. */
  function courseAt(step) {
    var cs = roadStops(), tot = 0, cum = 0, i;
    for (i = 0; i < cs.length; i++) tot += COURSE[cs[i]].w;
    if (!tot) return cs[cs.length - 1];
    var f = step / STEPS;
    for (i = 0; i < cs.length; i++) {
      cum += COURSE[cs[i]].w / tot;
      if (f < cum - 1e-9) return cs[i];
    }
    return cs[cs.length - 1];
  }

  /* 길과 점은 Figma 에서 내려받은 좌표 그대로다. 손으로 다시 풀면 모퉁이
     반지름이 좌우로 다르다는 것(오른쪽 18.13, 왼쪽 19.87)부터 놓친다.
     삽화 원본은 x=10 에 놓여 있고 라벨은 그 바깥까지 나오므로, 길 전체를
     10 만큼 밀어 두고 좌표계 하나로 라벨까지 함께 잡는다.
     양 끝만 원본(x=6 … x=248.819)에서 첫 점·끝 점의 한가운데로 당겨 두었다.
     원본은 길이 점 밖으로 8 남짓 더 나가는데, 회색일 때는 안 보이던 그 꼬리가
     초록이 차오르면 「지금」 왼쪽에 반달로 튀어나온다 — 둥근 마감이 점 밑에
     정확히 묻히도록 끝을 점 중심에 맞춘다. */
  var ROAD_D = "M14.06 10.3438H127.409H230.688C240.701 10.3438 248.819 18.4612 248.819 " +
    "28.4745C248.819 38.4878 240.701 46.6052 230.688 46.6052H131.525H34.1004C23.1269 " +
    "46.6052 14.2311 55.501 14.2311 66.4745C14.2311 77.448 23.1269 86.3438 34.1004 " +
    "86.3438H131.525H248.879";
  var ROAD_DOTS = [[14.06, 10.3438], [127.06, 10.3438], [248.879, 28.4745],
                   [127.06, 46.6052], [14.1207, 66.4745], [127.06, 86.3438],
                   [248.879, 86.3438]];
  var roadEls = null, roadFracs = null, roadShown = 0, roadRaf = null;

  /* 점이 길의 몇 퍼센트 지점인가. 호가 섞인 경로라 손으로 푸는 대신 길을 잘게
     훑어 가장 가까운 표본을 고른다 — 길 모양을 고쳐도 따라온다. */
  function measureDots(p) {
    var L = p.getTotalLength(), N = 600, pts = [], i;
    for (i = 0; i <= N; i++) pts.push(p.getPointAtLength(L * i / N));
    return ROAD_DOTS.map(function (d) {
      var best = 0, bd = Infinity, k;
      for (k = 0; k <= N; k++) {
        var dx = pts[k].x - d[0], dy = pts[k].y - d[1], q = dx * dx + dy * dy;
        if (q < bd) { bd = q; best = k; }
      }
      return best / N;
    });
  }

  function buildRoad() {
    var NS = "http://www.w3.org/2000/svg";
    var el = function (t, at) { var e = document.createElementNS(NS, t);
      for (var q in at) e.setAttribute(q, at[q]); return e; };
    road.innerHTML = "";
    var g = el("g", { transform: "translate(10 0)" });
    road.appendChild(g);

    g.appendChild(el("path", { "class": "rd-track", d: ROAD_D, fill: "none",
                               "stroke-width": "12", "stroke-linecap": "round" }));
    /* 채워지는 쪽. pathLength 를 1 로 정규화해 두면 dasharray 를 비율로 쓸 수
       있어서, 길의 실제 길이를 몰라도 「몇 퍼센트」 로 자를 수 있다. */
    var fill = el("path", { "class": "rd-fill", d: ROAD_D, fill: "none",
                            "stroke-width": "12", "stroke-linecap": "round",
                            pathLength: "1", "stroke-dasharray": "1 1",
                            "stroke-dashoffset": "1" });
    g.appendChild(fill);

    /* 지금 선 자리의 무른 후광. 점마다 하나씩 두고 켜고 끈다 — 하나를 옮기면
       길을 따라가는 게 아니라 허공을 가로질러 날아간다. */
    var halos = ROAD_DOTS.map(function (d) {
      var c = el("circle", { "class": "rd-halo", cx: d[0], cy: d[1], r: 13 });
      g.appendChild(c); return c;
    });
    /* 일곱 점이 다 같은 크기면 일곱 다 같은 무게로 읽힌다. 실제로 이름이 붙는
       자리는 넷뿐이다 — 지금(0)·⅓(2)·⅔(4)·도착(6). 나머지 셋은 줄 한가운데의
       걸음일 뿐이라 작은 눈금으로 내린다(.minor). 밟고 선 동안에는 어느 쪽이든
       제 크기로 커진다: 서 있는 자리가 눈금일 수는 없다.
       크기·색은 전부 trial.css 가 쥔다. 여기서 r 을 한 번 적어 두는 것은 CSS
       기하 속성을 모르는 브라우저용 바닥값이다. */
    var dots = ROAD_DOTS.map(function (d, i) {
      var c = el("circle", { "class": "rd-dot" + (i % 2 ? " minor" : ""),
                             cx: d[0], cy: d[1], r: 6 });
      g.appendChild(c); return c;
    });

    /* 라벨은 길 위가 아니라 줄과 줄 사이 빈 띠에 놓는다. 길 위에 얹으면 초록이
       차오를 때마다 글자가 배경을 잃어 테를 둘러 줘야 하고, 그 테가 다시 길을
       갉아먹는다. 「지금」 과 ⅓ 라벨은 같은 기준선에 서서 한 줄로 읽힌다. */
    var cap = function (cls, x, y, anchor) {
      var e = el("text", { "class": "rd-cap " + cls, x: x, y: y, "text-anchor": anchor });
      g.appendChild(e); return e;
    };
    cap("start", 14.06, 31, "middle").textContent = "지금";
    roadEls = { fill: fill, dots: dots, halos: halos,
                // 굽이 점의 바깥 지름이 17 남짓이라, 라벨은 그 가장자리에서 8쯤
                // 떨어뜨려 둔다 — 「지금」 이 첫 점 아래에서 얻는 여백과 같은 몫이다
                mo: [cap("wp", 232, 31, "end"),         // ⅓ 지점 = 점 2, 오른쪽 굽이 왼편
                     cap("wp", 31, 70, "start"),        // ⅔ 지점 = 점 4, 왼쪽 굽이 오른편
                     cap("dest", 254.879, 108, "end")] };
    roadFracs = measureDots(fill);
  }

  /* 지금 밟은 점까지 초록이 차오르고, 점은 셋 중 하나가 된다.
     지나온 점은 길과 같은 초록으로 채워 길에 녹여 버린다 — 차오른 초록 위에
     흰 도넛이 남으면 길이 그 자리에서 끊겨 보인다. 지금 선 점만 흰 속에
     초록 테를 두르고 후광을 켠다. 도착점은 아직 못 갔어도 초록 테를 두른다:
     지도에 목적지가 찍혀 있어야 길이 어디로 가는지 읽힌다. */
  function setRoadStep(step, animate) {
    var target = roadFracs[step], from = roadShown;
    if (roadRaf) { cancelAnimationFrame(roadRaf); roadRaf = null; }
    /* 점은 걸음이 아니라 차오른 초록을 따른다. 목표 칸을 보고 한 번에 갈아
       끼우면 초록이 아직 기어가는 450ms 동안 초록 점들이 회색 길 위에 떠 있다.
       파도가 지나간 자리부터 하나씩 물드니, 되짚어 갈 때도 그대로 되감긴다. */
    var paint = function (f) {
      roadShown = f;
      roadEls.fill.setAttribute("stroke-dashoffset", (1 - f).toFixed(4));
      roadEls.dots.forEach(function (c, i) {
        var here = f >= roadFracs[i] - 1e-4;
        // 등급(minor·goal)은 자리가 정하는 것이라 상태와 함께 매번 다시 쓴다 —
        // class 를 통째로 갈아 끼우므로 여기서 빠뜨리면 첫 칠에 등급이 날아간다
        c.setAttribute("class", "rd-dot" + (i % 2 ? " minor" : "") +
          (i === STEPS ? " goal" : "") +
          (!here ? "" : i === step ? " now" : " done"));
        roadEls.halos[i].setAttribute("class",
          "rd-halo" + (here && i === step ? " on" : ""));
      });
    };
    /* 숨은 탭에서는 rAF 가 돌지 않는다 — 애니메이션에 점까지 실려 있으니,
       그대로 두면 길이 중간에 얼어붙은 채 남는다. 못 움직일 때는 건너뛴다. */
    if (!animate || still || document.hidden ||
        Math.abs(target - from) < 0.001) { paint(target); return; }
    var t0 = null, DUR = 450;
    roadRaf = requestAnimationFrame(function tick(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min(1, (ts - t0) / DUR);
      paint(from + (target - from) * (1 - Math.pow(1 - p, 3)));
      roadRaf = p < 1 ? requestAnimationFrame(tick) : null;
    });
  }

  /* 모퉁이 라벨은 ⅓·⅔·끝. 눈금이 카드 제목과 같은 단위를 쓴다 — 제목이
     「3주차」 인데 길은 「1개월」 을 세고 있으면 같은 자리를 두 잣대로 재는 셈이다.
     그래도 눈금이 겹치는 계획이 있다(두 달짜리에 ⅓·⅔ 가 둘 다 1개월). 그때는
     되풀이하지 않고 지운다: 「1개월 · 1개월 · 2개월」 은 눈금이 아니라 실수로
     읽힌다. 끝 눈금은 언제나 남는다 — 그게 목표다. */
  function drawRoad(unit, suf, animate) {
    if (!road) return;
    if (!roadEls) buildRoad();
    var at = function (i) { return Math.max(1, Math.round(unit * i / STEPS)); };
    var end = at(STEPS), prev = 0;
    [2, 4].forEach(function (i, n) {
      var v = at(i), show = v > prev && v < end;
      roadEls.mo[n].textContent = show ? v + suf : "";
      if (show) prev = v;
    });
    roadEls.mo[2].textContent = end + suf;
    setRoadStep(roadStep, animate);
  }

  /* ---- 로드맵 카드 · 지금 밟고 있는 칸이 무엇인가 ---- */
  var curli = document.querySelector(".curli");

  if (roadCard) {
    roadCard.querySelector(".rc-prev").addEventListener("click", function () { stepRoad(-1); });
    roadCard.querySelector(".rc-next").addEventListener("click", function () { stepRoad(1); });
  }
  function stepRoad(by) {
    var next = Math.max(0, Math.min(STEPS, roadStep + by));
    if (next === roadStep) return;
    roadStep = next;
    renderCurriculum(true);        // 움직이는 건 이 카드뿐 — 레이더까지 다시 그리지 않는다
    sync.push(roadCard);
  }
  /* 몇 번째 칸인지는 DOM 만 봐서는 알 수 없으니 직접 읽고 쓴다. 칸 수가 이제
     추천 코스와 무관하게 늘 일곱이라, 번호를 그대로 주고받아도 양쪽이 같은
     점에 선다. */
  sync.register("roadstep", {
    read: function () { return { step: roadStep }; },
    apply: function (el, state) {
      // NaN 도 typeof 는 "number" 다 — 여기서 걸러 내지 않으면 Math.max/min 을
      // 그대로 통과해 칸 번호가 NaN 이 되고, 「NaN주차」 가 상대에게도 실려 간다
      if (!state || typeof state.step !== "number" || !isFinite(state.step)) return;
      var at = Math.max(0, Math.min(STEPS, Math.round(state.step)));
      if (at !== roadStep) { roadStep = at; renderCurriculum(true); }
    }
  });

  function renderCurriculum(animate) {
    if (!curli || !roadCard) return;
    var k = roadStep, key = courseAt(k), c = COURSE[key], g = GOALS[pick.goal];

    // 총 기간은 위 슬라이더가 정한다. 칸 i 의 「N개월차」 는 그 총량의 i/6 이다.
    var per = perWeek();
    var need = g ? Math.max(6, DONE[String(g.lv)] - DONE[String(overall())]) : 24;
    var total = months(need, per);
    /* 칸은 여섯인데 기간이 석 달이면 「1개월차」 가 두 번 나온다 — 다음을 눌러도
       제목이 그대로면 눌리지 않은 것처럼 보인다. 여섯 칸이 서로 다른 눈금을
       갖도록, 달로 나누어지지 않는 계획은 주로 센다. 길 위의 모퉁이 라벨은
       Figma 대로 개월을 유지한다: 지도는 성기게, 서 있는 자리는 촘촘하게. */
    var weeks = Math.max(1, Math.round(need / per));
    var unit = total < STEPS ? weeks : total, suf = total < STEPS ? "주" : "개월";
    var atNo = function (i) { return Math.max(i ? 1 : 0, Math.round(unit * i / STEPS)); };
    var startAt = atNo(k);

    roadCard.querySelector(".rc-t").textContent =
      k === 0 ? "지금 레벨에 맞는 수업" : startAt + suf + "차";
    /* 한 코스를 두 칸 넘게 밟는 일이 흔하다. 그때마다 「여기까지 오면 이런
       이야기를 해요」 를 되풀이하면 진도가 멈춘 것처럼 읽히니, 코스에 처음
       들어선 칸에서만 그렇게 말한다. 마지막 칸은 예외다 — 로드맵 전체가
       노리는 한 줄이라, 거기서 「이어서 공부해요」 로 끝나면 김이 샌다. */
    var fresh = k === 0 || k === STEPS || courseAt(k - 1) !== key;
    roadCard.querySelector(".rc-s").textContent =
      k === 0 ? "진단 결과에 맞춰 약한 항목부터 공부해요!"
      : fresh ? c.can + " — 여기까지 오면 이런 이야기를 해요."
              : c.t + (hasBatchim(c.t) ? "을" : "를") + " 이어서 공부해요.";

    // 왜 여기서 시작하는가. 가장 처지는 두 항목을 그대로 이유로 쓴다.
    var order = ranked(), why = roadCard.querySelector(".rc-why span");
    if (k === 0 && order.length >= 2) {
      var w2 = order.slice(-2);
      why.innerHTML = "포도님은 <b>" + w2[0].n + "</b>" + (hasBatchim(w2[0].n) ? "과 " : "와 ") +
        "<b>" + w2[1].n + "</b>" + (hasBatchim(w2[1].n) ? "이" : "가") +
        " 아쉬웠어요.<br>그래서 " + c.s + "부터 시작해요.";
      why.parentNode.classList.remove("hide");
    } else if (k === 0) {
      why.parentNode.classList.add("hide");
    } else if (k === STEPS) {
      why.innerHTML = "여기까지 <b>" + startAt + suf + "</b> — 목표한 자리예요.";
      why.parentNode.classList.remove("hide");
    } else {
      // 「개월」 은 받침이 있고 「주」 는 없다 — 서술격 조사가 갈린다
      why.innerHTML = "여기까지 " + startAt + suf + ", 다음 칸까지 " +
        Math.max(1, atNo(k + 1) - startAt) + suf + (hasBatchim(suf) ? "이에요." : "예요.");
      why.parentNode.classList.remove("hide");
    }

    curli.innerHTML =
      '<div class="cli">' +
        '<div class="cli-h">' +
          '<img class="cli-ico" src="../assets/report-icons/course.svg" alt="">' +
          '<span><b class="cli-t">' + c.t + '</b><span class="cli-s">' + c.s + '</span></span>' +
        '</div>' +
        '<div class="cli-e"><i>✓</i><span><b>' + c.can + '</b><em>' + c.ex + '</em></span></div>' +
      '</div>';

    // 몇 칸 중 몇 번째인지, 그리고 끝에서 더 못 가는지
    var dots = "", i;
    for (i = 0; i <= STEPS; i++) dots += '<i' + (i === k ? ' class="on"' : "") + '></i>';
    roadCard.querySelector(".rc-dots").innerHTML = dots;
    roadCard.querySelector(".rc-prev").disabled = k <= 0;
    roadCard.querySelector(".rc-next").disabled = k >= STEPS;

    drawRoad(unit, suf, animate);
  }

  function months(lessons, perWeek) {
    return Math.max(1, Math.round(lessons / (perWeek * 4.3)));
  }

  /* ---- 목표 카드 속은 고른 이유만 남긴다 ----
     카드(=거리)는 넷 그대로고, 그 안의 「할 수 있게 되는 일」 만 이 사람의
     이유로 좁힌다. 아직 이유를 고르지 않았으면 여섯 줄을 다 펴는 대신
     한 줄로 그 사실을 말한다 — 남의 이유가 여섯 줄씩 네 장이면, 정작
     고를 것(거리)이 그 밑에 묻힌다.
     원격 선택도 보드가 옵션을 합성 클릭해 오므로 양쪽이 같은 줄을 본다. */
  function renderGoalCards() {
    var items = [].slice.call(document.querySelectorAll(".glc-i[data-why]"));
    if (!items.length) return;
    var any = pick.why.some(function (w) { return WHY_COURSE[w]; });
    items.forEach(function (it) {
      it.classList.toggle("hide", pick.why.indexOf(it.getAttribute("data-why")) < 0);
    });
    document.querySelectorAll(".glc-e").forEach(function (e) { e.classList.toggle("hide", any); });
  }

  function render() {
    renderGoalCards();
    renderLevelPick();
    renderAxSteps();
    renderLevel();
    renderAspects();
    renderCourseCard();
    renderCurriculum();
  }

  stampDates();
  render();
})();
