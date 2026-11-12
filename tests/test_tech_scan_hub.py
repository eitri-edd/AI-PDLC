"""Offline editorial contracts; these do not establish live product truth."""
from pathlib import Path
import unittest

from test_sources import Document, normalise

ROOT = Path(__file__).resolve().parents[1]


def by_id(document, identity):
    return next(node for node in document.root.elements()
                if node.attrs.get("id") == identity)


class TechScanHubTests(unittest.TestCase):
    def document(self):
        return Document((ROOT / "site/dist/tech-scan.html").read_text())

    def test_task_illustration_separates_model_and_optional_tool_paths(self):
        figure = by_id(self.document(), "fig-task-chain")
        text = normalise(figure.text()).casefold()
        self.assertIn("illustrative", text)
        self.assertIn("model requests", text)
        self.assertIn("tool calls", text)
        self.assertIn("optional", text)
        self.assertIn("results return to the harness", text)
        self.assertNotIn("context spoke (wave 2)", text)
        description = by_id(self.document(), "fig-task-chain-title-desc")
        self.assertIn("results return to the harness", normalise(description.text()).casefold())

    def test_component_index_is_a_reader_choice_not_a_publication_status_table(self):
        section = by_id(self.document(), "published-spokes")
        self.assertEqual(normalise(next(section.elements("h2")).text()), "Choose a component")
        headings = [normalise(node.text()) for node in next(section.elements("thead")).elements("th")]
        self.assertEqual(headings, ["Your question", "Open this reference"])
        self.assertEqual(len(list(next(section.elements("tbody")).elements("tr"))), 4)
        self.assertNotIn("TBD", normalise(section.text()))

    def test_publication_plan_is_optional_and_old_figure_links_still_resolve(self):
        document = self.document()
        planned = by_id(document, "planned-spokes")
        self.assertEqual(normalise(next(planned.elements("h2")).text()), "Planned coverage")
        for identity in ("fig-waves", "fig-waves-title-caption", "fig-waves-title", "fig-waves-title-desc"):
            node = by_id(document, identity)
            ancestors = []
            while node.parent is not None:
                node = node.parent
                ancestors.append(node)
            self.assertTrue(any(n.tag == "details" and "open" not in n.attrs for n in ancestors), identity)

    def test_selection_assumptions_are_scoped_and_evidence_is_not_qualification(self):
        purpose = normalise(by_id(self.document(), "purpose").text())
        self.assertIn("For this scan", purpose)
        self.assertIn("managed Claude or OpenAI", purpose)
        evidence = normalise(by_id(self.document(), "how-to-read").text())
        self.assertIn("reference deployment", evidence.casefold())
        self.assertIn("does not establish", evidence)
        self.assertNotIn("Every spoke follows the same shape", evidence)

    def test_original_diagram_and_source_destinations_survive(self):
        identities = {node.attrs["id"] for node in self.document().root.elements() if "id" in node.attrs}
        expected = {"main", "tech-scan-note", "arrow", "arrow-accent", "d-grad-node", "d-grad-accent",
                    "page-map-caption", "page-map-note", "purpose", "fig-task-chain",
                    "fig-task-chain-title-caption", "fig-task-chain-title", "fig-task-chain-title-desc",
                    "how-to-read", "published-spokes", "planned-spokes", "fig-waves",
                    "fig-waves-title-caption", "fig-waves-title", "fig-waves-title-desc",
                    "cross-cutting-views", "gaps", "layer-map", "sources", "source-1", "source-2",
                    "source-3", "source-4", "source-5"}
        self.assertTrue(expected <= identities, expected - identities)

    def test_hub_lookup_index_replaces_redundant_page_map_with_recorded_exception(self):
        article = next(self.document().root.elements("article"))
        self.assertFalse(any(n.tag == "figure" and n.has_class("page-map") for n in article.elements()))
        self.assertEqual(next(article.elements("section")).attrs.get("id"), "published-spokes")
        design = (ROOT / "design.md").read_text()
        self.assertTrue("Tech Scan hub lookup exception" in design, "Record the scoped map exception")

    def test_writing_standard_records_the_narrow_research_reference_allowance(self):
        writing = (ROOT / "writing.md").read_text()
        self.assertTrue("Tech Scan research-reference exception" in writing, "Missing narrow Tech Scan status exception")
        self.assertTrue("consistent comparison fields, not identical section headings" in writing, "Missing task-fitting reference guidance")
        self.assertTrue("do not require readers to leave the page" in writing, "Missing contextual-definition guidance")


if __name__ == "__main__":
    unittest.main()
