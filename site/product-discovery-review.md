# Product discovery merge review

## Issue 29: changes and review after revision, 7 November 2026

Prepared a local revision of [Project Discovery](dist/product-discovery.html) against [issue 29](https://github.com/eitri-edd/AI-PDLC/issues/29). The issue's readability scores are editorial judgements; this revision does not treat them as measured comprehension. No GitHub comment, commit, publication or issue update forms part of this change.

Each item below records the intended improvement, actual revised wording or structural change, and the assessment after rereading it with the surrounding section. **Text intent met** means that the revised content supplies the explanation or action identified here. It does not mean that an aspiring PM has demonstrated comprehension. The representative-reader check required by `writing.md` remains pending.

### 1. Human judgement and the shared environment

**Intent:** show who does the work, what AI contributes, and who checks or decides.

**Changed:** the optional responsibility table now starts with a labelled Maya illustration: “AI groups Maya’s interview notes. Product checks the findings against the original notes; Engineering checks claims about permissions.” Specialist responsibility cells use questions about building, changing direction, data, dependable results and rules. The environment list asks where current information lives, what the agent may change, where work is visible, who reviews it and who can approve consequential actions.

**Review after change — text intent met.** A reader can assign a reviewer and identify the next investment decision without interpreting “runtime controls” or “control mapping”. Technical responsibilities and local decision authority remain explicit. The reference remains optional; the core role descriptions still stand independently. Real role assignments need the organisation's own arrangements.

### 2. AI-assisted development versus an AI product

**Intent:** let readers identify when additional agent-journey checks apply.

**Changed:** “Using AI to summarise Maya’s interviews is AI-assisted development. Adding AI that interprets members’ fault reports makes AI part of the product: an AI feature.” A separate sentence covers agents operating the product, including an external agent using software that contains no AI itself.

**Review after change — text intent met.** Development assistance, product AI and agents acting through a product are distinguishable. The previous sentence's restricted “only products with agents” implication is removed. The example does not assert that Maya's planned pilot contains AI; it illustrates the distinction conditionally. Applicability points directly to the agent checks.

### 3. Twelve-method catalogue

**Intent:** help a new PM choose the next test without learning twelve methods first.

**Changed:** moved the complete, already-collapsed catalogue from Step 3 into the optional reference toolkit. Kept a descriptive link from Step 3 and moved both contents entries into the toolkit's position. The core retains the four-risk questions, practical starting methods and their evidence limits.

**Review after change — text intent met.** Readers can proceed from uncertainty to a test without opening the catalogue. All twelve methods, source links, limits and the published `experiment-methods` anchor remain. The review does not claim that this material was previously fully expanded or compulsory. The core still explains that a small exploratory comparison cannot establish a population effect or settle every risk.

### 4. Arrangements for running and closing a test

**Intent:** translate data and access requirements into questions a PM can resolve before testing.

**Changed:** a fictional example starts with asset records, simulated actions, isolation from the live register and ownership of research access. The checklist asks: “What information may we use?”, “May this tool receive the information?”, “What will participants be told?”, “What can the prototype change?” and “Who closes the experiment?” Synthetic data and retention are explained in everyday language.

**Review after change — text intent met.** The experiment owner can take these questions to the appropriate specialists and record answers. Consent or other applicable participation requirements, withdrawal, provider handling, permissions, stop conditions, expiry and production checks remain. The text says fictional records can test an interface but do not establish real user behaviour; using safer test data does not become a substitute for research.

### 5. Step 6 measurement plan

**Intent:** make it possible to prepare a measurement plan while retaining enough precision to interpret the result.

**Changed:** five visible questions cover the useful result and counted cases, baseline and target, collection and ownership, unacceptable results, and review decisions. They link to Maya's completed planning example. Detailed fields sit in an optional “define and check the measurement record” disclosure. Numerator, denominator and instrumentation are explained where they appear.

**Review after change — text intent met; operational values remain to be agreed.** The first pass is an actionable set of questions rather than a dense collection specification. The detailed record still covers exclusions, failed attempts, source dates, missing baselines, duplicate counts, access, owners, comparisons and actions. Its collapsed state is not permission to omit necessary collection work; the handoff check still requires definitions, owners and collection plans.

### 6. AI-assisted findings and provenance

**Intent:** explain what to retain and why, without making the handoff a collection of unexplained metadata.

**Changed:** “AI suggests that members misunderstand asset status. Design checks the relevant interview passages and records which observations support or contradict the suggestion.” The accompanying instruction joins the finding, source passage or controlled link, reviewer, relevant AI setup and decision.

**Review after change — text intent met.** A finding is linked to the original observation and the requirement it changes. Tool versions and instructions have a purpose: investigating how a material generated claim arose. Sensitive originals remain controlled rather than being copied into every document. Generated scenarios and rejected interpretations remain distinct from user evidence. This explains provenance without claiming reproducibility from a version number alone.

### 7. Technical assumptions and spikes

**Intent:** help the PM commission and interpret a technical investigation rather than perform it without Engineering.

**Changed:** Step 3 defines a spike as “a short technical investigation to answer a specific question” and connects it to handover permissions. The technical reference starts with “What could prevent this solution working, and what small test would tell us?” Response time explains latency; the TRD appears as the destination for findings during technical design.

**Review after change — text intent met.** The PM can agree the question, time limit and decision. Engineering remains responsible for the technical method and evidence. The reference preserves tests of denied actions, actual dependencies, failure, recovery, cost and AI comparisons. A simulated interaction is explicitly distinguished from testing the real connection. Deep-linking to the technical reference remains supported.

### 8. Frameworks table

**Intent:** make the library useful for lookup without requiring a framework-selection exercise.

**Changed:** the introduction says, “You can use the six steps without choosing a named framework.” Each framework row starts with a question, such as “Are we choosing a solution too early?” and “How do we connect needs, options and tests?” The framework names, source links and working artefacts remain.

**Review after change — text intent met.** A reader can identify why to open a row and can skip the section entirely. The table remains a specialist reference and is still long when expanded; this revision does not claim to turn it into introductory reading. It preserves continuous collaboration, rather than implying separate discovery and delivery teams.

### 9. Agent journeys / AUX

**Intent:** explain agent interaction through a recognisable task before introducing the specialist label.

**Changed:** the reference starts with an agent drafting Alex's fault report. It asks whether Alex can check the asset and description and whether the agent checks for success before retrying after a timeout. “Task and information” and “human takeover” replace less familiar row labels. AUX is defined after the example.

**Review after change — text intent met.** The reader can recognise permission, duplicate-action and takeover failures. The section remains conditional on an agent operating the product. Its existing checks of missing information, denied access, partial completion, resulting system state and variable behaviour remain. A human-looking draft or successful API request is not presented as proof that the complete task succeeded.

### 10. Advanced intent, decision and requirement linking

**Intent:** show why linked records help before discussing machine-readable formats.

**Changed:** an example connects members choosing the wrong status, revised response choices, the requirement to preserve answers and the acceptance check on Maya's queue. The general instruction says, “A reviewer should be able to follow a requirement back to its reason and evidence.” Automatically checked records have a separate optional subsection.

**Review after change — text intent met.** The benefit is intelligible without knowing schemas or policy languages. Version ownership, conflicting requirements, source checks and decision records remain. Machine-readable records are described as checking specific conditions, not as understanding the user need or proving that the requirement is correct.

### 11. Measurement vocabulary and uptime

**Intent:** use stable meanings across selection, testing, handoff and later review.

**Changed:** the core defines value measure and North Star, then calls relevant behaviours “supporting measures” and effort/funding/compute “resources”. It explains the external term “input metric” once. The ladder uses resources invested, supporting measure, user-value measure and organisational outcome. It explicitly describes different questions rather than ranks of evidence strength. Uptime is illustrated as an asset-service reliability guardrail, with the broader contextual qualification retained in the source adaptation.

**Review after change — text intent met.** The guide no longer teaches two operational definitions of input. It does not claim uptime is always a guardrail, that usage proves value or that a higher ladder position establishes causation. Maya's candidate value measure is not declared an established North Star. The original page already explained the terminology distinction; the revision reduces the burden of remembering it rather than claiming to repair a proven technical contradiction.

**Measurement example review:** the case now separates record accuracy from resolution of reported problems. Additional explicitly fictional planning figures show 72 correct records out of a fixed roster of 100, an illustrative target of 90%, a four-week review, supporting handover acknowledgements, guardrails and named collection/review roles. An 86% result is conditional, not an invented observed outcome. The original eight-member study and annual-cycle limits remain separate. Real baselines, target justification and operating thresholds are deliberately left to the team before release.

### 12. Sources and attribution

**Intent:** preserve verification and attribution without presenting source history as another lesson.

**Changed:** collapsed section-attribution and adaptation notes in the existing final Sources section. The numbered bibliography remains visible, with every existing external source URL, reference number and ID retained. Material limitations stay beside the claims they qualify.

**Review after change — text intent met.** A reader can skip adaptation history or inspect it deliberately. Direct links to the measurement adaptation reveal the disclosure. Source prose was already at the end, so this is a small reading-path improvement rather than a major content correction. No external source was deleted and no new source-check date was invented.

### Review of the nine near-misses

| Pointer | Actual change | Assessment after the change |
| --- | --- | --- |
| Concept brief / draft PRD / evidence-backed PRD | Introduced the progression as why to investigate, behaviour worth testing and scope to build; explicitly avoided three compulsory document gates. | Text intent met: the table retains maturity and evidence expectations without adding an approval sequence. |
| North Star definition | Defined value measure before North Star; used accurate asset records as a candidate, linked to the completed case. | Text intent met: a feature-level target and an established product North Star remain distinct. Reader classification still needs observation. |
| Measurement thread | Replaced the abstract arrow chain with actions at selection, test planning and handoff, all pointing to the same case record. | Text intent met: readers can locate the next action and see why prototype results are separate. |
| SVPG four-risk note | Put four plain questions before the established labels and attribution in Step 3. | Text intent met: value, usability, feasibility and viability remain separate; the tests are alternative starting points. |
| Independent judgement | Named comparison with original observations, another explanation, limits and the treatment of unsupported claims. | Text intent met: the reviewer has a method; no new approval board or universal gate is invented. |
| Investigation / implementation / release | Added the questions of funding learning, funding the scope and permitting the implemented version into use. | Text intent met: funding a pilot remains separate from releasing it. The existing evidence table is preserved. |
| Human approval and risk tolerance | Specified permissions and approval points before action; exceeding a boundary stops work for referral. Approval cannot make a prohibited action permissible. | Text intent met: the action and escalation route are concrete. Actual authorities and limits remain local. |
| Figure 6 traceability | Added a wrong-status → distinct-answer requirement → saved-answer check in the case and linked it to the existing figure. | Text intent met: there is a concrete chain, and the topic diagram retains its accessible text equivalent. |
| Frameworks introduction | Stated that the six steps work without selecting a framework and made the table question-led. | Text intent met: frameworks are optional aids rather than extra stages. |

### Shared changes and second-pass corrections

- Moved the existing Maya introduction before roles and method, retaining its `worked-example` anchor and the six-chapter case. Short examples use the existing lavender treatment. Detailed cases remain separate from the general blue diagrams.
- Replaced the six existing Output/Next panels with PM action, record, next decision and readiness summaries. This reuses the existing panels rather than stacking six additional callouts.
- On rereading, the first draft's test-stage summaries only named owners. Revised Steps 3 and 4 to say what the PM agrees or checks.
- On rereading, “Maya needs dependable records” blurred a need with an outcome. Revised the case to describe the desired change separately from members' reporting difficulty and possible concepts.
- Split the Step 5 opening into the evidence comparison and the next investment action. Preserved Commit / Continue / Improve / Redesign / Pivot / Defer / Stop and their return routes.
- A link check found a newly mistyped Figure 6 anchor; corrected it to the existing `fig-stack` ID. Visual inspection found the relocated introductory panel's direct link could sit under the fixed header; added a page-specific scroll margin and checked it again.
- Kept diagram text alternatives rather than deleting accessible explanations to meet a word-count goal. Kept source mappings and all existing safety/evidence qualifications in moved references.

### Verification and remaining reader check

The browser and link verification results are recorded in `.preview/issue29-validation.json`. They cover 100 preserved IDs, all local page links and assets, balanced HTML, matching contents, the catalogue's placement, desktop/mobile layouts with references closed and expanded, direct links, header clearance, diagram text equivalents, print restoration, enlarged text and use without JavaScript. Screenshots of the introduction, measurement questions, mobile measurement example and framework reference were visually inspected. Whitespace checks cover the tracked changes.

**Representative-reader verification remains pending.** Following `writing.md`, ask a reader with delivery experience who is learning product management to do these tasks with the revised page:

1. Distinguish Maya's desired outcome, the researched opportunity and two possible concepts.
2. Select a test for the largest uncertainty and explain what it would leave unresolved.
3. Use the fictional measurement record to explain the denominator, why 86% misses the target and why 90% does not override unauthorised changes.
4. Explain why eight successful prototype tasks do not establish production readiness, population benefit or a causal improvement.
5. Identify their next action and the person who decides whether to fund it.

Record the reader's answers, hesitations, missing information and requested help. Revise any passage that fails the task. An author self-review and browser checks cannot substitute for this evidence, so the issue's comprehension intent is not marked fully verified.

## Writing standard refinements from issue 29, 7 November 2026

Reviewed the lessons above against the current [writing standard](../writing.md), including the task-based teaching-review section already added during the Product implementation work. Extended that section rather than duplicating its review protocol. These are house editorial choices drawn from the revisions, not new externally validated findings or organisational delivery requirements.

| Lesson from the change and reread | Refinement to the standard | Assessment after refining the rule |
| --- | --- | --- |
| A responsibility label did not explain the PM's contribution to a specialist test. | Distinguish work readers perform, commission and review; require the action and use of the result. Improve existing summaries before adding boxes. | Covers the actual failure without imposing a six-field template on every paragraph. |
| Separation of theory and examples could be read as forbidding a helpful early scene. | Permit a brief labelled case introduction and a compact example beside a difficult distinction, while keeping general instructions independent. | Resolves the tension between familiar-problem-first teaching and separate reading paths. It does not require Maya in every section or every page to start with a story. |
| Optional reference material was mistaken for compulsory core reading, while some technical checks were still essential. | Judge placement by the next reader action. Keep purpose, applicability, essential limits and next action visible; link question-led choices to detailed references. | Preserves applicable checks and technical precision. A collapsed panel alone neither establishes a defect nor makes its content unnecessary. |
| Existing definitions were present but did not resolve confusion between neighbouring concepts. | Contrast easily confused terms through the same task; reuse existing definitions and examples before adding another glossary. | Targets understanding of relationships rather than definition count. |
| Two sources' meanings of input increased the reader's burden; uptime was not universally misclassified. | Choose stable guide terminology, map source usage in adaptation notes and identify context-dependent classifications. | Prevents alternating definitions without declaring every vocabulary difference a factual error. |
| Separate metric passages did not teach a complete measurement decision; new numbers could resemble actual findings. | Teach one record from benefit through calculation, population, baseline, target, collection, result and decision. Distinguish observations, targets and conditional fictional results. | Retains denominators, provenance, owners, guardrails and evidence limits. The rule applies when teaching measurement, rather than requiring a full measurement tutorial around every reported number. |
| Replacing diagram prose wholesale could remove an accessible explanation. | Allow an adjacent table or list as the text equivalent only when it preserves relationships, choices and return routes. | Supports reducing duplication while preserving accessible meaning. |
| An edit could exist without fulfilling its intended teaching action. | Extend the existing per-change review rule to link the changed passage, explain the assessment, record corrections and reassess them. Strengthen the reader-evidence checklist. | Keeps editorial review, structural checks and observed human comprehension separate; pending reader work cannot be reported as a pass. |

Rereading the standards edit found two scope problems. Moved the measurement subsection after the general source and policy rules so it did not accidentally contain them. Narrowed its checklist item to passages that teach measurement, avoiding a new requirement to expand every numerical example into a tutorial. Rechecked the reading-path rules against familiar-problem-first guidance and the independent-playbook requirement; the compact example is an aid, not a dependency.

Preserved the existing terminology table, source URLs, organisational-authority boundary and representative-reader requirement. Checked Markdown headings, local document links, retained source references and whitespace. This standards change makes no new claim that the revised pages have passed a human-reader session.

## Targeted writing review, 4 November 2026

Refined the requested sections against `writing.md`, with concrete inputs, actions, evidence checks, recorded outputs and next decisions.

- Expanded each 6W question into research prompts and each 4C check into an assessment readers can perform. Retained the distinction between observed difficulty and an unconfirmed cause, including a route for further investigation.
- Explained the four weak substitutes with fictional statements, why each is incomplete and what to investigate next. Retained planning for foreseeable end-of-life risks before a service failure.
- Rewrote step 2 as “Choose a user need and compare solutions”. Separated opportunity importance from assumptions about a particular solution's effort or feasibility. Made the comparison, evidence limits and return routes explicit.
- Rewrote the experiment-record guidance as “Record the test plan and decision criteria”, including ownership, measures, inconclusive outcomes and links to test arrangements. Expanded “Match the test method to the uncertainty” with questions, methods, observable signals and limits.
- Rewrote step 6 as “Agree what to build first”, explaining a delivery slice, testable scope, blocking questions and the receiving team's check. Retained the measurement plan, handoff table, worked example and distinction between implementation commitment and release approval.
- Aligned both contents lists, the page map, decision labels, example heading and lifecycle overview. Preserved existing IDs and external source destinations. Updated the discovery review date to 4 November 2026.

Rechecked the relevant 6W, 4C and four-trap passages in the live Defence Product Playbook using an HTTP retrieval after the web reader could not open it. Also rechecked Torres's opportunity definitions and Microsoft's pre-experiment guidance. The expanded procedures are this guide's application of those practices; no new organisational requirements or measured results were introduced. Content owner and lifecycle version remain unconfirmed.

Validation passed: 863 local links and assets across thirteen HTML pages; duplicate-ID checks; preservation of existing IDs and external source URLs on all three edited pages; sequential headings; balanced HTML/SVG tags; matching chapter labels in discovery navigation; and whitespace checks. Reread the affected sections, surrounding guidance, worked examples and implementation-readiness handoff. This text revision did not include a browser layout review or publication.

## Natural discovery flow, 2 November 2026

Revised the discovery guide against `writing.md` after reviewing the sequence, worked example and implementation connection. Frame, Test and Decide now describe the learning rhythm; step 6 prepares a delivery slice after a justified commitment. Kept the six steps, existing anchor IDs, source destinations and earlier measurement guidance.

- Introduced entry routes based on the unresolved question and existing evidence. A provisional outcome guides problem research, with causes left explicit as hypotheses until supported. Research and comparisons can lead directly to more learning, a change or a stop.
- Made opportunity selection, comparison of responses and success measures separate actions within step 2. The fictional A-1 comparison records what simpler options help with, why the assistant earns another test and why that choice does not demonstrate superiority.
- Removed the blanket instruction to draft a PRD before prototyping. An experiment starts with a question, conditions and a decision rule; the PRD develops when proposed behaviour needs that detail.
- Separated current system context from candidate-specific feasibility tests. Moved the detailed technical checklist and Double Diamond mapping into optional references. Existing direct links open those references automatically.
- Renamed step 4 around running tests and recording findings. Steps 3–5 form a repeating cycle; improvement returns through test planning before another run. The example separates X-1 findings from the improvement decision and explicitly returns through planning and testing for X-2. Technical and cost checks are planned before results are reviewed for commitment.
- Renamed step 6 to “Agree the delivery slice”, explaining the small useful scope, shared ownership, evidence, requirements, measurement and remaining questions. Retained the handoff package and implementation-readiness links.
- Shortened repeated collaboration guidance, split dense paragraphs and retained concrete owners, inputs, checks, outputs and next actions. Aligned the lifecycle overview, diagram labels, text equivalents, contents lists, figure numbers and repository inventories.

These are handbook recommendations. All new comparison observations remain explicitly fictional; no organisational policy, performance claim or approval authority was added. The previously noted content owner and applicable lifecycle version remain unconfirmed and have not been invented. This revision does not claim complete metadata compliance or an independent reader-comprehension test.

Validation passed: 832 local links and assets across thirteen pages; twenty-six desktop/mobile page loads; expanded discovery and overview layouts at 1440, 768, 375 and 320 pixels; heading order and matching contents; all previous discovery IDs and external source links preserved; direct links into the moved references; consecutive figure numbers; SVG text within view boxes; print restoration, enlarged text and reading without JavaScript. Inspected the revised learning diagram and comparison example visually. No browser errors or failed local requests; whitespace checks passed. Changes remain local and unpublished.

## Product metrics and handoff supplement, 2 November 2026

Reviewed the discovery page's existing measurement ladder, experiment criteria and handoff table alongside the lifecycle overview and implementation-readiness package. The pages named measures but did not define a sufficiently concrete agreement for collecting and reviewing product outcomes after use.

### Research and source boundaries

- [Defence Product Playbook](https://defence-pp.vercel.app/): freshly retrieved its live HTML. The measurement section calls the value metric a North Star, connects it to a slower organisational outcome and recommends one value measure per problem. Retained the existing explicit adaptations of its metric ladder and subjective-measure guidance. Its twice-yearly movement advice is not a universal review cadence.
- [Torres, Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/): rechecked the distinction between business outcomes, product outcomes and feature traction. This supports measuring the proposed user benefit rather than treating adoption alone as success.
- [Microsoft Research, Pre-Experiment Stage](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/): rechecked hypotheses, success measures, guardrails, data quality and comparisons. These support a balanced experiment plan, not a claim that every pilot can establish a causal effect.
- [Amplitude, The North Star Playbook (PDF)](https://info.amplitude.com/rs/138-CDN-550/images/Amplitude-The-North-Star-Playbook.pdf): added as reference 19. Chapters 1–3 distinguish the main value measure from actionable inputs and explain precise definitions. The linked official PDF was readable; several web chapter URLs returned the introduction rather than the chapter content. Applying the framework to internal mission/service outcomes is explicitly a handbook recommendation.

### Changes

Added visible guidance in Frame for choosing product success measures together. Distinguish an established product North Star from the outcome for the proposed scope, supporting measures and guardrails. A feature can contribute to an existing North Star; the guidance does not require a new one per feature. If the main product measure is provisional, record how it will be assessed. Supporting input metrics are distinguished from resource inputs in the existing ladder.

Added a handoff measurement-plan checklist covering definitions and calculations, counted populations, time windows, exclusions, baseline provenance, targets, instrumentation, data verification, owners, review cadence and actions. Targets are agreed before exposure, and missing baselines remain explicit collection work. Acceptance-test success, exploratory prototype results and product outcomes after use remain separate.

Extended the existing fictional example with M-1: a candidate weekly correct-resolution count, demand and rate context, the existing handling-time target, supporting measures, controls and collection/review owners. It deliberately does not invent a measured weekly baseline or numerical North Star target. The example assigns a baseline collection period and target agreement before pilot exposure; the 8.5-minute and 8/8 prototype results remain exploratory.

Aligned the overview's handoff item and implementation's receiving checklist through links to the new measurement plan. Both discovery contents lists expose product success measures and the handoff plan. These are recommended working records, not newly asserted EDS policy.

Validation: 831 local links/assets across thirteen pages, twenty-six desktop/mobile browser loads, expanded layouts at 1440/768/375/320 pixels, heading order, matching contents, existing direct links, print restoration, enlarged text and no-JavaScript reading passed. Additional checks exercised the new anchors and links from both receiving pages. Visually inspected the success-measure guidance on desktop and the measurement plan on mobile. Whitespace checks passed. No commit or publication performed.

## Shared discovery emphasis, 2 November 2026

Rechecked the existing SVPG four-risk and discovery/delivery articles, Torres's opportunity-tree guidance and Sheth's 3-in-a-Box article. Refined “Start together” around the following points:

- Discovery involves Product, Design and Engineering throughout; the product owner does not perform discovery alone.
- Begin with the problem before fixing the solution. Any discipline can initiate the investigation.
- Bring complementary expertise in value and business constraints, user experience and usability, and technical feasibility. These are areas of focus, not exclusive ownership or sequential phases.
- Choose assumptions, develop alternatives and inspect user and technical evidence together. Keep the brief, experiment findings, PRD and recommendation linked.
- Preserve named investment authority, specialist involvement and human accountability. Shared discovery does not imply unanimous approval or invent an organisational decision rule.

SVPG explicitly describes the three disciplines working side by side and distinguishes value, usability, feasibility and business viability. Torres identifies opportunity-tree work as a product-trio activity. Sheth supports ongoing co-creation, initiation by any discipline and joint prototyping; retain this as practitioner advice rather than a demonstrated performance claim. The concrete working rhythm and fictional service-desk example are handbook recommendations, mapped to local roles rather than treating product manager and product owner as universally interchangeable titles.

Moved AI-assistance guidance after the human collaboration guidance so it supports the section's main message. Preserved the existing responsibility table, anchor IDs and source destinations. Updated the page review date to 2 November 2026; the earlier whole-bibliography audit date remains historical.

Validation passed: 817 local links/assets across thirteen pages; twenty-six desktop/mobile page loads; expanded discovery/overview layouts at 1440, 768, 375 and 320 pixels; matching contents, heading order, direct links, print restoration, enlarged text and no-JavaScript reading. No browser errors or failed local requests. Whitespace checks passed. Changes remain local and unpublished.

## Clarity review against writing.md, 28 October 2026

Reviewed the full discovery page against the repository's [writing standard](../writing.md), concentrating on reader purpose, concrete actions, terminology, paragraph structure and the separation of instructions from reference material.

| Clarity problem | Revision |
| --- | --- |
| The lead asked readers to hand over “evidence-backed intent” before explaining what discovery helps them decide. | Lead with choosing a problem, testing solutions and deciding what to build. Identify the six-step guide and fictional pilot in the opening. |
| Several introductory passages repeated collaboration advice, while source commentary interrupted the action. | Name responsibilities and the decision owner first. Consolidate collaboration instructions and keep practitioner attribution in the nearby source note. |
| Readers met abbreviations and specialist terms without enough explanation. | Expand PRD, UI and API; explain hypotheses, acceptance criteria, baselines, guardrails and technical spikes. Replace “falsification criteria”, “disposition” and unexplained testing jargon with concrete actions. |
| Navigation used slash-separated abbreviations that differed from the step headings. | Use the same full step names in the page map and both contents lists. |
| Twelve experiment methods interrupted the main procedure. | Keep method-selection guidance and all safety arrangements visible. Put the catalogue in a labelled reference disclosure, preserving its direct-link target, source links, mobile presentation and print behaviour. |
| Review, deferral and approval explanations repeated without adding a new action. | Remove duplicated instructions while retaining the decision table, return routes, local approval authority and separate release criteria. |
| The fictional commitment combined technical results, costs and limitations in one dense paragraph. | Split technical evidence F-1 and cost evidence C-1 into labelled paragraphs. Explain the test order and denied-access case in everyday language. |
| Optional headings named abstract topics rather than reader tasks. | Use headings about linking records, recording decisions between meetings, testing an agent's journey and connecting measures to value. |

Kept the seven figures, twelve tables, six fictional example panels, all existing IDs and all eighteen external references. Preserved the source qualifications, fictional numbers, experiment limitations and explicit departures from the playbook's measurement advice. Removed the unnecessary broad generalisation about weak products from the problem-framing introduction; the 6W/4C advice retains a direct source link.

The page still lacks a confirmed content owner and applicable lifecycle version, both requested by writing.md. No authoritative values were supplied, so this review does not invent them or claim complete editorial compliance. The last-reviewed date remains 28 October 2026.

Validation: all 814 local links/assets across thirteen pages passed, with twenty-six desktop/mobile browser loads. Expanded layouts at 1440, 768, 375 and 320 pixels, contents matching, headings, direct links, print restoration, enlarged text and reading without JavaScript passed. Additional checks confirmed preservation of every existing ID and external source URL, default collapse of the method catalogue, expansion by direct link and native no-JavaScript control, and SVG text within view boxes. Visually inspected the revised experiment instructions on desktop and the expanded catalogue on mobile. Whitespace checks passed. No commit or publication performed.

## Full content and reference audit, 28 October 2026

This audit supersedes the earlier limitation below that retained references had not all been freshly checked. Reviewed the complete current discovery page, including the seven diagrams and text alternatives, twelve tables, six fictional example panels, optional sections and bibliography. Opened all seventeen original reference destinations and added an eighteenth primary reference for Jobs To Be Done. Reviewed the relevant source passages, not just link availability.

### Material findings and corrections

| Finding | Correction |
| --- | --- |
| The opportunity definition included a potential outcome, blurring two levels of an Opportunity Solution Tree. | Distinguish a user need, pain point or desire from the desired outcome and proposed response; cite Torres beside the definition. |
| A general citation to team structure could imply that the playbook prescribed the agent responsibilities and shared environment. | Restrict the attribution to accountability and multidisciplinary teams; label agent-specific recommendations as this guide's. |
| Sheth's practitioner model could read as an established, demonstrated operating standard. | Describe it as advocacy, distinguish the handbook's application and avoid implying guaranteed outcomes or inventorship of the underlying product trio. |
| Eight staff, task completion fractions and task-time medians lacked an explicit unit of observation. The second test did not state a contemporaneous comparator result. | Specify one task per workflow per participant, matched tasks, counterbalanced order, reporting unsuccessful attempts, and the fictional X-2 comparator. Keep repeat-participant and small-sample limitations visible. |
| The fictional commitment showed user-test results but did not demonstrate why feasibility and affordability supported implementation. | Add explicitly fictional technical record F-1 and cost record C-1, with bounded sandbox results, pilot limits, cost ranges and support capacity. Carry both into handoff. These are teaching additions, not discoveries about EDS. |
| Figure 7's E-2 identifier was not explicitly mapped to the example's X-2. | Identify E-2 as the traceability summary of X-2. |
| The metric ladder changed the playbook's meaning of input, and accepted subjective measures that the playbook rejected, without making both departures explicit. | Explain the altered input category and the different treatment of subjective measures. Do not reproduce the source's confidence percentages as calibrated evidence. |
| GitHub Spec Kit appeared beneath measurement guidance it did not support and lacked a nearby explanation of its relevant scope. | Move its attribution to specification/plan traceability and feedback, bounding its aspirational claims. |
| “Version 1.0” could not be established from the retrieved live playbook. | Remove that edition label and record the live web edition and access date. |
| The older Dual-Track Agile title could conceal the author's updated preference. | Explain Cagan's move to continuous discovery and delivery. |
| JTBD relied on a secondary framework catalogue and omitted social and emotional dimensions. | Add the Christensen Institute as the primary explanatory reference and include those dimensions. |

### Reference-by-reference verification

Numbers match the page's displayed bibliography; existing anchor IDs remain intact.

| Ref | Source and relevant passage | Audit result |
| --- | --- | --- |
| 1 | [MINDEF and DSTA, The Defence Product Playbook](https://defence-pp.vercel.app/), problem/measurement, team structure and TEST sections | Retrieved and read the site's HTML because the web reader could not open it. The site identifies MINDEF and DSTA as joint developers. Confirmed 6W, four 4C names and meanings, four traps, SFR, TEST, ladder rung names, twice-yearly movement recommendation and outcome-per-dollar example with annual costs. Interpretive departures are now explicit. The cited web edition does not establish an EDS mandate or a numbered publication edition. |
| 2 | [Design Council, The Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) | Confirmed Discover, Define, Develop and Deliver, small-scale solution testing, revisiting earlier work and CC BY 4.0 attribution. Figure 4 explicitly identifies handbook labels and checkpoints as adaptations. |
| 3 | [Marty Cagan, The Four Big Risks](https://www.svpg.com/four-big-risks/) | Confirmed value, usability, feasibility and business viability, with Product, Design and Engineering collaborating. Figure 5's particular tests remain handbook recommendations; viability includes wider business constraints, not just operating cost. |
| 4 | [GitHub Spec Kit, Specification-Driven Development](https://github.com/github/spec-kit/blob/main/spec-driven.md) | Confirmed specifications, technical plans, versioned team review and feedback from implementation/operations. Does not independently substantiate measurement guidance or guaranteed correctness. The link tracks main and may change. |
| 5 | [Sumit Sheth, From Headless to Thoughtful](https://www.linkedin.com/pulse/from-headless-thoughtful-why-3-in-a-box-operating-model-sumit-sheth-imptc/) | Read the public article, dated 18 April 2026. Confirmed PM/UX/Engineering and Intent/Interaction/Implementation, continuous co-creation and AUX as designing agent interaction with products. No claim that Sheth invented product trios or that the handbook's agent checklist appears verbatim in the article. |
| 6 | [Product School, The Definitive Guide to Product Discovery and Frameworks](https://productschool.com/blog/product-fundamentals/what-is-product-discovery) | Confirmed all six listed framework families. Retained as an overview; individual technical explanations use primary references where available. |
| 7 | [Product School, The Product Experimentation Playbook for AI PMs](https://productschool.com/blog/product-fundamentals/product-experimentation) | Confirmed split/multivariate tests, demand and landing-page probes, usability, manual simulation, staged exposure and continuous personalisation. Retained as catalogue inspiration. The handbook adds methodological limits; rollout and adaptive allocation are not presented as automatic causal evidence. |
| 8 | [Teresa Torres, Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/) | Confirmed outcome → customer needs/pain points/desires → solutions → assumption tests. Figure 3 remains explicitly a simplified teaching map rather than a full tree. |
| 9 | [The Lean Startup, Methodology](https://theleanstartup.com/principles) | Confirmed Build–Measure–Learn, MVP learning and pivot/persevere decisions. The handbook's cost and control checks are recommendations. |
| 10 | [Marty Cagan, Dual-Track Agile](https://www.svpg.com/dual-track-agile/) | Confirmed parallel collaborative discovery/delivery and the author's update preferring continuous discovery/delivery terminology. No requirement for separate discovery and delivery teams. |
| 11 | [GV, The Design Sprint](https://www.gv.com/sprint) | Confirmed the five-day map/sketch/decide/prototype/test sequence. Separate feasibility spikes are handbook advice, not a prescribed extra sprint day. |
| 12 | [Nielsen Norman Group, The Wizard of Oz Method in UX](https://www.nngroup.com/articles/wizard-of-oz/) | Confirmed a mock interface partly or wholly controlled by a person. Kept the boundary between simulated interaction evidence and actual technical capability. Briefing/debriefing instructions are handbook recommendations. |
| 13 | [Microsoft Research, Patterns of Trustworthy Experimentation: Pre-Experiment Stage](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) | Confirmed falsifiable hypotheses, success/guardrail/data-quality measures, randomisation units, statistical power and safe exposure. A/B row requires an adequate sample and planned stopping rule without claiming a universal sample size. |
| 14 | [Optimizely, Multivariate testing](https://www.optimizely.com/optimization-glossary/multivariate-testing) | Confirmed combinations, interactions and greater observation needs. Unstructured simultaneous changes are not equated with a designed multivariate experiment. |
| 15 | [Product School, Your Guide on How to Improve Product Discovery with AI](https://productschool.com/blog/artificial-intelligence/how-improve-product-discovery-with-ai) | Confirmed AI-assisted discovery as the inspiration. Do not import its adoption statistics or promotional speed claims; source checking and provenance controls are supported separately by NIST. |
| 16 | [Nielsen Norman Group, Synthetic Users: If, When, and How to Use AI-Generated “Research”](https://www.nngroup.com/articles/synthetic-users/) | Confirmed hypotheses/desk-research uses and the limits on substitution for real-user research. Generated interviews are not reported as observations of participants. |
| 17 | [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), July 2024 | Confirmed suggested action MS-2.5-003 on verifying generated sources/citations and Appendix A.1.6 on content provenance. These are recommendations within a risk-management profile; the page does not turn them into a new organisational mandate. |
| 18 | [Christensen Institute, Jobs to Be Done Theory](https://www.christenseninstitute.org/theory/jobs-to-be-done/) | Added primary support for progress in particular circumstances and functional, social and emotional dimensions. |

### Quotation, evidence and policy boundaries

The page contains attributed paraphrases, named terms and titles rather than a long direct quotation from a source. Checked quoted names and terms against the relevant source text. The revised source introduction distinguishes these from original handbook templates, the four-phase/six-step model and fictional examples. A source's assertion is not automatically empirical evidence: the playbook's generalisation about weak problem statements remains attributed to the playbook, not presented as an independently measured prevalence.

The numerical service-desk results, thresholds, artefact IDs and new technical/cost records remain explicitly fictional. They are internally coherent teaching material and cannot be externally verified as organisational outcomes. No real EDS decision authority, content owner, mandatory gate, approved tool or policy has been inferred from the public sources. Those local facts need authoritative organisational records before claiming policy compliance. This review checks what the page attributes to its sources, not every assertion within the cited publications.

### Validation for this audit

Ran the existing browser/link checks after the substantive changes: thirteen HTML pages, 813 local links and asset references, twenty-six desktop/mobile loads, expanded discovery and overview layouts at 1440/768/375/320 pixels, matching contents, sequential headings, direct links, legacy anchors, print restoration, enlarged text and no-JavaScript reading. No browser errors or failed local requests were reported. The final rerun after wording changes passed with the same results. Whitespace checks passed. No commit or publication performed; pre-existing workspace changes were preserved.

## Earlier merge and visual review

Reviewed 28 October 2026 against both Git conflict versions, `../writing.md`, `../design.md` and the surrounding lifecycle pages. This record supersedes the earlier learning-flow review for the reconciled page. Earlier validation results in `product-pages-review.md` describe historical snapshots.

## Critical assessment

The conflict was substantive. One version organised discovery into four stages and added research, opportunity selection, feasibility, framework selection and AI evidence checks. The other offered a clearer six-step learning journey, six diagrams, an evolving PRD and one continuous fictional example. Choosing either version wholesale would discard useful work; the dates alone did not determine which content to retain.

| Issue | Resolution |
| --- | --- |
| Discovery and ideation were treated as interchangeable titles. | Use Product discovery consistently with the surrounding handbook. Explain that ideation generates options within discovery. Use the Product discovery URL; the later path-alignment update is recorded below. |
| Competing four-stage and six-step processes could leave readers following two lifecycles. | Use Frame → Test → Decide → Handoff as four phases containing six practical steps. Integrate research and opportunity selection into Frame; retain framework selection as an optional reference. |
| A simpler learning journey removed detailed technical and research coverage. | Retain AI synthesis checks, opportunity records, prioritisation limits, twelve experiment methods and the handover evidence table. Write fresh research and technical investigation guidance with clear evidence outputs. |
| Repeated examples used different thresholds and could imply a universal sample rule. | Keep the six-part fictional service-desk example and its single set of exploratory criteria. Omit the competing example. Retain explicit limits on sampling, repeat participation and production conclusions. |
| User testing could overshadow unresolved feasibility. | Keep business and technical discovery active throughout. Test critical assumptions, retain conditions and results, and return blocking unknowns to discovery or narrow scope before commitment. |
| Decisions could conflate investigation, implementation and release. | Retain separate evidence standards and feedback routes. Explain deferral with an owner and reopening trigger. Prototype success does not establish release readiness. |
| Removed public-service references still underpinned two source-specific passages. | Delete both bibliography entries, their explanatory passages and their historical source-mapping entries. Replace the associated research and feasibility material with newly written guidance using independent principles and explicit handbook recommendations. |
| Reference detail obscured the main reading path. | Keep frameworks, agentic UX and advanced measurement in native disclosures. Retain the main steps, six diagrams, versioned artefacts and linked example. |

## Source boundaries

Rechecked the [Design Council’s Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) for problem investigation, definition, alternatives and small-scale testing; [SVPG’s four risks](https://www.svpg.com/four-big-risks/) for value, usability, feasibility, viability and collaborative discovery; and [Teresa Torres’s opportunity trees](https://www.producttalk.org/opportunity-solution-trees/) for the distinction between outcomes, opportunities, solutions and assumption tests.

The replacement checklists and evidence records are editorial recommendations. They do not claim independent sources prescribe the handbook’s templates, roles or approval process. Other retained sources carry their existing scope; this reconciliation did not freshly validate every external claim or destination.

The excluded references are absent from tracked working content. Their source-specific phase distinction and explanations have been removed. The retained general discovery concepts are independently supported or explicitly identified as original working recommendations. This review does not rewrite Git history or ignored preview snapshots.

## Formatting and navigation

Retained six accessible inline SVG diagrams, twelve captioned tables and the continuous fictional example. The technical evidence table uses labelled mobile records. Both contents lists follow document order and include research, feasibility and experiment-method links. Kept page styling and disclosure support consistent with the existing handbook.

All anchors from both conflict versions remain except the two removed bibliography entries. Remaining sources keep their existing anchor IDs for direct links; displayed reference numbers are consecutive. The page title, primary navigation and repository inventories now agree on Product discovery.

## Validation

Fresh checks for this reconciliation passed:

- 811 local links and asset references across all 13 HTML pages; unique IDs and 81 anchors on the discovery page.
- Preservation of both versions’ anchors except the two intentionally removed bibliography entries; no remaining conflict markers or excluded references in tracked working files.
- Matching mobile and desktop contents, one H1, sequential heading levels and captions and scroll wrappers for all twelve tables.
- Chromium layouts at 1440, 768, 375 and 320 pixels with disclosures collapsed and expanded; no page overflow or browser exceptions.
- Direct links opening optional content, reading with JavaScript disabled and enlarged text without page overflow.
- Visual inspection of the revised technical guidance on desktop and mobile, plus whitespace checks.

These checks do not establish complete accessibility conformance or production readiness. Earlier Lighthouse scores and broader accessibility claims describe prior snapshots and have not been reasserted here. Changes remain local; the merge has not been committed or published.

## Terminology and path alignment, 28 October 2026

Renamed the page to `dist/product-discovery.html`, its reading aids to `dist/product-discovery.css`, its disclosure support to `dist/product-discovery.js`, and this review to `product-discovery-review.md`. Updated links across all thirteen HTML pages, repository inventories and review records. The new page path replaces the former path; no redirect page is included. Existing section aliases remain available on the new page.

Reviewed the surrounding handbook for terminology and process consistency. Updated the lifecycle overview’s introduction, comparison table, loop explanation, accessible diagram text and SVG labels to Frame, Test, Decide and Handoff, containing the same six steps as the discovery guide. Only a justified commitment proceeds to Handoff. Updated the authoring terminology rule, page description, diagram classes and disclosure identifiers. Ideation remains the activity of generating options within discovery; dated review entries retain historical terminology.

Fresh validation checked all thirteen pages and 811 local links and asset references, including fragment targets. All twenty-six desktop/mobile page loads passed without overflow, browser exceptions or failed local requests. The discovery and lifecycle overview pages also passed expanded layouts at 1440, 768, 375 and 320 pixels. Matching contents lists, heading order, linked optional content, legacy section aliases, print expansion/restoration, enlarged text and no-JavaScript reading passed. Visually inspected the updated overview diagram. No commit or publication was performed; these are current workspace edits.

## Critical visual explanation review, 28 October 2026

Assessed the discovery guide’s six existing figures and its relationship to the lifecycle overview. The page already had substantial visual coverage. The useful addition was a missing conceptual relationship: one observed need can lead to several solutions, each requiring evidence suited to its assumptions. Extra diagrams for the framework catalogue or every checklist would increase length without clarifying a new relationship.

| Visual | Assessment and action |
| --- | --- |
| Learning journey (Figure 1) | Retained its four-phase/six-step map. Made continuous business and technical discovery visible in the heading, retained the human collaboration explanation, and included defer alongside stop. Corrected the decision-figure cross-reference. |
| Problem framing (Figure 2) | Retained. It already distinguishes a request, observations and a causal hypothesis, using the same fictional service-desk evidence as the narrative. |
| Opportunity, concepts and tests (new Figure 3) | Replaced the competing access-request example with a teaching map connected to the main service-desk example. One observed opportunity branches into three concepts. The assistant branch illustrates separate user/value and permission/feasibility tests feeding a joint review. No winner or successful result is implied. The caption explicitly distinguishes this simplified map from a complete Opportunity Solution Tree. |
| Double Diamond (now Figure 4) | Retained. It explains widening and narrowing, distinguishes small-scale testing from production deployment, and preserves attribution and the boundary on organisational gates. |
| Test selection (now Figure 5) | Generalised staff/retrieval-specific wording to users, task completion, capabilities and integrations. Replaced overlapping copies of the distribution line with one shared trunk and four clear branches. Retained four different evidence types and the warning against treating them as a sequence. |
| Decision routes (now Figure 6) | Rebuilt. The former text alternative incorrectly described an earlier lifecycle. The former sufficiency check could also send a supported finding for change back to further testing. The new tree checks permission, risk, value and budget; makes temporary deferral visible; routes supported changes to improve/redesign/pivot; and distinguishes inconclusive evidence from support for bounded implementation. Updated the text alternative and decision table to match. |
| Evidence trace (now Figure 7) | Retained. Its job is traceability between evidence, requirements, interface states and verification. It explicitly avoids a causal or runtime interpretation and preserves the limits on prototype evidence. |
| Lifecycle overview | Retained the previously aligned cross-loop diagram. It explains where discovery sits in delivery; the discovery page explains the detailed work and decisions. Adding the new teaching map here would repeat detail at the wrong level. |

The diagrams use the existing inline SVG system, captions, text alternatives, scroll containers, controls and reduced-motion support. All existing figure anchors remain; the new teaching map has its own anchor. No new source, tool dependency or excluded reference was introduced. Repository inventories now state seven discovery diagrams.

Validation passed: 811 local links/assets across thirteen pages, twenty-six desktop/mobile page loads, matching contents, heading order, expanded layouts at 1440/768/375/320 pixels, direct links, legacy section aliases, printing, enlarged text and reading without JavaScript. Browser geometry checks found no SVG text outside view boxes or overlapping text in all seven figures. Visually inspected the new opportunity map, rebuilt decision tree, revised selector and mobile text/scroll presentation. Diagrams retain horizontal scrolling on narrow screens with readable text alternatives; complete accessibility conformance was not assessed. Workspace files were edited directly, with no commit or publication.
