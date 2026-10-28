# Writing standard

## Purpose

Help readers understand a practice, decide when to use it, and complete the next step. Write for product owners, engineers, designers and reviewers who bring different levels of AI experience.

This document proposes house rules for the site. It does not establish EDS policy or prescribe an approved lifecycle. Examples are illustrative; validate roles, requirements and lifecycle stages against the organisation’s actual process before publishing.

## Reference and interpretation

The page defines its subject early, explains the problem behind the approach, and introduces named practices with their purpose. It moves from explanation to practical steps and acknowledges adoption trade-offs. Descriptive headings let readers scan before committing to the detail.

Use these qualities as editorial inspiration. The rules, terminology choices and examples below are an original proposal for this site, not a reproduction of the reference or an endorsement of its technical claims.

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

## Sentence and paragraph rules

- Prefer active voice: “The product owner records the decision.”
- Put the main point before qualifications. Follow it with the reason or example.
- Aim for 15–25 words per sentence. Treat this as an editing prompt, not a rigid limit.
- Keep one main idea per paragraph, usually in two to four sentences.
- Replace noun-heavy phrases with verbs: “review the evidence”, rather than “conduct an evidence review exercise”.
- Name the referent when “it”, “this” or “they” could mean more than one thing.
- Explain a specialist term at first use. Keep the precise term when a simpler replacement would change its meaning.
- Remove repeated introductions, promotional claims and conclusions that merely restate the opening.

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

| Term | House usage |
| --- | --- |
| AI-Software Development Lifecycle | Use the displayed site title on the home page and in formal references. |
| AI-SDLC | Introduce after the full title on a page that uses the abbreviation. Prefer “the lifecycle” in nearby prose. Keep the repository name `AI-PDLC`. The discovery page uses `product-discovery.html`; keep other URL paths unchanged unless explicitly requested. |
| Product discovery | Research needs, compare opportunities and test concepts before a bounded investment. Use this as the lifecycle page title and `product-discovery.html` as its path. Ideation means generating options within discovery. |
| AI-assisted development | Development work supported by AI tools. Do not assume the resulting product contains AI. |
| AI product | A product whose behaviour includes an AI capability. Explain that capability where relevant. |
| AI agent | Software that uses an AI model to choose or adapt actions and tool use towards a goal, within agreed permissions and limits. A workflow can combine agents with predefined code paths and automated checks. |
| Artefact | A recorded output of work. Prefer the specific name, such as “evaluation report”, when known. |
| Evaluation | A structured assessment against defined criteria. Name the criteria, cases and method. |
| Review | An examination by a person or group. State who reviews what and what decision follows. |
| Approval | A decision by an authorised role. Do not use it as a synonym for review. |

Keep a shared glossary as the site grows. Use one term for one concept. Do not alternate between “stage”, “phase” and “step” unless their relationship is defined.

## Requirements and evidence

Use **must** only for a confirmed requirement, with a link to its authority and a clear scope. Use **should** for a recommendation and explain when it may not apply. Use **can** for a capability or option. Write direct imperatives for procedural actions: “Record the test results.”

Separate three kinds of statement:

| Kind | What the reader needs |
| --- | --- |
| Requirement | The rule, its applicability and its authoritative source. |
| Recommendation | The proposed action, its reason and any meaningful trade-off. |
| Example | A visible “Example” label and enough context to prevent it being mistaken for policy. |

Support factual claims with a source close to the claim. For performance claims, include the measurement context and date. If a result has not been measured, describe the intended benefit rather than claiming it has been achieved.

Never invent EDS committees, approval gates, job titles, mandatory templates or policy references. Mark unresolved details as authoring placeholders and resolve them before publication.

## Page structures

Choose a structure that fits the reader’s task. Omit sections that do not help; do not fill a template with generic text.

### Concept page

1. **Title:** Name the concept in familiar terms.
2. **Opening:** Explain what it means and where it applies in two or three sentences.
3. **Problem:** Describe a concrete situation the reader recognises.
4. **Explanation:** Show how the practice works, using a small example.
5. **Limits:** Explain prerequisites, costs or cases where it may not help.
6. **Next step:** Link to a relevant procedure or template.

### Lifecycle stage page

Use a consistent set of questions across stages:

- **Purpose:** What outcome does this stage support?
- **When to use it:** What brings the team here, including when to revisit it?
- **Inputs:** What information or completed work is needed?
- **Activities:** What does each role do?
- **Outputs:** What records or working results are produced?
- **Checks and decisions:** What evidence is reviewed, by whom, and against which criteria?
- **Next step:** What happens after the decision, including rework where applicable?

Stage names and decision authorities must come from the agreed lifecycle, not from this template.

### Procedure or template page

State the intended result, prerequisites and expected output. Use numbered steps when order matters. Begin each step with a verb and explain how the reader knows it is complete. For a downloadable template, describe its purpose, fields and one fictional worked example.

## Headings, links and supporting content

Use one page title and sentence case for headings. Prefer specific headings such as “Define acceptance criteria” over “Considerations”. Keep heading levels sequential.

Use prose for explanation, numbered lists for sequences, bullets for parallel items and tables for comparisons. Avoid deeply nested lists and wide tables filled with paragraphs.

Make link text meaningful on its own: “Read the evaluation guide”, not “click here”. Include the file type for downloads. Use callouts only for an exception, a consequential requirement or a useful example; keep essential instructions in the main flow.

Diagrams need a caption explaining their purpose and a text equivalent for the relationships they convey. Do not make the image the only place an instruction appears.

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

### Example: making a review instruction actionable

**Before:** “Validate the AI summary against the research.”

**After:** “Ask the reviewer to compare each finding that affects the decision with its original interview passage or observation note. Check the context, duplicate counts and evidence the summary omitted. Record supported findings, source links and unanswered questions. Use the remaining questions to choose the next study or test.”

**Fictional distinction:** An AI summary says, “The search system is broken.” The notes show that staff needed help finding an article in 7 of 24 cases. The observation supports investigating that difficulty; it does not establish the cause. Check search behaviour and article quality before choosing a fix.

## Page metadata

Record a content owner, last-reviewed date and applicable lifecycle version for maintained guidance. Page status metadata is not required. Do not add editorial status fields or badges to page headers or description metadata. Editorial status may be tracked in maintenance records when useful.

Display dates as “27 September 2026”. Store machine-readable dates as `2026-09-27`. Change the review date after a substantive review, not automatically on every site build.

## Editorial acceptance checklist

- [ ] The opening tells the intended reader what the page helps them do or understand.
- [ ] Instructions identify actions, outputs and ownership where needed.
- [ ] Each procedure or review explains its inputs, actual checks, basis for judging the result, recorded output and next action.
- [ ] “Check”, “review”, “validate” and “ensure” are followed by enough detail for the reader to perform the work.
- [ ] Difficult distinctions have a short example where needed; observations, interpretations and untested explanations remain separate.
- [ ] Terms are consistent and abbreviations are explained.
- [ ] Claims have appropriate evidence; recommendations and examples are labelled clearly.
- [ ] Requirements cite a confirmed authority and state where they apply.
- [ ] Examples contain no invented organisational facts.
- [ ] Headings and link text make sense when scanned independently.
- [ ] The page includes a useful next step and current ownership metadata.
- [ ] A colleague outside the author’s specialism can explain the main point after reading it.

Do not mark a procedure or review activity editorially complete while readers still have to invent the checking method or infer what to record. Before accepting it, ask whether a reader unfamiliar with the topic could carry out the next action using the passage and its linked inputs. Revise the passage if they could not. This is an authoring acceptance rule, not a new organisational approval gate.

Use [design.md](design.md) for the presentation of this content.
