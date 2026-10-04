# AI-PDLC guide

Static site source and publishable files are in `dist/`. No build or package installation is required. Serve this folder with a local static web server to preview the site.

- `dist/index.html`: Introduction, based on the user-provided Chapter 0 and audience brief, with three inline SVG figures and a comparison table.
- `dist/transformation.html`: Organisation transformation: practical changes across people, process, culture and technology, with three inline SVG figures, cited research and a measurable pilot procedure. See `transformation-review.md` for the editorial review and source limitations.
- `dist/concept.html`: Seven concepts covering intent, specifications, context, harnesses, loops, execution graphs and software factories. Each is explained separately with an inline SVG diagram, a fictional example, sources and a practical next step. See `concepts-review.md` for the online source review and editorial decisions.
- `dist/product-ideation.html`: Product ideation ("making the right product"), based on Chapter 2: the two-loop model, ideation loop, problem statements (6W, 4C, SFR), thesis and theory of change, prototyping, validation and decisions, product team, product intent, measurement (metric ladder) and the handoff of the PRD and UI artefacts, with six inline SVG figures. Supplemented on 30 September 2026 from the Defence Product Playbook; see `product-pages-review.md`.
- `dist/product-implementation.html`: Product implementation ("making the product right"), based on Chapter 3: readiness package (PRD, UI artefacts, organisational context), PRD to TRD to tasks, the six-stage loop, gates and independent assurance, factory platform, autonomy modes, measures and pilot readiness, with three figures. The final section, "Run the loop with the EDS workflow", summarises the EDS AI Development Workflow handbook (`../docs/EDS_Product_Development_Guide.docx`, cited by title only) with four more figures.
- `dist/training.html`: Training, a study guide to the Eitri Agentic Dev Workflow self-paced training (SGTechStack, linked): course map, key concepts from the prerequisites (model behaviour, context and loops, development principles, multi-agent patterns), one section per lesson (PO workflow, workflow skills, team context) and a study plan with self-check questions, with three figures.
- `dist/styles.css`: Shared styles from `../design.md`.
- `dist/site.js`: Responsive navigation and current-section indication.

Read `../writing.md`, `../design.md` and `../plan.md` before changes. Reference documents are not included in the public output. Publish only the contents of `dist/`, not the entire workspace. Relative links support hosting below a repository path.

Content remains a draft. Confirm the content owner, applicable lifecycle version and substantive review date before publishing maintained guidance. No remote repository or deployment has been created.

The ideation and implementation pages were reviewed and supplemented with online sources on 28 September 2026. See `product-pages-review.md` for the source mapping, editorial changes and validation, including experiment design, AI evaluation, delivery measures and release recovery.
