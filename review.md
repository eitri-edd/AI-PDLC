# Review standard

## Purpose

This document consolidates every assessment requirement used so far to
check the AI-SDLC playbook for content sourcing and evaluation, so that
a future review applies the same rules instead of inventing new ones.

It is a summary of past practice, not a new policy. It does not replace
the authoritative standards. If this file and one of those standards
disagree, follow the standard and correct this file.

## Scope and authority

- **Scope:** all pages in `site/dist/` on the `main` branch of
  `eitri-edd/AI-PDLC`, plus the standards that govern them.
  At the time of writing (14 November 2026, main `eba535b`,
  Merge PR #91) that is 25 pages: the introduction, AI-SDLC overview,
  Concepts, Organisation Transformation, Project Discovery, Product
  Implementation, Training, About, six EDS AI Workflow pages, the
  Tech Scan hub and ten Tech Scan component references.
- **Authoritative writing standard:** `writing.md` (452 lines on main
  `eba535b`). Read it in full before drafting or reviewing. Other
  summaries must not override it.
- **Authoritative presentation standard:** `design.md` (v0.8,
  7 November 2026). Content clarity takes priority over decoration.
- **Curation and maintenance:** `site/dist/about.html` and
  `site/README.md`. Every content change requires human approval
  before it is merged and published; agent checks and scores support
  that decision and do not authorise publication.
- **Reference inventory:** `site/reference-checks.json` (317 unique
  URLs, 323 distinct hrefs at the last recorded census; top-level
  `checked_on` 2026-11-12). Per-source check history lives here,
  not in page text.
- **Status of this file:** draft for review, prepared 14 November 2026
  from main `eba535b`. Proposed location: repository root, beside
  `writing.md` and `design.md`. Proposed standard changes also require
  human approval (see `about.html`).

## Audiences and lenses

Judge a page by the reader it serves, and say which lens was used.

| Pages | Reader | Lens |
| --- | --- | --- |
| Organisation Transformation | Strategic leaders and team leads | Can a leader read a section once and know what to decide, sponsor or change next? Keep it strategic and outcome-focused; link to implementation detail rather than teaching it. |
| Concepts, AI-SDLC overview | Everyone: product, design, engineering, delivery and leadership readers, with no AI experience assumed | Can any reader understand the idea and know where to go next? Explain terms at first use, avoid unexplained role-specific jargon and route role-specific depth to the page that owns it. |
| Project Discovery, Product Implementation | Aspiring product manager who formerly specialised in IT project delivery | Can the reader read a section once and know what to do next? Is it human-centred, or too robotic, too technical, or too abstract? |
| Tech Scan hub and spokes | Experienced development leads and engineers | Factual, industry-standard guidance. Prefer verified developments and their technical implications; do not soften a finding for a general reader. |
| EDS AI Workflow pages | EDS delivery roles using the Eitri workflow | Same lens as Project Discovery and Product Implementation, plus the workflow's own sources and limits. |

Reader assignments for Organisation Transformation, Concepts, the AI-SDLC overview and Tech Scan were set on 14 November 2026 on Christopher's instruction (issue #99).

- **Running example:** Maya's asset-management application.
  Do not use the meeting-room booking example in new or revised
  material. Concepts still uses booking on main; that is a known
  gap, not a precedent.
- **Cloud scope:** AWS only. No Azure, GCP or other cloud platform
  as an option. Vendor SaaS products are products, not cloud platforms.
- **Language:** British English in authored prose (`organisation`,
  `prioritise`, `behaviour`, `programme`). Preserve official product
  names, code identifiers and quoted titles exactly.
- **Dates:** display as `14 November 2026`; store machine-readable
  dates as `2026-11-14`. The target date of a run is that run's
  calendar date in Asia/Singapore. Verify every dated component
  (page fetch, source, issue, PR) matches that target date before
  using it; do not reuse an earlier run's output.

## Content sourcing — rules every review applies

These come from `writing.md`, `about.html` and the Tech Scan
authoring rules. A review checks them on every page it touches.

1. **One final Sources section per sourced page**, headed `Sources`,
   with stable HTML ID `sources`, before the article footer.
   One visible ordered list (`<ol class="source-list">`) for the
   complete listing. No second bibliography, section-ending
   attribution panel, or separate learning-reference list.
2. **One canonical entry per work.** Author or publisher, meaningful
   title, link to the original work, publication date, edition or
   version where it affects interpretation, and the scope, evidence
   limits, adaptation and attribution in that entry, with concise
   links back to the content it supports
   (`Used in <a href="#section-id">Section name</a>.`).
   Do not list the same work twice under a different heading.
3. **One page-wide reference-check date**, in a single paragraph
   immediately after the Sources heading, class `source-check-date`,
   label `References last checked:`. It records the last page-wide
   maintenance pass, not the most recent partial check, edit or
   deployment. If no page-wide check is recorded, say
   `References last checked: not recorded`; do not invent a date.
   Keep individual retrieval and check dates, methods, results and
   unresolved outcomes in `site/reference-checks.json` or the
   relevant maintenance record. Do not repeat `checked`, `accessed`,
   `retrieved` or `referenced on` dates beside individual links,
   source entries or model examples. A date does not imply that
   every claim, inaccessible document or internal implementation
   was verified.
4. **Citations match their entries.** Numbered labels and accessible
   `Source N` labels must match the entry's displayed list number.
   Preserve existing source and learning anchors, including aliases;
   repair every affected citation if display numbers change.
   External URLs appear only inside the Sources list, never in body
   prose (Tech Scan rule); each external URL appears in exactly one
   Sources entry on the page.
5. **A source must support the particular claim.** Check that it
   applies to the activity described. Distinguish a source's
   findings from this guide's interpretation or adaptation, and
   keep a declared adaptation beside the claim it qualifies — a
   declared adaptation is not an error. Keep a consequential caveat
   beside its claim: research population, sample size, limitations,
   applicability and uncertainty affecting the reader's decision.
   Operational links (training entry points, installation links,
   approval requirements, security cautions) stay where readers
   need them; they are not attribution.
6. **No invented facts.** Never invent EDS committees, approval
   gates, job titles, mandatory templates or policy references.
   Never invent claims, numbers, dates or URLs: every factual claim
   and every URL must be traceable to a source. If a claim cannot
   be traced to a source URL, omit it and report it as omitted.
   For performance claims, include the measurement context and
   date. If a result has not been measured, describe the intended
   benefit rather than claiming it has been achieved.
7. **Recheck categorical negatives against current first-party
   documentation.** A product's general availability does not
   establish that every feature is production-ready. An issue
   proposal or a successful HTTP request is not independent support
   for a vendor capability or lifecycle claim.
8. **No prices anywhere** (they move monthly). **No star counts as
   evidence.** No invented short pointer codes for requirements,
   acceptance checks, experiments, evidence or tasks in
   reader-facing content; use descriptive names
   (`writing.md` — "Use descriptive names for references").
9. **Modal language:** use `must` only for a confirmed requirement,
   with a link to its authority and a clear scope; `should` for a
   recommendation, explaining when it may not apply; `can` for a
   capability or option. Write direct imperatives for procedural
   actions. Separate requirements, recommendations and examples so
   a suggestion is never presented as an organisational mandate.
10. **Terms:** explain an unfamiliar or ambiguous term at first use
    and use it consistently. Use `Project Discovery` in full, never
    `Discovery` alone. Keep one term for one concept; where sources
    use the same term differently, choose one term for the guide
    and explain the source mapping. For emerging terms (harness,
    loop, graph and software-factory engineering), explain the
    mechanism, state this guide's usage, give the date or
    attribution where relevant, and cite the source.
11. **Worked examples are fictional and labelled.** Use the shared
    Method first treatment from `design.md` on every page: visible
    `Worked example` label, descriptive method or topic title, and
    a concrete learning benefit for standalone examples and main
    journey chapters. Keep the continuous example coherent across
    chapters; keep topic explanations (blue diagrams) and fictional
    applications (lavender panels) in separate visuals.
12. **Measurement is taught with a complete record.** What counts,
    who or what is included, the observation period, the baseline
    and its source, the target and review date, how the result is
    collected and checked, who owns it, applicable guardrails, and
    what meeting, missing or breaching a criterion would change.
    Show the calculation and keep the denominator visible. Do not
    invent a historical baseline for a new service. Distinguish
    zero from an unobserved or undefined measure. Keep observed
    findings, targets and hypothetical future results distinguishable.

## Evaluation — the eight assessments

Apply the assessment that fits the question. Do not mix scales:
a readability score, a factual score, a terminology score and a
criticality score measure different things and are not interchangeable.

### 1. Peer review (standing, `about.html`)

- **Method:** separate reviewer agents examine existing articles
  paragraph by paragraph. Each paragraph receives a score from
  1 to 10 for each of three qualities: how natural it sounds, how
  easy it is to understand, and how accurately it represents the
  evidence. Higher is stronger.
- **Output:** issues that identify the passage, explain the problem
  and propose an improvement. Scores direct attention; the
  explanation and source evidence give the writer something
  concrete to assess.
- **Limit:** an agent's readability score does not establish that a
  reader has understood the article.

### 2. Readability assessment (daily, 04:00 Singapore)

- **Pages:** six — Concepts (`concept.html`, singular;
  `concepts.html` returns a 404), Organisation Transformation,
  AI-SDLC overview, Project Discovery, Product Implementation,
  Tech Scan hub only (spokes not covered).
- **Lens:** the reader for each page in "Audiences and lenses":
  strategic leaders and team leads for Organisation Transformation;
  everyone for Concepts and the AI-SDLC overview; aspiring product
  manager, formerly IT project delivery, for Project Discovery and
  Product Implementation; experienced development leads and
  engineers for the Tech Scan hub.
- **Method:** read each page live, in full, paragraph by paragraph.
  Score each section 1–10, where 10 means the reader can read it
  once and know what to do next, and below 4 means it needs an
  expert to translate it and is unsuitable as core reading. Judge
  whether the page is too robotic / not human-centred, too technical,
  or too abstract.
- **Baseline:** compare against
  `hidden_files/readability-baseline-2026-11-08.md` (line count,
  wording, sections, worked example, running example). If a page
  is unchanged, file nothing for it, even if it still has sections
  below 4 — the open issue already covers them.
- **Filing rule:** if a page changed, re-score it fully. File a new
  issue for that page only if the new assessment differs materially
  (a section moved above or below 4, a score changed by 2 or more,
  a new below-4 section appeared, or the previous readability issue
  for that page is now closed) **and** it scores Medium or High on
  the three-metric criticality scale (§9). At most one new issue
  per page per run. Check open issues first so nothing is re-filed
  while an equivalent issue is open.
- **Provenance:** set up 8 November 2026; issues #29–#33, #35, #47,
  #48, #50. Re-filing for the Medium findings in closed #47
  (Concepts) and #48 (Transformation) stays paused until
  Christopher confirms otherwise.

### 3. Reference check (daily, 21:00 Singapore)

- **Method:** start from a fresh `main` clone or fetch every run;
  record the main HEAD SHA first. Base all reads — inventory,
  pages, source comparisons — on that fresh copy. Never start from
  `dev`, a stale copy, or a previous run's output.
- **Scope:** every entry in `site/reference-checks.json`
  `references`, plus every external href in all `site/dist/*.html`
  pages (25 pages on current main). Reconcile the two: a page href
  not in the inventory is still checked and, if valid, added as a
  new entry; an inventory URL no longer cited is noted in the
  report, not silently deleted. Count distinct URLs after stripping
  `#` fragments.
- **Per-source checks:** (a) valid link — fetch the URL (direct HTTP
  and, where needed, a web reader). Valid means it returns a
  readable source (HTTP 200 or equivalent), not a 404, error page,
  placeholder or dead redirect. Follow redirects and record the
  final destination; a redirect to a different work than the one
  cited is a failure, not a pass. (b) factual quoting — for each
  page's Sources section, check every claim, number, date, finding
  and attribution that cites a source against the retrieved source
  text. It must match the source. Respect declared adaptations.
  A source that cannot be retrieved, a claim the source does not
  support, or a quote that misstates the source is a failure.
- **Result vocabulary:** use the inventory's existing results —
  `retrieved` means a readable source was returned, not blanket
  verification of every claim in the source; other recorded results
  include `dynamic_page_no_text` and `verification_challenge`.
  Record per URL: HTTP status, page title, method, result.
- **If all valid:** update `checked_on` (top level and every entry
  checked and passed) to the run date, update the `scope` sentence
  and `counts` to this run's results, update the
  `References checked on …` / `References last checked: …` date
  (text and `<time datetime>` together) on the pages that carry one,
  validate JSON, run the repo tests, commit to `dev` and open one
  PR `dev` → `main` for approval. Never commit to `main` or merge.
  If the dates already equal today and nothing else changed, commit
  nothing and open no PR.
- **If anything fails:** update no dates anywhere — a failed night
  leaves the old dates standing so nobody mistakes an unchecked day
  for a checked one. Record every failure precisely (URL, citing
  page(s), what was expected, what was found). Check open issues
  for duplicates, then file at most one issue listing all of the
  night's failures. No commit and no PR that night.
- **Known lesson:** the first all-clear (9 November 2026) was wrong
  because it trusted a cached reader copy and missed a dead AWS
  outbox link. Verify links live; a search result or a cached copy
  does not establish that a link is live.
- **Provenance:** set up 9 November 2026; issues #44, #45 (fix),
  #81 (ArcBeta 404, fixed by PR #82). The six-page wording in the
  job's scope section stays exactly as it is, per Christopher's
  11 November decision ("Leave it as is") — do not re-apply the
  13-page fix without him asking.

### 4. Weekly research enrichment (Saturday, 09:00 Singapore)

- **Method:** research AI-SDLC and product-management best
  practice from the past 7 days (older only if it is a landmark
  guide the playbook clearly lacks). Prefer primary sources —
  engineering blogs, DORA / McKinsey / Martin Fowler / Defence
  Product Playbook, vendor release notes, academic papers — over
  roundups. Record title, author, publication date and URL for
  every candidate. Separate validated outcomes from practitioner
  opinion and vendor roadmap claims. Read the playbook and
  `writing.md` from `main` first; check open issues and open PRs
  and the seen-findings log so nothing is duplicated.
- **Scoring:** score every candidate 1–5 on each of three metrics
  (see §9). Criticality is the sum (3–15).
- **Action by level:** High (12–15) — implement the change on
  `dev`, then raise the issue and a PR `dev` → `main`; this is the
  only level that gets an edit, a commit and a PR. Medium (8–11)
  with loss-if-missed ≥ 4 — file the issue only, no edit, commit
  or PR. Medium with loss < 4, and Low (3–7) — file nothing,
  implement nothing. Take the single highest-scoring qualifying
  finding only; list other qualifying findings in the issue's
  `Other candidates considered` section.
- **Implementing a High finding:** minimal, focused edit to the
  page source under `site/dist/`; review and refine it against
  `writing.md` (including its Editorial acceptance checklist) and
  `design.md` before committing. Base on `main`, apply to `dev`'s
  current version (never reset `dev` to `main`, never commit to
  `main`), verify the edit by reading it back from `dev`. Record
  what was checked and what was **not** checked (rendered preview
  and a representative-reader task are unverified unless actually
  done). Raise the issue before committing, so the commit and PR
  can reference its number.
- **Provenance:** authorised 6 November 2026, at most one finding
  per run, documentation only, in `eitri-edd/AI-PDLC` only.
  Issue #85 / PR #87 (Fowler, "Tests as data", 14 November 2026)
  is the most recent High finding implemented.

### 5. Terminology review (ad hoc; last run 10 November 2026)

- **Method:** extract every distinctive, coined or load-bearing
  term (search for `*-engineering`, `*-Ops`, framework and model
  names, capitalised multi-word phrases, tool and method names).
  Check each against independent online use — standards bodies,
  vendor documentation, academic papers, widely used glossaries —
  not against the playbook itself. Terms that appear only as
  ordinary words are not scored.
- **Scale (1–5):** 5 established industry-standard term, widespread
  independent use; 4 recognised but niche, vendor-specific or
  young, with real independent use; 3 emerging or contested, used
  by only a few sources, or defined differently by different
  sources; 2 largely coined by this playbook or by one
  organisation, with no meaningful independent use; 1 misleading —
  conflicts with an established meaning, or presented as fact when
  the source says something different.
- **Threshold:** flag every term below 3. Propose a rename, a
  definition on first use, or attribution — usually a one-line fix,
  not a rewrite. Watch in particular for collisions with unrelated
  products or meanings (for example `Eitri`, `inner loop`,
  `guardrails`).
- **Counting care:** re-check counts case-sensitively; a
  case-insensitive search overstated CLARA (matching
  "declaration") and RAG (matching "encourage") in the 10 November
  run.
- **Provenance:** 10 November 2026, main `a9bc489`, all 14 pages
  then in `site/dist/`; 48 terms scored (15×5, 13×4, 9×3, 11×2,
  0×1); 11 below 3. Filed as issue #49 — do not re-file it.

### 6. Tech Scan factual review (ad hoc, per wave)

- **Method:** score every substantive paragraph, list item, table
  row or cell, figure caption and diagram text-equivalent 1–10
  for **factual correctness only**: 10 fully correct or verifiable;
  5 half-right, misleading or unverifiable; 1 false. Live-check
  every below-5 candidate and every doubted date, version or
  number against vendor or official sources.
- **Threshold:** flag items below 5 as must-fix before publication;
  list borderline 5–6 items as fix-or-soften; record cross-page
  inconsistencies separately (the same error stated twice counts
  twice, once per page).
- **Before filing:** re-check every item against the current `dev`
  head — in the 12 November run, 15 of 21 below-5 items were already
  fixed by newer refinement commits, so only the 6 survivors plus
  3 new items were filed.
- **Provenance:** 12 November 2026, dev `4e43801`, five Tech Scan
  pages; 288 units scored, 21 below 5 (20 distinct errors), no 1s.
  Filed as issue #62 — do not re-file it. Wave 2 and Wave 3
  critical reviews (13 November 2026) add: judge ease of flow,
  factual technical terms, additional information that fits gaps,
  and redundant information, for experienced development leads and
  engineers.

### 7. Whole-playbook critical review (ad hoc; last run 14 November 2026)

- **Method:** read the whole site in full from a fresh `main`
  clone — every page plus `writing.md` — in reading order, not
  nav order. Check every cross-page anchor resolves. Every
  material claim carries a `file:line` reference; "zero hits"
  means a grep across the stated files returned nothing.
- **Dimensions, scored 1–5** (5 exemplary; 4 good with minor gaps;
  3 workable but material gaps; 2 weak; 1 broken or misleading):
  (1) Flow — does the reading order make sense? (2) Concepts →
  Tech Scan — does Tech Scan deliver what Concepts requires?
  (3) Areas to improve, in priority order (P0/P1/P2).
  (4) Conciseness — what can be cut, especially in Tech Scan?
- **Concepts → Tech Scan matrix:** list each Concepts requirement,
  its verdict (covered / thin / missing), the Tech Scan coverage,
  and the gap. On 14 November 2026: 14 requirements, 2 covered,
  9 thin, 3 missing (skill versions, protected-rule guardrails,
  EDS workflow).
- **Conciseness check:** look for repetition across pages (same
  warning on many pages, a hub map shown several times), toolkit
  and example material that roughly doubles a page, and overview
  detail that belongs in a Concepts or EDS page.
- **Provenance:** 14 November 2026, main `a0069e14`, 16 pages +
  `writing.md`; all four dimensions 2/5, overall 2/5. Filed as
  issue #84 — do not re-file it. Two corrections from that run
  stand: Jev Box **is** covered (do not repeat "No Box anywhere");
  Harness and Sandbox **do** have do-not-use/gaps sections — only
  Context, Verification, Delivery and Stack views lack them.

### 8. Styling-drift audit against `design.md` (ad hoc; last run 12 November 2026)

- **Method:** read every page in `site/dist/` plus the shared and
  per-page stylesheets and `site.js` directly from a fresh `main`
  clone. Direct file reads and grep/regex counts; no cached or web
  copies. Check tokens value-for-value against `design.md`.
- **Criticality scale (1–5):** 1 cosmetic or minor inconsistency,
  barely visible; 2 noticeable inconsistency, low impact on
  reading; 3 clear drift from the design system, breaks consistency
  across pages; 4 significant violation, impairs readability,
  usability or a core component; 5 critical, breaks accessibility,
  the core template, or misleads.
- **Limit:** responsive behaviour at specific widths was verified
  from CSS only, not rendered in a browser — record that limit.
  State what static checks cannot verify.
- **Provenance:** 12 November 2026, main `ee8ebb9`; 29 findings
  (0×5, 0×4, 6×3, 10×2, 13×1); no page fully conforming. Filed as
  issue #58 — do not re-file it.

## The three-metric criticality scale (shared)

Used by the readability filing rule (§2) and the weekly enrichment
run (§4). Score each candidate 1–5 on each metric; criticality is
the sum (3–15). High 12–15, Medium 8–11, Low 3–7. Show all three
scores, the total and the level, with one line of justification
per score.

| Metric | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Novelty — is it new information readers should know? | Already covered in the playbook | A useful update or sharper framing of something covered | Entirely new, timely practice readers would otherwise miss |
| Enrichment / gap coverage — does it enrich the write-up or cover a gap? | No fit, or duplicates an existing section | Strengthens an existing section with a concrete technique or example | Directly fills a clear gap or fixes a weak section |
| Loss if missed — if the reader never learns this, how big is the loss? | Trivial, nice-to-know | A missed improvement or avoidable rework | Material risk, costly mistake, security / quality / value failure, or a major missed opportunity |

## Evidence and reporting rules (all assessments)

1. **Start from `main`, fresh.** Clone or fetch `main` fresh and
   record the HEAD SHA before doing any checking. Base all reads
   on that copy. Never base a finding on `dev`, a stale copy, a
   cached reader copy, or a previous run's output. A branch-scoped
   read that returns another branch's history must be cross-checked
   against a fresh fetch before it is trusted.
2. **Quote or link the affected passage.** Give `file:line`
   references, and quote the passage where the finding turns on
   its wording. Separate observed problems, interpretations and
   proposed changes. A score alone does not establish comprehension
   or a defect.
3. **Verify live, against the primary source.** Prefer first-party
   vendor documentation, standards bodies and academic papers.
   For changing product capabilities, recheck categorical negatives
   against current first-party documentation. Record source title,
   author, publication date and URL for every candidate finding.
4. **Re-check against the current `dev` head before filing.**
   Do not file items already fixed by newer commits.
5. **Check open issues and open PRs before filing.** Search and
   list open issues in `eitri-edd/AI-PDLC`; do not duplicate an
   open issue or PR. Verify a filing afterwards with `list_issues`,
   not `get_issue`. File with `"method": "create"`.
6. **Record what was checked and what was not.** Distinguish
   author reread (assesses the explanation), markup and link checks
   (assess structure), browser checks (assess behaviour and layouts
   exercised), and a reader session (supplies evidence of
   comprehension). Identify skipped checks and remaining limits.
   A browser may repair malformed HTML, so a readable rendering
   does not establish valid source structure.
7. **Reader-task review, for a substantial learning change.**
   Define the reader action the edit should improve before
   rewriting. After the change, use a short task with an expected
   answer — can the reader identify who acts, what they compare,
   the evidence they retain and the next decision? — rather than
   asking only whether the page is clear. For new or substantially
   changed teaching, ask a representative reader with the stated
   prerequisites to attempt the intended task without corrective
   coaching; record their answer, hesitation, assistance and
   consequential misunderstandings, revise, and repeat. If that
   session has not happened, retain the prompts and report
   comprehension as unverified. An agent's successful answer is
   not a substitute for observed reader results.
8. **Do not claim what was not done.** Never claim an issue was
   filed, a commit landed, or a PR was opened while it is still
   waiting on approval. Log the exact partial state (what was
   filed / committed / opened and what was not) and include the
   full draft so the work can be completed manually.
9. **Keep the record durable.** Save full drafts, file contents and
   commit SHAs under `~/workspace/goals/ai-pdlc-daily-research-enrichment/`,
   never only in `/tmp`. Record run notes in `~/memory/YYYY-MM-DD.md`.

## Acceptance gates before a change is accepted

A change is not editorially complete until these have been run
for the pages it touches. Mark an item only after verification.

1. **`writing.md` Editorial acceptance checklist** (30 items at the
   end of `writing.md`): one final Sources section, one list, one
   page-level check date; teaching chapters distinguish general
   guidance, continuous case and reference material; opening tells
   the reader what the page helps them do; terms explained and
   consistent; instructions identify actions, outputs and ownership;
   `check / review / validate / ensure` followed by enough detail
   to perform the work; observations, interpretations and untested
   explanations kept separate; decision examples show a completed
   record and its consequence; reorganised content retains usable
   anchors and correct attribution; requirements cite a confirmed
   authority; examples contain no invented organisational facts.
   Do not mark a procedure or review activity complete while
   readers still have to invent the checking method or infer what
   to record.
2. **`design.md` Design acceptance checklist** (13 items): blue
   theme for topic explanations, shared lavender Method first
   treatment for worked examples with visible label and learning
   benefit, page maps link to their destinations, diagrams have
   text equivalents and descriptive labels, reading remains legible
   on desktop, tablet, mobile and enlarged text, motion serves
   explanation and honours reduced motion, examples remain
   distinguishable without colour, without JavaScript and in print.
   Accessibility target: WCAG 2.2 Level AA (4.5:1 normal text,
   3:1 large text and non-text indicators).
3. **Repo tests:** `python3 -m unittest discover -s tests -v`
   from the repository root. The source-list regression checks
   cover the single heading/list/date, citation numbering,
   duplicate IDs and local fragments; also compare changed source
   URLs and anchors with the previous revision. On main `eba535b`,
   144 tests pass. Inspect the rendered Sources section and moved
   citation destinations on desktop and mobile.
4. **Coherence reread:** after every edit, reread the affected
   passage and its surrounding text; scale the wider review to the
   change. Check the page opening, headings, next step and
   dependent linked guidance. Repair references and transitions
   after shortening or moving text. Confirm captions, source notes
   and directly linked sections still give readers enough context.
5. **Reader evidence:** see §"Evidence and reporting rules", item 7.
   Report comprehension as unverified unless a representative-reader
   task has actually been observed.

## Governance — filing, branching and approval

- **Human approval for every content change.** A human reviews the
  change and its evidence, requests revisions where needed, and
  decides whether to approve it. Only an approved change is merged
  and published. Proposed standard changes also require human
  approval.
- **Branches:** work on `dev`; publish via a PR `dev` → `main`
  for approval. Never commit to `main`, never merge a PR yourself,
  never reset `dev` to `main` (that would lose unmerged work).
  The one recorded exception is the Tech Scan sub-nav removal on
  14 November 2026, committed directly to `main` as `7a26e0c` on
  Christopher's explicit instruction — an exception, not a standing
  change. The published site serves `main` only; `dev` is a public
  preview under `/dev/`, not a private environment.
- **GitHub writes are fresh-consent only.** Each filing, commit and
  PR raises one system approval card; the run must wait for it.
  Cards expire (about 30 minutes has been observed). Do not bypass
  the safeguard with a direct API or token route.
- **Filing limits:** at most one new issue per page per run
  (readability), at most one finding per run (weekly enrichment),
  at most one issue listing all of a night's failures (reference
  check). A re-assessment is a new issue titled
  `Re-check … readability after the update`, not a duplicate of the
  closed one.
- **Do not re-file** issues #31, #32, #33, #35, #47, #48, #49, #50,
  #54, #58, #59, #62, #64, #65, #66, #75, #76, #81, #84, #85
  without checking open issues first and, for #47/#48, without
  Christopher's go-ahead. Closed Medium findings are preserved in
  their closed issue for future review when the page is next
  revised; closing them does not authorise automatic re-filing.

## Maintaining this standard

- Update this file when a new assessment type is introduced, a
  scale or threshold changes, or a past rule is corrected by a
  later decision. Record the date, the main HEAD it was checked
  against, and the issue or decision that changed it.
- When a review corrects content, consider whether the standards
  also need refinement — and file that as a separate proposal,
  not as a side effect of the content fix.
- Known open questions at the time of writing: any PRs still awaiting
  review (check the open PR list before acting — PR #80, Grok Bot in
  the About diagram, was open on 14 November 2026); the P2 findings from the Wave 2 review; the Wave 3 items
  flagged unverified for re-check after re:Invent (sessions
  30 November – 4 December 2026); the Product Implementation
  readability draft that was never filed after two timed-out
  approval cards (retry only on Christopher's go-ahead).

## Sources

References last checked: not recorded.

1. `writing.md` — authoritative writing standard, main `eba535b`.
2. `design.md` — design system proposal v0.8, 7 November 2026.
3. `site/README.md` — site structure, deployment (`main` → production, `dev` → `/dev/`), and local verification.
4. `site/dist/about.html` — curation loop, shared standards, reference maintenance, peer review.
5. `site/reference-checks.json` — reference inventory, per-source check history and evidence policy.
6. Daily readability baseline, `~/workspace/goals/ai-pdlc-daily-research-enrichment/hidden_files/readability-baseline-2026-11-08.md` (last updated 14 November 2026).
7. Daily readability, reference-check and weekly enrichment job definitions, `~/workspace/goals/ai-pdlc-daily-research-enrichment/crons/`.
8. Term review, 10 November 2026 — issue #49.
9. Tech Scan factual review, 12 November 2026 — issue #62.
10. Styling-drift audit, 12 November 2026 — issue #58.
11. Whole-playbook critical review, 14 November 2026 — issue #84.
12. Tech Scan authoring rules, Wave 1, 12 November 2026.
