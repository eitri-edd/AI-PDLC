# Product ideation learning-flow review

Updated 28 October 2026 against the referenced critical review, `../writing.md`, `../design.md` and the current published source at `dist/product-ideation.html`.

## Result

The page now follows **Frame → Test → Decide → Handoff**, with six practical steps:

1. Understand the problem.
2. Define value and explore alternatives.
3. Design the experiment.
4. Prototype and learn.
5. Evaluate and decide.
6. Prepare the handoff after a justified commitment.

Product, Design and Engineering collaborate from the start. The baseline, outcome measure, target and guardrails precede experiment construction. The concept brief develops into a draft PRD for testing, then a versioned evidence-backed PRD for bounded implementation. The PRD remains revisable.

A continuous fictional service-desk knowledge-assistant example links problem P-1, concept brief v0.1, draft PRD versions, experiments X-1/X-2, decision D-1 and PRD v1.0. The first test misses its rule and triggers improvement; the second supports a bounded pilot, with explicit sampling limits and owned open questions. Every result, identifier and threshold is labelled fictional. The example grants no access and submits no requests.

The decision model distinguishes commitment, inconclusive evidence requiring continued testing, rework (improve, redesign or pivot), and stop. Each returns to the appropriate practical step, with risk and budget reconsidered each cycle. Commitment is distinct from production approval.

## Figures and retained principles

The six inline SVG figures cover the learning journey, 6W/4C problem framing, Double Diamond alignment, uncertainty-driven experiment selection, the evidence-to-decision tree and evidence/requirements/test traceability. Each has a numbered caption, accessible title and description, text equivalent, scrolling region and the existing shared diagram controls. The Double Diamond mapping is an adaptation, attributed to the Design Council under CC BY 4.0. Develop spans options in Frame and experiments in Test; Deliver means testing solutions at small scale, not production deployment. The problem checkpoint does not introduce a formal organisational gate.

The existing white-based Editorial Enterprise Light system, shell, primary navigation, shared styles and shared script remain. Local reading aids use existing tokens; scoped SVG borders meet the design system's 3:1 contrast target. Design variance, motion and density follow the existing handbook (approximately 3/4/5); motion remains limited to the existing diagram explanation and respects reduced-motion preferences.

Security, privacy, approved tools, participant information, access restrictions, prototype expiry/disposition, accountable risk acceptance, high-consequence human approval and the distinction between investigation, implementation and release are retained. The metric ladder, cross-level intent/constraints discussion and agentic UX checks remain available as optional references. Generated research is explicitly distinguished from user observations; deterministic permission boundaries are not averaged with probabilistic quality metrics.

Implementation procedures are cross-linked rather than duplicated. All 38 original IDs remain, including legacy figure aliases. Both contents lists match the new section order. Direct links open optional content, and print handling expands it while restoring the reader's previous state afterwards. Native disclosures and page content work without JavaScript.

## Files changed

| File | Change |
| --- | --- |
| `dist/product-ideation.html` | Six-step learning path, six diagrams, integrated example, PRD evolution, decisions and optional references; accessibility and contents updates. |
| `dist/index.html` | Remove the editorial draft qualifier from the page description metadata. |
| `dist/product-ideation.css` | Page-specific example/reference styling, metadata, focus treatment and diagram border contrast using existing tokens. |
| `dist/product-ideation.js` | Direct-link disclosure handling and print expansion/restoration. |
| `../writing.md` | Align the expanded AI-SDLC title and preserve repository/path names. |
| `../design.md` | Align the project title with AI-SDLC branding. |
| `../README.md` | Update the ideation synopsis and terminology. |
| `README.md` | Update page inventory, preview/publication information and remove a reference to absent `plan.md`. |
| `product-ideation-review.md` | Record changes, validation and limits. |
| `product-pages-review.md` | Remove the excluded discovery-source entry from the older source mapping. |

## Validation

Temporary QA tooling was kept outside the repository and published output: Playwright/Chromium, axe-core 4.14.0, html-validate 11.17.0 and Lighthouse 13.6.0. The site still requires no build or package installation.

All 24 automated check groups passed:

- Unique IDs, preserved legacy anchors, sequential headings and synchronised desktop/mobile contents.
- All 46 distinct outgoing local links/assets and all incoming site links to ideation resolve. All six distinct external destinations returned HTTP 200; the Design Council source now uses its canonical destination.
- No document overflow at 320, 390, 768, 1024 and 1440 pixels with optional content collapsed and expanded; no overflow with 200% text size.
- Keyboard skip-link focus, native disclosure activation, diagram step-through and play/pause state, reduced-motion defaults, direct-link landing and in-page example navigation.
- Print disclosure expansion/restoration and no-JavaScript reading/disclosure operation.
- No axe WCAG A/AA or best-practice violations with all content expanded at desktop and 320 pixels.
- Valid HTML, described SVGs, no SVG text overlap, no text outside viewBoxes or crowded node edges, and no browser errors or failed local requests.

HTML validation retains deliberate `role="list"` and `role="table"` declarations used by the site's styled native elements, with the redundant-role lint rule disabled. Other source, structure and accessibility checks passed.

The local Lighthouse mobile audit scored **99 performance, 100 accessibility, 100 best practices and 100 SEO**, with 1.7-second lab LCP. Cache/compression findings reflect the local static preview; these are lab observations, not production measurements. Automated accessibility checks do not establish complete conformance. Desktop, mobile example content and every diagram were also visually inspected.

## Source and workflow limits

The Design Council and SVPG descriptions were checked against their primary sources. Existing Defence Product Playbook, Spec Kit and AUX attributions remain; no new EDS policy or decision authority is asserted. The Playbook web tool could not extract its application content, although the URL loaded successfully during the link check. Existing playbook interpretations remain qualified as adaptations or recommendations.

The connected GitHub account can read the upstream repository but cannot push directly. The change is prepared on `improve/product-ideation-learning-journey` in an authenticated fork for upstream pull-request review. The live site changes only when the maintainers merge the pull request and the existing Pages workflow succeeds.

## Metadata and reference cleanup

Removed the remaining excluded discovery-source entry from the older review's source mapping. The public pages contain no coverage attributed to that source or reference to it. Removed the Draft status from Product Ideation's header metadata and the draft qualifier from the Introduction's description metadata. Retained the update date and updated the authoring guidance to keep editorial status out of rendered page metadata.

Checked every HTML page for the excluded reference and draft-status metadata, previewed both changed pages at desktop and mobile widths, and reran the 24 ideation validation groups successfully. Working draft PRDs and draft responses remain substantive product concepts rather than page-status labels.

The authoring standards now explicitly state that page status metadata is not required. The header template allows date or ownership metadata where useful, without a page status field. Editorial status is optional in maintenance records, rather than a required field moved elsewhere.
