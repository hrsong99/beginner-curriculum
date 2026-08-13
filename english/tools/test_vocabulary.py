#!/usr/bin/env python3
"""Regression tests for vocabulary ownership, load and ledger generation."""

from __future__ import annotations

import pathlib
import sys
import unittest


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_running_lexicon
import check_deck
import vocabulary


ROOT = pathlib.Path(__file__).resolve().parent.parent
PILOT = ROOT / "tracks/1-core-patterns/courses/core-first-exchanges-2/lessons/20-asking-for-help/lesson.html"


def metadata(new: str = "box|箱", *, status: str = "reviewed", waiver: str = "") -> str:
    waiver_meta = f'<meta name="podo:vocabulary-waiver" content="{waiver}">' if waiver else ""
    return f"""
<meta name="podo:vocabulary-status" content="{status}">
<meta name="podo:vocabulary:new" content="{new}">
<meta name="podo:vocabulary:recycled" content="big|大きい|CORE-19">
<meta name="podo:vocabulary:assumed" content="menu|メニュー">
<meta name="podo:vocabulary:receptive" content="counter|カウンター">
{waiver_meta}
"""


class VocabularyTests(unittest.TestCase):
    def test_pilot_has_five_new_words_and_valid_provenance(self):
        data = vocabulary.parse(PILOT.read_text(encoding="utf-8"), source=PILOT)
        self.assertEqual(data["status"], "reviewed")
        self.assertEqual(len(data["categories"]["new"]), 5)
        self.assertEqual({item["source"] for item in data["categories"]["recycled"]}, {"CORE-19"})

    def test_duplicate_across_categories_is_rejected(self):
        with self.assertRaisesRegex(vocabulary.VocabularyError, "both new and assumed"):
            vocabulary.parse(metadata().replace("menu|メニュー", "box|ボックス"))

    def test_more_than_eight_requires_a_waiver(self):
        nine = "; ".join(f"word{i}|語{i}" for i in range(9))
        result = vocabulary.load_result(vocabulary.parse(metadata(nine)))
        self.assertEqual(result[0], "error")
        waived = vocabulary.load_result(vocabulary.parse(metadata(nine, waiver="scene requires it")))
        self.assertEqual(waived[0], "warning")

    def test_hint_chip_words_are_machine_readable(self):
        page = '<span class="hint-chip">箱:box</span><span class="hint-chip">運ぶ:carry</span>'
        self.assertEqual(vocabulary.hint_words(page), {"box", "carry"})

    def test_running_lexicon_is_current(self):
        records = build_running_lexicon.collect(build_running_lexicon.decks())
        actual = (ROOT / "reference/running-lexicon.md").read_text(encoding="utf-8")
        self.assertEqual(actual, build_running_lexicon.render(records))


if __name__ == "__main__":
    unittest.main()
