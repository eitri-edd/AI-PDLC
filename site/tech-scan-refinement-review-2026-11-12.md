# Tech Scan refinement review · 12 November 2026

## Scope and authority

Implements the nine proposals approved after reviewing issues #54 and #59. The starting revision is `4e438010b935d50df6fcd9a5b4e46ac1079c0ea9` on `dev`. Scope is the Tech Scan hub and four published component references, their regression tests, the writing-standard clarification and this source/maintenance record.

The work retains the hub-and-spoke structure, current navigation, managed Claude/OpenAI selection assumptions, AWS deployment scope and existing acceptance/release authority. It does not build the planned spokes, provision cloud resources, benchmark products, migrate repositories or change standing monitoring jobs. A software library, an AWS deployment and a third-party managed service are different choices; listing one does not authorise its data path or an exception.

This is a targeted factual/editorial refinement, not a new whole-site source-maintenance pass. Existing page-wide reference dates and historical publication/editorial dates remain unchanged. The inventory retains the exact preceding inventory and records new or changed claim scopes separately. Previous source access limitations remain evidence, not silently cleared status.

## Approved proposal mapping

| Proposal | Change and location | Remaining limit |
| --- | --- | --- |
| Refresh current capabilities and feature maturity | Gateway distinguishes inference targets from tool/MCP targets, and treats the separate Langfuse gateway as beta. Models separates product availability from experimental Box output. | Documentation is not a qualified configuration in the intended account. |
| Clarify execution and security boundaries | Harness and Sandbox distinguish repository shell, optional computation tools, workload isolation, egress and credential controls; the secrets and gVisor descriptions are scoped. | No attack simulation or cloud pilot performed. |
| Compare responsibilities before products | Harness separates the managed loop, framework/SDK, Runtime hosting and supporting services; registry discovery is not gateway authorisation. Additional candidates are optional research when evidence does not discriminate them. | No comparative local performance or reliability findings. |
| Lead with reader decisions | The hub starts with four questions and links to the corresponding references. The task figure separates model and optional tool paths; its caption and source note identify the adaptation. | The illustration is not a deployment architecture or a guarantee of enforcement. |
| Use natural, connected prose | One compact research qualification per page replaces repeated generic disclaimers and author-facing instructions. Specific safety and availability caveats stay beside the affected choice. | Author and independent-agent reviews are not human comprehension evidence. |
| Use consistent fields rather than identical headings | Section names distinguish exclusions, lifecycle warnings and configuration mistakes. The authoritative reference-page guidance records the shared comparison meanings. | Existing deep links and source identities remain stable despite visible-label changes. |
| Clarify terminology and scope | Definitions distinguish protocols, formats, toolkits and local conventions; React is a UI library. Local selection assumptions do not become organisation-wide policy. | Product and protocol versions need rechecking for an actual selection. |
| Make evidence useful | Decisive corrections cite primary documentation. Availability, reference deployment, reported operation and local qualification remain separate. Source history is retained. | A successful fetch is not evidence for an entire product table. |
| Assess actual reader decisions | The tasks below identify expected distinctions and what to observe in a representative-reader session. | **Session not performed; reader comprehension remains unverified.** |

## Diagram and anchor decisions

The original AWS reference architecture has a tool-gateway path and a separate LiteLLM inference-gateway path. The revised hub diagram adapts those responsibilities, not the original numbered sequence. It adds a conditional code-execution branch and returns results to the harness before continuation or completion. Retrieval is not shown as a feature awaiting publication: only the dedicated Context reference is planned.

The large wave figure is replaced with compact optional publication-plan text. Its four existing IDs remain meaningful destinations. The original-layer crosswalk moves into the maintenance section below; the public `layer-map` destination retains a compact optional explanation. This is a reading-path change, not deletion of coverage obligations.

## Original coverage and publication plan

The original proposal's ten responsibilities remain accounted for:

1. Model access and hosting → published Models reference; model-weight self-hosting remains outside the recommended route.
2. Agent loop and workflow graph → published Harness reference; distinguish outer workflow decisions from the model/tool loop.
3. Context and retrieval → dedicated Context reference planned; current gateway/harness guidance retains relevant retrieval and identity limits.
4. Specifications and work tracking → Workflows planned; preserve the existing GitHub/GitLab source of truth.
5. Execution and isolation → published Sandbox reference.
6. Build-loop verification → Verification planned; deterministic checks and independent acceptance remain outside the agent's ability to redefine success.
7. Security scanning and quality gates → Verification planned; include exact-commit and dependency-coverage boundaries, not a claim that continuous scanning is a promotion gate.
8. CI/CD and release → Delivery planned; preserve authorised human release decisions and workload-specific deployment tooling.
9. Policy, identity and governance → Delivery planned, with relevant current controls retained in the component references; machine checks do not enforce an entire policy framework.
10. Observability and outcome measurement → current Harness covers agent telemetry; Delivery will cover operational/outcome measurement and full accepted-outcome cost.

Gateway is an additional published responsibility. Workflows, Factories and Agents form the next writing wave. Context, Verification and Delivery follow, then Languages and AWS-platform cross-cutting views. Those views will link to canonical product entries rather than duplicate them. The spec-durability choice and future product shortlists are not resolved by this refinement.

## Standards decision

`writing.md` now explicitly permits one plain-text draft research qualification on the Tech Scan hub and independently linked component pages, together with the existing `Tech Scan (draft)` navigation label. It does not introduce a status badge or description-metadata status field. Material operational caveats and feature maturity remain beside their claims.

The reference-page section clarifies existing flexibility: use consistent comparison fields, not identical H2 headings, and explain unfamiliar mechanisms locally rather than requiring a Concepts detour. No exemption from source-list, date, accessibility or approval requirements is introduced. The component pages retain their page maps. The hub uses the approved narrow lookup exception now recorded in `design.md`: its question-led component index replaces the redundant separate page map. Initial desktop and mobile rendering showed the duplicate map pushing the actual choice table below the opening viewport. Its existing caption/note IDs now belong to the component index, and fragment offsets remain covered by browser checks.

## Representative-reader check — pending

Ask a representative reader with the stated product/IT-delivery background to use the pages without corrective coaching. Ask them to explain what they would ask an engineer or platform specialist to establish; do not require the reader to execute cloud-security tests personally.

- **Model versus tool traffic:** Which component or configuration controls each path? Expected distinction: inference routing and tool access are different responsibilities, even when one product supports both.
- **Code execution:** Where would repository commands run, and when would a calculation tool be added? Expected distinction: the harness shell/filesystem is not automatically a separate Code Interpreter deployment, and each environment has its own controls.
- **Alternative choice:** Which unmet requirement justifies moving beyond a proposed starting choice? Expected response: cite a specific supported capability or deployment constraint, not popularity or an identical generic trigger.
- **Evidence before adoption:** What still needs checking, and who makes the next decision? Expected response: identify exact configuration/data/control evidence, retain unresolved findings and preserve existing approval authority.

Record the participant's answer, route, hesitation, assistance, errors and consequential misunderstandings. Revise the affected passage and repeat the task when needed. Do not replace this observation with an agent-generated answer or an invented completion time.

## Ownership, draft exit and monitoring

A named content owner has not been confirmed by this change; the former public `TBD` table column is not a substitute for assigning one. Keep the draft label until ownership is agreed, the current published source scope has a recorded disposition, consequential publication defects are resolved and the representative-reader check has been completed. This does not require pretending that every product is locally qualified: adoption qualification remains a separate decision.

The existing scheduled reference/readability jobs are not modified. Their coverage of Tech Scan is not established by this change. Follow-up ownership should identify who checks vendor releases, feature maturity, lifecycle/security notices and categorical negative claims when those sources change. This record does not create a schedule or new organisational gate.

## Verification record

The integrated candidate passes **86 standard-library tests**. The parent replayed all four new regression modules against a pristine baseline fixture: they rejected old behaviour through assertion failures, including subtests, with **zero execution errors**. The candidate also exercises inverted-meaning and preservation mutations. These are offline editorial and structural checks, not future live-availability guarantees.

All **766 original HTML IDs**, inherited canonical source URLs and labelled dates are preserved across **19 pages**. The **14 unrelated HTML pages are byte-for-byte unchanged**. The source census contains **214 fetch destinations**, **220 exact external link values** and **347 page/URL assessments**. There are **21 newly cited fetch destinations** and **29 targeted primary page/source checks**; inherited claims that were not re-fetched retain explicit limitations. The exact pre-refinement inventory is preserved as the latest history snapshot, including its earlier history. Current result counts are regenerated from the current unique records rather than accumulated from previous passes.

Browser checks cover all **five Tech Scan pages** at **1440, 768, 375 and 320 pixels**: **20 viewport checks**, no document-level horizontal overflow or script errors, visible Sources sections, working citation destinations and restored disclosure states after PDF printing. Native content and legacy wave destinations were exercised without JavaScript. The hub's question/destination index does not require horizontal scrolling at phone widths. Wider technical comparison tables retain their labelled horizontal-scrolling regions.

The first browser probe exposed desktop legacy wave aliases beneath the sticky header and the phone-width component index hiding its action column. A later screenshot inspection also found that Harness/Sandbox local navigation still used the old template labels; a regression first rejected those mismatches, then passed after the link labels were aligned with the tailored headings. Scoped hub offsets and a wrapping two-column index corrected those observed problems; repeat checks passed. The revised diagram was visually inspected, and the cited AWS PDF was extracted and its separate gateway paths inspected. Representative-reader comprehension is still unverified. Independent final review is recorded separately when complete.

No local AWS deployment, product benchmark or representative-reader session was performed.
