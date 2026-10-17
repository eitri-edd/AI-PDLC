# Design system proposal

For EDS’s AI-Product Development Lifecycle knowledge site  
Status: Proposed visual system · Version: 0.2 · Updated: 17 October 2026

## Design direction

Build a crisp, white-based enterprise knowledge site ("Editorial Enterprise Light") with refined slate surfaces, precision royal-blue accents, clear typographic hierarchy and generous reading space. The experience should feel like an authoritative, modern engineering and product handbook: effortless to scan, comfortable for long-form reading, and visually clear about workflows, human decision gates and guidance status.

This is a proposed project design system, not an official EDS brand standard. Confirm approved identity assets and corporate requirements before launch. Use the project title and icon mark until an approved corporate logo is available.

Pair this system with [writing.md](writing.md). Content clarity takes priority over decorative treatment.

## Principles

1. **Make reading the primary activity.** Give explanations a stable, comfortable reading column (`47.5rem`) on a pure white canvas (`#FFFFFF`), framed by subtle cool-alabaster navigation and context panels (`#F8FAFC`).
2. **Use blue to communicate action, selection and decision authority.** Apply royal blue (`#1D4ED8`) to links, selected navigation, focus rings, primary actions and human-in-the-loop (HITL) decision nodes. Keep large surfaces white or neutral slate.
3. **Create depth through crisp borders and micro-elevation.** Use `1px` hairline borders (`#E2E8F0`) paired with subtle, multi-layered ambient shadows on cards, tables and diagram frames so structure is immediately legible without visual clutter.
4. **Make context and flow visible.** Show where the reader is in the site, provide at-a-glance page maps at the top of articles, and use purposeful diagram motion to illustrate forward flow, decision gates and feedback loops.
5. **Keep interactions predictable and accessible.** Prefer familiar links, disclosures, filterable tables and keyboard-accessible diagram controls. Always honour `prefers-reduced-motion`.

## Colour tokens

Use semantic tokens in components so the palette remains consistent across pages and diagrams.

| Token | Value | Intended use |
| --- | --- | --- |
| `background` | `#FFFFFF` | Main reading canvas, article surface and card interior |
| `surface-subtle` | `#F8FAFC` | Sidebar, table headers, figure canvas and secondary panels |
| `surface-muted` | `#F1F5F9` | Code pills, neutral badges and subtle hover states |
| `surface-selected` | `#EFF6FF` | Selected navigation, callouts and highlighted diagram nodes |
| `surface-accent-subtle` | `#F5F8FF` | Subtle tinted backgrounds for page maps and next-step banners |
| `text-primary` | `#0F172A` | Headings, primary labels and diagram node titles |
| `text-body` | `#1E293B` | Long-form article body text for comfortable contrast |
| `text-secondary` | `#475569` | Metadata, captions, table cells and supporting descriptions |
| `text-muted` | `#64748B` | De-emphasised hints, breadcrumb dividers and secondary labels |
| `border-subtle` | `#E2E8F0` | Hairline separators, table borders and card outlines |
| `border-strong` | `#CBD5E1` | Emphasised card borders, diagram containers and hover outlines |
| `border-control` | `#64748B` | Form controls, checkboxes and high-contrast diagram strokes |
| `accent` | `#1D4ED8` | Links, primary actions, active indicators and decision highlights |
| `accent-hover` | `#1E40AF` | Hovered links and interactive controls |
| `accent-pressed` | `#1E3A8A` | Pressed primary controls |
| `accent-soft` | `#DBEAFE` | Soft accent badge fill and diagram pulse rings |
| `accent-border` | `#93C5FD` | Border for highlighted callouts, active cards and HITL nodes |
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
| Eyebrow label | 12 / 18 px (`0.75rem`) | 600, uppercase, `0.06em` letter-spacing, accent pill |
| Page title (`h1`) | 40 / 48 px (`2.5rem`) | 700, `-0.025em` letter-spacing |
| Section heading (`h2`) | 28 / 36 px (`1.75rem`) | 650, `-0.018em` letter-spacing, subtle top divider |
| Subsection heading (`h3`) | 21 / 30 px (`1.3125rem`) | 600, `-0.01em` letter-spacing |
| Small heading (`h4`) | 18 / 28 px (`1.125rem`) | 600 |
| Introductory lead (`.lead`) | 20 / 32 px (`1.25rem`) | 400, `--text-secondary` |
| Article body | 17.5 / 29 px (`1.09375rem`) | 400, `--text-body` |
| Navigation and controls | 15 / 24 px (`0.9375rem`) | 500; 600 when selected |
| Metadata and captions | 14 / 22 px (`0.875rem`) | 400 |
| Code and skill tokens | 14 / 22 px (`0.875rem`) | 500 |

At narrow widths, reduce the page title to `2rem` (32 px) and article body to `1rem` (16 px). Implement sizes in `rem` and line heights as unitless ratios so text responds to user settings.

Limit article paragraphs to 65–75 characters per line. Use sentence case for headings and navigation.

## Spacing, elevation and shape

Use a 4 px base with the scale `4, 8, 12, 16, 24, 32, 48, 64` px. Use 8 px between an icon and label, 16 px between paragraphs, 24 px inside panels, and 48 px between major article sections. Reduce section gaps to 32 px on mobile.

Use `6px` (`0.375rem`) corner radii for controls, `10px` (`0.625rem`) for panels and tables, and `12px` (`0.75rem`) for diagram frames and page maps. Reserve pill shapes (`999px`) for status badges and eyebrow tags.

Pair `1px solid var(--border-subtle)` borders with restrained elevation tokens:
- `--shadow-xs`: `0 1px 2px rgba(15, 23, 42, 0.04)` for cards, tables and status keys.
- `--shadow-sm`: `0 2px 8px -2px rgba(15, 23, 42, 0.06), 0 1px 3px -1px rgba(15, 23, 42, 0.04)` for diagram containers, page maps and hovered task cards.
- `--shadow-md`: `0 10px 24px -4px rgba(15, 23, 42, 0.08), 0 2px 6px -1px rgba(15, 23, 42, 0.04)` for floating popovers or active interactive focus.

## Responsive page layout

Centre the site within a maximum width of `1440px` (`90rem`), including outer padding. Use `32px` outer padding on desktop, `24px` on tablet and `16px` on mobile.

| Viewport | Layout |
| --- | --- |
| `1400px` and wider | `248px` (`15.5rem`) left sidebar, flexible article up to `760px` (`47.5rem`), `208px` (`13rem`) right-hand page contents; `40px` (`2.5rem`) column gaps. |
| `1100–1399px` | `224px` (`14rem`) left sidebar plus flexible article; move "On this page" above the article body in a compact disclosure card. |
| Below `1100px` | Single column; navigation opens from a labelled disclosure bar at the top; "On this page" stays above the article body. |

Use a `64px` sticky translucent white header (`rgba(255, 255, 255, 0.92)` with `backdrop-filter: blur(10px)`) containing the project identity mark and organisation badge. Sticky navigation must scroll independently within the viewport and must not obscure focused controls or heading anchors.

## Information architecture and page templates

### Home and overview pages

Start with an eyebrow badge, the page title, a concise lead paragraph and a compact metadata bar. Follow with an at-a-glance **Page map** (`This page at a glance`) formatted as connected step cards, and—where task routing applies—an interactive grid of task entry cards.

### Guidance and workflow pages

Use this visual order:

1. Breadcrumb trail with subtle chevron separators.
2. Eyebrow badge, page title, lead summary and metadata bar.
3. At-a-glance page map (`figure.page-map`) showing the main sections or flow stages.
4. Article sections with clear `h2` dividers, structured tables, animated SVG diagrams, and tinted example/note callouts.
5. A prominent "Next step" action panel at the end of key sections or the page footer.

## Component specifications

| Component | Appearance and behaviour |
| --- | --- |
| Text link | Royal blue (`--accent`), underlined with subtle offset and `1px` thickness. Darkens on hover with stronger underline. |
| Sidebar item | Comfortable `42px` row target with `20px` outline icon. Selected item uses `--surface-selected`, `--accent` text, a `3px` left accent bar, subtle shadow and `aria-current="page"`. |
| Page contents | Right-hand sticky rail (`On this page`). Active section uses `--accent` text, font-weight `600`, and a `2px` blue left indicator bar. |
| Page map (`.page-map`) | Elevated subtle panel (`--surface-subtle`) with a 4-column horizontal step grid. Each step is a white card with a top accent border, step number badge, bold heading and direct anchor links, joined by directional connectors. |
| Task entry cards (`.task-entry`) | Responsive 2-column card grid on white surfaces with `1px` border, subtle shadow, bold title link with trailing arrow, and clear workflow steps. Hovering elevates the border to `--accent-border`. |
| Callout & Example (`.callout`, `.example`) | Tinted panel (`--surface-selected` or `#F8FAFC`) with `1px solid var(--accent-border)` and a `4px` solid `--accent` left rule. Includes an uppercase pill label (`Note`, `Example`). |
| Status badge (`.status`) | Pill badge (`999px` radius) with `1px` semantic border and subtle fill: `Core` (slate dark), `HITL` (royal blue), `Planned` (amber), `Optional · Recommended` (dashed blue-slate), `One-time setup` (indigo-slate). |
| Table | Wrapped in a rounded `.table-scroll` card with `1px` border and `--shadow-xs`. Features a generous, balanced first-column system (`13.5rem`–`17.5rem` minimum widths depending on content, `white-space: nowrap` for code slugs/stage badges, `overflow-wrap: break-word` with no mid-word truncation), uppercase header row (`--surface-subtle`), and responsive minimum table widths (`46rem`–`62rem`) so multi-column layouts never crush row labels. |
| Code token (`code`) | Monospace font on `--surface-muted` with `1px solid var(--border-subtle)` and `4px` radius. |
| Next-step panel (`.next-step`) | Rounded call-to-action card with a soft blue-tinted gradient background, `1px solid var(--accent-border)` and clear action links. |

## Diagrams, icons and purposeful motion

Diagrams are a signature part of the AI-SDLC handbook. They must look like precision architectural blueprints: clean, high-contrast, structured and purposefully animated.

1. **Visual styling of SVG diagrams**:
   - Present diagrams inside a `.figure-scroll` frame with a subtle dot-grid technical canvas background (`radial-gradient(#cbd5e1 1px, transparent 1px)` at `16px` intervals on `#f8fafc`), rounded corners (`12px`) and a clean top header bar showing the figure caption and controls.
   - **Standard nodes (`.d-node`)**: Crisp white cards (`#FFFFFF`) with `8px`–`10px` corner radius, `#94A3B8` border (`1.5px`), and a soft drop shadow (`drop-shadow(0 2px 4px rgba(15, 23, 42, 0.06))`).
   - **Highlighted / HITL / Decision nodes (`.d-node-accent`, `.d-decision`)**: Soft blue gradient fill (`#EFF6FF` to `#DBEAFE`), `2px` royal blue stroke (`#2563EB`), and a subtle pulsing focus ring to emphasise human accountability and key gates.
   - **Grouping boundaries (`.d-group`, `.d-boundary`)**: Rounded swimlanes or containers with `#F1F5F9` / `rgba(241, 245, 249, 0.55)` tint and dashed or subtle slate borders.
   - **Typography in SVG**: Primary node titles in `15px–16px` semi-bold (`#0F172A`); subtitles and descriptions in `13px–14px` regular (`#475569`); path labels backed by white halo/pill readability masks so connectors never cut through text.

2. **Purposeful animation and interactivity**:
   - **Animated flow signals**: Forward connectors (`.d-line`, `.d-line-accent`) display a smooth, continuous directional flow pulse along the path (`stroke-dashoffset` animation) so readers can immediately trace how work and evidence move through a loop or pipeline.
   - **Animated rework / feedback paths**: Dashed feedback arrows (`.d-dash`) animate gently in the direction of rework or learning feedback.
   - **Decision gate pulse**: Highlighted decision/HITL nodes (`.d-node-accent`) feature a gentle, non-distracting breathing border glow (`3s ease-in-out infinite`).
   - **Interactive node focus**: Hovering over any diagram node subtly lifts the node and highlights its connected paths.
   - **User control & Accessibility**: Every diagram includes a compact **Pause / Play flow** toggle button in the figure toolbar, and all CSS/SVG animations automatically pause when `prefers-reduced-motion: reduce` is enabled or when printing.
   - **Default visibility**: Diagrams are visible by default on all screens (no hidden `<details>` required to see the diagram), paired with a clean collapsible "Read as text" summary for screen readers and text-first readers.

## Accessibility target

Target WCAG 2.2 Level AA:
- Minimum text contrast of 4.5:1 for normal text and 3:1 for large text and non-text UI/diagram indicators.
- Full keyboard navigation, visible `2px` focus outlines with `2px` white offset, skip-to-content link and semantic landmarks.
- Respect `prefers-reduced-motion: reduce` across all CSS transitions and SVG diagram animations.
- Clean print output that expands text equivalents, removes navigation chrome and disables animations.

## Starter implementation tokens

```css
:root {
  color-scheme: light;
  --background: #ffffff;
  --surface-subtle: #f8fafc;
  --surface-muted: #f1f5f9;
  --surface-selected: #eff6ff;
  --surface-accent-subtle: #f5f8ff;
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
  --focus: #2563eb;
  --success-text: #166534;
  --success-bg: #f0fdf4;
  --warning-text: #92400e;
  --warning-bg: #fffbeb;
  --danger-text: #991b1b;
  --danger-bg: #fef2f2;
  --shadow-xs: 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-sm: 0 2px 8px -2px rgba(15, 23, 42, 0.06), 0 1px 3px -1px rgba(15, 23, 42, 0.04);
  --shadow-md: 0 10px 24px -4px rgba(15, 23, 42, 0.08), 0 2px 6px -1px rgba(15, 23, 42, 0.04);
}
```

## Design acceptance checklist

- [x] Crisp white and cool-alabaster surfaces dominate; royal blue consistently identifies links, active navigation and human decision gates.
- [x] All 13 site pages share unified tokens, elevated cards, refined tables and consistent typographic hierarchy.
- [x] Reading width, typography and spacing remain comfortable on desktop, tablet and mobile.
- [x] Every inline SVG diagram features professional node elevation, animated flow connectors, pulsing decision gates, interactive hover states and a Pause/Play motion control.
- [x] All animations honour `prefers-reduced-motion: reduce` and print cleanly.
- [x] Tables, diagrams and status badges include accessible text equivalents and semantic markup.

