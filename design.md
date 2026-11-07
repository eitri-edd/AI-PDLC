# Design system proposal

For EDS’s AI-Software Development Lifecycle knowledge site
Status: Proposed visual system · Version: 0.6 · Updated: 7 November 2026

## Design direction

Build a sleek, polished, white-based enterprise knowledge site ("Editorial Enterprise Light", futuristic refresh) with pure white reading surfaces, whisper-quiet cool-alabaster panels, precision royal-blue accents extended by a sky-cyan secondary (`#0EA5E9`) and indigo, a subtle ambient sky wash behind the canvas, gradient accent hairlines on headings, cards and active navigation, crisp typographic hierarchy with a geometric display face (Space Grotesk) for titles and system labels, and generous whitespace. The experience should feel like an authoritative, modern engineering and product handbook—effortless to scan, comfortable for long-form reading, and crystal clear when presenting complex multi-agent workflows, human decision gates and delivery status.

This is a proposed project design system, not an official EDS brand standard. Confirm approved identity assets and corporate requirements before launch. Use the project title and icon mark until an approved corporate logo is available.

Pair this system with [writing.md](writing.md). Content clarity takes priority over decorative treatment.

## Principles

1. **Make reading and comprehension effortless.** Give explanations a stable, comfortable reading column (`47.5rem`, expanding to `58rem` when the left navigation rail is collapsed) on a pure white canvas (`#FFFFFF`), framed by subtle cool-alabaster navigation and context panels (`#F8FAFC`).
2. **Give topic explanations and examples distinct treatments.** Reserve the existing blue diagram theme for explaining topics, methods and general processes. Use the separate Matte Stone palette for fictional learning content. Royal blue still identifies navigation, links and focus; indigo can identify setup badges and secondary accents.
3. **Create depth through crisp hairline borders and micro-elevation.** Use `1px` borders (`#E2E8F0` and `#CBD5E1`) paired with subtle, multi-layered ambient shadows on cards, tables and diagram frames so structure is immediately legible without heavy chrome.
4. **Make structure, context and flow immediately visible.** Include an eyebrow label, lead paragraph and a 4-step at-a-glance **Page map** (`This page at a glance`) on every page, and use purposeful diagram geometry and motion to illustrate enclosing loops, decision gates, parallel fan-out and feedback paths.
5. **Keep interactions predictable, fast and accessible.** Prefer familiar links, collapsible navigation rails, instant table filtering and keyboard-accessible diagram controls (`Step through` and `Pause / Play`). Always honour `prefers-reduced-motion`.

## Colour tokens

Use semantic tokens in components so the palette remains consistent across pages and diagrams.

| Token | Value | Intended use |
| --- | --- | --- |
| `background` | `#FFFFFF` | Main reading canvas, article surface, table interior and diagram card shell |
| `surface-canvas` | `#FCFDFF` | Ultra-clean background for technical diagram grids and elevated cards |
| `surface-subtle` | `#F8FAFC` | Sidebar rail, table headers, figure headers and secondary panels |
| `surface-muted` | `#F1F5F9` | Code pills, neutral badges and subtle hover states |
| `surface-selected` | `#EFF6FF` | Selected navigation, note callouts and highlighted diagram nodes |
| `surface-accent-subtle` | `#F5F8FF` | Subtle tinted backgrounds for page maps and next-step banners |
| `surface-example` | `#F3F0EB` | Matte Stone surface for fictional learning content; alias of `example-surface` |
| `text-primary` | `#0F172A` | Headings, primary labels and diagram node titles |
| `text-body` | `#1E293B` | Long-form article body text for comfortable contrast |
| `text-secondary` | `#475569` | Metadata, captions, table cells and supporting descriptions |
| `text-muted` | `#64748B` | De-emphasised hints, breadcrumb dividers and secondary labels |
| `border-subtle` | `#E2E8F0` | Hairline separators, table row borders and card outlines |
| `border-strong` | `#CBD5E1` | Emphasised card borders, diagram frames and input outlines |
| `border-control` | `#64748B` | High-contrast diagram connectors and form controls |
| `accent` | `#1D4ED8` | Links, primary actions, active indicators and HITL decision highlights |
| `accent-2` | `#0EA5E9` | Sky-cyan secondary accent for gradient hairlines, glows and highlight dots |
| `accent-hover` | `#1E40AF` | Hovered links and interactive controls |
| `accent-pressed` | `#1E3A8A` | Pressed primary controls |
| `accent-soft` | `#DBEAFE` | Soft accent badge fill and diagram pulse rings |
| `accent-2-soft` | `#E0F2FE` | Soft sky fill for highlight rings and tinted gradients |
| `accent-border` | `#93C5FD` | Border for highlighted callouts, active cards and HITL nodes |
| `gradient-accent` | `linear-gradient(90deg, #1D4ED8, #0EA5E9 55%, #6366F1)` | Gradient hairlines on headings, card top rules, active nav bars and figure accents |
| `glow-accent` | `0 10px 30px -12px rgba(29, 78, 216, 0.3)` | Restrained accent glow on primary panels such as next-step cards |
| `indigo` / `indigo-soft` | `#4338CA` / `#EEF2FF` | One-time setup pills and secondary accents in the main theme |
| `focus` | `#2563EB` | Keyboard focus outline |
| `success-text` / `success-bg` | `#166534` / `#F0FDF4` | Confirmed completion or passing checks |
| `warning-text` / `warning-bg` | `#92400E` / `#FFFBEB` | Planned status, rework paths or conditions needing attention |
| `danger-text` / `danger-bg` | `#991B1B` / `#FEF2F2` | Errors, blockers or failed checks |

Use white text on solid accent buttons. Use primary, body or secondary text on white and neutral surfaces. Pair semantic status colours only with their designated light backgrounds and borders. Always include a text status label; colour alone does not convey meaning.

Keep blue purposeful. Avoid dark-mode neon glows, heavy full-bleed gradients or decorative AI stock art.

## Topic diagrams and fictional learning examples

Choose the visual's purpose before choosing its colours. The existing Editorial Enterprise Light blue diagram theme explains the topic or general content. Fictional applications use a separate **Matte Stone** treatment: warm neutral surfaces, charcoal text and muted clay accents. This gives the learning journey a restrained, serious appearance while its label makes the illustrative status explicit.

| Content | Theme and caption | What belongs in the visual |
| --- | --- | --- |
| Topic explanation | Existing white/alabaster and blue diagram theme; caption names the process or relationship being explained | General actions, roles, choices, dependencies and feedback that help explain the topic without a fictional application |
| Fictional learning example | Matte Stone; a visible “Learning example” label and a descriptive application caption | Application-specific actions, supplied scenario details, illustrative findings, example requirements and the worked journey |

A diagram that uses fictional asset-management records or sample results belongs to the second category. Split a visual that mixes general teaching and fictional evidence into two clearly bounded figures. Keep the main AI-SDLC overview at the topic level; place the continuous application journey in the product chapters. Follow [the writing standard's reference rules](writing.md#use-descriptive-names-for-references) for readable node, caption and link names.

### Matte Stone palette

| Token | Value | Use |
| --- | --- | --- |
| `example-surface` | `#F3F0EB` | Flat warm-stone background for the learning section or callout |
| `example-canvas` | `#E8E3DC` | Diagram canvas, caption band and table header |
| `example-card` | `#FAF8F4` | Flat node and table-cell surface |
| `example-ink` | `#2F3437` | Charcoal headings, body text and node labels |
| `example-secondary` | `#57534E` | Supporting text and captions |
| `example-accent` | `#7A4B3A` | Muted clay left rule, example badge, important node outlines and selected steps |
| `example-border` | `#837569` | Taupe connectors, boundaries and meaningful borders |

Use flat, opaque fills with no gradients, glossy highlights, neon colours, glows, dot grids, raised hover effects or decorative drop shadows. Keep typography, spacing and geometry consistent with the handbook. A clay border or stronger outline can emphasise the current step; retain textual roles and decision labels. This palette denotes fictional learning, not risk, approval or implementation status.

Charcoal text on the section surface has approximately 11.1:1 contrast; secondary text has 6.7:1. Clay on the canvas has 5.7:1, and the connector colour on the canvas has 3.5:1. Recheck actual combinations, overlays and interaction states during implementation. Preserve the existing accessible link and keyboard-focus colours; navigation controls need not adopt the example accent. Keep semantic success/warning/error colours only for genuine statuses, with text labels.

### Scope the complete learning example

- Apply the matte treatment to the whole example: heading/label, disclosure summary and body, tables, captions, node fills, connectors and diagram legends. A coloured badge above a blue blueprint is not sufficient.
- Use `.learning-example` for an explicit example wrapper; existing `.example` and `.worked-example` components adopt the same palette. Mark an applied SVG figure with `.concept-figure--example`, including when it stands outside a wrapper. These are authoring selectors to implement in the shared styles and diagram enhancer.
- Retain `.concept-figure` as the shared accessible figure structure. The default mode explains the topic; the example modifier overrides its appearance. Do not let the shared enhancer restore blue gradients, node elevation or flow pulses inside an example figure.
- Keep example figures still by default. A reader-controlled **Step through** action can reveal a meaningful sequence using a flat outline or fill change. Provide motion controls only when motion is actually used; honour reduced motion and print preferences.
- Use explicit “Learning example” text and a caption that names the application and action. Labels use descriptive names such as “Yearly declaration requirement” and “Check that retries preserve responses”, rather than pointer codes.
- When a reference table combines general guidance and an applied row or cell, separate and label the application with the matte treatment. Prefer a separate example block when a mixed table would obscure the distinction.
- AI assistance in a fictional application remains inside the matte example boundary, with a plain descriptive label. The teal “How AI can help” component continues to identify general delivery guidance outside that example.

The flat palette, labels, accessible text equivalents and readable boundaries also apply in print and with JavaScript disabled. Evaluate compliance on the rendered page; this specification does not imply that every existing page has already been migrated.

## How AI can help

Use this treatment to make AI assistance recognisable within the activity it supports. Keep the existing white reading surface, typography, navigation and status colours. Teal identifies AI assistance; it does not indicate that work is implemented, correct or approved.

| Token | Value | Use |
| --- | --- | --- |
| `ai-ink` | `#0F666A` | AI assistance labels and field headings; contrast exceeds 6:1 on white and the AI surface |
| `ai-rule` | `#147D82` | Recognisable left rule and framed AI text mark |
| `ai-surface` | `#F0F9F9` | Pale surface for a substantive AI task explanation |
| `ai-border` | `#B8D9DA` | Quiet dividers inside that explanation |

Apply the pattern at three scales:

- **Chapter orientation (`.ai-chapter-map`):** after the existing page map, show “How AI can help in this chapter” with two to four descriptive links to the relevant passages. Keep the existing table of contents as the complete reading route.
- **Task explanation (`.ai-help`):** place a pale teal panel beside the relevant activity. Use the literal label “How AI can help”, a descriptive task heading, and enough detail to identify the inputs, AI action, human checks and retained evidence. Use `.ai-help-facts` for “Give AI”, “AI helps by”, “People check” and “Keep as evidence” when a task needs structured explanation. Highlight existing useful passages rather than repeating them.
- **Short guidance (`.ai-help.ai-help--inline`):** use a slim teal rule and the same label when a short paragraph can explain the assistance and how its result is checked. Keep it on the white reading surface.

Use semantic asides for supporting guidance and preserve existing section anchors, sources, examples, status labels and decision authority. The framed “AI” mark is decorative; the visible text label communicates meaning without colour. Keep links and focus rings blue. Stack structured fields on narrow screens and retain labels and rules in print. The treatment needs no animation or JavaScript.

Reserve this treatment for AI helping the team perform delivery work. Keep guidance about AI inside the delivered product in its existing reference or example treatment, with an explicit explanation of when it applies. Deterministic tests, scanners and pipeline gates retain their own meanings, even when an agent invokes them or summarises their results. Describe proposed benefits as work AI can help with; measure improvements locally.

### Chapter-link alignment and responsive behaviour

Keep the chapter label on its own line, followed by a semantic list of links. Align the label and link list to the same left edge inside the teal rule.

- Above `40rem`, use a wrapping flex row with `align-items: baseline`. Links on the same row share a text baseline. Use `0.25rem` between rows and `1.25rem` between items; let links wrap naturally when the reading column narrows.
- Reset every direct list item with `.ai-chapter-map ul > li { margin: 0; min-width: 0; }`. This selector overrides the article’s general `.concept-article li + li` spacing rule. Otherwise, later links inherit a top margin and appear lower than the first link.
- At `40rem` and below, stack the links vertically. Use `0.5rem` vertical padding on each link for comfortable touch spacing; keep list-item margins at zero.
- Preserve blue, underlined links and visible keyboard focus. Use real section anchors so navigation works without JavaScript. In the skills catalogue, following an AI-help link clears active filters when necessary to reveal its target.

Check alignment across all 13 handbook pages at `1440px`, `768px`, `375px` and `320px`. Confirm that links on the same row align, wrapped rows retain consistent spacing, mobile links stack without horizontal overflow and every link reveals its destination. Keep this adjustment in the shared stylesheet rather than adding page-specific offsets.

## Typography

Use a modern enterprise sans-serif stack: `"Inter", "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif` for body text, loaded from Google Fonts (variable, `opsz` + `wght` axes) with `font-feature-settings: "cv02", "cv03", "cv04", "cv11"`. Use `"Space Grotesk", "Inter", "Segoe UI", system-ui, sans-serif` (Google Fonts, `wght 300–700`) for display roles: page/section/subsection headings, the brand identity, eyebrow and figure-number pills, uppercase system labels (page contents heading, status-key intro, page-map captions, table headers, kickers) and task-entry / learning-path card titles. Use `"JetBrains Mono", "Cascadia Code", Consolas, "SFMono-Regular", monospace` (Google Fonts, `wght 400–600`) for code and skill identifiers.

| Role | Desktop size / line height | Weight & styling |
| --- | --- | --- |
| Eyebrow label | 12 / 18 px (`0.75rem`) | 700, uppercase, `0.055em` letter-spacing, accent pill with leading dot |
| Page title (`h1`) | 40 / 47 px (`2.5rem`) | Space Grotesk, 700, `-0.035em` letter-spacing |
| Section heading (`h2`) | 27 / 35 px (`1.6875rem`) | Space Grotesk, 700, `-0.025em` letter-spacing, bottom hairline with `--gradient-accent` rule |
| Subsection heading (`h3`) | 20 / 28 px (`1.25rem`) | Space Grotesk, 650, `-0.015em` letter-spacing |
| Small heading (`h4`) | 18 / 26 px (`1.125rem`) | 600 |
| Introductory lead (`.lead`) | 19.5 / 32 px (`1.21875rem`) | 400, `--text-secondary` |
| Article body | 17 / 29 px (`1.0625rem`) | 400, `--text-body` |
| Navigation and controls | 14.5 / 22 px (`0.90625rem`) | 500; 600 when selected |
| Metadata and captions | 13.5 / 21 px (`0.84375rem`) | 500 |
| Code and skill tokens | 13.5 / 20 px (`0.84375rem`) | 500 |

At narrow widths, reduce the page title to `2rem` (32 px) and article body to `1rem` (16 px). Implement sizes in `rem` and line heights as unitless ratios so text responds to user settings.

Limit article paragraphs to 65–75 characters per line. Use sentence case for headings and navigation.

## Spacing, elevation and shape

Use a 4 px base with the scale `4, 8, 12, 16, 24, 32, 48, 64` px. Use 8 px between an icon and label, 16 px between paragraphs, 24 px inside panels, and 48 px between major article sections. Reduce section gaps to 36 px on mobile.

Use `6px` (`0.375rem`) corner radii for controls, `10px` (`0.625rem`) for callouts and status panels, and `12px` (`0.75rem`) for tables, diagram frames and page maps. Reserve pill shapes (`999px`) for status badges, figure numbers and eyebrow tags.

Pair `1px solid var(--border-subtle)` borders with restrained, sleek elevation tokens:
- `--shadow-xs`: `0 1px 2px rgba(15, 23, 42, 0.03), 0 1px 1px rgba(15, 23, 42, 0.02)` for cards, inputs and status keys.
- `--shadow-sm`: `0 4px 12px -2px rgba(15, 23, 42, 0.06), 0 1px 3px -1px rgba(15, 23, 42, 0.04)` for tables, diagram containers, page maps and hovered task cards.
- `--shadow-md`: `0 12px 28px -6px rgba(15, 23, 42, 0.09), 0 4px 10px -2px rgba(15, 23, 42, 0.04)` for hovered diagram cards and active interactive focus.

## Responsive page layout

Centre the site within a maximum width of `1440px` (`90rem`), including outer padding. Use `32px` outer padding on desktop, `24px` on tablet and `16px` on mobile.

| Viewport | Layout |
| --- | --- |
| `1400px` and wider | Collapsible `248px` (`15.5rem`) left sidebar (collapses to a `52px` / `3.25rem` slim rail), flexible article up to `760px` (`47.5rem`, expanding to `58rem` when sidebar is collapsed), `208px` (`13rem`) right-hand page contents; `40px` (`2.5rem`) column gaps. |
| `1100–1399px` | Collapsible `232px` (`14.5rem`) left sidebar plus flexible article; move "On this page" above the article body in a compact disclosure card. |
| Below `1100px` | Single column; navigation opens from a labelled disclosure bar at the top; "On this page" stays above the article body. |

Use a `64px` sticky translucent white header (`rgba(255, 255, 255, 0.94)` with `backdrop-filter: blur(12px)`) and a subtle `2px` royal-blue to indigo top border accent containing the project identity mark and organisation badge.

## Information architecture and page templates

Every page across the handbook follows a unified, predictable visual order:

1. **Breadcrumb trail** with subtle chevron separators (on all interior pages).
2. **Article header** (`.article-header`) with an uppercase **Eyebrow badge** (`.eyebrow`), **Page title** (`h1`), **Lead summary** (`.lead`) and supporting context.
3. **At-a-glance Page map** (`figure.page-map`) showing the 4 main reading steps or workflow stages on the page with direct anchor links.
4. **Mobile table of contents** (`details.mobile-contents`) for viewports below `1400px`.
5. **Article sections** (`section`) with crisp `h2` dividers, structured `.table-scroll` tables, interactive `.concept-figure` SVG diagrams, and distinct `.callout` (Note) and `.example` (Worked example) panels.
6. **Next-step action card** (`.next-step`) and a consistent **Article footer** (`.article-footer`).

## Component specifications

| Component | Appearance and behaviour |
| --- | --- |
| Text link | Royal blue (`--accent`), underlined with subtle offset and `1px` thickness. Darkens on hover with stronger underline. |
| Sidebar item | Comfortable `42px` row target with `18px` outline icon. Selected item uses a pure white card (`#FFFFFF`), `--accent` text, a `3px` left bar with a vertical `--accent` → `--accent-2` gradient, `--shadow-xs` and `aria-current="page"`. |
| Page contents | Right-hand sticky rail (`On this page`). Active section uses `--accent` text, font-weight `600`, a `2px` blue left indicator bar and soft blue tint. |
| Page map (`.page-map`) | Minimal Editorial Ledger spec-sheet (`1.5px` top rule, `1px` bottom rule, zero card background or shadow) with a unified 4-column horizontal hairline grid (`.page-map-nodes` and `.page-map-steps`). Each column is separated by a `1px` vertical hairline rule and displays a monospace slate numeral (`01`–`04` in JetBrains Mono, no pill), a bold heading in Space Grotesk and direct anchor links. |
| Task entry & learning path cards (`.task-entry`, `.discovery-path-card`, `.implementation-path-card`) | Responsive card grids on white-to-alabaster surfaces (`#FFFFFF` → `#F8FAFC`) with `1px` border, subtle shadow, bold title in Space Grotesk with animated trailing arrow, and clear workflow descriptions. Learning path cards use a unified, understated cool-slate palette at rest (soft slate pill kicker, `#CBD5E1` top rule, deep navy-slate heading) that highlights to royal blue on hover/focus. |
| Note Callout (`.callout`) | White-to-ice-blue panel (`#FFFFFF` to `#F5F8FF`) with `1px solid var(--accent-border)` and a `4px` solid `--accent` left rule. Includes a royal-blue uppercase pill label (`Note`). |
| Learning example (`.learning-example`, `.example`, `.worked-example`) | Flat `--example-surface` with a `1px` `--example-border` border, `4px` `--example-accent` left rule and charcoal text. Use a visible “Learning example” label on a flat canvas-coloured badge. Related tables and diagrams use the same Matte Stone palette. |
| Applied example figure (`.concept-figure--example`) | Shared accessible figure structure with the Matte Stone overrides above; flat nodes/canvas, descriptive labels and static default presentation. Keep the application caption and illustrative status visible. |
| Status badge (`.status`) | Pill badge (`999px` radius) with `1px` semantic border and subtle fill: `Core` (slate dark), `HITL` (royal blue), `Planned` (amber), `Optional · Recommended` (dashed blue-slate), `One-time setup` (indigo), `Available` (emerald green). |
| Table (`.table-scroll`) | Wrapped in a rounded `12px` white card with `1px` border and `--shadow-sm`. Features a generous first-column width system (`13.5rem`–`17.5rem` minimum widths depending on content, `white-space: nowrap` for code slugs/stage badges, `overflow-wrap: break-word`), `#F8FAFC` uppercase header row, and subtle row hover highlighting. |
| Code token (`code`) | Monospace font on `--surface-muted` (`#F1F5F9`) with `1px solid var(--border-subtle)` and `5px` radius. |
| Next-step panel (`.next-step`) | Rounded call-to-action card with a soft blue-tinted surface, `1px solid var(--accent-border)`, subtle shadow and clear action links. |

## Diagrams, icons and purposeful motion

A diagram earns its place by making the topic easier to understand. Choose a clear relationship, sequence or decision to explain, then use the smallest readable visual that conveys it. The blue blueprint styling below is reserved for general topic explanations. Fictional applications follow the Matte Stone specification above, while sharing accessible markup, legible geometry and text equivalents.

1. **Visual styling of topic SVG diagrams**:
   - **Figure container (`.concept-figure`)**: Pure white card (`#FFFFFF`) with `12px` border radius, `1px solid var(--border-strong)` border, and `--shadow-sm` (lifting to `--shadow-md` on hover).
   - **Figure header (`figcaption`)**: Clean top bar on `#F8FAFC` with an automatic pill badge (`Figure 1`, `Figure 2`, etc. in royal blue), clear title text, and the right-aligned interactive `.figure-toolbar`.
   - **Technical canvas (`.figure-scroll`)**: Ultra-clean white-alabaster surface (`#FCFDFF`) with a delicate `18px` dot grid (`radial-gradient(#CBD5E1 0.85px, transparent 0.85px)`) and `24px` (`1.5rem`) padding. All SVG `viewBox` dimensions include a safe outer margin so node borders and drop shadows never clip.
   - **Standard process nodes (`.d-node`)**: Crisp white cards (`url(#d-grad-node)`: `#FFFFFF` to `#F8FAFC`) with `8px` corner radius, `#94A3B8` border (`1.5px`), and a soft architectural drop shadow (`drop-shadow(0 3px 6px rgba(15, 23, 42, 0.06))`).
   - **Highlighted / HITL nodes (`.d-node-accent`)**: Soft blue gradient fill (`url(#d-grad-accent)`: `#EFF6FF` to `#DBEAFE`), `2px` royal blue stroke (`#1D4ED8`), and a subtle pulsing focus glow (`@keyframes d-gate-pulse`).
   - **Decision gates (`.d-decision`)**: Cut-corner octagon/diamond shapes with a dedicated decision fill (`url(#d-grad-decision)`: `#F0F7FF` to `#E0F2FE`) and `2px` `#2563EB` stroke so automated and human decision points stand out clearly from standard rectangular steps.
   - **Enclosing loops and phase swimlanes (`.d-group`, `.d-boundary`)**: Rounded containers (`rx="10"`–`12`) with `rgba(248, 250, 252, 0.92)` or `#FFFFFF` fills and crisp `#94A3B8` / dashed `#64748B` borders to visually enclose inner loops, parallel fan-out stages and phase columns.
   - **High-contrast SVG typography**:
     - `.d-title`: `15px–15.5px` bold (`700`) in deep navy-slate (`#0F172A`).
     - `.d-sub`: `13px–13.5px` medium (`500`) in slate (`#334155`).
     - `.d-label` and `.d-label-accent`: `12.5px–13px` semi-bold/bold (`#1E293B` / `#1D4ED8`) with a `5px` pure white (`#FFFFFF`) stroke halo (`paint-order: stroke fill`) so connector lines never cut through label text.
   - **Diagram legend footer (`.diagram-key`)**: Explain the line styles, symbols and decision highlights actually used in the figure. Keep the legend concise; do not add decorative keys for relationships the diagram does not contain.

2. **Purposeful animation and interactivity for topic diagrams**:
   - Use motion only when it helps explain sequence, direction, feedback or a decision. Static explanatory figures are valid; do not animate merely to decorate the page. The following effects are available for topic diagrams, not requirements for every figure or for examples.
   - **Animated flow signals (`.d-flow-pulse`)**: Forward connectors (`.d-line`, `.d-line-accent`) display a smooth, continuous directional flow pulse along the path (`stroke-dashoffset` animation) so readers can trace how work and evidence move through a loop or pipeline.
   - **Animated rework / feedback paths (`.d-dash`)**: Dashed feedback arrows animate gently in the direction of rework or learning feedback.
   - **Decision gate pulse**: Highlighted decision/HITL nodes (`.d-node-accent`, `.d-decision`) feature a gentle, non-distracting breathing glow.
   - **Interactive node focus & Step-through**: Hovering over any diagram node lifts the node and highlights it; clicking **Step through** in the figure toolbar highlights each node and connector in sequence.
   - **User control & Accessibility**: Every animated diagram includes a **Pause / Play** control. Pause animations when `prefers-reduced-motion: reduce` is enabled or when printing. Do not show playback controls on a still figure that has no animation.

3. **Readable labels and references**:
   - Describe actions, decisions and evidence in words. A node reading “Check yearly workflow retries” is understandable without a legend of pointer codes.
   - Apply the same names in the text equivalent, legend, caption, tables and links. Keep machine identifiers in anchors or linked technical records; do not expose them as the diagram's main vocabulary.
   - Retain meaningful step/figure numbers for navigation. Define established method/document abbreviations before using them; shorten or wrap descriptive labels before reducing text size.

## Accessibility target

Target WCAG 2.2 Level AA:
- Minimum text contrast of 4.5:1 for normal text (7:1+ achieved on body prose and diagram titles) and 3:1 for large text and non-text UI/diagram indicators.
- Full keyboard navigation, visible `2px` focus outlines with `2px` white offset, skip-to-content link and semantic landmarks.
- Respect `prefers-reduced-motion: reduce` across all CSS transitions and SVG diagram animations.
- Clean print output that expands text equivalents, removes navigation chrome and disables animations.

## Starter implementation tokens

```css
:root {
  color-scheme: light;
  --background: #ffffff;
  --surface-canvas: #fcfdff;
  --surface-subtle: #f8fafc;
  --surface-muted: #f1f5f9;
  --surface-selected: #eff6ff;
  --surface-accent-subtle: #f5f8ff;
  --example-surface: #f3f0eb;
  --example-canvas: #e8e3dc;
  --example-card: #faf8f4;
  --example-ink: #2f3437;
  --example-secondary: #57534e;
  --example-accent: #7a4b3a;
  --example-border: #837569;
  --surface-example: var(--example-surface);
  --text-primary: #0f172a;
  --text-body: #1e293b;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --border-subtle: #e2e8f0;
  --border-strong: #cbd5e1;
  --border-control: #64748b;
  --accent: #1d4ed8;
  --accent-hover: #1e40af;
  --accent-pressed: #1e3a8a;
  --accent-2: #0ea5e9;
  --accent-soft: #dbeafe;
  --accent-2-soft: #e0f2fe;
  --accent-border: #93c5fd;
  --gradient-accent: linear-gradient(90deg, #1d4ed8 0%, #0ea5e9 55%, #6366f1 100%);
  --glow-accent: 0 10px 30px -12px rgba(29, 78, 216, 0.3);
  --indigo: #4338ca;
  --indigo-soft: #eef2ff;
  --indigo-border: #c7d2fe;
  --focus: #2563eb;
  --success-text: #166534;
  --success-bg: #f0fdf4;
  --warning-text: #92400e;
  --warning-bg: #fffbeb;
  --danger-text: #991b1b;
  --danger-bg: #fef2f2;
  --shadow-xs: 0 1px 2px rgba(15, 23, 42, 0.03), 0 1px 1px rgba(15, 23, 42, 0.02);
  --shadow-sm: 0 4px 12px -2px rgba(15, 23, 42, 0.06), 0 1px 3px -1px rgba(15, 23, 42, 0.04);
  --shadow-md: 0 12px 28px -6px rgba(15, 23, 42, 0.09), 0 4px 10px -2px rgba(15, 23, 42, 0.04);
}
```

## Design acceptance checklist

Use this checklist for each changed page; mark items only after verification.

- [ ] The existing blue theme explains general topics and processes; each figure improves understanding of the surrounding content.
- [ ] Fictional learning panels, tables and diagrams use the complete, flat Matte Stone treatment with a visible “Learning example” label.
- [ ] No example-specific records or invented results appear in a blue topic diagram; mixed visuals are separated.
- [ ] Diagram labels, captions, accessible descriptions and links use descriptive names rather than invented pointer codes.
- [ ] Shared page chrome, navigation, focus indicators and genuine semantic statuses retain their intended roles.
- [ ] Reading width, typography, wrapping and diagrams remain legible on desktop, tablet, mobile and enlarged text settings.
- [ ] SVG content is unclipped, has an accurate text equivalent and explains connector/decision meanings where needed.
- [ ] Motion serves explanation, has controls where used, honours reduced motion and prints cleanly; learning examples are still by default.
- [ ] The diagram enhancer respects example scope rather than reapplying blueprint effects.
- [ ] Examples remain distinguishable without colour, without JavaScript and in print.
