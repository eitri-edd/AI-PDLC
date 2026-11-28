"""Targeted DORA source provenance for the maturity page."""
import json
from pathlib import Path
import re
import unittest
from test_sources import Document, Element, normalise, statically_hidden

ROOT = Path(__file__).resolve().parents[1]
PAGE = 'concept-maturity.html'
MODEL = 'https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model'
ANNOUNCEMENT = 'https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report'

class MaturityDoraInventoryTests(unittest.TestCase):
    def assert_visible_capabilities(self, raw):
        doc = Document(raw)
        section = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'delivery-system')
        def visible_text(node):
            if statically_hidden(node):
                return ''
            return ' '.join(visible_text(child) if isinstance(child, Element) else child
                            for child in node.children)

        text = normalise(' '.join(visible_text(n) for n in section.elements('p')))
        match = re.search(r'DORA names seven capabilities that magnify AI.s benefits: (.*?)\[5\]', text)
        self.assertIsNotNone(match, 'Visible DORA capability list missing')
        assert match is not None
        names = match.group(1).strip().split(', ')
        names[-1:] = names[-1].split(' and ')
        self.assertEqual(names, ['a clear and communicated AI stance', 'healthy data ecosystems',
                                 'AI-accessible internal data', 'user-centric focus',
                                 'strong version control', 'small batches', 'quality internal platforms'])

    def test_visible_capability_list_rejects_platform_engineering_substitution(self):
        raw = (ROOT / 'site/dist' / PAGE).read_text()
        self.assert_visible_capabilities(raw)
        prose_marker = "DORA names seven capabilities that magnify AI's benefits: a clear and communicated AI stance, healthy data ecosystems, AI-accessible internal data, user-centric focus"
        mutated = raw.replace(prose_marker, prose_marker.replace('user-centric focus', 'platform engineering'), 1)
        self.assertNotEqual(mutated, raw)
        with self.assertRaises(AssertionError):
            self.assert_visible_capabilities(mutated)

    def test_followup_correctly_describes_announcement_and_prior_page(self):
        inventory = json.loads((ROOT / 'site/reference-checks.json').read_text())
        announcement = next(r for r in inventory['references'] if r['url'] == ANNOUNCEMENT)
        followup = next(r for r in announcement['claim_reviews'] if r.get('followup') == 'maturity-dora-capabilities')
        self.assertIn('announcement visual names all seven', followup['evidence_summary'])
        self.assertIn('page previously listed the seven incorrectly', followup['evidence_summary'])
        self.assertIn('corroborates', followup['evidence_summary'])
        self.assertIn('targeted', inventory['page_passes'][PAGE]['scope'])
        self.assertIn('14 destinations', inventory['page_passes'][PAGE]['scope'])

    def test_capability_model_citation_and_targeted_provenance(self):
        inventory = json.loads((ROOT / 'site/reference-checks.json').read_text())
        references = {r['url']: r for r in inventory['references']}
        model = references[MODEL]
        self.assertIn(PAGE, model['files'])
        self.assertIn({'file': PAGE, 'id': 'source-5'}, model['source_entries'])
        reviews = [r for r in model['claim_reviews'] if r.get('file') == PAGE]
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['checked_on'], '2026-11-20')
        self.assertEqual(reviews[0]['outcome'], 'supported')
        self.assertIn('seven', reviews[0]['scope'])
        self.assertTrue(reviews[0]['limitation'])
        announcement = references[ANNOUNCEMENT]
        self.assertTrue(any('seven capabilities' in r['scope'] for r in announcement['claim_reviews']))
        correction = [r for r in announcement['claim_reviews'] if r.get('followup') == 'maturity-dora-capabilities']
        self.assertEqual(len(correction), 1)
        self.assertEqual(correction[0]['checked_on'], '2026-11-20')
        self.assertIn(MODEL, correction[0]['evidence_summary'])
        self.assertIn({'file': 'transformation.html', 'id': 'source-8'}, model['source_entries'])
        self.assertTrue(any(r['file'] == 'transformation.html' for r in model['claim_reviews']))
        page_pass = inventory['page_passes'][PAGE]
        self.assertEqual((page_pass['checked_on'], page_pass['source_entries'], page_pass['unique_fetch_destinations']), ('2026-11-28', 13, 14))
        doc = Document((ROOT / 'site/dist' / PAGE).read_text())
        source = next(n for n in doc.root.elements('li') if n.attrs.get('id') == 'source-5')
        links = {a.attrs.get('href') for a in source.elements('a')}
        self.assertTrue({MODEL, ANNOUNCEMENT, '#delivery-system'} <= links)
        delivery = next(n for n in doc.root.elements('section') if n.attrs.get('id') == 'delivery-system')
        self.assertGreaterEqual(sum(a.attrs.get('href') == '#source-5' for a in delivery.elements('a')), 2)

if __name__ == '__main__':
    unittest.main()
