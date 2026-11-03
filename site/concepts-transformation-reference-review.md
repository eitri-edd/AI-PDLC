# Concepts and Organisation transformation: reference accuracy review

Reviewed on 3 November 2026 against the current working copies of [Concepts](dist/concept.html) and [Organisation transformation](dist/transformation.html).

## Scope and result

Reviewed every external URL on both pages: 37 on Concepts and 13 on Organisation transformation, with one shared training destination, giving 49 distinct URLs. This includes numbered supporting sources, the software-factory republication, learning references and the shared training link. Checked source identity and subject matter, then compared cited definitions, capabilities, findings and qualifications with the surrounding handbook claims. This is a citation-accuracy review, not a reproduction of the experiments or independent certification of provider performance.

The references support the main content. Corrections concern precision and attribution rather than replacing the bibliography. All original source URLs and anchor IDs were preserved.

## Corrections made

| Location | Finding | Correction |
| --- | --- | --- |
| Concepts: intent-driven development | The opening reduced the approach to agreeing the need before choosing a solution. The cited account also emphasises retaining explicit intent throughout agent work. | Included outcomes, behaviour and constraints, carried through planning, implementation and review. |
| Concepts: harness diagram | The handbook presents six components; Walking Labs explicitly groups its harness into five subsystems. | Identified the six-part diagram as the handbook’s synthesis and named the different grouping used by Walking Labs. No claim that the three sources prescribe a common taxonomy remains. |
| Concepts: graph review | The wording implied that separate reviewers necessarily catch defects. | Changed the claim to a capability with explicit limits: reviewers can expose defects and can also share errors or miss defects. |
| Concepts: decision-model preprint | Saying both models performed at chance was stronger than the paper’s reported failure to outperform chance. The comparator was unnamed. | Used the narrower result, named Laya, retained the nine-of-eleven scope and identified deployment findings as the paper’s self-audit. |
| Concepts: source scope and model dates | Learning resources, provider claims and research could be read as equivalent evidence. | Distinguished their roles, labelled the diagrams and evaluation procedures as synthesis, and refreshed both model-reference check dates after checking the cited providers. |
| Transformation: McKinsey survey | A majority claim was less directly traceable than the source’s comparative finding; the high-performer definition was missing. | Used the reported relative comparison and defined the group. Retained the association-versus-causation qualification. This is business-impact survey evidence, not a software-team productivity experiment. |
| Transformation: METR experiment | The intervention was allowing tools, rather than mandating a particular quantity of AI use. | Described the randomised treatment more precisely. Retained the reported result, task and participant context and follow-up limitations. |
| Transformation: IMDA | The bibliography did not identify the actual version currently returned by the PDF URL. | Recorded version 1.5, publication on 20 May 2026 and update on 5 June 2026. Added document locations and clarified that the handbook’s permission options are examples, not IMDA tiers. |
| Transformation: recommendations | Adjacent source citations could imply that studies prescribed the four-area layout, role allocation or exact pilot scorecard. | Identified these as handbook recommendations. Kept DORA’s supporting capability findings separate from the proposed pilot and adoption rules. |

## Concepts: numbered sources

The source column uses the visible citation number. The existing `source-11` anchor remains nested inside citation 10 for the republication; later visible numbers differ from their retained anchor suffixes.

| Citation | Source | Assessment |
| --- | --- | --- |
| 1 | [Intent-driven.dev: Intent-Driven Development](https://intent-driven.dev/knowledge/intent-driven-development/) | Supports explicit, durable intent and context throughout AI-assisted work. Practitioner account; revised the opening definition to preserve that scope. |
| 2 | [GitHub Spec Kit: Specification-Driven Development](https://github.com/github/spec-kit/blob/main/spec-driven.md) | Supports specifications informing plans, tasks and tests, separating behaviour from implementation choices and making uncertainty explicit. Did not adopt the source’s stronger completeness or time-saving promises. |
| 3 | [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Supports selective context, ongoing curation, retrieval and persisted notes. The handbook’s source-owner and authority checks are additional working guidance. |
| 4 | [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/) | Supports environment design, accessible repository knowledge, executable checks and feedback. An experience report about a particular internal project, not proof of universal throughput gains or a six-component standard. |
| 5 | [Walking Labs: What a harness actually is](https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/) | Supports the surrounding infrastructure and repeatable verification. Its five-subsystem taxonomy differs from the diagram; this distinction is now explicit. Its anecdotal success rates are not repeated as general evidence. |
| 6 | [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | Supports initial setup, incremental work, persistent progress, clean handovers and end-to-end checks. Does not establish the handbook’s exact diagram or a universal review policy. |
| 7 | [IBM: Loop engineering](https://www.ibm.com/think/topics/loop-engineering) | Supports repeated action, observation, adjustment, stopping criteria and saved state. The fictional code/skill experiment and paired comparison procedure are proposed handbook practice, not reported IBM experiment results. |
| 8 | [PuppyGraph: Graph engineering](https://www.puppygraph.com/learn/graph-engineering) | Supports execution graphs, state, routing, checking and the distinction from knowledge graphs. Vendor-authored explanation of an emerging term; the CSV-export graph is a fictional application. |
| 9 | [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Supports the workflow/agent distinction and parallel, orchestrator–worker and evaluator patterns. Human control and the simplest useful architecture remain relevant. Its tooling examples are historical; the handbook does not rely on their being current. |
| 10: original | [Addy Osmani: Software Factories, Light and Dark](https://addyosmani.com/blog/software-factories/) | Confirmed title, author and 20 July 2026 date. Supports the review-arrangement distinction and warnings about declining comprehension. The handbook adds local authorisation and recovery conditions. |
| 10: republication | [O’Reilly: Software Factories, Light and Dark](https://www.oreilly.com/radar/software-factories-light-and-dark/) | Confirms the 18 September 2026 date and explicit authorised republication. Correctly treated as the same article, not independent corroboration. |
| 11 | [OpenAI: GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) | Confirms the described reasoning/coding/tool capabilities, configurable reasoning, text/image input and text output. Provider documentation, not an independently demonstrated ranking. |
| 12 | [Gururangan et al.: Don’t Stop Pretraining](https://aclanthology.org/2020.acl-main.740/) | Confirms title, authorship and 2020 publication. Domain/task pretraining gains concern four domains and eight classification tasks. No universal specialist-model advantage is asserted. |
| 13 | [Wu et al.: BloombergGPT](https://arxiv.org/abs/2303.17564) | Confirms the 2023 paper, 50-billion-parameter example and financial/general training mixture. Claims remain limited to reported evaluations. |
| 14 | [Abdin et al.: Phi-3 Technical Report](https://arxiv.org/abs/2404.14219) | Confirms the 2024 report, Phi-3-mini’s scale, filtered/synthetic data and phone-deployment feasibility. The handbook does not promise speed or privacy solely from size. |
| 15 | [Yu et al.: Distilling System 2 into System 1](https://arxiv.org/abs/2407.06023) | Supports training on reasoning-derived outputs for direct responses, with gains in the evaluated settings. Correctly distinguished from TypeSafe’s product interface. |
| 16 | [OpenAI: GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) | Confirms coding/professional-work use, reasoning controls and the stated modalities. Listed token rates are lower than Astra’s; this does not guarantee a lower total task cost. |
| 17 | [Anthropic: Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview) | Confirms task positioning, text/image input, text output, adaptive thinking, effort controls and active status. No unsupported comparative benchmark claim was added. |
| 18 | [Anthropic: Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview) | Confirms agentic coding/knowledge-work positioning, adaptive thinking and documented capabilities. Thinking remains enabled; the handbook does not claim that it can be disabled. |
| 19 | [Anthropic: Transparency Hub](https://www.anthropic.com/transparency) | Confirms model reports, safety assessments and links to matching system cards. Correctly presented as provider evidence with limitations. |
| 20 | [OpenAI: Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) | Supports reasoning controls and model/tool guidance. This is a moving URL, so the page directs readers to check the exact version and current documentation. |
| 21 | [TypeSafe: Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | Supports attribution of the interface and provider performance claims. The handbook appropriately rejects an inference that typed output establishes factual correctness. |
| 22 | [TypeSafe: System One](https://docs.typesafe.ai/concepts/system-one) | Confirms text-only state input, constrained decisions/probabilities and composition within application code. |
| 23 | [TypeSafe: Primitives](https://docs.typesafe.ai/primitives) | Confirms Choice, Score and Noul, ordered score levels and independent questions evaluated against shared state. Dependent questions need a subsequent request. |
| 24 | [TypeSafe: Confidence](https://docs.typesafe.ai/confidence) | Confirms distribution-derived confidence for Choice/Score and no separate confidence field for Noul. Local threshold and calibration checks remain recommendations, not proof of correctness. |
| 25 | [Li: Fast Models, Slow Evidence](https://arxiv.org/abs/2610.02267) | Confirms title, Jiawei Li authorship and October 2026 preprint. Corrected the routing result’s wording and identified the comparator and self-audit scope. Not presented as peer-reviewed or universal validation. |

## Concepts: additional learning destinations

These descriptions identify what the resources cover. They do not endorse every linked lesson’s product instructions, marketing claim or default policy.

| Destination | Assessment |
| --- | --- |
| [CircleCI: Intent-driven development](https://circleci.com/blog/intent-driven-development/) | Covers objectives, constraints, success criteria and keeping intent available through planning, implementation and validation, as described. |
| [AI Agent Factory: Spec-driven development](https://agentfactory.panaversity.org/docs/spec-driven-development-crash-course) | Covers specifications, clarification, plans and task breakdown. Tool-specific details are supplementary learning material. |
| [Context-engineering resource collection](https://github.com/mlnjsh/context-engineering) | Contains techniques, research links and a learning roadmap. A curated collection, not original empirical evidence. |
| [Intent-driven.dev: Context engineering](https://intent-driven.dev/knowledge/context-engineering/) | Covers structuring requirements, constraints, examples and domain knowledge. Does not prove that context prevents all implementation errors. |
| [Walking Labs: Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) | Provides lectures, hands-on projects and copy-ready templates, matching the learning description. |
| [AI Agent Factory: Harness engineering](https://agentfactory.panaversity.org/docs/harness-engineering-crash-course) | Covers constraints, verification and failure-driven harness improvements. Its exercises are learning resources, not EDS policy. |
| [Iwo Szapar: Loop Engineering Playbook](https://www.iwoszapar.com/resources/loop-engineering-playbook/access) | Includes a design canvas, verifier checks, retry limits and human gates. The stated canvas description is accurate. |
| [AI Agent Factory: Loop engineering](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course) | Covers triggers, durable progress, checks and run limits as described. No claim that its tool configuration is universally applicable. |
| [AI Agent Factory: Graph engineering](https://agentfactory.panaversity.org/docs/graph-engineering-crash-course) | Covers fan-out, verification, fan-in and handling missing results. The short course description is accurate. |
| [Vercel Academy: Creating a Software Factory](https://vercel.com/academy/creating-a-software-factory) | An implementation course with risk routing, evidence, isolated builds and verification. Correctly linked for learning, not cited as measured universal benefit. |

## Organisation transformation: numbered sources

| Citation | Source | Assessment |
| --- | --- | --- |
| 1 | [DORA: State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/) | The report page explicitly describes amplification of existing organisational conditions. Retained that attribution without claiming a universal causal effect. |
| 2 | [McKinsey: The state of AI in 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025) | Confirmed the November survey’s high-performer definition and relative workflow-redesign finding. Corrected the summary for traceability. The historical 2025 survey is intentionally retained rather than silently replaced by a newer survey. |
| 3 | [METR: Early-2025 developer productivity study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | Confirmed the randomised setting, 16 experienced contributors, 246 repository tasks, 19% longer completion and contradictory participant perceptions. Clarified the allowed-tools intervention. |
| 4 | [METR: February 2026 design update](https://metr.org/blog/2026-02-24-uplift-update/) | Confirms selection, recruitment, task submission and concurrent-work timing limitations. Supports caution about the magnitude of current productivity effects, not an inference that no speedup exists. |
| 5 | [IMDA: Agentic AI governance framework PDF](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) | Downloaded the current 53-page PDF. Cover confirms version 1.5 and both dates; page 5 lists additions; page 13 states the four governance dimensions. Sections 2.1–2.3 support bounded authority, accountability and lifecycle controls. |
| 6 | [IMDA: Updated framework factsheet](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai) | Official indexed text confirms the 20 May update, case studies and new practices. The directly downloaded PDF independently confirms the additions and identifies the later June update. |
| 7 | [DORA: Generative organisational culture](https://dora.dev/capabilities/generative-organizational-culture/) | Supports the association of high trust and effective information flow with delivery and organisational performance. The page’s practical retrospective instructions are adaptations. |
| 8 | [DORA: AI Capabilities Model introduction](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model) | Confirmed 23 September 2025 publication and the capabilities used: communicated AI position, internal data and platform quality. Does not prescribe the handbook’s exact pilot, staffing or adoption scorecard. |
| 9 | [OWASP: LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) | Supports minimising functionality, permissions and autonomy; authorisation in downstream systems; appropriate approval; monitoring and limits. Accurate summary. |
| 10 | [Microsoft Cloud Adoption Framework: Automation](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/automation) | Supports versioned infrastructure code, peer review and CI/CD validation. Allocation to the proposed Platform / Cloud Engineer role is now expressly distinguished from the source. |
| 11 | [Microsoft Cloud Adoption Framework: Security roles](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles) | Supports shared responsibility across engineering, platform and security functions, adjusted to organisational size. Does not mandate the handbook’s staffing structure. |
| 12 | [DORA: Monitoring and observability](https://dora.dev/capabilities/monitoring-and-observability/) | Supports health and user-experience signals, operational diagnosis and developer access to observability. The proposed owner/support allocation remains local working guidance. |

## Shared navigation destination

[Foundations of Agentic Engineering training](https://sgtechstack.github.io/ai-coding-workflow-d2-self-paced-training/) returned its published prerequisite/course page through direct retrieval. Both navigation links identify it as training; no additional research claim is attributed to it.

## Retrieval and validation

Used the original publishers’ pages and official documentation. Checked bibliographic details and paper abstracts for the bounded research claims; no claim of reproducing their experiments is made. Checked relevant sections of longer practitioner and course material rather than treating a successful URL response as verification.

The web reader returned an anti-bot page for IMDA. A normal direct download returned the complete framework PDF; extracted its text and checked the relevant document pages. The factsheet’s substantive content was available in the official indexed result, while direct HTML did not expose the full article text. The framework PDF corroborates the claims used here. The web reader also failed on the shared training site; direct retrieval returned the published page. No CAPTCHA was solved and no login or restricted content was accessed.

Local checks passed: 183 local link/asset references, unique and preserved anchor IDs, preserved external URLs and SVGs, citation numbering including the republication alias, matching desktop/mobile contents, reading without JavaScript, and Chromium layouts at 1440, 768, 375 and 320 pixels. No browser errors or failed local requests occurred. Visually inspected the harness explanation and transformation evidence summary at desktop and mobile widths. Whitespace checks passed.

Changes remain local and unpublished. Unrelated working-tree edits were preserved. This review does not establish current EDS policy, approved model access, or a confirmed handbook content owner/lifecycle version.
