"""Offline contracts for the Context reference, not live service tests."""
from pathlib import Path
import unittest

from test_sources import Document, normalise

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-scan-context.html'


class ContextReferenceTests(unittest.TestCase):
    def test_context_page_exists(self):
        self.assertTrue(PAGE.is_file(), 'Context reference page is missing')

    def test_read_boundary_links_existing_write_guidance(self):
        doc = Document(PAGE.read_text())
        memory = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'memory')
        self.assertIn('validating a write does not prove', normalise(memory.text()))
        self.assertTrue(any(a.attrs.get('href') == 'concept.html#context-engineering'
                            for a in memory.elements('a')))

    def test_pilot_checks_private_and_authorised_shared_content(self):
        doc = Document(PAGE.read_text())
        pilot = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'pilot')
        prose = normalise(pilot.text())
        for expected in ('user A', 'user B', 'broader namespace paths', 'Confirm A can retrieve it',
                         'shared artefact may itself be returned', 'If an isolation test fails'):
            self.assertIn(expected, prose)

    def test_sources_backlink_to_citing_sections(self):
        doc = Document(PAGE.read_text())
        sections = {n.attrs['id']: n for n in doc.root.elements('section') if 'id' in n.attrs}
        for name in ('choices', 'memory', 'construction'):
            for a in sections[name].elements('a'):
                href = a.attrs.get('href', '')
                if href.startswith('#source-'):
                    entry = next(n for n in sections['sources'].elements('li') if '#' + n.attrs.get('id', '') == href)
                    self.assertTrue(any(x.attrs.get('href') == '#' + name for x in entry.elements('a')), (name, href))

    def test_navigation_is_compact_and_links_neighbour_pages(self):
        doc = Document(PAGE.read_text())
        contents = [n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'On this page']
        self.assertEqual(len(contents), 2)
        for nav in contents:
            self.assertLessEqual(len(list(nav.elements('a'))), 5)
        links = {a.attrs.get('href') for a in doc.root.elements('a')}
        for link in ('tech-scan-verification.html', 'tech-scan-harness.html', 'tech-scan-gateway.html', 'eds-team-context.html'):
            self.assertIn(link, links)
