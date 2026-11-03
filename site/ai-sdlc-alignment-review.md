# AI-SDLC flow alignment review

Reviewed on 3 November 2026 against the current working copies of:

- [AI-SDLC overview](dist/ai-pdlc.html)
- [Product discovery](dist/product-discovery.html)
- [Product implementation](dist/product-implementation.html)

The repository has no separate Product Ideation page. `writing.md` defines ideation as generating options within discovery. This review therefore treats discovery and implementation as the two detailed pages that the overview needs to summarise.

The main lifecycle was already consistent: Frame → Test → Decide, then prepare a delivery slice after a justified commitment; handoff carries the evidence into Plan → Slice → Implement → Verify → Release and observe → Learn. The gaps were in the overview's branches, readiness conditions, decisions and illustration. Updated the overview without changing the detailed pages or introducing new approval authorities.

## Findings and corrections

| Finding | Basis in the detailed pages | Overview correction |
| --- | --- | --- |
| The discovery diagram returned only to framing, obscuring the shorter test loop. | Discovery distinguishes inconclusive evidence, improve, redesign and pivot, with specific return steps. | Added a return path to Test. The text equivalent and prose identify step 3, steps 3–4, step 2 and step 1 respectively. Defer retains an owner and reopening trigger; stop preserves learning. |
| Context appeared to enter only implementation. | Discovery uses architecture, operating constraints and feasibility findings from its earliest investigations. | Renamed the diagram input Shared context and connected it to discovery as well as implementation. Added usability and viability to the discovery risk label. |
| A fixed sequence could be inferred from the overview. | Discovery chooses an entry point from the uncertainty and checks whether existing evidence still applies. | Made that entry rule explicit and located ideation within discovery. Retained ongoing Product, Design and Engineering collaboration. |
| Investment and release decisions were insufficiently distinguished in the overview. | Discovery's Decide authorises the next bounded investment; implementation separately verifies and controls release. | Named the authorised discovery decision owner, separated commitment from release, and described independent review, accountable acceptance and release controls. |
| The handoff could imply a new formal screen-approval gate and did not distinguish blockers from accepted uncertainty. | Discovery and implementation use a joint walkthrough, interface alternatives for services without screens, and bounded plans for accepted unknowns. Concept-invalidating unknowns return to discovery or narrow the scope. | Replaced unexplained “approved” screens with reviewed artefacts, made screen alternatives explicit in readiness checks, and added unknown impact, next check, bound and escalation trigger. Labelled readiness checks as recommendations. |
| The overview's fictional handover used three prototype rounds and access-request scope, unlike the current discovery example. | Discovery examples 5–6 use the second test cycle, routine guidance, a read-only contract, technical and cost findings, and an explicit pilot commitment. | Replaced the separate story with a linked summary of that example. Preserved its limits: exploratory evidence does not establish production safety or long-term value. |
| The diagram shortened “Release and observe” to “Release”. | Implementation explicitly separates observation from the subsequent Learn decision. | Restored the full stage name and displayed Learn on its own line in the grouped node. |
| Feedback routing focused on value versus quality and omitted feasibility or cost invalidating scope. | Both detailed pages allow technical findings to reopen discovery and distinguish product outcomes from acceptance-test success. | Added the feasibility/cost/constraint route and linked joint feedback review to product measures, guardrails, operating evidence and recorded next actions. Learn now names its owner and revised artefacts. |

## Resulting flow

1. Enter discovery at the step justified by current evidence. Product, Design and Engineering investigate user, business and technical questions together.
2. Frame the problem and compare options; choose and run tests; evaluate the evidence. Return to the appropriate step, defer with a trigger, stop, or commit to a bounded delivery investment.
3. After commitment, agree the delivery slice. Carry the PRD, relevant UI or interface artefacts, evidence and limitations, technical findings, measurement plan and owned uncertainty into a joint readiness review. Shared organisational context constrains both loops.
4. Plan the TRD, slice into verifiable tasks, implement with evidence, verify independently, release and observe under applicable controls, then learn. A discovery commitment does not authorise production release.
5. Route bounded defects and delivery improvements to implementation. Reopen discovery when evidence challenges the intended outcome, scope or feasibility. Record who decides, what changes and what evidence will be checked next.

## Verification and limits

Checked 244 local links and asset references across the three pages, including anchor destinations. Existing overview anchor IDs were preserved; desktop and mobile contents lists match their sections. Chromium checks at 1440, 768, 375 and 320 pixels found no page overflow, SVG text outside the view box, browser errors or failed local requests. Checked reading without JavaScript and loading with reduced motion. Visually inspected the revised overview diagram on desktop and the handoff at mobile width. `git diff --check` passed.

This is an internal consistency review of the current handbook, not a fresh validation of its external bibliography or EDS policy. Existing source links and unrelated working-tree changes were preserved. No commit or publication was performed. No confirmed content owner or lifecycle version was supplied, so neither was invented.

## Follow-up: external reference accuracy, 3 November 2026

Checked all three external references cited by the AI-SDLC overview against their current source content. The passages are summaries and adaptations, rather than attributed verbatim quotations. The main attributions were supported; the changes below clarify where this handbook adds interpretation.

| Reference and claim | Check result and action |
| --- | --- |
| [DORA, User-centric focus](https://dora.dev/capabilities/user-centric-focus/): accessible feedback and visible user measures alongside technical measures. | Supported by the feedback-loop and metrics guidance. Retained the summary. DORA also warns against using output volume as the measure of user value. The page displays an update date of 12 January 2026. |
| [McKinsey, How an AI-enabled software product development life cycle will fuel innovation](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/how-an-ai-enabled-software-product-development-life-cycle-will-fuel-innovation): broader AI assistance, connected research and usage data, earlier experiments and earlier quality controls. | Supported, particularly by shifts 2, 3 and 5 and the tooling discussion. Confirmed publication on 10 February 2025. Made its prospective character explicit and included compliance in the summary. Its forecasts and interview perspectives do not demonstrate benefits for every team or prescribe this handbook’s lifecycle. |
| [Defence Product Playbook, Tools to use](https://defence-pp.vercel.app/#/tools): ProductOps learning cycles and concurrent delivery. | Supported. Added the source’s distinction between initial problem research and later research prompted by a changed problem. Explicitly separated its iterative principle from this handbook’s six discovery steps and six implementation stages. |
| [Defence Product Playbook, Define the problem, measure the value](https://defence-pp.vercel.app/#/problems): 4C and five causes/actions for stalled measures. | Supported. Confirmed all four 4C labels and the five table categories. The table deliberately substitutes local decision authority for the source’s Steering Committee and adds lifecycle destinations. Made that adaptation explicit. |
| [Defence Product Playbook, Govern and review](https://defence-pp.vercel.app/#/govern): value plateaus and maintenance. | The source suggests redirecting investment when a product has delivered its available value. The handbook’s checks for measurement limits, changing conditions and essential obligations are additional recommendations. Labelled that distinction explicitly. |
| [Defence Product Playbook, Tools to use](https://defence-pp.vercel.app/#/tools): four quality layers. | Confirmed prevention before build, outcome validation from design, scanning at pull request and integration verification after merge. Retained the four-layer summary and clarified that this model does not establish EDS policy or substitute for release criteria. |

The playbook’s current HTML identifies it as jointly developed by MINDEF and DSTA and names Tan Min Min (MPO) and Alvin Loh (DSTA) as co-authors. That verifies the site’s self-description, rather than independently establishing organisational approval or the version applicable to EDS. Adjusted the overview’s attribution accordingly. Its source does not display a stable release/version identifier in the retrieved content.

DORA and McKinsey were read through the web tool. The web tool could not retrieve the playbook, so its current public HTML was fetched directly and the relevant sections inspected. The HTML contains the article content and navigation routes; this check did not rely solely on an earlier cached extract. Added direct section links and a reference-check date to the overview.

After these edits, the 244 local link/asset checks, preserved anchors, matching contents lists, four responsive widths, SVG bounds, reduced-motion load and no-JavaScript reading passed again. No browser errors occurred. No commit or publication was performed.
