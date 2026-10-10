# Concepts editorial review

## Models · 11 October 2026

Added Models before the seven development practices, with entries in both contents menus. The summary separates scale (large/small), specialisation (general/domain-specific) and response approach (System One/more deliberative reasoning). These dimensions overlap; they are an editorial synthesis rather than a formal taxonomy. System One is interpreted as the research term System 1, not a named vendor product. No universal SLM parameter cutoff is imposed.

Research references were opened on 11 October 2026 and are cited beside the relevant explanations and in Sources, with their contribution stated:

| Reference | Contribution and scope |
| --- | --- |
| [Brown et al., 2020](https://arxiv.org/abs/2005.14165) | LLM capabilities through instructions/examples and the 175-billion-parameter GPT-3 example. Historical study, not a current ranking. |
| [Gururangan et al., ACL 2020](https://aclanthology.org/2020.acl-main.740/) | Continued domain/task pretraining; evidence from four domains and eight classification tasks. |
| [Wu et al., 2023](https://arxiv.org/abs/2303.17564) | BloombergGPT as a 50-billion-parameter domain model using financial and general data. Domain specialisation does not imply small size. |
| [Abdin et al., 2024](https://arxiv.org/abs/2404.14219) | Phi-3-mini as a 3.8-billion-parameter model, training-data quality and phone deployment feasibility. No promise of equivalent capability on every task. |
| [Yu et al., 2024](https://arxiv.org/abs/2407.06023) | System 2 intermediate reasoning versus System 1 direct responses; successful distillation for several tested techniques, not a universal replacement for reasoning. |

The service-request example and model evaluation advice are editorial recommendations. Distinguish model adaptation from retrieval, a subject domain from a programming DSL, and local deployment from a privacy guarantee. Retained existing edits and the established site layout. The README mentions `plan.md`, which is absent; the available writing and design standards were used.

Validation: both contents menus link to Models; all five new source IDs resolve; no duplicate IDs or unresolved internal anchors; section opening/closing counts match; whitespace checks pass. No browser rendering check was performed for this content-only addition.

## Web application examples · 11 October 2026

Reviewed the examples for concrete browser behaviour, server responsibilities and a clear distinction between the seven concepts. Replaced generic test-suite repair, documentation renaming and formatting automation with fictional service-request web application scenarios. These are original examples, not claims about the repository or a production system.

- Intent: preserve unfinished form work; compare explicit saving with automatic saving without assuming the solution.
- Specification: define incomplete drafts, successful and failed saves, ownership enforcement and conflicting updates from two browser tabs.
- Context: connect a status filter’s meaning to current status values, URL state, the API contract and access rules.
- Harness: supply browser tools, a local app/API, test storage, saved state and observable upload evidence.
- Loop: reproduce out-of-order search responses, adjust the implementation and stop on verified results, blockage or an illustrative attempt cap.
- Graph: agree an API contract, separate frontend/backend work, join their outputs and verify the combined candidate. Updated Figure 6 and its text equivalent to match.
- Factory: route a queue of web-app issues through isolated work, checks, previews, review, release and operational feedback. Distinguish preview deployment from unattended production release.

Updated the fourteen application ideas to use these web scenarios. Retained the concept-focused structure and learning-reference list. Local links and whitespace checks passed; browser checks cover section structure, internal anchors and the revised graph.

## Concept-focused revision · 11 October 2026

Following the revised brief, the page now follows the concept-page structure in `writing.md`: definition, recognisable problem, explanation, example, limits and a useful next step. Removed the study route, shared exercise setup, learning outcomes, timed exercises, saved-output prompts and self-checks. Retained the seven conceptual explanations and figures, including the six-part harness diagram.

Replaced lessons with two possible applications per concept. These are concise ideas for team discussion, each naming an action and an observable result. They cover comparing solutions against intent, making requirements testable, improving task context, addressing harness failures, bounding repetition, identifying dependencies and piloting a small work queue. The ideas are editorial suggestions informed by the previously reviewed references, not reproduced course instructions.

Grouped all supplied learning links by concept in one list, with brief descriptions. Retained citations beside explanatory claims and supporting sources separately. No new external claims or performance promises were introduced. This revision supersedes the learning-page structure described below.

## Learning revision · 11 October 2026

Refined the existing concepts page to support understanding and practice. Preserved the working-tree navigation and AI-SDLC/EDS terminology. Each of the seven concepts now has an observable learning outcome, a three-step exercise, an output to retain, a self-check and a relevant training path. Estimated exercise times exclude setup and external courses. One fictional search-filter bug connects the exercises; design walkthroughs are explicitly distinguished from executed checks.

The harness figure is an original inline SVG adaptation of the user-supplied image: agent state, tools, memory, orchestration, safety and observability. Its caption credits the supplied reference, and prose explains every component and how they work together. The duplicate rate-limit label is consolidated. A vector database is described as optional, and external memory is distinguished from information currently available to the model. This six-part map replaces the previous five-part teaching model; it is not presented as a universal standard.

All eleven distinct URLs supplied for this revision were opened. The content and training links appear beside their relevant concepts and in the source list:

| Concept | Revision references and use |
| --- | --- |
| Intent | [CircleCI](https://circleci.com/blog/intent-driven-development/): preserve desired outcomes and constraints as plans change; distinguish intent from the specification carrying it. |
| Specification | [AI Agent Factory](https://agentfactory.panaversity.org/docs/spec-driven-development-crash-course): clarify behaviour before implementation and practise specification, planning and tasks. |
| Context | [intent-driven.dev](https://intent-driven.dev/knowledge/context-engineering/): deliberately structure requirements and supporting information. [mlnjsh resource collection](https://github.com/mlnjsh/context-engineering): techniques and roadmap, accurately labelled as a collection rather than an assessed course. |
| Harness | [Walking Labs](https://walkinglabs.github.io/learn-harness-engineering/en/): environment, continuity and verification, with baseline/minimal-harness projects. [AI Agent Factory](https://agentfactory.panaversity.org/docs/harness-engineering-crash-course): controls and practice projects. The six components themselves come from the supplied image. |
| Loop | [Iwo Szapar playbook](https://www.iwoszapar.com/resources/loop-engineering-playbook/access): a practice canvas and check/stop decisions. [AI Agent Factory](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course): recurring triggers, saved progress and maker–checker separation. |
| Graph | [AI Agent Factory](https://agentfactory.panaversity.org/docs/graph-engineering-crash-course): independent branches, checking and merging. The local exercise adds explicit candidate versions, stale evidence and failed/missing-result traces. |
| Factory | [Addy Osmani](https://addyosmani.com/blog/software-factories/): light/dark review choices. [Vercel Academy](https://vercel.com/academy/creating-a-software-factory): work-order outcomes, scoped work and reviewable candidates; implementation prerequisites remain with the course. |

External tutorials were treated as reference material, not as instructions to execute their workflows in this repository. New exercises and example limits are editorial teaching choices, not organisational policy or claims of measured improvement. Earlier references remain separately labelled as further reading; their full historical source review is below.

Validation for this revision: seven exercises, seven self-checks and seven accessible figures; no duplicate HTML IDs or unresolved internal anchors. Browser inspection confirmed narrow-screen reflow and desktop layout, keyboard activation of a self-check and no reported browser errors. The harness text label was shortened after visual inspection to fit its box. This is a focused content/layout check, not a full accessibility audit.

## Previous review · 28 September 2026

Reviewed 28 September 2026 against `../writing.md`, `../design.md` and the online sources below. Updated `dist/concept.html` in place.

## Findings and changes

- Retained the seven standalone concepts, examples, diagrams and next steps. Replaced the opening's implied ladder towards autonomy with an explanation of overlapping concepts.
- Intent: added a decision point for unresolved questions. Specification: replaced “a few seconds” with a clearly illustrative, measurable export criterion.
- Context: retained the distinction between a prompt and the evolving working information available to a model, including durable decisions and source authority.
- Harness: added Walking Labs' five-part teaching model (instructions, tools, environment, state and feedback), a linked audit exercise, and a distinction between test evidence and acceptance decisions. Retained primary engineering accounts alongside the course.
- Loop: separated successful completion, blockage and budget exhaustion. Removed the implication that a second agent guarantees a more reliable result.
- Graph: clarified that an execution graph can contain ordinary functions and one agent. Removed claims that a single agent is necessarily limited to one context window or that a separate verification node establishes independence. Explained runtime enforcement and resumption concerns.
- Factory: removed universal claims that generation and checks are cheap and human review is the only costly activity. Replaced the lint-to-production example with a bounded pilot. Distinguished human review from automated release decisions. Corrected the figure's light-path arrow to point to review and its monitoring return to point to the queue.

## Source mapping

Sources were opened and reviewed on 28 September 2026. Links appear near the relevant explanation on the page.

| Concept | Sources and scope |
| --- | --- |
| Intent | [Intent-Driven Development](https://intent-driven.dev/knowledge/intent-driven-development/): explicit, durable intent. The four-question exercise is editorial guidance. |
| Specification | [GitHub Spec Kit](https://github.com/github/spec-kit/blob/main/spec-driven.md): specification, plan and tasks; behaviour versus implementation choices. No productivity claims adopted. |
| Context | [Anthropic: Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): selecting and maintaining working context, retrieval and continuity. |
| Harness | [Walking Labs: What a harness actually is](https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/): its own five-part teaching framework and audit exercise. [OpenAI's engineering account](https://openai.com/index/harness-engineering/): environment, documentation and feedback. [Anthropic's long-running agents experiment](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): progress records, incremental work and end-to-end checks. |
| Loop | [IBM: Loop engineering](https://www.ibm.com/think/topics/loop-engineering): goal, action, observation and adjustment. Specific caps and example tasks are illustrative. |
| Graph | [PuppyGraph](https://www.puppygraph.com/learn/graph-engineering): terminology for execution graphs. [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): routing, workflows and starting with the simplest adequate structure. |
| Factory | [Addy Osmani](https://addyosmani.com/blog/software-factories/), also [republished by O'Reilly](https://www.oreilly.com/radar/software-factories-light-and-dark/): light/dark terminology and comprehension risk. Treated as a practitioner account, not a measured universal delivery model. |

The Walking Labs course includes performance anecdotes and product comparisons that were not independently established here; these were not adopted. No organisational roles, approval authorities or mandatory practices were invented. Draft ownership and lifecycle-version fields remain unresolved and visible.

## Presentation and verification

Reused the shared white/neutral canvas, blue links, system typography, reading column and heading hierarchy. Essential explanations remain visible in prose; each diagram retains its accessible title, caption, text equivalent and focusable horizontal scroll region.

The existing `.preview/check-concepts.cjs` passes: seven sections and figures, next steps, anchor targets, selected navigation, keyboard operation, 320–1440 px reflow, 200% text, no-JavaScript content and no browser errors. Visually inspected the revised factory figure and harness content at mobile width. These checks do not constitute a full accessibility conformance assessment.
