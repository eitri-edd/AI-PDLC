"""Regression contracts for issue 112's mobile presentation fixes."""
from pathlib import Path
import unittest

from test_sources import Document, Element, normalise

DIST = Path(__file__).resolve().parents[1] / 'site' / 'dist'


def document(name):
    return Document((DIST / name).read_text())


def children(node):
    return [child for child in node.children if isinstance(child, Element)]


class Issue112MobileTests(unittest.TestCase):
    def test_verification_example_header_uses_icon_and_copy_columns(self):
        doc = document('tech-scan-verification.html')
        header = next(node for node in doc.root.elements('div')
                      if node.has_class('learning-example-header'))
        parts = children(header)
        self.assertEqual(len(parts), 2, 'header must have icon and copy as grid children')
        icon, copy = parts
        self.assertEqual(icon.tag, 'svg')
        self.assertTrue(icon.has_class('learning-icon'))
        self.assertEqual(icon.attrs.get('aria-hidden'), 'true')
        self.assertTrue(copy.has_class('learning-header-copy'))
        kind = next(node for node in copy.elements() if node.has_class('learning-kind'))
        title = next(node for node in copy.elements() if node.has_class('learning-title'))
        benefit = next(node for node in copy.elements() if node.has_class('learning-benefit'))
        self.assertEqual(normalise(kind.text()), 'Worked example')
        self.assertEqual(title.tag, 'h3')
        self.assertEqual(normalise(title.text()), 'Interpret a critical failure')
        self.assertIn('aggregate', normalise(benefit.text()))

    def test_target_tables_have_labeled_keyboard_scroll_regions(self):
        targets = (
            ('tech-scan-sandbox.html', 'Boundary'),
            ('tech-scan-workflows-factories.html', 'Stage'),
        )
        for filename, first_column in targets:
            with self.subTest(filename=filename):
                doc = document(filename)
                table = next(table for table in doc.root.elements('table')
                             if normalise(next(table.elements('th')).text()) == first_column)
                wrapper = table.parent
                assert wrapper is not None
                self.assertTrue(wrapper.has_class('table-scroll'),
                                'target table must use the shared scrolling wrapper')
                self.assertEqual(wrapper.attrs.get('tabindex'), '0')
                self.assertEqual(wrapper.attrs.get('role'), 'region')
                self.assertTrue(wrapper.attrs.get('aria-label', '').strip())
        css = (DIST / 'styles.css').read_text()
        self.assertRegex(css, r'(?s)\.table-scroll\s*\{[^}]*overflow-x\s*:\s*auto\s*;')


if __name__ == '__main__':
    unittest.main()
