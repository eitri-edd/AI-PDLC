# Tech Scan component-map update — 13 November 2026

## Scope

Targeted diagram update from dev `cc321c6ffd377216a4e694834234225a72b997c8`. Replaces the hub's text-only publication-plan placeholder with a static SVG relationship map inside the existing optional Planned coverage disclosure. It does not implement the broader expert-reader rewrite proposed in issue #66 or publish the future component pages.

## Coverage and meaning

- Wave 1, published: Models, Harness, AI gateway and Sandbox. Each node links to its existing reference.
- Wave 2, planned: Workflows, Factories and Coding agents.
- Wave 3, planned: Context, Verification and Delivery, followed by the Languages and AWS platform cross-cutting views.
- Ten labelled conceptual relationships connect specifications, issue-to-PR coordination, coding agents, the agent loop, context, direct or optionally mediated model access, code execution, verification evidence and release responsibility.
- The two views index all ten component references; they are not additional runtime services. Publication waves are not request order, product maturity or a requirement to deploy every component separately.
- A text equivalent and SVG title/description carry the same meaning. Verification supplies evidence; existing authorised release decisions remain separate.

## Presentation

Uses the site's existing light blueprint vocabulary. Published/planned states are written in each node as well as distinguished visually. No dead links to unpublished pages are introduced. The relationship map opts out of sequence animation with `data-diagram="static"`; the small shared enhancement guard retains native SVG links and avoids misleading playback controls. Existing animated figures are unchanged by that opt-in behaviour.

## Verification

- 89 unit tests passed. The two new diagram contracts were observed failing before their corresponding node/relationship implementations.
- The browser check first rejected the unwanted sequence toolbar, then passed after the static-map enhancement guard.
- Nine negative fixtures rejected missing/incorrect publication coverage, dead planned links, inverted or phantom relationships, missing arrow labels, incomplete cross-cutting membership and removal of the static marker. All failed intentional assertions with no execution errors.
- Five map viewports passed: 1440, 1024, 768, 375 and 320px. Checked node-text/viewBox bounds, connectors avoiding unrelated nodes, native link keyboard focus/navigation, four legacy figure aliases, document overflow, print restoration, no-JavaScript content and script errors.
- All 19 site pages passed a browser smoke check of script errors and animated/static/example control behaviour. JavaScript syntax check passed.
- All 34 original hub IDs survive, with 14 new IDs. External links, dated metadata, the original task-flow figure and the amber disclaimer are unchanged. The other 18 HTML pages are byte-for-byte unchanged.

This is a diagram/relationship review, not a new whole-page reference audit. The existing source-check and editorial dates are retained, and no source-history inventory is rewritten. Browser checks establish rendering and interaction behaviour, not measured human comprehension, cloud deployment or product qualification.
