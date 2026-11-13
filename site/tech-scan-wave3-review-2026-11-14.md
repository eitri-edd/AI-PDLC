# Tech Scan Wave 3 source and editorial review · 14 November 2026

## Scope and method

The four new pages were reviewed against their canonical source entries and materially cited claims. On 14 November 2026 (UTC+08), direct HTTP GET returned 200 and parsed visible text for each of the 21 page-specific source entries below. The same source can appear elsewhere; this pass applies only to the named page. Existing source histories and earlier page dates are unchanged. The comments in Context and Delivery describe their authors’ source passes; this record independently checks the primary passages, not just those comments. The Stack views and Verification pages have no such source-pass comments.

The census includes every published HTML file and every external `href` or `src`, including navigation, fonts and preconnects. It found **25 pages, 277 unique fragment-free URLs and 283 exact href/src values**. These are different measures. Shared operational links retain their earlier retrieval disposition; they were not re-fetched for this pass. The inventory preserves prior source outcomes and records page-specific additions; census inclusion is not a fresh claim review for older pages.

## Source evidence

The excerpts below are short locating aids from the retrieved primary text; linked documents may change. Capability statements do not establish a local service, security or entitlement. For operational advice, independently confirm configuration and controls.

### Context — `tech-scan-context.html`

1. [Managed ingestion, storage, indexing and retrieval](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-build-managed.html) — HTTP 200; passage: “dge Base, Amazon Bedrock manages the ingestion, storage, indexing, and retrieval infrastructure for you. You provide your data sources and Amazon”.
2. [Managed connector ACL filtering excludes web crawler](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) — HTTP 200; passage: “ng Access Control Lists (except for Web Crawler) at retrieval time. The Smart Parsing feature auto-selects parsing strategy per document type inclu”.
3. [Source changes require sync](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html) — HTTP 200; passage: “om your data source, you must sync the data source so that it is re-indexed to the knowledge base. Syncing is incremental, so Amazon Bedrock only proc”.
4. [Guardrails do not cover runtime retrieved references](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve.html) — HTTP 200; passage: “e from the LLM. They are not applied to the references retrieved from Knowledge Bases at runtime. After your knowledge base is set up, you can query it and retrieve”.
5. [Namespaces logically group long-term memories](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-terminology.html) — HTTP 200; passage: “mespace A namespace is a structured path used to logically group and organize long-term memories. By defining a namespace in your memory strategy, you maintain that”.
6. [Memory read IAM keys and path normalization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/specify-long-term-memory-organization.html) — HTTP 200; passage: “olicies – The values for condition keys such as bedrock-agentcore:namespace and bedrock-agentcore:namespacePath . Use the same normalized value that your application sends, fo”.
7. [Registry provides metadata, not approval](https://modelcontextprotocol.io/registry/about) — HTTP 200; passage: “Registry is the official centralized metadata repository for publicly accessible MCP servers, backed by major trusted contributors to the MCP ecosystem such”.
8. [Layered write validation addresses memory poisoning](https://aws.amazon.com/blogs/security/help-defend-against-memory-poisoning-in-amazon-bedrock-agentcore-with-multi-layer-write-validation/) — HTTP 200; passage: “The solution extends AgentCore security layers—Identity, Policy (Cedar), and Gateway—with write-time content validation on AgentCore Memory operations.”.

### Delivery — `tech-scan-delivery.html`

1. [Pipeline action categories include source, build, test, deploy and approval](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions.html) — HTTP 200; passage: “ine provides support for six types of actions: Source Build Test Deploy Approval Invoke For information about the AWS service and partner product”.
2. [Manual approval action is configurable with separate permissions](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-action-add.html) — HTTP 200; passage: “You can add an approval action to a stage in a CodePipeline pipeline at the point where you want the pipeline to stop so someone can manually approve or reject the action.”.
3. [Self-review prevention applies to run initiator](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) — HTTP 200; passage: “proceed. Optionally, to prevent users from approving workflows runs that they triggered, select Prevent self-review . Click Save protection rules . Optionally, specify the amount of time”.
4. [Rollback redeploys an earlier revision as a new deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html) — HTTP 200; passage: “olls back deployments by redeploying a previously deployed revision of an application as a new deployment. These rolled-back deployments are technically new deployment”.

### Stack Views — `tech-scan-stack-views.html`

1. [Cross-region profiles identify destinations and opt-in-region storage](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) — HTTP 200; passage: “Regions in your account. Your input prompts and output results may be stored in the opt-in Regions for abuse detection purposes. Service Control Policies (SCPs) and AWS Identit”.
2. [Public subnet does not itself provide internet access](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html) — HTTP 200; passage: “th a private IP address. Using a public subnet does not provide internet connectivity. To enable internet access, place it in private subnets with a route to a NAT Gateway. Supported Av”.
3. [Bedrock retention modes vary with configuration and model](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html) — HTTP 200; passage: “n . Data retention modes Data retention is controlled by a mode rather than a simple on/off toggle: Mode Behavior none Zero data retention. No request or response”.

### Verification — `tech-scan-verification.html`

1. [Evaluation includes on-demand, batch and sampled online modes](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-types.html) — HTTP 200; passage: “nteractions. You can set percentage-based sampling to evaluate a portion of all sessions (for example, 10%) or define conditional filters for more tar”.
2. [Built-in and custom evaluators; built-in configurations cannot be modified](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluators.html) — HTTP 200; passage: “ncy and reliability, the configurations of built-in evaluators cannot be modified. Third-party evaluators Third-party evaluators come from the DeepEval and AutoEval open source libr”.
3. [Inspector scans source, dependencies and infrastructure as code](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) — HTTP 200; passage: “curity, Amazon Inspector scans first-party application source code, third-party application dependencies, and Infrastructure as Code for vulnerabilities. You can acti”.
4. [Ragas lists context precision and recall](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/) — HTTP 200; passage: “val Augmented Generation Context Precision Context Recall Context Entities Recall Noise Sensitivity Response Relevancy Faithfulness Nvidia Metrics Nvidia Met”.
5. [Study reports position, verbosity and self-enhancement biases](https://arxiv.org/abs/2306.05685) — HTTP 200; passage: “LM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited reasoning ability, and propose solutions to mitigate some of them. We then veri”.
6. [Faithfulness measures consistency with retrieved context](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/) — HTTP 200; passage: “c measures how factually consistent a response is with the retrieved context . It ranges from 0 to 1, with higher scores indicating better consistency. A response is considered”.

## Editorial decisions and boundaries

- Context separates source discovery from authorisation and memory-write validation from read isolation. Test identity and access controls, sync freshness, and prompt-injection handling in the actual deployment; namespace naming does not itself enforce access.
- Verification distinguishes independent oracles, held-out data and human decisions. The fictional 18/20 example is instructional, not a measured outcome; a critical access failure blocks acceptance regardless of aggregate. The 2023 judging study concerns its studied settings, not all present-day judges.
- Delivery separates merge, deployment and release authority. GitHub self-review prevention concerns the workflow initiator, not necessarily the merger; require and test any stronger separation. CodeDeploy rollback redeploys a prior revision and is not a universal reversal of side effects.
- Stack views are cross-cutting indexes, not additional runtime components. Provider networking and data-retention claims apply only to the stated service, endpoint, configuration and geography; recheck the intended account. AWS preference does not override security or approval gates.

## Verification and limitations

The author reread the new pages for source-to-claim fit, bounded vendor claims, explicit ownership and handoffs. Source documentation establishes advertised capabilities, not local implementation, plan eligibility, geographic enforcement or security guarantees. Live HTTP retrieval does not test link stability, a working pilot, deployment, benchmark, or representative-reader comprehension. No local pilot or human reader study was conducted in this review. Offline inventory and source-contract test results are recorded in the change handoff; they do not establish factual truth or browser layout.
