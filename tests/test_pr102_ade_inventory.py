"""Offline contracts for PR 102's targeted ADE source follow-up."""
import copy
import hashlib
import json
from pathlib import Path
import unittest
from urllib.parse import urldefrag, urlsplit
from test_sources import Document

ROOT = Path(__file__).resolve().parents[1]

class ADEInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads((ROOT / 'site/reference-checks.json').read_text())
        cls.by_url = {r['url']: r for r in cls.inventory['references']}

    def test_targeted_page_source_reviews_are_recorded(self):
        required = {
            ('concept.html', 'https://git-scm.com/docs/git-worktree'),
            ('concept.html', 'https://code.claude.com/docs/en/sandboxing'),
            ('tech-scan-agents.html', 'https://code.claude.com/docs/en/worktrees'),
            ('tech-scan-agents.html', 'https://code.claude.com/docs/en/sandboxing'),
        }
        reviews = self.inventory.get('pr102_targeted_followup', {}).get('reviews', [])
        self.assertEqual({(r['file'], r['url']) for r in reviews}, required)
        captures = {
            'https://git-scm.com/docs/git-worktree': ('https://git-scm.com/docs/git-worktree', 'a9c89ae3bf0f6ee142347a5b7b3eba46b1f0e9291c18a721c52b90e4fcc52f97'),
            'https://code.claude.com/docs/en/worktrees': ('https://code.claude.com/docs/en/worktrees.md', '66f5501dc74194bc0b5db1a4df1806394f66da5d473fa79cb2638379d74c9922'),
            'https://code.claude.com/docs/en/sandboxing': ('https://code.claude.com/docs/en/sandboxing.md', '2df1b27e787a5c7919c328a565ee08e5cb34a706d0b89e1390f70c39a915e447'),
        }
        for review in reviews:
            with self.subTest(review=review['url'], page=review['file']):
                self.assertEqual((review['capture_url'], review['capture_sha256']), captures[review['url']])
                self.assertTrue(review['evidence_excerpts'])
                self.assertTrue(review['limitation'])
                self.assertIn(review['file'], self.by_url[review['url']]['files'])
                self.assertIn(review['file'], {r['file'] for r in self.by_url[review['url']]['claim_reviews']})

    def test_current_href_census_and_target_source_entries(self):
        expected = {}
        for path in (ROOT / 'site/dist').rglob('*.html'):
            page = path.relative_to(ROOT / 'site/dist').as_posix()
            doc = Document(path.read_text())
            for node in doc.root.elements():
                for attribute in ('href', 'src'):
                    url = node.attrs.get(attribute, '')
                    if urlsplit(url).scheme in ('http', 'https'):
                        expected.setdefault(urldefrag(url)[0], set()).add(url)
        self.assertEqual(set(expected), set(self.by_url))
        self.assertEqual(self.inventory['current_unique_urls'], len(expected))
        self.assertEqual(self.inventory['current_unique_hrefs'], len(set().union(*expected.values())))
        for url, hrefs in expected.items():
            self.assertEqual(set(self.by_url[url]['hrefs']), hrefs, url)
        for url, page, source in [
            ('https://git-scm.com/docs/git-worktree', 'concept.html', 'source-46'),
            ('https://code.claude.com/docs/en/sandboxing', 'concept.html', 'source-47'),
            ('https://code.claude.com/docs/en/worktrees', 'tech-scan-agents.html', 'source-35'),
            ('https://code.claude.com/docs/en/sandboxing', 'tech-scan-agents.html', 'source-36'),
        ]:
            self.assertIn({'file': page, 'id': source}, self.by_url[url]['source_entries'])
            doc = Document((ROOT / 'site/dist' / page).read_text())
            entries = [n for n in doc.root.elements('li') if n.attrs.get('id') == source]
            self.assertEqual(len(entries), 1)
            self.assertIn(url, [n.attrs.get('href') for n in entries[0].elements('a')])

    def test_inherited_reviews_history_and_page_passes_preserved(self):
        new_urls = {'https://git-scm.com/docs/git-worktree', 'https://code.claude.com/docs/en/worktrees',
                    'https://orca.dev/docs/agents/supported',
                    'https://code.claude.com/docs/en/agent-view',
                    'https://www.conductor.build/announcement',
                    'https://www.conductor.build/changelog/0.93.0-conductor-is-joining-meta',
                    'https://www.conductor.build/changelog/0.94.2-conductor-is-back',
                    'https://platform.claude.com/docs/en/managed-agents/dreams',
                    'https://claude.com/resources/articles/new-in-claude-managed-agents',
                    'https://techcrunch.com/2026/11/04/meta-acquires-ai-coding-startup-conductor/'}
        # Later pages add their own pass, source and shared-link reviews; exclude
        # only those additions so inherited records stay pinned.
        later_pages = {'tech-scan-ai-workflows.html', 'tech-radar.html'}
        # URLs that exist only for the AI workflows page are part of that page's
        # source pass, not the inherited inventory this digest pins.
        new_urls |= {r['url'] for r in self.inventory['references'] if set(r['files']) <= later_pages}
        new_urls |= {'https://github.com/eitri-edd/AI-PDLC/issues/60'}
        # Issue 122 adds only these four records; inherited records remain pinned.
        new_urls |= {
            'https://kiro.dev/docs/specs/correctness/',
            'https://www.anthropic.com/research/formal-verification',
            'https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/',
            'https://aws.amazon.com/blogs/migration-and-modernization/from-mainframes-to-microservices-specification-driven-mainframe-modernization-with-ai-agents/',
        }
        # PR 125 review: the OpenRouter completion release is cited from the
        # gateway page as well as the radar. Exclude it so the inherited digest
        # stays pinned to records that predate this pass.
        new_urls |= {
            'https://prtimes.jp/main/html/rd/p/000000142.000077879.html',
        }
        baseline = {'page_passes': {k: v for k, v in self.inventory['page_passes'].items() if k not in later_pages},
                    'history': self.inventory['history'],
                    'reviews': {r['url']: [v for v in r['claim_reviews']
                                           if v.get('followup') != 'pr102' and v.get('file') not in later_pages]
                                for r in self.inventory['references'] if r['url'] not in new_urls}}
        baseline['reviews']['https://orca.dev/docs/model/worktrees'] = [v for v in baseline['reviews']['https://orca.dev/docs/model/worktrees'] if v.get('followup') != 'ade-tech-scan']
        digest = hashlib.sha256(json.dumps(baseline, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        # Digests advanced by the daily reference check on 17 November 2026,
        # which legitimately advances page_passes dates and per-entry
        # checked_on/http_status/final_url/method. History, claim_reviews,
        # source_entries and evidence_digests are unchanged by that pass.
        self.assertEqual(digest, 'e9fe8787cb9e4d5897dbbbf1a497775b8e1c5218e5cc993a3845d200183b35c1')
        # Compare inherited retrieval metadata and source mappings to a digest
        # of the PR's original inventory. New page mappings are excluded only
        # from the one inherited URL to which this follow-up adds entries.
        fields = ('checked_on', 'result', 'http_status', 'final_url', 'method', 'source_entries', 'evidence_digests')
        metadata = {r['url']: {k: copy.deepcopy(r[k]) for k in fields if k in r}
                    for r in self.inventory['references'] if r['url'] not in new_urls}
        for entry in metadata.values():
            if 'source_entries' in entry:
                entry['source_entries'] = [e for e in entry['source_entries'] if e.get('file') != 'tech-radar.html']
        sandbox = metadata['https://code.claude.com/docs/en/sandboxing']
        for entry in ({'file': 'concept.html', 'id': 'source-47'},
                      {'file': 'tech-scan-agents.html', 'id': 'source-36'}):
            sandbox['source_entries'].remove(entry)
        metadata['https://orca.dev/docs/model/worktrees']['source_entries'].remove(
            {'file': 'tech-scan-agents.html', 'id': 'source-37'})
        actual = hashlib.sha256(json.dumps(metadata, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        self.assertEqual(actual, '34da0fff590e9c1b46e3aa133bd5530b9e80f512bf2586df8d0a4e25b6eb1740')

    def test_misidentified_issue101_review_scopes_match_source_entries(self):
        for url, source_id in [('https://x.com/aparnadhinak/status/2109040646627721384', 'source-41'), ('https://claude.com/resources/articles/auto-mode-default-in-claude-code', 'source-42')]:
            record = self.by_url[url]
            self.assertIn({'file': 'concept.html', 'id': source_id}, record['source_entries'])
            self.assertIn('('+source_id+')', record['claim_reviews'][0]['scope'])

class ADEInventoryMutationTests(ADEInventoryTests):
    def mutated_validator(self, method):
        case = ADEInventoryTests(method)
        case.inventory = copy.deepcopy(self.inventory)
        case.by_url = {r['url']: r for r in case.inventory['references']}
        return case

    def test_rejects_wrong_unique_url_census(self):
        case = self.mutated_validator('test_current_href_census_and_target_source_entries')
        case.inventory['current_unique_urls'] += 1
        with self.assertRaises(AssertionError):
            case.test_current_href_census_and_target_source_entries()

    def test_rejects_fake_capture_digest(self):
        case = self.mutated_validator('test_targeted_page_source_reviews_are_recorded')
        case.inventory['pr102_targeted_followup']['reviews'][0]['capture_sha256'] = '0' * 64
        with self.assertRaises(AssertionError):
            case.test_targeted_page_source_reviews_are_recorded()

    def test_rejects_removed_inherited_source_entries(self):
        case = self.mutated_validator('test_inherited_reviews_history_and_page_passes_preserved')
        record = next(r for r in case.inventory['references'] if r.get('source_entries'))
        del record['source_entries']
        with self.assertRaises(AssertionError):
            case.test_inherited_reviews_history_and_page_passes_preserved()

if __name__ == '__main__':
    unittest.main()
