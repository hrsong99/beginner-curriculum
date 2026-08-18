#!/usr/bin/env python3
"""Verify the five rules that govern every teaching surface in a deck.

They exist because an audit of 535 뜻과 쓰임 boxes found the same four habits
everywhere, and none of them is visible while you are writing one deck:

  1  ANCHOR      a pN-teach box is the .anchor slot plus ONE spoken sentence.
                 The Japanese equivalent lives in .anchor-ja with its Hangul
                 reading in .anchor-ko; the sentence that used to quote the
                 Japanese inline is gone. Prose has no floor, and where the
                 author could not name a Japanese counterpart the sentence grew
                 into a paragraph — every deck in core-upper-intermediate-1/2
                 and core-advanced-1 had no anchor and ran 149-154 자 against a
                 beginner median of 94.

  2  SPOKEN JA   no Japanese script in a line the tutor reads aloud (.ko,
                 .tutor-note is exempt — see below). Korean tutors are not
                 assumed to read Japanese, and 313 spoken lines handed them
                 kana to say out loud. If the Japanese is useful, it belongs in
                 .tutor-note WITH a Hangul reading in parentheses.

  3  LESSON REF  no lesson numbers, anywhere — prose, tutor notes, diagram
                 labels, chips. Neither a tutor nor a learner can resolve "90과"
                 on sight. Name the form instead.

  4  TAIL        no boilerplate close. 제가 읽을게요. 잘 듣고 따라 읽어 보세요.
                 was identical on 246 of 255 boxes: 21% of the median box
                 carrying no information a tutor does not already have.

  5  LENGTH      a teach box's spoken line stays at or under LIMIT 자. The
                 blueprint has asked for two sentences since it was written and
                 got 3% compliance, because prose does not hold a line. This is
                 the number that does.

Rule 5's budget is deliberately loose (the contextual track's own median is 48)
— it is a backstop against paragraphs, not a style gauge.

  python3 korean/tools/check_teaching.py                    # whole repo
  python3 korean/tools/check_teaching.py <deck…>            # named decks
  python3 korean/tools/check_teaching.py --rule ref         # one rule
"""
import re
import sys
from pathlib import Path
from collections import Counter

REPO = Path(__file__).resolve().parent.parent.parent

LIMIT = 60          # 자, the spoken line of a teach box
RULE_LIMIT = 90     # 자, a rule page's subtitle — it may name a second branch

TAG = re.compile(r"<[^>]+>")
PID = re.compile(r'data-page-id="([^"]+)"')
KO = re.compile(r'<span class="ko">(.*?)</span>', re.S)
TUTOR = re.compile(r'<div class="tutor-note">(.*?)</div>', re.S)
PM = re.compile(r'<p class="section-subtitle pattern-meaning"[^>]*>(.*?)</p>', re.S)
SUB = re.compile(r'<p class="section-subtitle"[^>]*>(.*?)</p>', re.S)
ANCHOR = re.compile(r'<span class="anchor">\s*<span class="anchor-ja">(.*?)</span>'
                    r'\s*<span class="anchor-ko">(.*?)</span>\s*</span>', re.S)

# kana, kanji, halfwidth katakana. NOT the 「」 quotes, which are punctuation.
JA_SCRIPT = re.compile(r"[぀-ヿ㐀-䶿一-鿿ｦ-ﾟ]")
# 「N과」 / 「N課」 / 「68~70과」.  (?<![가-힣]) keeps the particle 과 out —
# "파트 1과 똑같아요" is 과 the particle, not lesson 1, and it cost us a
# false positive on the very first deck.
LESSON_REF = re.compile(r"(?<![가-힣])\d+\s*[~～\-–]?\s*\d*\s*[과課](?![가-힣])")
TAIL = re.compile(r"(제가 읽을게요|읽어 드릴게요|들려 드릴게요|잘 듣고 따라 읽어|"
                  r"따라 읽어 ?보세요|한 번에 읽을게요|이어서 읽을게요)")

RULES = ("anchor", "spoken-ja", "ref", "tail", "length")


def strip(s):
    return re.sub(r"\s+", " ", TAG.sub("", s)).strip()


QUOTE_OPEN, QUOTE_CLOSE = "“‘「『", "”’」』"


def sentences(t):
    """Count sentences the way runtime/js/script-lines.js does.

    These decks cite expressions mid-sentence — 장소는 ‘어디예요?’예요 — so a
    naive split on .!? reports two sentences where the tutor says one. Same
    trap the migration script hit; the fix is the same: punctuation inside a
    quote does not end a sentence, and in Korean the mark must be followed by
    whitespace or end-of-string because a citation is glued to its particle.
    """
    out, cur, depth = [], "", 0
    for i, ch in enumerate(t):
        cur += ch
        if ch in QUOTE_OPEN:
            depth += 1
        elif ch in QUOTE_CLOSE and depth:
            depth -= 1
        elif ch in ".!?" and not depth:
            if i + 1 >= len(t) or t[i + 1].isspace():
                out.append(cur.strip())
                cur = ""
    if cur.strip():
        out.append(cur.strip())
    return out


def pages(src):
    """(page-id, chunk) for every data-page-id in document order"""
    idx = [(m.start(), m.group(1)) for m in PID.finditer(src)]
    for i, (pos, pid) in enumerate(idx):
        end = idx[i + 1][0] if i + 1 < len(idx) else len(src)
        yield pid, src[pos:end]


COMMENT = re.compile(r"<!--.*?-->", re.S)


def check(path, want):
    # Authoring comments are not a teaching surface. They are written in
    # English and discuss the lesson — "they are 과 3 과 1 material" tripped the
    # lesson-number rule on a deck that had no reference in it at all.
    src = COMMENT.sub("", Path(path).read_text(encoding="utf-8"))
    out = []

    def hit(rule, pid, detail, text):
        if rule in want:
            out.append((rule, pid, detail, text))

    for pid, chunk in pages(src):
        pm = PM.search(chunk)

        # ---- rule 1: a teach box carries an anchor slot and one sentence ----
        if pm:
            inner = pm.group(1)
            ko = strip(KO.search(inner).group(1)) if KO.search(inner) else ""
            if not ANCHOR.search(inner):
                hit("anchor", pid, "뜻과 쓰임 상자에 .anchor 슬롯이 없음", ko)
            elif not strip(ANCHOR.search(inner).group(2)):
                hit("anchor", pid, ".anchor-ko 읽기가 비어 있음", ko)
            n = len(sentences(ko))
            if n > 1:
                hit("anchor", pid, f"말하는 줄이 {n}문장 (1문장이어야 함)", ko)
            if len(ko) > LIMIT:
                hit("length", pid, f"{len(ko)}자 > {LIMIT}", ko)

        # ---- rule 5b: a rule page's subtitle ----
        elif "rule" in pid:
            sb = SUB.search(chunk)
            if sb:
                ko = strip(KO.search(sb.group(1)).group(1)) if KO.search(sb.group(1)) else ""
                if len(ko) > RULE_LIMIT:
                    hit("length", pid, f"{len(ko)}자 > {RULE_LIMIT}", ko)

        # ---- rule 2: no Japanese in a line the tutor says out loud ----
        # .anchor-ja is the one place Japanese belongs — it is shown, not said,
        # and .anchor-ko is what the tutor reads. .tutor-note is never read
        # aloud, so Japanese is allowed there (with a reading, rule 2b).
        body = ANCHOR.sub("", chunk)
        for m in KO.finditer(body):
            ko = strip(m.group(1))
            if JA_SCRIPT.search(ko):
                found = "".join(sorted(set(JA_SCRIPT.findall(ko))))
                hit("spoken-ja", pid, f"소리 내어 읽는 줄에 일본어 [{found}]", ko)

        # ---- rule 2b: Japanese in a tutor note needs its Hangul reading ----
        for m in TUTOR.finditer(chunk):
            note = strip(m.group(1))
            for run in re.finditer(r"[぀-ヿ㐀-䶿一-鿿]+", note):
                after = note[run.end():run.end() + 2]
                if not after.startswith("(") and not after.startswith("（"):
                    hit("spoken-ja", pid,
                        f"튜터 노트의 ‘{run.group()}’에 한글 읽기가 없음", note)
                    break

        # ---- rule 3: lesson numbers, in any element on the page ----
        for m in LESSON_REF.finditer(chunk):
            seg = strip(chunk[max(0, m.start() - 60):m.end() + 30])
            hit("ref", pid, f"‘{m.group().strip()}’ 참조", seg)

        # ---- rule 4: the boilerplate close ----
        # Only inside a 뜻과 쓰임 box. On a pN-read page "네 문장을 천천히 따라
        # 읽어 보세요" is the page's actual instruction, not boilerplate — the
        # first cut of this rule flagged 238 of those and the number was
        # meaningless until the scope was right.
        if pm:
            ko = strip(KO.search(pm.group(1)).group(1)) if KO.search(pm.group(1)) else ""
            if TAIL.search(ko):
                hit("tail", pid, "상투적 마무리", ko)

    return out


def main(argv):
    want = set(RULES)
    if "--rule" in argv:
        i = argv.index("--rule")
        want = {argv[i + 1]}
        del argv[i:i + 2]
        bad = want - set(RULES)
        if bad:
            print(f"unknown rule {bad}; pick from {RULES}")
            return 2
    paths = argv or [str(p) for p in sorted(
        (REPO / "korean/tracks").glob("**/lesson.html"))]

    tally, decks = Counter(), Counter()
    for p in paths:
        rows = check(p, want)
        if not rows:
            continue
        print(f"\n### {Path(p).parents[2].name}/{Path(p).parent.name}")
        for rule, pid, detail, text in rows:
            print(f"  [{rule:<9}] {pid:<18} {detail}")
            if text:
                print(f"      {text[:120]}")
            tally[rule] += 1
        decks[Path(p).parents[2].name] += len(rows)

    total = sum(tally.values())
    print(f"\n{len(paths)} deck(s) · {total} finding(s)")
    for r in RULES:
        if r in want:
            print(f"   {r:<10}{tally[r]}")
    if decks:
        print("\n  worst decks:")
        for d, n in decks.most_common(8):
            print(f"   {d:<48}{n}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
