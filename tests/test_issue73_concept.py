import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / 'site/dist/concept.html'


def paragraph_with(text, marker):
    return next((p for p in re.findall(r'<p\b[^>]*>.*?</p>', text, re.S) if marker in p), '')


class SourceList(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_list = False
        self.ordinal = 0
        self.numbers = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'ol' and attrs.get('class') == 'source-list':
            self.in_list = True
        elif self.in_list and tag == 'li':
            value = attrs.get('value')
            self.ordinal = int(value) if value is not None else self.ordinal + 1
            if 'id' in attrs:
                self.numbers[attrs['id']] = self.ordinal

    def handle_endtag(self, tag):
        if tag == 'ol' and self.in_list:
            self.in_list = False


class Issue73ConceptTests(unittest.TestCase):
    def test_instruction_loading_and_enforcement_are_distinct(self):
        html = PAGE.read_text()
        p = paragraph_with(html, 'Instruction files:')
        for phrase in ('AGENTS.md', 'CLAUDE.md', 'Codex', 'Claude Code', 'client', 'permissions', 'outside'):
            self.assertIn(phrase, p)
        self.assertIn('https://x.com/trq212/status/2101009392611278961', html)
        self.assertIn('https://github.com/anthropics/claude-code/issues/6235', html)
        self.assertIn('https://code.claude.com/docs/en/memory', html)
        self.assertIn('https://learn.chatgpt.com/docs/agent-configuration/agents-md', html)


    def test_model_change_rechecks_configuration_and_same_safety_acceptance(self):
        html = PAGE.read_text()
        p = paragraph_with(html, 'When the model changes:')
        for phrase in ('instructions', 'tools', 'same', 'acceptance', 'safety', 'compare'):
            self.assertIn(phrase, p)
        self.assertIn('https://x.com/ericzakariasson/status/2102853511637774551', html)
        self.assertIn('https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices', html)

    def test_new_citations_match_real_list_ordinals_and_accessible_labels(self):
        html = PAGE.read_text()
        sources = SourceList()
        sources.feed(html)
        for source in range(31, 36):
            number = sources.numbers[f'source-{source}']
            self.assertRegex(html, rf'href="#source-{source}" aria-label="Source {number}: [^"]+">\[{number}\]</a>')

    def test_new_source_entries_link_back_to_supported_sections(self):
        html = PAGE.read_text(encoding='utf-8')
        for source, section in ((31, 'context-engineering'), (32, 'context-engineering'),
                                (33, 'context-engineering'), (34, 'models'), (35, 'models')):
            with self.subTest(source=source):
                entry = re.search(rf'<li id="source-{source}">.*?</li>', html, re.S)
                self.assertIsNotNone(entry)
                if entry is not None:
                    self.assertIn(f'href="#{section}"', entry.group())
                self.assertIn(f'id="{section}"', html)

    def test_reproduction_links_to_verified_comment(self):
        html = PAGE.read_text(encoding='utf-8')
        self.assertIn('https://github.com/anthropics/claude-code/issues/6235#issuecomment-5734364232', html)

    def test_existing_source_anchors_and_review_dates_remain(self):
        html = PAGE.read_text()
        for source in range(1, 31):
            self.assertIn(f'id="source-{source}"', html)
        self.assertIn('id="learning-references"', html)
        self.assertIn('References last checked: <time datetime="2026-11-14">', html)
        self.assertIn('Last editorial review: <time datetime="2026-11-06">', html)


if __name__ == '__main__':
    unittest.main()
