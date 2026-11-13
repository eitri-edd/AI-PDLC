# Targeted reference addition — issues #70 and #71 (13 November 2026)

## Scope

Two new source URLs, added to support the editorial changes in
[issues #70](https://github.com/eitri-edd/AI-PDLC/issues/70) and
[#71](https://github.com/eitri-edd/AI-PDLC/issues/71). This is a targeted
addition, not a new whole-site claim review. No other reference was
re-fetched for this change.

## New URLs (both verified live on 13 November 2026)

- `https://aws.amazon.com/blogs/security/help-defend-against-memory-poisoning-in-amazon-bedrock-agentcore-with-multi-layer-write-validation/`
  — Tarun Kumar, AWS Security Blog, 9 November 2026. HTTP 200. Used in
  `concept.html` (source-29) and `product-implementation.html` (source-17).
  The demo classifies 11 simulated cases (3 benign, 8 attack) and returns
  the expected decision for all 11, using a local keyword-overlap
  approximation of semantic similarity instead of Amazon Titan Text
  Embeddings V2; thresholds and scores are illustrative, not field accuracy.
- `https://arxiv.org/abs/2611.10058`
  — Wu et al. (2026), *From Delegation to Action Approval*. Submitted
  6 November 2026. HTTP 200. Used in `concept.html` (source-30) and
  `transformation.html` (source-16). Self-reported survey of 203 developers;
  it does not measure exploit incidence.

## Inventory dating note

`reference-checks.json` enforces a single `checked_on` date for every
record (currently 2026-11-12), and the test suite requires every record to
carry it. The two records above therefore carry `checked_on: 2026-11-12`
in the inventory, although they were first verified live on
13 November 2026. Do not read the 12 November date on these two entries as
the day they were first checked. The nightly whole-site reference pass
re-dates the inventory when it next runs on `main` after this change merges,
and the history in `reference-checks.json` retains the previous inventory
without relabelling its dates.

## Inventory changes

- `current_unique_urls`: 215 → 217; `current_unique_hrefs`: 221 → 223;
  `counts.retrieved`: 197 → 199.
- `concept.html` page pass: `source_entries` 37 → 39,
  `unique_fetch_destinations` 42 → 44.
- `product-implementation.html` page pass: `source_entries` 16 → 17,
  `unique_fetch_destinations` 22 → 23.
- `transformation.html` page pass: `source_entries` 15 → 16,
  `unique_fetch_destinations` 20 → 21.
- Page-level "References last checked" dates are unchanged
  (12 November 2026) on all pages, because no page-wide pass was run.
