# Organisation transformation: editorial review

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
