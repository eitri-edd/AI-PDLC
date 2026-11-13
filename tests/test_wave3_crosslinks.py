"""Navigation density and contextual hand-offs on existing references."""
from pathlib import Path
import unittest
from test_sources import Document

DIST = Path(__file__).resolve().parents[1] / 'site/dist'
PAGES = ('agents', 'gateway', 'harness', 'models', 'sandbox', 'workflows-factories')

class Wave3Crosslinks(unittest.TestCase):
    def document(self, page):
        return Document((DIST / f'tech-scan-{page}.html').read_text())

    def test_mobile_and_desktop_contents_are_compact_and_match(self):
        for page in PAGES:
            with self.subTest(page=page):
                doc = self.document(page)
                navs = [n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'On this page']
                self.assertEqual(len(navs), 2)
                routes = [[a.attrs.get('href') for a in n.elements('a')] for n in navs]
                self.assertEqual(routes[0], routes[1])
                self.assertLessEqual(len(routes[0]), 5)
                ids = {n.attrs.get('id') for n in doc.root.elements()}
                self.assertTrue(all(h.startswith('#') and h[1:] in ids for h in routes[0]))

    def test_contextual_handoffs_are_in_article_prose(self):
        for page, destinations in {'harness': ('context',), 'agents': ('verification',),
                                   'workflows-factories': ('verification', 'delivery')}.items():
            article = next(self.document(page).root.elements('article'))
            for destination in destinations:
                with self.subTest(page=page, destination=destination):
                    links = [a for a in article.elements('a') if a.attrs.get('href') == f'tech-scan-{destination}.html']
                    self.assertTrue(any(a.parent.tag in ('p', 'li') for a in links))

if __name__ == '__main__':
    unittest.main()
