from __future__ import annotations

import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import plan_courses


class CourseMarketContractTests(unittest.TestCase):
    def test_rendered_course_has_exactly_one_japan_market_country_code(self):
        course = {
            "level": "초급",
            "slug": "test-course",
            "title": {"ko": "테스트", "en": "Test", "ja": "テスト"},
            "note": "테스트",
            "lessons": [],
        }
        rendered = plan_courses.course_yaml(
            course,
            {"type": "BASIC"},
            "100.010",
            "test-track",
            {},
        )
        self.assertEqual(re.findall(r"^  countryCode: (\S+)$", rendered, re.MULTILINE), ["JP"])

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
