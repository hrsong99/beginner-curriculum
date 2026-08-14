#!/usr/bin/env python3
"""Regression tests for the live English curriculum parsers."""

from __future__ import annotations

import pathlib
import sys
import unittest


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import track_parsers


class LiveCurriculumTests(unittest.TestCase):
    def test_all_tracks_parse_to_the_declared_size(self):
        expected = {
            "1-core-patterns": 122,
            "2-contextual-english": 60,
            "3-freetalking": 121,
            "4-pronunciation": 12,
        }
        for track, count in expected.items():
            with self.subTest(track=track):
                self.assertEqual(len(track_parsers.parse_track(track)), count)

    def test_core_contract_is_complete(self):
        lessons = track_parsers.parse_core()
        self.assertEqual(lessons[0]["id"], "CORE-1")
        self.assertEqual(lessons[-1]["id"], "CORE-122")
        self.assertTrue(all(len(lesson["models"]) == 2 for lesson in lessons))
        self.assertTrue(all(lesson["jp"] for lesson in lessons))
        self.assertEqual(sum(bool(lesson["grammar"]) for lesson in lessons), 70)
        self.assertEqual([lesson["no"] for lesson in lessons if not lesson["grammar"]], list(range(71, 123)))
        self.assertTrue(all("___" in pattern for lesson in lessons for pattern in lesson["patterns"]))
        self.assertTrue(all("___" not in model["model"] for lesson in lessons for model in lesson["models"]))

    def test_contextual_reactions_and_core_references_are_structured(self):
        lessons = track_parsers.parse_contextual()
        self.assertTrue(all(len(lesson["models"]) == 2 for lesson in lessons))
        self.assertTrue(all(model["reaction"] for lesson in lessons for model in lesson["models"]))
        self.assertTrue(all("___" in pattern for lesson in lessons for pattern in lesson["patterns"]))
        self.assertTrue(all("___" not in model["model"] for lesson in lessons for model in lesson["models"]))
        self.assertEqual({lesson["areaNo"] for lesson in lessons}, {1, 2})
        self.assertEqual({lesson["courseNo"] for lesson in lessons}, set(range(1, 11)))
        self.assertTrue(all(lesson["courseSize"] == 6 for lesson in lessons))
        self.assertEqual([lesson["area"] for lesson in lessons[:30]], ["Travel English"] * 30)
        self.assertEqual([lesson["area"] for lesson in lessons[30:]], ["Business English"] * 30)
        self.assertEqual(
            [lessons[index]["floor"] for index in range(0, 60, 6)],
            [47, 59, 70, 91, 103, 47, 59, 81, 92, 103],
        )
        self.assertGreaterEqual(min(lesson["floor"] for lesson in lessons), 47)
        self.assertEqual(lessons[7]["models"][1]["coreRefs"], [57, 60])
        self.assertEqual(lessons[25]["models"][1]["coreRefs"], [72, 65])
        self.assertFalse(
            [
                (lesson["id"], model["pattern"], ref)
                for lesson in lessons
                for model in lesson["models"]
                for ref in model["coreRefs"]
                if ref > lesson["floor"] + 12 and not model["chunk"]
            ],
            "patterns more than about two Core units above the course floor must be bounded chunks",
        )
        refs = [ref for lesson in lessons for model in lesson["models"] for ref in model["coreRefs"]]
        self.assertTrue(refs)
        self.assertTrue(all(1 <= ref <= 122 for ref in refs))

    def test_freetalking_has_an_immediate_opening_and_ladder(self):
        lessons = track_parsers.parse_freetalking()
        self.assertTrue(all(lesson["opening"] and lesson["ladder"] for lesson in lessons))
        self.assertEqual({lesson["themeNo"] for lesson in lessons}, set(range(1, 12)))
        self.assertTrue(lessons[0]["opening"].endswith("a coworker)*"))
        self.assertTrue(lessons[0]["ladder"].endswith("what would surprise *me* about Japan"))
        self.assertIn("the essay prompt this track exists to avoid", lessons[65]["shared"])
        self.assertEqual(lessons[8]["title"], "A purchase that was worth it")
        self.assertEqual(lessons[106]["title"], "More money or more time?")
        self.assertFalse([lesson["id"] for lesson in lessons if lesson["title"].startswith("My ")])

    def test_pronunciation_stays_planning_only(self):
        lessons = track_parsers.parse_pronunciation()
        self.assertTrue(all(lesson["level"] == "planning only" for lesson in lessons))


if __name__ == "__main__":
    unittest.main()
