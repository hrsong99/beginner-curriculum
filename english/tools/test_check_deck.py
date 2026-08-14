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


if __name__ == "__main__":
    unittest.main()
