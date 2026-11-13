# Tech Scan Wave 2 — critical review (developer/architect audience)

Date: 13 November 2026. Reviewer: 小强.
Scope: main at `bda3db3` (Merge PR #74, "docs: integrate Wave 2 Tech Scan and simplify navigation",
merged 13 Nov 2026 16:45 SGT — so Wave 2 is live on the published site, not only on dev).
Files: new `site/dist/tech-scan-agents.html` (119 lines) and
`site/dist/tech-scan-workflows-factories.html` (107 lines); hub `site/dist/tech-scan.html`;
Wave 1 spokes (Models, Harness, AI gateway, Sandbox) as changed by the same PR.
Compared against: issues #64 / #65 and the full Wave 2 record
(`files/draft-issue-wave2-full-2026-11-12.md`, ~97k chars), the PR's own source review
(`site/tech-scan-wave2-review-2026-11-13.md`), and live primary sources re-checked 13 Nov 2026
(Anthropic Claude Code on Bedrock, OpenAI on Bedrock, `claude-code-action/action.yml`,
Kiro available-models, Zed AI Quick Start, Spec Kit quickstart).
Tests: all 48 `test_tech_scan*.py` tests pass on main HEAD.

## Verdict

Accurate where it speaks, but thin — and the PR introduced two navigation defects.
The conservative choice (publish only what was re-verified on 13 Nov) is sound, and the
source-verification document is unusually thorough. But it silently dropped several
findings from #64/#65 that were already verified live on 12 Nov, so a developer reading
only the published pages can still pick a dead product, miss the only managed factory
option, or misconfigure the Bedrock route. The two new pages also break the spoke pattern
every Wave 1 page follows: neither has a do-not-use or gaps section.

Nothing here was filed or edited. This is a review only.

## P0 — defects introduced by PR #74 (fix first, small and safe)

### 1. Gateway and Sandbox pages omit themselves from the sidebar navigation
- `tech-scan-gateway.html:34`: the nav-children list is Models, Harness, Agents, Workflows.
  There is no link to the Gateway page itself, and `aria-current="location"` sits on the
  **Models** link. A screen reader announces Models as current while the reader is on Gateway.
- `tech-scan-sandbox.html:35`: same shape — Sandbox itself is missing from the list, and
  `aria-current="location"` sits on the **Harness** link.
- Models, Harness, Agents and Workflows & factories mark themselves correctly with
  `aria-current="page"`. So this is not a convention difference; two files were hand-edited
  wrong (note also the 24-space indent on the Models line in both files, vs 12 elsewhere).
- Fix: restore the self link in both files, mark it `aria-current="page"`, remove the
  misplaced `aria-current="location"`, and normalise the indent. Add a test asserting every
  Tech Scan page's nav lists all six spokes with exactly one current marker on itself.

### 2. "On this page" tables of contents now orphan live sections
The PR trimmed the TOC (both the mobile `<details>` and the aside) on the hub and on all
four Wave 1 spokes, but left the sections in the body:
- Hub: Planned coverage (`#planned-spokes`), Shared interfaces (`#cross-cutting-views`),
  Limits before adoption (`#gaps`), Other delivery responsibilities (`#layer-map`) are no
  longer in the TOC.
- Models / Harness / Gateway / Sandbox: `#do-not-use` and `#gaps` are no longer in the TOC —
  on every spoke, the two sections a developer most needs before adoption (what is excluded,
  what is still unknown).
- The new pages' own TOCs are complete, so this is confined to the hub + Wave 1 spokes.
- Fix: restore the removed TOC entries. If the intent was a shorter TOC, collapse the
  lower sections under one entry rather than deleting their links; do not hide exclusions
  and gaps from navigation.

## P1 — gaps against issues #64 / #65 (verified findings dropped)

### 3. The headline finding is missing: AWS has no managed software factory
The Workflows page says the Claude Code Action "is not a complete factory" but never states
the load-bearing sentence from #64: AWS has no managed product that takes a GitHub issue to
a reviewed PR out of the box. A reader can still leave believing the Action plus a few
gates *is* the factory. State it plainly, then present the Action as the owned composition.
Related: **Kiro Web + the Kiro GitHub App** — the only AWS offering verified live that does
issue intake → branch → implement → test → PR, never auto-merging — appears nowhere in Tech
Scan (0 mentions). Add it as the closest managed default, with its exception stated up front:
it is not Bedrock-only, and its Auto mode mixes frontier models (see §12). The build-your-own
substrate (AgentCore Harness/Runtime + Step Functions + GitHub, per the Harness page) should
get one pointer line in the candidate section, not a repeat.

### 4. No do-not-use list on either new page — dead products are still pickable
These were verified live on 12 Nov in #64/#65 and none appears in the published pages:
- Amazon Q Developer for GitHub — end of support 30 Jan 2027; **new app installations stop
  18 Nov 2026, five days from this review**.
- Google Jules — winds down 31 Dec 2026; sessions read-only since 11 Nov 2026.
- Amazon CodeCatalyst — closed to new customers 7 Nov 2025, maintenance only.
- Microsoft AutoGen — archived, no Microsoft fixes (README, opened live 12 Nov).
- OpenAI Assistants API — sunset 26 Aug 2026, use Responses + Conversations.
- Microsoft Semantic Kernel — superseded by Microsoft Agent Framework 1.0 (GA 3 Apr 2026).
- LangChain `AgentExecutor` — removed from core in LangChain 1.0 (22 Oct 2025); use `create_agent`.
- Roo Code / Continue — shut down / read-only June 2026; SWE-agent superseded, Sweep dead, Aider stalled.
- Bedrock Agents Classic — maintenance mode, no new customers from 30 Jul 2026.
Fix: add a do-not-use section to both new pages (restoring the Wave 1 spoke pattern),
each entry one line with its replacement and date. Re-confirm each at implementation time;
all were primary- or live-verified on 12 Nov, so this is a re-check, not new research.

### 5. "AWS AI Factories" name collision is never disambiguated
#64 explicitly flags it: AWS AI Factories is on-premises managed AI *infrastructure*
(Trainium3 / Blackwell racks in the customer's data centre) for training and inference —
not a software-development factory, does not do issue→PR. An AWS architect searching
"factory" will hit it first. One sentence on the Workflows page suffices.

### 6. The factory alternatives table is absent
#64's alternatives each carry a concrete trigger: GitHub Copilot cloud agent (issue→draft PR
inside GitHub, GA 25 Sep 2025), OpenAI Codex Cloud, Cursor Cloud Agents, OpenHands (MIT,
self-hostable, BYOK), Devin, Factory Droids, and GitHub Agent HQ (a platform layer for
comparing providers' PRs, not a factory). Without even a compact version, the Claude Code
Action reads as the only factory. Add a short "assessed alternatives" table — product, flow,
trigger — or explicitly defer it with a dated note. Do not silently imply the single
candidate was the only one considered.

### 7. Work tracking is claimed by the hub but absent from the Workflows page
Hub Figure 2's text reads "Workflows defines specifications and work tracking", and the hub
layer-map repeats it. The Workflows page contains no work tracking at all. #64's position:
default GitHub Issues + GitHub Projects (or GitLab issues) — the tracker lives where the
code and PRs live; Linear only when a human/orchestrator delegates each issue to one agent,
never when agents self-claim from a queue (vendor race: 10/10 rounds, multiple claimants,
183 silent overwrites); Jira: existing shops keep Jira, handoff shape is the same, not
otherwise assessed. Add the paragraph, or correct the hub figure text.

### 8. Spec Kit is undersold
The page says its flow "separates specification, plan and tasks". The quickstart's full path
is constitution (once per project) → specify → clarify → plan → checklist → tasks → analyze
→ implement → converge; the quality gates — checklist, analyze, converge — are the
differentiator against Kiro specs and are omitted. Also unnamed: Copilot is the quickstart's
documented default integration (`specify init --integration copilot`); the page's "a supported
integration" never says which agents are supported. Name Copilot as the documented default
and link the integration list for others. Add Spec Kit's own security boundary: shell steps
run with local user privileges and no capability sandbox — a spec workflow is not a sandbox.

### 9. Agents page: no pinned defaults, no orchestrator comparison
- No model versions anywhere on the page. #65's recommended default (Claude Code via Bedrock
  Invoke API, pinned Opus 5.5 / Sonnet 4.5; Codex via Bedrock Runtime, GPT-5.6 tiers) is
  dropped. The OpenAI Bedrock guide re-checked today now lists GPT-6 Sol/Luna/Astra on
  Bedrock, so the 12 Nov tier recommendation needs a re-check at implementation — but
  "confirm current model IDs" in the closing paragraph is not a substitute for naming the
  current tier with its check date.
- Orchestration covers Strands and LangGraph only. #65's table (CrewAI, Microsoft Agent
  Framework 1.0 GA, Google ADK 2.0, OpenAI Agents SDK pre-1.0, AG2 1.0) is dropped entirely,
  so a reader cannot tell what was assessed. A compact assessed/excluded table would do.
- "Start with a single agent" is stated without a source. #65 notes the OpenAI guidance is
  secondary-only; either cite it as such or soften the sentence to a stated heuristic.

### 10. November 2026 security items are absent; the controls section is generic
#65's dated items — Claude Code "Don't ask again" writing secrets into
`.claude/settings.local.json` (Apiiro, 5 Nov 2026, 1,122 public copies with a real secret);
account email in the User-Agent header; Postman silently installing plugins/remote MCP into
Claude Code and Codex (25 Oct–5 Nov); the Miasma worm delivered via agent instruction files
(9 Nov); malicious MCP packages on npm (3 Nov); AgentCorruption on AgentCore (Oct 2026);
EMBRACE embedded-browser issues — none appears. The controls paragraph ("treat them as
untrusted data… protect the agent's own permissions") is correct but gives a developer
nothing checkable. At minimum, carry over the two checkable rules: no agent writes its own
trust configuration (`mcp.json`, `.vscode/tasks.json`, `.claude/settings.json`, hooks), and
no secrets in commands/prompts/allow-rules — with the Apiiro and Kiro CVE-2026-10591
references (minimum Kiro version 0.11.130, fixed; current builds 1.4.x).

## P1 — terminology (live-checked 13 Nov 2026)

### 11. Mantle and Invoke API are used but never defined
Agents page: "identify Invoke API or Mantle, model ID and region". Anthropic's docs
(re-checked today): "Mantle is an Amazon Bedrock endpoint that serves Claude models through
the native Anthropic API shape rather than the Amazon Bedrock Invoke API." The actionable
facts for an architect are the ones omitted: Mantle has its own IAM actions under the
`bedrock-mantle:` prefix (`CreateInference`, `CountTokens`) — `bedrock:` actions do not cover
it, so a team granting only `bedrock:*` gets 403s; Mantle model IDs use the `anthropic.`
prefix with no version suffix (e.g. `anthropic.claude-sonnet-5`); inference-profile IDs such
as `us.anthropic.claude-sonnet-4-6` do not work on Mantle; both endpoints can run in one
session, with Mantle-format IDs routed to Mantle. Add a 3–4 line definition box. Same for
the `CLAUDE_CODE_USE_BEDROCK=1` / `CLAUDE_CODE_USE_MANTLE=1` switches.

### 12. Runtime vs Mantle (Codex) is compressed past the point of action
Agents page: "Runtime and Mantle differ: in the Responses API, hosted web search and
background mode are not available on Runtime; background mode on Mantle is subject to
retention settings." Accurate per OpenAI's Bedrock guide (re-checked today) but a reader
cannot act on it. The guide: two Bedrock endpoints, `bedrock-runtime` and `bedrock-mantle`;
Mantle is the native OpenAI API shape at `bedrock-mantle.<region>.api.aws/openai/v1`, model
IDs with the `openai.` prefix; Runtime uses `us.`/`global.` inference-profile IDs; hosted
web search is Mantle-only; background mode is Mantle-only and unavailable when the effective
retention mode is `none`; `store: false` does not guarantee zero data retention (ZDR).
Also directly relevant to the page's data gate, and omitted: "An AWS Region is not an OpenAI
data residency jurisdiction" — check the inference profile's destination regions, not just
the endpoint URL. Name the endpoints, the ID formats, and the ZDR/background interaction.

### 13. "Inference profile" is used once and defined nowhere
Agents page: "record the endpoint, model or inference profile, region and potential
cross-region processing" — the only occurrence of "inference profile" in all of Tech Scan
(0 matches in the Models page it points to). Define it once in Models (a named routing
object: model + region set + routing policy; `us.`/`global.` prefixes; application inference
profiles for pinning versions) and link it from Agents.

### 14. "Graph or fixed workflow" conflates two patterns
Coordination bullet: "use explicit nodes and edges when the task needs defined branches…
Strands documents graphs and fixed task workflows; LangGraph offers stateful graph
orchestration. A graph can have conditional paths…" Strands Graph is a developer flowchart
with an LLM decision per node and shared state; Strands Workflow is a fixed DAG with
parallel independent tasks and no cycles. The page's own source review already flags the
Strands page as inconsistent (Graph called model-driven and deterministic in different
places). Split the bullet: Graph = conditional branching (state which conditions are
model-driven and which are defined in code); Workflow = fixed sequence. Also note "graph"
means two different things on this page — a Strands pattern and the LangGraph framework.

### 15. "Swarm" collides across three products
Strands Swarm (autonomous peer handoffs) vs LangGraph Swarm (`create_swarm`, peer handoffs)
vs OpenAI Swarm (the educational library superseded by the Agents SDK). The page says "a
swarm can let specialists choose the next agent" without saying whose swarm. Qualify every
use, and add OpenAI Swarm to the do-not-use list (§4) so a search does not land a reader on
the archived repo.

### 16. "Coordinator" vs supervisor
The page uses "coordinator", "Manager and specialists", and "agents as tools" interchangeably.
Strands' own term for the recommended-first pattern is agents-as-tools under a supervisor.
Standardise on supervisor (the industry term) with "coordinator" defined once as the local
synonym, or the reverse — but pick one.

### 17. "Disposable runner" is not a GitHub term
Workflows candidate step 2: "Use an isolated, disposable runner". GitHub-hosted runners are
ephemeral by default; self-hosted runners need just-in-time / ephemeral configuration to be
disposable. Say "an ephemeral GitHub-hosted runner, or a just-in-time self-hosted runner",
and add the trust-policy condition the page omits: the OIDC role's trust policy must
condition on repository/branch/environment (`sub` claim), not merely on the AWS account.

### 18. Kiro Auto citation points at the wrong page
Agents page cites [5][6] for "Kiro says Auto can route to active models outside the approved
list". The sentence lives on the **available-models** page ("When Auto is enabled, it may
route requests to any Active model available to the user's Kiro profile, including models
outside the administrator's approved list… To limit processing to models on the approved
list, block Auto and set an approved model as the default." — re-checked live today), not
on the governance page (source 6). It is currently buried as a sub-link inside source 6's
description. Promote available-models to its own numbered source. Two precision adds from
the same page: Auto does **not** route to Experimental models, but it **can** route to
open-weight models (Grok 4.7, Kimi K3, MiniMax, DeepSeek, Qwen) — that is why the block
matters to a Bedrock-only policy. Also note Fable 5.1 is US East only with traffic retained
up to 30 days for abuse detection.

### 19. Zed paragraph blurs two paths
"Zed documents both Amazon Bedrock as a gateway and external agents" — accurate, but the
distinction is the point and it is half-stated. Zed's quick start (re-checked today): the
**Zed Agent** uses Zed-configured models, including a Bedrock gateway; **External Agents**
(Claude, Codex, OpenCode, Copilot, Cursor, Pi Coding Agent, Gemini CLI via ACP, or a CLI/TUI
via Terminal Threads) "usually own their own auth, model configuration, subscriptions, tools,
instructions, and MCP configuration". Name the ACP agents and state explicitly that choosing
Zed does not put external agents through the Bedrock gateway.

### 20. Factory controls: name the mechanism, not just the principle
The controls section is strong on principles and weak on the two inputs a developer will
actually set in `claude-code-action` (re-checked live today in `action.yml`):
- `restrict_untrusted_prs` defaults to `true` — it denies code-running commands on PRs from
  authors without write access. Name it; the page's pilot ("attempt a merge with a failing
  check and with the agent identity") should also attempt a command from an untrusted PR.
- `allowed_non_write_users: "*"` is the anti-pattern: it bypasses the security checks and
  the action's own docs warn it should only be used for workflows with very limited
  permissions. Name it as a do-not-use.
- CODEOWNERS: the page says "protect workflow files… with code-owner review" but omits the
  two facts the 13 Nov source review flagged — any one listed owner suffices, and GitHub
  reads CODEOWNERS from the *base* branch. Both change how a team writes the file.
- `use_bedrock: "true"` as written is correct (string input, default `"false"`), so no
  change there — but the page should also note the action supports Vertex and Foundry
  providers, so `use_bedrock` is a choice, not the only OIDC route.

## P2 — flow and structure

### 21. Hub "Choose a component": Wave 2 rows are bare links
Wave 1 rows each carry a one-line description; the Agents and Workflows rows are just links.
Also, two questions are now merged into each Wave 1 row ("Which model and access route fit
the task? How are model and tool calls controlled?"), breaking the one-question → one
reference pattern. Split the table to six rows, one per spoke, each with a description.

### 22. Hub "What is changing" duplicates the table above it
Two paragraphs that amount to "see the new pages". Either give it the actual signals
(Kiro Auto hole, no managed factory, the EOL dates) or fold it into the component table.
As written it adds a section to scroll past without adding information.

### 23. Stale counts and dates on the hub
- `#gaps`: "The four references do not yet form a complete delivery platform." There are now
  six references.
- Hub Sources date and "Last editorial review" still say 12 November 2026; the new pages say
  13 November. Re-date on the next edit, and consider a single site-wide check date.

### 24. The gate rule is repeated five times
"A failed required gate rules out that configuration, even if it is AWS-first / AWS preference
does not override a hard gate" appears in the hub (purpose, how-to-read), Agents (decision),
and Workflows (purpose, candidate hard gates). Define the rule once on the hub; spokes link
to it and list only their page-specific gates.

### 25. Three different disclaimer wordings
Agents: "Draft research reference: vendor documentation, not locally deployed or benchmarked.
Availability is not evidence that a configuration meets your organisation's needs."
Workflows: "Draft research reference; not locally deployed or benchmarked. Vendor documentation
describes capabilities, not proof that this composition works in your environment."
Wave 1 spokes: "Draft research reference. Based on published documentation, not local
deployment tests." (Harness/Sandbox add a review date and a Concepts link.)
Pick one canonical wording; the per-page review date can stay separate.

### 26. The new pages break the spoke pattern — no do-not-use / gaps sections
Every Wave 1 spoke ends with excluded-route and gaps sections. The two new pages end at
controls/pilot. That is exactly where findings §§4, 10 and the open questions (Kiro Web GA
date, Copilot Approve, model-tier re-check after re:Invent 29 Nov–4 Dec 2026) belong.
Add the sections rather than scattering the material.

### 27. Hub layer-map contains an editor's note, not reader content
"The ten responsibilities are listed in the refinement record; the detailed layer-to-spoke
table was removed from this page." A reader cannot act on this. Either restore the table
(or a link to it) or delete the sentence.

### 28. Naming drift
Nav says "Models & access" / "Harness & execution" but the pages' `<title>` and H1 still say
"Models" / "Harness". Hub Figure 2 node says "Coding agents" while the page is "Coding
agents and coordination". Align titles, or decide the nav label is a short form and note it
once.

### 29. No cost or observability line
Coordination says "set delegation limits, timeouts, budgets" but no page says how a budget is
metered (Bedrock invocation logging / CloudWatch, gateway logs, OpenTelemetry traces — the
hub already notes OTel is a framework, not a backend). One forward pointer to Wave 3
Verification, plus a metering source per route, would close it.

### 30. No figure for the factory sequence
The hub's Figure 1 shows the agent task flow; the factory's sequence (issue → assign → run →
PR → CI → review → merge → release gate) exists only as a prose numbered list. Architects
skim diagrams. A small sequence figure, or a component/owner table (intake, runner, PR bot,
CI, review, release — each with its owner and enforcement point), would make the composition
concrete — and would expose that "factory" here means "composition you own", per §3.

## P2 — redundancy (fold into the above edits, not separate work)
- Decision gates appear three times with overlapping lists (Agents §decision, Workflows
  §candidate "Hard gates", hub §how-to-read). Keep the hub's canonical list; spokes keep
  only gates that differ by page.
- "Not a complete factory" / "a composition, not a guarantee" is said twice on the Workflows
  page (purpose + candidate). Say it once, in purpose.
- The pilot / "no local pilot" disclaimer is necessary per page, but see §25 on wording.

## What PR #74 got right (keep)
- Kiro Auto block with the correct remedy (exclude Auto, approved named default, test
  enforcement and geography) — the single most important control on the Agents page.
- Quick Spec's lack of approval gates called out explicitly, correcting #64's
  overgeneralisation.
- OIDC presented as a documented capability, not turnkey setup (trust, credentials,
  `id-token: write` still required).
- Merge ≠ release approval, with the self-review caveat stated precisely (prevents the
  initiator approving, does not by itself separate merger from release approver).
- Graph determinism hedge ("specify which conditions are model-driven and which are defined
  in code") instead of repeating the Strands page's inconsistency.
- The 13 Nov source review document is unusually honest about its limits, including the
  Kiro Auto quotation resolving via the available-models page rather than the governance page.
- Cross-linking between the new pages and Wave 1 spokes is good in the body text
  (Agents → Models ×2, Harness ×2, Gateway, Sandbox; Workflows → Agents, Harness, Sandbox).

## Suggested order
1. P0 (§§1–2): nav self-links, aria-current, TOC restoration. Small, safe, no new research.
2. P1 terminology (§§11–13, 18–20): Mantle/Runtime definitions, inference-profile definition,
   Kiro Auto citation fix, action inputs. All re-checked live 13 Nov; implementable now.
3. P1 gaps (§§3–10): do-not-use boxes, Kiro Web row, alternatives table, work tracking,
   Spec Kit gates, orchestrator table, security items. Re-confirm the 12 Nov verifications
   at implementation (notably Q Developer installs stopping 18 Nov, Jules read-only since
   11 Nov, GPT-6 now on Bedrock).
4. P2 (§§21–30): hub tidy, canonical disclaimer, gate de-duplication, factory figure.

---

## Implementation note — 13 November 2026

The P0 findings (§§1–2) and P1 findings (§§3–20) in this review were implemented on the `dev` branch on 13 November 2026 and opened as a pull request from `dev` to `main` for approval. The P2 findings (§§21–30) were not implemented, except for two factual corrections inside files already being edited (the hub "four references" count and the hub editorial-review date). No GitHub issue was filed from this review.
