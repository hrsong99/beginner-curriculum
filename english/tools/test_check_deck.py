#!/usr/bin/env python3
"""Regression tests for silent deck checks shared by English and Korean."""

from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import check_deck


class DeckCheckTests(unittest.TestCase):
    def test_meta_content_is_attribute_order_tolerant(self):
        source = (
            '<meta content="notranslate" name="google">'
            '<meta content="07-daily-routine" data-owner="author" '
            'name="podo:lesson-id">'
        )
        self.assertEqual(check_deck.meta_content(source, "google"), "notranslate")
        self.assertEqual(
            check_deck.meta_content(source, "podo:lesson-id"),
            "07-daily-routine",
        )

    def test_sentence_split_ignores_quoted_expression_punctuation(self):
        korean = "제가 ‘도대체 왜 그랬어?’라고 물을게요. 대답해 보세요."
        japanese = "私が「どうしてそうしたの」と聞きます。答えてみてください。"
        self.assertEqual(
            len(check_deck.sentences(korean, check_deck.KO_END, spaced=True)),
            2,
        )
        self.assertEqual(
            len(check_deck.sentences(japanese, check_deck.JA_END, spaced=False)),
            2,
        )

    def test_korean_mixed_reorder_counts_are_review_warnings(self):
        with tempfile.TemporaryDirectory() as temporary:
            lesson = pathlib.Path(temporary) / "01-test"
            lesson.mkdir()
            deck = lesson / "lesson.html"
            deck.write_text(
                '<meta name="google" content="notranslate">'
                '<meta name="podo:lesson-id" content="01-test">'
                '<div data-page-id="p1-reorder">'
                '<div class="task-block"><span class="choice">가</span>'
                '<span class="choice">나</span></div>'
                '<div class="task-block"><span class="choice">가</span>'
                '<span class="choice">나</span><span class="choice">다</span></div>'
                '</div>',
                encoding="utf-8",
            )
            errors, warnings = check_deck.check(deck)
            self.assertEqual(errors, [])
            self.assertTrue(any("mixed chip counts" in item for item in warnings))

    def test_runtime_promoted_control_shell_is_an_error(self):
        with tempfile.TemporaryDirectory() as temporary:
            lesson = pathlib.Path(temporary) / "01-test"
            lesson.mkdir()
            deck = lesson / "lesson.html"
            deck.write_text(
                '<meta name="google" content="notranslate">'
                '<meta name="podo:lesson-id" content="01-test">'
                '<span class="slot" data-sync-id="answer">yes</span>',
                encoding="utf-8",
            )
            errors, _ = check_deck.check(deck)
            self.assertTrue(any("runtime-promoted control" in item for item in errors))

    def test_static_control_is_not_reported_as_a_shell(self):
        with tempfile.TemporaryDirectory() as temporary:
            lesson = pathlib.Path(temporary) / "01-test"
            lesson.mkdir()
            deck = lesson / "lesson.html"
            deck.write_text(
                '<meta name="google" content="notranslate">'
                '<meta name="podo:lesson-id" content="01-test">'
                '<input class="slot-input" data-sync-id="answer" data-answer="yes">',
                encoding="utf-8",
            )
            errors, _ = check_deck.check(deck)
            self.assertFalse(any("runtime-promoted control" in item for item in errors))

    def test_reorder_accepts_any_chip_order_without_id_convention(self):
        chunk = (
            '<div data-page-id="p1-reorder">'
            '<div class="task-block">'
            '<span class="answer-space build-zone" data-sync-id="p1-row" '
            'data-sync-kind="order" data-a="Could you help me?"></span>'
            '<span class="choice" data-item-id="arbitrary-a">help</span>'
            '<span class="choice" data-item-id="arbitrary-b">me?</span>'
            '<span class="choice" data-item-id="arbitrary-c">Could you</span>'
            '</div></div>'
        )
        self.assertEqual(
            check_deck.reorder_solvability_errors("p1-reorder", chunk),
            [],
        )

    def test_reorder_rejects_chips_that_cannot_build_answer(self):
        chunk = (
            '<div data-page-id="p1-reorder">'
            '<div class="task-block">'
            '<span class="answer-space build-zone" data-sync-id="p1-row" '
            'data-sync-kind="order" data-a="Could you help me?"></span>'
            '<span class="choice">help</span>'
            '<span class="choice">them?</span>'
            '<span class="choice">Could you</span>'
            '</div></div>'
        )
        errors = check_deck.reorder_solvability_errors("p1-reorder", chunk)
        self.assertTrue(any("cannot reconstruct data-a" in item for item in errors))

    def test_freetalking_article_accepts_seven_rows_with_exact_gloss_parity(self):
        script = (
            '<p class="section-subtitle"><span class="ko">'
            'Did you have any questions about the article?'
            '</span><span class="ja">記事について何か質問はありましたか？</span></p>'
        )
        row = (
            '<div class="sent"><span class="s-key">curiosity</span>'
            '<span class="s-w"><b>curiosity</b>好奇心</span></div>'
        )
        errors, warnings = check_deck.article_structure_issues(script + row * 7)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_freetalking_article_rejects_five_rows_and_mismatched_glosses(self):
        script = (
            '<p class="section-subtitle"><span class="ko">'
            'Did you have any questions about the article?'
            '</span><span class="ja">記事について何か質問はありましたか？</span></p>'
        )
        matched = (
            '<div class="sent"><span class="s-key">curiosity</span>'
            '<span class="s-w"><b>curiosity</b>好奇心</span></div>'
        )
        mismatched = '<div class="sent"><span class="s-key">curiosity</span></div>'
        errors, _ = check_deck.article_structure_issues(script + matched * 4 + mismatched)
        self.assertTrue(any("5 sentence rows" in item for item in errors))
        self.assertTrue(any("1 highlighted item(s) but 0 gloss(es)" in item for item in errors))

    def test_freetalking_article_rejects_in_class_reading_coaching(self):
        script = (
            '<p class="section-subtitle"><span class="ko">'
            'Did you read the article? If not, skim it now.'
            '</span><span class="ja">記事を読みましたか？ まだなら今読んでください。</span></p>'
        )
        rows = '<div class="sent"></div>' * 7
        errors, _ = check_deck.article_structure_issues(script + rows)
        self.assertTrue(any("one question" in item for item in errors))
        self.assertTrue(any("must ask whether the learner has questions" in item for item in errors))
        self.assertTrue(any("coaches page use or in-class reading" in item for item in errors))

    def test_freetalking_question_note_accepts_followups_only(self):
        chunk = (
            '<div class="tutor-note"><div class="tn-body">'
            '<span class="tn-cap">Follow up</span><ul class="tn-more">'
            '<li>What happened next?</li><li>How did you react?</li>'
            '</ul></div></div><div class="fb"></div>'
        )
        self.assertEqual(check_deck.freetalk_question_note_issues("q1", chunk), [])

    def test_freetalking_question_note_rejects_coaching_preamble(self):
        chunk = (
            '<div class="tutor-note"><div class="tn-body">Build the story in short steps.'
            '<span class="tn-cap">Follow up</span><ul class="tn-more">'
            '<li>What happened next?</li><li>How did you react?</li>'
            '</ul></div></div><div class="fb"></div>'
        )
        errors = check_deck.freetalk_question_note_issues("q1", chunk)
        self.assertTrue(any("has coaching before the follow-ups" in item for item in errors))

    def test_freetalking_question_note_rejects_nonquestion_and_duplicate(self):
        chunk = (
            '<p class="section-subtitle ask"><span class="ko">What changed?</span>'
            '<span class="ja">何が変わりましたか？</span></p>'
            '<div class="tutor-note"><div class="tn-body">'
            '<span class="tn-cap">Follow up</span><ul class="tn-more">'
            '<li>Give one example.</li><li>Why did it change?</li>'
            '<li>Why did it change?</li></ul></div></div><div class="fb"></div>'
        )
        errors = check_deck.freetalk_question_note_issues("q2", chunk)
        self.assertTrue(any("is not a question" in item for item in errors))
        self.assertTrue(any("duplicate follow-up" in item for item in errors))

    def test_freetalking_question_note_rejects_repeated_main_question(self):
        chunk = (
            '<p class="section-subtitle ask"><span class="ko">What changed?</span>'
            '<span class="ja">何が変わりましたか？</span></p>'
            '<div class="tutor-note"><div class="tn-body">'
            '<span class="tn-cap">Follow up</span><ul class="tn-more">'
            '<li>What changed?</li><li>Why did it change?</li>'
            '</ul></div></div><div class="fb"></div>'
        )
        errors = check_deck.freetalk_question_note_issues("q2", chunk)
        self.assertTrue(any("repeats the printed question" in item for item in errors))

    def test_freetalking_tutor_notes_reject_japanese_or_korean(self):
        source = (
            '<div class="tutor-note">Answer questions, then move on.</div>'
            '<div class="tutor-note">質問に答えてください。</div>'
            '<ul class="opt-note"><li>질문에 답해 주세요.</li></ul>'
        )
        errors = check_deck.freetalk_tutor_language_issues(source)
        self.assertEqual(len(errors), 2)

    def test_freetalking_style_accepts_canonical_direct_wording(self):
        chunk = (
            '<p class="section-subtitle"><span class="ko">'
            'Please choose your preferred discussion style.'
            '</span><span class="ja">希望する会話の進め方を選んでください。</span></p>'
            '<button>Discussion first</button><button>Correction first</button>'
        )
        self.assertEqual(check_deck.freetalk_style_issues(chunk), [])

    def test_freetalking_style_rejects_support_question_and_fluency_label(self):
        chunk = (
            '<p class="section-subtitle"><span class="ko">'
            'How would you like me to support your English today?'
            '</span><span class="ja">今日はどうしますか？</span></p>'
            '<button>Fluency first</button><button>Correction first</button>'
        )
        errors = check_deck.freetalk_style_issues(chunk)
        self.assertTrue(any("canonical direct script" in item for item in errors))
        self.assertTrue(any("Discussion first" in item for item in errors))

    def test_freetalking_title_accepts_exact_brief_title_with_level_suffix(self):
        title = "Something that surprised you about another culture"
        source = (
            f"<title>{title} · Full — PODO English</title>"
            '<div data-page-id="lesson-goal">'
            f'<h2 class="transition-title">{title} '
            '<span class="title-ja">(異文化で驚いたこと)</span></h2></div>'
        )
        self.assertEqual(check_deck.freetalk_title_issues(source, title), [])

    def test_freetalking_title_rejects_improvised_short_title(self):
        expected = "Something that surprised you about another culture"
        source = (
            "<title>This surprised me · Full — PODO English</title>"
            '<div data-page-id="lesson-goal">'
            '<h2 class="transition-title">This surprised me '
            '<span class="title-ja">(驚いたこと)</span></h2></div>'
        )
        errors = check_deck.freetalk_title_issues(source, expected)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("document title" in item for item in errors))
        self.assertTrue(any("visible title" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
