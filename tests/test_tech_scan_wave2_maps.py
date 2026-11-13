"""Accessible page maps and compact contents for Wave 2 references."""
from pathlib import Path
import unittest

from test_sources import Document, normalise

DIST = Path(__file__).resolve().parents[1] / 'site/dist'
PAGES = {
    'tech-scan-agents.html': ['decision', 'routes', 'coordination', 'controls', 'do-not-use', 'gaps', 'sources'],
    'tech-scan-workflows-factories.html': ['purpose', 'candidate', 'controls', 'pilot', 'do-not-use', 'gaps', 'sources'],
}


class Wave2MapTests(unittest.TestCase):
    def test_maps_name_describe_and_link_to_each_reading_destination(self):
        for name, targets in PAGES.items():
            with self.subTest(page=name):
                doc = Document((DIST / name).read_text())
                article = next(doc.root.elements('article'))
                maps = [e for e in article.elements('figure') if e.has_class('page-map')]
                self.assertEqual(len(maps), 1, 'one page map required')
                page_map = maps[0]
                caption = next(page_map.elements('figcaption'))
                self.assertEqual(normalise(caption.text()), 'This page at a glance')
                self.assertEqual(page_map.attrs.get('aria-labelledby'), caption.attrs.get('id'))
                notes = [e for e in page_map.elements() if e.attrs.get('id') == page_map.attrs.get('aria-describedby')]
                self.assertEqual(len(notes), 1)
                self.assertTrue(normalise(notes[0].text()))
                groups = [e for e in page_map.elements('li') if e.has_class('page-map-node')]
                self.assertEqual(len(groups), 4)
                self.assertTrue(all(normalise(next(g.elements('strong')).text()) for g in groups))
                links = list(page_map.elements('a'))
                self.assertEqual([a.attrs.get('href') for a in links], ['#' + t for t in targets])
                ids = [e.attrs['id'] for e in doc.root.elements() if 'id' in e.attrs]
                self.assertEqual(len(ids), len(set(ids)), 'IDs must be unique')
                sections = {e.attrs.get('id') for e in article.elements('section')}
                self.assertTrue(set(targets) <= sections)
                self.assertTrue(all(normalise(a.text()) for a in links))
                children = [e for e in article.children if not isinstance(e, str)]
                self.assertLess(children.index(page_map), next(i for i, e in enumerate(children) if e.has_class('mobile-contents')))

    def test_compact_contents_match_and_remain_flat(self):
        for name, targets in PAGES.items():
            with self.subTest(page=name):
                doc = Document((DIST / name).read_text())
                navs = [n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'On this page']
                self.assertEqual(len(navs), 2)
                for nav in navs:
                    links = list(nav.elements('a'))
                    self.assertLessEqual(len(links), 5)
                    self.assertFalse(list(nav.elements('ul')))
                    self.assertEqual([a.attrs.get('href') for a in links],
                                     ['#' + t for t in targets if t not in {'do-not-use', 'gaps'}])


if __name__ == '__main__':
    unittest.main()
