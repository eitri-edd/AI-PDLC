import re
import unittest
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1] / 'site' / 'dist'
PAGE = ROOT / 'tech-scan-stack-views.html'

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = []; self.hrefs = []; self.contents = [] ; self.in_contents = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.ids.append(a['id'])
        if tag == 'nav' and a.get('aria-label') == 'On this page': self.in_contents = True; self.contents.append([])
        if tag == 'a' and a.get('href'):
            self.hrefs.append(a['href'])
            if self.in_contents: self.contents[-1].append(a['href'])
    def handle_endtag(self, tag):
        if tag == 'nav': self.in_contents = False

class StackViewsTests(unittest.TestCase):
    def test_cross_cutting_reference_navigation_and_citations(self):
        self.assertTrue(PAGE.exists(), 'stack views page is missing')
        text = PAGE.read_text(); doc = Links(); doc.feed(text)
        for section in ('languages', 'aws-platform', 'sources'):
            self.assertIn(section, doc.ids)
        self.assertEqual(len(doc.ids), len(set(doc.ids)))
        self.assertTrue(doc.contents)
        for items in doc.contents:
            self.assertLessEqual(len(items), 5)
            self.assertIn('#sources', items)
        for href in doc.hrefs:
            if href.startswith('#'):
                self.assertIn(href[1:], doc.ids, href)
            elif href.startswith('tech-scan-') and '.html#' in href:
                filename, fragment = href.split('#', 1)
                target = ROOT / filename
                self.assertTrue(target.exists(), href)
                target_doc = Links(); target_doc.feed(target.read_text())
                self.assertIn(fragment, target_doc.ids, href)
        for owner in ('models', 'harness', 'gateway', 'sandbox', 'agents', 'workflows-factories', 'context', 'verification', 'delivery'):
            self.assertTrue(any(h.startswith('tech-scan-' + owner + '.html#') for h in doc.hrefs), owner)
        self.assertIn('References last checked:', text)
        self.assertIn('not locally', text.lower())
        self.assertRegex(text.lower(), r'cross-cutting.{0,120}not runtime')
        for term in ('retention', 'identity', 'region', 'endpoint', 'language'):
            self.assertIn(term, text.lower())
        for source in re.findall(r'id="(source-\d+)"', text):
            self.assertIn('#' + source, doc.hrefs)

if __name__ == '__main__': unittest.main()
