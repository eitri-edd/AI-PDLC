"""Offline regressions for the model-reference correction in issue #55.

These checks lock the reviewed example and citation together; they do not
replace live provider lifecycle checks during reference maintenance.
"""

from pathlib import Path
import unittest

from test_sources import Document, normalise


DIST = Path(__file__).resolve().parents[1] / "site/dist"


class ConceptModelTests(unittest.TestCase):
    def test_fable_example_keeps_the_provider_retention_limit_beside_the_claim(self):
        document = Document((DIST / "concept.html").read_text())
        paragraph = next((node for node in document.root.elements("p")
                          if "Fable 5.2 requires" in node.text()), None)
        self.assertIsNotNone(paragraph, "Keep the retention limit beside the model example")
        assert paragraph is not None
        text = normalise(paragraph.text())
        self.assertIn("30-day data retention", text)
        self.assertIn(
            "Zero data retention is unavailable unless expressly authorised by Anthropic.",
            text,
        )
        self.assertTrue(any(link.attrs.get("href") == "#source-18"
                            for link in paragraph.elements("a")))
        models = next(node for node in document.root.elements("section")
                      if node.attrs.get("id") == "models")
        self.assertIn(paragraph, list(models.elements("p")))

    def test_reviewed_fable_example_and_all_citations_use_the_same_version(self):
        document = Document((DIST / "concept.html").read_text())
        nodes = list(document.root.elements())
        source = next(node for node in nodes if node.attrs.get("id") == "source-18")
        source_link = next(source.elements("a"))
        with self.subTest(location="canonical source"):
            self.assertEqual(
                source_link.attrs["href"],
                "https://platform.claude.com/docs/en/models/fable-5-2/overview",
            )
            self.assertIn("Claude Fable 5.2", normalise(source_link.text()))
        example = next(node for node in nodes if node.tag == "p"
                       and "Anthropic’s current examples" in node.text())
        with self.subTest(location="model example"):
            self.assertIn("Claude Fable 5.2", normalise(example.text()))
        citations = [node for node in nodes if node.tag == "a"
                     and node.attrs.get("href") == "#source-18"]
        self.assertTrue(citations)
        for index, citation in enumerate(citations):
            with self.subTest(location="accessible citation", index=index):
                self.assertEqual(normalise(citation.text()), "[17]")
                self.assertEqual(
                    citation.attrs.get("aria-label"),
                    "Source 17: Anthropic, Claude Fable 5.2 documentation",
                )
        with self.subTest(location="published text and attributes"):
            raw = (DIST / "concept.html").read_text()
            self.assertFalse("Fable 5.1" in raw, "Legacy Fable version remains published")
            self.assertFalse("fable-5-1" in raw, "Legacy Fable URL remains published")


if __name__ == "__main__":
    unittest.main()
