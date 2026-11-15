import re
import unittest
from pathlib import Path

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/concept.html'


def paragraph(html, marker):
    return next((p for p in re.findall(r'<p\b[^>]*>.*?</p>', html, re.S) if marker in p), '')


class ADERefinementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = PAGE.read_text(encoding='utf-8')

    def test_worktree_is_not_access_boundary(self):
        p = paragraph(self.html, 'not a security sandbox')
        self.assertIn('same identity', p)
        self.assertIn('other worktrees', p)
        self.assertNotIn('cannot overwrite', p)
        self.assertIn('https://git-scm.com/docs/git-worktree', self.html)

    def test_worktree_setup_may_expose_untracked_secrets(self):
        p = paragraph(self.html, 'An ADE may run multiple coding agents')
        self.assertIn('plain Git checkout does not copy untracked files', p)
        self.assertIn('setup may copy or link', p)
        self.assertIn('secrets', p)
        self.assertIn('inspect setup and access', p)
        entry = re.search(r'<li id="source-40">.*?</li>', self.html, re.S)
        self.assertIsNotNone(entry)
        if entry is not None:
            self.assertIn('setup can copy or link', entry.group())
            self.assertNotIn('secrets outside version control are missing', entry.group())

    def test_task_access_and_runtime_controls(self):
        p = paragraph(self.html, 'For each task, grant')
        for term in ('short-lived credentials', 'test data', 'ports', 'hosted', 'location', 'filesystem', 'network', 'threat', 'tech-scan-sandbox.html#sandbox-trust-boundaries', '#action-approval'):
            self.assertIn(term, p)
        self.assertIn('https://code.claude.com/docs/en/sandboxing', self.html)

    def test_resumption_checks_validity_and_side_effects(self):
        p = paragraph(self.html, 'An interrupted run')
        for term in ('commit', 'inputs', 'configuration', 'rerun', 'side effects'):
            self.assertIn(term, p)

    def test_action_policy_has_three_distinct_outcomes(self):
        p = paragraph(self.html, 'Keep approvals risk-based')
        for term in ('permit', 'approval', 'deny'):
            self.assertIn(term, p)
        self.assertIn('configured', p)

    def test_review_and_final_integrated_evidence(self):
        p = paragraph(self.html, 'An approval covers')
        self.assertIn('reviewed commit', p)
        self.assertIn('policy', p)
        self.assertNotIn('checks cannot vouch', p)
        self.assertIn('required checks on the final integrated commit', self.html)

    def test_owner_decision_precedes_implementation(self):
        p = paragraph(self.html, 'Agents implement agreed changes')
        self.assertIn('after the owner decides', p)

    def test_next_step_links_to_ade_reference(self):
        p = paragraph(self.html, 'Compare two independent, low-risk development tasks')
        self.assertIn('tech-scan-agents.html#ade-supervision', p)

    def test_source_entries_link_to_ade(self):
        for source in ('source-46', 'source-47'):
            entry = re.search(rf'<li id="{source}">.*?</li>', self.html, re.S)
            self.assertIsNotNone(entry)
            self.assertIn('href="#supervise-agent-work"', entry.group())
