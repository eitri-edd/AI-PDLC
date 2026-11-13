from pathlib import Path
from html.parser import HTMLParser
import re
import unittest

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-scan-agents.html'


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.tocs = [], [], []
        self.in_toc = False
        self.depth = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'nav' and attrs.get('aria-label') == 'On this page':
            self.in_toc = True
            self.tocs.append([])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
            if self.in_toc:
                self.tocs[-1].append(attrs.get('href', ''))

    def handle_endtag(self, tag):
        if tag == 'nav' and self.in_toc:
            self.in_toc = False



class TechScanAgentsTests(unittest.TestCase):
    def test_coding_agents_reference_exists_and_is_a_research_draft(self):
        assert PAGE.exists(), 'Coding agents reference is missing'
        text = PAGE.read_text(encoding='utf-8').lower()
        assert 'coding agents' in text
        assert 'draft' in text and 'not locally' in text


    def test_navigation_and_citations_resolve_to_unique_local_targets(self):
        doc = Document(PAGE.read_text(encoding='utf-8'))
        assert len(doc.tocs) == 2
        assert doc.tocs[0] == doc.tocs[1]
        assert 1 <= len(doc.tocs[0]) <= 7
        assert 'do-not-use' in doc.ids and 'gaps' in doc.ids
        assert len(doc.ids) == len(set(doc.ids))
        assert all(href[1:] in doc.ids for href in doc.links if href.startswith('#'))
        for destination in ('tech-scan-harness.html', 'tech-scan-sandbox.html'):
            assert destination in doc.links
            assert (PAGE.parent / destination).exists()


    def test_sources_are_canonical_and_reference_date_is_singular(self):
        text = PAGE.read_text(encoding='utf-8')
        doc = Document(text)
        assert 'https://kiro.dev/docs/models/' in doc.links
        assert len(re.findall('References last checked:', text)) == 1
        assert len(re.findall(r'<section id="sources">', text)) == 1
        source_ids = [x for x in doc.ids if re.fullmatch(r'source-\d+', x)]
        assert source_ids and all('#' + x in doc.links for x in source_ids)


    def test_decision_routes_and_coordination_limits_are_explained(self):
        text = PAGE.read_text(encoding='utf-8').lower()
        for phrase in ('failed required gate', 'retention', 'authorisation', 'fallback',
                       'runtime and mantle', 'exclude auto', 'single', 'handoff',
                       'human reviews', 'no local pilot', 'direct provider',
                       'inference profile', 'bedrock-mantle', 'do not start on retired'):
            assert phrase in text
