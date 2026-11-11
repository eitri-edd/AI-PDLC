"""Offline regressions for material findings from the November reference pass."""

from pathlib import Path
import unittest

from test_sources import Document, normalise


DIST = Path(__file__).resolve().parents[1] / "site/dist"


class ReferenceRefreshClaimTests(unittest.TestCase):
    def test_survey_fieldwork_is_distinct_from_publication(self):
        raw = (DIST / "transformation.html").read_text()
        self.assertIn("25 June to 29 July 2025", raw)
        self.assertIn("published on 5 November 2025", raw)
        self.assertFalse("McKinsey's November 2025 survey" in raw)

    def test_sandbox_startup_and_retry_escape_are_separately_bounded(self):
        raw = (DIST / "ai-pdlc.html").read_text()
        self.assertIn("sandbox.failIfUnavailable", raw)
        self.assertIn("sandbox.allowUnsandboxedCommands", raw)
        self.assertIn("excludedCommands", raw)
        self.assertFalse("but the CI run cannot" in raw)

    def test_partial_source_recovery_is_disclosed_in_canonical_entries(self):
        for page, identifier in (("concept.html", "source-4"),
                                 ("ai-pdlc.html", "source-5"),
                                 ("ai-pdlc.html", "source-2")):
            with self.subTest(page=page, source=identifier):
                document = Document((DIST / page).read_text())
                entry = next(node for node in document.root.elements("li")
                             if node.attrs.get("id") == identifier)
                text = normalise(entry.text()).casefold()
                self.assertTrue("partial" in text or "only the" in text,
                                "Retain the recovered source's limited scope")
                self.assertTrue("not reverified" in text or "not independently reverified" in text,
                                "Do not imply full-source verification")


if __name__ == "__main__":
    unittest.main()
