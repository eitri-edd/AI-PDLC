"""Regression contracts for Tech Scan readability aids."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "site" / "dist"


class TechScanReadabilityTests(unittest.TestCase):
    def test_every_tech_scan_page_has_a_visible_key_points_panel(self):
        pages = sorted(DIST.glob("tech-scan*.html"))
        self.assertTrue(pages)
        for page in pages:
            with self.subTest(page=page.name):
                html = page.read_text()
                self.assertEqual(html.count('class="tech-scan-key-points"'), 1)
                panel = re.search(r'<aside class="tech-scan-key-points".*?</aside>', html, re.S)
                self.assertIsNotNone(panel)
                assert panel is not None
                self.assertEqual(len(re.findall(r"<li>", panel.group(0))), 3)
                self.assertNotIn("<details>", html)

    def test_shared_detail_class_and_print_selector_are_present(self):
        css = (DIST / "styles.css").read_text()
        js = (DIST / "site.js").read_text()
        self.assertIn(".tech-scan-key-points", css)
        self.assertIn(".tech-scan-detail", css)
        self.assertIn(".tech-scan-detail", js)


if __name__ == "__main__":
    unittest.main()
