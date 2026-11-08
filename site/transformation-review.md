# Organisation transformation: editorial review

## Issue 31 · Reader-focused restructure · 8 November 2026

Revised `dist/transformation.html` locally in response to [issue 31](https://github.com/eitri-edd/AI-PDLC/issues/31). The reader is a product manager, team lead or delivery colleague familiar with planning and review who needs to commission specialist checks and make an evidence-based adoption proposal. The scope remains delivery-team and shared-service adoption of AI-assisted development.

### Findings verified before editing

The published page was inspected in the browser on 8 November. It already displayed three upload-example panels without expansion: planning across four areas, correction of the omitted recipient-access check, and the 60-to-20-minute drafting comparison with 90 minutes total effort in each period. The issue's crawler-based absence claim does not describe the page observed in this check; no conclusion is made about the 7 November snapshot. Several requested definitions also already existed. The actionable problem was fragmented teaching, dense specialist material in the core path and incomplete interpretation of the scorecard.

Other local untracked reviews describe different chapter snapshots and audiences. They were consulted as historical context, not treated as the current chapter or overwritten by this change.

### Changes and author assessment

| Reader task | Change | Assessment after rereading |
| --- | --- | --- |
| Plan connected changes across the four areas | Retains People, Process, Culture and Technology, with four concise planning questions and a lead-action block per area. | Each block names the record to keep, how the lead uses it and the relevant specialist or existing decision authority. |
| Follow one case without opening reference material | Six visible upload panels progress from setup and reviewer capacity through failure, correction, learning, control recheck and adoption review. | The same recipient-access rule and isolated scope recur throughout. The control setup precedes drafting; later demonstrations recheck the existing boundary. No new running example is introduced. |
| Understand what demonstrates a correction | Shows expected denial, the original delivery failure and corrected authorised/unauthorised/unsupported-file results, with revision and review records. | Original results support the isolated acceptance decision. Functional acceptance, security findings, production release and broader adoption remain distinct. |
| Commission technical evidence | Reframes the core Technology section as demonstrations of access, blocked progress and recovery. | The lead asks for and uses evidence rather than being instructed to configure infrastructure. AI assessment retains an explicit critical-error rule. |
| Find specialist detail when needed | Moves unchanged role, platform and shared-ownership matrices after the pilot decision, along with permission and full measurement references. Retains all four topic diagrams, with three in the reference. | Detailed content remains available through native disclosures, section pointers and retained public anchors. |
| Understand specialist terms | Defines harness and CI/CD in the core; explains design tokens, prompt injection, infrastructure as code and multi-agent orchestration beside their reference uses. Defines evaluation cases and separates development-tool assessment from feature tests and AI-product behaviour. | Terms describe mechanisms and use the upload scenario where applicable. Orchestration stays optional; the pilot uses one agent. |
| Interpret research | Leads with the practical takeaway, retains causal/applicability limits beside claims and moves numerical research detail into Sources. Includes practical IMDA, OWASP and DORA summaries. | External research motivates local measurement without supplying a promised productivity gain. Existing source URLs and numbering remain. |
| Calculate and act on results | Adds attempt/acceptance counts, periods, non-overlapping effort categories, underlying totals, quality follow-up, unknown results and a completed Keep testing decision. | Each period contains 540 human task minutes divided by six accepted changes: 90 minutes, missing the 75-minute target. The next six-attempt trial tests a stated instruction change within the same permissions and has an end date and follow-up review. |

All dates, events and figures in the upload case are labelled fictional. Baseline attempts are seven (six accepted, one abandoned); trial attempts are eight (six accepted, two abandoned). The totals include abandoned work and count each person's task effort once. Waiting, shared setup and training are excluded from the 90-minute task-effort comparison and remain part of the unknown overall cost. Missing timestamps, cost allocation, live-use evidence and baseline participant feedback are not represented as zero or improvement. Four feedback respondents are named; platform feedback was not collected.

The 19 October decision follows the 14-day follow-up ending 17 October. Further task attempts end 30 October, follow-up ends by 13 November and the next fictional adoption review is 16 November. A missed effort target and incomplete scorecard support a bounded further experiment, not expansion or production access. The Expand / Restrict / Stop / Keep testing options and immediate stop conditions remain.

The root and site README summaries now describe the actual reading paths and supporting files. No organisational policy, staffing mandate or new approval authority was introduced.

### Verification and limits

- **Source checks:** balanced explicit tags, paragraph nesting, sequential headings, one page title and unique IDs passed. All 51 original IDs, three incoming chapter anchors, 104 local resource/link references and 16 distinct external URLs are preserved or resolve. The three moved matrices are textually unchanged. The final chapter has six tables; navigation includes the delivery reference. Evidence: `.preview/issue31-source-checks.json`.
- **Arithmetic:** independently recalculated baseline 360 + 120 + 60 = 540 and trial 120 + 300 + 120 = 540; both divided by six give 90. The 40-minute drafting saving is offset by 30 additional review minutes and 10 correction minutes. The 15-minute target gives a maximum of 75 minutes per accepted change.
- **Browser:** at 320, 375, 768, 1100 and 1440 pixels, no page-level horizontal overflow was observed with the references closed or open. The worked table fits its container and stacks with visible baseline/trial labels on phones. Six direct reference/diagram fragments revealed their target disclosures; keyboard toggling worked. No page-script errors were observed. Evidence: `.preview/issue31-browser-checks.json`, `issue31-comparison-375.png` and `issue31-comparison-1440.png`.
- **No scripts and enlarged text:** a QA-only response omitted scripts and, separately, applied 200% root text size. The six main case panels remained outside disclosures; native keyboard expansion worked. At 375 pixels with both conditions, the table and page fit after correcting long-word wrapping. This is a root-text enlargement check, not a full browser-zoom or accessibility audit.
- **Print/disclosure code:** a DOM fixture exercised initial deep links, reopening a closed current fragment, print expansion/restoration and malformed fragments. It also checked interaction with the shared figure-reading print handler. The page script avoids taking ownership of that shared state. Evidence: `.preview/issue31-interaction-checks.json`. Actual browser print pagination was not tested.
- **Sources:** DORA 2025, the McKinsey survey, both METR publications and OWASP were retrieved during the proposal review on 8 November. IMDA's public search-indexed summaries were checked after its direct page returned a bot-verification response. The full IMDA framework and the unchanged Microsoft/DORA supporting references were not newly revalidated.
- **Author reread:** checked the changed chapter, reference definitions, preserved matrices, source mappings, responsibilities and case chronology against `writing.md` and `design.md`. JavaScript syntax and `git diff --check` passed. These checks do not establish reader comprehension.

### Representative-reader checks still outstanding

Ask an aspiring PM or team lead to answer without corrective coaching. Record the answer, hesitation, assistance and consequential misunderstanding; revise the responsible passage and repeat where needed.

| Task | Expected answer |
| --- | --- |
| Has the trial saved human effort or met its target? | No. Both periods use 90 human task minutes per accepted change; the target is at most 75. Faster drafting is offset by review and correction. |
| What demonstrates that the access defect is corrected? | The same corrected revision denies unauthorised delivery, permits authorised delivery and rejects unsupported files; original failed/passing results and specialist findings are retained. |
| Can missing cost data be treated as no additional cost? | No. Total cost is unknown, including setup, training, support allocation and incomplete tool charges. |
| What does the lead commission from specialists? | Demonstrations of permissions, blocked required checks, stop/recovery and support, retained in a readiness record. |
| Does isolated acceptance allow production deployment or broader agent access? | No. Those decisions retain their existing authorities and require evidence for the proposed scope. |
| What happens next? | Keep testing six attempts of an explicit acceptance-case step, within the same permissions, to a fixed end date and follow-up review. No expansion is supported yet. |

No representative-reader session, full HTML conformance audit, complete accessibility audit, browser print-pagination check, commit, push or deployment was performed. Changes remain local. Earlier entries below describe earlier snapshots and are not verification of this revision.

## Alignment with the revised writing standard · 4 November 2026

Revised the chapter against the current `writing.md`, focusing on the reader’s task, connected explanations, terminology and the distinction between general guidance and implementation-specific practices.

- Rewrote the opening for team leads and delivery teams, connecting faster drafting to requirements, review capacity and a bounded pilot.
- Combined People and Team composition into one section. Retained `#team-composition` on the delegated-work heading for existing links, and updated both contents lists, the page map and the discovery page’s incoming link label.
- Removed the overlapping contributions table while retaining the detailed competency table, specialist responsibilities and the distinction between QA acceptance and security approval. Clarified product-owner usage and the contribution of business analysis without assigning new authority.
- Replaced the glossary with explanations beside the relevant passages. Separated PRD/TRD meanings from workflow-specific preparation and approval, linked to implementation guidance, and removed the generic two-tier review prescription.
- Replaced the search-filter scenario with the upload-feature pilot used elsewhere in the chapter. The example now traces an omitted recipient-access check through correction, independent review and retained evidence, with effort counted in the final comparison.
- Promoted shared capability ownership into a separate section, retaining its anchor and maintenance, support and funding responsibilities. Distinguished development-tool evaluation cases from evaluation of AI behaviour in a delivered product.
- Specified how reviewers compare AI assessments with original evidence, record missed defects and unsupported findings, and handle unresolved disagreements.
- Preserved the existing research claims, nearby limitations, source-check date, pilot scorecard, stop conditions, decision authority and fictional effort figures. No new empirical claims were introduced.

Validation: source-level checks passed for balanced tags, heading order, unique IDs, local files and anchors, incoming chapter anchors, table headers and diagram text references. `git diff --check` passed for the edited files. Browser policy blocked opening the local HTML file, so no visual layout review was completed. A comprehension check with a representative reader remains outstanding; this is not recorded as completed reader validation. Changes remain local and unpublished.

## Clarity and pilot examples · 4 November 2026

Assessed the requested Introduction passage, four-area example and pilot guidance against `writing.md`. The main issues were an abstract explanation of late feedback, categories presented as actors, compressed review instructions and an indirect decision heading.

The revision follows three editorial steps: explain the practical problem, name the people and checks, then show how the results lead to a decision.

| Passage | Revision and example |
| --- | --- |
| Introduction: specialist handoffs | Explain why decisions need timely discussion. A fictional upload feature shows how a late recipient-access review leads to changes in design, code and tests. |
| Four areas of change | Replace the single sentence with actions by the product owner, developer, reviewers and platform engineer. Keep one upload-feature pilot across all four areas and introduce AI agent before using the term. |
| Run a pilot and decide from evidence | Define a pilot and baseline, separate boundaries from assessment criteria, and name who collects results, checks them and decides. Explain scorecard measures in everyday language. |
| Agree what the evidence permits | Rename the heading to state the four choices. Explain the conditions and follow-up for each, including a bounded trial of a proposed revision. Fictional figures show drafting effort falling from 60 to 20 minutes while total human effort remains 90 minutes. |

Reread the revised passages with the surrounding explanation, page opening, headings, next steps and linked process and shared-ownership guidance. Retained existing approval authority, stop conditions, recovery, observation periods and comparison limitations. The examples remain fictional; no new empirical claims or organisational requirements were added.

Validation: checked balanced HTML tags, heading sequence, duplicate IDs and all local links and anchors on both edited pages; checks passed. `git diff --check` passed. No browser layout or accessibility audit was performed. Changes remain local and unpublished.

## T07 · Orchestration glossary · 21 October 2026

Broadened the subagent orchestration definition in `dist/transformation.html` to include dependent tasks running in sequence and independent tasks running in parallel where appropriate, followed by integration. The surrounding accountability and review guidance remains unchanged.

Reviewed [Anthropic's Building effective agents](https://www.anthropic.com/research/building-effective-agents), which describes dynamic task decomposition, delegation and synthesis in the orchestrator–worker pattern and discusses parallelisation separately. The glossary uses a broader practical definition without making parallel execution essential.

Validation: checked the one-line glossary change and the diff for whitespace errors. No structure, links or styling changed. Changes remain local and unpublished.

## Platform / Cloud Engineer proposal · 18 October 2026

- Added Platform / Cloud Engineer to the contributions and competency tables, with existing expertise, AI-assisted responsibilities and observable evidence of competence.
- Included the role in the accountable-delegation diagram, its text equivalents and the fictional team example. The added SVG label fits inside the existing owner node.
- Defined three areas of work: CI/CD pipeline setup and maintenance, infrastructure provisioning and hardening, and operations and application health monitoring. Included blocked checks, reviewed infrastructure code, hardening evidence, tested alerts and recovery procedures as practical outputs.
- Clarified collaboration: developers provide application health signals and diagnose code failures; platform engineers maintain shared delivery and monitoring foundations; QA and security retain their respective review responsibilities. Existing release and risk authorities still apply. The role can be available within a squad or through a named shared team with support coverage.
- Extended shared-service ownership, pilot preparation, operational health measures and total cost to cover these responsibilities. The proposal does not create an EDS staffing requirement or grant agents production authority.
- Consulted [Microsoft platform automation guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/automation), [Microsoft security role guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles) and [DORA monitoring and observability guidance](https://dora.dev/capabilities/monitoring-and-observability/). These support the practices; their mapping to this role is an editorial proposal. No new performance claims were added.

Validation: browser checks at 320, 375, 768, 1100 and 1440 px found no page overflow, including expanded diagram text and horizontal scrolling of the competency table. Checked heading order, duplicate IDs, internal anchors, local links and the new SVG label bounds. Both role rows remain available without JavaScript at 320 px, with no page overflow. No browser script errors were observed. Inspected the updated diagram and mobile and desktop content visually. At 375 px with the root text size doubled, the page still has the same 483 px overflow as the unchanged page; this existing text-enlargement issue is outside this content revision. No complete accessibility audit or deployment was performed.

## Follow-up revision · 17 October 2026

- Replaced the legacy/emergent competency comparison with existing expertise, additional responsibilities and observable work. Examples assess flawed specifications, unsafe permission boundaries, incomplete evidence and specialist escalation. Multi-agent orchestration is an optional specialism.
- Separated QA and security contributions and competency rows, with distinct acceptance responsibilities under the existing process. Updated the delegation diagram and its text equivalents to name both reviewers.
- Added suggested ownership for the shared harness, approved models, policy content, evaluation datasets, support, incident response and ongoing funding. These responsibilities map to existing roles; they do not establish new EDS authorities.
- Expanded the pilot scorecard to publish comparable task types, review effort, rework, escaped defects, total cost and developer experience alongside baseline results. Added example evidence rules for expansion, restriction, retirement and bounded further testing.
- Retained the qualified productivity evidence, human accountability and rejection of fixed staffing ratios. Explicitly rejected smaller teams or greater autonomy as maturity measures.

Validation for this follow-up: checked HTML structure, heading order, table headers, internal anchors and local link targets, and checked the diff for whitespace errors. The existing visual styling is unchanged; no browser accessibility audit or publication was performed. The checks below describe the earlier review, not a repeated visual audit. The live page could not be retrieved; the repository copy was used as the editing source. No new empirical research claims were added.

Reviewed on 28 September 2026 against `writing.md` and `design.md`.

## Findings and changes

| Finding | Revision |
| --- | --- |
| The opening implied organisational change had to precede any value from AI. | Define transformation and the reader's task; recommend a bounded pilot with supporting changes. |
| Several claims suggested causal or universal benefits. | Identify survey associations, retain study context and separate evidence from recommendations. |
| METR's old productivity result lacked the detail of its follow-up. | Include the 16-developer, 246-task context and the February 2026 follow-up's selection and measurement limitations. |
| Role comparisons reduced existing jobs to administrative or manual tasks. | Describe illustrative contributions and outputs without inventing responsibilities or approval authority. |
| The autonomy table mixed overlapping levels and high-impact restrictions. | Replace the ranking with task-specific permission options. Higher autonomy is not presented as the goal. |
| Passing automated checks appeared to authorise progress in the control diagram. | Change the result to “Ready for decision” and explain that existing approval authority still applies. |
| Culture largely repeated the process controls. | Focus on communicating change, raising concerns, supported learning and acting on failures. |
| Technology implied new platforms and agent identities were universally required. | Start from existing capabilities; allow scoped credentials or delegated access with attributable actions. |
| The closing advice lacked measurable inputs and a decision. | Add baseline, trial boundaries, scorecard, review decision and a fictional worked example. |
| Multiple long lists repeated the same message. | Consolidate the content and remove tangential consultancy/customer-support studies and the productivity-curve detour. |

## Source review

Primary sources used in the revised chapter:

- [DORA 2025 report](https://dora.dev/research/2025/dora-report/): AI amplifies organisational conditions.
- [DORA AI Capabilities Model introduction](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model): survey-based supporting capabilities, including clear policy communication, internal data and platforms.
- [DORA organisational culture guidance](https://dora.dev/capabilities/generative-organizational-culture/): trust and information flow.
- [McKinsey 2025 survey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025): workflow redesign among its high-performer group. Retained as explicitly dated historical evidence, not the latest survey.
- [METR July 2025 trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) and [February 2026 follow-up](https://metr.org/blog/2026-02-24-uplift-update/): historical trial and limits on newer productivity estimates.
- [IMDA framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) and [May 2026 update](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai): bounding risk, traceability and deployment examples. Direct IMDA retrieval encountered a bot-verification page. The retained, narrow claims were checked against search-indexed excerpts from IMDA itself; the full framework was not reviewed. No third-party summary was used as authority for a EDS requirement.
- [OWASP Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/): minimise functionality and authority, enforce permissions in connected systems.

## Writing and design assessment

- The opening defines scope and audience; headings describe useful actions.
- Recommendations identify inputs, participants, outputs and decisions where needed.
- British English is retained. AI-PDLC, AI agent and T-shaped practitioner are explained at first use.
- Examples are labelled; the chapter makes no new claim about EDS policy or decision authority.
- Three existing inline diagrams are retained and refined, with captions and adjacent text equivalents. No extra diagram was needed: the pilot is clearer as a numbered procedure and compact scorecard.
- The existing white and neutral handbook layout, restrained blue accents and shared typography are retained.
- Draft status, review date and unresolved owner/version metadata remain visible. A real content owner and applicable lifecycle version still need confirmation before publication.
- External links and nearby citations preserve traceability. The chapter is a synthesis, not a reproduction of a source.

## Verification

The existing transformation-page checks pass: heading hierarchy, anchors, table headers, three titled diagrams, diagram text bounds, keyboard navigation, current-section indication, no-JavaScript content, 320–1440 px layout and 200% text. No browser errors or failed local asset requests were recorded. Desktop and mobile opening views and all three diagrams were also inspected visually.

This is an editorial and page-level review, not a complete accessibility conformance audit. No publication or deployment was performed.
