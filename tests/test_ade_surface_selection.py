"""Contracts for a practical, bounded ADE comparison."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ADESurfaceSelectionTests(unittest.TestCase):
    def test_supervision_section_compares_native_and_dedicated_surface(self):
        html = (ROOT / 'site/dist/tech-scan-agents.html').read_text()
        section = html.split('id="ade-supervision"', 1)[1].split('id="persistent-role-agents"', 1)[0]
        self.assertIn('Claude Code', section)
        self.assertIn('Orca', section)
        self.assertIn('href="#source-37"', section)
        self.assertIn('not a security boundary', section)
        self.assertIn('task-scoped credentials', section)
        self.assertIn('href="tech-scan-verification.html"', section)
        self.assertIn('href="tech-scan-delivery.html"', section)
        self.assertIn('id="source-37"', html)
        self.assertIn('https://orca.dev/docs/model/worktrees', html)
        self.assertIn('href="#source-38"', section)
        self.assertIn('permission-bypass', section)
        self.assertIn('custom', section)
        self.assertIn('https://orca.dev/docs/agents/supported', html)

    def test_orca_followup_tracks_the_agents_page(self):
        import json
        inventory = json.loads((ROOT / 'site/reference-checks.json').read_text())
        record = next(r for r in inventory['references'] if r['url'] == 'https://orca.dev/docs/model/worktrees')
        self.assertIn('tech-scan-agents.html', record['files'])
        self.assertIn({'file': 'tech-scan-agents.html', 'id': 'source-37'}, record['source_entries'])
        self.assertTrue(any(r.get('followup') == 'ade-tech-scan' and r['file'] == 'tech-scan-agents.html' and r['limitation'] for r in record['claim_reviews']))

if __name__ == '__main__':
    unittest.main()
