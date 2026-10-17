# Product pages editorial review

Reviewed 28 September 2026 against `../writing.md` and `../design.md`. Updated `dist/product-ideation.html` and `dist/product-implementation.html` in place.

## Editorial approach

Preserve the two-loop model, existing section anchors, figures and handbook layout. Make the openings explain the reader’s task; add practical inputs, evidence records, decision rules and next actions within the existing sections. Keep prose in the reading column and use the existing example treatment. No new visual system or organisational authority is introduced.

## Findings and changes

- Replaced claims of assured validation, reliability or recurrence prevention with bounded claims. Defined validation as evidence under recorded conditions.
- Clarified when to enter or revisit ideation, and when a bounded defect or maintenance issue can proceed directly to implementation.
- Added discovery prompts, the four product risks, an experiment record, a fictional worked test, and limitations on small studies and A/B comparisons. Generated personas and interviews are not user observations.
- Reconciled the ideation decisions with the handoff: commitment to a bounded scope is explicit; inconclusive evidence has a recorded next test rather than a forced verdict.
- Added evidence and decision records to the handoff. Clarified alternatives to screens for products without a UI and the continued feedback between the two loops.
- Clarified local decision rights rather than assigning investment or risk acceptance to every product owner. Distinguished the guide’s six-stage model from organisational requirements.
- Added practical independence checks, repeated AI evaluation trials, outcome and side-effect checks, grader calibration, consistent delivery measures, and rollout and recovery planning.
- Distinguished successful completion from budget exhaustion, blocked work and escalation. Corrected the suggestion that repository behaviour could override applicable policies.
- Shortened dense paragraphs and replaced repeated broad McKinsey commentary with direct practice guidance and primary sources. The existing remote McKinsey PDF could not be retrieved in this review; no claims depend on it in the revised pages.
- Retained EDS handbook attribution and its reported thresholds. Checked the local handbook text for human gates, independent proof, coverage and mutation defaults, and planned pre-production checks. This checks the summary against the supplied document, not its current organisational approval status.

## Source mapping

Online sources opened on 28 September 2026. Links appear beside the relevant explanations and in the page source lists.

| Source | Use and limits |
| --- | --- |
| [GOV.UK: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) | Users, wider journey, constraints, alternatives and continuation decision. UK delivery stages and approval rules are not adopted as EDS policy. |
| [SVPG: The Four Big Risks](https://www.svpg.com/four-big-risks/) | Value, usability, feasibility and business viability as prompts for untested assumptions. Its role assignments are not imported. |
| [Design Council: The Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/) | Existing divergent and convergent activities retained. Human decision points in the diagram are identified as this guide’s adaptation. |
| [GitHub Spec Kit: Specification-Driven Development](https://github.com/github/spec-kit/blob/main/spec-driven.md) | Specifications, plans and tasks. PRD/TRD naming remains this guide’s usage; speed claims and claims of eliminating ambiguity are not adopted. |
| [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Tasks, repeated trials, graders, final outcomes, human calibration and regression evaluation. This is practitioner guidance, not a guarantee of independent assurance. |
| [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics/) | Current five measures and application-level context. No numerical AI productivity claim or individual ranking is introduced. |
| [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) | Limited exposure and comparison with the current version. Recovery details are editorial recommendations adapted to the guide’s scope. |
| EDS AI Development Workflow: Simplified Operating Handbook, `../docs/EDS_Product_Development_Guide.docx` | Existing workflow, gates, skill statuses and default thresholds. Keep the local reference out of the public output and confirm the applicable handbook version before relying on its authority. |

The experiment fields, fictional thresholds, handoff additions, review checks and release procedure are editorial recommendations. External sources support the cited principles; they do not prescribe these examples or establish EDS responsibilities.

## Validation

The existing product browser checks passed after the final edit. They cover headings, contents anchors, cross-page links, selected navigation, figure labels and numbering, keyboard navigation, 320–1440 px layouts, enlarged text, no-JavaScript access, encoding and browser errors. The checks also confirmed the unchanged training page and shared navigation.

Visually inspected the desktop validation content and fictional experiment, and the mobile AI evaluation content. Corrected narrow wrapping in the decision table with explicit column proportions and local scrolling, then inspected the result and reran the checks successfully. Shared styles and navigation code were unchanged.

Draft status, unassigned content ownership and unconfirmed lifecycle applicability remain visible. Publication was not part of this review.


## Ideation update, 30 September 2026

Reviewed `dist/product-ideation.html` against [The Defence Product Playbook](https://defence-pp.vercel.app/), `../writing.md` and `../design.md`.

### Content changes

- Added three conditions that suit a product approach to "Know when to enter or revisit ideation", and noted that stable requirements may suit conventional planning.
- Added a section, "Write a problem statement worth solving": 6W questions, a 4C check table, four traps with fictional wording, a fictional before-and-after statement, and SFR prioritisation. The thesis now builds on this statement.
- Added "Make the theory of change visible" to the thesis section.
- Aligned the Double Diamond explanation with the playbook's framing: the first diamond closes on a problem statement, the second on a bounded scope.
- Added the TEST habits and the playbook's proof-of-concept and proof-of-value reference points, presented as reference points rather than targets.
- Added single-line accountability and three enabling conditions to the product team section. The playbook's role names (Ops Manager, two-in-a-box) and committees are not adopted; readers are asked to map the principle to local roles.
- Added the metric ladder, metric rejection criteria, SMART, the value-cost ratio and a stalled-metric diagnosis table to the measurement section. The layer table now shows each layer's rung. "Escalate to the Steering Committee" became "Escalate to whoever can clear it" to avoid assigning an unconfirmed body.
- Added the problem statement, value metric and baseline to the handover package and readiness checks.
- Added the playbook to the source list and updated the review date.

### Figures

- New Figure 3: theory of change, four linked steps with the three assumptions between them.
- Figure 4 (Double Diamond, formerly Figure 3): decision nodes now read "Passes the 4C check" and "Commit or change" instead of "Product owner decides", so the figure no longer assigns a role.
- New Figure 6: metric ladder, with the value metric as the single blue emphasis.
- Renumbered Figure 5 (product intent). All figures keep a caption, a text alternative and an adjacent prose explanation, and use the existing diagram tokens.

### Limits

The playbook describes itself as a EDS guide. This review did not confirm its organisational status, so the page cites it as a source and does not present its guidance as policy. The playbook's interactive tools (4C scorer, VCR calculator, team explorer) were not reproduced; the site's design standard prefers static, predictable content.

### Validation

A headless Chromium check at 1440, 1100, 768 and 320 px passed: no page overflow, no broken anchors or duplicate IDs, sequential headings, figure and region labels numbered 1–6, every SVG linked to its title, no SVG text outside its viewBox, crowding its box or overlapping other text, all tables captioned, no console errors, and the first Tab reaches the skip link. Figures 3, 4 and 6 were inspected visually.

## Ideation qualifications, 17 October 2026

Updated `dist/product-ideation.html` against the supplied review comments, retaining the existing layout and section anchors.

- Limited severity–frequency–reach scoring to a prioritisation aid for discretionary improvements. Added overrides for mandatory obligations and intolerable risks, including mission failure, serious harm, security and accessibility.
- Reframed end-of-life concerns around current and foreseeable consequences. Teams can address loss of support, security maintenance or recoverability before user-facing failure.
- Distinguished resource inputs from operational reliability and usage measures. Explained uptime as a possible guardrail, service outcome or contributor to mission value, depending on context.
- Retained satisfaction, perceived effort and trust as potentially meaningful outcomes, triangulated with behavioural and operational evidence and explicit sampling limitations.
- Preserved attribution of the playbook's outcome/annual-cost ratio while qualifying it as an efficiency measure. Financial ROI and comparisons across different outcome units need further justification. A plateau does not remove the value of essential maintenance or obligations.
- Added a safety check before creating or running prototypes: permitted data, approved tools, participant information, access restrictions and prototype disposition. Linked the check to the experiment record and handoff.
- Distinguished evidence for investigation, bounded implementation and production release. Qualified the prototype table and handoff so prototype success does not imply production readiness.

These qualifications and safety checks are editorial recommendations responding to the review, not newly verified quotations from the playbook or new organisational policy. The public ideation URL could not be retrieved by the web tool; the review used the repository's publishable HTML.

Validation passed: UTF-8 decoding; all 68 links checked for local destinations and anchors where applicable; unique IDs; sequential heading levels; all nine tables captioned; and no whitespace errors in the diff. Headless Chromium checks at 1440, 768 and 320 px found no page overflow or browser script errors and confirmed the safety check and three decision labels. External link availability and full accessibility conformance were not assessed. Publication was not part of this change.
