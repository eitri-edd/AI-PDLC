"""Offline editorial regressions, not live availability or deployment tests.

Use the site's stdlib parser so disclosures, claims and canonical citations are
checked together. Representative-reader comprehension remains untested.
"""

from pathlib import Path
import re
import unittest
from unittest.mock import patch

from test_sources import Document, Element, normalise, statically_hidden
from test_tech_scan_harness_sandbox import BASELINE

DIST = Path(__file__).resolve().parents[1] / "site/dist"

# Inherited contracts at 4e438010. IDs are identities, not display numbers.
LEGACY_URLS = {
    "models": [
        "https://developers.openai.com/api/docs/guides/amazon-bedrock",
        "https://github.com/eitri-edd/AI-PDLC/blob/f1ed9b1bdc7ba502ffbbd233ed0780f6748f5c79/site/dist/concept.html",
        "https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-openai.html",
        "https://learn.chatgpt.com/docs/amazon-bedrock",
        "https://code.claude.com/docs/en/amazon-bedrock",
        "https://developers.openai.com/api/docs/guides/decisions",
        "https://docs.aws.amazon.com/bedrock/latest/userguide/models-api-compatibility.html",
        "https://docs.aws.amazon.com/claude-platform/latest/userguide/feature-support.html",
        "https://s5labs.io/resources/insights/open-decision-models-clef-d1-jev/",
    ],
    "gateway": [
        "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.md",
        "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html",
        "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html",
        "https://developers.openai.com/api/docs/guides/amazon-bedrock",
        "https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-openai.html",
        "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-managed-kb.md",
        "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html",
        "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-acl.md",
        "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.md",
        "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-guard.html",
        "https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents",
        "https://vdf.ai/blog/ai-gateway-comparison/",
        "https://langfuse.com/self-hosting/deployment/aws",
        "https://kiro.dev/docs/models/available-models",
        "https://kiro.dev/docs/enterprise/governance/model",
        "https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter",
    ],
}
# "References last checked" / "Last editorial review" per page.
# Check dates moved to 14 November 2026 with the daily reference check;
# gateway was 13 November 2026 after the issue #81 source replacement.
# Editorial review dates stay where the last edit left them.
CHECK_DATES = {
    "models": ("14 November 2026", "2026-11-14"),
    "gateway": ("14 November 2026", "2026-11-14"),
}
EDITORIAL_DATES = {
    "models": "2026-11-12",
    "gateway": "2026-11-13",
}
LEGACY_IDS = {"main", "tech-scan-note", "page-map-caption", "page-map-note",
              "purpose", "aws-first-default", "conditional-alternatives",
              "research-only", "do-not-use", "gaps", "sources"}


def document(page):
    return Document((DIST / f"tech-scan-{page}.html").read_text())


def by_id(doc, identifier):
    return next(node for node in doc.root.elements()
                if node.attrs.get("id") == identifier)


def paragraph(section, phrase):
    node = next((node for node in section.elements("p")
                 if phrase in normalise(node.text())), None)
    assert node is not None, f"Missing qualified claim: {phrase}"
    return node


class ModelsGatewayTests(unittest.TestCase):
    def assert_cited(self, node, source):
        self.assertIsNotNone(node, "The qualified claim must remain in a paragraph")
        self.assertIn(f"#source-{source}",
                      [link.attrs.get("href") for link in node.elements("a")])

    def test_typesafe_box_maturity_is_feature_specific_and_cited(self):
        doc = document("models")
        research = by_id(doc, "research-only")
        claim = paragraph(research, "Box is opt-in and not production-ready.")
        self.assert_cited(claim, 10)
        self.assertIn("Jev itself is in public beta, not GA, and Box is a preview feature on top of that: neither the product's status nor the feature's status makes Box production-ready.",
                      normalise(claim.text()))
        source = by_id(doc, "source-10")
        self.assertEqual(next(source.elements("a")).attrs["href"],
                         "https://docs.typesafe.ai/primitives/box")
        gap = normalise(by_id(doc, "gaps").text())
        self.assertIn("No suitable approved route for typed visual grounding is established here.", gap)
        self.assertNotIn("No Box support verified anywhere", doc.root.text())
        self.assertNotIn("typed visual-grounding decisions stay a human judgement, not a model call", gap)

    def test_agentcore_inference_routing_is_not_confused_with_tool_targets(self):
        doc = document("gateway")
        default = by_id(doc, "aws-first-default")
        claim = paragraph(default, "AgentCore Gateway inference targets provide a unified LLM proxy")
        self.assert_cited(claim, 17)
        self.assertIn("Amazon Bedrock, OpenAI and Anthropic", normalise(claim.text()))
        fallback = paragraph(default, "Gateway rules configure model routing and fallback for inference targets.")
        self.assert_cited(fallback, 18)
        self.assertIn("Every fallback destination still needs approval.", normalise(fallback.text()))
        for number, suffix in [(17, "gateway-targets-inference.html"), (18, "gateway-rules-fallback.html")]:
            self.assertEqual(next(by_id(doc, f"source-{number}").elements("a")).attrs["href"],
                             "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/" + suffix)
        text = normalise(doc.root.text())
        for obsolete in ["There is no AWS product that is a multi-provider LLM router",
                         "No AWS multi-provider LLM router exists",
                         "tool/MCP gateway, not an LLM router",
                         "approved-model policy is enforced nowhere"]:
            self.assertNotIn(obsolete, text)
        self.assertIn("IAM and client configuration can also restrict model access", text)
        self.assertIn("Gateway policy governs traffic through the Gateway, not arbitrary shell networking.", text)
        self.assertIn("Check the selected region, model, operation and API dialect", text)
        self.assertIn("Add only the controls the use case needs", text)

    def test_langfuse_gateway_beta_separates_current_features_from_roadmap(self):
        doc = document("gateway")
        research = by_id(doc, "research-only")
        claim = paragraph(research, "Langfuse now documents a separate AI Gateway in public beta.")
        self.assert_cited(claim, 19)
        roadmap = paragraph(research, "Provider fallbacks, hard spend caps and automatic task-based model routing are roadmap items, not implemented features.")
        self.assert_cited(roadmap, 19)
        self.assertIn("Keep this option research-only", normalise(research.text()))
        self.assertNotIn("Langfuse is observability, not a gateway", doc.root.text())
        self.assertEqual(next(by_id(doc, "source-19").elements("a")).attrs["href"],
                         "https://langfuse.com/docs/gateway/overview")
        self.assertIn("deployment", by_id(doc, "source-13").text())

    def test_models_core_route_keeps_policy_without_catalogue_or_boilerplate(self):
        doc = document("models")
        article = next(doc.root.elements("article"))
        text = normalise(article.text())
        self.assertEqual(text.count("Draft research reference. Based on published documentation, not local deployment tests."), 1)
        self.assertFalse(any(n.has_class("callout--disclaimer") for n in article.elements()))
        self.assertIn("Use approved Claude and OpenAI models through Amazon Bedrock.", text)
        self.assertIn("Direct provider APIs are exceptions", text)
        self.assertIn("Fallbacks, retrieval reasoning and evaluator models need the same model approval", text)
        self.assertIn("Excluded from this route", by_id(doc, "do-not-use").text())
        self.assertNotIn("Offer one default and at most one justified alternative", text)
        self.assertNotIn("Nothing here is locally validated", text)
        self.assertNotIn("No option on this page has been locally deployed", text)
        research = by_id(doc, "research-only")
        details = list(research.elements("details"))
        self.assertTrue(details, "Additional candidates belong in optional detail")
        extra = " ".join(n.text() for n in details)
        for name in ["Strands Decider 2B", "Cloudflare Clef", "Convai Laya", "Liquid AI d1", "Perplexity pplx-decider", "Mapika decider-2b"]:
            self.assertIn(name, extra)
        self.assertIn("A fixed output shape", text)
        self.assertIn("does not establish accuracy or calibrated confidence", text)
        self.assertNotIn("OpenAI calls the same type", text)

    def test_gateway_alternatives_start_from_missing_capability_not_platform_buckets(self):
        doc = document("gateway")
        alternatives = by_id(doc, "conditional-alternatives")
        text = normalise(alternatives.text())
        self.assertIn("First name the capability the Bedrock and AgentCore baseline cannot meet.", text)
        self.assertIn("Then consider existing infrastructure and who will operate the alternative.", text)
        claim = paragraph(alternatives, "LiteLLM documents load balancing, fallbacks, timeouts and retries")
        self.assert_cited(claim, 20)
        self.assertEqual(next(by_id(doc, "source-20").elements("a")).attrs["href"],
                         "https://docs.litellm.ai/docs/routing")
        details = list(alternatives.elements("details"))
        self.assertTrue(details)
        extra = " ".join(n.text() for n in details)
        for name in ["OpenRouter", "Portkey", "Kong AI Gateway", "Envoy AI Gateway", "Unkey"]:
            self.assertIn(name, extra)
        for obsolete in ["Zero infrastructure →", "Kubernetes-native →", "On AWS →"]:
            self.assertNotIn(obsolete, text)
        self.assertIn("secondary comparison", text)
        self.assertIn("not independently verified", text)
        self.assertIn("Licensing, incident and lifecycle claims", text)

    def test_gateway_core_prose_keeps_controls_and_identity_limits_visible(self):
        doc = document("gateway")
        article = next(doc.root.elements("article"))
        text = normalise(article.text())
        self.assertEqual(text.count("Draft research reference. Based on published documentation, not local deployment tests."), 1)
        self.assertFalse(any(n.has_class("callout--disclaimer") for n in article.elements()))
        self.assertIn("Controls and common mistakes", by_id(doc, "do-not-use").text())
        self.assertNotIn("No option on this page has been locally deployed", text)
        default = by_id(doc, "aws-first-default")
        identity = paragraph(default, "does not authenticate the end user")
        self.assert_cited(identity, 8)
        self.assertIn("verified identity", normalise(identity.text()))
        node = identity
        while node is not default:
            self.assertNotEqual(node.tag, "details", "Identity limit must stay in the core route")
            node = node.parent
        self.assertIn("Direct provider APIs remain exceptions", text)
        self.assertIn("fail closed", normalise(by_id(doc, "gaps").text()))

    def test_local_contents_describe_tailored_sections_without_changing_anchors(self):
        for page, purpose, exclusions in [("models", "Choose a model for the task", "Excluded from this route"),
                                          ("gateway", "Separate model routing from tool access", "Controls and common mistakes")]:
            doc = document(page)
            for nav in doc.root.elements("nav"):
                if nav.attrs.get("aria-label") != "On this page":
                    continue
                labels = {a.attrs.get("href"): normalise(a.text()) for a in nav.elements("a")}
                self.assertEqual(labels["#purpose"], purpose)
                self.assertEqual(labels["#do-not-use"], exclusions)
                self.assertEqual(labels["#gaps"], "Gaps and open questions")
                self.assertEqual(normalise(next(by_id(doc, "do-not-use").elements("h2")).text()), exclusions)
        research = by_id(document("models"), "research-only")
        self.assertIn("A typed decision returns an answer in a fixed form", normalise(research.text()))

    def assert_inherited_contract(self, page, raw):
        doc = Document(raw)
        ids = [node.attrs["id"] for node in doc.root.elements() if "id" in node.attrs]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate HTML ID")
        expected = LEGACY_IDS | {f"source-{n}" for n in range(1, len(LEGACY_URLS[page]) + 1)}
        self.assertTrue(expected.issubset(ids), expected - set(ids))
        for number, url in enumerate(LEGACY_URLS[page], 1):
            source = by_id(doc, f"source-{number}")
            self.assertEqual(next(source.elements("a")).attrs["href"], url)
        guide = re.search(r'<nav aria-label="Guide">.*?</nav>', raw, re.S)
        self.assertIsNotNone(guide)
        assert guide is not None
        nav = next(n for n in doc.root.elements("nav") if n.attrs.get("aria-label") == "Guide")
        expected = BASELINE["harness"]["nav"][:4] + BASELINE["harness"]["nav"][8:]
        self.assertEqual([(a.attrs.get("href"), normalise(a.text())) for a in nav.elements("a")], expected)
        check_text, check_datetime = CHECK_DATES[page]
        dates = [node for node in doc.root.elements("p") if node.has_class("source-check-date")]
        self.assertEqual(len(dates), 1)
        self.assertEqual(normalise(dates[0].text()), f"References last checked: {check_text} .")
        self.assertEqual(next(dates[0].elements("time")).attrs["datetime"], check_datetime)
        reviews = [node for node in doc.root.elements("p") if "Last editorial review:" in node.text()]
        self.assertEqual(len(reviews), 1)
        self.assertEqual(next(reviews[0].elements("time")).attrs["datetime"], EDITORIAL_DATES[page])
        published = (["15 September 2026", "23 October 2026"] if page == "models" else
                     ["19 August 2026", "29 May 2026", "10 September 2026", "March and October 2026"])
        for value in published:
            self.assertIn(value, normalise(doc.root.text()), "Preserve publication and historical dates")

    def test_inherited_urls_anchors_dates_and_guide_navigation_are_preserved(self):
        for page in LEGACY_URLS:
            with self.subTest(page=page):
                raw = (DIST / f"tech-scan-{page}.html").read_text()
                self.assert_inherited_contract(page, raw)

    def test_preservation_assertions_reject_removed_url_and_anchor_fixtures(self):
        raw = (DIST / "tech-scan-models.html").read_text()
        for broken in [raw.replace(LEGACY_URLS["models"][0], "https://invalid.example/", 1),
                       raw.replace('id="tech-scan-note"', 'id="lost-anchor"', 1)]:
            with self.assertRaises(AssertionError):
                self.assert_inherited_contract("models", broken)

    def test_sources_stay_final_visible_and_citation_numbers_follow_list_order(self):
        for page, count in [("models", 11), ("gateway", 26)]:
            with self.subTest(page=page):
                doc = document(page)
                source = by_id(doc, "sources")
                lists = [n for n in doc.root.elements("ol") if n.has_class("source-list")]
                self.assertEqual(len(lists), 1)
                self.assertIs(lists[0].parent, source)
                self.assertFalse(statically_hidden(lists[0]))
                entries = [n for n in lists[0].children if isinstance(n, Element) and n.tag == "li"]
                self.assertEqual(len(entries), count)
                self.assertEqual([normalise(n.text()) for n in source.elements("h2")], ["Sources"])
                sections = list(next(doc.root.elements("article")).elements("section"))
                self.assertIs(sections[-1], source)
                targets = {entry.attrs["id"]: (i, normalise(next(entry.elements("a")).text()))
                           for i, entry in enumerate(entries, 1)}
                all_ids = {n.attrs["id"] for n in doc.root.elements() if "id" in n.attrs}
                cited = set()
                for link in doc.root.elements("a"):
                    href = link.attrs.get("href", "")
                    if href.startswith("#"):
                        self.assertIn(href[1:], all_ids)
                    if href.startswith("#source-"):
                        number, title = targets[href[1:]]
                        self.assertEqual(normalise(link.text()), f"[{number}]")
                        self.assertEqual(link.attrs.get("aria-label"), f"Source {number}: {title}")
                        cited.add(href[1:])
                self.assertEqual(cited, set(targets), "Every retained source needs an actual content citation")

    def test_model_vendor_sources_are_not_presented_as_local_approval_authority(self):
        doc = document("models")
        source = normalise(by_id(doc, "source-1").text())
        self.assertNotIn("Documents approved Claude", source)
        self.assertIn("The approved-provider route and exception criteria are this guide's selection constraints.", source)
        self.assertNotIn("Omit it from the minimal shortlist", doc.root.text())
        typed = paragraph(by_id(doc, "research-only"), "A typed decision returns an answer in a fixed form")
        self.assertEqual(normalise(typed.text()).count("check the form of an answer"), 0)

    def test_semantic_assertions_reject_inverted_claim_relationships(self):
        cases = [
            ("models", "Box is opt-in and not production-ready.",
             "Box is opt-in and production-ready.",
             self.test_typesafe_box_maturity_is_feature_specific_and_cited),
            ("gateway", "provide a unified LLM proxy", "do not provide a unified LLM proxy",
             self.test_agentcore_inference_routing_is_not_confused_with_tool_targets),
            ("gateway", "Every fallback destination still needs approval.",
             "Not every fallback destination still needs approval.",
             self.test_agentcore_inference_routing_is_not_confused_with_tool_targets),
            ("gateway", "are roadmap items, not implemented features.",
             "are implemented features, not roadmap items.",
             self.test_langfuse_gateway_beta_separates_current_features_from_roadmap),
        ]
        load = document
        for page, before, after, check in cases:
            with self.subTest(mutation=after):
                raw = (DIST / f"tech-scan-{page}.html").read_text()
                self.assertIn(before, raw)
                broken = Document(raw.replace(before, after, 1))
                with patch(__name__ + ".document",
                           side_effect=lambda name: broken if name == page else load(name)):
                    with self.assertRaises(AssertionError):
                        check()


if __name__ == "__main__":
    unittest.main()
