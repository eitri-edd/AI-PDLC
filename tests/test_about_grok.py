"""About-page attribution for Grok Bot's role in finding X material."""

from pathlib import Path
import re
import unittest


ABOUT = Path(__file__).resolve().parents[1] / "site/dist/about.html"


class AboutGrokTests(unittest.TestCase):
    def test_scouting_discloses_grok_leads_and_verification(self):
        html = ABOUT.read_text(encoding="utf-8")
        match = re.search(r'<section id="scouting">(.*?)</section>', html, re.S)
        self.assertIsNotNone(match)
        scouting = match.group(1)
        self.assertRegex(scouting, r'Grok.*X posts.*leads')
        self.assertIn('verify the original post and its context', scouting)
        self.assertIn('credit the original author', scouting)
        self.assertIn('human review', scouting)
        self.assertIn('href="#source-6"', scouting)
        self.assertRegex(html, r'<li id="source-6">.*x\.ai/news/grok-bot-and-x.*href="#scouting"')


if __name__ == "__main__":
    unittest.main()
