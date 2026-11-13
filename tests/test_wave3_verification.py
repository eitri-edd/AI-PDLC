"""Offline contracts for the Verification reference."""
from pathlib import Path
import unittest
from test_sources import Document, normalise

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-scan-verification.html'

class VerificationTests(unittest.TestCase):
    def test_reference_provides_decision_evidence_and_safe_boundaries(self):
        doc = Document(PAGE.read_text() if PAGE.exists() else '')
        self.assertTrue(list(doc.root.elements('h1')), 'Verification reference is missing')
        text = normalise(doc.root.text()).lower()
        for term in ('held-out', 'representative', 'oracle', 'retrieval', 'security', 'failure', 'human', 'release', 'agentcore', 'ragas', 'retention'):
            self.assertIn(term, text)
        for nav in doc.root.elements('nav'):
            if nav.attrs.get('aria-label') == 'On this page':
                self.assertLessEqual(len(list(nav.elements('a'))), 5)
        ids = {n.attrs.get('id') for n in doc.root.elements()}
        for a in doc.root.elements('a'):
            href = a.attrs.get('href', '')
            if href.startswith('#'):
                self.assertIn(href[1:], ids)
        hrefs = {a.attrs.get('href') for a in doc.root.elements('a')}
        for href in ('tech-scan-context.html', 'tech-scan-delivery.html', 'tech-scan-workflows-factories.html', 'eds-path-to-production.html'):
            self.assertIn(href, hrefs)
        sources = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'sources')
        self.assertEqual(len(list(sources.elements('ol'))), 1)
        for entry in sources.elements('li'):
            self.assertTrue(any(a.attrs.get('href', '').startswith('#') for a in entry.elements('a')))

if __name__ == '__main__':
    unittest.main()
