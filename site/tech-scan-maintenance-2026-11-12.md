# Tech Scan link-verification pass · 12 November 2026

## Scope

Verifies the five new Tech Scan pages (hub plus Wave 1 spokes Models, Harness,
AI gateway and Sandbox) added to `site/dist/` on branch `dev`, based on main
`ee8ebb9` (merge PR #57). The 14 previously published pages were not
re-checked in this pass; their 12 November 2026 records in
[reference-checks.json](reference-checks.json) stand, except that the four
records whose link appears on every page (the three Google Fonts origins and
the training entry point) gained the five new pages in their `files` lists and
one claim review per new page.

Every external URL on the five new pages was fetched by direct HTTP GET on
12 November 2026 and received a disposition in `reference-checks.json`. The
inventory now covers 19 pages, 190 fetch destinations and 196 distinct
external link values (138 and 144 before this pass). Each new page displays
**References last checked: 12 November 2026**.

## Outcomes

- 51 new destinations retrieved directly (HTTP 200, readable text);
- 1 partial reader recovery: BeyondTrust's AgentCore CVE post returns 403 to
  direct fetch (bot protection). The live reader recovered the article's key
  findings and both CVE sections, so its record is `partial_reader_recovery`
  with a `limited` claim outcome and the 403 recorded, following the
  precedent for the Medium guardrails post in the whole-site pass.

A successful HTTP request was not treated as factual verification. Dated and
quantitative claims were checked against the fetched text where the claim
depends on a single source.

## Corrections found by the check

Two claims on the new pages did not match their cited source and were fixed
before the push:

1. **Gateway, OpenRouter row.** The row stated Stripe agreed to acquire
   OpenRouter, announced August 2026, citing the ArcBeta gateway comparison.
   ArcBeta contains no Stripe mention; it does support the row's LiteLLM
   (malicious PyPI releases in March and October 2026) and Portkey (Palo Alto
   Networks closed its acquisition on 29 May 2026) claims. The Stripe claim
   is true — Stripe's newsroom announced the agreement on 19 August 2026 —
   so the row now cites Stripe's newsroom announcement as source 16 instead.
2. **Sandbox, Lambda MicroVMs.** The page stated in the present tense that
   MicroVMs "are ARM64 only with no GPUs". That was true at launch (22 June
   2026, ARM64, five regions, no Singapore) but AWS added x86_64 support on
   5 November 2026 and has since expanded regions. The sentence now states
   the launch facts in the past tense, cites the AWS News Blog launch post
   (source 14) and a 7 November 2026 builder article recording the x86_64
   addition and 14 regions (source 15), and tells the reader to review
   current architectures and regions before recommending MicroVMs.

One boundary is recorded as a limitation rather than a fix. The Models page
cites the S5 Labs decision-model survey for its Box statements; the survey
documents choice, score and noul types for Jev, Clef and d1 but never
mentions Box, so the Box absence claims rest on the research pass and the
Decider README check, not on that survey alone. The inventory record for the
S5 Labs URL carries that limitation, and the page's wording stays hedged
("not confirmed", "not verified").

## What this pass does not establish

This is a link and cited-claim check for the five new pages, not a re-run of
the whole-site reference maintenance. It does not certify every statement in
every cited source, reader comprehension, live Eitri execution or
organisational policy compliance. The Tech Scan pages are labelled drafts;
their entries are research references from web sources reviewed 11–12
November 2026, not locally deployed or benchmarked options.
