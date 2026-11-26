"""Rendered-structure regressions for the maturity page and shared mobile header."""
from pathlib import Path
import unittest

from test_sources import Document, Element

DIST = Path(__file__).resolve().parents[1] / 'site' / 'dist'


def direct_elements(node):
    return [child for child in node.children if isinstance(child, Element)]


class MaturityUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = Document((DIST / 'concept-maturity.html').read_text())

    def test_concept_figure_captions_are_headers_before_disclosures(self):
        figures = [n for n in self.doc.root.elements('figure') if n.has_class('concept-figure')]
        self.assertEqual(len(figures), 7)
        for figure in figures:
            with self.subTest(figure=figure.attrs.get('id')):
                first = direct_elements(figure)[0]
                self.assertEqual(first.tag, 'figcaption')

    def test_scrollable_tables_and_l0_diagram_are_keyboard_regions(self):
        for table in self.doc.root.elements('table'):
            if not table.has_class('compact-table'):
                continue
            wrapper = table.parent
            self.assertTrue(wrapper.has_class('table-scroll'))
            self.assertEqual(wrapper.attrs.get('tabindex'), '0')
            self.assertEqual(wrapper.attrs.get('role'), 'region')
            self.assertTrue(wrapper.attrs.get('aria-label', '').strip())
        level0 = next(n for n in self.doc.root.elements('figure') if n.attrs.get('id') == 'fig-level-0')
        scroll = next(n for n in level0.elements('div') if n.has_class('figure-scroll'))
        self.assertEqual(scroll.attrs.get('tabindex'), '0')
        self.assertEqual(scroll.attrs.get('role'), 'region')
        self.assertTrue(scroll.attrs.get('aria-label', '').strip())

    def test_shared_header_has_responsive_labels_and_mobile_nav_default(self):
        for page in DIST.glob('*.html'):
            doc = Document(page.read_text())
            with self.subTest(page=page.name):
                for class_name in ('identity-full', 'identity-short', 'organisation-full', 'organisation-short'):
                    matches = [n for n in doc.root.elements('span') if n.has_class(class_name)]
                    self.assertEqual(len(matches), 1, class_name)
        styles = (DIST / 'styles.css').read_text()
        self.assertIn('@media (max-width: 700px)', styles)
        self.assertIn('.identity-short { display: inline; }', styles)
        self.assertIn('@media (max-width: 420px)', styles)
        self.assertIn('.organisation-short { display: inline; }', styles)
        script = (DIST / 'site.js').read_text()
        self.assertIn("window.matchMedia('(max-width: 1099px)')", script)
        self.assertIn('navigation.open = !singleColumnNavigation.matches;', script)


if __name__ == '__main__':
    unittest.main()
