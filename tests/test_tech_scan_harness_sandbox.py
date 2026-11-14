"""Offline claim relationships for the Harness and Sandbox reference pages.

These checks establish editorial/source contracts, not live cloud behaviour or
reader comprehension. Reuse the site's stdlib HTML parser.
"""
from pathlib import Path
import unittest

from test_sources import Document, normalise

DIST = Path(__file__).resolve().parents[1] / "site/dist"


def document(page):
    return Document((DIST / f"tech-scan-{page}.html").read_text())


def node_by_id(doc, identifier):
    return next(n for n in doc.root.elements() if n.attrs.get("id") == identifier)


def text(node):
    return normalise(node.text())


class HarnessSandboxTests(unittest.TestCase):
    def test_harness_coding_uses_shell_not_mandatory_code_interpreter(self):
        doc = document("harness")
        section = node_by_id(doc, "aws-first-default")
        prose = text(section)
        self.assertIn("built-in shell and filesystem tools", prose)
        self.assertIn("clone a repository, run tests", prose)
        self.assertIn("Code Interpreter is optional", prose)
        self.assertIn("Python, JavaScript or TypeScript", prose)
        self.assertNotIn("Code Interpreter is the preferred setup", prose)
        for suffix in ("harness-tools.html", "harness-environment.html"):
            url = "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/" + suffix
            entries = [n for n in doc.root.elements("li")
                       if any(a.attrs.get("href") == url for a in n.elements("a"))]
            self.assertEqual(len(entries), 1)
            self.assertTrue(any(a.attrs.get("href") == "#" + entries[0].attrs["id"]
                                for a in section.elements("a")))

    def test_harness_compares_responsibilities_not_discovery_to_runtime(self):
        doc = document("harness")
        purpose = node_by_id(doc, "purpose")
        rows = [text(n) for n in purpose.elements("tr")]
        for responsibility in ("State and loop", "Tools and authorisation", "Memory", "Evaluation", "Observability"):
            self.assertTrue(any(responsibility in row for row in rows), responsibility)
        prose = text(purpose)
        self.assertIn("discovery metadata, not a replacement for AgentCore Gateway", prose)
        self.assertIn("OPA needs an enforcement integration", prose)
        self.assertIn("Conftest tests structured configuration", prose)
        self.assertIn("preview", text(node_by_id(doc, "source-27")))
        self.assertIn("data resets", text(node_by_id(doc, "research-only")))
        self.assertNotIn("There is no single canonical six", prose)

    def test_harness_approval_limitation_is_integration_specific(self):
        doc = document("harness")
        prose = text(node_by_id(doc, "aws-first-default"))
        self.assertIn("Inline functions", prose)
        self.assertIn("pauses", prose)
        self.assertIn("not a general absence of AgentCore approval support", prose)
        self.assertNotIn("no managed approval-callback pattern", text(node_by_id(doc, "gaps")))
        self.assertIn("hosting for agent code, not a model-serving endpoint", prose)

    def test_harness_optional_catalogue_does_not_create_false_defaults(self):
        doc = document("harness")
        section = node_by_id(doc, "conditional-alternatives")
        prose = text(section)
        self.assertIn("ToolLoopAgent", prose)
        self.assertIn("server-side state", prose)
        self.assertIn("does not require Vercel hosting", prose)
        self.assertTrue(list(section.elements("details")), "Defer the extended catalogue")
        self.assertNotIn("edge only", prose)
        for ranking in ("smallest code", "Fastest working demo", "strongest public AWS evidence", "least support"):
            self.assertNotIn(ranking, prose)
        for url in ("https://ai-sdk.dev/docs/agents/overview",
                    "https://ai-sdk.dev/providers/ai-sdk-providers/amazon-bedrock"):
            self.assertTrue(any(a.attrs.get("href") == url for a in doc.root.elements("a")))
        self.assertIn("initial research", text(node_by_id(doc, "do-not-use")))

    def test_secret_storage_distinguishes_mounts_from_kubernetes_sync(self):
        doc = document("sandbox")
        section = node_by_id(doc, "aws-first-default")
        row = next(n for n in section.elements("tr")
                   if text(n).startswith("Secrets "))
        prose = text(row)
        self.assertIn("ESO creates Kubernetes Secret objects", prose)
        self.assertIn("CSI mounts without sync", prose)
        self.assertIn("optional sync", prose)
        self.assertIn("etcd", prose)
        self.assertIn("encryption at rest", prose)
        self.assertNotIn("Never stored", prose)
        for identifier in ("source-16", "source-17", "source-18"):
            self.assertTrue(any(a.attrs.get("href") == "#" + identifier for a in row.elements("a")))

    def test_sandbox_isolation_is_qualified_and_not_a_generic_nesting_recipe(self):
        doc = document("sandbox")
        purpose = text(node_by_id(doc, "purpose"))
        self.assertIn("plain shared-kernel containers alone", purpose)
        self.assertIn("reduces risk", purpose)
        self.assertIn("not a guarantee", purpose)
        self.assertNotIn("never the host", purpose)
        alternatives = text(node_by_id(doc, "conditional-alternatives"))
        self.assertIn("documented deployment contract", alternatives)
        self.assertIn("gVisor is a userspace application kernel, not a microVM", alternatives)
        self.assertNotIn("run it inside Nitro", alternatives)
        source = node_by_id(doc, "source-19")
        self.assertTrue(any(a.attrs.get("href") == "https://gvisor.dev/docs/architecture_guide/intro/"
                            for a in source.elements("a")))

    def test_sandbox_baseline_depends_on_task_not_an_augmentation_stack(self):
        doc = document("sandbox")
        section = node_by_id(doc, "aws-first-default")
        tables = list(section.elements("table"))
        rows = [text(n) for n in tables[0].elements("tr")]
        self.assertTrue(any("Repository coding" in row and "shell and filesystem" in row for row in rows))
        self.assertTrue(any("Data analysis" in row and "Code Interpreter" in row for row in rows))
        self.assertTrue(any("Own EKS or ECS" in row and "Nitro Sandboxes" in row for row in rows))
        self.assertIn("not a prescription to deploy them together", text(section))
        self.assertNotIn("Augmentation stack", text(section))
        self.assertTrue(list(section.elements("details")), "Keep configuration detail optional")
        purpose = text(node_by_id(doc, "purpose"))
        self.assertNotIn("Code Interpreter for coding work", purpose)
        self.assertIn("Gateway policy", purpose)
        self.assertIn("not arbitrary shell networking", purpose)
        self.assertIn("VPC attachment alone", purpose)
        self.assertIn("not a host escape", text(section))
        self.assertIn("does not approve the change", text(node_by_id(doc, "gaps")))
        self.assertIn("cloud compute", text(node_by_id(doc, "do-not-use")))

    def test_references_have_one_compact_status_and_optional_product_detail(self):
        for page in ("harness", "sandbox"):
            with self.subTest(page=page):
                doc = document(page)
                header = next(n for n in doc.root.elements("header") if n.has_class("article-header"))
                status = node_by_id(doc, "tech-scan-note")
                self.assertEqual(status.tag, "p")
                self.assertIs(status.parent, header)
                self.assertIn("not locally deployed or benchmarked", text(status))
                self.assertFalse(any(n.has_class("callout--disclaimer") for n in doc.root.elements()))
                self.assertIn("?", text(header))
        doc = document("sandbox")
        self.assertTrue(list(node_by_id(doc, "conditional-alternatives").elements("details")))
        self.assertTrue(list(node_by_id(doc, "research-only").elements("details")))
        self.assertIn("initial research", text(node_by_id(doc, "do-not-use")))
        self.assertNotIn("not an isolation boundary", text(node_by_id(doc, "do-not-use")))

    def test_sandbox_records_boundary_checks_before_adoption(self):
        prose = text(node_by_id(document("sandbox"), "gaps"))
        for evidence in ("denied network destination", "credential access", "cleanup", "exact runtime", "expected and observed"):
            self.assertIn(evidence, prose)
        self.assertIn("does not approve the change", prose)

    def test_local_navigation_matches_the_tailored_section_headings(self):
        for page in ("harness", "sandbox"):
            doc = document(page)
            sections = {n.attrs.get("id"): text(next(n.elements("h2")))
                        for n in doc.root.elements("section") if list(n.elements("h2"))}
            containers = [n for n in doc.root.elements()
                          if n.has_class("page-map") or
                          (n.tag == "nav" and n.attrs.get("aria-label") == "On this page")]
            for container in containers:
                for link in container.elements("a"):
                    identity = link.attrs.get("href", "").removeprefix("#")
                    if identity in sections:
                        with self.subTest(page=page, destination=identity):
                            self.assertEqual(text(link), sections[identity])

    def test_inherited_anchors_sources_navigation_and_dates_are_preserved(self):
        for page, before in BASELINE.items():
            with self.subTest(page=page):
                doc = document(page)
                ids = {n.attrs['id'] for n in doc.root.elements() if 'id' in n.attrs}
                self.assertTrue(set(before['ids']).issubset(ids))
                for ordinal, url in enumerate(before['sources'], 1):
                    entry = node_by_id(doc, f"source-{ordinal}")
                    self.assertEqual(next(entry.elements('a')).attrs['href'], url)
                nav = next(n for n in doc.root.elements('nav') if n.attrs.get('aria-label') == 'Guide')
                expected = before['nav'][:4] + before['nav'][8:]
                self.assertEqual([(a.attrs.get('href'), text(a)) for a in nav.elements('a')], expected)
                self.assertEqual([(n.attrs.get('datetime'), text(n)) for n in doc.root.elements('time')], before['dates'])


BASELINE = {'harness': {'ids': ['aws-first-default',
                     'conditional-alternatives',
                     'do-not-use',
                     'gaps',
                     'main',
                     'page-map-caption',
                     'page-map-note',
                     'purpose',
                     'research-only',
                     'source-1',
                     'source-10',
                     'source-11',
                     'source-12',
                     'source-13',
                     'source-14',
                     'source-15',
                     'source-16',
                     'source-17',
                     'source-18',
                     'source-19',
                     'source-2',
                     'source-20',
                     'source-21',
                     'source-22',
                     'source-23',
                     'source-24',
                     'source-3',
                     'source-4',
                     'source-5',
                     'source-6',
                     'source-7',
                     'source-8',
                     'source-9',
                     'sources',
                     'tech-scan-note'],
             'sources': ['https://github.com/eitri-edd/AI-PDLC/blob/f1ed9b1bdc7ba502ffbbd233ed0780f6748f5c79/site/dist/concept.html',
                         'https://automater.ai/intel/harness-engineering/',
                         'https://www.heyuan110.com/posts/ai/2026-04-18-harness-six-layers-reverse-build/',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.md',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-models.html',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.md',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-instances-security.md',
                         'https://docs.aws.amazon.com/step-functions/latest/dg/connect-bedrockagentcore.html',
                         'https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html',
                         'https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-managed-kb.md',
                         'https://aws.amazon.com/blogs/machine-learning/how-thomson-reuters-built-an-agentic-platform-engineering-hub-with-amazon-bedrock-agentcore',
                         'https://github.com/All-Hands-AI/OpenHands',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-operations.html',
                         'https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/coding-agents-insights.html',
                         'https://langfuse.com/self-hosting/deployment/aws',
                         'https://github.com/langfuse/langfuse-terraform-aws',
                         'https://langfuse.com/handbook/product-engineering/infrastructure/ecs',
                         'https://agentopsguide.com/smithery-vs-glama-vs-official-mcp-registry/',
                         'https://github.com/eitri-edd/AI-PDLC/issues/54',
                         'https://www.getzep.com/blog/announcing-a-new-direction-for-zeps-open-source-strategy/',
                         'https://theainewsreport.com/2026-11-02-trigger-dev-env-vars-exposure-explained.html'],
             'nav': [('index.html', 'Introduction'),
                     ('transformation.html', 'Organisation transformation'),
                     ('concept.html', 'Concepts'),
                     ('tech-scan.html', 'Tech Scan (draft)'),
                     ('tech-scan-models.html', 'Models'),
                     ('tech-scan-harness.html', 'Harness'),
                     ('tech-scan-gateway.html', 'AI gateway'),
                     ('tech-scan-sandbox.html', 'Sandbox'),
                     ('ai-pdlc.html', 'AI-SDLC'),
                     ('product-discovery.html', 'Project Discovery'),
                     ('product-implementation.html', 'Product implementation'),
                     ('eds-ai-workflow.html', 'EDS AI Workflow (Eitri)'),
                     ('eds-po-ba-harness.html', 'PO/BA harness'),
                     ('eds-developer-harness.html', 'Developer harness'),
                     ('eds-path-to-production.html', 'Path to production'),
                     ('eds-team-context.html', 'Team context'),
                     ('eds-skills-catalogue.html', 'Skills catalogue'),
                     ('https://sgtechstack.github.io/ai-coding-workflow-d2-self-paced-training/',
                      'Training'),
                     ('about.html', 'About')],
             'dates': [('2026-11-12', '12 November 2026'), ('2026-11-12', '12 November 2026')]},
 'sandbox': {'ids': ['aws-first-default',
                     'conditional-alternatives',
                     'do-not-use',
                     'gaps',
                     'main',
                     'page-map-caption',
                     'page-map-note',
                     'purpose',
                     'research-only',
                     'source-1',
                     'source-10',
                     'source-11',
                     'source-12',
                     'source-13',
                     'source-14',
                     'source-15',
                     'source-2',
                     'source-3',
                     'source-4',
                     'source-5',
                     'source-6',
                     'source-7',
                     'source-8',
                     'source-9',
                     'sources',
                     'tech-scan-note'],
             'sources': ['https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/',
                         'https://aws.amazon.com/blogs/containers/aws-nitro-sandboxes-hardware-enforced-workload-isolation-on-amazon-eks/',
                         'https://github.com/aws-samples/sample-eks-nitro-sandbox',
                         'https://www.qovery.com/blog/aws-nitro-sandboxes-eks-vs-daytona-e2b',
                         'https://waveo.io/insights/signal-noise-2026-11-09/',
                         'https://aws.amazon.com/security/security-bulletins/2026-065-aws/',
                         'https://www.beyondtrust.com/blog/entry/amazon-bedrock-agentcore-python-sdk-rce-cves',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html',
                         'https://github.com/perplexityai/SPACE',
                         'https://schristoph.online/blog/aws-lambda-microvms/',
                         'https://prized.dev/docs/sandboxes-vs-aws-nitro-sandboxes-lambda-microvms',
                         'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-instances-security.md',
                         'https://github.com/eitri-edd/AI-PDLC/issues/54',
                         'https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/',
                         'https://builder.aws.com/content/3LmNG2STjfdIrh1BIvWkHHDZpsi'],
             'nav': [('index.html', 'Introduction'),
                     ('transformation.html', 'Organisation transformation'),
                     ('concept.html', 'Concepts'),
                     ('tech-scan.html', 'Tech Scan (draft)'),
                     ('tech-scan-models.html', 'Models'),
                     ('tech-scan-harness.html', 'Harness'),
                     ('tech-scan-gateway.html', 'AI gateway'),
                     ('tech-scan-sandbox.html', 'Sandbox'),
                     ('ai-pdlc.html', 'AI-SDLC'),
                     ('product-discovery.html', 'Project Discovery'),
                     ('product-implementation.html', 'Product implementation'),
                     ('eds-ai-workflow.html', 'EDS AI Workflow (Eitri)'),
                     ('eds-po-ba-harness.html', 'PO/BA harness'),
                     ('eds-developer-harness.html', 'Developer harness'),
                     ('eds-path-to-production.html', 'Path to production'),
                     ('eds-team-context.html', 'Team context'),
                     ('eds-skills-catalogue.html', 'Skills catalogue'),
                     ('https://sgtechstack.github.io/ai-coding-workflow-d2-self-paced-training/',
                      'Training'),
                     ('about.html', 'About')],
             'dates': [('2026-11-12', '12 November 2026'), ('2026-11-12', '12 November 2026')]}}


if __name__ == "__main__":
    unittest.main()
