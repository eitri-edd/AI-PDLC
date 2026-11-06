# Writing standard

## Purpose

Help readers understand a practice, decide when to use it, and complete the next step. Write for product owners, engineers, designers and reviewers who bring different levels of AI experience.

This document proposes house rules for the site. It does not establish EDS policy or prescribe an approved lifecycle. Examples are illustrative; validate roles, requirements and lifecycle stages against the organisation’s actual process before publishing.

## Scope and authority

In this guide, AI-SDLC means the software development lifecycle supported by AI tools and agents. It covers Project Discovery, implementation, release and learning from use. The resulting product may or may not contain AI. This is the guide’s house definition; distinguish it from a named methodology when discussing an external source.

This file is the authoritative writing standard for the site. Other authoring documents should link here rather than duplicate its rules. If an existing summary differs, follow this file and correct the summary when maintaining that document.

Editorial requirements govern how authors prepare guidance. Organisational requirements govern delivery work and need a confirmed authority. An editorial instruction to explain a decision does not create a new approval gate or assign decision authority.

## Write for the reader’s task

Before drafting, identify the intended reader, what they already know and what the page will help them understand or do. A role name alone does not establish someone’s AI experience. State prerequisites where they affect the reader’s ability to follow the page.

Start with a familiar problem and explain the mechanism before introducing specialist labels. Build from the reader’s existing knowledge, with a short example where an unfamiliar relationship needs explanation. Link to optional detail without making the reader leave the page to understand its main point.

Keep general principles, operating guidance and the current Eitri implementation distinguishable. Explain whether a statement describes a concept, an agreed organisational practice or a tool-specific implementation. Give readers a clear route from understanding the concept to trying or applying it.

## Voice and tone

Sound like a knowledgeable colleague explaining work clearly. Be calm, direct and precise. Give readers enough context to make a decision without making them decode organisational language.

| Quality | Apply it | Avoid |
| --- | --- | --- |
| Clear | Name the action and the person responsible. | Abstract phrases that conceal who does the work. |
| Practical | Explain the input, action and expected output. | Advice such as “ensure quality” without a check. |
| Measured | State what a practice can help achieve and its limits. | Claims that AI guarantees speed, quality or safety. |
| Respectful | Explain unfamiliar terms without assuming inexperience. | “Obviously”, “simply”, “just” and “as everyone knows”. |
| Accountable | Distinguish evidence, advice and requirements. | Presenting a suggestion as an organisational mandate. |

Use “you” for an instruction the reader can perform. Use a role name when ownership matters. Use “we” only when its meaning is explicit; it must not imply an official EDS position without a supporting source.

Describe what a model or agent generates, retrieves, checks or executes. Explain the observable behaviour instead of attributing beliefs, intentions or accountability to the AI.

## Sentence and paragraph rules

- Prefer active voice: “The product owner records the decision.”
- Put the main point before qualifications. Follow it with the reason or example.
- Aim for 15–25 words per sentence. Treat this as an editing prompt, not a rigid limit.
- Keep one main idea per paragraph, usually in two to four sentences.
- Vary sentence length and openings. Use a short sentence for emphasis when useful; do not turn an explanation into a succession of clipped statements.
- Connect ideas by explaining the relationship, such as a cause, consequence or condition. Use a transition when it helps, rather than adding one mechanically to every paragraph.
- Replace noun-heavy phrases with verbs: “review the evidence”, rather than “conduct an evidence review exercise”.
- Name the referent when “it”, “this” or “they” could mean more than one thing.
- Explain a specialist term at first use. Keep the precise term when a simpler replacement would change its meaning.
- Remove repeated introductions, promotional claims and conclusions that merely restate the opening.

Read difficult passages aloud. Revise wording that sounds stiff, obscures the relationship between ideas or requires a second reading. Sentence and paragraph lengths are editing prompts; understanding takes priority over a word count.

## Avoid redundant disclaimers

Keep a qualification when it changes what readers can infer, decide or do. Remove it when it only repeats a status or distinction already clear in context.

- Explain the guide’s status once under Introduction’s “Read the guide in three layers”. Link to “About this guidance” from other pages instead of repeatedly saying that practices are recommendations, citations are not endorsement or the guide does not establish policy.
- Attribute sources positively: identify the practice being used and any material adaptation. Replace repeated statements about what a source does not prescribe with a concise description of what this guide adds or changes.
- Keep research limitations beside the claims they qualify. Preserve operational boundaries, approval authority, availability labels, source credits and licence notices where readers need them.
- Label a worked example as fictional and explain its illustrative data once. Keep a short fictional label on independently linked examples and diagrams that could be read or shared without that introduction; avoid repeating the full explanation.
- Put publication metadata and adaptation history in source notes. Maintain shared Eitri version-check guidance in one reference, with compact links from other pages. Keep specific Available/Planned states and consequential control limits beside the affected steps.

Judge repetition by the reader’s likely entry point. A shared explanation can replace generic boilerplate, but it cannot replace a warning needed to interpret a result or perform the current action.

## Check coherence on every edit

After every edit, reread the affected passage and its surrounding text. Scale the wider review to the change: a spelling correction needs a local check; a change in meaning, terminology or workflow also needs a review of the page’s opening, headings, next step and dependent linked guidance. A sentence can be accurate on its own and still interrupt or contradict the explanation.

- Give each paragraph a clear purpose and connect it to the next. Introduce ideas before relying on them, and remove abrupt topic changes or repeated explanations.
- Keep terminology, roles, step names, example data and artefact identifiers consistent across prose, tables, diagrams and linked procedures.
- Check that outputs support the next action, and that conditions, exceptions and decision authority agree throughout the affected workflow.
- After shortening or moving text, repair references and transitions. Confirm that captions, source notes and directly linked sections still give readers enough context.

Treat this reread as part of completing every edit. Revise any gap, contradiction or unnecessary repetition before marking the change complete.

## Make guidance actionable

Apply this editorial rule to every procedure, review activity and decision check: give readers enough detail to carry out the work and recognise when it is complete. A heading such as “Check accuracy” does not provide the method.

Answer these questions in the surrounding passage:

- **Who acts?** Name the role or address the reader directly. Identify the decision owner when the activity leads to a decision.
- **What do they use?** Name the input, source record or version they need.
- **What do they do?** Use concrete verbs and describe the comparison, observation or test. Replace “validate”, “ensure” or “review” used alone with the actual check.
- **How do they judge the result?** Explain what supports the conclusion and what would leave it uncertain or require further work. Use confirmed criteria where available; label suggested criteria as recommendations.
- **What do they record?** Name the result, evidence link, unresolved question or updated artefact.
- **What happens next?** State the decision, follow-up action or route for unresolved findings.

Keep the detail proportional to the task. A simple instruction can answer several questions in one sentence. Do not repeat information already clear in the section or add six labelled fields to every paragraph. Use a short list when a review contains several distinct checks; number it only when order matters.

For research and AI-generated summaries, explain how to compare claims with original records. Include relevant checks for duplicate counts, missing or contradictory evidence, and the difference between an observation and a proposed explanation. State what the reviewer retains and how unresolved claims affect the next decision.

Use one short, labelled example when readers could still confuse two ideas or misapply the instruction. Show the original statement, what the evidence supports and what still needs checking. Explain unfamiliar terms in everyday language before relying on them in the steps.

## Language and terminology

Use British English in authored prose: “organisation”, “prioritise”, “behaviour” and “programme”. Preserve official product names, code identifiers and quoted titles.

Use established software development lifecycle (SDLC) terminology for engineering concepts and explain specialist terms at first use. Keep the term precise while making its meaning concrete: “Regression testing reruns related workflows to detect unintended effects of a change.” Avoid replacing a useful engineering term with a vague word such as “checks”, or adding jargon that does not help the reader perform the task.

| Term | House usage |
| --- | --- |
| AI-Software Development Lifecycle | The displayed site title. Use it on the home page and in formal references; explain its scope using the house definition above. |
| AI-SDLC | Introduce after the full title on a page that uses the abbreviation. Prefer “the lifecycle” in nearby prose. |
| AI-DLC | When referring to AWS’s AI-Driven Development Lifecycle methodology, use its name and abbreviation with a source. Do not treat AI-DLC as an interchangeable spelling of this guide’s AI-SDLC. |
| Project Discovery | Research needs, compare opportunities and test concepts to inform an investment decision. Ideation means generating options within Project Discovery. Project Discovery can continue as implementation and use reveal new questions. |
| Pilot project | Use “pilot project” for the project trialling the application. State its scope separately; avoid “one-project pilot”. |
| AI-assisted development | Development work supported by AI tools. Do not assume the resulting product contains AI. |
| AI product | A product whose behaviour includes an AI capability. Explain that capability where relevant. |
| AI agent | Software that uses an AI model to choose or adapt actions and tool use towards a goal, within agreed permissions and limits. A workflow can combine agents with predefined code paths and automated checks. |
| AI model | A trained computational model used to produce outputs from inputs. Distinguish the model from the application, tools and controls around it. |
| AI assistant | A user-facing application or capability that helps a person perform tasks using AI. Explain whether it suggests content, uses tools or delegates work to agents. |
| Workflow | An arrangement of activities, dependencies and decision points. For a predefined workflow, code or configured rules determine the route; an agent can choose or adapt actions within its permitted scope. This is the distinction adopted by this guide. |
| Context | Information supplied or made available to a model for the current task. Name the relevant instructions, records or other inputs. |
| Retrieval | Finding and selecting information from a source for use in the task. Retrieval supplies context; it does not establish that the retrieved material is correct or sufficient. |
| Memory | Information retained for later use by an application or agent. Explain what is stored, how it is retrieved and its lifetime; do not assume model calls retain earlier interactions. |
| Artefact | A recorded output of work. Prefer the specific name, such as “evaluation report”, when known. |
| Testing | Exercising software or a system under stated conditions and comparing observed results with expected behaviour. Name the cases and expected results. |
| Evaluation | A structured assessment against defined criteria. Name the criteria, cases and method. |
| Verification | Checking whether an output meets specified requirements. State which requirements and what evidence demonstrates conformance. |
| Validation | Checking whether the proposed or delivered solution meets its intended use and user needs. State the users, conditions and evidence involved. |
| Review | An examination by a person or group. State who reviews what and what decision follows. |
| Approval | A decision by an authorised role. Do not use it as a synonym for review. |

These definitions guide usage; testing, evaluation, verification and validation can contribute to the same activity. Name the actual method and purpose rather than relying on a label to explain the work.

Use “stage” for a named part of the lifecycle, “activity” for work within it, “step” for an action in a procedure and “decision point” for a choice that affects what happens next. Preserve “phase” when describing an external methodology that uses it, and explain its relationship to the guide’s stages.

Keep a shared glossary as the site grows. Use one term for one concept and distinguish established terms, working definitions adopted by this guide and product-specific vocabulary. For an emerging or ambiguous term, explain the mechanism in plain language, state how this guide uses the term and cite the source where relevant. Apply this rule to labels such as “harness engineering”, “loop engineering”, “graph engineering” and “software factory”; do not assume they have the same meaning across publications.

### Use descriptive names for references

Name the behaviour, finding, decision or task the reader needs to follow. Do not invent short pointer codes for requirements, acceptance checks, experiments, evidence or tasks in published explanations and learning journeys. A reader should understand a reference without memorising a key or consulting a separate identifier table.

| Avoid in reader-facing content | Use a descriptive label |
| --- | --- |
| R-2/AC-3 | Yearly declaration requirement and the check that retries preserve existing responses |
| X-1 → X-2 | First usability test → revised usability test |
| AM-3 | Build the annual declaration workflow |
| T-CAMPAIGN-01 | Check that a yearly workflow retry creates no duplicate task |

Apply this rule to prose, headings, diagram nodes, captions, accessible descriptions, table rows, labels and link text. Use the same descriptive name across Project Discovery, implementation and the linked evidence. State the relationship in words: “The yearly declaration requirement is checked by retrying the worker and inspecting the saved response.” Avoid chains of unexplained codes separated by slashes or arrows.

Keep traceability through descriptive links, stable HTML anchors and technical metadata. Preserve existing anchors when changing visible labels. A real issue or test identifier can appear beside its descriptive name in a technical reference or linked record when readers need it to locate that record; it is not the primary label in a learning journey. Do not create a new code system merely to make an example look formal.

Established terms such as product requirements document (PRD), technical requirements document (TRD), six questions (6W) and four checks (4C) can be used after their full names and purpose are explained. These abbreviations name a document or taught method; they do not replace the meaning of an individual pointer. Ordinary step numbers, figure numbers and meaningful version/date information remain useful for sequence and navigation.

## Repository and maintenance conventions

Use “Project Discovery” in full whenever referring to this guide’s stage or page. Do not shorten the stage name to “Discovery”. Apply the name consistently in prose, headings, navigation, learning examples, captions, diagrams and accessible descriptions. Preserve published source titles and established method names when citing them.

Keep the repository name `AI-PDLC`. Use “Project Discovery” as the lifecycle page title and `product-discovery.html` as its path. Keep other URL paths unchanged unless explicitly requested.

Maintain writing rules here and presentation rules in [design.md](design.md). Keep summaries in other authoring documents brief and link to the relevant standard. Check summaries for conflicting terminology, page structures or length guidance when maintaining them.

## Requirements and evidence

In published delivery guidance, use **must** only for a confirmed requirement, with a link to its authority and a clear scope. Use **should** for a recommendation and explain when it may not apply. Use **can** for a capability or option. Write direct imperatives for procedural actions: “Record the test results.” Make the procedure’s applicability clear so that an imperative does not imply a wider organisational mandate.

Separate three kinds of statement:

| Kind | What the reader needs |
| --- | --- |
| Requirement | The rule, its applicability and its authoritative source. |
| Recommendation | The proposed action, its reason and any meaningful trade-off. |
| Example | A visible “Example” label and enough context to prevent it being mistaken for policy. |

Support factual claims with a source close to the claim. For performance claims, include the measurement context and date. If a result has not been measured, describe the intended benefit rather than claiming it has been achieved.

Check that a source supports the particular claim and applies to the activity being described. Distinguish a source’s findings from this guide’s interpretation or adaptation. Guidance on developing AI models or products containing AI does not automatically apply to every use of an AI coding assistant.

Never invent EDS committees, approval gates, job titles, mandatory templates or policy references. Mark unresolved details as authoring placeholders and resolve them before publication.

## Separate topic explanations from learning examples

Use the handbook's existing blue diagram theme to explain a topic, mechanism, method or general process. Its labels show the actions, roles, decisions and relationships the reader needs to understand. The explanation should make sense without knowing the fictional application used elsewhere on the page.

Place fictional applications, worked journeys, simulated results and example-specific evidence in clearly labelled learning-example sections. Use the separate **Matte Stone** treatment defined in [design.md](design.md#topic-diagrams-and-fictional-learning-examples) for all related text panels, tables and diagrams. Keep a continuous example across the relevant chapters and link its descriptive records; give a topic explanation and its application their own visual boundaries.

Give every learning example a short, descriptive title in sentence case: “Learning example · Problem background” or “Learning example · The annual-task retry requirement”. Name the topic or situation the example illustrates. Apply this format to worked journeys, compact examples in tables and diagram labels. Avoid a bare “Learning example” label or a title that only names the fictional application or tells readers to continue reading.

A visual containing asset-specific actions, sample participants, invented results or a fictional requirement is an example diagram even when its boxes resemble the general process. Split a mixed visual into a topic explanation and a separate applied example. Do not rely on colour alone: include a visible “Learning example” label and explain which premise was supplied and which findings or results are illustrative.

Keep the AI-SDLC overview focused on the end-to-end lifecycle, responsibilities, evidence and feedback. Put the continuous application journey in Project Discovery and Product implementation. Captions, accessible descriptions and surrounding prose follow the same topic/example distinction as the visual.

## Structure substantial learning chapters

When a lifecycle chapter combines general guidance, one sustained fictional case and a method catalogue, make three distinct and optional reading paths:

1. **Understand — playbook.** Explain the general purpose, prerequisites, people, actions, expected outputs, evidence and decision authority without relying on fictional characters. Keep its explanatory diagrams, method tables and primary headings case-independent.
2. **Apply — continuous worked example.** Introduce the fictional premise once. Follow one coherent story, with each chapter showing the situation, team action, observed evidence, decision and what changes next. Present implementation as requirements → technical design → small tasks → implementation → independent verification → authorised release → monitoring and learning. Explain feedback routes; never imply a preselected solution or automatic approval.
3. **Explore — reference toolkit.** Defer optional frameworks, deeper platform and risk checks, measurement catalogues and supplementary case illustrations. Do not interrupt concept tables or role descriptions with multiple miniature fictional examples.

Give each reading path a meaningful text label and a clear visual boundary using `design.md`. Link theory steps and the corresponding case chapters both ways; preserve deep-link IDs and cross-page handoffs. A reader should understand the playbook without the fictional case and follow the case without opening the optional library.

Use this structure when it materially improves a long learning chapter. Do not add navigation cards or a case story to a short procedure or simple reference page. The teaching order does not alter the actual lifecycle, local approval authority or safety requirements.

## Source attribution belongs at the end of each page

Place **all standalone source-attribution notes in the final page-level `Sources` section**, before the article footer. This includes source recaps placed at the end of content sections, framework inspiration, references supporting a table, method adaptations, and research/sources notes. A content section should not end with a separate “Source:”, “Sources:”, “Basis:”, “Supporting guidance:”, “Measurement source:” or equivalent standalone credit.

- Keep one Sources section per page that cites external works. Preserve the established reference IDs, source names, source URLs and links. List source-to-section mappings under a descriptive “Section attribution and adaptations” subheading, with section links, without duplicating the entire numbered bibliography.
- Preserve precise inline numbered source links next to a material claim when needed for traceability, but move standalone attribution explanations and bibliographic recaps to the Sources section.
- **Do not separate a consequential caveat from its claim.** Research population, sample size, limitations, applicability and uncertainty affecting the reader's decision stay next to the relevant statement. Licensed-image credits or required quotation credits stay with the asset when required by the licence, with fuller reference details at the bottom.
- An operational link or resource is not automatically attribution. Video links, training entry points, Eitri version warnings, approval requirements and actionable security cautions remain where the reader needs them even if they currently use a `source-ref` CSS class. Do not create empty Sources sections for pages with no external citations.
- Preserve all existing HTML IDs, links, intended meaning, reference numbering and factual claims. A move is not permission to remove a source or weaken a qualification.

**Editorial validation:** inspect all published pages for standalone source credits before the last Sources section; distinguish source credits from instructional prose and operational links. Check section-to-source mapping, stable anchors, source URLs, meaningful caveats, navigation, chronological worked journeys and responsive presentation before merging.

## Page structures

Choose a structure that fits the reader’s task. Omit sections that do not help; do not fill a template with generic text.

Choose the main purpose before drafting. Explanation helps readers understand; a tutorial helps them learn through a guided exercise; a procedure helps them complete a task; reference helps them look up a definition or specification. These distinctions follow [Diátaxis](https://diataxis.fr/). Link between page types where useful instead of making every page serve all four purposes.

### Concept page

1. **Title:** Name the concept in familiar terms.
2. **Opening:** Explain what it means and where it applies in two or three sentences.
3. **Problem:** Describe a concrete situation the reader recognises.
4. **Explanation:** Explain the general mechanism, using a topic diagram where useful. Put a small worked application in a separate labelled learning-example panel.
5. **Limits:** Explain prerequisites, costs or cases where it may not help.
6. **Next step:** Link to a relevant procedure or template.

### Tutorial

State what the reader will learn, the experience assumed and the starting materials. Guide them through a bounded exercise with expected results at useful checkpoints. Include common mistakes and how to recover, then show a completed example and explain what they have learned. Defer optional approaches and extensive theory to linked guidance.

### Reference page

Organise definitions, fields, commands or specifications for quick lookup. Use consistent entries with precise meanings, applicable versions or scope, and examples where needed. Link to explanations and procedures instead of embedding a tutorial in each entry.

### Lifecycle stage page

Use a consistent set of questions across stages:

- **Purpose:** What outcome does this stage support?
- **When to use it:** What brings the team here, including when to revisit it?
- **Inputs:** What information or completed work is needed?
- **Activities:** What does each role do?
- **AI contribution and responsibility:** What can AI contribute, who checks its output before it is used, and which responsibilities or decisions remain with people?
- **Outputs:** What records or working results are produced?
- **Checks and decisions:** What evidence is reviewed, by whom, and against which criteria?
- **Next step:** What happens after the decision, including rework where applicable?

Use stage names and decision authorities from the agreed lifecycle. Treat stage pages as an overview of the work, with links to detailed explanations, tutorials, procedures and reference material where useful. Do not imply that stages always occur once or in a fixed sequence; describe feedback and rework where they apply.

Distinguish checks on AI-produced development work from checks on AI behaviour in the delivered product. For products containing AI, explain the additional evaluation and operational considerations that apply to the stated capability, such as variable outputs, failure to find supporting evidence, or changes after a model update. Link to the relevant method and criteria rather than adding a generic AI-risk checklist to every stage.

### Procedure or template page

State the intended result, prerequisites and expected output. Use numbered steps when order matters. Begin each step with a verb and explain how the reader knows it is complete. For a downloadable template, describe its purpose, fields and one fictional worked example.

Explain what to do when a check fails or required information is missing. Keep learning exercises distinct from operational procedures: a procedure can assume stated prerequisites, while a tutorial supplies the guidance needed to build that experience.

## Headings, links and supporting content

Use one page title and sentence case for headings. Prefer specific headings such as “Define acceptance criteria” over “Considerations”. Keep heading levels sequential.

Use prose for explanation, numbered lists for sequences, bullets for parallel items and tables for comparisons. Avoid deeply nested lists and wide tables filled with paragraphs.

When an example contains three or more parallel items, types, options or checks, put them in a bullet list rather than running them together in a sentence. Introduce the list with a complete thought, keep the items grammatically consistent and explain the result or next action afterwards where needed. Apply this rule inside learning panels and table cells as well as in the main text. Use numbered lists when order matters, and keep comparison tables when readers need to compare the same attributes across options. Keep connected explanation in prose; do not turn every sentence into a bullet.

Write learning examples in familiar language that readers could use in conversation with a colleague. Spell out relationships such as “who holds the asset and whether it works” instead of compressed wording such as “custody/status”. Keep precise terms where needed, explain them at first use and use the same names throughout a continuous example.

Make link text meaningful on its own: “Read the evaluation guide”, not “click here”. Include the file type for downloads. Use callouts only for an exception, a consequential requirement or a useful example; keep essential instructions in the main flow.

Diagrams need a caption explaining their purpose and a text equivalent for the relationships they convey. Classify each as a topic explanation or learning example before styling it. Use descriptive action and decision labels; do not make the image the only place an instruction appears.

## Editing examples

All examples below are fictional editorial demonstrations, not EDS requirements.

| Before | After | Why |
| --- | --- | --- |
| Leverage AI to accelerate the end-to-end delivery paradigm. | Use AI to draft test cases. Review them against the acceptance criteria before adding them to the test suite. | Names a task and the human check. |
| Appropriate validation should be undertaken. | The engineer runs the agreed tests and records any failures. | Makes ownership and evidence visible. |
| AI ensures high-quality deliverables. | AI can produce a first draft. The team still needs to check its accuracy and completeness. | Bounds the claim. |
| Ensure robust stakeholder alignment. | Ask the product owner and engineering lead to agree on the problem, constraints and acceptance criteria. | Turns an abstraction into observable work. |
| The solution must be production-ready. | Before release, review the evaluation results, unresolved defects and recovery procedure against the agreed release criteria. | Replaces an undefined label with reviewable evidence. |

### Example: opening a guidance page

> Acceptance criteria describe the behaviour a product needs to demonstrate. They give the team a shared basis for reviewing work, including work produced with AI tools.
>
> Start with a user task. Describe the expected result and the conditions that could change it. For a document search tool, include cases where no relevant document exists, so the team can check how the product responds when it cannot answer.

### Example: explaining a trade-off

> A larger evaluation set covers more situations, but takes longer to maintain and run. Begin with the cases that would most affect users if the product failed. Add cases when reviews or operational evidence reveal gaps.

### Example: connecting an explanation

**Before:** “Context provides information. Harnesses provide tools. Loops provide feedback. Graphs organise tasks.”

**After:** “An agent needs relevant information and tools to carry out a task. The surrounding software controls access to those tools and checks the results. When a check fails, the workflow determines whether to retry, revise the approach or ask a person for help.”

The revised passage explains the relationships before introducing specialist labels. Use the labels afterwards if readers need them to follow the rest of the guide.

### Example: explaining AI’s contribution

> AI can draft acceptance criteria from the problem statement. The product owner checks that they reflect the intended outcome, and the engineer checks that they are testable. Resolve unsupported assumptions before using the criteria to guide implementation.

### Example: making a review instruction actionable

**Before:** “Validate the AI summary against the research.”

**After:** “Ask the reviewer to compare each finding that affects the decision with its original interview passage or observation note. Check the context, duplicate counts and evidence the summary omitted. Record supported findings, source links and unanswered questions. Use the remaining questions to choose the next study or test.”

**Fictional distinction:** An AI summary says, “The search system is broken.” The notes show that staff needed help finding an article in 7 of 24 cases. The observation supports investigating that difficulty; it does not establish the cause. Check search behaviour and article quality before choosing a fix.

## Page metadata

Record a content owner, last-reviewed date and applicable lifecycle version for maintained guidance. Page status metadata is not required. Do not add editorial status fields or badges to page headers or description metadata. Editorial status may be tracked in maintenance records when useful.

Display dates as “27 September 2026”. Store machine-readable dates as `2026-09-27`. Change the review date after a substantive review, not automatically on every site build.

## Editorial acceptance checklist
- [ ] Standalone source credits and adaptations appear only in the final Sources section, while material caveats and operational links remain in context.
- [ ] Substantial teaching chapters separate independent theory, the continuous fictional case and optional reference material when that structure aids learning.

- [ ] The opening tells the intended reader what the page helps them do or understand.
- [ ] Prerequisites match the reader’s assumed knowledge, and the page structure fits its main purpose.
- [ ] Explanations introduce unfamiliar mechanisms before relying on specialist labels and connect ideas naturally.
- [ ] Instructions identify actions, outputs and ownership where needed.
- [ ] Each procedure or review explains its inputs, actual checks, basis for judging the result, recorded output and next action.
- [ ] “Check”, “review”, “validate” and “ensure” are followed by enough detail for the reader to perform the work.
- [ ] Difficult distinctions have a short example where needed; observations, interpretations and untested explanations remain separate.
- [ ] Terms are consistent and abbreviations are explained.
- [ ] References use descriptive names rather than invented pointer codes; traceability is retained through links and technical records.
- [ ] Topic diagrams explain the general content in the blue theme; fictional application diagrams and related panels use the labelled Matte Stone theme.
- [ ] The overview explains the lifecycle, while the continuous learning example stays in the product chapters; supplied premises and illustrative findings remain distinguishable.
- [ ] Ambiguous terms have a clear scope; house definitions and named external methodologies remain distinguishable.
- [ ] Stage guidance explains AI’s contribution, the checks on its output and the responsibilities or decisions retained by people.
- [ ] Generic disclaimers are consolidated; material limitations, control boundaries, attribution and licence credits remain where needed.
- [ ] The changed section, surrounding passages and affected linked guidance have been reread for coherent flow, consistent examples and complete handoffs.
- [ ] Claims have appropriate evidence; recommendations and examples are labelled clearly.
- [ ] Requirements cite a confirmed authority and state where they apply.
- [ ] Examples contain no invented organisational facts.
- [ ] Learning examples sound natural, and groups of three or more parallel items use bullets; sequences and comparisons retain the structure that helps readers follow them.
- [ ] Headings and link text make sense when scanned independently.
- [ ] The page includes a useful next step and current ownership metadata.
- [ ] A representative reader can explain the concept in their own words, identify the next action and distinguish recommendations from requirements.

Do not mark a procedure or review activity editorially complete while readers still have to invent the checking method or infer what to record. Before accepting it, ask whether a reader unfamiliar with the topic could carry out the next action using the passage and its linked inputs. Revise the passage if they could not. This is an authoring acceptance rule, not a new organisational approval gate.

For a new or substantially changed explanation, tutorial or procedure, check understanding with a representative reader who has the stated prerequisites. Ask them to explain the concept or perform a representative task using the documentation. Observe where they hesitate, misinterpret a term or need missing information; revise those passages. Record the task and findings in maintenance notes. A general statement that the page is clear does not demonstrate that the reader can use it.

## Sources for this standard

The following sources inform the editorial approach and terminology choices. The page structures and definitions above are adaptations for this guide.

- [Google: Voice and tone](https://developers.google.com/style/tone) informs natural prose, varied sentence openings, useful transitions and reading difficult passages aloud.
- [Google: Audience](https://developers.google.com/tech-writing/one/audience) informs analysis of readers’ existing knowledge, prerequisites and learning needs.
- [Diátaxis](https://diataxis.fr/) distinguishes explanation, tutorials, how-to guides and reference by the reader’s purpose.
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents) informs the adopted distinction between predefined workflows and model-directed agents. Its tooling discussion dates from December 2024; check current product documentation for implementation details.
- [AWS: Building with AI-DLC using Amazon Q Developer](https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/) identifies the named AI-DLC methodology discussed in the terminology table.
- [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) addresses secure development practices for AI models and systems using them. It illustrates why authors need to check a source’s scope before applying its recommendations to AI-assisted development.

Use [design.md](design.md) for the presentation of this content.
