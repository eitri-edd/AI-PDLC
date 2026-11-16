"""Editorial contracts for the AI workflows trend reference (content-sourcing agent scan)."""
from pathlib import Path
import unittest

from test_sources import Document, normalise, statically_hidden

DIST = Path(__file__).resolve().parents[1] / "site/dist"
PAGE = "tech-scan-ai-workflows.html"
PACKS = ("Matt Pocock skills", "Superpowers", "Agent Skills", "pstack", "gstack", "tstack", "ub-mode")


def by_id(doc, identity):
    return next(n for n in doc.root.elements() if n.attrs.get("id") == identity)


class AIWorkflowsTests(unittest.TestCase):
    def document(self, name=PAGE):
        return Document((DIST / name).read_text())

    def test_hub_and_workflows_reference_link_to_the_page(self):
        for name in ("tech-scan.html", "tech-scan-workflows-factories.html"):
            with self.subTest(page=name):
                article = next(self.document(name).root.elements("article"))
                self.assertIn(PAGE, {a.attrs.get("href") for a in article.elements("a")})
        hub = self.document("tech-scan.html")
        for section in ("agents-workflows", "research-signals"):
            self.assertIn(PAGE, {a.attrs.get("href") for a in by_id(hub, section).elements("a")})

    def test_rankings_cover_every_pack_and_separate_attention_from_acceptance(self):
        signals = by_id(self.document(), "signals")
        table = next(signals.elements("table"))
        rows = [normalise(next(r.elements("th")).text()) for r in next(table.elements("tbody")).elements("tr")]
        self.assertEqual(len(rows), len(PACKS))
        for pack in PACKS:
            self.assertTrue(any(row.startswith(pack) for row in rows), pack)
        text = normalise(signals.text()).casefold()
        for phrase in ("viral index", "acceptance", "not a measurement of productivity"):
            self.assertIn(phrase, text)

    def test_authority_limits_and_pilot_checks_stay_visible(self):
        doc = self.document()
        for section in ("controls", "pilot"):
            node = by_id(doc, section)
            visible = [p for p in node.elements("p") if not statically_hidden(p)]
            text = normalise(" ".join(p.text() for p in visible)).casefold()
            with self.subTest(section=section):
                if section == "controls":
                    for phrase in ("does not enforce", "full-send", "merge", "no significant pass-rate gain"):
                        self.assertIn(phrase, text)
                else:
                    self.assertIn("no-pack baseline", text)
        checklist = next(n for n in by_id(doc, "pilot").elements("ul") if n.has_class("checklist"))
        self.assertFalse(statically_hidden(checklist))
        self.assertIn("deploy", normalise(checklist.text()).casefold())

    def test_star_counts_are_not_presented_as_evidence(self):
        text = normalise(self.document().root.text())
        self.assertIn("GitHub stars are not usage", text)
        self.assertNotIn("322,429", text)


if __name__ == "__main__":
    unittest.main()
