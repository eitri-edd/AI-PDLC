"""Offline checks for material course/local-harness revision differences."""

from pathlib import Path
import re
import unittest

from test_sources import Document, normalise

DIST = Path(__file__).resolve().parents[1] / "site/dist"
EDS_PAGES = (
    "eds-ai-workflow.html", "eds-developer-harness.html",
    "eds-path-to-production.html", "eds-po-ba-harness.html",
    "eds-skills-catalogue.html", "eds-team-context.html",
)


def element(page, identifier):
    document = Document((DIST / page).read_text())
    return next(node for node in document.root.elements()
                if node.attrs.get("id") == identifier)


def text(page, identifier):
    return re.sub(r"\s+([,.;:])", r"\1", normalise(element(page, identifier).text()))


class TrainingReferenceRefreshTests(unittest.TestCase):
    def test_course_source_entries_distinguish_mixed_revisions_from_local_19_steps(self):
        for page in EDS_PAGES:
            with self.subTest(page=page):
                entry = text(page, "source-training")
                self.assertIn("The public course contains mixed revisions.", entry)
                self.assertIn("S1 setup, S2 planning with /project-horizon, S3 architecture guardrails", entry)
                self.assertIn("developer Steps 1–5", entry)
                self.assertIn("five-phase video and interactive diagram as earlier material", entry)
                self.assertIn("This guide retains the local 19-step view.", entry)
                self.assertIn("Confirm the applicable harness revision and release controls with the workflow owner", entry)
                self.assertNotIn("Its five-phase view and /dependency-orchestrator differ", entry)

    def test_current_course_e2e_requirement_is_not_silently_equated_with_local_optional_gate(self):
        for page, identifier in (("eds-developer-harness.html", "closeout"),
                                 ("training.html", "workflow-skills")):
            with self.subTest(page=page):
                content = text(page, identifier)
                self.assertIn("requires /e2e", content)
                self.assertIn("final story MR cannot merge", content)
                self.assertIn("local 19-step", content)
                self.assertIn("optional", content)

    def test_standards_registration_retains_the_public_local_revision_conflict(self):
        content = text("eds-team-context.html", "standards")
        self.assertIn("does not tag stories", content)
        self.assertIn("skills/project-horizon/configs/standards.md", content)
        self.assertIn("installed revision", content)

    def test_training_companion_labels_its_retained_view_as_earlier(self):
        content = text("training.html", "source-2")
        self.assertIn("earlier five-phase view", content)
        self.assertIn("/project-horizon", content)
        self.assertIn("Steps 1–5", content)

    def test_reconciliation_warnings_bound_forecasts_at_each_call_site(self):
        for page, section in (
            ("eds-developer-harness.html", "plan"),
            ("eds-po-ba-harness.html", "handoff"),
            ("eds-skills-catalogue.html", "planning"),
            ("training.html", "po-workflow"),
        ):
            with self.subTest(page=page):
                content = text(page, section)
                self.assertIn("/reconcile-stories", content)
                self.assertIn("/project-horizon does not consume its reconciled files", content)
                self.assertIn("completed-task rounding inflates remaining-time estimates", content)
                self.assertIn("not to commit to a remaining-time forecast", content)
                self.assertIn("workflow owner verifies fixes in the installed revision", content)
                entry_id = "source-2" if page == "training.html" else "source-training"
                links = [node.attrs.get("href") for node in element(page, entry_id).elements("a")]
                self.assertIn("https://sgtechstack.github.io/ai-coding-workflow-d2-self-paced-training/00-pm-ba-workflow.html", links)


if __name__ == "__main__":
    unittest.main()
