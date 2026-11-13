from pathlib import Path
import re
import unittest

PAGE = Path(__file__).resolve().parents[1] / 'site/dist/tech-scan-agents.html'


class Issue73AgentsTests(unittest.TestCase):
    def test_kiro_command_sandbox_scope_and_backend_are_sourced(self):
        page = PAGE.read_text(encoding='utf-8')
        routes = page.split('<section id="routes">', 1)[1].split('</section>', 1)[0]
        for phrase in (
            'local command sandbox is off by default',
            'shell commands and their child processes',
            'built-in file tools and remote HTTP and SSE MCP servers remain outside',
            'stdio MCP servers can be wrapped optionally',
            'platform backend is unavailable',
            'without operating-system isolation unless the current mode requires protection',
        ):
            self.assertIn(phrase, routes)
        self.assertIn('href="#source-20"', routes)
        self.assertRegex(page, r'<li id="source-20"><a href="https://kiro\.dev/docs/sandbox\.md">')

    def test_new_source_entries_link_back_to_supported_sections(self):
        page = PAGE.read_text(encoding='utf-8')
        for source, section in ((20, 'routes'), (21, 'controls')):
            with self.subTest(source=source):
                entry = re.search(rf'<li id="source-{source}">.*?</li>', page, re.S)
                self.assertIsNotNone(entry)
                if entry is not None:
                    self.assertIn(f'href="#{section}"', entry.group())
                self.assertIn(f'id="{section}"', page)

    def test_x_discussion_is_in_controls(self):
        page = PAGE.read_text(encoding='utf-8')
        controls = page.split('<section id="controls">', 1)[1].split('</section>', 1)[0]
        self.assertIn('Tibo (@thsottiaux)', controls)
        self.assertIn('href="#source-21"', controls)

    def test_x_discussion_is_separate_from_kiro_evidence(self):
        page = PAGE.read_text(encoding='utf-8')
        self.assertIn('Tibo (@thsottiaux) highlights approval fatigue when discussing OpenAI Auto-review', page)
        self.assertIn('Automated review is not an isolation boundary', page)
        self.assertIn('href="#source-21"', page)
        self.assertRegex(page, r'<li id="source-21"><a href="https://x\.com/thsottiaux/status/2107368734981517634">')
        self.assertEqual(len(re.findall(r'References last checked:', page)), 1)


if __name__ == '__main__':
    unittest.main()
