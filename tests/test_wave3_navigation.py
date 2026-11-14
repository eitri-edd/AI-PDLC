"""Wave 3 hub and grouped guide-navigation contracts."""
from pathlib import Path
import unittest
from test_sources import Document, normalise

DIST = Path(__file__).resolve().parents[1] / 'site/dist'
GROUPS = ['models-access', 'agent-environment', 'agents-workflows', 'verification-delivery']
SPOKES = ['tech-scan-agents.html', 'tech-scan-context.html', 'tech-scan-delivery.html',
          'tech-scan-gateway.html', 'tech-scan-harness.html', 'tech-scan-models.html',
          'tech-scan-sandbox.html', 'tech-scan-stack-views.html',
          'tech-scan-verification.html', 'tech-scan-workflows-factories.html']
REFERENCES = {
    'models-access': {'tech-scan-models.html', 'tech-scan-gateway.html'},
    'agent-environment': {'tech-scan-harness.html', 'tech-scan-sandbox.html', 'tech-scan-context.html'},
    'agents-workflows': {'tech-scan-agents.html', 'tech-scan-workflows-factories.html'},
    'verification-delivery': {'tech-scan-verification.html', 'tech-scan-delivery.html'},
}

class Wave3NavigationTests(unittest.TestCase):
    def test_guide_navigation_has_no_tech_scan_subnav(self):
        # The four group links all pointed at anchors on the hub page itself,
        # so the hub link stands alone; the next guide entry is AI-SDLC.
        for name in sorted(p.name for p in DIST.glob('*.html')):
            with self.subTest(page=name):
                doc = Document((DIST / name).read_text())
                nav = next(n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'Guide')
                hrefs = [a.attrs.get('href') for a in nav.elements('a')]
                self.assertEqual(hrefs.count('tech-scan.html'), 1, name)
                self.assertFalse([h for h in hrefs if h.startswith('tech-scan.html#')], name)
                self.assertEqual(hrefs[hrefs.index('tech-scan.html') + 1], 'ai-pdlc.html', name)
                self.assertFalse(any(a.attrs.get('aria-current') == 'location' for a in nav.elements('a')), name)
                current = [a.attrs.get('href') for a in nav.elements('a') if a.attrs.get('aria-current') == 'page']
                self.assertLessEqual(len(current), 1, name)
                if current:
                    self.assertEqual(current, [name], name)

    def test_spoke_pages_keep_parent_active_without_subnav(self):
        for name in SPOKES:
            with self.subTest(page=name):
                doc = Document((DIST / name).read_text())
                nav = next(n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'Guide')
                hub = next(a for a in nav.elements('a') if a.attrs.get('href') == 'tech-scan.html')
                self.assertIn('nav-parent-active', hub.attrs.get('class', '').split())
                self.assertFalse(any(a.attrs.get('aria-current') == 'location' for a in nav.elements('a')))
                self.assertFalse(any(a.attrs.get('aria-current') == 'page' for a in nav.elements('a')))

    def test_hub_groups_offer_direct_reference_choices(self):
        doc = Document((DIST / 'tech-scan.html').read_text())
        for group, expected in REFERENCES.items():
            with self.subTest(group=group):
                node = next((n for n in doc.root.elements() if n.attrs.get('id') == group), None)
                self.assertIsNotNone(node)
                self.assertTrue(expected <= {a.attrs.get('href') for a in node.elements('a')})
        links = {a.attrs.get('href') for a in doc.root.elements('a')}
        self.assertTrue({'tech-scan-stack-views.html#languages', 'tech-scan-stack-views.html#aws-platform'} <= links)

    def test_hub_contents_are_short_matching_and_valid(self):
        doc = Document((DIST / 'tech-scan.html').read_text())
        ids = {n.attrs['id'] for n in doc.root.elements() if 'id' in n.attrs}
        contents = [n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'On this page']
        self.assertEqual(len(contents), 2)
        links = [[a.attrs.get('href') for a in nav.elements('a')] for nav in contents]
        self.assertEqual(*links)
        self.assertEqual(links[0], [
            '#published-spokes', '#purpose', '#research-signals', '#how-to-read',
            '#planned-spokes', '#cross-cutting-views', '#gaps', '#layer-map', '#sources',
        ])
        self.assertTrue(all(link.startswith('#') and link[1:] in ids for link in links[0]))

if __name__ == '__main__':
    unittest.main()
