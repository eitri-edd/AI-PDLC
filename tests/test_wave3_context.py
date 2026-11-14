"""Offline contracts for the Context reference, not live service tests."""
from pathlib import Path
import unittest

from test_sources import Document, normalise

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-scan-context.html'


class ContextReferenceTests(unittest.TestCase):
    def test_context_page_exists(self):
        self.assertTrue(PAGE.is_file(), 'Context reference page is missing')

    def test_read_boundary_links_existing_write_guidance(self):
        doc = Document(PAGE.read_text())
        memory = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'memory')
        self.assertIn('validating a write does not prove', normalise(memory.text()))
        self.assertTrue(any(a.attrs.get('href') == 'concept.html#context-engineering'
                            for a in memory.elements('a')))

    def test_pilot_checks_private_and_authorised_shared_content(self):
        doc = Document(PAGE.read_text())
        pilot = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'pilot')
        prose = normalise(pilot.text())
        for expected in ('user A', 'user B', 'broader namespace paths', 'Confirm A can retrieve it',
                         'shared artefact may itself be returned', 'If an isolation test fails'):
            self.assertIn(expected, prose)

    def test_sources_backlink_to_citing_sections(self):
        doc = Document(PAGE.read_text())
        sections = {n.attrs['id']: n for n in doc.root.elements('section') if 'id' in n.attrs}
        for name in ('choices', 'memory', 'construction'):
            for a in sections[name].elements('a'):
                href = a.attrs.get('href', '')
                if href.startswith('#source-'):
                    entry = next(n for n in sections['sources'].elements('li') if '#' + n.attrs.get('id', '') == href)
                    self.assertTrue(any(x.attrs.get('href') == '#' + name for x in entry.elements('a')), (name, href))

    def test_kendra_closure_and_managed_kb_defaults(self):
        doc = Document(PAGE.read_text())
        choices = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'choices')
        prose = normalise(choices.text())
        for expected in ('Maintenance Mode effective 30 June 2026', 'closed it to new customers on 30 July 2026',
                         'Bedrock Managed Knowledge Base', 'five results by default',
                         'semantic chunking is not supported for managed knowledge bases',
                         'cannot be changed afterwards', 'RetrieveAndGenerate'):
            self.assertIn(expected, prose)

    def test_vector_store_table_chooses_by_workload_shape(self):
        doc = Document(PAGE.read_text())
        choices = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'choices')
        prose = normalise(choices.text())
        for expected in ('OpenSearch Serverless', 'Amazon S3 Vectors', 'Aurora PostgreSQL with pgvector',
                         'DynamoDB vector search', '16,000 dimensions; hybrid search supported',
                         'not a Knowledge Bases backend', 'pgvector 0.8.2 on Aurora PostgreSQL 18.6',
                         'cosine or Euclidean only'):
            self.assertIn(expected, prose)

    def test_do_not_use_and_gaps_sections(self):
        doc = Document(PAGE.read_text())
        sections = {n.attrs['id']: n for n in doc.root.elements('section') if 'id' in n.attrs}
        self.assertIn('do-not-use', sections)
        self.assertIn('gaps', sections)
        do_not_use = normalise(sections['do-not-use'].text())
        for expected in ('Amazon Kendra', 'Bedrock Agents Classic', 'Zep Community Edition',
                         'actor-less', 'unvetted MCP server', 'prompt instruction as a memory boundary'):
            self.assertIn(expected, do_not_use)
        gaps = normalise(sections['gaps'].text())
        for expected in ('No AWS service enforces retrieval freshness', 'No AWS-native cross-store retrieval',
                         '17 June 2026', 'Chroma Cloud wind-down dates', 'NextGen collections',
                         'GraphRAG', 'RetrieveAndGenerate'):
            self.assertIn(expected, gaps)

    def test_navigation_is_compact_and_links_neighbour_pages(self):
        doc = Document(PAGE.read_text())
        contents = [n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'On this page']
        self.assertEqual(len(contents), 2)
        for nav in contents:
            # Five entries, following the Workflows/Agents precedent:
            # do-not-use and gaps live in the body, not in this nav.
            self.assertLessEqual(len(list(nav.elements('a'))), 5)
            self.assertEqual([a.attrs.get('href') for a in nav.elements('a')],
                             ['#choices', '#memory', '#construction', '#pilot', '#sources'])
        links = {a.attrs.get('href') for a in doc.root.elements('a')}
        for link in ('tech-scan-verification.html', 'tech-scan-harness.html', 'tech-scan-gateway.html', 'eds-team-context.html'):
            self.assertIn(link, links)
