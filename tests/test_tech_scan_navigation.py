"""Tech Scan navigation and publication contracts."""
from pathlib import Path
import unittest
from test_sources import Document, normalise

DIST = Path(__file__).resolve().parents[1] / 'site/dist'
CHILDREN = ['tech-scan-models.html', 'tech-scan-harness.html', 'tech-scan-gateway.html', 'tech-scan-sandbox.html', 'tech-scan-agents.html', 'tech-scan-workflows-factories.html']
EXISTING = ['tech-scan.html', 'tech-scan-models.html', 'tech-scan-harness.html', 'tech-scan-gateway.html', 'tech-scan-sandbox.html']

class NavigationTests(unittest.TestCase):
    def test_hub_includes_research_signals_and_not_just_publication_plan(self):
        doc = Document((DIST / 'tech-scan.html').read_text())
        section = next((n for n in doc.root.elements('section') if n.attrs.get('id') == 'research-signals'), None)
        self.assertIsNotNone(section, 'Hub should present research signals')
        assert section is not None
        links = {a.attrs.get('href', '').split('#')[0] for a in section.elements('a')}
        self.assertTrue({'tech-scan-agents.html', 'tech-scan-workflows-factories.html'} <= links)
        for nav in (n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'On this page'):
            self.assertIn('#research-signals', [a.attrs.get('href') for a in nav.elements('a')])

    def test_sidebar_on_every_page_has_six_destinations_and_correct_page(self):
        for path in DIST.glob('*.html'):
            doc = Document(path.read_text())
            nav = next(n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'Guide')
            hub = next(a for a in nav.elements('a') if a.attrs.get('href') == 'tech-scan.html')
            siblings = hub.parent.children
            index = siblings.index(hub)
            group = next(n for n in siblings[index + 1:] if not isinstance(n, str))
            self.assertEqual([a.attrs.get('href') for a in group.elements('a')], CHILDREN, path.name)
            for a in group.elements('a'):
                expected = 'page' if path.name == a.attrs['href'] else None
                self.assertEqual(a.attrs.get('aria-current'), expected, path.name)

    def test_flat_matching_contents_have_at_most_nine_valid_targets(self):
        for name in EXISTING:
            doc = Document((DIST / name).read_text())
            contents = [n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'On this page']
            self.assertEqual(len(contents), 2, name)
            lists = []
            ids = {n.attrs['id'] for n in doc.root.elements() if 'id' in n.attrs}
            for nav in contents:
                links = list(nav.elements('a'))
                self.assertLessEqual(len(links), 9, name)
                self.assertFalse(list(nav.elements('ul')), name)
                self.assertTrue(all(a.attrs.get('href', '')[1:] in ids for a in links), name)
                lists.append([a.attrs['href'] for a in links])
            self.assertEqual(*lists, name)

    def test_chooser_exposes_all_six_references_in_four_rows(self):
        doc = Document((DIST / 'tech-scan.html').read_text())
        section = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'published-spokes')
        rows = list(next(section.elements('tbody')).elements('tr'))
        self.assertEqual(len(rows), 4)
        links = {a.attrs.get('href') for a in section.elements('a')}
        self.assertTrue(set(CHILDREN) <= links)

    def test_component_pages_crosslink_related_reference(self):
        for source, target in [('tech-scan-models.html', 'tech-scan-gateway.html'), ('tech-scan-gateway.html', 'tech-scan-models.html'), ('tech-scan-harness.html', 'tech-scan-sandbox.html'), ('tech-scan-sandbox.html', 'tech-scan-harness.html')]:
            doc = Document((DIST / source).read_text())
            article = next(doc.root.elements('article'))
            self.assertTrue(any(a.attrs.get('href') == target for a in article.elements('a')), source)
