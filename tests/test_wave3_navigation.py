"""Wave 3 hub and grouped guide-navigation contracts."""
from pathlib import Path
import unittest
from test_sources import Document, normalise

DIST = Path(__file__).resolve().parents[1] / 'site/dist'
GROUPS = ['models-access', 'agent-environment', 'agents-workflows', 'verification-delivery']
PREEXISTING = [p.name for p in DIST.glob('*.html') if p.name not in {
    'tech-scan-context.html', 'tech-scan-verification.html',
    'tech-scan-delivery.html', 'tech-scan-stack-views.html'}]
REFERENCES = {
    'models-access': {'tech-scan-models.html', 'tech-scan-gateway.html'},
    'agent-environment': {'tech-scan-harness.html', 'tech-scan-sandbox.html', 'tech-scan-context.html'},
    'agents-workflows': {'tech-scan-agents.html', 'tech-scan-workflows-factories.html'},
    'verification-delivery': {'tech-scan-verification.html', 'tech-scan-delivery.html'},
}

class Wave3NavigationTests(unittest.TestCase):
    def test_guide_navigation_groups_link_to_hub_on_existing_pages(self):
        for name in PREEXISTING:
            with self.subTest(page=name):
                doc = Document((DIST / name).read_text())
                nav = next(n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'Guide')
                hub = next(a for a in nav.elements('a') if a.attrs.get('href') == 'tech-scan.html')
                siblings = hub.parent.children
                group = next(n for n in siblings[siblings.index(hub) + 1:] if not isinstance(n, str))
                self.assertEqual([a.attrs.get('href') for a in group.elements('a')],
                                 ['tech-scan.html#' + g for g in GROUPS])
                self.assertLessEqual(sum(a.attrs.get('aria-current') == 'page' for a in nav.elements('a')), 1)
                for a in nav.elements('a'):
                    if a.attrs.get('aria-current') == 'page':
                        self.assertEqual(a.attrs.get('href'), name)
                matches = [g for g, pages in REFERENCES.items() if name in pages]
                current = [a.attrs.get('href') for a in group.elements('a') if a.attrs.get('aria-current') == 'location']
                self.assertEqual(current, ['tech-scan.html#' + matches[0]] if matches else [])

    def test_new_page_sidebar_groups_and_current_location(self):
        expected = {
            'tech-scan-context.html': 'agent-environment',
            'tech-scan-verification.html': 'verification-delivery',
            'tech-scan-delivery.html': 'verification-delivery',
            'tech-scan-stack-views.html': None,
        }
        for name, current_group in expected.items():
            with self.subTest(page=name):
                doc = Document((DIST / name).read_text())
                nav = next(n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'Guide')
                hub = next(a for a in nav.elements('a') if a.attrs.get('href') == 'tech-scan.html')
                self.assertIn('nav-parent-active', hub.attrs.get('class', '').split())
                group = next(n for n in hub.parent.children[hub.parent.children.index(hub) + 1:] if not isinstance(n, str))
                self.assertEqual([a.attrs.get('href') for a in group.elements('a')],
                                 ['tech-scan.html#' + g for g in GROUPS])
                current = [a.attrs.get('href') for a in nav.elements('a') if a.attrs.get('aria-current') == 'location']
                self.assertEqual(current, ['tech-scan.html#' + current_group] if current_group else [])
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
        self.assertLessEqual(len(links[0]), 5)
        self.assertTrue(all(link.startswith('#') and link[1:] in ids for link in links[0]))

if __name__ == '__main__':
    unittest.main()
