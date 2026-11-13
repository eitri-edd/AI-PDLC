# Targeted reference fix — issue #81 (13 November 2026)

## Scope

The ArcBeta LLM gateway pricing comparison cited by
`tech-scan-gateway.html` source [11] returns 404 (verified 13 November
2026 by the nightly reference check, and again by direct curl). The
article is also absent from the site's live sitemap and no new slug was
found. This is a targeted replacement, not a new whole-site claim
review. No other reference was re-fetched for this change.

## Changes

- Removed: `https://www.arcbeta.com/Blog/llm-gateway-pricing-litellm-openrouter-portkey-2026`
  — 404 after a 301 to the lowercase path.
- Added (all verified live on 13 November 2026, direct HTTP 200):
  - `https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents`
    — Palo Alto Networks, *Palo Alto Networks Completes Acquisition of
    Portkey to Secure AI Agents*, press release, 29 May 2026. Used in
    `tech-scan-gateway.html` (source-11). Confirms the acquisition
    closed on 29 May 2026 and Portkey became the core AI Gateway for
    Prisma AIRS.
  - `https://docs.litellm.ai/blog/security-update-march-2026`
    — LiteLLM, *Security Update: Suspected Supply Chain Incident*,
    March 2026. Used in `tech-scan-gateway.html` (source-22). Confirms
    malicious PyPI releases `litellm==1.82.7` and `litellm==1.82.8`,
    live on 24 March 2026 for about 40 minutes before PyPI
    quarantined them.
  - `https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain`
    — LiteLLM, *The attack chain behind the v1.107.0 LiteLLM release*,
    root-cause analysis, 23 October 2026. Used in
    `tech-scan-gateway.html` (source-23). Confirms a compromised
    `litellm==1.107.0` was published to PyPI on 21 October 2026 and
    quarantined the same day.
  - `https://openrouter.ai/docs/quickstart`
    — OpenRouter, *Quickstart Guide*. Used in `tech-scan-gateway.html`
    (source-24). Confirms access to hundreds of models through a
    single API endpoint, with automatic fallbacks. The old "380+
    models" figure is dropped: it was already flagged as an unverified
    count and OpenRouter's own docs do not state it.
- The LiteLLM and Portkey capability descriptions are now attributed
  to the VDF comparison [12], which documents the same features
  (MIT core, self-hosting, virtual keys, budgets, routing, guardrails,
  semantic caching). The page's "earlier secondary comparisons" is now
  the singular "earlier secondary comparison".

## Inventory dating note

The four new records carry `checked_on: 2026-11-13` (verified today).
The test suite allows record dates up to the latest page pass
(2026-11-13, `tech-scan-agents.html` and
`tech-scan-workflows-factories.html`). The inventory top-level
`checked_on` stays 2026-11-12; the next nightly run refreshes the
whole inventory. The gateway page's own "References last checked" and
"Last editorial review" dates move to 13 November 2026, and the
pinned tests are updated with them.
