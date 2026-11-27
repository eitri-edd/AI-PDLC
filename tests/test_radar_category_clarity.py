"""Reader-facing category introductions and the inventory they precede."""
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import re
import unittest

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-radar.html'
CATEGORIES = {
    'models-access': ('Models and model access', 46),
    'gateways': ('AI gateways and routing', 12),
    'context-memory': ('Context and memory', 9),
    'harness-frameworks': ('Harness and agent frameworks', 15),
    'agentic-development-environments': ('Agentic development environments', 9),
    'persistent-agents': ('Persistent agents', 10),
    'verification': ('Verification', 11),
    'sandbox': ('Sandbox and execution', 11),
    'software-factories': ('Software factories', 15),
    'delivery': ('Delivery', 6),
    'skill-packs': ('AI workflow skill packs', 12),
}

# Snapshot parsed tables separately from the changing introductory prose.
TABLE_DIGESTS = {
    # Moved when the Hermes Agent release date was corrected 23 Nov to
    # 24 Nov 2026 (issue #179, 27 November 2026).
    'persistent-agents': '49ac5b7d08a419da80451f05136a93582daba3ec32212b6db8c76f4a10dd3a6d',
    # Moved when Models and model access split into LLM model, coding tool,
    # provider and decision-model tables (20 November 2026).
    # Moved again when the Antigravity Carbon tier was corrected from
    # Ultra-only to paid Pro, Ultra and Enterprise (issue #179,
    # 27 November 2026).
    'models-access': '4fe945f94a492892c162528f9b0b05410bca2b82d26f6b7551eb5dad08b200f0',
    'gateways': 'ae023c9871d10226b02a8b6d5b3307e9dc2d2166d0c76edfa43996699d836621',
    'context-memory': '549d8b33fd2b8553cb6436cc914908c9c0b9fa221b180f8e186c962958deb4b0',
    # Moved when the Microsoft Agent Framework row gained its pin condition (issue #133).
    'harness-frameworks': '6e2b92014e6ff20e383e9e0a6a620506097ed933347267e7fe3c01de8e58f578',
    # Moved when eight ADE products were added (Orca, T3 Code, Paradev, Paseo,
    # Orchestrator, Traycer, OpenChamber, Kepler) on 25 November 2026.
    'agentic-development-environments': '079037811d1d445cf16168c5a85e2b37c555948e5152b6d1f1c514d831fa29d4',
    'verification': 'bbb5a3775c7e29c1a3d6f8a3c8fd4e5a7967d6ebfb9d2b401a782b756cdf7fa7',
    'sandbox': '13f6de24c96f576a698b8ab4e7f67b242ef63d69a205d6b1531552eac45d915b',
    'software-factories': '551c87eb1a65bd5cbe1533fd33f89c73449d604e98c021a389f7bffeb3968bc7',
    'delivery': '73afae9379cad3c853f314b41a8bf7198f4f52eef2aac1ba3194292a5fff7dad',
    'skill-packs': 'b5883de49331083c50512aa33e9ddd2993033ac15c6b22f00b1cd3781da9f37c',
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
                self.sections[ident] = {'heading': '', 'paragraphs': [], 'table': '', 'rows': 0, 'tables': 0}
        if self.section is None:
            return
        data = self.sections[self.section]
        if tag == 'table':
            self.table_depth += 1
            if self.table_depth == 1:
                data['tables'] += 1
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
                self.assertEqual(section['rows'], count + section['tables'])  # one header per table plus products

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

    def test_persistent_agents_separate_ongoing_ownership_from_access(self):
        self.assert_concepts('persistent-agents', r'\bongoing\b', r'\bmemory\b',
                             r'\b(schedule|event)\b', r'\b(identity|secrets?|access)\b')

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

    def test_delivery_covers_release_operations_and_agent_evidence(self):
        self.assert_concepts('delivery', r'\b(release|rollout)\b', r'\b(incident|monitor)\b',
                             r'\bmetric\w*\b', r'\bagent-produced\b')

    def test_skill_packs_are_reusable_agent_workflows(self):
        self.assert_concepts('skill-packs', r'\b(reusable|repeatable|reuse)\b',
                             r'\b(agent|agents)\b', r'\b(procedure\w*|workflow\w*|instructions|skills)\b')


if __name__ == '__main__':
    unittest.main()
