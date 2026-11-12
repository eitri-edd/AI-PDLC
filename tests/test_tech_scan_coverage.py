"""Offline diagram contracts; wave numbers describe publication, not execution."""
from pathlib import Path
import unittest

from test_sources import Document, normalise

ROOT = Path(__file__).resolve().parents[1]
WAVES = {
    "models": "1", "harness": "1", "gateway": "1", "sandbox": "1",
    "workflows": "2", "factories": "2", "agents": "2",
    "context": "3", "verification": "3", "delivery": "3",
    "languages": "3", "aws-platform": "3",
}


class TechScanCoverageTests(unittest.TestCase):
    def document(self):
        return Document((ROOT / "site/dist/tech-scan.html").read_text())

    def figure(self):
        figure = next((n for n in self.document().root.elements("figure")
                       if n.attrs.get("id") == "fig-waves"), None)
        self.assertIsNotNone(figure, "Planned coverage needs an actual component figure")
        assert figure is not None
        return figure

    def test_all_three_waves_have_their_real_publication_state_and_only_live_links(self):
        figure = self.figure()
        self.assertEqual(figure.attrs.get("data-diagram"), "static", "A relationship map has no playback order")
        svg = next(figure.elements("svg"), None)
        self.assertIsNotNone(svg, "The coverage map must be a visual SVG, not just prose")
        assert svg is not None
        nodes = [n for n in svg.elements("g") if "data-component" in n.attrs]
        self.assertEqual(len(nodes), 12)
        self.assertEqual({n.attrs["data-component"]: n.attrs.get("data-wave") for n in nodes}, WAVES)
        for node in nodes:
            name = node.attrs["data-component"]
            wave = WAVES[name]
            text = normalise(node.text()).casefold()
            self.assertIn("wave " + wave, text, name)
            state = "published" if wave == "1" else "planned"
            self.assertEqual(node.attrs.get("data-publication"), state, name)
            self.assertIn(state, text, name)
            links = list(node.elements("a"))
            if wave == "1":
                self.assertEqual([a.attrs.get("href") for a in links], [f"tech-scan-{name}.html"], name)
            else:
                self.assertEqual(links, [], "Do not link to unpublished pages: " + name)
            self.assertEqual(node.attrs.get("data-role"),
                             "view" if name in ("languages", "aws-platform") else "component", name)

    def test_relationships_distinguish_model_access_execution_and_cross_cutting_views(self):
        figure = self.figure()
        relationships = [n for n in figure.elements("g") if "data-from" in n.attrs]
        expected = {
            ("workflows", "factories"), ("factories", "agents"),
            ("factories", "verification"), ("verification", "delivery"),
            ("agents", "harness"), ("context", "harness"),
            ("harness", "gateway"), ("gateway", "models"),
            ("harness", "models"), ("harness", "sandbox"),
        }
        self.assertEqual({(n.attrs["data-from"], n.attrs.get("data-to")) for n in relationships}, expected)
        for relation in relationships:
            paths = list(relation.elements("path"))
            self.assertEqual(len(paths), 1)
            self.assertTrue(paths[0].attrs.get("d"))
            self.assertTrue(paths[0].attrs.get("marker-end"))
            self.assertTrue(list(relation.elements("text")), "Every conceptual arrow needs a visible label")
        nodes = [n for n in figure.elements("g") if "data-component" in n.attrs]
        components = {name for name in WAVES if name not in ("languages", "aws-platform")}
        for node in nodes:
            if node.attrs.get("data-role") == "view":
                self.assertEqual(set(node.attrs.get("data-references", "").split()), components)
        equivalent = normalise(next(figure.elements("details")).text()).casefold()
        for phrase in ("directly", "optional gateway", "sandbox", "context", "verification", "delivery",
                       "languages", "aws platform", "not runtime services"):
            self.assertIn(phrase, equivalent)
        for name in ("role", "aria-labelledby", "aria-describedby"):
            self.assertTrue(next(figure.elements("svg")).attrs.get(name), name)
        self.assertIn("not a runtime sequence", normalise(figure.text()).casefold())


if __name__ == "__main__":
    unittest.main()
