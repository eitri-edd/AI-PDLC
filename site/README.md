# AI-SDLC guide

Static site source and publishable files are in `dist/`. No build or package installation is required. Serve this folder with a local static web server to preview the site.

- `dist/index.html`: Introduction, based on the user-provided Chapter 0 and audience brief, with three inline SVG figures and a comparison table.
- `dist/transformation.html`: Leadership guidance for the established Enterprise Systems Department. The continuous fictional case connects specialist-owned context, T-shaped practice, delegated routine reviews and retained human gates. Its outcome example repeats evaluation and adjustment to balance agent governance, delivery efficiency and full cost, without fabricated measurements or additional departments. Specialist matrices and supporting diagrams remain optional. `transformation.css` preserves responsive presentation and deep-link offsets; `transformation.js` reveals reference targets and prepares references for print. See `transformation-review.md` for checks and limits.
- `dist/concept.html`: Models plus seven development concepts covering intent, specifications, context, harnesses, loops, execution graphs and software factories. Models summarises large language models, domain-specific language models, small language models and System One, with a comparison table, practical example and five annotated research references. The seven development concepts explain their purpose, operation and limits with diagrams, examples and concise application ideas. Learning resources share the page's single Sources list. The harness diagram explains the six components in the supplied reference image. See `concepts-review.md` for source reviews and editorial decisions.
- `dist/ai-pdlc.html`: AI-SDLC overview: a high-level explanation of Project Discovery, the delivery agreement, implementation, release and learning. Retains the lifecycle diagram, responsibilities, evidence and feedback routes without a fictional product example; detailed methods and the learning journey live in the two product chapters.
- `dist/product-discovery.html`: Three distinct learning paths: the six-step concept-first playbook, Maya’s continuous six-part worked example, and an optional method/reference toolkit. The case preserves six journey chapters and relocates 62 smaller asset-specific illustrations from theory and method tables into optional example supplements. Readers can navigate between corresponding playbook and case steps; existing public anchors are retained. See `asset-management-journey-review.md`, `product-discovery-review.md` and `product-pages-review.md` for evidence and previous editorial decisions.
- `dist/product-implementation.html`: Three paths: implementation playbook, continuous seven-chapter asset-management case study (handoff, readiness, PRD/TRD/tasks, implement, verify, release, learn), and optional tooling, autonomy and measurement references. The original 37 smaller fictional illustrations are preserved in optional supplements, with original IDs, citations, AWS architecture and decisions retained. `dist/product-implementation.css` adds responsive navigation and case styling.
- `dist/eds-ai-workflow.html` and five child pages: EDS AI Workflow (Eitri Agentic Dev Workflow), based on the harness documentation in `../harness-workflow/` (cited by title only), with the earlier EDS handbook retained for working principles. Overview (`eds-ai-workflow.html`), PO/BA harness (`eds-po-ba-harness.html`), developer harness (`eds-developer-harness.html`), path to production (`eds-path-to-production.html`), team context (`eds-team-context.html`) and skills catalogue (`eds-skills-catalogue.html`). The sidebar nests the child pages under the overview. See `eds-workflow-review.md` for decisions, source inconsistencies resolved and validation.
- `dist/training.html`: Training, a study guide to the Eitri Agentic Dev Workflow self-paced training. No longer linked from the site; the sidebar's Training entry points to the external self-paced course.
- `dist/about.html`: How the site is curated, with an overview diagram connecting scouting, peer review, source monitoring, the writer’s context and standards, and human approval for every content change. Linked at the bottom of the navigation on every page.
- `dist/tech-scan.html` and four component references: an AWS-first, decision-led research shortlist for Models, Harness, AI gateway and Sandbox. The hub separates model and tool paths and links to the appropriate component; optional catalogues retain candidates without implying qualification. See [the original Tech Scan pass](tech-scan-maintenance-2026-11-12.md) and [the refinement review](tech-scan-refinement-review-2026-11-12.md) for source corrections, standards decisions, verification and pending human-reader tasks.
- `dist/styles.css`: Shared styles from `../design.md`.
- `dist/site.js`: Responsive navigation and current-section indication.

For substantial lifecycle chapters, keep the playbook, fictional worked journey and optional method toolkit distinct. Follow [the source-listing standard](../writing.md#standardise-source-listings): one final Sources section, one visible numbered list with attributions and adaptations inside their canonical entries, and one page-wide reference-check date. Retain per-source check history in maintenance records and material research limitations and operational links beside the instructions they qualify.

Read `../writing.md` and `../design.md` before changes. Reference documents are not included in the public output. Publish only the contents of `dist/`, not the entire workspace. Relative links support hosting below a repository path.

The authoring standards reserve blue diagrams for topic explanations and teal panels for AI assistance. Every worked example uses the shared Method first treatment: a pale lavender surface, plum left rule and framed book mark, visible “Worked example” label and descriptive topic title. Standalone examples and main journey chapters state a learning benefit; accordion headers keep their purpose visible when closed. Apply the same palette to related tables and applied diagrams. See `../design.md` and `../writing.md` for the shared specification. Preserve descriptive reference names and stable anchors, and verify the rendered result on every affected page.

Confirm the content owner, applicable lifecycle version and substantive review date before publishing maintained guidance. Page status metadata is not required and should not be added to page headers or description metadata. Editorial status may be tracked in maintenance records when useful. The narrow [Tech Scan research-reference exception](../writing.md#page-metadata) permits one draft qualification—using the About page's existing disclaimer callout on the hub—and the existing navigation label, without new status badges. GitHub Pages publishes `main:site/dist/` at the site root and `dev:site/dist/` under `/dev/` through `.github/workflows/pages.yml`.

The Project Discovery and implementation pages were reviewed and supplemented with online sources on 28 September 2026. See `product-pages-review.md` for the source mapping, editorial changes and validation, including experiment design, AI evaluation, delivery measures and release recovery.

## Production and dev deployments

- **Production:** https://eitri-edd.github.io/AI-PDLC/ uses `site/dist/` from `main`.
- **Dev:** https://eitri-edd.github.io/AI-PDLC/dev/ uses `site/dist/` from the long-lived `dev` branch. It is a public preview, not a private environment; do not publish secrets or confidential draft content.

Each deployment reads both current branch tips and uploads one complete artefact. Production files stay at the root; dev files go into `dev/`. Files are copied without rewriting links or content. Keep links and asset URLs relative so navigation, styles, scripts and images stay within the selected branch's path. Reserve `main:site/dist/dev/` for the dev subtree rather than adding production content there.

Relevant pushes to `main` trigger deployment directly. Relevant pushes to `dev` run the read-only **Validate Pages** workflow, which tests assembly and stages production plus candidate content without publishing. Its successful push runs trigger the deployment workflow on the default branch (`main`) through `workflow_run`. Pull request validation never deploys. Documentation-only changes outside the workflow's path filters do not republish the site.

Deployment continues to use the existing main-only `github-pages` environment protection. The privileged workflow executes assembly code from `main`; it only copies static content from `dev` and does not consume its workflow artefacts. Deployments share the `pages` concurrency group and do not cancel a running deployment. Each queued run reads fresh branch tips, so a dev update cannot replace production with dev content, and a main update cannot remove the dev subtree.

### Rollout and maintenance

Merge the deployment PR from `dev` into `main` to publish the first combined artefact. **Keep the `dev` branch after merging.** It starts from the production revision and carries the validation workflow needed to notify `main` about subsequent dev changes. Keep `.github/workflows/pages-checks.yml` on `dev`, including its **Validate Pages** name; changing or removing that trigger stops automatic dev publishing.

Commit preview content to `dev`, then use a pull request to promote approved content into `main`. After production-only fixes, merge `main` back into `dev` as needed; deployment does not synchronise branch history. To republish both current tips manually, run **Deploy site to GitHub Pages** from `main`. A manual run from another branch is intentionally skipped. Missing source indexes, symlinks, or a production `/dev/` collision fail assembly before upload, leaving the last successful deployment in place.

To roll back the deployment change, revert its PR on `main`. The next successful main-only deployment removes `/dev/` and restores the former production-only layout. To roll back content on either branch, revert its content commit and let the combined deployment run again.

### Local verification

Run the standard-library regression tests from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

To stage the real branch contents locally, use a fresh directory outside your checkout. Replace `<preview-dir>` with that directory's absolute path, and run these commands from the repository root:

```sh
git worktree add --detach <preview-dir>/main origin/main
git worktree add --detach <preview-dir>/dev origin/dev
python3 .github/scripts/assemble_pages.py \
  <preview-dir>/main/site/dist <preview-dir>/dev/site/dist <preview-dir>/AI-PDLC
python3 -m http.server 8000 --directory <preview-dir>
```

Open `http://localhost:8000/AI-PDLC/` and `http://localhost:8000/AI-PDLC/dev/`. Follow navigation links and check CSS, JavaScript and images under both prefixes. The output directory must not already exist; assembly refuses to mix new content with stale files. When finished, stop the server and remove the two detached worktrees with `git worktree remove`.


## Accuracy review

The [6 November 2026 accuracy review](accuracy-review.md) records its original 13-page scope, corrections and outstanding source/version checks. The [12 November 2026 whole-site maintenance pass](reference-review-2026-11-12.md) covers the 14 pages present at that pass, source drift, access limitations and verification. Five Tech Scan pages were added afterwards; their [initial source pass](tech-scan-maintenance-2026-11-12.md) and [targeted refinement](tech-scan-refinement-review-2026-11-12.md) are separate records. The [reference inventory](reference-checks.json) separates current URL/page outcomes from retained historical records, including the original 100 external URLs. Public-source checks do not establish the current internal Eitri release or policy-pack version.
