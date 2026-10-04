# Design system proposal

For DSTA’s AI-Product Development Lifecycle knowledge site  
Status: Proposed visual system · Version: 0.1 · Updated: 27 September 2026

## Design direction

Build a white-based knowledge site with restrained blue accents, clear typography and generous reading space. The experience should feel like a well-edited enterprise handbook: easy to navigate, comfortable to read and precise about the status of its guidance.

This is a proposed project design system, not an official DSTA brand standard. Confirm approved identity assets and corporate requirements before launch. Use the project title as text until an approved logo is available.

Pair this system with [writing.md](writing.md). Content clarity takes priority over decorative treatment.

## Principles

1. **Make reading the primary activity.** Give explanations a stable, narrow reading column. Reserve cards for navigation and summaries.
2. **Use blue to communicate.** Apply it to links, selected navigation, focus and the main action. Keep large surfaces white or neutral.
3. **Show structure consistently.** Reuse heading levels, spacing and page templates across lifecycle stages.
4. **Make context visible.** Show where the reader is, which guidance they are reading and where to go next.
5. **Keep interactions predictable.** Prefer familiar links, buttons, disclosures and tables over bespoke controls.

## Colour tokens

Use semantic tokens in components so the palette can change without rewriting layouts.

| Token | Value | Intended use |
| --- | --- | --- |
| `background` | `#FFFFFF` | Main canvas and article surface |
| `surface-subtle` | `#F8FAFC` | Sidebar, table headers and code background |
| `surface-selected` | `#EFF6FF` | Selected navigation and informational panels |
| `text-primary` | `#0F172A` | Headings and body text |
| `text-secondary` | `#475569` | Metadata, captions and supporting text |
| `border-subtle` | `#E2E8F0` | Decorative separators and card outlines |
| `border-control` | `#64748B` | Input and control boundaries where needed |
| `accent` | `#1D4ED8` | Links, primary buttons and selected indicators |
| `accent-hover` | `#1E40AF` | Hovered links and primary buttons |
| `accent-pressed` | `#1E3A8A` | Pressed primary button |
| `focus` | `#2563EB` | Keyboard focus outline |
| `success-text` / `success-bg` | `#166534` / `#F0FDF4` | Confirmed completion |
| `warning-text` / `warning-bg` | `#92400E` / `#FFFBEB` | A condition needing attention |
| `danger-text` / `danger-bg` | `#991B1B` / `#FEF2F2` | Errors or failed checks |

Use white text on solid accent buttons. Use primary or secondary text on white and neutral surfaces. Pair semantic status colours only with their designated light backgrounds. Always include a status label; colour alone does not convey meaning.

Keep blue visually sparse. Avoid full-page blue backgrounds, gradients, glow effects, glass effects and decorative AI imagery. The subtle border token is decorative; do not rely on it alone to identify an interactive control.

## Typography

Use the locally available system sans-serif stack: `"Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif`. This suits an enterprise reading experience without an external font request. Use `Consolas, "SFMono-Regular", monospace` for code.

| Role | Desktop size / line height | Weight |
| --- | --- | --- |
| Page title | 40 / 48 px | 600 |
| Section heading | 28 / 36 px | 600 |
| Subsection heading | 22 / 30 px | 600 |
| Small heading | 18 / 28 px | 600 |
| Introductory paragraph | 20 / 32 px | 400 |
| Article body | 18 / 30 px | 400 |
| Navigation and controls | 16 / 24 px | 400; 600 when selected |
| Metadata and captions | 14 / 22 px | 400 |
| Code | 14 / 22 px | 400 |

At narrow widths, reduce the title to 32 / 40 px and article body to 16 / 28 px. Keep labels at least 14 px. Implement sizes in `rem` and line heights as unitless ratios so text responds to user settings.

Limit article paragraphs to about 65–75 characters per line. Use sentence case, left alignment and bold sparingly. Do not justify paragraphs or use all caps for navigation.

## Spacing and shape

Use a 4 px base with the scale `4, 8, 12, 16, 24, 32, 48, 64` px. Use 8 px between an icon and label, 16 px between paragraphs, 24 px inside panels, and 48 px between major article sections. Reduce section gaps to 32 px on mobile.

Use 6 px corner radii for controls and 8 px for panels. Reserve pill shapes for short status labels. Default to borders without shadows; a small shadow is appropriate for a floating menu or search dialog. Avoid making every paragraph a separate panel.

## Responsive page layout

Centre the site within a maximum width of 1440 px, including its outer padding. Use 32 px outer padding on desktop, 24 px on tablet and 16 px on mobile.

| Viewport | Layout |
| --- | --- |
| 1280 px and wider | 240 px left navigation, flexible article up to 760 px, 192 px page contents; 32 px column gaps. |
| 960–1279 px | 224 px left navigation plus flexible article; move page contents above the article body in a disclosure. |
| Below 960 px | Single column; navigation opens from a labelled menu button; page contents stays above the body. |

Use a 64 px header containing the project identity and a small number of primary navigation links. Allow it to grow if labels wrap. Sticky navigation must scroll within the viewport and must not obscure focused controls or heading anchors.

On mobile, keep the project title legible and the menu button reachable. If navigation uses a modal drawer, move focus into it, support Escape, contain focus while open and return focus to its trigger when closed.

## Information architecture and page templates

Proposed top-level sections are **Overview**, **Lifecycle**, **Practices**, **Templates** and **Glossary**. Confirm their content and labels as the lifecycle is defined. Keep each page in one primary location and cross-link related guidance.

### Home page

Start with the project title, a brief explanation of the site and a “Explore the lifecycle” link styled as the primary action. Follow with a lifecycle overview and a short set of entry points for common tasks. Use a modest introduction rather than a tall promotional hero.

Present the agreed lifecycle as a numbered list or connected sequence. Use a vertical list on mobile. Show feedback paths where the actual process includes them; numbering must not imply a strictly linear process if stages can be revisited.

### Guidance and stage pages

Use this visual order:

1. Breadcrumbs.
2. Page title and short introduction.
3. Compact metadata: content status, owner, last reviewed and applicable version.
4. Article sections following the appropriate template in `writing.md`.
5. Related guidance and a clear next step.

Keep the active page visible in the sidebar. Use the right-hand contents list only for headings on the current page. Distinguish article status from project or product status.

### Template pages

Describe the template’s purpose and required inputs before the download link. Show format, version and a short preview or worked example. Offer an HTML explanation even when the reusable file is a download.

## Component specifications

| Component | Appearance and behaviour |
| --- | --- |
| Text link | Blue and underlined within prose. Darken on hover. Retain a visible keyboard focus ring. |
| Primary action | Solid blue, white label, 6 px radius, minimum 44 px height, 16 px horizontal padding. Use one visually dominant action per section. Use a link for navigation and a button for an action. |
| Secondary action | White background, dark text and control border. Use a subtle neutral hover fill. |
| Sidebar item | Comfortable 44 px row target. Selected item uses pale blue fill, blue text, a 3 px leading indicator and `aria-current="page"`. |
| Page contents | Compact heading links. Current section has a visible marker as well as blue text. Anchor navigation preserves normal browser history. |
| Navigation card | White, 1 px subtle border, 8 px radius and 24 px padding. Include a specific title and short description. Hover changes border colour; no lifting or scaling. Avoid nested interactive elements. |
| Callout | Label, concise text, pale background and 3 px leading rule. Use “Note”, “Example” or “Requirement” according to the content. Requirements still need a source. |
| Status badge | Short text on a light background. Editorial draft is neutral; in review may use amber; published may use neutral or blue. Green is reserved for an actual completed or successful condition. |
| Table | Left-aligned text, subtle header background and row separators; right-align comparable numbers. Include proper headers and a caption where useful. Use local horizontal scrolling for genuinely wide tables. |
| Code block | Neutral surface, monospace text and language label. A copy button confirms “Copied” accessibly and reports failure without losing the code. |
| Disclosure | Labelled button with a direction indicator and expanded state. Use for supporting detail; leave essential instructions visible. |

Interactive components need default, hover, focus and pressed states. Add disabled, loading and error states only where the action requires them. Disabled controls must have an understandable reason nearby; links to unavailable pages should not pretend to be usable.

If search is introduced, provide a visible label, query-preserving results and a helpful no-results state: “No results for ‘…’. Try a stage name or a shorter phrase.” Do not display a search box until search works.

## Diagrams, icons and motion

Use simple line diagrams with dark labels, neutral connectors and blue emphasis for the relationship being explained. Keep text readable without zooming and provide an adjacent explanation. Do not use a different colour for every lifecycle stage.

Use one consistent outline icon family at 20 px, with 16 px icons for compact metadata. Accompany unfamiliar symbols with text. Decorative icons should be ignored by assistive technology.

Keep optional transitions between 120 and 180 ms, limited to colour and opacity. Honour reduced-motion preferences. Avoid animated backgrounds, auto-advancing content and motion that delays access to guidance.

## Accessibility target

Target WCAG 2.2 Level AA. Selected requirements from the [W3C WCAG quick reference](https://www.w3.org/WAI/WCAG22/quickref/) include text contrast of 4.5:1 for normal text and 3:1 for large text; relevant non-text indicators need 3:1 contrast. Support keyboard operation, visible unobscured focus, meaningful headings and text alternatives. Content should reflow at 320 CSS px, with exceptions such as genuinely two-dimensional tables. These checks are a starting point, not a complete conformance assessment.

Additional house implementation choices:

- Prefer 44 × 44 px standalone control targets; retain natural inline text links.
- Use a 2 px blue focus outline with a 2 px white separation so it remains visible beside a blue button.
- Include a skip-to-content link, semantic page landmarks and logical heading levels.
- At 200% text size, preserve content and controls without clipping.
- Ensure print output retains the title, metadata, content and meaningful link destinations while removing navigation.

Verify final foreground/background pairs and all interactive states in the implementation. Passing token contrast checks alone does not establish accessibility.

## Starter implementation tokens

```css
:root {
  --background: #ffffff;
  --surface-subtle: #f8fafc;
  --surface-selected: #eff6ff;
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --border-subtle: #e2e8f0;
  --border-control: #64748b;
  --accent: #1d4ed8;
  --accent-hover: #1e40af;
  --accent-pressed: #1e3a8a;
  --focus: #2563eb;
  --success-text: #166534;
  --success-bg: #f0fdf4;
  --warning-text: #92400e;
  --warning-bg: #fffbeb;
  --danger-text: #991b1b;
  --danger-bg: #fef2f2;
  --font-body: "Segoe UI", system-ui, -apple-system,
    BlinkMacSystemFont, sans-serif;
  --font-code: Consolas, "SFMono-Regular", monospace;
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --radius-control: 0.375rem;
  --radius-panel: 0.5rem;
  --article-width: 47.5rem;
  --site-width: 90rem;
}
```

## Design acceptance checklist

- [ ] White and neutral surfaces dominate; blue consistently identifies interactions and selected context.
- [ ] The home page, one stage page and one long guidance page use the same tokens and hierarchy.
- [ ] Reading width, typography and spacing remain comfortable on desktop and mobile.
- [ ] Keyboard navigation, mobile menu focus and heading anchors work correctly.
- [ ] All visible states meet their applicable contrast requirements.
- [ ] The layout survives narrow screens, text enlargement and long titles.
- [ ] Tables, diagrams and downloads have accessible context and alternatives.
- [ ] There are no placeholder links, decorative controls or unsupported status claims.
- [ ] Approved identity assets and the actual lifecycle terminology replace proposal placeholders before launch.

## Implementation boundary

These standards are independent of the static-site framework and hosting provider. Repository setup and publishing are separate work. The brief names GitLab for the repository and GitHub Pages for hosting; resolve the intended publishing arrangement when implementing the site.
