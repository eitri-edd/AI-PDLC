"""Issue #140: inspect published maturity guidance, including diagram alternatives.

MATURITY_HTML may point at a baseline snapshot for a RED check. Offline only;
semantic heuristics catch concrete regressions but do not replace editorial review.
"""
import os
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

from test_sources import Document, normalise

DIST = Path(__file__).resolve().parents[1] / 'site' / 'dist'
PAGE = Path(os.environ.get('MATURITY_HTML', DIST / 'concept-maturity.html'))
SOURCES = {
    'source-1': 'https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/',
    'source-2': 'https://addyosmani.com/blog/agentic-autonomy-levels/',
    'source-3': 'https://codex.danielvaughan.com/2026/04/21/ai-codebase-maturity-model-codex-cli-five-levels-self-sustaining-systems/',
    'source-4': 'https://knightcolumbia.org/research/levels-of-autonomy-for-ai-agents',
    'source-5': 'https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report',
    'source-6': 'https://arxiv.org/abs/2507.09089',
    'source-7': 'https://martinfowler.com/bliki/MaturityModel.html',
    'source-8': 'https://www.anthropic.com/research/measuring-agent-autonomy',
    'source-9': 'https://www.danshapiro.com/blog/2026/03/dark-factories-rise-of-the-trycycle/',
    'source-10': 'https://dev.to/dominik_ddd/the-oversight-ladder-the-five-levels-of-ai-coding-autonomy-1d94',
    'source-11': 'https://www.augmentcode.com/guides/steve-yegge-8-levels-ai-assisted-development',
    'source-12': 'https://futurumgroup.com/insights/qodo-builds-the-governance-layer-agentic-sdlc-has-been-missing/',
    'source-13': 'https://gametime.co/blog/how-gametime-engineering-hit-level-3-and-why-the-real-work-starts-now/',
}


def by_id(doc, ident):
    return next((n for n in doc.root.elements() if n.attrs.get('id') == ident), None)


def text(node):
    return normalise(node.text()).casefold()


def unsupported_claims(content):
    """Catch unconditional baseline claims in text, SVG descriptions and alternatives."""
    patterns = {
        'false L1 safety': r'risk is wasted effort, not shipped defects',
        'universal holdout threshold': r'(?:only when|needs|requires?|must (?:have|use)|minimum check.{0,60})[^.]{0,100}holdout',
        'universal minute threshold': r'(?:only when|needs|requires?|must|minimum check.{0,60})[^.]{0,100}rollback (?:measured )?in minutes',
        'parallelism is required': r'(?:only climb|climb to l3 when|exit criterion[^.]{0,40})[^.]{0,100}(?:second agent|parallel)',
        'trigger defines L4': r'if [^.]{0,100}starts work from triggers[^.]{0,100}you are at l4',
        'protected check guarantees correctness': r'(?:protected (?:checks?|tests?)|(?:checks?|tests?)[^.]{0,80}cannot edit)[^.]{0,60}(?:guarantees?|proves?) (?:correctness|safety)',
    }
    return [name for name, pattern in patterns.items() if re.search(pattern, content, re.I)]


def level_chunks(ladder):
    """Content between adjacent L0…L5 headings, independent of wrapper classes."""
    groups = {}
    active = None
    for child in ladder.children:
        if not hasattr(child, 'tag'):
            continue
        if child.tag in {'h3', 'h4'}:
            match = re.match(r'\s*l([0-5])\b', text(child))
            if match:
                active = int(match.group(1))
                groups[active] = []
        if active is not None:
            groups[active].append(child)
    return groups


class MaturityIssue140Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = Document(PAGE.read_text(encoding='utf-8'))
        cls.ladder = by_id(cls.doc, 'ladder')
        cls.verification = by_id(cls.doc, 'verification-gate')

    def test_no_unconditional_safety_or_fixed_threshold_claims_in_prose_or_figures(self):
        # Only published article sections: includes SVG text, descriptions and details.
        sections = [n for n in self.doc.root.elements('section') if n.attrs.get('id') != 'sources']
        for section in sections:
            with self.subTest(section=section.attrs.get('id')):
                self.assertEqual(unsupported_claims(text(section)), [])

    def test_claim_detector_rejects_inverted_mutations(self):
        for bad in ('The risk is wasted effort, not shipped defects.',
                    'You only climb when a second agent runs in parallel.',
                    'This requires holdout evaluation.',
                    'This requires rollback in minutes.',
                    'The protected checks guarantee safety.'):
            with self.subTest(bad=bad):
                self.assertTrue(unsupported_claims(bad), bad)
        self.assertFalse(unsupported_claims('Holdout evaluation can be useful. Rollback speed depends on risk.'))

    def test_l1_verification_acknowledges_real_defect_or_security_risk(self):
        rows = [r for r in self.verification.elements('tr') if re.match(r'l1\b', text(r))]
        self.assertEqual(len(rows), 1)
        self.assertRegex(text(rows[0]), r'defect|bug|vulnerabilit|security|harm|incorrect|mistake|error')
        self.assertNotRegex(text(rows[0]), r'not (?:shipped )?(?:defects|bugs|security)')

    def test_fictional_comparison_makes_the_task_and_authority_visible(self):
        section = by_id(self.doc, 'start-here')
        self.assertIsNotNone(section)
        if section is None:
            return
        case = next(text(p) for p in section.elements('p') if 'fictional example' in text(p))
        for concept in ('handover', 'report', 'permission', 'check', 'decision'):
            with self.subTest(concept=concept):
                self.assertIn(concept, case)

    def test_l0_attribution_is_not_a_page_invention(self):
        paragraphs = [text(p) for p in self.ladder.elements('p')]
        shapiro_l0 = [p for p in paragraphs if 'shapiro' in p and re.search(r'\bl0\b', p)]
        self.assertTrue(shapiro_l0, 'Explain Shapiro’s own L0 framing near the attribution')
        self.assertFalse(any(re.search(r'extend(?:ed|s)? (?:with|by).{0,35}\bl0\b', p) for p in shapiro_l0))

    def test_levels_distinguish_human_review_and_release(self):
        rows = {text(list(r.elements('td'))[0]): [text(c) for c in r.elements('td')]
                for r in self.ladder.elements('tr') if list(r.elements('td'))}
        for level in ('l2', 'l3', 'l4', 'l5'):
            self.assertIn(level, rows)
        self.assertRegex(' '.join(rows['l2']), r'diff|review')
        self.assertRegex(' '.join(rows['l3']), r'evidence|review|supervis')
        self.assertRegex(' '.join(rows['l4']), r'approv|decision|plan|goal')
        self.assertRegex(' '.join(rows['l5']), r'releas|ship|deploy')
        self.assertRegex(' '.join(rows['l5']), r'authori[sz]|scope|permi|route')

    def test_verification_is_scoped_and_not_a_guarantee(self):
        body = text(self.verification)
        self.assertRegex(body, r'(?:independen|protect)')
        self.assertRegex(body, r'(?:risk|scope|task|impact)')
        self.assertRegex(body, r'(?:coverage|adequac|quality|blind spot|false negative|limit|not (?:prove|guarantee)|does not (?:prove|guarantee)|cannot (?:prove|guarantee))',
                         'State the limits or adequacy of protected checks, not merely their immutability')

    def test_each_level_has_its_own_radar_role_links(self):
        groups = level_chunks(self.ladder)
        radar = Document((DIST / 'tech-radar.html').read_text(encoding='utf-8'))
        for level in range(6):
            with self.subTest(level=level):
                self.assertIn(level, groups)
                links = [a for node in groups[level] for a in node.elements('a')
                         if urlsplit(a.attrs.get('href', '')).path == 'tech-radar.html']
                self.assertTrue(links, 'Each level needs its own role strip, not a shared navigation link')
                for link in links:
                    target = urlsplit(link.attrs['href']).fragment
                    self.assertTrue(target, 'Radar links must identify real categories')
                    self.assertIsNotNone(by_id(radar, unquote(target)))
                    self.assertTrue(normalise(link.text()) or link.attrs.get('aria-label', '').strip())

    def test_links_are_nonempty_and_local_fragments_resolve(self):
        cache = {'concept-maturity.html': self.doc}
        for a in self.doc.root.elements('a'):
            href = a.attrs.get('href', '').strip()
            with self.subTest(href=href):
                self.assertTrue(href)
                self.assertTrue(normalise(a.text()) or a.attrs.get('aria-label', '').strip())
                parts = urlsplit(href)
                if parts.scheme or parts.netloc:
                    continue
                filename = unquote(parts.path) or 'concept-maturity.html'
                path = DIST / filename
                self.assertTrue(path.is_file(), href)
                if parts.fragment and path.suffix == '.html':
                    if filename not in cache:
                        cache[filename] = Document(path.read_text(encoding='utf-8'))
                    self.assertIsNotNone(by_id(cache[filename], unquote(parts.fragment)), href)

    def test_overview_alternative_explains_every_rung(self):
        figure = by_id(self.doc, 'fig-ladder-overview')
        alt = next(d for d in figure.elements('details') if d.has_class('figure-reading'))
        items = [text(li) for li in alt.elements('li')]
        expectations = [('l0', 'baseline', 'line'), ('l1', 'operator', 'reads'),
                        ('l2', 'collaborator', 'diff'), ('l3', 'consultant', 'evidence'),
                        ('l4', 'approver', 'goal'), ('l5', 'observer', 'outcomes')]
        for expected in expectations:
            self.assertTrue(any(all(word in item for word in expected) for item in items), expected)

    def test_l5_visible_flow_geometry_and_gate(self):
        figure = by_id(self.doc, 'fig-level-5')
        svg = next(figure.elements('svg'))

        def connected(source, target):
            nodes = {n.attrs.get('id'): n for n in svg.elements('rect')}
            def inside(point, node):
                a = node.attrs
                x, y = point
                return (float(a['x']) <= x <= float(a['x']) + float(a['width']) and
                        float(a['y']) <= y <= float(a['y']) + float(a['height']))
            def endpoints(path):
                # Our connectors use absolute M/L/H/V commands; inspect geometry,
                # not edge metadata. Reject unsupported syntax rather than guess.
                tokens = re.findall(r'[A-Za-z]|-?\d+(?:\.\d+)?', path.attrs.get('d', ''))
                if not tokens or tokens[0] != 'M':
                    return None
                try:
                    x, y = float(tokens[1]), float(tokens[2])
                    start = (x, y)
                    i = 3
                    while i < len(tokens):
                        cmd = tokens[i]; i += 1
                        if cmd == 'H':
                            x = float(tokens[i]); i += 1
                        elif cmd == 'V':
                            y = float(tokens[i]); i += 1
                        elif cmd == 'L':
                            x, y = float(tokens[i]), float(tokens[i+1]); i += 2
                        else:
                            return None
                    return start, (x, y)
                except (ValueError, IndexError):
                    return None
            if source not in nodes or target not in nodes:
                return []
            return [p for p in svg.elements('path') if p.attrs.get('marker-end') and
                    (points := endpoints(p)) and inside(points[0], nodes[source]) and
                    inside(points[1], nodes[target])]

        for source, target in [('l5-task', 'l5-automation'),
                               ('l5-automation', 'l5-check'),
                               ('l5-check', 'l5-release'),
                               ('l5-check', 'l5-stop')]:
            self.assertTrue(connected(source, target), f'Missing directed {source} → {target} geometry')
        release = by_id(self.doc, 'l5-release')
        self.assertIn('d-node', release.attrs.get('class', ''))
        svg_text = text(svg)
        for term in ('release', 'pass', 'policy', 'fail', 'stop', 'monitor'):
            self.assertIn(term, svg_text)
        alternative = text(next(d for d in figure.elements('details') if d.has_class('figure-reading')))
        for term in ('pass', 'policy', 'fail', 'stop', 'release', 'cannot undo'):
            self.assertIn(term, alternative)
        # Swap actual path geometry while preserving all labels/metadata.
        gate = by_id(self.doc, 'l5-pass-arrow')
        failure = by_id(self.doc, 'l5-fail-arrow')
        self.assertIn(gate, connected('l5-check', 'l5-release'))
        self.assertIn(failure, connected('l5-check', 'l5-stop'))
        gate.attrs['d'], failure.attrs['d'] = failure.attrs['d'], gate.attrs['d']
        try:
            self.assertNotIn(gate, connected('l5-check', 'l5-release'))
            self.assertNotIn(failure, connected('l5-check', 'l5-stop'))
        finally:
            gate.attrs['d'], failure.attrs['d'] = failure.attrs['d'], gate.attrs['d']

    def test_each_figure_has_local_native_arrowheads(self):
        ids = [n.attrs['id'] for n in self.doc.root.elements() if 'id' in n.attrs]
        self.assertEqual(len(ids), len(set(ids)), 'IDs must be unique')
        for ident in ['fig-ladder-overview'] + [f'fig-level-{i}' for i in range(6)]:
            with self.subTest(figure=ident):
                figure = by_id(self.doc, ident)
                svg = next(figure.elements('svg'))
                markers = {n.attrs.get('id'): n for n in svg.elements('marker')}
                paths = [n for n in svg.elements('path') if n.attrs.get('marker-end')]
                self.assertTrue(paths)
                for path in paths:
                    match = re.fullmatch(r'url\(#([^)]*)\)', path.attrs['marker-end'])
                    self.assertIsNotNone(match)
                    self.assertNotEqual(match.group(1), 'arrow')
                    self.assertIn(match.group(1), markers)
                    self.assertTrue(list(markers[match.group(1)].elements('path')))

    def test_original_source_records_and_diagram_accessibility_survive(self):
        for ident, href in SOURCES.items():
            with self.subTest(source=ident):
                node = by_id(self.doc, ident)
                self.assertIsNotNone(node)
                self.assertIn(href, [a.attrs.get('href') for a in node.elements('a')])
        for ident in ['fig-ladder-overview'] + [f'fig-level-{i}' for i in range(6)]:
            with self.subTest(figure=ident):
                figure = by_id(self.doc, ident)
                self.assertIsNotNone(figure)
                self.assertEqual(figure.tag, 'figure')
                self.assertTrue(list(figure.elements('figcaption')))
                self.assertTrue(list(figure.elements('details')), 'Keep a text alternative')
                self.assertTrue(list(figure.elements('desc')), 'Keep the SVG accessible description')


if __name__ == '__main__':
    unittest.main()
