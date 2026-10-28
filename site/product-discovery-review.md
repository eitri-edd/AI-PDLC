# Product discovery merge review

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
