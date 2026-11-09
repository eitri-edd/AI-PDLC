"""Negative fixtures exercise the published-site checks, not a second validator."""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import test_sources as contracts


STRUCTURE = "test_one_final_sources_section_and_one_complete_numbered_list"
DATES = "test_one_recorded_reference_check_date_without_per_source_dates"
CITATIONS = "test_citation_numbers_and_aria_labels_match_their_canonical_entry"
LINKS = "test_all_page_ids_and_local_fragments_remain_unambiguous"
VALID_PAGE = """<!doctype html><html><body><main>
<section id="content"><h1>Example</h1><p><a href="#source-example"
aria-label="Source 1: Example">[1]</a></p></section>
<section id="sources"><h2>Sources</h2>
<p class="source-check-date">References last checked:
<time datetime="2026-11-09">9 November 2026</time>.</p>
<ol class="source-list"><li id="source-example"><a href="https://example.org/paper">Example</a>.</li></ol>
</section><footer>Last editorial review: 6 November 2026.</footer>
</main></body></html>"""


class SourceContractRegressionTests(unittest.TestCase):
    def run_contract(self, method, pages=None, case_class=None):
        case = (case_class or contracts.SourceListingTests)(method)
        if pages is not None:
            case.documents = {name: contracts.Document(raw) for name, raw in pages.items()}
            case.source_pages = set(case.documents) - contracts.ORIENTATION_ONLY_PAGES
        result = unittest.TestResult()
        case.run(result)
        self.assertEqual(result.errors, [], "Fixture must reach a contract assertion, not crash")
        return result

    def assert_rejected(self, method, raw, pages=None):
        result = self.run_contract(method, pages or {"example.html": raw})
        self.assertTrue(result.failures, f"Invalid fixture was accepted by {method}")

    def assert_accepted(self, method, raw, pages=None):
        result = self.run_contract(method, pages or {"example.html": raw})
        self.assertEqual(result.failures, [])

    def assert_nested_page_checked(self, relative_path):
        with tempfile.TemporaryDirectory() as temporary:
            dist = Path(temporary)
            (dist / "example.html").write_text(VALID_PAGE)
            (dist / "index.html").write_text("<h1>Orientation only</h1>")
            nested = dist / relative_path
            nested.parent.mkdir(parents=True)
            nested.write_text("<h1>Missing mandatory sources</h1>")

            class FixtureSite(contracts.SourceListingTests):
                pass

            with patch.object(contracts, "DIST", dist):
                FixtureSite.setUpClass()
                result = self.run_contract(STRUCTURE, case_class=FixtureSite)
            self.assertTrue(result.failures, f"Invalid nested page {relative_path} was accepted")
            self.assertIn(relative_path, FixtureSite.documents)
            self.assertNotIn("index.html", FixtureSite.source_pages)

    def test_nested_new_page_cannot_bypass_source_contract(self):
        self.assert_nested_page_checked("guides/new-page.html")

    def test_nested_index_is_not_an_orientation_exception(self):
        self.assert_nested_page_checked("guides/index.html")

    def test_canonical_listing_and_ancestors_cannot_be_hidden(self):
        for attribute in (
            'hidden', 'hidden="until-found"', 'aria-hidden="true"',
            'style="display: none !important"', 'style="visibility: hidden"',
            'style="visibility:collapse"', 'style="opacity: 0"',
            'style="content-visibility:hidden"', 'aria-expanded="false"',
        ):
            for tag in ('<main', '<section id="sources"', '<ol class="source-list"',
                        '<li id="source-example"'):
                with self.subTest(attribute=attribute, tag=tag):
                    self.assert_rejected(STRUCTURE, VALID_PAGE.replace(tag, f'{tag} {attribute}', 1))

    def test_source_listing_cannot_have_a_collapsed_details_ancestor(self):
        raw = VALID_PAGE.replace('<main>', '<details><summary>References</summary><main>')
        self.assert_rejected(STRUCTURE, raw.replace('</main>', '</main></details>'))

    def test_hidden_parallel_bibliography_is_rejected(self):
        extra = '<div hidden><ol class="source-list"><li>Second bibliography</li></ol></div>'
        self.assert_rejected(STRUCTURE, VALID_PAGE.replace('<main>', '<main>' + extra))

    def test_extra_sources_heading_outside_canonical_section_is_rejected(self):
        for level in range(1, 7):
            with self.subTest(level=level):
                extra = f'<h{level}>Sources</h{level}>'
                self.assert_rejected(STRUCTURE, VALID_PAGE.replace('<main>', '<main>' + extra))

    def test_parallel_bibliography_headings_are_rejected(self):
        for heading in ('References', 'Bibliography', 'Further reading', 'Research sources',
                        'Sources and references', 'Sources and scope',
                        'Sources and learning references', 'Sources and maintenance records',
                        'Supporting sources', 'Section attribution and adaptations'):
            with self.subTest(heading=heading):
                extra = f'<h2>{heading}</h2><ul><li>Separate source</li></ul>'
                self.assert_rejected(STRUCTURE, VALID_PAGE.replace('<main>', '<main>' + extra))

    def test_parallel_bibliography_containers_are_rejected(self):
        for attribute in ('id="bibliography"', 'class="references-list"',
                          'id="sources"', 'aria-label="References"'):
            with self.subTest(attribute=attribute):
                extra = f'<div {attribute}><ul><li>Separate source</li></ul></div>'
                self.assert_rejected(STRUCTURE, VALID_PAGE.replace('<main>', '<main>' + extra))

    def test_instructional_heading_and_operational_links_remain_allowed(self):
        extra = ('<h3>Choose relevant, current and authoritative sources</h3>'
                 '<p>Use <a href="https://example.org/tool">this operational tool</a>.</p>')
        self.assert_accepted(STRUCTURE, VALID_PAGE.replace('<main>', '<main>' + extra))

    def test_open_details_and_explicitly_visible_listing_remain_allowed(self):
        raw = VALID_PAGE.replace('<main>', '<details open><summary>Reading</summary><main>')
        raw = raw.replace('</main>', '</main></details>')
        raw = raw.replace('<ol class="source-list"',
                          '<ol aria-hidden="false" style="display:block;opacity:1" class="source-list"')
        self.assert_accepted(STRUCTURE, raw)

    def test_impossible_machine_check_dates_are_rejected(self):
        for value in ('2026-99-99', '2026-02-29', '2026-04-31', '0000-11-09'):
            with self.subTest(value=value):
                self.assert_rejected(DATES, VALID_PAGE.replace('datetime="2026-11-09"',
                                                              f'datetime="{value}"'))

    def test_displayed_check_date_must_match_machine_date(self):
        self.assert_rejected(DATES, VALID_PAGE.replace('9 November 2026', '8 November 2026'))

    def test_per_source_check_dates_with_punctuation_are_rejected(self):
        for text in ('Accessed: 2026-11-09', 'Retrieved (2026-11-09)',
                     'Referenced, 9 Nov 2026', 'Checked on: 9 November 2026',
                     'Rechecked [2026/11/09]', 'Checked — 09/11/2026',
                     'Accessed: 09-Nov-2026', 'Retrieved: 9.11.2026',
                     'Accessed: November 9, 2026'):
            with self.subTest(text=text):
                self.assert_rejected(DATES, VALID_PAGE.replace('Example</a>.</li>',
                                                               f'Example</a>. {text}.</li>'))

    def test_per_source_check_date_cannot_hide_in_a_standalone_span(self):
        extra = '<div><span>Accessed: 2026-11-09</span></div>'
        self.assert_rejected(DATES, VALID_PAGE.replace('<main>', '<main>' + extra))

    def test_not_recorded_cannot_contain_a_time_element(self):
        raw = VALID_PAGE.replace('9 November 2026', 'not recorded')
        self.assert_rejected(DATES, raw)

    def test_honest_not_recorded_without_time_remains_allowed(self):
        raw = VALID_PAGE.replace('<time datetime="2026-11-09">9 November 2026</time>',
                                 'not recorded')
        self.assert_accepted(DATES, raw)

    def test_real_leap_day_check_date_remains_allowed(self):
        raw = VALID_PAGE.replace('2026-11-09', '2024-02-29').replace('9 November 2026', '29 February 2024')
        self.assert_accepted(DATES, raw)

    def test_publication_and_editorial_review_dates_remain_allowed(self):
        raw = VALID_PAGE.replace('Example</a>.</li>',
                                 'Example</a>. Published: 2020-01-02; publication updated: 3 March 2021.</li>')
        self.assert_accepted(DATES, raw)
        self.assert_accepted(DATES, raw.replace('Last editorial review: 6 November 2026',
                                               'Last reviewed: 2026-11-06'))

    def test_reversed_bibliographies_are_rejected(self):
        for attribute in ('reversed', 'reversed="reversed"', 'reversed="false"'):
            for method in (STRUCTURE, CITATIONS):
                with self.subTest(attribute=attribute, method=method):
                    raw = VALID_PAGE.replace('<ol class="source-list"',
                                             f'<ol {attribute} class="source-list"')
                    self.assert_rejected(method, raw)

    def test_forward_start_and_explicit_list_values_remain_supported(self):
        raw = VALID_PAGE.replace('<ol class="source-list"', '<ol start="3" class="source-list"')
        raw = raw.replace('Source 1:', 'Source 3:').replace('[1]', '[3]')
        raw = raw.replace('</ol>', '<li value="7" id="source-second">Second source</li></ol>')
        raw = raw.replace('</p></section>',
                          '<a href="#source-second" aria-label="Source 7: Second">[7]</a></p></section>')
        self.assert_accepted(STRUCTURE, raw)
        self.assert_accepted(CITATIONS, raw)

    def test_normalized_relative_links_reject_missing_local_fragments(self):
        for page, href, target in (
            ('example.html', './concept.html#missing-local-fragment', 'concept.html'),
            ('example.html', 'guides/../concept.html#missing-local-fragment', 'concept.html'),
            ('example.html', './%63oncept.html#missing-local-fragment', 'concept.html'),
            ('guides/new-page.html', '../concept.html#missing-local-fragment', 'concept.html'),
            ('guides/new-page.html', './concept.html#missing-local-fragment', 'guides/concept.html'),
            ('guides/deep/new-page.html', '../../concept.html?view=full#missing-local-fragment', 'concept.html'),
            ('example.html', './guides/#missing-local-fragment', 'guides/index.html'),
        ):
            with self.subTest(page=page, href=href):
                raw = VALID_PAGE.replace('<main>', f'<main><a href="{href}">Local link</a>')
                self.assert_rejected(LINKS, raw, pages={page: raw, target: VALID_PAGE})

    def test_local_html_fragment_cannot_target_an_undiscovered_page(self):
        raw = VALID_PAGE.replace('<main>', '<main><a href="./missing-page.html#content">Missing page</a>')
        self.assert_rejected(LINKS, raw)

    def test_relative_links_resolve_against_containing_page_not_root(self):
        raw = VALID_PAGE.replace('<main>', '<main><a href="./concept.html#nested-target">Nested link</a>')
        nested = VALID_PAGE.replace('<main>', '<main id="nested-target">')
        self.assert_accepted(LINKS, raw, pages={
            'guides/new-page.html': raw, 'guides/concept.html': nested, 'concept.html': VALID_PAGE,
        })

    def test_normalized_valid_fragments_and_external_links_remain_allowed(self):
        for href in ('./concept.html#source-%65xample', 'guides/../concept.html#source-example',
                     'https://elsewhere.example/concept.html#not-local',
                     '//elsewhere.example/concept.html#not-local'):
            with self.subTest(href=href):
                raw = VALID_PAGE.replace('<main>', f'<main><a href="{href}">Link</a>')
                self.assert_accepted(LINKS, raw, pages={'example.html': raw, 'concept.html': VALID_PAGE})

    def test_all_aria_idref_tokens_must_exist_in_the_same_document(self):
        for attribute in ('aria-labelledby', 'aria-describedby'):
            for tokens in ('missing-aria-target', 'content missing-aria-target',
                           'content\tmissing-aria-target\nsource-example'):
                for tag in ('<main', '<a href="#source-example"'):
                    with self.subTest(attribute=attribute, tokens=tokens, tag=tag):
                        raw = VALID_PAGE.replace(tag, f'{tag} {attribute}="{tokens}"', 1)
                        self.assert_rejected(LINKS, raw)

    def test_multiple_valid_aria_idref_tokens_remain_allowed(self):
        raw = VALID_PAGE.replace('<main>', '<main aria-labelledby="content source-example" '
                                 'aria-describedby="source-example\tcontent">')
        self.assert_accepted(LINKS, raw)


if __name__ == "__main__":
    unittest.main()
