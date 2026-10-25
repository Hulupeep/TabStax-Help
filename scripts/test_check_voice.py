import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_voice  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class CheckVoiceTest(unittest.TestCase):
    def test_bad_page_is_flagged(self):
        kinds = " ".join(check_voice.check_page(FIXTURES / "bad-voice.md"))
        for kind in ("em dash", "positioning", "wellness", "hype"):
            self.assertIn(kind, kinds)

    def test_clean_page_passes(self):
        self.assertEqual(check_voice.check_page(FIXTURES / "good-planned.md"), [])

    def test_strict_mode_fails_on_findings(self):
        self.assertEqual(check_voice.main([str(FIXTURES / "bad-voice.md")]), 1)

    def test_report_mode_never_fails(self):
        self.assertEqual(check_voice.main([]), 0)


if __name__ == "__main__":
    unittest.main()
