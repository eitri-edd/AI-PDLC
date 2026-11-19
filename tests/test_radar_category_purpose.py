"""Category definitions stay generic while product evidence remains accessible."""
import os
import re
import unittest
from pathlib import Path

from test_radar_category_clarity import CATEGORIES, PAGE, Radar
from test_sources import Document, normalise, statically_hidden

# Aliases include product names that do not match their full table-row label.
PRODUCT_NAMES = (
    'Amazon Bedrock', 'Claude', 'OpenAI', 'Codex', 'Jev', 'Strands',
    'LiteLLM', 'OpenRouter', 'Portkey', 'Unkey', 'Agent Router',
    'Managed Knowledge Base', 'AgentCore', 'OpenSearch', 'Aurora', 'pgvector', 'Zep',
    'AutoGen', 'AG2', 'LangGraph', 'OpenHands', 'CodeGuru', 'Guardrails',
    'Nitro Sandboxes', 'Nitro Enclaves', 'Lambda MicroVMs', 'E2B', 'Daytona', 'Modal', 'Lizard',
    'Copilot', 'Jules', 'CodeCatalyst', 'Aider', 'Superpowers', 'pstack', 'gstack', 'tstack', 'ub-mode',
    'Devin', 'Kiro', 'dots', 'Grok', 'Cursor', 'Muse', 'Cue', 'OpenClaw', 'Meta', 'Manus', 'Hermes', 'Nous',
    'Gemini', 'GPT', 'GLM', 'DeepSeek', 'Qwen', 'Kimi', 'MiniMax', 'OpenCode', 'Droid',
    'Vertex', 'Fireworks',
)
# Citations originally attached to product notes, not just bibliography entries.
SECTION_SOURCES = {
    'models-access': (25, 24, 69, 71, 72) + tuple(range(112, 133)),
    'gateways': (64, 65, 66, 67, 61, 27, 75, 29, 62, 63, 30),
    'context-memory': (56, 17, 21),
    'harness-frameworks': (18, 34, 70, 73),
    'verification': (14, 15, 16),
    'sandbox': (12, 22, 57, 59, 58, 23, 68),
    'software-factories': (53, 42, 43, 60, 44, 45, 71),
    'skill-packs': (52,),
    'persistent-agents': (92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111),
}


class RadarCategoryPurposeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Optional fixture enables RED against git HEAD without changing the page.
        raw = Path(os.environ.get('RADAR_TEST_PAGE', str(PAGE))).read_text(encoding='utf-8')
        cls.radar = Radar(raw)
        cls.doc = Document(raw)
        cls.sections = {e.attrs['id']: e for e in cls.doc.root.elements('section')
                        if e.attrs.get('id') in CATEGORIES}

    def test_every_category_opens_with_a_generic_definition_before_its_table(self):
        self.assertEqual(set(self.radar.sections), set(CATEGORIES))
        for ident, section in self.radar.sections.items():
            with self.subTest(category=ident):
                self.assertTrue(section['table'])
                self.assertTrue(section['paragraphs'])
                self.assertGreaterEqual(len(section['paragraphs'][0].split()), 10)
                intro = normalise(' '.join(section['paragraphs']))
                # Derive full row names from the actual inventory as well as
                # checking aliases used in the original product notes.
                names: set[str] = set(PRODUCT_NAMES)
                for category in self.sections.values():
                    for th in category.elements('th'):
                        if th.attrs.get('scope') == 'row':
                            label = next((e for e in th.elements('span')
                                          if e.has_class('cell-label')), None)
                            name = normalise(th.text(exclude=label))
                            if name:
                                names.add(name)
                for name in sorted(names):
                    self.assertNotRegex(intro, re.compile(r'(?<!\w)' + re.escape(name) + r'(?!\w)', re.I),
                                        f'{ident} introduction names {name}')

    def test_no_dated_source_citations_in_pre_table_introductions(self):
        for ident, section in self.sections.items():
            with self.subTest(category=ident):
                for node in section.elements():
                    if node.tag == 'table':
                        break
                    if node.tag == 'a':
                        self.assertNotRegex(node.attrs.get('href', ''), r'^#source-\d+$')

    def test_product_note_citations_remain_in_their_sections_after_the_table(self):
        for ident, expected in SECTION_SOURCES.items():
            with self.subTest(category=ident):
                elements = list(self.sections[ident].elements())
                table_index = next(i for i, e in enumerate(elements) if e.tag == 'table')
                refs = {e.attrs.get('href') for e in elements[table_index + 1:] if e.tag == 'a'}
                self.assertTrue({f'#source-{n}' for n in expected} <= refs)
                for n in expected:
                    matching = [e for e in elements[table_index + 1:]
                                if e.tag == 'a' and e.attrs.get('href') == f'#source-{n}']
                    self.assertTrue(any(not statically_hidden(e) for e in matching), f'hidden source {n}')

    def test_critical_access_and_safety_warnings_remain_visible_in_section(self):
        # Locate the smallest matching elements, so a hidden paragraph cannot be
        # masked by visible text in the surrounding section or table.
        checks = {
            'gateways': (r'1\.82\.7.*1\.82\.8.*1\.107\.0.*malicious', r'GHSA-mgwh-j6v5-5mf8', r'FSL-1\.1-ALv2'),
            'context-memory': (r'Zep Community Edition.*(?:retired|deprecated|do not use)',),
            'verification': (r'(?:detect.only|not to block|does not block)', r'closed to new customers'),
            'software-factories': (r'(?:read.only|winds down)', r'new (?:installs|installations).*stop', r'closed to new customers'),
            'skill-packs': (r'ub-mode.*(?:push|main line)',),
        }
        for ident, patterns in checks.items():
            elements = list(self.sections[ident].elements())
            for pattern in patterns:
                with self.subTest(category=ident, warning=pattern):
                    candidates = [e for e in elements if re.search(pattern, normalise(e.text()), re.I)]
                    leaves = [e for e in candidates if not any(c in candidates for c in e.elements())]
                    self.assertTrue(any(not statically_hidden(e) for e in leaves),
                                    f'missing or hidden warning: {pattern}')

    def test_product_specific_boundaries_are_in_the_matching_row(self):
        checks = {
            'Nitro Enclaves': r'not a general-purpose sandbox for untrusted agent code',
            'ub-mode': r'push.*main line',
        }
        for name, pattern in checks.items():
            with self.subTest(product=name):
                headers = [e for e in self.doc.root.elements('th')
                           if e.attrs.get('scope') == 'row'
                           and normalise(e.text()).removeprefix('Product ').strip() == name]
                self.assertEqual(len(headers), 1)
                row = headers[0].parent
                self.assertIsNotNone(row)
                if row is None:
                    self.fail('missing product row')
                self.assertRegex(normalise(row.text()).lower(), pattern)

    def test_all_inherited_source_targets_still_exist_once(self):
        ids = [e.attrs.get('id') for e in self.doc.root.elements()]
        for n in range(1, 76):
            with self.subTest(source=n):
                self.assertEqual(ids.count(f'source-{n}'), 1)


if __name__ == '__main__':
    unittest.main()
