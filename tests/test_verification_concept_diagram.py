"""Contracts for the general verification-engineering figure."""
from pathlib import Path
import unittest
import re
from test_sources import Document, normalise

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/concept.html'

class VerificationConceptDiagramTests(unittest.TestCase):
    def test_static_figure_has_accessible_explanation(self):
        doc = Document(PAGE.read_text())
        figures = [n for n in doc.root.elements('figure') if n.attrs.get('id') == 'fig-verification-concept']
        self.assertEqual(len(figures), 1, 'general verification figure is missing')
        figure = figures[0]
        self.assertEqual(figure.attrs.get('data-diagram'), 'static')
        svg = next(figure.elements('svg'))
        self.assertEqual(svg.attrs.get('role'), 'img')
        ids = {n.attrs.get('id') for n in svg.elements()}
        self.assertIn(svg.attrs.get('aria-labelledby'), ids)
        self.assertIn(svg.attrs.get('aria-describedby'), ids)
        self.assertTrue(list(figure.elements('figcaption')))
        self.assertTrue(list(figure.elements('details')))
        text = normalise(figure.text()).lower()
        for phrase in ('agree the rule', 'independent checks', 'exercise the candidate', 'review evidence', 'correct', 'recheck', 'human', 'not proof'):
            self.assertIn(phrase, text)

    def test_connector_endpoints_follow_the_drawn_nodes(self):
        figure = next(n for n in Document(PAGE.read_text()).root.elements('figure') if n.attrs.get('id') == 'fig-verification-concept')
        nodes = {n.attrs['data-node']: n for n in figure.elements('rect') if 'data-node' in n.attrs}
        edges = {(n.attrs['data-from'], n.attrs['data-to']): n for n in figure.elements('path') if 'data-from' in n.attrs}
        self.assertEqual(set(edges), {('rule', 'checks'), ('checks', 'exercise'), ('exercise', 'review'), ('review', 'correct'), ('correct', 'exercise')})
        def on_boundary(point, node):
            x, y = point
            a = node.attrs
            left, top, width, height = (float(a[k]) for k in ('x', 'y', 'width', 'height'))
            return left <= x <= left + width and top <= y <= top + height and (x in (left, left + width) or y in (top, top + height))
        for (source, target), path in edges.items():
            self.assertEqual(path.attrs.get('marker-end'), 'url(#verification-concept-arrow)')
            coords = re.findall(r'[ML]\s*(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)', path.attrs['d'])
            self.assertGreaterEqual(len(coords), 2)
            start, end = [tuple(map(float, p)) for p in (coords[0], coords[-1])]
            self.assertTrue(on_boundary(start, nodes[source]), (source, target, start))
            self.assertTrue(on_boundary(end, nodes[target]), (source, target, end))
