# EDS Developer Harness Page Redesign Considerations

The design considerations apply only to the following pages and nothing else:
1. eds-ai-workflow.html
2. eds-developer-harness.html
3. eds-path-to-production.html
4. eds-po-ba-harness.html
5. eds-skills-catalogue.html
6. eds-team-context.html

Refer to eds-workflow-review.md for the original design of these pages.

## 1. Generic (applies to all 6 pages)
### 1.1. Summarise existing pages to provide high-level descriptions instead of going deep technical
The target audience for the website is for higher management to read and understand the high-level concepts of the AI-PDLC.

### 1.2. Supply links to 3rd-party skills and software
Some of the pages mention certain skills and software that are not developed by EDS. There has to be external links to these skills in order for someone who has never seen said skills.

List of external links are as follows:
(i) Skills not maintained by EDS
/thermo-nuclear-review: https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md
/impeccable: https://impeccable.style
(ii) Tools that EDS Skills wrap
Semgrep: https://semgrep.dev/
Playwright: https://playwright.dev
ArchUnit: https://www.archunit.org
dependency-cruiser: https://github.com/sverweij/dependency-cruiser/tree/main
PIT: https://pitest.org
StrykerJS: https://stryker-mutator.io
OWASP Threat Dragon: https://owasp.org/projects/threat-dragon
agent-browser: https://agent-browser.dev
(iii) MCP Servers and outside products
Context7: https://context7.com
Sonar: https://www.sonarsource.com
Google Stitch: https://stitch.withgoogle.com
Figma Make: https://www.figma.com/make/
SpecKit: https://speckit.org
CLARA: https://github.com/dsta-productops/clara
(iv) Policies and frameworks
IM8: https://info.standards.tech.gov.sg
ARC: https://govtech-responsibleai.github.io/agentic-risk-capability-framework/
SPDD: https://www.thoughtworks.com/en-sg/insights/decoder/s/spec-driven-development
OKF: https://okf.md

---

## 2. eds-ai-workflow.html
### Fine-tune the foreward section
- Remove "This section is for product owners, business analysts, project managers, architects, developers and reviewers." There is no need to explicitly mention the target audience.

### Summarise the section "Follow the route from requirements to production"
- Figure 1 (EDS AI Workflow diagram) explicitly shows “steps x-y”, but content before this diagram did not state what these “steps” are, only reference is “Install Eitri and work through its 19 steps”. There is a link to “Developer harness” that has the diagram showing all 19 steps, but it requires the reader to backtrack to the link. I would recommend summarising the diagram using high-level terms instead of specific steps
- “Read the top row from left to right…” is not required if the diagram already has arrows.

### Remove "Read the status labels" section.
- This is not needed if the entire developer harness is not shown in detail.

