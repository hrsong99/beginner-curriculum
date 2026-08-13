from __future__ import annotations

import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import plan_courses


class CoursePlanTests(unittest.TestCase):
    def test_approved_course_allocation_is_complete_and_unique(self):
        courses = plan_courses.planned_courses()
        self.assertEqual(len(courses), 43)
        self.assertEqual(len({course["slug"] for course in courses}), 43)
        self.assertEqual(len({course["classLevel"] for course in courses}), 43)
        self.assertIn("talk-balance-games-full", {course["slug"] for course in courses})

    def test_every_rendered_course_has_exactly_one_japan_market_country_code(self):
        for course in plan_courses.planned_courses():
            with self.subTest(course=course["slug"]):
                rendered = plan_courses.course_yaml(course)
                self.assertEqual(
                    re.findall(r"^  countryCode: (\S+)$", rendered, re.MULTILINE),
                    ["JP"],
                )
                self.assertNotIn("LANG_TYPE", "\n".join(
                    line for line in rendered.splitlines()
                    if not line.lstrip().startswith("#")
                ))
                self.assertIn("  enabled: false", rendered)

    def test_country_code_cannot_be_omitted(self):
        with self.assertRaisesRegex(ValueError, "required"):
            plan_courses.market_country_code(None)

    def test_country_code_must_be_supported_downstream(self):
        with self.assertRaisesRegex(ValueError, "KR.*JP|JP.*KR"):
            plan_courses.market_country_code("US")

    def test_japanese_market_course_cannot_use_kr(self):
        with self.assertRaisesRegex(ValueError, "require.*JP"):
            plan_courses.market_country_code("KR")


if __name__ == "__main__":
    unittest.main()
