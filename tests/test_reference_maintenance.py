"""Offline completeness checks for recorded source-maintenance passes.

These checks establish inventory/date consistency, not live source truth.
"""

from datetime import date
import json
from pathlib import Path
import unittest
from urllib.parse import urldefrag, urlsplit

from test_sources import Document


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "site/dist"


class ReferenceMaintenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads((ROOT / "site/reference-checks.json").read_text())
        cls.pages = {path.relative_to(DIST).as_posix(): Document(path.read_text())
                     for path in sorted(DIST.rglob("*.html"))}
        cls.expected = {}
        for page, document in cls.pages.items():
            for node in document.root.elements():
                for attribute in ("href", "src"):
                    url = node.attrs.get(attribute, "")
                    if urlsplit(url).scheme in {"http", "https"}:
                        cls.expected.setdefault(urldefrag(url)[0], set()).add(page)

    def test_current_inventory_covers_every_published_external_url(self):
        references = self.inventory["references"]
        actual = {record["url"]: record for record in references}
        self.assertEqual(len(references), len(actual), "Duplicate current inventory URL")
        self.assertEqual(set(actual), set(self.expected))
        self.assertEqual(self.inventory.get("current_unique_urls"), len(actual))
        for url, record in actual.items():
            with self.subTest(url=url):
                self.assertEqual(set(record["files"]), self.expected[url])

    def test_each_page_pass_matches_its_published_reference_check_date(self):
        checked_on = date.fromisoformat(self.inventory["checked_on"]).isoformat()
        passes = self.inventory.get("page_passes", {})
        self.assertEqual(set(passes), set(self.pages))
        for page, document in self.pages.items():
            with self.subTest(page=page):
                self.assertEqual(passes[page]["checked_on"], checked_on)
                paragraphs = [node for node in document.root.elements("p")
                              if node.has_class("source-check-date")]
                if page == "index.html":
                    self.assertEqual(paragraphs, [])
                    self.assertEqual(passes[page]["scope"], "orientation-only operational links")
                else:
                    self.assertEqual(len(paragraphs), 1)
                    self.assertEqual(next(paragraphs[0].elements("time")).attrs["datetime"], checked_on)

    def test_each_current_url_has_dated_outcomes_and_prior_history_is_retained(self):
        outcomes = {"supported", "limited", "changed", "inaccessible", "operational", "unverified"}
        for record in self.inventory["references"]:
            with self.subTest(url=record["url"]):
                self.assertEqual(record["checked_on"], self.inventory["checked_on"])
                self.assertTrue(record.get("method"))
                self.assertTrue(record.get("result"))
                reviews = record.get("claim_reviews", [])
                self.assertEqual({review["file"] for review in reviews}, set(record["files"]))
                for review in reviews:
                    self.assertIn(review["outcome"], outcomes)
                    self.assertTrue(review["scope"])
                    if review["outcome"] in {"limited", "inaccessible", "unverified"}:
                        self.assertTrue(review.get("limitation"))
        history = self.inventory.get("history", [])
        self.assertTrue(history, "Keep the previous retrieval records, not only the new date")
        self.assertTrue(all("references" in run and "checked_on" in run for run in history))


if __name__ == "__main__":
    unittest.main()
