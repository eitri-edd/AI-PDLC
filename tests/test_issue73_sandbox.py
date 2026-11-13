"""Offline editorial and source contracts for issue 73's sandbox note."""
from pathlib import Path
import unittest

from test_sources import Document, normalise

PAGE = Path(__file__).resolve().parents[1] / "site/dist/tech-scan-sandbox.html"
OPENAI = "https://openai.com/index/securing-our-frontier-model-training-environment"
RAUCH = "https://x.com/rauchg/status/2114770919436808572"


def node(doc, identifier):
    return next(n for n in doc.root.elements() if n.attrs.get("id") == identifier)


class SandboxResidualRiskTests(unittest.TestCase):
    def test_shared_host_risk_is_scoped_and_cited_to_canonical_sources(self):
        doc = Document(PAGE.read_text())
        gaps = node(doc, "gaps")
        paragraphs = [normalise(p.text()) for p in gaps.elements("p")]
        note = next((p for p in paragraphs if "synthetic secrets" in p), "")
        self.assertIn("controlled frontier-model research", note)
        self.assertIn("shared CPU cache", note)
        self.assertIn("supplied", note)
        self.assertIn("not evidence of ordinary tenant compromise", note)
        self.assertIn("Guillermo Rauch", note)
        self.assertIn("partial extract", note)
        self.assertIn("co-resident", note)
        self.assertIn("patch", note)
        self.assertIn("platform owner", note)
        self.assertIn("residual", note)
        note_node = next(p for p in gaps.elements("p") if "synthetic secrets" in normalise(p.text()))
        refs = {a.attrs.get("href") for a in note_node.elements("a")}
        for identifier, url in (("source-23", OPENAI), ("source-24", RAUCH)):
            self.assertIn("#" + identifier, refs)
            entry = node(doc, identifier)
            self.assertIn(url, {a.attrs.get("href") for a in entry.elements("a")})
            self.assertIn("#gaps", {a.attrs.get("href") for a in entry.elements("a")})
        self.assertIn("partial", normalise(node(doc, "source-24").text()))
        self.assertIn("12 November 2026", normalise(node(doc, "sources").text()))


if __name__ == "__main__":
    unittest.main()
