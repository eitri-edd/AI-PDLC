# Design system proposal

For EDS’s AI-Software Development Lifecycle knowledge site  
Status: Proposed visual system · Version: 0.3 · Updated: 17 October 2026

## Design direction

Build a sleek, polished, white-based enterprise knowledge site ("Editorial Enterprise Light") with pure white reading surfaces, whisper-quiet cool-alabaster panels, precision royal-blue and indigo accents, crisp typographic hierarchy and generous whitespace. The experience should feel like an authoritative, modern engineering and product handbook—effortless to scan, comfortable for long-form reading, and crystal clear when presenting complex multi-agent workflows, human decision gates and delivery status.

This is a proposed project design system, not an official EDS brand standard. Confirm approved identity assets and corporate requirements before launch. Use the project title and icon mark until an approved corporate logo is available.

Pair this system with [writing.md](writing.md). Content clarity takes priority over decorative treatment.

## Principles

1. **Make reading and comprehension effortless.** Give explanations a stable, comfortable reading column (`47.5rem`, expanding to `58rem` when the left navigation rail is collapsed) on a pure white canvas (`#FFFFFF`), framed by subtle cool-alabaster navigation and context panels (`#F8FAFC`).
2. **Use royal blue and indigo with surgical precision.** Apply royal blue (`#1D4ED8`) to links, selected navigation, focus rings, primary actions and human-in-the-loop (HITL) decision nodes. Use soft indigo (`#4338CA`) to distinguish worked examples and setup badges from normative notes. Keep large surfaces pure white or whisper-soft slate.
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
| `surface-example` | `#F8FAFF` | Soft indigo-tinted surface for worked example callouts |
| `text-primary` | `#0F172A` | Headings, primary labels and diagram node titles |
| `text-body` | `#1E293B` | Long-form article body text for comfortable contrast |
| `text-secondary` | `#475569` | Metadata, captions, table cells and supporting descriptions |
| `text-muted` | `#64748B` | De-emphasised hints, breadcrumb dividers and secondary labels |
| `border-subtle` | `#E2E8F0` | Hairline separators, table row borders and card outlines |
| `border-strong` | `#CBD5E1` | Emphasised card borders, diagram frames and input outlines |
| `border-control` | `#64748B` | High-contrast diagram connectors and form controls |
| `accent` | `#1D4ED8` | Links, primary actions, active indicators and HITL decision highlights |
| `accent-hover` | `#1E40AF` | Hovered links and interactive controls |
| `accent-pressed` | `#1E3A8A` | Pressed primary controls |
| `accent-soft` | `#DBEAFE` | Soft accent badge fill and diagram pulse rings |
| `accent-border` | `#93C5FD` | Border for highlighted callouts, active cards and HITL nodes |
| `indigo` / `indigo-soft` | `#4338CA` / `#EEF2FF` | Worked example badges, one-time setup pills and secondary accents |
| `focus` | `#2563EB` | Keyboard focus outline |
| `success-text` / `success-bg` | `#166534` / `#F0FDF4` | Confirmed completion or passing checks |
| `warning-text` / `warning-bg` | `#92400E` / `#FFFBEB` | Planned status, rework paths or conditions needing attention |
| `danger-text` / `danger-bg` | `#991B1B` / `#FEF2F2` | Errors, blockers or failed checks |

Use white text on solid accent buttons. Use primary, body or secondary text on white and neutral surfaces. Pair semantic status colours only with their designated light backgrounds and borders. Always include a text status label; colour alone does not convey meaning.

Keep blue purposeful. Avoid dark-mode neon glows, heavy full-bleed gradients or decorative AI stock art.

## Typography

Use a modern enterprise sans-serif stack: `"Inter", "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif`. Use `"JetBrains Mono", "Cascadia Code", Consolas, "SFMono-Regular", monospace` for code and skill identifiers.

| Role | Desktop size / line height | Weight & styling |
| --- | --- | --- |
| Eyebrow label | 12 / 18 px (`0.75rem`) | 700, uppercase, `0.055em` letter-spacing, accent pill with leading dot |
| Page title (`h1`) | 40 / 47 px (`2.5rem`) | 750, `-0.03em` letter-spacing |
| Section heading (`h2`) | 27 / 35 px (`1.6875rem`) | 700, `-0.02em` letter-spacing, bottom hairline with accent rule |
| Subsection heading (`h3`) | 20 / 28 px (`1.25rem`) | 650, `-0.012em` letter-spacing |
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
| Sidebar item | Comfortable `42px` row target with `18px` outline icon. Selected item uses a pure white card (`#FFFFFF`), `--accent` text, a `3px` left accent bar, `--shadow-xs` and `aria-current="page"`. |
| Page contents | Right-hand sticky rail (`On this page`). Active section uses `--accent` text, font-weight `600`, a `2px` blue left indicator bar and soft blue tint. |
| Page map (`.page-map`) | Sleek white-and-alabaster container (`12px` radius, `1px` border, `--shadow-sm`) with a 4-column horizontal step grid. Each step is a crisp white card with a top accent bar, `01`–`04` pill badge, bold heading and direct anchor links, joined by directional connectors. |
| Task entry cards (`.task-entry`) | Responsive 2-column card grid on white surfaces with `1px` border, subtle shadow, bold title link with animated trailing arrow, and clear workflow steps. |
| Note Callout (`.callout`) | White-to-ice-blue panel (`#FFFFFF` to `#F5F8FF`) with `1px solid var(--accent-border)` and a `4px` solid `--accent` left rule. Includes a royal-blue uppercase pill label (`Note`). |
| Example Callout (`.example`) | White-to-indigo-alabaster panel (`#FFFFFF` to `#F8FAFF`) with `1px solid #C7D2FE` and a `4px` solid `#4338CA` left rule. Includes an indigo uppercase pill label (`Example`) so examples are visually distinct from policy/guidance notes. |
| Status badge (`.status`) | Pill badge (`999px` radius) with `1px` semantic border and subtle fill: `Core` (slate dark), `HITL` (royal blue), `Planned` (amber), `Optional · Recommended` (dashed blue-slate), `One-time setup` (indigo), `Available` (emerald green). |
| Table (`.table-scroll`) | Wrapped in a rounded `12px` white card with `1px` border and `--shadow-sm`. Features a generous first-column width system (`13.5rem`–`17.5rem` minimum widths depending on content, `white-space: nowrap` for code slugs/stage badges, `overflow-wrap: break-word`), `#F8FAFC` uppercase header row, and subtle row hover highlighting. |
| Code token (`code`) | Monospace font on `--surface-muted` (`#F1F5F9`) with `1px solid var(--border-subtle)` and `5px` radius. |
| Next-step panel (`.next-step`) | Rounded call-to-action card with a soft blue-tinted surface, `1px solid var(--accent-border)`, subtle shadow and clear action links. |

## Diagrams, icons and purposeful motion

Diagrams are a signature part of the AI-SDLC handbook. They must look like sleek, precision architectural blueprints on a clean white-based canvas: high-contrast, unclipped, structured and purposefully animated.

1. **Visual styling of SVG diagrams**:
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
   - **Diagram legend footer (`.diagram-key`)**: Every diagram includes a concise legend bar at the bottom of the figure explaining solid forward paths, dashed rework/feedback paths and highlighted decision gates.

2. **Purposeful animation and interactivity**:
   - **Animated flow signals (`.d-flow-pulse`)**: Forward connectors (`.d-line`, `.d-line-accent`) display a smooth, continuous directional flow pulse along the path (`stroke-dashoffset` animation) so readers can trace how work and evidence move through a loop or pipeline.
   - **Animated rework / feedback paths (`.d-dash`)**: Dashed feedback arrows animate gently in the direction of rework or learning feedback.
   - **Decision gate pulse**: Highlighted decision/HITL nodes (`.d-node-accent`, `.d-decision`) feature a gentle, non-distracting breathing glow.
   - **Interactive node focus & Step-through**: Hovering over any diagram node lifts the node and highlights it; clicking **Step through** in the figure toolbar highlights each node and connector in sequence.
   - **User control & Accessibility**: Every diagram includes a **Pause / Play** toggle button in the figure toolbar, and all animations automatically pause when `prefers-reduced-motion: reduce` is enabled or when printing.

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
  --surface-example: #f8faff;
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
  --accent-soft: #dbeafe;
  --accent-border: #93c5fd;
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

- [x] Crisp white (`#FFFFFF`) and cool-alabaster (`#F8FAFC`) surfaces dominate; royal blue and indigo consistently identify links, active navigation, examples and human decision gates.
- [x] All 13 site pages share unified tokens, eyebrow labels, 4-step at-a-glance page maps, elevated cards, refined tables, next-step banners and article footers.
- [x] Reading width, typography and spacing remain comfortable on desktop, tablet and mobile, with a collapsible left navigation rail that defaults to open.
- [x] Every inline SVG diagram features unclipped node elevation, gradient fills, distinct cut-corner decision styling, animated flow connectors, pulsing decision gates, interactive hover/step-through states and a diagram key.
- [x] All animations honour `prefers-reduced-motion: reduce` and print cleanly.
- [x] Tables, diagrams and status badges include accessible text equivalents and semantic markup.
