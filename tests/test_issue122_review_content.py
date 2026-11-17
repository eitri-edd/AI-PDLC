import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'site' / 'dist'


def text(name):
    return (ROOT / name).read_text(encoding='utf-8')


class ReviewContentTests(unittest.TestCase):
    def test_retry_narrative_orders_independent_failure_and_property_evidence(self):
        page = text('product-implementation.html')
        story = page.split('id="example-annual-workflow"', 1)[1].split('<figure', 1)[0]
        milestones = [
            'release candidate A', 'independent check', 'creates a second task',
            'After that failure', 'Product confirms', 'old candidate A fails',
            'deliberately broken', 'candidate B', 'property passes',
            'independent reviewer repeats', 'Separately, the reviewer checks that retries preserve reminder history',
        ]
        for part in milestones:
            self.assertIn(part, story)
        positions = [story.index(part) for part in milestones]
        self.assertEqual(positions, sorted(positions))
        self.assertIn('not proof', story)
        self.assertNotIn('minimal failing case', page)


    def test_quality_report_records_property_results_for_each_candidate(self):
        page = text('product-implementation.html')
        report = page.split('id="implementation-quality-report"', 1)[1].split('</table>', 1)[0]
        self.assertIn('Existing automated checks pass', report)
        self.assertIn('new property check fails on A', report)
        self.assertIn('property check passes on B', report)
        self.assertIn('reminder history', report)

    def test_formal_check_records_counterexample_only_if_found(self):
        page = text('tech-scan-verification.html')
        formal = page.split('id="formal-model-checks"', 1)[1].split('<section id="choices"', 1)[0]
        self.assertIn('If a counterexample is found', formal)
        failed = formal.split('If a counterexample is found', 1)[1].split('</li>', 1)[0]
        for evidence in ('specification', 'assumptions', 'counterexample', 'reproduction', 'corrected test'):
            self.assertIn(evidence, failed)
        self.assertIn('For a successful or inconclusive check', formal)

    def test_formal_checks_distinguish_outcomes_and_cite_scoped_sources(self):
        page = text('tech-scan-verification.html')
        formal = page.split('id="formal-model-checks"', 1)[1].split('<section id="choices"', 1)[0]
        for phrase in ('counterexample', 'bounded', 'inconclusive', 'assumptions', 'implementation'):
            self.assertIn(phrase, formal)
        for number, domain in [('12', 'kiro.dev/docs/specs/correctness/'), ('13', 'anthropic.com/research/formal-verification'), ('14', 'microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/')]:
            self.assertRegex(page, rf'id="source-{number}"[^>]*>.*?{re.escape(domain)}')
            self.assertIn(f'href="#source-{number}"', page)
        self.assertIn('Kiro IDE', page)
        self.assertIn('64 MB', formal)
        self.assertIn('RISC-V', formal)
        self.assertIn('login', formal)
        self.assertIn('trusted', formal)
        product = text('product-implementation.html')
        self.assertRegex(product, r'id="source-18"[^>]*>.*?aws\.amazon\.com/blogs/migration-and-modernization/')
        self.assertIn('href="#source-18"', product)


if __name__ == '__main__':
    unittest.main()
