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

## Ideation collaboration and agent journeys, 18 October 2026

Reviewed `dist/product-ideation.html` against [Sumit Sheth’s From Headless to Thoughtful](https://www.linkedin.com/pulse/from-headless-thoughtful-why-3-in-a-box-operating-model-sumit-sheth-imptc/), published 18 April 2026, and the repository’s writing and design guides. The article was accessible in full. Existing uncommitted page-shell changes were retained.

### Findings and changes

- The page already covered evidence, product risks, experiments and decision ownership. Its collaboration guidance needed a working practice. Added a short shared brief and a suggested experiment rhythm for Product, Design and Engineering, while retaining specialist involvement and named decision authorities.
- Discovery did not explicitly cover an agent operating the product for a user. Added an AUX subsection with checks for context, permissions, completed outcomes, retries, recovery and human takeover. A fictional sandbox experiment makes the checks concrete. This guidance applies to products operated by agents; AI-assisted development alone does not require an agent journey.
- Connected agent journey findings to the handoff, and made continuing collaboration through implementation and production feedback explicit. Qualified the specification loop around evidence for bounded implementation.
- Added the article beside the relevant explanations and in the source list. Its collaboration and AUX framing are practitioner guidance. The detailed checks, example and feedback controls are editorial recommendations, not quotations or new EDS requirements. No automatic model retraining or expansion of permissions is implied by feedback.
- Added the subsection to both contents lists and the page map. Reused the existing responsive reference-table style for the new checks so they remain readable on mobile.

### Validation

Checked 72 local links, 36 unique IDs, matching contents lists, sequential headings and captions for all ten tables. All existing anchors and the three current figures were preserved. Headless Chromium checks passed at 1440, 768 and 320 px, with no page overflow or browser errors; enlarged text, no-JavaScript access and the keyboard skip link also passed. Visually inspected the new agent checks and collaboration content on desktop and mobile, including the stacked mobile table. The diff has no whitespace errors. Full accessibility conformance was not assessed. This review updates local source; it does not publish the site.

## Practical design workflow additions, 18 October 2026

Evaluated the user-supplied text, “AI in PDLC: 5 Practical Steps to Speed Up Product Design”, against the current ideation page and `../writing.md`. The notes supplied no author, source link or measurement context. They were treated as editorial input rather than verified evidence of performance or organisational requirements.

| Supplied point | Decision and application |
| --- | --- |
| Start with a concept brief | Adopted within the thesis section. Added a suggested brief covering evidence, outcome, proposed direction, alternatives, feasibility and falsification criteria, with ownership and a next experiment. One page is an aim rather than a mandatory template. |
| Three-in-a-box | Extended the existing guidance by naming the people covering each discipline and linking their shared brief to the experiment record. No second collaboration model or new approval authority was introduced. |
| Prototype-led customer discovery | Retained and extended with complete administrative workflows, progress, interruption and recovery. Participation follows relevant groups, access needs and decision uncertainty; ten touchpoints is not treated as a sufficient sample or universal target. |
| Two levels of design review | Adapted into focused review and targeted cross-team input, including design-system consistency, accessibility, feasibility and dependencies. The proposed 10–30 participants was omitted; attendance follows affected responsibilities. Review remains distinct from approval. |
| Check for concept drift | Added a check of changes to intent, evidence, scope, risk, estimates and the next investment decision. Evidence can justify changing direction. Earlier criteria and results remain recorded, with revised criteria agreed before the next experiment. |
| Complex administrative workflows | Added realistic tasks across screens, roles and systems, including approvals, waiting, missing information and recovery. Did not adopt the claim that user understanding is never the cause of difficulty. |
| Asynchronous collaboration | Added version-specific feedback, a question and deadline, a named decision owner and one linked decision record. Tool brands are not prescribed. AI summaries need checking; recordings remain subject to permitted use, access and retention. |
| Practical AI assistance | Added useful prototype inputs and review of generated results. Measure generation, review and correction effort alongside learning. Omitted the unsupported 60–80% contribution claim and product-specific integration claims. |

The additions use British English, direct actions, explicit ownership and measured recommendations. They extend the existing Frame–Test–Decide structure rather than creating a parallel five-step lifecycle. No new external source or EDS policy claim was added. Existing diagrams, anchors, header wording and unrelated working-tree edits were retained.

Validation passed: 74 local links, 38 unique IDs, matching contents lists, sequential headings and captions for all ten tables. All previous anchors and three figures were preserved. Headless Chromium checks at 1440, 768 and 320 px found no page overflow or browser errors; enlarged text, no-JavaScript access and the keyboard skip link also passed. Visually inspected the concept brief and scope check on desktop and mobile. The diff has no whitespace errors. Full accessibility conformance was not assessed. Publication was not part of this update.
