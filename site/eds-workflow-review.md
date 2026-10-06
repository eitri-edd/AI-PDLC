# EDS AI Workflow editorial review

Reviewed 6 October 2026 against `../writing.md` and `../design.md`. The single `dist/eds-ai-workflow.html` page was split into an overview and five child pages, based on the harness documentation in `../harness-workflow/`.

## Decisions

1. **Source priority.** `harness-workflow/README.md` (manually extracted, latest) takes priority over the EDS operating handbook. `skills-catalogue.md` and `team-context-ingestion.md` supplement it. All three are cited by title only; the only public link is the self-paced training site.
2. **Handbook content.** Handbook items that conflict with or were superseded by the README were removed: the sprint contract, architecture tests as an in-loop gate, `/flaky-test-detector`, `/gen-uat-scripts`, feature-contract states and the six execution-ready criteria (replaced by the eight `/issue-verification` criteria). Handbook guidance without a conflict stays in a labelled "Working principles" part of the overview, cited to the handbook: the seven principles, instruction layers, search order, harness diagnosis, workflow-health measures and the fictional example.
3. **Structure.** A parent section, "EDS AI Workflow (Eitri Agentic Dev Workflow)", shortened to "EDS AI Workflow (Eitri)" in the sidebar, with nested child pages.
4. **Publication detail.** Install commands and repository names appear as code text, not links. Knowledge-base variables, the standards registry name and its file path are described by purpose only. Third-party tools are named without links. Control counts are kept. AppStandards topics include "MCC Platform Services (MCNS, MPDS)".
5. **Training.** `dist/training.html` is kept but no longer linked; every Training link points to the external course.

## Pages

| File | Content | Main source |
| --- | --- | --- |
| `eds-ai-workflow.html` | Page index, route figure, status labels, PRD vs story TRD, roles, working principles, harness diagnosis, health measures | README; handbook for the principles part |
| `eds-po-ba-harness.html` | Three PO/BA paths, wayfinder labels, handoff | README section 1; context guide section 1 |
| `eds-developer-harness.html` | Installation, 19 steps, AppStandards topics, verdicts, execution modes, `/do-work` loop and gates, software factory, closeout, evidence locations, definition of done | README sections 2–3 |
| `eds-path-to-production.html` | Stages 4.1–4.4, `/pre-prod-check`, pipeline and pre-production definition of done | README sections 3–4 |
| `eds-team-context.html` | Context matrix, ingestion per stage, quick-start checklist | Context guide |
| `eds-skills-catalogue.html` | Every skill with maintainer, status and arguments | Skills catalogue |

Five new inline SVG figures follow the existing diagram classes: the route summary, the three PO/BA paths, the 19 steps, the `/do-work` loop and the pipeline stages. The harness-diagnosis figure is retained.

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

## Other pages changed

- All pages: Guide navigation rewritten with nested EDS children (`.nav-children`, `.nav-parent-active` in `styles.css`). Added `.status`, `.status-planned`, `.status-hitl` and `.checklist` styles.
- `product-implementation.html`: strategy mapping table, readiness and context links repointed to the new pages and anchors; source 2 now cites the harness documentation; Release row reflects pipeline stages 4.1–4.4.
- `training.html`: links to the EDS workflow point to the developer harness page.

## Validation

Checked on 6 October 2026:

- Every internal link and fragment across `dist/*.html` resolves; no duplicate IDs; every `aria-labelledby` target exists; each page has exactly one Guide navigation.
- External links on the EDS pages point only to the self-paced training site.
- Rendered in Chromium at 1400 px and 390 px: all five new figures display correctly, the nested navigation shows the current page, no horizontal page overflow at 390 px, no console errors or warnings.

Not verified: the current status of skills marked Available or Planned beyond what the supplied documents state, and whether the handbook guidance retained in "Working principles" is still endorsed by its owner.
