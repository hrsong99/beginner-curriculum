#!/usr/bin/env python3
"""Write a Japanese kana string in Hangul, per 국립국어원 외래어 표기법 제2장 표4.

This exists for one line in the deck: .anchor-ko, the reading under the
Japanese in a 뜻과 쓰임 box. A Korean tutor is asked to say that Japanese out
loud, and we do not assume they read kana. The reading is a crutch for the
tutor, not a pronunciation model for the learner — the learner already knows
the Japanese and is looking at it directly.

Following 표기법 rather than transcribing by ear is the whole point: it is a
rule, so 164 anchors come out consistent, and it happens to be closer to the
Japanese anyway. か word-initially is 가, not 카, because Japanese /k/ there is
unaspirated and Korean ㄱ is the nearer sound. Transcribing by ear is what
produces 카모시레나이, and then the next author writes 가모시레나이 and the deck
has two spellings of the same word.

What it will NOT do is kanji: 聞く has a reading only a reader knows. Those come
back as None with the kanji named, and are written by hand — see KANJI below
for the ones this curriculum actually uses.

  python3 korean/tools/ja_to_hangul.py '~かもしれない'      → 가모시레나이
  python3 korean/tools/ja_to_hangul.py --self-test
"""
import re
import sys

# ---- 표4. か행과 た행만 어두/어중이 갈린다 ---------------------------------
#      (어두, 어중·어말).  나머지는 두 자리가 같다.
MORA = {
    "あ": ("아", "아"), "い": ("이", "이"), "う": ("우", "우"), "え": ("에", "에"), "お": ("오", "오"),
    "か": ("가", "카"), "き": ("기", "키"), "く": ("구", "쿠"), "け": ("게", "케"), "こ": ("고", "코"),
    "さ": ("사", "사"), "し": ("시", "시"), "す": ("스", "스"), "せ": ("세", "세"), "そ": ("소", "소"),
    "た": ("다", "타"), "ち": ("지", "치"), "つ": ("쓰", "쓰"), "て": ("데", "테"), "と": ("도", "토"),
    "な": ("나", "나"), "に": ("니", "니"), "ぬ": ("누", "누"), "ね": ("네", "네"), "の": ("노", "노"),
    "は": ("하", "하"), "ひ": ("히", "히"), "ふ": ("후", "후"), "へ": ("헤", "헤"), "ほ": ("호", "호"),
    "ま": ("마", "마"), "み": ("미", "미"), "む": ("무", "무"), "め": ("메", "메"), "も": ("모", "모"),
    "や": ("야", "야"), "ゆ": ("유", "유"), "よ": ("요", "요"),
    "ら": ("라", "라"), "り": ("리", "리"), "る": ("루", "루"), "れ": ("레", "레"), "ろ": ("로", "로"),
    "わ": ("와", "와"), "を": ("오", "오"),
    "が": ("가", "가"), "ぎ": ("기", "기"), "ぐ": ("구", "구"), "げ": ("게", "게"), "ご": ("고", "고"),
    "ざ": ("자", "자"), "じ": ("지", "지"), "ず": ("즈", "즈"), "ぜ": ("제", "제"), "ぞ": ("조", "조"),
    "だ": ("다", "다"), "ぢ": ("지", "지"), "づ": ("즈", "즈"), "で": ("데", "데"), "ど": ("도", "도"),
    "ば": ("바", "바"), "び": ("비", "비"), "ぶ": ("부", "부"), "べ": ("베", "베"), "ぼ": ("보", "보"),
    "ぱ": ("파", "파"), "ぴ": ("피", "피"), "ぷ": ("푸", "푸"), "ぺ": ("페", "페"), "ぽ": ("포", "포"),
    # 요음
    "きゃ": ("갸", "캬"), "きゅ": ("규", "큐"), "きょ": ("교", "쿄"),
    "ぎゃ": ("갸", "갸"), "ぎゅ": ("규", "규"), "ぎょ": ("교", "교"),
    "しゃ": ("샤", "샤"), "しゅ": ("슈", "슈"), "しょ": ("쇼", "쇼"),
    "じゃ": ("자", "자"), "じゅ": ("주", "주"), "じょ": ("조", "조"),
    "ちゃ": ("자", "차"), "ちゅ": ("주", "추"), "ちょ": ("조", "초"),
    "にゃ": ("냐", "냐"), "にゅ": ("뉴", "뉴"), "にょ": ("뇨", "뇨"),
    "ひゃ": ("햐", "햐"), "ひゅ": ("휴", "휴"), "ひょ": ("효", "효"),
    "びゃ": ("뱌", "뱌"), "びゅ": ("뷰", "뷰"), "びょ": ("뵤", "뵤"),
    "ぴゃ": ("퍄", "퍄"), "ぴゅ": ("퓨", "퓨"), "ぴょ": ("표", "표"),
    "みゃ": ("먀", "먀"), "みゅ": ("뮤", "뮤"), "みょ": ("묘", "묘"),
    "りゃ": ("랴", "랴"), "りゅ": ("류", "류"), "りょ": ("료", "료"),
}

# the vowel each mora ends on, for the 장음 rule
VOWEL = {}
for _k in MORA:
    VOWEL[_k] = "aiueo"["あいうえお".index(_k[-1])] if _k[-1] in "あいうえお" else \
                {"や": "a", "ゆ": "u", "よ": "o", "ゃ": "a", "ゅ": "u", "ょ": "o",
                 "わ": "a", "を": "o"}.get(_k[-1], "aiueo"[
                     "かさたなはまらがざだばぱ".find(_k[-1]) % 5] if _k[-1] in "かさたなはまらがざだばぱ" else "a")
# the table above is fiddly for the base rows; state them outright instead
for _row, _v in (("あかさたなはまやらわがざだばぱ", "a"),
                 ("いきしちにひみりぎじぢびぴ", "i"),
                 ("うくすつぬふむゆるぐずづぶぷ", "u"),
                 ("えけせてねへめれげぜでべぺ", "e"),
                 ("おこそとのほもよろをごぞどぼぽ", "o")):
    for _c in _row:
        VOWEL[_c] = _v
for _k in MORA:
    if len(_k) == 2:
        VOWEL[_k] = {"ゃ": "a", "ゅ": "u", "ょ": "o"}[_k[1]]

# 받침. 촉음 っ은 'ㅅ', 발음(撥音) ん은 'ㄴ' — 표기법이 예외 없이 하나로 정한다.
JONG = {"っ": 19, "ん": 4}

KATA = {chr(c): chr(c - 0x60) for c in range(0x30A1, 0x30F7)}

# 표기법 transcribes the sound, and the particle は is said /wa/. Which は is a
# particle is grammar, not kana, so this does not guess: は counts as a particle
# only directly after one of these, which covers every anchor in the corpus
# (ことは · のは · ては · では). Any other non-initial は is reported for a human
# — 「やはり」 is 야하리, and a blanket rule would have written 야와리.
PARTICLE_AFTER = set("のてでと")

# The kanji this curriculum's anchors actually use. Kept here rather than in a
# general dictionary because the point is coverage of these decks, and a wrong
# reading is worse than no reading — anything absent comes back as None and
# gets written by a person.
KANJI = {
    "名詞": "메이시", "動詞": "도시", "形容詞": "케이요시",
    "後": "아토", "前": "마에", "時": "토키", "人": "히토", "方": "호",
    "何": "나니", "誰": "다레", "中": "나카", "上": "우에", "下": "시타",
    "聞": "키", "知": "시", "行": "이", "思": "오모", "言": "이",
    "終": "오", "見": "미", "来": "쿠", "食": "타", "話": "하나",
    "作": "쓰쿠", "使": "쓰카", "持": "모", "待": "마", "帰": "카에",
    "出": "데", "入": "하이", "住": "스", "働": "하타라", "休": "야스",
    "途中": "도추", "最中": "사이추", "大丈夫": "다이조부", "一番": "이치반",
    "本当": "혼토", "自分": "지분", "気": "키", "度": "도", "回": "카이",
    "予定": "요테이", "必要": "히쓰요", "一緒": "잇쇼", "外": "소토",
    "私": "와타시", "会": "아", "個": "코", "分": "훈", "名": "메이",
    # Compounds come first in the lookup because a character's reading is not
    # its reading in every word: 上 is 우에 by itself and あげ inside
    # 差し上げる, and a single-character table quietly wrote 시우에게마스.
    "差し上げ": "사시아게", "召し上が": "메시아가", "上げ": "아게",
    "何個": "난코", "何名": "난메이", "何月": "난가쓰", "何日": "난니치",
    "何曜日": "난요비", "曜日": "요비", "月": "가쓰", "日": "니치",
    "上手": "조즈", "全然": "젠젠", "何も": "나니모", "運動": "운도", "勉強": "벤쿄",
    "同じ": "오나지", "価値": "카치", "代わり": "카와리", "別": "베쓰", "兼ねて": "카네테",
}


def compose(syl, jong):
    """put a 받침 under an already-formed hangul syllable"""
    code = ord(syl) - 0xAC00
    if code < 0 or code > 11171 or code % 28:
        return syl
    return chr(0xAC00 + code + jong)


def reading(text):
    """(hangul, unresolved) — unresolved lists kanji this cannot read"""
    text = "".join(KATA.get(c, c) for c in text)
    text = text.replace("〜", "").replace("~", "").strip()

    # a bare は as the whole string is the particle, said /wa/ — the anchor
    # ~は is the topic marker, not the first mora of a word like はず
    if text == "は":
        return "와", []

    unresolved = []
    out = []
    i = 0
    prev_vowel = None
    while i < len(text):
        c = text[i]

        # kanji: whole-word lookup first, then single character
        if "一" <= c <= "鿿":
            for size in (4, 3, 2, 1):
                word = text[i:i + size]
                if word in KANJI:
                    out.append(KANJI[word])
                    prev_vowel = None
                    i += size
                    break
            else:
                unresolved.append(c)
                out.append("?")
                prev_vowel = None
                i += 1
            continue

        # 받침
        if c in JONG:
            if out and out[-1]:
                out[-1] = out[-1][:-1] + compose(out[-1][-1], JONG[c])
            prev_vowel = None
            i += 1
            continue

        # 장음부호는 적지 않는다
        if c == "ー":
            i += 1
            continue

        if c == "は" and out and text[i - 1] in PARTICLE_AFTER:
            out.append("와")
            prev_vowel = "a"
            i += 1
            continue
        if c == "は" and out:
            unresolved.append("は(조사인지 확인)")

        mora = text[i:i + 2] if text[i:i + 2] in MORA else c
        if mora not in MORA:
            # punctuation, ・, latin — pass it through untouched
            out.append(c)
            prev_vowel = None
            i += 1
            continue

        # 장음: おう / うう 의 う 는 적지 않는다
        if mora == "う" and prev_vowel in ("o", "u"):
            i += 1
            continue

        head, tail = MORA[mora]
        # 어두는 문장 첫 자리, 그리고 ・ 로 나뉜 각 낱말의 첫 자리
        at_start = not out or out[-1] in ("・", "·", " ", "/")
        out.append(head if at_start else tail)
        prev_vowel = VOWEL[mora]
        i += len(mora)

    return "".join(out), unresolved


CASES = [
    ("かもしれない", "가모시레나이"),   # か word-initial → 가, not 카
    ("はずがない", "하즈가나이"),
    ("してみてください", "시테미테쿠다사이"),
    ("とうきょう", "도쿄"),             # 장음 두 군데
    ("さっぽろ", "삿포로"),             # 촉음 → ㅅ 받침
    ("しんぶん", "신분"),               # 발음 → ㄴ 받침
    ("ではありません", "데와아리마센"),   # 조사 は
    ("やはり", "야하리"),               # 조사가 아닌 は
    ("は", "와"),                       # 조사 하나만 있는 앵커
    ("しなくてもいいです", "시나쿠테모이이데스"),
    ("がっこう", "갓코"),      # 촉음은 예외 없이 ㅅ
    ("きょうしつ", "교시쓰"),           # 어두 요음도 か행 규칙을 따른다 (京都 = 교토)
]


def self_test():
    bad = 0
    for src, want in CASES:
        got, _ = reading(src)
        ok = got == want
        bad += not ok
        print(f"  {'ok ' if ok else 'FAIL'} {src:<18}{got:<16}{'' if ok else '≠ ' + want}")
    print(f"\n{len(CASES) - bad}/{len(CASES)} pass")
    return 1 if bad else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    for arg in sys.argv[1:]:
        got, un = reading(arg)
        print(got + (f"   ← 한자 미해결: {un}" if un else ""))
