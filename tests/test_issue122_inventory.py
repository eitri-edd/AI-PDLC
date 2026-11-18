"""Issue 122 source inventory contracts; offline, not a live-source check."""
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'https://kiro.dev/docs/specs/correctness/': ('tech-scan-verification.html', 'source-12'),
    'https://www.anthropic.com/research/formal-verification': ('tech-scan-verification.html', 'source-13'),
    'https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/': ('tech-scan-verification.html', 'source-14'),
    'https://aws.amazon.com/blogs/migration-and-modernization/from-mainframes-to-microservices-specification-driven-mainframe-modernization-with-ai-agents/': ('product-implementation.html', 'source-18'),
}

class Issue122InventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads((ROOT / 'site/reference-checks.json').read_text())

    def test_sources_are_current_inventory_records_with_correct_mappings(self):
        records = self.inventory['references']
        for url, (page, source) in SOURCES.items():
            with self.subTest(url=url):
                matches = [r for r in records if r['url'] == url]
                self.assertEqual(len(matches), 1)
                record = matches[0]
                self.assertEqual(record['files'], [page])
                self.assertEqual(record['hrefs'], [url])
                self.assertEqual(record['source_entries'], [{'file': page, 'id': source}])
                self.assertEqual(record['checked_on'], '2026-11-18')
                self.assertTrue(record['method'])
                self.assertTrue(record['result'])
                self.assertEqual(len(record['claim_reviews']), 1)
                review = record['claim_reviews'][0]
                self.assertEqual(review['file'], page)
                self.assertIn(review['outcome'], {'supported', 'limited'})
                self.assertTrue(review['scope'])
                self.assertTrue(review['limitation'])

    def test_counts_are_derived_from_inventory(self):
        records = self.inventory['references']
        self.assertEqual(self.inventory['current_unique_urls'], len({r['url'] for r in records}))
        self.assertEqual(self.inventory['current_unique_hrefs'], len({h for r in records for h in r['hrefs']}))
        self.assertEqual(self.inventory['counts'], dict(Counter(r['result'] for r in records)))

if __name__ == '__main__':
    unittest.main()
