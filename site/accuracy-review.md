# Handbook accuracy and reference review

Reviewed on 2 November 2026.

All 13 HTML pages in `site/dist/` were examined, including the retained, unlinked training companion. The original pages cite 100 distinct external URLs. Each URL was requested: 97 yielded readable content, one returned a JavaScript application without readable text, and two IMDA references returned verification challenges. These are retrieval results, not a claim that every statement within every external source is correct.

The public technical descriptions are broadly consistent with their cited sources. Corrections focus on overgeneralised training claims, source attribution, version-dependent workflow claims and the difference between reviewing a control and enforcing it. Current Eitri implementation status cannot be certified from public references alone.

## Page findings and disposition

| Page | Review result |
| --- | --- |
| Introduction | Task routes, evidence and human accountability remain consistent with the detailed pages. No factual correction required. |
| AI-SDLC overview | Retained the local two-loop lifecycle as the handbook's model. Replaced the unsupported fixed Defence Playbook version label with “live web edition”. Added the same plateau/maintenance qualification already present in discovery: an essential service can sustain value without a rising headline metric. |
| Organisation transformation | Retained the bounded interpretation of METR's 2025 experiment and February 2026 update, and the distinction between correlation and causation in the survey findings. DORA's linked introductory capability article is dated September 2025; the later report is distinct. IMDA's May update date is corroborated by official indexed information, but the complete framework could not be re-read. |
| Concepts | Rechecked the named OpenAI and Claude models against live provider documentation and refreshed the two model-example check dates. Current descriptions of TypeSafe's Choice, Score, Noul and confidence fields agree with its documentation. Historical domain-adaptation, BloombergGPT, Phi-3 and distillation papers remain appropriate conceptual examples; they are not presented as the newest models. Retained course links as learning resources. |
| Product discovery | Reviewed research, four-risk attribution, experiments, evidence limits, handoff and measurement guidance against the originating framework references, NIST and Amplitude. Retained the fictional example and its explicit sampling limits. No change to the six-step process required. |
| Product implementation | The PRD/TRD names and six stages remain local working conventions, rather than a claim about a universal standard. The five named DORA metrics match the current DORA guide. Canary and agent-evaluation guidance remains appropriately bounded. Updated the Anthropic evaluation link to its redirected destination. |
| EDS workflow | Replaced the generic SDD citation for SPDD with the method's primary author account. Attributed the organisational direction to the Eitri training, and replaced assumed compatibility with a check against the target workflow. Added version scope for workflow and availability claims. |
| PO/BA harness | Linked GitHub's Spec Kit directly to its repository. Distinguished EDS's documented Confluence path from the upstream CLARA core, which also supports Plane. Retained the three local handoff paths. |
| Developer harness | Removed the implication that declared dependencies alone make parallel changes safe. Qualified independent-review claims and the scope of IM8. Retained 80% coverage and 70% mutation thresholds as documented, configurable harness defaults. Added version scope. |
| Path to production | Clarified that local pre-commit hooks can be bypassed, and recommended shared-pipeline enforcement for required controls. Preserved the documented four-stage route and human decision. Added version scope. |
| Team context | Removed categorical context-window and correct-behaviour claims. Distinguished Markdown audit input from executable enforcement. Clarified that 36 IM8 and 88 ARC are counts in the documented Eitri checklists, not independently established totals for the entire current frameworks. |
| Skills catalogue | Added the upstream base-skills link and revision guidance. Scoped availability to the documented installation. Clarified the packaged policy counts. |
| Training companion | Corrected the universal “40%” threshold, memory and weights descriptions, step-by-step prompting advice, absolute planning and testing claims, and attribution of orchestration restrictions to Anthropic. Added explicit bounded-loop stopping conditions, host-dependent skill invocation and direct primary references. Preserved the training's older command names and five-phase layout with a version note. |

## Evidence that matters for the corrections

- [OpenAI model catalogue](https://developers.openai.com/api/docs/models), [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview) and [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview): the named examples remain documented. No unsupported model replacement or claim of universal superiority was added.
- [TypeSafe primitives](https://docs.typesafe.ai/primitives) and [confidence](https://docs.typesafe.ai/confidence): typed answers and confidence statistics have different meanings. The separate [Jev/Laya evaluation preprint](https://arxiv.org/abs/2610.02267) supports task-specific limitations; it is not peer-reviewed deployment assurance.
- [SPDD by Wei Zhang and Jessie Jie Xia](https://martinfowler.com/articles/structured-prompt-driven/): the primary account describes maintained prompt artefacts, alignment and iterative review. It cannot establish EDS adoption decisions or Eitri compatibility.
- [CLARA core](https://github.com/dsta-productops/clara): the shared core has Plane and Confluence adapters. The [EDS context lesson](https://sgtechstack.github.io/ai-coding-workflow-d2-self-paced-training/02-team-context-ingestion.html) still describes the Confluence deployment.
- [Lost in the Middle](https://arxiv.org/abs/2307.03172): evidence concerns position sensitivity on the tested tasks and models, not a universal 40% utilisation limit. [Anthropic context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) describes retrieval, compaction and durable notes.
- [OpenAI reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices): explicit chain-of-thought prompting is not a general recommendation for reasoning models. [Agent Skills specification](https://agentskills.io/specification): progressive disclosure is documented; invocation depends on the host.
- [Anthropic agent patterns](https://www.anthropic.com/research/building-effective-agents): orchestration includes decomposition, delegation and synthesis; it does not forbid a coordinator from reading files.
- [Current DORA metrics](https://dora.dev/guides/dora-metrics/): five measures, including failed deployment recovery time and deployment rework rate. Existing implementation wording matches.
- [Live Eitri skills lesson](https://sgtechstack.github.io/ai-coding-workflow-d2-self-paced-training/01-eitri-skills.html): supports the 80% and 70% defaults and the documented 36/88 checklist split. These numbers are version-dependent.
- [ARC controls guidance](https://govtech-responsibleai.github.io/agentic-risk-capability-framework/arc_framework/controls/): applicability and residual risk need assessment. A model's document audit does not establish runtime enforcement.

## Items requiring internal confirmation

The checkout does not contain the `../harness-workflow/` source documents cited by the earlier EDS review. Public training is accessible, but its `/dependency-orchestrator` and five-phase structure differ from the local catalogue's `/project-horizon` and 19-step view. These may represent different revisions; neither was silently substituted for the other.

The workflow owner should provide the applicable harness revision, policy-pack versions, current skill catalogue and pipeline configuration. Confirm Available/Planned labels, Stitch/HTML conversion, Context7/Sonar integration, control coverage, gate enforcement and sign-off authorities against that revision. An audit report, a public product homepage or a passing model review cannot establish those implementation facts.

The current organisational SPDD adoption plan also needs owner confirmation. Retained skill and workflow descriptions remain explicitly scoped to the documented setup.

## Reference retrieval limitations

The full original reference inventory, affected pages, retrieval methods and exceptions are recorded in [reference-checks.json](reference-checks.json). The ledger preserves original URLs even where the handbook now uses a canonical destination.

The training site, Defence Product Playbook, Figma Make and LINDDUN returned readable public content through direct HTTP retries after web-reader failures. No broken link was inferred solely from a failed tool request.

Google Stitch returned an application shell with no readable lines. Both cited IMDA endpoints challenged the web reader; direct HTTP returned a sparse shell rather than the complete framework. Official indexed information corroborates the January publication and May update, but full current framework content/version remains unverified. These references were retained rather than replaced with an assumed document.

New references used by the corrections were also opened. Existing historical papers and dated research were retained where they explain the underlying concept; “latest” does not require replacing sound foundational sources.

## Validation

Passed: all 13 pages loaded at 320 px and 1440 px (26 viewport checks), with no JavaScript page errors or page-level horizontal overflow. All 821 internal link occurrences resolved, including fragments. Each page has one H1; no duplicate IDs or missing aria-labelledby targets were found. Visually inspected the revised training and policy content in saved screenshots. Git diff whitespace validation passed. The final HTML contains 101 distinct external URLs; each has a retrieval record or a checked canonical/new-source entry. This is a content and reference review, not a certification of organisational policy, a live Eitri execution test or a complete accessibility audit.
