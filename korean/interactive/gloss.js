/* ================================================================
   GLOSS · 일본어 호버 툴팁 (한국어 뜻/발음) — 공유 스크립트

   화면 디자인은 그대로 두고, 일본어 텍스트에 마우스를 올리면 한국어
   번역을 보여 준다(가타카나 발음 표기는 "발음:"). 리뷰용 보조 장치다.

   과가 주는 것은 사전 하나뿐이다. 이 파일보다 먼저 선언해 두면 된다:

     <script>
       window.LESSON_GLOSS = { "こんにちは！": "안녕하세요!", ... };
       window.LESSON_GLOSS_PLACEHOLDERS = { "名前": "이름" };   // 입력칸 placeholder, 없으면 생략
       window.LESSON_GLOSS_PAIRED = [".s-ja"];                  // 이 덱만의 예외, 없으면 생략
     </script>
     <script src="../../interactive/gloss.js"></script>

   사전이 없으면 아무 일도 하지 않는다.
   ================================================================ */
(function () {
  const D = window.LESSON_GLOSS;
  if (!D) return;
  const P = window.LESSON_GLOSS_PLACEHOLDERS || {};

  const norm = s => (s || "").replace(/[\s　]+/g, " ").trim();

  const tip = document.createElement("div");
  tip.setAttribute("lang", "ko");
  tip.style.cssText =
    "position:fixed;z-index:9999;max-width:300px;padding:8px 12px;" +
    "background:#1c1c1c;color:#fff;font-size:13px;line-height:1.55;font-weight:600;" +
    "border:1.5px solid #b5fd4c;border-radius:9px;box-shadow:0 6px 18px rgba(0,0,0,.28);" +
    "pointer-events:none;opacity:0;transition:opacity .12s;word-break:keep-all;";
  document.body.appendChild(tip);

  const style = document.createElement("style");
  style.textContent = "[data-ko]{cursor:help;}";
  document.head.appendChild(style);

  /* 화면에 한국어가 이미 짝으로 붙어 있는 자리에는 툴팁을 달지 않는다.
     짝은 디자인이 정한 것이라(스크립트의 .ja 위에는 .ko, 말풍선의 번역
     위에는 한국어 원문), 목록도 디자인을 따라 적는다 — 구조로 추정하면
     중첩된 한글을 놓치고 번역이 아닌 캡션을 번역으로 오인한다.

     네 덱의 목록을 합친 것이다. 그 덱에 없는 컴포넌트의 선택자는 아무것도
     고르지 못하므로 그냥 지나간다 — 목록을 덱마다 갈라 둘 이유가 없다. */
  const PAIRED = [
    ".ja",                                     // KO/JA 짝의 일본어 쪽 전부
    ".title-ja",
    ".translation", ".answer-label", ".answer-box",
    ".known-row .j",
    ".br-cn", ".br-ko small",                  // 漢字 → 한글 다리: 한국어가 바로 옆 칸에 있다
    ".word-card .mean",
    ".letter-card .kana-eq",
    ".opt-row .opt-main",
    ".s-ja",                                   // 지문 한 문장의 일본어 번역
    ".fb-cap",                                 // 피드백 칸의 라벨
    ".who", ".who-name",
    ".zone", ".yomi", ".yomi-line",
    ".transition-kicker", ".brand-title", ".podo-badge .tag"
  ].concat(window.LESSON_GLOSS_PAIRED || []).join(",");

  document.querySelectorAll("body *").forEach(el => {
    if (el === tip) return;
    if (el.matches(PAIRED)) return;             // 한국어가 이미 옆에 있다
    let own = "";
    el.childNodes.forEach(n => { if (n.nodeType === 3) own += n.textContent; });
    const val = D[norm(own)] || D[norm(el.textContent)];
    if (val) el.setAttribute("data-ko", val);
    if (el.placeholder && P[el.placeholder]) el.setAttribute("data-ko", P[el.placeholder]);
  });

  document.addEventListener("mouseover", e => {
    const t = e.target.closest ? e.target.closest("[data-ko]") : null;
    if (!t) { tip.style.opacity = 0; return; }
    tip.textContent = t.getAttribute("data-ko");
    tip.style.opacity = 1;
    const r = t.getBoundingClientRect();
    const tw = tip.offsetWidth, th = tip.offsetHeight;
    let x = Math.min(Math.max(8, r.left), window.innerWidth - tw - 8);
    let y = r.top - th - 8;
    if (y < 8) y = r.bottom + 8;
    tip.style.left = x + "px";
    tip.style.top = y + "px";
  });
  document.addEventListener("scroll", () => { tip.style.opacity = 0; }, true);
})();
