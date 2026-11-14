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
                # Five entries, following the Workflows/Agents precedent:
                # do-not-use and gaps live in the body, not in this nav.
                self.assertLessEqual(len(list(nav.elements('a'))), 5)
                self.assertEqual([a.attrs.get('href') for a in nav.elements('a')],
                                 ['#evidence', '#independence', '#choices', '#decision', '#sources'])
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

    def test_codeguru_end_of_support_and_named_successors(self):
        doc = Document(PAGE.read_text())
        choices = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'choices')
        prose = normalise(choices.text())
        for expected in ('CodeGuru Security reached end of support on 20 November 2025',
                         'CodeGuru Reviewer has been in maintenance mode since 7 November 2025',
                         'Amazon Q Developer for code review',
                         'Amazon Inspector for code scanning',
                         'AWS Security Agent is not named as a CodeGuru successor'):
            self.assertIn(expected, prose)

    def test_no_managed_service_evaluates_code_correctness(self):
        doc = Document(PAGE.read_text())
        choices = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'choices')
        prose = normalise(choices.text())
        for expected in ('15 built-in evaluators',
                         'No managed AWS service evaluates code correctness',
                         'mutation testing'):
            self.assertIn(expected, prose)

    def test_automated_reasoning_is_detect_only(self):
        doc = Document(PAGE.read_text())
        choices = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'choices')
        prose = normalise(choices.text())
        for expected in ('detect mode only', 'no prompt-injection protection',
                         'English (US) only'):
            self.assertIn(expected, prose)

    def test_do_not_use_and_gaps_sections(self):
        doc = Document(PAGE.read_text())
        sections = {n.attrs['id']: n for n in doc.root.elements('section') if 'id' in n.attrs}
        self.assertIn('do-not-use', sections)
        self.assertIn('gaps', sections)
        do_not_use = normalise(sections['do-not-use'].text())
        for expected in ('CodeGuru Security', 'single benchmark number',
                         'same model family', "author agent's own tests",
                         'screening eval quoted as a release gate',
                         'blocking control or prompt-injection protection'):
            self.assertIn(expected, do_not_use)
        gaps = normalise(sections['gaps'].text())
        for expected in ('No managed AWS DAST service exists',
                         '31 March 2026', 'lists 13', 'up to 99%'):
            self.assertIn(expected, gaps)

if __name__ == '__main__':
    unittest.main()
