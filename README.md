# AI-SDLC Handbook — Authoring, Design, and Maintenance Guide

This repository contains the **Enterprise Digital Services (EDS) AI-SDLC Handbook** static documentation site (`site/dist/`) together with its governing editorial and design specifications:

- **[`writing.md`](./writing.md)** — Editorial guide defining voice, tone, British English conventions, house terminology, page archetypes, and the separation of requirements, recommendations, and examples.
- **[`design.md`](./design.md)** — Visual design and component guide defining the **Editorial Enterprise Light** theme (Version 0.2), layout architecture, typography, collapsible navigation, table column sizing, and interactive animated SVG diagrams.
- **[`site/dist/`](./site/dist/)** — The published static HTML handbook, shared stylesheet (`styles.css`), and progressive enhancement script (`site.js`).

Use this README as the operational reference whenever refining existing pages, updating diagrams or tables, or adding new content to the handbook.

---

## 1. Repository & Page Inventory

All published pages live in `site/dist/` and are organised into two main navigation groups plus three cross-referenced deep-dive pages.

### 1.1 Primary Navigation: AI-SDLC Core (`site/dist/`)

| File | Nav Title | Archetype | Primary Purpose & Scope |
| :--- | :--- | :--- | :--- |
| [`index.html`](./site/dist/index.html) | **Introduction** | Overview / Orientation | Explains why AI changes software delivery, the shifting bottleneck (from typing code to intent, verification, and context), the three handbook layers (*Principles*, *Operating requirements*, *Eitri implementation*), and the 6 key pointers. |
| [`transformation.html`](./site/dist/transformation.html) | **Organisation transformation** | Concept + Operating Guide | Covers the 4 pillars (*People*, *Process*, *Culture*, *Technology*), T-shaped role evolution, multidisciplinary squads, human vs agent task boundaries, and the 3-month pilot scorecard. |
| [`concept.html`](./site/dist/concept.html) | **Concepts** | Concept Reference | Defines 8 foundational concepts with animated diagrams: *Intent-driven development*, *Spec-driven development*, *Context engineering*, *Harness engineering*, *Loop engineering*, *Graph engineering* (multi-agent execution with automated decision gates), *Software factories*, and *AI models*. |
| [`ai-pdlc.html`](./site/dist/ai-pdlc.html) | **AI-SDLC overview** | Lifecycle Overview | Introduces the two connected loops—**Product ideation** and **Product implementation**—joined across the middle by the *Handoff* (PRD + UI artefacts) and shared *Context input*, with inner rework loops and production feedback. |
| [`product-ideation.html`](./site/dist/product-ideation.html) | **Product ideation** | Lifecycle Stage | Details the outer discovery loop: **Frame** (thesis, explore, challenge), **Test** (specify, prototype, measure, learn), and **Decide** (commit, rework, or stop), plus the 4C readiness check and metric ladder. |
| [`product-implementation.html`](./site/dist/product-implementation.html) | **Product implementation** | Lifecycle Stage | Details the inner delivery loop: readiness package (PRD + UI artefacts + context), the `PRD → TRD → Tasks` artefact chain, the 6 implementation stages (*Plan*, *Slice*, *Implement*, *Verify*, *Release & observe*, *Learn*), separation of duties, and factory modes (*Co-pilot*, *Light factory*, *Dark factory*). |

### 1.2 Primary Navigation: EDS AI Workflow (`site/dist/`)

| File | Nav Title | Archetype | Primary Purpose & Scope |
| :--- | :--- | :--- | :--- |
| [`eds-ai-workflow.html`](./site/dist/eds-ai-workflow.html) | **EDS AI Workflow (Eitri)** | Implementation Overview | Maps the AI-SDLC operating model onto the Eitri toolchain across 4 areas: *PO/BA harness*, *Developer harness*, *Path to production*, and *Team context*, with delivery status badges (`Implemented`, `Planned`, `Under evaluation`, `Draft`). |
| [`eds-po-ba-harness.html`](./site/dist/eds-po-ba-harness.html) | **PO/BA harness** | Procedure / Harness Guide | Explains the 3 paths to produce a structured PRD before engineering begins: *Path 1 (SpecKit)*, *Path 2 (Socratic workflow)*, and *Path 3 (CLARA research)*. |
| [`eds-developer-harness.html`](./site/dist/eds-developer-harness.html) | **Developer harness** | Procedure / Step Reference | Walks through the 19 Eitri developer workflow steps across 4 phases: **Plan** (Steps 1–6), **Check** (Steps 7–10, including HITL Gate 1 & Gate 2), **Build** (Steps 11–12), and **Close out** (Steps 13–19). |
| [`eds-path-to-production.html`](./site/dist/eds-path-to-production.html) | **Path to production** | Gate & Pipeline Guide | Defines the 4 automated and human release stages: *4.1 Pre-commit (local)*, *4.2 Merge to Dev*, *4.3 Merge to QA*, and *4.4 Pre-production readiness*. |

### 1.3 Cross-Referenced Companion Pages (`site/dist/`)

These pages are linked from within the workflow pages and top breadcrumbs and share the exact same shell and navigation:

| File | Title | Archetype | Primary Purpose & Scope |
| :--- | :--- | :--- | :--- |
| [`eds-team-context.html`](./site/dist/eds-team-context.html) | **Team context** | Setup & Reference | Explains the 5-stage progressive context model, domain knowledge documents (`domain.md`), AppStandards registration, and the project context checklist. |
| [`eds-skills-catalogue.html`](./site/dist/eds-skills-catalogue.html) | **Skills catalogue** | Filterable Reference | Interactive, searchable catalogue of all Eitri, Matt Pocock, Impeccable, review, compliance, architecture, and MCP skills (`data-filter-input` + `data-filter-button`). |
| [`training.html`](./site/dist/training.html) | **Training companion guide** | Training / Curriculum | Practical onboarding guide covering Prerequisites and Lessons 0–2 (foundations, memory stores, RAG/OKF/MCP, and 5-phase context injection). |

---

## 2. Editorial & Writing Standards (from `writing.md`)

Every content update must follow the rules in [`writing.md`](./writing.md).

### 2.1 Audience & Layer Separation
Write for mixed delivery squads (Product Owners, Business Analysts, Engineers, QA, Security, Risk, and Engineering Managers). Keep the three content layers distinct:
1. **Principles and concepts** — Why the practice matters and what problem it solves (`index.html`, `transformation.html`, `concept.html`).
2. **Operating requirements** — What artefacts, checks, roles, and handoffs must exist (`ai-pdlc.html`, `product-ideation.html`, `product-implementation.html`).
3. **Eitri implementation** — How EDS implements those requirements today with specific skills, commands, and pipeline gates (`eds-*.html`, `training.html`).

### 2.2 Voice, Tone, and Language Rules
- **British English**: Use British spelling throughout (*organisation*, *artefact*, *standardise*, *behaviour*, *prioritise*, *catalogue*, *analyse*).
- **Direct, active voice**: Address the reader as *you* or name the specific role (*the Product Owner*, *the tech lead*, *the developer*, *the release owner*).
- **Sentence & paragraph length**: Aim for **15–25 words** per sentence and **3–5 sentences** per paragraph. Put one idea in each sentence.
- **Concrete verbs over buzzwords**: Prefer *specify, test, review, approve, deploy, measure, roll back*. Avoid *unlock, supercharge, revolutionary, seamless, paradigm, game-changing*.
- **Personification boundary**: Describe what a model or agent *generates*, *retrieves*, *checks*, or *executes*. Never write that an AI *believes*, *understands*, *cares*, or *takes responsibility*.

### 2.3 House Terminology

Always use the preferred term consistently across all pages:

| Preferred Term | Usage Rule | Avoid |
| :--- | :--- | :--- |
| **AI-Product Development Lifecycle** (`AI-SDLC`) | Expand on first mention on top-level pages, then use `AI-SDLC`. | Unexplained switching between `AI-PDLC` and `AI-SDLC` |
| **AI-assisted development** | Use when AI tools help teams design, write, test, or document software. | Confusing with an *AI product* |
| **AI product** or **AI feature** | Use when the delivered software itself uses AI at runtime. | Calling every project an "AI project" |
| **AI agent** | A system that plans or executes multi-step tasks using tools within defined bounds. | Using *agent* for a simple prompt or autocomplete |
| **Artefact** | Any durable output: PRD, TRD, task list, test report, threat model, runbook. | Vague references to "outputs" |
| **Evaluation** | Structured testing of model, prompt, or agent quality against defined criteria. | Calling ad-hoc spot checks "evaluation" |
| **Review** vs **Approval** | **Review** = examining work and giving feedback; **Approval** = formal sign-off by a named role to pass a gate. | Using *review* when a gate requires formal sign-off |

### 2.4 Requirements vs Recommendations vs Examples

Never blur mandatory policy with advice or illustrative scenarios:

1. **Requirements (`must` / `required`)**:
   - Use **only** when backed by a confirmed EDS source document or mandatory gate.
   - Always state **who** is accountable, **what** action is required, **when** it happens, and **what artefact** proves completion.
2. **Recommendations (`should` / `recommended`)**:
   - Use for good practice that teams may adapt. State the trade-off or condition when teams adapt it.
3. **Examples (`Example` callout or explicit label)**:
   - Label clearly as an example. Use neutral, realistic software delivery scenarios (such as an internal service-request portal or CSV export feature).
   - **Never** invent EDS policy names, committee names, mandatory roles, metrics, or approval boards inside an example.

### 2.5 Page Archetype Templates

When creating or refactoring a page, follow its archetype structure from `writing.md`:

- **Concept Page (`concept.html`, `transformation.html`)**:
  1. **Summary** (2–3 sentences: what it is and why it matters)
  2. **Why it matters** (risk reduced or delivery problem solved)
  3. **How it works** (steps, loops, inputs/outputs, animated SVG diagram)
  4. **In practice at EDS** (how roles apply it)
  5. **Common pitfalls** (3–5 specific failure modes and fixes)
  6. **Related pages**
- **Lifecycle Stage Page (`ai-pdlc.html`, `product-ideation.html`, `product-implementation.html`)**:
  Answer in order: *Purpose*, *Entry criteria*, *Activities* (human vs AI tasks), *Outputs & artefacts*, *Exit criteria & approval gates*, *Risks & controls*, and *Hand-off to the next stage*.
- **Procedure / Harness Page (`eds-*.html`)**:
  Include *Goal*, *When to use*, *Prerequisites*, *Numbered steps* (one action per step + expected output), *Verification*, and *Owner / review cycle*.

---

## 3. Visual Design & Technical Standards (from `design.md`)

All pages share [`site/dist/styles.css`](./site/dist/styles.css) (**Editorial Enterprise Light**, Version 0.2) and [`site/dist/site.js`](./site/dist/site.js).

### 3.1 Colour Palette & Contrast Rules
- **Surfaces**: Crisp alabaster page canvas (`--bg-canvas: #fafcff`), pure white elevated cards and tables (`--bg-surface: #ffffff`), cool slate headers/code blocks (`--bg-subtle: #f3f6fb`), and soft blue active highlights (`--bg-muted: #e8eef7`).
- **Typography**: Deep navy-slate primary ink (`--text-primary: #0f172a`), secondary prose (`--text-secondary: #334155`), and muted captions (`--text-muted: #475569`).
- **Accents & Status Badges**:
  - Royal cobalt primary (`--accent-primary: #1d4ed8`) and indigo secondary (`--accent-secondary: #4338ca`).
  - Semantic status pills (`.status-badge`):
    - `.status-implemented` / `.status-complete` — Emerald (`#047857` on `#ecfdf5`)
    - `.status-planned` — Amber (`#b45309` on `#fffbeb`)
    - `.status-evaluation` — Indigo (`#4338ca` on `#eef2ff`)
    - `.status-draft` — Slate (`#334155` on `#f1f5f9`)
- **Accessibility**: Maintain **WCAG 2.2 AA** minimum contrast (`4.5:1` for body text, `7:1+` target for prose, `3:1` for borders and diagram connectors). Never use colour alone to communicate status.

### 3.2 Page Shell & Collapsible Left Navigation

Every HTML page in `site/dist/` must use the standard 3-zone layout inside `<div class="page-layout">`:

1. **Skip link & Sticky Header** (`<a class="skip-link" href="#main-content">`, `<header class="site-header">`).
2. **Collapsible Left Navigation** (`<aside class="sidebar-left" aria-label="Primary">`):
   - Wrap the navigation in `<details class="site-navigation" open>` so it is **open by default** on all viewports and collapsible into a `3.25rem` slim rail on desktop (`≥ 64rem`).
   - Place `aria-current="page"` on the link for the current page.
   - `site.js` automatically binds `.site-navigation` to toggle `.page-layout.sidebar-collapsed` and updates the `title` and `aria-label`.
3. **Main Article** (`<main id="main-content"> <article>`):
   - Breadcrumb (`<nav class="breadcrumbs" aria-label="Breadcrumb">`)
   - Article header (`<header class="article-header">` with `<p class="eyebrow">`, `<h1>`, `<p class="lead">`, and `<ul class="metadata-bar">`)
   - Page summary box (`<aside class="page-map" aria-label="Page summary">` with *What this page covers*, *Key takeaways*, and *Read time*)
   - Mobile table of contents (`<details class="mobile-contents">`)
   - Body sections (`<section id="..."><h2>...</h2>...</section>`)
   - Next-step card (`<aside class="next-step" aria-label="Next step">`) and `<footer class="article-footer">`
4. **Right On-Page Contents** (`<aside class="page-contents" aria-label="On this page">`).

### 3.3 Tables & First-Column Width System

Wide multi-column tables must be wrapped in `<div class="table-wrap" role="region" aria-label="..." tabindex="0">` so they scroll horizontally on small screens without breaking the layout.

To prevent the first column from wrapping prematurely on multi-word labels, steps, or skill names, apply the appropriate semantic table class from `styles.css`:

| Table Class | First-Column Width | When to Use |
| :--- | :--- | :--- |
| *(default `table`)* | `min-width: 13.5rem` (`22%–30%`) | Standard 2-to-4 column comparison and reference tables. |
| `.wide-col-first` | `min-width: 15.5rem` (`25%–32%`) | Tables with multi-word stage names, role titles, or artefact labels in column 1. |
| `.step-table` | `min-width: 5.5rem` (col 1), `14rem` (col 2) | Numbered workflow tables where column 1 is a step badge (`Step 1`) and column 2 is the step or command name (`eds-developer-harness.html`). |
| `.skills-table` | `min-width: 15.5rem` (`24%–30%`) | Tables listing hyphenated skill identifiers or slash commands in column 1 (`eds-skills-catalogue.html`, `eds-po-ba-harness.html`). |
| `.pipeline-table` | `min-width: 14.5rem` (`23%–28%`) | CI/CD and release gate tables (`eds-path-to-production.html`). |
| `.stage-table` | `min-width: 14.5rem` (`23%–28%`) | Lifecycle stage breakdown tables (`product-ideation.html`, `product-implementation.html`). |
| `.competency-table` | `min-width: 15rem` (`24%–30%`) | Role and competency matrices (`transformation.html`). |
| `.wide-table` | `min-width: 44rem` overall table | Combine with any class above when a table has 4+ dense columns. |

### 3.4 Animated & Interactive SVG Diagrams

All conceptual and workflow diagrams must be authored as accessible inline SVGs inside `<figure class="concept-figure">` and follow these rules:

1. **Top Caption & Reading Guide**:
   - Place `<figcaption>` **at the top** of `<figure class="concept-figure">` with a `<span class="figure-number">Figure N</span>` badge and title.
   - Immediately follow with a collapsed `<details class="figure-reading"><summary>How to read this diagram</summary>...</details>`.
2. **Interactive SVG Container**:
   - Place the `<svg>` inside `<details class="diagram-detail" open>` and `<div class="diagram-scroll">`.
   - Include `<title id="...">` and `<desc id="...">` linked via `aria-labelledby` on the `<svg>`.
3. **Standard SVG Classes (`styles.css` + `site.js`)**:
   - **Containers & boundaries**: `.d-boundary` (outer loop/system container, `#f8fafc` fill, dashed border) and `.d-group` (inner stage/loop container).
   - **Nodes**: `.d-node` (standard white card node), `.d-node-accent` (highlighted blue card node), `.d-decision` (amber decision gate, automatically receives subtle `@keyframes d-gate-pulse`). Add `data-step="1"`, `data-step="2"`, etc. on `<g>` nodes if you want the interactive **Step through** toolbar button to highlight nodes in sequence.
   - **Connectors & Animation**:
     - `.d-line` (primary solid connector) and `.d-line-accent` (primary active flow connector). `site.js` automatically clones these paths into animated `.d-flow-pulse` overlays and injects the `.figure-toolbar` (*Animated flow*, *Pause/Play*, and *Step through*).
     - `.d-dash` (rework, feedback, or conditional loop path—automatically animates with marching dashes `@keyframes d-march`).
   - **High-Contrast Typography**:
     - `.d-title` (`13.5px`, weight `700`, `#0f172a`) for node headings.
     - `.d-sub` (`11.5px`, weight `500`, `#1e293b`) for node subtitles.
     - `.d-label` (`11.5px`, weight `600`, `#0f172a` with a `3px` `#fafcff` paint-order halo so labels remain legible even when crossing connector lines).
4. **Reduced Motion**:
   - All CSS keyframe animations and JS flow pulses automatically respect `@media (prefers-reduced-motion: reduce)` and can be paused at any time via the diagram toolbar.

---

## 4. Step-by-Step Workflow for Updating or Adding Content

### Step 1: Plan the Change Against the Three Layers
1. Identify whether the change belongs to **Principles & concepts** (`index.html`, `transformation.html`, `concept.html`), **Operating requirements** (`ai-pdlc.html`, `product-ideation.html`, `product-implementation.html`), or **Eitri implementation** (`eds-*.html`, `training.html`).
2. Check whether the update introduces a **Requirement** (`must`—requires a confirmed EDS source), a **Recommendation** (`should`), or an **Example** (must be explicitly labelled and use fictional product scenarios).

### Step 2: Author or Update the HTML Structure
1. Use semantic headings (`<h2>` with a kebab-case `id`, followed by `<h3>` where needed). Never skip heading levels.
2. Update both the `<details class="mobile-contents">` list and the right-hand `<aside class="page-contents">` list whenever you add, rename, or remove an `<h2>` section.
3. If adding a new page, add its link to `<details class="site-navigation" open>` across **all** HTML files in `site/dist/` so navigation stays identical site-wide.
4. Update the `<ul class="metadata-bar">` (*Last updated* date and *Status*) when making substantive changes.

### Step 3: Add or Refine Callouts, Tables, and Diagrams
- **Callouts**: Use `<aside class="callout callout-note|callout-tip|callout-warning|callout-danger|callout-example">` with `<p class="callout-title">`. Keep callouts to 2–4 sentences and never stack two callouts back-to-back.
- **Tables**: Wrap in `<div class="table-wrap" role="region" aria-label="..." tabindex="0">` and apply the appropriate first-column width class (`.wide-col-first`, `.step-table`, `.skills-table`, `.pipeline-table`, `.stage-table`, or `.competency-table`).
- **Diagrams**: Follow the `<figure class="concept-figure">` structure, ensure every text node uses `.d-title`, `.d-sub`, or `.d-label` (never low-contrast grey text on shaded backgrounds), and verify that inner and outer loops are visually enclosed when depicting iterative workflows.

### Step 4: Run the Pre-Publication Checklist

Before considering any content or design update complete, verify every item below:

- [ ] **Layer & source accuracy (`writing.md`)**: Requirements (`must`), recommendations (`should`), and examples are clearly separated; no EDS committees, roles, or policies are invented inside examples.
- [ ] **Language & tone (`writing.md`)**: British English spelling is used throughout; sentences average 15–25 words; active voice and house terminology (`AI-SDLC`, `artefact`, `evaluation`, `review` vs `approval`) are used consistently.
- [ ] **Navigation & ToC sync (`design.md`)**: `<details class="site-navigation" open>` is present and collapsible on all pages; `aria-current="page"` is set on the active page; mobile and desktop "On this page" links match all `<h2>` IDs.
- [ ] **Table readability (`design.md`)**: Every multi-column table is inside `.table-wrap` and uses the appropriate table class so first-column labels do not wrap awkwardly.
- [ ] **Diagram legibility & animation (`design.md`)**: Every SVG diagram has `<title>` and `<desc>`, uses high-contrast node fills (`.d-node`, `.d-node-accent`) and text classes (`.d-title`, `.d-sub`, `.d-label`), and works cleanly with the interactive `.figure-toolbar`.