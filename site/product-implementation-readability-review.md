# Product Implementation readability changes and review

Reviewed 7 November 2026. Scope: `dist/product-implementation.html` and its local presentation. This record assesses each edit after applying it, against issue #30 and the critical analysis in the accompanying chat. Assessments are editorial checks, not observed reader-comprehension results.

## Starting evidence

- Browser inspection of the published page confirmed that all seven main journey chapters contain visible text; the independent verification chapter already includes a defect, correction and retesting. The chapters are not hidden inside closed disclosures.
- GitHub records PR #20 as merged on 6 November 2026. Issue #30's draft-PR premise is stale.
- Platform capabilities, platform principles and autonomy already occupy the optional toolkit. AI evaluation mechanics were still in core assurance guidance.
- TRD, software factory, fitness function and canary already had definitions. Retain those explanations and improve remaining terms in context.
- Preserve the six activities, independent verification, acceptance/release distinction, five DORA measures, established anchors and technical references. Existing Discovery edits in the working tree are outside this change.

## Change 1 — Make the product contribution explicit

**Intent:** a product contributor can distinguish their work, engineering work and decision authority at each activity.

**Change:** replaced the existing six-activity table with product responsibilities, engineering/assurance responsibilities and evidence/next decisions. Clarified the reader role and Maya's role as a project-manager user of the application.

**Review after change:** the six rows retain Plan, Slice, Implement, Verify, Release and observe, Learn. Each names a concrete product action and an engineering action. Acceptance and release authority are explicitly separate; role allocation remains local. On rereading, the initial Plan row implied an extra design approval gate. Revised it to an engineering readiness check with unresolved risk referred to the applicable authority.

**Assessment:** meets the editorial intent after correction. Actual organisational role allocation still needs the applicable team procedure; the table does not create that allocation.

## Change 2 — Explain checks and decisions in plain language

**Intent:** the reader can identify the input, comparison, evidence, decision maker and failure route without translating abstract governance nouns.

**Change:** replaced the governable-transitions list with a concrete check/rework sequence; defined traceability through linked records. Replaced Figure 2's text alternative with a who/evidence/decision table. Rewrote Figure 1's text alternative as six ordered activities to remove competing numbering. Explained characterisation and mutation testing in context.

**Review after change:** a failed criterion returns for correction and independent retesting; an unclear criterion returns to Product, Design and Engineering. The alternative table retains blocking findings, unresolved disagreement, exception referral and separate release authority. An exception request does not authorise release. The Plan wording no longer implies a new universal approval gate.

**Assessment:** meets the editorial intent. Browser checks of table access, diagrams and narrow layouts are recorded below after the full edit.

## Change 3 — Keep the story readable through technical planning

**Intent:** a product contributor can follow requirement → technical choice → tasks → independent verification without needing AWS service knowledge.

**Change:** replaced the main journey's service catalogue with the decisions that protect saved responses and distinguish task, notification and response status. Added four task groups with expected checks. Moved the complete Java/React/AWS design and detailed tasks into an optional engineering supplement. Preserved the original technical anchors and corrected main-story continuation links. Removed competing numeric prefixes from journey headings.

**Review after change:** the shorter story still explains background processing, shared manual/scheduled rules, duplicate prevention, saved responses and task dependencies. The complete service design, outbox, queue delivery semantics, retry/recovery details and detailed tasks remain available. An anchor comparison found no removed IDs. The build chapter now explains that the developer's simulated-store test omitted the real database/dashboard integration; the independent failure chapter explicitly tests that omitted integration.

**Assessment:** meets the editorial intent. The new explanation resolves the apparent contradiction between an earlier passing retry test and the later retry failure. Evidence remains fictional; it does not assert a real test was run on an application.

## Change 4 — Separate essential AI decisions from evaluation mechanics

**Intent:** product contributors understand their responsibilities for AI behaviour without having to learn evaluation tooling before following delivery.

**Change:** rewrote the AI-product note around variable outputs, unacceptable mistakes, affected users, permitted data use and human fallback. Retained core checks for agent-produced changes and actual tool actions. Moved the complete repeated-trial/evaluation material to a labelled optional section, with definitions for tasks, trials, grading and grader calibration. Explained MCP and sustained operability where they occur in the toolkit.

**Review after change:** the main route still distinguishes AI-assisted development from an AI product. Product acceptance rules remain in core reading; evaluation mechanics remain available through direct links. No AI capability was added to Maya's pilot. The original evaluation guidance and reference remain present, with attribution pointing to the relocated section. Rereading identified that “AI responses” was too narrow for AI influencing decisions; broadened the note to AI output affecting product behaviour and retained permitted data use explicitly.

**Assessment:** meets the editorial intent after correction. This edit does not certify an actual AI product or evaluation design.

## Change 5 — Demonstrate evidence-to-decision reasoning

**Intent:** the reader can interpret a quality report and delivery measures without mistaking an aggregate score for acceptance, product value or permission to release.

**Change:** added a fictional two-candidate quality report in the main verification chapter, including green automation, a blocking independent failure, correction, retest and separate release status. Summarised documented Eitri defaults in five items, linked to the maintained readiness, build, closeout and pipeline procedures. Added a five-measure DORA comparison with explicit periods, counts, calculations, a local improvement target, product guardrail and next investigation.

**Review after change:** candidate A remains blocked despite 86% coverage and a 74% optional mutation score. Candidate B's passing checks support acceptance of its scope, with release still awaiting a separate decision. Defaults preserve 80% coverage and optional/recommended 70% mutation testing; closeout steps remain subject to their documented statuses and repository configuration. The example establishes a new service's delivery baseline after launch and separates it from the spreadsheet product baseline. Recalculation confirms 2/8 = 25%, 2/10 = 20%, and 8/4 = 2 versus 10/4 = 2.5 deployments per week. Recovery durations support the stated medians. Both periods have two failed deployments: the text does not infer fewer incidents, improved product value or AI causation from the lower rate.

**Assessment:** meets the editorial intent. All added results, times, targets and report roles are explicitly fictional. Actual harness configuration, policy applicability and real operating measurements remain outside this editorial verification.

## Change 6 — Make future reviews test the intended learning

**Intent:** a review can show what changed, why it helps and which evidence supports the assessment, without treating subjective scores or browser checks as measured comprehension.

**Change:** added task-based teaching-review guidance to `../writing.md` and this per-change record. Each change records its intended reader action, implementation, reread, correction and remaining limits. Added the reader-session protocol below.

**Review after change:** the record distinguishes live observation, editorial interpretation, proposed examples and human evidence. It corrects stale premises rather than silently implementing them. The writing guidance requires a dated/revisioned review target, checks of actual behaviour and related work, and a full-journey reread. It explicitly prevents reporting agent answers as human-reader evidence.

**Assessment:** meets the review-process intent. Human comprehension remains unverified until actual readers attempt the tasks.

## Representative-reader session to run

Recruit aspiring product contributors who have not written this page. Give them the page without explaining the answers. Ask each participant to point to the evidence used, and record their answer, hesitation, navigation path and any assistance. A small session guides the next edit; it does not estimate population-wide comprehension.

| Task | Expected evidence and answer | Interpretation of a failure |
| --- | --- | --- |
| Follow the saved-response requirement into a design choice, task and test. | Main Chapter 3 and Verify: retain saved responses during repeated processing; test interrupted processing against stored data and the dashboard. | The requirement/design/task relationship still needs explanation or a better link. |
| Candidate A's automated checks are green. What happens next? | The quality report records an independent acceptance failure; return for correction and retest. | Evidence hierarchy or the blocking decision remains unclear. |
| Candidate B is accepted. May it go live? | Release remains subject to a separate authority's readiness, rollout and recovery decision. | Acceptance and release are still being conflated. |
| What does a product contributor do during Plan and Verify? | Clarify behaviour and disputed criteria, check coverage of intended user behaviour; Engineering designs and independent assurance reproduces checks. | Responsibility labels or role assumptions need revision. |
| Route a hidden saved report and a finding that members cannot identify their equipment. | The hidden report is an implementation defect; inability to identify equipment challenges the product assumptions and reopens discovery. | The two feedback routes remain unclear. |
| Did the DORA example show fewer failed deployments or prove AI helped? | No: two failures occurred in both periods; the denominator changed and no causal AI comparison was made. | The worked measurement explanation still encourages an unsupported inference. |

Suggested local completion criterion: every critical decision task is answered without corrective coaching; investigate and revise any consequential misunderstanding. This is a proposed editorial criterion, not an organisational delivery gate.

## Integrated review and validation

The browser review exposed a presentation defect in the first edit: the responsibility table's final decision column required horizontal scrolling at the normal desktop reading width. Corrected all four new decision/evidence tables to fit the desktop column, wrap headings and use the site's existing labelled stacked-row treatment below a 700px content width. Kept semantic table, row and header roles. Rechecked the affected layouts after the correction.

Moving the detailed technical design also required a behaviour change: the implementation-page anchor handler now opens the target's enclosing disclosures before positioning it. Original `asset-plan`, `asset-slice` and notification-task anchors retain their detailed content. Main-story continuation links point to the shorter explanation. Source attribution links for AWS now point to the engineering supplement. Removed the old 7–12 continuation numbering from the handoff list and heading prefixes, leaving the seven chapter labels as the story's navigation.

The final raw-HTML check caught a mismatched closing list tag introduced while removing that continuation numbering. Corrected the opening list tag and reran the structural checks; do not rely on the browser repairing malformed markup.

Completed checks:

- Balanced raw HTML; 69 unique IDs; all 62 original IDs retained; 155 relative links and asset references in the edited page resolve. All original external link destinations remain present. The repeatable static check and JSON result are in the ignored `.preview/check-issue30-static.cjs` and `.preview/issue30-static-validation.json` files.
- Browser inspection confirmed all seven main chapters remain outside closed disclosures. The engineering supplement starts closed and its full content remains in the HTML.
- At the normal 1280px browser width, the new activity table fits its 759px reading column without sideways scrolling. At 375px and 320px, new evidence tables stack into labelled rows and the page has no horizontal overflow. Visually inspected the desktop activity table, mobile quality report and mobile DORA example.
- Enter opens Figure 2's text alternative, exposing its five-row who/evidence/decision table. Enter on the engineering-detail link reveals the supplement. A fresh load at `#asset-plan` opens the relocated content and positions its heading below the sticky header.
- The browser error log contained no errors during these checks. JavaScript syntax validation passed for `product-implementation.js`.
- Reviewed the existing print handlers: the new engineering disclosure uses the existing supplement selector that opens for print and restores closed state afterwards. Added print sizing for the new tables. Actual print rendering and a JavaScript-disabled browser session were not exercised in this pass; those remain verification limits, not claimed passes.

**Final assessment:** all six changes meet their stated editorial intent after the recorded corrections. This is supported by a passage-by-passage reread, preserved-content/link checks and the focused browser checks above. It does not establish measured comprehension or certify real release readiness. The representative-reader tasks remain pending.
