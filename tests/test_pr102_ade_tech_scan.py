"""Regression checks for the Tech Scan's ADE supervision guidance."""
import re
import unittest
from pathlib import Path

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-scan-agents.html'


def ade_guidance(page):
    match = re.search(r'<h3 id="ade-supervision">.*?</h3>(.*?)(?=<h[1-6]\b|</section>)', page, re.S)
    return match.group(1).lower() if match else ''


class AdeTechScanTests(unittest.TestCase):
    def test_supervision_guidance_connects_choices_boundaries_and_evidence(self):
        page = PAGE.read_text(encoding='utf-8')
        guidance = ade_guidance(page)
        self.assertTrue(guidance, 'ADE guidance is missing from coordination')
        for phrase in ('supervis', 'harness', 'worktree', 'not a security boundary',
                       'approval', 'task', 'credential', 'hosted', 'test',
                       'integrate', 'review', 'pilot'):
            self.assertIn(phrase, guidance)
        for target in ('concept.html#supervise-agent-work', 'tech-scan-sandbox.html',
                       '#controls', '#source-35', '#source-36'):
            self.assertIn(target, guidance)
        for number, url in ((35, 'https://code.claude.com/docs/en/worktrees'),
                            (36, 'https://code.claude.com/docs/en/sandboxing')):
            entry = re.search(rf'<li id="source-{number}">(.*?)</li>', page, re.S)
            self.assertIsNotNone(entry)
            self.assertIn(url, entry.group(1))
            self.assertIn('href="#ade-supervision"', entry.group(1))
            self.assertRegex(guidance, rf'aria-label="source {number}: [^"]+">\[{number}\]')

    def test_approval_settings_can_cross_worktrees_and_are_pilot_tested(self):
        guidance = ade_guidance(PAGE.read_text(encoding='utf-8'))
        for phrase in ('claude code', 'bash', 'don’t ask again', 'main checkout',
                       'other worktrees', 'effective settings', 'approval crosses', 'task'):
            self.assertIn(phrase, guidance)
        self.assertRegex(guidance, r'(?s)don’t ask again.*?main checkout.*?other worktrees.*?#source-35')

    def test_guidance_excludes_next_heading(self):
        page = ('<h3 id="ade-supervision">ADE</h3><p>actual guidance</p>'
                '<h3>Unrelated</h3><p>approval crosses task</p></section>')
        self.assertNotIn('approval crosses task', ade_guidance(page))


if __name__ == '__main__':
    unittest.main()
