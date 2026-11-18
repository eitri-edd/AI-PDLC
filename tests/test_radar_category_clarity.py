"""Reader-facing category introductions and the inventory they precede."""
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import re
import unittest

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-radar.html'
CATEGORIES = {
    'models-access': ('Models and model access', 6),
    'gateways': ('AI gateways and routing', 6),
    'context-memory': ('Context and memory', 5),
    'harness-frameworks': ('Harness and agent frameworks', 9),
    'agentic-development-environments': ('Agentic development environments', 1),
    'verification': ('Verification', 3),
    'sandbox': ('Sandbox and execution', 4),
    'software-factories': ('Software factories', 10),
    'skill-packs': ('AI workflow skill packs', 7),
}

# Snapshot parsed tables separately from the changing introductory prose.
TABLE_DIGESTS = {
    'models-access': 'dbe407f53646276972a244a664bcb7de8a11993deaf9553684b78f06f2bc935e',
    'gateways': '7740fe80eae4b75b8bba48729dde5dc2f7778fa8cd196e515736eb687d4271e4',
    'context-memory': 'eb84382835a2273eafb1eeabf9705d19a391b73a4f8af9b2e007fcfefc9863b6',
    'harness-frameworks': '34e1d8f3460b17af03c30c0c57ae7fe6afc1ce4dacdd79994caf7a11ce28a40b',
    'agentic-development-environments': 'df0f89c2d5b981e7093b1e9e04c37bd61541a92bea117f1c13a157a65afd3a97',
    'verification': '2ca114ac9fc6e2d17417b911c5474ea46d42bc506ead8c199c5b4ad21abad2b0',
    'sandbox': '41bb3b17fdc4f386b32d676a8a048b25980bfd652ea0bd09e3991906b07855d5',
    'software-factories': 'ac9e4fed18a557c6e6d5b502bb76501b095dd65355120ed158df9f489438ac73',
    'skill-packs': '20852c303149043ba29db05ed8ffa554e9c4622c4a8ee06f7a6c946ebb5cb28b',
}


class Radar(HTMLParser):
    """Collect each section's heading, pre-table paragraphs and table markup."""
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.sections = {}
        self.section = None
        self.element = None
        self.table_depth = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        if tag == 'section':
            ident = dict(attrs).get('id')
            if ident in CATEGORIES:
                if ident in self.sections:
                    raise ValueError('duplicate category: ' + ident)
                self.section = ident
                self.sections[ident] = {'heading': '', 'paragraphs': [], 'table': '', 'rows': 0}
        if self.section is None:
            return
        data = self.sections[self.section]
        if tag == 'table':
            self.table_depth += 1
        if self.table_depth:
            data['table'] += self.get_starttag_text()
            if tag == 'tr':
                data['rows'] += 1
        elif tag == 'h2':
            self.element = 'heading'
        elif tag == 'p' and not data['table']:
            self.element = 'paragraphs'
            data['paragraphs'].append('')

    def handle_endtag(self, tag):
        if self.section is None:
            return
        if self.table_depth:
            self.sections[self.section]['table'] += f'</{tag}>'
            if tag == 'table':
                self.table_depth -= 1
        elif tag in ('h2', 'p'):
            self.element = None
        if tag == 'section':
            self.section = None
            self.element = None

    def handle_data(self, data):
        if self.section is None:
            return
        section = self.sections[self.section]
        if self.table_depth:
            section['table'] += data
        elif self.element == 'heading':
            section['heading'] += data
        elif self.element == 'paragraphs':
            section['paragraphs'][-1] += data


def prose(section):
    return ' '.join(section['paragraphs']).lower()


class RadarCategoryClarityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = Radar(PAGE.read_text(encoding='utf-8'))

    def assert_concepts(self, ident, *patterns):
        text = prose(self.doc.sections[ident])
        for pattern in patterns:
            with self.subTest(category=ident, concept=pattern):
                self.assertRegex(text, pattern)

    def test_category_headings_and_introductions_precede_tables(self):
        self.assertEqual(set(self.doc.sections), set(CATEGORIES))
        for ident, (heading, count) in CATEGORIES.items():
            with self.subTest(category=ident):
                section = self.doc.sections[ident]
                self.assertEqual(section['heading'].strip(), heading)
                self.assertTrue(section['paragraphs'], 'missing introductory prose')
                self.assertGreaterEqual(len(section['paragraphs'][0].split()), 10)
                self.assertTrue(section['table'])
                self.assertEqual(section['rows'], count + 1)  # header plus products

    def test_introductions_are_concise_and_avoid_prescribing_a_product_choice(self):
        for ident, section in self.doc.sections.items():
            with self.subTest(category=ident):
                text = prose(section)
                self.assertLessEqual(len(text.split()), 60, 'avoid an overly long category introduction')
                self.assertNotRegex(text, r'\bconsider (?:a|an|the|using)\b',
                                    'describe the category rather than prescribe a choice')

    def test_product_tables_are_preserved(self):
        for ident, expected in TABLE_DIGESTS.items():
            with self.subTest(category=ident):
                actual = hashlib.sha256(self.doc.sections[ident]['table'].encode()).hexdigest()
                self.assertEqual(actual, expected, 'product rows or table markup changed')

    def test_models_access_distinguishes_service_clients_and_decision_models(self):
        self.assert_concepts('models-access', r'\b(service|platform|provider)\b',
                             r'\b(client|clients|agent|agents)\b',
                             r'\b(decision|probabilit\w*)\b')

    def test_gateways_describe_optional_routing_features(self):
        text = prose(self.doc.sections['gateways'])
        self.assertRegex(text, r'\b(gateway|router)\b')
        self.assertRegex(text, r'\b(rout\w*|endpoint|api)\b')
        # Qualify capabilities rather than assigning every feature to every product.
        definition = ' '.join(re.split(r'(?<=[.!?])\s+', text)[:2])
        self.assertRegex(definition, r'\b(some|may|can|might|depending|vary|varies|optional)\b')

    def test_context_explains_retrieval_and_memory(self):
        self.assert_concepts('context-memory', r'\b(retriev\w*|search)\b',
                             r'\b(memory|memories)\b')

    def test_harness_explains_model_tool_loop(self):
        self.assert_concepts('harness-frameworks', r'\b(loop|orchestrat\w*)\b',
                             r'\bmodel\b', r'\btools?\b')

    def test_development_environment_distinguishes_worktrees_from_sandboxes(self):
        self.assert_concepts('agentic-development-environments',
                             r'\b(parallel|several|multiple)\b',
                             r'\b(workspace\w*|worktree\w*)\b',
                             r'\b(person|human|review\w*|steer\w*)\b')
        text = prose(self.doc.sections['agentic-development-environments'])
        self.assertRegex(text, r'worktree[^.]*\b(not|isn.t|does not)\b[^.]*sandbox')
        self.assertNotIn('a coding client running several worktree sessions is not the same thing', text)
        self.assertRegex(text, r'\b(client|coding agent)\b[^.]*\b(may|can|some)\b')

    def test_verification_distinguishes_evaluation_from_code_checks(self):
        self.assert_concepts('verification', r'\b(check\w*|verif\w*|evaluat\w*)\b',
                             r'\b(code|software)\b', r'\b(agent|model|ai)\b')
        text = prose(self.doc.sections['verification'])
        self.assertRegex(text, r'for agent-produced work, use checks independent of (its author|the producing agent)')

    def test_sandbox_does_not_equate_isolation_with_access_controls(self):
        self.assert_concepts('sandbox', r'\b(isolat\w*|bound\w*)\b',
                             r'\b(code|execution|workload)\b')
        text = prose(self.doc.sections['sandbox'])
        self.assertRegex(text, r'\b(not|separate|additional|independent)\b[^.]*\b(credentials|identity|network|egress|access)\b')

    def test_software_factory_includes_more_than_cloud_agents(self):
        self.assert_concepts('software-factories', r'\b(code|software|work|development)\b',
                             r'\b(review|pull request|workflow)\b')
        text = prose(self.doc.sections['software-factories'])
        self.assertRegex(text, r'\b(local|terminal|cli|orchestrat\w*|platform)\b[^.]*\b(agent|tool|client|work|task|platform|run\w*)\b|\b(agent|tool|client|work|task|platform|run\w*)\b[^.]*\b(local|terminal|cli|orchestrat\w*|platform)\b')

    def test_skill_packs_are_reusable_agent_workflows(self):
        self.assert_concepts('skill-packs', r'\b(reusable|repeatable|reuse)\b',
                             r'\b(agent|agents)\b', r'\b(procedure\w*|workflow\w*|instructions|skills)\b')


if __name__ == '__main__':
    unittest.main()
