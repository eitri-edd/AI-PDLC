# Tech Scan critical gaps for issues #65, #75, #76 — implementation review, 14 November 2026

- **Base:** dev HEAD `1f6023d` (main content identical for the Tech Scan pages; main HEAD `a0069e14`).
- **Scope:** critical gaps only, per the closeout reviews
  `files/tech-scan-issues-64-65-66-75-76-closeout-review-2026-11-13.md` and
  `...-2026-11-14.md`. Issues #64 and #66 were not touched. No issue was closed.
- **Rebuild note:** a first implementation (local commit `2414a8b`, 14 Nov 00:47 SGT)
  was never pushed — its approval card timed out — and was lost when /tmp was
  wiped on a VM replacement. This rebuild re-verified every claim against its
  live primary source; the verification notes per issue are in
  `hidden_files/gaps-rebuild-2026-11-14/{65,75,76}-verification.md`, the
  patches in `{65,75,76}-patch.diff`, and a backup of every changed file plus
  the snapshot manifest in the same directory.
- **writing.md:** the copy in the repo is 452 lines at dev HEAD (SHA `b9055ba0`).
  The "883 lines (SHA 77bf9da1)" figure in older notes is stale: blob `77bf9da1`
  is writing.md as of 7 Nov and is 417 lines.
- **Tests:** 144 tests pass (132 baseline + 12 new/changed assertions).
- **Inventory:** `site/reference-checks.json` 278 → 317 records
  (39 new, all `retrieved`, HTTP 200, checked 2026-11-14; `current_unique_urls`
  317, `current_unique_hrefs` 323, `counts.retrieved` 295). The Zep Community
  Edition URL already had a record (harness.html); it was extended to
  context.html rather than duplicated.
- **Page-level dates unchanged:** writing.md updates "References last checked"
  only after a documented page-wide pass; this is a partial edit. Agents stays
  13 November 2026; the four Wave 3 pages stay 14 November 2026. Page passes
  in the inventory are likewise unchanged (pass-time snapshots).

## #65 — Agents (`site/dist/tech-scan-agents.html`, sources 21 → 31)

- `enforceAvailableModels` / `availableModels` paragraph in #routes, cited to
  the Claude Code settings reference: the allowlist alone does not constrain
  the `/model` Default option; `enforceAvailableModels: true` (v2.1.175+)
  closes it; Bedrock Invoke API startup checks honour the list only in
  managed settings (v2.1.287+); `availableModelsMatch` / `deniedModels`
  (v2.1.283+, managed settings only).
- AgentCorruption / default execution role in #controls: per-agent
  least-privilege roles; never ship on a CLI-created or default role; default
  role narrowed by 29 Sep 2026; MMDSv2 mandatory since 30 Jun 2026;
  169.254.169.254 egress blocking as defence in depth. The "never use the
  default role" rule is labelled this guide's own prescription, not an AWS
  quotation; AWS's "documented and expected behaviour" position is stated.
- Five further 2026 reports: Copilot CVE-2026-103572 (fixed 13 Oct 2026, VS
  2022 17.14.42 / VS 2026 18.10.4; Microsoft names no fixed SSMS build),
  Kiro CLI CVE-2026-9255 (AWS bulletin 2026-035-AWS, 22 May 2026; CVSS 4.0
  8.4 / 3.1 7.8; fixed in 1.28.0), Miasma/testmetest (SafeDep, 9 Nov 2026,
  12 repos — not 42), Postman Desktop 12.33.4 auto-install (GitHub issue
  #14370; no exfiltration claimed), EMBRACE (Forever Security, 29 Oct 2026;
  Cursor patched silently 1 Oct, Copilot fixed 1.1.29 on 13 Oct, Codex/VS
  Code unpatched at publication; Claude Desktop fix status not asserted).
  Neither CVE is a November disclosure; the page states the real dates.
- Caveats: MSRC itself was not directly readable for CVE-2026-103572 (404/429
  via the reader); the fixed builds rest on two independent MSRC-citing
  secondaries. The Postman revert statement is secondary-reported only.
  One secondary misattributes CVE-2026-10591's scores (4.0 8.6 / 3.1 8.8) to
  CVE-2026-9255; the page uses the correct 4.0 8.4 / 3.1 7.8.
- Open questions in #gaps: pre-29-Sep-2026 default roles retroactively
  narrowed (AWS unstated); Postman revert scope; EMBRACE fix status for
  Codex/VS Code/Claude Desktop; fixed SSMS build for CVE-2026-103572.

## #75 — Context + Verification

### Context (`site/dist/tech-scan-context.html`, sources 8 → 16)

- Kendra closure verified against the primary AWS notice (Kendra
  availability-change docs page + AWS Service Availability Updates):
  Maintenance Mode 30 Jun 2026, closed to new customers 30 Jul 2026,
  existing deployments keep running; new work starts at Bedrock Managed
  Knowledge Bases.
- Managed-KB defaults: service-managed reranker by default, 5 results by
  default, `Retrieve` vs `RetrieveAndGenerate`, chunking unchangeable
  afterwards, semantic chunking not supported for managed KBs. Managed KB GA
  date (reported 17 Jun 2026) was not primary-verified and is left dateless.
- Vector-store table (decision-guide table): OpenSearch Serverless,
  S3 Vectors, Aurora pgvector, DynamoDB — DynamoDB is **not** a Knowledge
  Bases backend, verified against the primary decision-guide table.
  S3 Vectors distance metrics (`euclidean | cosine`) and Aurora pgvector
  0.8.2 on 18.6 verified against the API reference / release notes.
- Do-not-use + gaps sections added (body only — see the navigation note
  below). Context do-not-use: Kendra, Bedrock Agents Classic, Zep Community
  Edition, shared actor-less namespace, unvetted MCP server, prompt-as-boundary.

### Verification (`site/dist/tech-scan-verification.html`, sources 6 → 10)

- CodeGuru: Security end of support 20 Nov 2025, Reviewer maintenance since
  7 Nov 2025; Q Developer for review and Inspector for scanning are the
  named replacements. The dedicated CodeGuru Security EOS doc page is gone
  (live HTTP 404 on 14 Nov 2026); the page cites the AWS SDK for Java API
  reference, which carries the EOS notice verbatim, and the Reviewer
  availability-change page. AWS Security Agent was **not** named as a
  successor on either notice and is not presented as one.
- "No managed AWS service evaluates code correctness" is stated plainly,
  with the CI + rulesets + mutation-testing route. AgentCore Evaluations has
  15 built-in evaluators (AWS ML Blog, 10 Nov 2026); the older README's 13
  is recorded in gaps.
- Automated Reasoning limits added (detect mode only, no prompt-injection
  protection, no streaming, English (US) only). Do-not-use + gaps sections
  added (body only).

## #76 — Delivery + Languages/AWS platform views

### Delivery (`site/dist/tech-scan-delivery.html`, sources 4 → 14)

- ECS-native blue/green is "now the recommended option for most teams and
  new projects" (AWS DevOps Blog, 11 Feb 2026; built in Jul 2025,
  canary/linear Oct 2025). **AWS does not call CodeDeploy "legacy"** — the
  issue's wording is corrected; CodeDeploy "remains a valid option for
  existing customers". The word "legacy" appears nowhere on the page
  (test-enforced).
- Deployment-target table (ECS/EKS/Lambda/EC2); CodePipeline V2 paragraph
  (stage conditions, stage rollback, entry conditions with Skip, automatic
  retry are V2-only — verified against the AWS pipeline-types doc).
  "V1 frozen" and "new pipelines default to V2" are **not** AWS statements
  and are left as a gaps open question.
- X-Ray SDK maintenance date **25 Feb 2026 verified** against the AWS
  migration guide (direct page read, 14 Nov 2026): "On February 25th, 2026,
  the AWS X-Ray SDKs/Daemon will enter maintenance mode". No Feb 2027 EOS
  date is asserted.
- Incident Manager closed to new customers 7 Nov 2025, new accounts pointed
  at OpsCenter (verified against the AWS page). OpsCenter composition
  verified against the AWS doc: CloudWatch alarm / EventBridge event
  auto-creates an OpsItem; SNS is the notification leg, not an
  OpsItem-creation hop. Evidently support ended 17 Oct 2025, AppConfig
  recommended (verified against the AWS blog).
- DORA: five metrics (dora.dev, last updated 5 Jan 2026); AWS computes none;
  the published route is an Argo → DevLake → Grafana blueprint, not a
  managed service. Do-not-use + gaps sections added (body only).

### Stack views (`site/dist/tech-scan-stack-views.html`, sources 3 → 11)

- Python/TypeScript-only agent-SDK paragraph: Strands, Claude Agent SDK
  (current name — "Claude Code SDK" was renamed 29 Sep 2025), OpenAI Agents
  SDK; Java route is AWS SDK for Java v2 + community LangChain4j
  (Apache-2.0, confirmed via the project repo). The Claude "Python and
  TypeScript only" wording rests on the worker's snippet verification; the
  directly fetched overview page confirms "programmable in Python and
  TypeScript".
- Singapore model/region paragraph: Claude Sonnet 5 in-region since 29 Sep
  2026; Opus 5 named for Seoul only; GPT-6 via Global profiles only on the
  Bedrock Runtime endpoint (Global profiles route worldwide, not a residency
  boundary); AgentCore Harness GA in Singapore (GA 17 Jun 2026 in all
  commercial regions where AgentCore is available). Harness GA is stated
  once on the page (test-enforced). Nitro Sandboxes cross-link added.
- Do-not-use + gaps sections added (body only).

## Integration corrections (coordinator)

- **Navigation cap kept at 5.** The #75/#76 workers added do-not-use and
  gaps links to the "On this page" navs (7 links) and raised the test cap.
  The repo's compact-navigation contract caps that nav at 5 links (PR #83,
  enforced by tests). The Wave 1 pages fit do-not-use/gaps into the nav
  only because they have two content sections; Workflows and Agents (four
  content sections) carry those sections in the body only. The four Wave 3
  pages now follow the Workflows/Agents precedent: sections in the body,
  navs back to 5 links, test caps restored. Stack views already had 5 nav
  links (two content sections) and was left unchanged. The Delivery
  page-map figure (which links the new sections) is a figure, not a nav,
  and was kept.
- **Strands quickstart URL fixed.** The #76 worker cited
  `strandsagents.com/docs/user-guide/quickstart/overview/`, which returns a
  live HTTP 404. The page now cites
  `strandsagents.com/docs/user-guide/quickstart/` (live HTTP 200; the cited
  "available in both Python and TypeScript" sentence verified on the page).
- **Zep deduplication.** The Zep Community Edition URL already had an
  inventory record (harness.html); the record was extended to context.html
  instead of adding a duplicate.
- **Inventory re-dump.** The first dump used ASCII-escaped JSON and produced
  a 1,345-line diff; re-dumped with `ensure_ascii=False`, indent 2, matching
  the file's existing style: 1,146 insertions / 4 deletions.
- **Still unverified (in gaps, not asserted):** Kiro Web GA date/region,
  Copilot Approve GA/toggles, Chroma Cloud wind-down dates, AgentCore
  Evaluations/Inspector/Security Agent GA dates and regions, most
  open-source version numbers, Managed KB GA date, CodePipeline V1 freeze,
  Evidently/AppConfig experimentation GA date, Bedrock PrivateLink in
  ap-southeast-1, Go SDK v2 Bedrock client, LlamaIndex.TS deprecation,
  GPT-6 profile IDs (confirm on the model card before building).
