# Source-listing standardisation review

## Scope and intent

Base revision: `15a79da44b2ca0339cd16fbf6bea0c88e606e00d` from freshly fetched `main`, fast-forwarded into `dev` before editing.

Readers should find a work, its applicability and any adaptation in one place rather than alternating between attribution, learning-reference and bibliography lists. The source-check date should describe one recorded page-wide maintenance pass, not conflict with older dates repeated beside links.

Audited all 14 published HTML pages. Consolidated the 13 pages that cite works or primary workflow documents into one final `Sources` heading, one visible numbered list and one page-level check-date paragraph. Introduction contains orientation and operational navigation, not a separate bibliography, and is unchanged.

## Changes and author review

- `writing.md` defines the canonical-entry structure, citation numbering, date provenance, operational-link exceptions and regression command. Its own sources now use one numbered list and say `not recorded` rather than inventing a source-check date. The former writing-standard heading anchors remain available.
- `design.md` and `site/README.md` point to the same standard rather than describing a separate attribution panel.
- Source entries contain the work's title, original link, useful scope and concise `Used in` links. Attribution/adaptation notes and optional learning works no longer form parallel lists or disclosures.
- Existing publication dates, study periods, version distinctions and consequential evidence limitations remain. In particular, the METR/McKinsey limits, IMDA full-document caveat, TypeSafe corrections, guardrail guidance, metric-ladder adaptation and fictional-case qualification are retained.
- The 9 November 2026 page-wide date is inherited from the recorded main-branch public-reference maintenance pass; this restructuring does not advance individual retrieval records or claim fresh verification of all external sources. The About page's repository records were inspected during this task. Unavailable internal harness documents, source revisions and installed controls still require owner confirmation.
- Citation labels now agree with their displayed list ordinal while existing source and learning IDs remain stable. Operational installation, training and video links remain available in context.
- Source aliases and moved adaptation notes receive desktop and mobile scroll offsets. Browser checks exposed a desktop sticky-header overlap; a regression assertion failed before the CSS fix and passed afterwards.
- The validation workflow watches `tests/**`, so changes to the new source-contract tests are not silently omitted from CI.

## Structural and execution evidence

- Baseline: all 9 existing regression tests passed before implementation.
- New source-contract checks failed on the original parallel lists, headings, check dates, missing EDS lists and inconsistent citation labels. Final `python3 -m unittest discover -s tests -v`: **41 tests passed**, including 26 negative/compatibility regression tests of the actual source-contract checks. Review-driven fixtures reject nested-page bypasses, hidden or parallel bibliographies, invalid/mismatched dates, per-link ISO access dates, reversed numbering, unnormalised fragment bypasses and missing ARIA targets.
- All **551 original HTML IDs** and every original per-page distinct external source URL are preserved. There are **169 source-list entries across 13 pages**, not 169 globally distinct works.
- Checked **1,017 local fragment occurrences** and **84 ARIA label/description target occurrences** across all 14 pages: no missing targets or duplicate IDs.
- Existing assembly/HTTP tests deliver real pages and assets below both `/AI-PDLC/` and `/AI-PDLC/dev/`; local link/asset resolution remains within the selected prefix.
- `actionlint` 1.7.12 and `git diff --check`: passed.

## Browser evidence and limits

Exercised all 14 pages at 1440 px and 375 px: **28 page/viewport combinations**, with no observed page-level horizontal overflow or captured JavaScript page errors. Sourced pages exposed one visible Sources heading/list, not a closed attribution disclosure. Visually inspected Product implementation's consolidated list on desktop and mobile.

Exercised five moved/preserved destinations at both widths: Concepts' `source-11`, `learning-references` and `learning-models`; Project Discovery's `metric-adaptation`; and Transformation's `research-detail`. All **10 source-link/anchor probes** landed below the sticky header after the CSS fix. Existing links were clicked where present; otherwise a temporary browser-only link probed the preserved destination. Retested with cache disabled after noticing stale styles in the browser session.

These checks establish the structure, destinations and layouts exercised. This task did not freshly fact-check every linked external work, validate internal Eitri implementation, conduct a full accessibility audit or run a representative-reader comprehension session. Historical per-reference retrieval dates and unresolved outcomes remain in the existing maintenance records.
