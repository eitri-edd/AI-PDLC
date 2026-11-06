# Asset management learning journey review

Reviewed 6 November 2026 against the current writing and design standards. The AI-SDLC overview remains a general explanation of the lifecycle. Project Discovery and Product implementation carry one continuous fictional asset-management journey.

## Findings and resulting changes

The previous version used invented pointer codes throughout the story, repeated handoff detail and mixed fictional evidence into blue topic diagrams. Those patterns made readers decode labels before understanding the method.

The revised journey follows Maya, the project manager, and Alex and the other project members. It uses descriptive names such as the first usability test, the annual-declaration requirement and the retry check. Existing technical anchors remain intact. The main panels now lead from a concrete task to the method, evidence, decision and next action; supporting method examples remain concise and separately labelled.

The supplied starting problem remains unchanged: managers use spreadsheets for assignments; members cannot directly record handovers, loss or faults; managers manually initiate annual asset checks. The proposed application supports ongoing reporting and an automatically scheduled annual declaration with manager follow-up. The names and follow-up research/test outcomes are explicitly fictional.

## Continuous journey

| Part | What the example teaches |
| --- | --- |
| Understand the problem | Use the six questions and four checks to investigate reporting gaps, distinguish observed mismatches from causes and choose further research. The illustrative walkthrough checks 20 records with eight members, finding six custody mismatches and three fault reports outside the register. |
| Compare responses | Compare spreadsheets/messages, a controlled form, platform configuration and a dedicated app against the same need. State the theory of change and retain alternatives. |
| Plan the test | Ask eight members to hand over a monitor, report a faulty laptop and respond to an annual task for an item they cannot find; have the manager review the queue. Technical and cost investigations answer separate questions. |
| Learn from failure | Six of eight complete all tasks correctly; unclear exception choices lead to false healthy confirmations. Improve the flow rather than attributing blame to members. |
| Decide | The revised test reaches eight of eight, with scripted exceptions visible to the manager. Review repeated-participant limitations, sandbox findings, cost and follow-up capacity before funding a bounded pilot. |
| Prepare delivery | Carry descriptive requirements, screens, evidence, acceptance checks, unknowns and measurement work into implementation. The first slice covers member changes, yearly declarations and manager action together. |
| Plan and slice | Record the technical approach and split import/assignment, member reports, annual declarations and manager review/measurement into reviewable tasks. Preserve the intended behaviour across those tasks. |
| Build and verify | Independently retry the implemented yearly worker after a faulty declaration is saved. A duplicate task hides that response in the manager summary; correction is followed by fresh checks of the actual saved records and summary. |
| Release and learn | Limit initial exposure, rehearse reconciliation/recovery and compare product outcomes with a baseline. Route code defects to delivery and challenged product assumptions back to discovery. |

Custody means the current holder. Member declaration, physical sighting, repair completion and write-off authority remain distinct. Report unresolved lost/faulty cases and overdue replies alongside completion; do not claim annual effectiveness from advancing a sandbox clock. Actual baselines, numerical pilot targets and applicable organisational authority still need confirmation for a real project.

## Diagrams and visual treatment

- Rebuilt three blue discovery diagrams as general explanations: investigating a problem, connecting outcomes/opportunities/responses/tests, and tracing a change into its acceptance checks. They contain no fictional names, asset records or sample results.
- Added a matte diagram inside the discovery journey showing the ongoing member-reporting path and the scheduled annual path joining the manager’s follow-up queue.
- Added a matte implementation diagram showing the expected retry behaviour, observed failure, correction and independent retest.
- Implemented the Matte Stone palette in shared components, including disclosures, applied table/list snippets, captions, nodes and legends. The fictional content uses flat fills and charcoal text; navigation and focus retain their normal affordances.
- Updated the shared enhancer to leave learning diagrams static, with no blueprint gradients, flow pulses, hover elevation or playback toolbar. General topic figures retain their existing explanatory controls.
- Preserved the twelve experiment methods, six discovery frameworks, technical and agent-journey checks, and the implementation practices. All 88 applied reference/list snippets use descriptive text in separate matte blocks.

## Verification

- Checked all 930 local links and asset references across the 13-page site, including fragments and preserved anchors.
- Passed 26 sitewide desktop/mobile loads after shared-style and script changes, without page overflow or browser errors.
- Checked the three target pages at 1440, 768, 375 and 320 pixels with disclosures collapsed and expanded. Checked heading order, matching contents lists, captions and table cell counts.
- Checked topic/example separation, absence of visible invented pointer codes, SVG view-box and node text bounds, flat example fills, charcoal text, no shadows/animation and no example playback controls.
- Checked all six discovery links, cross-page continuation, implementation heading targets below the sticky header, print disclosure restoration and reading without JavaScript.
- Passed enlarged-text checks on all three pages and inspected static example content in print.
- Visually inspected desktop problem framing, generic topic flow, application flow and retry diagrams, plus mobile application and method-reference layouts. QA scripts, reports and screenshots are in the ignored .preview directory.

The initial review did not revalidate external sources or publish or commit the work. Unrelated pre-existing exercise assets were preserved. Existing content-owner and organisational lifecycle-version confirmation gaps remain as recorded in earlier reviews.

A representative-reader session has not been run. Suggested tasks: ask a product contributor to use the six questions and choose the next asset experiment; ask an engineer to find the yearly retry requirement, expected result, failure evidence and release decision route. Check whether each can follow the descriptive records across both pages and distinguish member declaration from physical sighting. No human-reader findings are claimed.

## Follow-up editorial review

On 6 November 2026, revised the 114 main and compact examples across the two product chapters for natural language, concrete actions and consistent SDLC terminology. All 116 example labels, including the two diagram labels, now include descriptive titles. Groups of three or more parallel items use bullet lists. The writing standard records these rules and the preferred names “Project Discovery” and “pilot project”.

The implementation example now carries one annual-verification user story from PRD scope and acceptance criteria into a TRD and small development tasks. The illustrative TRD retains Java/Spring Boot and React and uses AWS services for hosting, storage, scheduling, queues and notifications. Official AWS references support the SQS, EventBridge Scheduler, SES, ECS/Fargate and CloudFront explanations. The retry design retains idempotent processing, a transactional outbox, visibility-timeout handling and dead-letter queues. Confirmation testing and regression testing have separate explanations with an ASTQB reference.

Focused rendering checks passed at 1440, 768, 375 and 320 pixels, with disclosures collapsed and expanded. Checked original anchors, example links, heading order, table structure, text wrapping, enlarged text and reading without JavaScript. The final site checks are recorded in the ignored `.preview/learning-redesign-validation.json` and `.preview/aws-asset-validation.json` files. These are automated and visual editorial checks; no human-reader study is claimed. The unused exercise assets remain outside the pull request.
