"""Issue 112 terminology and targeted-source contracts."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Issue112TermsTests(unittest.TestCase):
    def test_dreams_preview_is_distinct_from_a_policy_approval(self):
        html = (ROOT / 'site/dist/tech-scan-context.html').read_text()
        self.assertIn('Anthropic’s Dreams API', html)
        self.assertIn('research preview', html)
        self.assertIn('not an approved default', html)
        self.assertIn('https://platform.claude.com/docs/en/managed-agents/dreams', html)
        self.assertIn('https://claude.com/resources/articles/new-in-claude-managed-agents', html)
        data = json.loads((ROOT / 'site/reference-checks.json').read_text())
        for url in ('https://platform.claude.com/docs/en/managed-agents/dreams', 'https://claude.com/resources/articles/new-in-claude-managed-agents'):
            record = next((r for r in data['references'] if r['url'] == url), None)
            self.assertIsNotNone(record)
            if record is None:
                continue
            self.assertIn('tech-scan-context.html', record['files'])
            self.assertTrue(any(r['file'] == 'tech-scan-context.html' and r.get('limitation') for r in record['claim_reviews']))

    def test_verification_uses_clear_terms_and_identifies_autoeval(self):
        html = (ROOT / 'site/dist/tech-scan-verification.html').read_text()
        self.assertIn('<strong>test oracle</strong>', html)
        self.assertIn('A lightweight preliminary evaluation quoted as a release gate', html)
        self.assertIn('third-party evaluators from the DeepEval and <a href="#source-7">AutoEval</a> libraries', html)
        self.assertIn('href="#source-7"', html)

    def test_role_is_descriptive_not_a_security_boundary(self):
        html = (ROOT / 'site/dist/tech-scan-agents.html').read_text()
        self.assertIn('Use persistent agents with a defined role only for ongoing goals', html)
        self.assertIn('not a filesystem or authorisation boundary', html)

if __name__ == '__main__':
    unittest.main()
