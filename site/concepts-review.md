# Concepts editorial review

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
