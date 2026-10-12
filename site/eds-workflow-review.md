# EDS AI Workflow editorial review

Reviewed 6 October 2026 against `../writing.md` and `../design.md`. The single `dist/eds-ai-workflow.html` page was split into an overview and five child pages, based on the harness documentation in `../harness-workflow/`.

Revised 12 October 2026 for a higher-management audience, following `../scratch/considerations.md`. The six pages were rewritten as high-level descriptions and third-party tools were linked. See [Revision of 12 October 2026](#revision-of-12-october-2026); decisions and tables below are updated where that revision superseded them.

## Decisions

1. **Source priority.** `harness-workflow/README.md` (manually extracted, latest) takes priority over the EDS operating handbook. `skills-catalogue.md` and `team-context-ingestion.md` supplement it. All three are cited by title only; the only public link is the self-paced training site.
2. **Handbook content.** Handbook items that conflict with or were superseded by the README were removed: the sprint contract, architecture tests as an in-loop gate, `/flaky-test-detector`, `/gen-uat-scripts`, feature-contract states and the six execution-ready criteria (replaced by the eight `/issue-verification` criteria). Handbook guidance without a conflict stays in a labelled "Working principles" part of the overview, cited to the handbook: the seven principles, instruction layers, search order, harness diagnosis, workflow-health measures and the fictional example.
3. **Structure.** A parent section, "EDS AI Workflow (Eitri Agentic Dev Workflow)", shortened to "EDS AI Workflow (Eitri)" in the sidebar, with nested child pages.
4. **Publication detail.** Knowledge-base variables, the standards registry name and its file path are described by purpose only. Control counts are kept. AppStandards topics include "MCC Platform Services (MCNS, MPDS)". Superseded on 12 October 2026: install commands and repository names no longer appear, and third-party tools are now linked (see the revision below).
5. **Training.** `dist/training.html` is kept but no longer linked; every Training link points to the external course.

## Pages

| File | Content | Main source |
| --- | --- | --- |
| `eds-ai-workflow.html` | Page index, route figure in plain terms, status-label key, PRD vs story TRD, roles, working principles, context layers, harness diagnosis, health measures | README; handbook for the principles part |
| `eds-po-ba-harness.html` | Three PO/BA paths described by outcome, handoff | README section 1; context guide section 1 |
| `eds-developer-harness.html` | What setup puts in place, 19 steps in four phases with a label per step, execution modes, build loop and gates, software factory, closeout, definition of done | README sections 2–3 |
| `eds-path-to-production.html` | Stages 4.1–4.4 by what runs and what blocks, pre-production gates, pipeline and pre-production definition of done | README sections 3–4 |
| `eds-team-context.html` | Context matrix, how each kind of context is added, quick-start checklist | Context guide |
| `eds-skills-catalogue.html` | Skill-group summary, then every skill with maintainer, status and a one-line description | Skills catalogue |

Five new inline SVG figures follow the existing diagram classes: the route summary, the three PO/BA paths, the 19 steps, the `/do-work` loop and the pipeline stages. The harness-diagnosis figure is retained. All six figures remain after the 12 October 2026 revision; four had their labels reworded (see the revision below).

## Inconsistencies resolved in the source

| # | Inconsistency | Resolution on the site |
| --- | --- | --- |
| 1 | `/im8-review` and `/im8-reviewer` both used | `/im8-review` throughout, as in the catalogue |
| 2 | Pre-commit runs `/im8-reviewer` and `/code-reviewer`, which already includes IM8 | Pre-commit runs `/code-reviewer`, including `/im8-review` |
| 3 | 4.4 note says IM8 runs at MR-diff scope in 4.3; 4.3 says full codebase | Full codebase at 4.3 |
| 4 | Pre-production claims IM8/ARC via `/im8-review`, which checks IM8 only | "IM8 (code)", with a note that ARC is assessed on the TRD by `/spec-compliance` |
| 5 | `/e2e` core in the flow, optional in the definition of done; blocking statements contradict | Optional · Recommended; runs as a pre-push hook, a failing campaign does not block push unless CI enforces it |
| 6 | Definition of done requires `/spec-compliance` "all PASS" despite five verdicts | No FAIL; AUTO-FIX applied; DEFERRED tracked |
| 7 | Diagram and text disagree on Context7 and mutation-gate status | Text labels used |
| 8 | `/grill-me` and `/grill-with-docs` used but absent from the catalogue | Listed under Matt Pocock skills with a note |
| 9 | PM/BA vs Architect/Tech Lead running `/dependency-orchestrator` | PM/BA mode builds the graph and PM Report; Tech Lead runs Developer mode |
| 10 | Context guide uses old step numbers and `/speckit-specify` | README numbering (Step 12, 15) and `/speckit.specify` |
| 11 | `checklists/` vs `artifacts/` output paths | README paths; auth matrix stays in `checklists/` |
| 12 | Persona journey files linked but not supplied | Omitted |

The TRD owner and the approvers at HITL 1 and HITL 2 are not named in the source; the overview asks teams to agree them locally.

After the 12 October 2026 revision, rows 10 and 11 no longer show on the site: `/speckit.specify` and the output paths were removed with the other commands and file paths. The resolutions still apply if that detail is restored.

## Other pages changed on 6 October 2026

- All pages: Guide navigation rewritten with nested EDS children (`.nav-children`, `.nav-parent-active` in `styles.css`). Added `.status`, `.status-planned`, `.status-hitl` and `.checklist` styles.
- `product-implementation.html`: strategy mapping table, readiness and context links repointed to the new pages and anchors; source 2 now cites the harness documentation; Release row reflects pipeline stages 4.1–4.4.
- `training.html`: links to the EDS workflow point to the developer harness page.

## Validation of 6 October 2026

Checked on 6 October 2026:

- Every internal link and fragment across `dist/*.html` resolves; no duplicate IDs; every `aria-labelledby` target exists; each page has exactly one Guide navigation.
- External links on the EDS pages point only to the self-paced training site. No longer true after the 12 October 2026 revision.
- Rendered in Chromium at 1400 px and 390 px: all five new figures display correctly, the nested navigation shows the current page, no horizontal page overflow at 390 px, no console errors or warnings.

Not verified: the current status of skills marked Available or Planned beyond what the supplied documents state, and whether the handbook guidance retained in "Working principles" is still endorsed by its owner.

## Revision of 12 October 2026

Applied `../scratch/considerations.md` to the six EDS pages only.

### Decisions

1. **Audience.** The pages are written for higher management. They describe what each phase achieves, not how to operate each skill. Structure, section IDs, sources and the 6 October inconsistency resolutions are unchanged.
2. **Detail removed.** Install commands, repository names, file paths, skill arguments and flags, the `/code-reviewer` targets table, the AppStandards topics table, the `/spec-compliance` verdicts table, the eight `/issue-verification` criteria, the wayfinder labels table, the six bug-diagnosis phases, the evidence-locations table and the handbook's search order. Most are condensed to a sentence; skill names now appear almost only in the skills catalogue.
3. **Third-party links.** The 20 tools, products, policies and frameworks listed in the considerations are linked where they are mentioned. This supersedes the "named without links" rule in decision 4 above.
4. **Overview foreword.** The sentence naming the target audience was removed. A one-sentence definition of "skill" was added.
5. **Route figure.** Figure 1 on the overview uses plain terms (Plan the story, Human gate 1, Build loop, Release gates) with no step or stage numbers. The sentence telling readers which direction to read each row was removed, here and on the other figures.
6. **Status labels.** The overview section is a short conceptual explanation with a key. Each page that uses labels repeats a key for them, so readers need not return to the overview. All labels are pills: Core, Optional · Recommended, Optional, One-time setup, Planned, HITL and, in the catalogue, Available.
7. **Skills catalogue.** Kept as a lookup by skill name, with a new skill-groups summary table and one-line descriptions. The seven Spring reviews share one row.
8. **Wording.** `/do-work` is called "the build loop" in prose and is named once on the developer harness page. Stage numbering 4.1–4.4 is kept because `product-implementation.html` refers to it.
9. **Metadata.** "Last reviewed" is 12 October 2026 on all six pages. The skills catalogue meta description no longer mentions arguments.

### Figures

No figure was added or removed. Labels changed on four: the overview route (decision 5), the three PO/BA paths (file names replaced by descriptions), the 19 steps (Live docs, Choose a mode, Interface scaffold, Build loop, Improve design, Code review, End-to-end tests) and the build loop (Tests first, Build and quality, This issue only). The pipeline figure names what runs instead of the skill.

### Files changed outside the six pages

- `styles.css`: added `.status-core`, `.status-recommended`, `.status-optional` and `.status-key`, with a single-column key below 600 px. No existing rule was changed.

### Validation

Checked on 12 October 2026:

- Every internal link and fragment across `dist/*.html` resolves; no duplicate IDs; every `aria-labelledby` target exists; each EDS page has exactly one Guide navigation; each page's contents list matches its sections.
- Inbound anchors from other pages are preserved, including `#install`, `#plan`, `#check`, `#modes`, `#do-work` and `#closeout` on the developer harness and `#context-practice`, `#harness` and `#workflow-health` on the overview.
- All 20 external links from the considerations are present, alongside the self-paced training link.
- Rendered in headless Chrome at 1400 px: the reworded figures fit their boxes and the label pills and keys display as intended.

Not verified: that the external URLs resolve (they were taken from the considerations as given), rendering at 390 px (headless Chrome would not render narrower than about 500 px), and browser console output.
