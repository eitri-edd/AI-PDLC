import re
import unittest
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'site/dist/tech-scan-delivery.html'


class DeliveryPageTest(unittest.TestCase):
    def test_delivery_reference_present_with_release_boundary(self):
        self.assertTrue(PAGE.exists(), 'Delivery reference must exist')
        text = PAGE.read_text(encoding='utf-8').lower()
        for phrase in ('verification', 'merge', 'deploy', 'human', 'rollback', 'digest'):
            self.assertIn(phrase, text)
        for link in ('tech-scan-verification.html', 'tech-scan-workflows-factories.html', 'eds-path-to-production.html'):
            self.assertIn('href="' + link + '"', text)

    def test_navigation_and_source_backlinks_are_consistent(self):
        text = PAGE.read_text(encoding='utf-8')
        ids = re.findall(r'\bid="([^"]+)"', text)
        self.assertEqual(len(ids), len(set(ids)), 'IDs must be unique')
        navs = re.findall(r'<nav aria-label="On this page">(.*?)</nav>', text, re.S)
        self.assertEqual(len(navs), 2)
        for nav in navs:
            links = re.findall(r'href="#([^"]+)"', nav)
            self.assertTrue(links)
            self.assertLessEqual(len(links), 5)
            self.assertTrue(set(links) <= set(ids))
        source_section = text.split('<section id="sources">', 1)[1].split('</section>', 1)[0]
        sources = re.findall(r'<li id="source-(\d+)">(.*?)</li>', source_section, re.S)
        self.assertEqual(len(sources), 14)
        for expected, (number, source) in enumerate(sources, 1):
            self.assertEqual(number, str(expected))
            self.assertIn('href="https://', source)
            backlinks = re.findall(r'href="#([^"]+)"', source)
            self.assertTrue(backlinks)
            for target in backlinks:
                match = re.search(r'<section id="' + re.escape(target) + r'">(.*?)</section>', text, re.S)
                self.assertIsNotNone(match)
                if match is not None:
                    self.assertIn(f'href="#source-{number}"', match.group(1))
        self.assertEqual(text.count('class="source-check-date"'), 1)

    def test_issue76_delivery_gaps_are_present(self):
        text = PAGE.read_text(encoding='utf-8')
        lowered = text.lower()
        for section in ('do-not-use', 'gaps'):
            self.assertIn(f'id="{section}"', text)
        for phrase in ('ecs-native blue/green', 'deployment target', 'codepipeline v2',
                       'opentelemetry', 'x-ray', 'incident manager', 'opscenter',
                       'dora', 'devlake', 'deployment rework rate'):
            self.assertIn(phrase, lowered)
        for target in ('ECS', 'EKS', 'Lambda', 'EC2'):
            self.assertIn(target, text)
        self.assertIn('now the recommended option for most teams and new projects', text)
        self.assertIn('CodeDeploy remains a valid option for existing CodeDeploy deployments', text)

    def test_issue76_hard_rules_are_kept(self):
        lowered = PAGE.read_text(encoding='utf-8').lower()
        self.assertNotIn('legacy', lowered)
        self.assertNotIn('february 2027', lowered)
        self.assertNotIn('feb 2027', lowered)
        self.assertNotIn('v1 is frozen', lowered)
        self.assertNotIn('v1 frozen', lowered)


if __name__ == '__main__':
    unittest.main()
