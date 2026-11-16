"""Editorial contracts for the AI workflows comparison (issue #115)."""
from pathlib import Path
import unittest

from test_sources import Document, normalise, statically_hidden

DIST = Path(__file__).resolve().parents[1] / "site/dist"
PAGE = "tech-scan-ai-workflows.html"
PACKS = ("Matt Pocock skills", "Superpowers", "Agent Skills", "pstack", "gstack", "tstack", "ub-mode")
ANCHORS = ("approaches", "signals", "lifecycle", "controls", "pilot", "gaps", "sources")


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
        blurb = normalise(by_id(hub, "research-signals").text()).casefold()
        self.assertIn("engineering approach", blurb)
        self.assertNotIn("by acceptance", blurb)

    def test_comparison_covers_every_pack_without_a_ranked_winner(self):
        doc = self.document()
        approaches = by_id(doc, "approaches")
        table = next(approaches.elements("table"))
        rows = [normalise(next(r.elements("th")).text()) for r in next(table.elements("tbody")).elements("tr")]
        self.assertEqual(len(rows), len(PACKS))
        for pack in PACKS:
            self.assertTrue(any(row.startswith(pack) for row in rows), pack)
        header = normalise(" ".join(th.text() for th in table.elements("th"))).casefold()
        for phrase in ("engineering approach", "what changes versus a plain agent run",
                       "evaluate it for", "trade-off", "prerequisites and permissions",
                       "evidence confidence"):
            self.assertIn(phrase, header)
        text = normalise(approaches.text()).casefold()
        self.assertIn("not a ranking", text)
        self.assertNotIn("universal winner", text)
        self.assertNotIn("industry acceptance", text)

    def test_scores_are_demoted_and_attention_stays_separate_from_outcomes(self):
        doc = self.document()
        signals = by_id(doc, "signals")
        text = normalise(signals.text()).casefold()
        for phrase in ("viral index", "ecosystem evidence score", "not a measurement of productivity",
                       "not a shortlist"):
            self.assertIn(phrase, text)
        details = next(signals.elements("details"))
        self.assertIn("research methods and historical signals", normalise(details.text()).casefold())
        score_table = next(details.elements("table"))
        rows = [normalise(next(r.elements("th")).text()) for r in next(score_table.elements("tbody")).elements("tr")]
        self.assertEqual(len(rows), len(PACKS))
        for pack in PACKS:
            self.assertTrue(any(row.startswith(pack) for row in rows), pack)
        self.assertIn("analyst-assigned", normalise(score_table.text()).casefold())
        # The old league table is disclosure, not the page headline.
        headline = " ".join(normalise(node.text()) for node in doc.root.elements(("h1", "h2")))
        header = next(doc.root.elements("header"))
        key_points = next(n for n in doc.root.elements("aside") if n.has_class("tech-scan-key-points"))
        for node in (header, key_points):
            self.assertNotIn("industry acceptance", normalise(node.text()).casefold())
        self.assertNotIn("industry acceptance", headline.casefold())

    def test_authority_limits_are_versioned_and_pilot_has_three_arms(self):
        doc = self.document()
        controls = by_id(doc, "controls")
        visible = [p for p in controls.elements("p") if not statically_hidden(p)]
        text = normalise(" ".join(p.text() for p in visible)).casefold()
        for phrase in ("does not enforce", "full-send", "full-stop", "merge",
                       "no significant pass-rate gain", "0.4.4", "on by default",
                       "autopilot-full", "push to the main line"):
            self.assertIn(phrase, text)
        self.assertNotIn("108-task", text)
        pilot = by_id(doc, "pilot")
        pilot_text = normalise(" ".join(p.text() for p in pilot.elements("p") if not statically_hidden(p))).casefold()
        self.assertIn("no-pack baseline", pilot_text)
        self.assertIn("three arms", pilot_text)
        self.assertIn("single most relevant skill", pilot_text)
        checklist = next(n for n in pilot.elements("ul") if n.has_class("checklist"))
        self.assertFalse(statically_hidden(checklist))
        checks = normalise(checklist.text()).casefold()
        for phrase in ("deploy", "acceptance tests", "tokens", "data sent off the machine", "skill actually fired"):
            self.assertIn(phrase, checks)

    def test_known_factual_errors_are_not_repeated_as_current_guidance(self):
        text = normalise(self.document().root.text())
        folded = text.casefold()
        self.assertNotIn("108-task", folded)
        self.assertNotIn("plan before touching code", folded)
        self.assertIn("108", text)
        self.assertIn("planning is not a default", folded)
        self.assertIn("code-review", folded)

    def test_navigation_anchors_and_star_counts_stay_in_place(self):
        doc = self.document()
        ids = {n.attrs.get("id") for n in doc.root.elements()}
        for anchor in ANCHORS:
            self.assertIn(anchor, ids)
        self.assertIn("source-1", ids)
        text = normalise(doc.root.text())
        self.assertIn("GitHub stars are not usage", text)
        self.assertNotIn("322,429", text)
        for nav in (n for n in doc.root.elements("nav") if n.attrs.get("aria-label") == "On this page"):
            hrefs = [a.attrs.get("href") for a in nav.elements("a")]
            self.assertEqual(hrefs, ["#approaches", "#lifecycle", "#signals", "#controls", "#pilot", "#gaps", "#sources"])


if __name__ == "__main__":
    unittest.main()
