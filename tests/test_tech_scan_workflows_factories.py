"""Offline checks for the Workflows & factories research reference."""
from pathlib import Path
import unittest

from test_sources import Document, normalise

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-scan-workflows-factories.html'


def get_doc():
    return Document(PAGE.read_text() if PAGE.exists() else '')


def section(doc, name):
    return next(n for n in doc.root.elements('section') if n.attrs.get('id') == name)


def text(node):
    return normalise(node.text())


class WorkflowsFactoriesTests(unittest.TestCase):
    def test_reference_explains_the_decision_and_safe_candidate(self):
        doc = get_doc()
        self.assertTrue(list(doc.root.elements('h1')), 'The reference page must exist')
        self.assertIn('workflow', text(section(doc, 'purpose')).lower())
        self.assertIn('factory', text(section(doc, 'purpose')).lower())
        candidate = text(section(doc, 'candidate'))
        for phrase in ('use_bedrock', 'human', 'requirements', 'not a complete factory'):
            self.assertIn(phrase, candidate)
        gates = text(section(doc, 'controls'))
        for phrase in ('status checks', 'human', 'deploy', 'prompt', 'bypass'):
            self.assertIn(phrase, gates)

    def test_sources_navigation_and_local_validation(self):
        doc = get_doc()
        sources = section(doc, 'sources')
        self.assertEqual(len(list(sources.elements('ol'))), 1)
        entries = list(sources.elements('li'))
        self.assertGreaterEqual(len(entries), 5)
        ids = {n.attrs.get('id') for n in doc.root.elements()}
        for a in doc.root.elements('a'):
            href = a.attrs.get('href', '')
            if href.startswith('#'):
                self.assertIn(href[1:], ids)
        for nav in doc.root.elements('nav'):
            if nav.attrs.get('aria-label') == 'On this page':
                self.assertLessEqual(len(list(nav.elements('a'))), 5)
        hrefs = {a.attrs.get('href') for a in doc.root.elements('a')}
        for href in ('tech-scan-agents.html', 'tech-scan-harness.html', 'tech-scan-sandbox.html'):
            self.assertIn(href, hrefs)
        self.assertIn('not locally', text(next(n for n in doc.root.elements('header') if n.has_class('article-header'))))
        self.assertIn('pilot', text(section(doc, 'pilot')).lower())


if __name__ == '__main__':
    unittest.main()
