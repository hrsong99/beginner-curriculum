#!/usr/bin/env python3
"""Focused tests for the non-creative lesson shell operations."""

from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import new_lesson


PILOT = new_lesson.ENGLISH / "tracks/1-core-patterns/courses/core-first-exchanges-2/lessons/20-asking-for-help/lesson.html"


class LessonShellTests(unittest.TestCase):
    def test_split_removes_pages_and_canonical_identity_comment(self):
        head, foot = new_lesson.split_shell(PILOT.read_text(encoding="utf-8"))
        self.assertIn('<div class="phone">', head)
        self.assertNotIn('data-page-id=', head + foot)
        self.assertNotIn('CORE 20', head + foot)
        self.assertIn('runtime/js/pager.js', foot)

    def test_retarget_changes_all_identity_fields(self):
        head, _foot = new_lesson.split_shell(PILOT.read_text(encoding="utf-8"))
        changed = new_lesson.retarget(head, lesson_id="31-past-action", level="A2", title="Past action", version="2099-01-02")
        self.assertIn('content="31-past-action"', changed)
        self.assertIn('content="A2"', changed)
        self.assertIn('content="2099-01-02"', changed)
        self.assertIn('<title>Past action — PODO English</title>', changed)

    def test_redepth_resolves_shared_refs_from_a_planned_deck_location(self):
        with tempfile.TemporaryDirectory(dir=new_lesson.ENGLISH / "tracks/1-core-patterns") as tmp:
            out = pathlib.Path(tmp) / "courses/x/lessons/31-past-action/lesson.html"
            page = new_lesson.redepth('<link href="../../runtime/css/lesson-card.css"><img src="../../korean/trial/assets/well-done.svg">', out)
            refs = [part.split('"')[1] for part in page.split('>') if '="' in part]
            self.assertTrue(all((out.parent / ref).resolve().is_file() for ref in refs))


if __name__ == "__main__":
    unittest.main()
