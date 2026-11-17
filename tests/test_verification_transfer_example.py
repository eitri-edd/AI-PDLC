"""Content contract for the verification engineering worked example."""
import re
import unittest
from html import unescape
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "site/dist/concept.html"


class VerificationTransferExampleTest(unittest.TestCase):
    def test_transfer_rule_and_independent_evidence_are_explained(self):
        html = PAGE.read_text(encoding="utf-8")
        section = html.split('id="verification-engineering"', 1)[1].split('</section>', 1)[0]
        example = re.search(r'<aside class="example learning-example".*?</aside>', section, re.S)
        self.assertIsNotNone(example)
        if example is None:
            self.fail('Verification worked example is missing')
        self.assertIn('<ul>', example.group())
        self.assertGreaterEqual(len(re.findall(r'<li>', example.group())), 3)
        text = unescape(re.sub(r'<[^>]+>', ' ', example.group()))
        text = re.sub(r'\s+', ' ', text).strip()
        for expected in (
            'Fictional scenario', 'Task:', 'Situation:', 'Rule:', 'Output:',
            'Independent checks:', 'Decision:',
            'at most one pending transfer per asset',
            'different recipients', 'one request is accepted and one is rejected',
            'another asset', 'after the pending transfer is resolved',
            'current holder', 'acknowledges', 'test environment',
            'independently', 'deliberately broken', 'evidence, not proof',
            'human',
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, text)


if __name__ == '__main__':
    unittest.main()
