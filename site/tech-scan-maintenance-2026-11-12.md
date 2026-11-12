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

## Terminology and writing.md review — 12 November 2026

Reviewed the five Tech Scan pages against writing.md (441 lines at main ee8ebb9) and checked every invented or internal term against industry usage.

Renamed: "AWS spine" to "AWS platform" (spine is not an industry term for a cloud-platform view); "Spines and portable seams" to "Cross-cutting views"; "portable seams" to "shared integration standards" (MCP, OpenTelemetry, Spec Kit with OKF, GitLab/GitHub, SARIF/JSON); "concept anchor" to "Concepts section". Removed the misattribution "Orange ITS": the pillar names come from Automater alone (context assembly, tool design, permissions, memory, evals, observability); the heyuan110 framing names a different six and is the source of the "about 80% of agent stability" figure, now attributed to that one 60-day production report. Dropped the count "three 2026 framings" (only two are cited) and "the brief's list" (now "the proposal's list"). Dropped "Mode 3" (undefined) and the unverified "Temporal, validated by AWS as a Nitro Sandbox driver".

Defined at first use: typed decision and its four types (Choice, Score, Noul as a yes/no question, Box as visual grounding); OKF (Open Knowledge Format); IM8 (Instruction Manual 8) and ARC (Agentic Risk & Capability Framework), linked to the definitions in eds-developer-harness.html; Cedar (policy language); CloudFormation Guard; ACL-aware retrieval; NSM (Nitro Security Module); SIG (Special Interest Group); SLA; AMI. Corrected two dates: Zep stopped maintaining Community Edition in April 2025, not 2026 (source 23, Zep's own blog); the Lambda MicroVMs 14-region figure comes from a November 2026 builder article, not October. Added source 24 for the Trigger.dev 1 November 2026 environment-variable disclosure (verified against the vendor disclosure as reported 2 November 2026).

Writing.md fixes: parallel items of three or more (hard gates, trust rules, integration standards, qualification checks, broadening routes, control mappings) are now bullet lists; long sentences split; author-facing notes moved here (draft-label removal conditions; "rename the pillars if a later framing settles"); the draft-label conditions paragraph and the "rename the pillars" instruction were removed from the hub and harness pages. "Must" kept only for the hard-gate and trust-rule statements; other necessities reworded ("needs to", "needs to design"). Kept "spoke" (standard hub-and-spoke vocabulary) and "primitive" (defined on the page as "isolation building blocks").

Editorial note: writing.md is 441 lines at main ee8ebb9 (the 883-line figure in earlier notes was a miscount; the file on disk is 441 lines, 53,709 characters).

## Request-flow diagram — 12 November 2026

Added Figure 1 to the hub's Purpose section: a seven-step chain following one task through the Wave 1 spokes (task arrives; harness runs the loop; loop gathers context; loop asks the model; gateway routes the tool call; sandbox runs the code; answer and evidence return), with a dashed loop-back arrow from step 6 to step 4 (repeat until a final answer) and a dashed band for Observability (planned, cross-cutting). Step 3 (context) is an amber planned node: the Context spoke is Wave 2, and today Bedrock Knowledge Bases are reached through the Gateway.

The step order follows the AWS reference architecture "Guidance for Building Agentic AI Foundation Solutions on AWS" (reviewed for technical accuracy 29 January 2026), adapted to the four spokes: its flow runs authenticated user, AgentCore Runtime, Identity and Guardrails, LangGraph Agent, Memory, Gateway, tools and Knowledge Base, Bedrock Models, then the answer back, with Observability throughout. The guidance is the hub's source 5; its canonical PDF URL (d1.awsstatic.com) was verified live and the PDF fetched (4 pages, SHA-256 04a3bdeb8b876abe1636a372bffa10c1fbb481f6550e3b6b74e139e2d621e66a). An earlier search result for the same document carried a search-proxy host; the canonical address was confirmed before citing. The Strands workshop loop and the AWS multi-tenancy blog Figure 1 were considered as alternative bases and not used: the loop does not show where a request starts and ends, and the layered map repeats the hub's layer-map table.

The figure follows the site's existing concept-figure pattern (SVG with figure-reading text equivalent, diagram-detail disclosure, caption; the shared diagram defs block was added to the hub page, as on concept.html). Each figure-reading step links to its spoke. No new navigation item: the figure sits inside the Purpose section.

## Slim navigation — 12 November 2026

The 41-link Tech Scan tree in the sidebar (hub + 8 hub sections + 4 spokes x 7 sections) was too long, so the sidebar now lists pages only, matching the rest of the guide: Tech Scan (draft) with its four spokes — Models, Harness, AI gateway, Sandbox — and nothing below them. All section links were removed from the sidebar on all 19 pages; the sections still exist in the pages and remain reachable through each page's On-this-page navigation and in-page links. The collapsible second-layer groups are gone with the section lists, and the .nav-group styles added for them were removed from styles.css as unused. Spoke pages keep aria-current on their own spoke link and nav-parent-active on the Tech Scan link; the hub keeps aria-current on its own link.

## Waves figure and page disclaimer — 12 November 2026

Added Figure 2 to the hub's Waves 2 and 3 section: three boxes in build order (Wave 1 published: Models, Harness, AI gateway, Sandbox; Wave 2 planned: Workflows, Factories, Agents; Wave 3 planned: Context, Verification, Delivery), with a dashed box below Wave 3 for Languages and the AWS platform, marked "Last on purpose". The wave membership and the last-on-purpose rule come from the hub's own text and issue #59 (hub source 2); no new source was needed. The figure follows the site's concept-figure pattern (SVG, figure-reading text equivalent with links to the four Wave 1 spokes, diagram-detail disclosure, caption).

Added the same disclaimer to the front of all five Tech Scan pages, right after the article header, using the About page's callout-disclaimer form: "Tech Scan is an early exploration of emerging agentic technologies that support the key areas of the AI-SDLC. It is still in its early stages: entries are research references, not settled recommendations, and they may not reflect the latest products or releases. Use your own judgement and do your own research before adopting anything listed here." No new external URLs, so the reference inventory is unchanged.
