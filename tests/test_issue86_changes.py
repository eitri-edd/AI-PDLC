"""Issue #86 editorial and source-integrity regression checks.

These offline checks verify that selected guidance, source anchors and the reference
inventory remain present. They are not security tests or live provider qualification.
"""

from html import unescape
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urldefrag, urlsplit

from test_sources import Document, normalise


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "site" / "dist"
INVENTORY = ROOT / "site" / "reference-checks.json"

SECTIONS = {
    "tech-scan-sandbox.html": ("sandbox-trust-boundaries", "local-command-sandbox"),
    "tech-scan-gateway.html": ("gateway-credential-custody",),
    "tech-scan-workflows-factories.html": ("workflow-secret-boundary", "factory-maturity-ladder"),
    "tech-scan-agents.html": ("agent-deny-boundaries", "persistent-role-agents"),
    "tech-scan-context.html": ("memory-maintenance",),
    "tech-scan-verification.html": ("formal-model-checks",),
    "tech-scan-stack-views.html": ("typescript-auth-proofs",),
    "tech-scan-harness.html": ("agentcore-runtime-v2", "harness-code-mode"),
}
PAGES = (*SECTIONS, "concept.html")


class Issue86GuidanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {name: Document((DIST / name).read_text(encoding="utf-8"))
                     for name in PAGES}
        cls.raw = {name: (DIST / name).read_text(encoding="utf-8")
                   for name in PAGES}

    def test_decisions_are_attached_to_existing_page_sections(self):
        for page, ids in SECTIONS.items():
            document = self.pages[page]
            elements = {node.attrs.get("id"): node for node in document.root.elements()
                        if node.attrs.get("id")}
            for anchor in ids:
                with self.subTest(page=page, anchor=anchor):
                    self.assertIn(anchor, elements)
                    self.assertEqual(elements[anchor].tag, "h3")
                    self.assertTrue(normalise(elements[anchor].text()))

    def test_material_limits_stay_beside_cited_recommendations(self):
        expectations = {
            "tech-scan-sandbox.html": ("outside the command sandbox", "unavailable"),
            "tech-scan-gateway.html": ("credential", "revoke"),
            "tech-scan-workflows-factories.html": ("protected environments", "governance"),
            "tech-scan-agents.html": ("Trust", "not a filesystem"),
            "tech-scan-context.html": ("consolidation", "source"),
            "tech-scan-verification.html": ("invariant", "wrong specification"),
            "tech-scan-stack-views.html": ("runtime", "authorisation"),
            "tech-scan-harness.html": ("platformVersion", "host-bridge"),
        }
        for page, terms in expectations.items():
            text = normalise(self.pages[page].root.text()).lower()
            for term in terms:
                with self.subTest(page=page, term=term):
                    self.assertIn(term.lower(), text)

    def test_concepts_adds_vocabulary_and_calibrated_eval_guidance(self):
        text = normalise(self.pages["concept.html"].root.text()).lower()
        for term in ("domain vocabulary", "bounded", "threshold", "calibrate",
                     "held-out", "room-booking"):
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_citation_numbers_match_whole_ordered_sources_list(self):
        for page, doc in self.pages.items():
            sections = [node for node in doc.root.elements("section")
                        if node.attrs.get("id") == "sources"]
            self.assertEqual(len(sections), 1, page)
            lists = [node for node in sections[0].elements("ol")
                     if node.has_class("source-list")]
            self.assertEqual(len(lists), 1, page)
            entries = list(lists[0].elements("li"))
            ordinal = {node.attrs["id"]: idx
                       for idx, node in enumerate(entries, 1)
                       if node.attrs.get("id", "").startswith("source-")}
            for node in doc.root.elements("a"):
                href = node.attrs.get("href", "")
                if not re.fullmatch(r"#source-\d+", href):
                    continue
                with self.subTest(page=page, citation=href):
                    self.assertIn(href[1:], ordinal)
                    expected = ordinal[href[1:]]
                    self.assertEqual(normalise(node.text()), f"[{expected}]")
                    self.assertTrue(node.attrs.get("aria-label", "").startswith(
                        f"Source {expected}:"), node.attrs.get("aria-label"))

    def test_targeted_reference_inventory_covers_new_urls_and_pages(self):
        inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        records = {r["url"]: r for r in inventory["references"]}
        for page, raw in self.raw.items():
            urls = {urldefrag(unescape(raw_href))[0] for raw_href
                    in re.findall(r'\b(?:href|src)="(https?://[^"]+)"', raw)}
            for url in urls:
                with self.subTest(page=page, url=url):
                    self.assertIn(url, records)
                    self.assertIn(page, records[url]["files"])
                    self.assertTrue(any(c["file"] == page
                                        for c in records[url]["claim_reviews"]))
        self.assertEqual(inventory["current_unique_urls"], len(records))
        self.assertEqual(
            inventory["current_unique_hrefs"],
            len({href for item in records.values() for href in item["hrefs"]}),
        )


if __name__ == "__main__":
    unittest.main()
