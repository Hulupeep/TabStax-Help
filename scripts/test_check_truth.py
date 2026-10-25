import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_truth  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class CheckTruthTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caps = check_truth.load_ledger()

    def check(self, name):
        return check_truth.check_page(FIXTURES / name, self.caps)

    def test_planned_without_badge_fails(self):
        errors, _ = self.check("bad-planned.md")
        self.assertTrue(any("@scribe" in e for e in errors), errors)

    def test_old_mcp_url_fails(self):
        errors, _ = self.check("bad-old-url.md")
        self.assertTrue(any("dash.tabstax.app" in e for e in errors), errors)

    def test_partial_without_badge_fails(self):
        errors, _ = self.check("bad-partial.md")
        self.assertTrue(any("invoice" in e.lower() for e in errors), errors)

    def test_badged_page_passes(self):
        errors, _ = self.check("good-planned.md")
        self.assertEqual(errors, [])

    def test_live_capability_only_warns(self):
        errors, warnings = self.check("live-warn.md")
        self.assertEqual(errors, [])
        self.assertTrue(warnings)

    def test_current_site_has_no_errors(self):
        errors = []
        for page in check_truth.page_files():
            errors += check_truth.check_page(page, self.caps)[0]
        self.assertEqual(errors, [], "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
