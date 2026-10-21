# Introduction: editorial review

## Site disclaimer refinement · 21 October 2026

At the user's request, removed the policy, authority and ownership disclaimers flagged in the site-wide review. Refined the surrounding passages across `dist/index.html`, `dist/concept.html`, `dist/transformation.html`, `dist/product-ideation.html`, `dist/ai-pdlc.html` and `dist/eds-skills-catalogue.html`:

- Replaced the introduction's policy-status disclaimers with direct guidance on finding applicable policies, owners, evidence and approvals. Renamed the audience section and aligned its navigation labels.
- Made the concept example introduction, platform role description, shared-service ownership and pilot decision rules more direct.
- Clarified how the product-team table supports responsibility and decision ownership, shortened the attributed lifecycle analysis, and removed repeated external-maintainer notices while retaining author attribution and the maintainer table.

Validation: 405 local links and anchors and unique IDs passed across the six changed pages. Browser layout checks at 320, 768 and 1440 px passed with no page overflow or script errors; external media requests were blocked during these local copy/layout checks. The initial full-load check timed out on the introduction's external content, so the completed checks used document readiness. Visually inspected the introduction on desktop and shared-service ownership on mobile. Confirmed that the flagged wording is absent from the public pages. Changes remain local and unpublished.

## Previous review · 17 October 2026

Reviewed on 17 October 2026 against `writing.md`, `design.md` and the supplied introduction feedback. Revised `dist/index.html`.

## Findings and revisions

| Finding | Revision |
| --- | --- |
| Audience language focused on developers despite broader responsibilities elsewhere. | Named product, design, engineering, QA, security and operations participants, with organisational leaders as readers for adoption and support. |
| The opening could be read as an approved EDS lifecycle. | Positioned the site as a proposed organisational playbook with Eitri implementation guidance. Added draft status, review date and explicit unresolved owner and lifecycle-version fields. |
| Principles, obligations and tool support were not visibly separated. | Added a three-layer table and linked starting points. Applicable requirements derive from authoritative policy or process, not the tool or this draft. Missing tool support calls for an agreed alternative with the control owner. |
| Navigation named documents rather than the reader’s task. | Added routes for an idea, feature, defect and high-risk change, each with a minimum starting workflow, evidence and decision responsibilities. High-risk guidance supplements feature and defect work; an active incident follows the existing incident process. |
| The small upload pilot mixed usability success with security and implementation acceptance. | Used synthetic documents and simulated recipients, labelled the threshold illustrative and separated exploratory usability evidence, security assurance and production acceptance. No observed failures in ten users does not establish the absence of rare security failures. |
| Broad historical claims and diagram wording could overstate the case. | Described sequential delivery as illustrative and changed the assessment caption to make results evidence for a human choice. Preserved the downstream-bottleneck discussion and costly-to-reverse decision warning. |
| The closing repeated an evergreen claim and sent every reader towards an experiment. | Added a task-based next step and a concrete route for recording gaps and confirming changes with the responsible owner. Defined AI-assisted development and AI agent. |

## Authority and remaining editorial limits

The user’s suggested positioning was adapted to describe decisions, evidence and accountability to agree, rather than claim this draft defines approved requirements. `writing.md` explicitly says the site does not establish EDS policy. Content ownership, the applicable lifecycle version and authoritative policy references remain unresolved and are visible as such. No EDS authority, approval body or mandatory template was invented.

The existing AI-SDLC site terminology was retained for consistency with navigation and neighbouring pages. `writing.md` proposes AI-Product Development Lifecycle as the formal project title and asks for confirmation before launch; this site-wide naming decision remains open.

The supplied public URL could not be retrieved. The repository page was the editing source. The revision adds recommendations and a fictional example, without new empirical productivity claims or research citations.

## Verification

Checked balanced HTML elements, heading order, unique IDs, internal and cross-page fragment targets, local assets, table captions and headers, and diagram titles and text alternatives. Checked the changed files for whitespace errors. The existing stylesheet and diagrams were retained; no browser visual or accessibility conformance audit was performed. No publication or deployment was performed.
