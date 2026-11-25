"""Offline behavioral regression for the pinned MIT-licensed actions/deploy-pages."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github/scripts/patch_deploy_pages.py"
# Extracted from actions/deploy-pages v5.0.1, MIT licensed.
FIXTURE = 'async function getArtifactMetadata({ artifactName }) {\n  const artifactClient = new DefaultArtifactClient()\n\n  // Primarily for debugging purposes, accuracy is not critical\n  const requestOptions = {\n    method: \'POST\',\n    url: `${getArtifactsServiceOrigin()}/twirp/github.actions.results.api.v1.ArtifactService/ListArtifacts`,\n    headers: {\n      \'content-type\': \'application/json\'\n    },\n    body: {}\n  }\n\n  try {\n    core.info(`Fetching artifact metadata for "${artifactName}" in this workflow run`)\n\n    let response\n    try {\n      const twirpResponse = await artifactClient.listArtifacts()\n      response = wrapTwirpResponseLikeOctokit(twirpResponse, requestOptions)\n    } catch (twirpError) {\n      core.error(\'Listing artifact metadata failed\', twirpError)\n      const octokitError = wrapTwirpErrorLikeOctokit(twirpError, requestOptions)\n      throw octokitError\n    }\n\n    const filteredArtifacts = response.data.artifacts.filter(artifact => artifact.name === artifactName)\n\n    const artifactCount = filteredArtifacts.length\n    core.debug(`List artifact count: ${artifactCount}`)\n\n    if (artifactCount === 0) {\n      throw new Error(\n        `No artifacts named "${artifactName}" were found for this workflow run. Ensure artifacts are uploaded with actions/upload-artifact@v4 or later.`\n      )\n    } else if (artifactCount > 1) {\n      throw new Error(\n        `Multiple artifacts named "${artifactName}" were unexpectedly found for this workflow run. Artifact count is ${artifactCount}.`\n      )\n    }\n\n    const artifact = filteredArtifacts[0]\n    core.debug(`Artifact: ${JSON.stringify(artifact)}`)\n\n    if (!artifact.size) {\n      core.warning(\'Artifact size was not found. Unable to verify if artifact size exceeds the allowed size.\')\n    }\n\n    return artifact\n  } catch (error) {\n    core.error(\n      \'Fetching artifact metadata failed. Is githubstatus.com reporting issues with API requests, Pages, or Actions? Please re-run the deployment at a later time.\',\n      error\n    )\n    throw error\n  }\n}\n'

# Unmodified deployment creation function from the same pinned bundle.
CREATE = "async function createPagesDeployment({ githubToken, artifactId, buildVersion, idToken, isPreview = false }) {\n  const octokit = github.getOctokit(githubToken)\n\n  const payload = {\n    artifact_id: artifactId,\n    pages_build_version: buildVersion,\n    oidc_token: idToken\n  }\n  if (isPreview === true) {\n    payload.preview = true\n  }\n  core.info(`Creating Pages deployment with payload:\\n${JSON.stringify(payload, null, '\\t')}`)\n\n  try {\n    const response = await octokit.request('POST /repos/{owner}/{repo}/pages/deployments', {\n      owner: github.context.repo.owner,\n      repo: github.context.repo.repo,\n      ...payload\n    })\n\n    return response.data\n  } catch (error) {\n    core.error('Creating Pages deployment failed', error)\n    throw error\n  }\n}\n"

class LookupRetryTests(unittest.TestCase):
    def test_eventual_visibility_retries_inside_lookup(self):
        if not SCRIPT.exists():
            self.fail("lookup patch script is missing")
        spec = importlib.util.spec_from_file_location("patch_deploy_pages", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        data = FIXTURE.encode()
        patched = module.patch_bundle(data, hashlib.sha256(data).hexdigest()).decode()
        harness = """
let calls = 0;
const core = {info(){}, debug(){}, warning(){}, error(){}};
const getArtifactsServiceOrigin = () => 'https://example.invalid';
const wrapTwirpResponseLikeOctokit = (x) => ({data:x});
const wrapTwirpErrorLikeOctokit = x => x;
const setTimeout = fn => fn();
class DefaultArtifactClient { async listArtifacts() { calls++; return {artifacts: calls < 3 ? [] : [{name:'github-pages',size:1,id:7}]}; } }
""" + patched + """
getArtifactMetadata({artifactName:'github-pages'}).then(x=>console.log(JSON.stringify({calls,id:x.id}))).catch(e=>{console.error(e); process.exit(1)});
"""
        result = subprocess.run(["node", "-e", harness], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), {"calls": 3, "id": 7})

    def test_zero_duplicates_and_errors_do_not_create_or_retry_wrong_operation(self):
        spec = importlib.util.spec_from_file_location("patch_deploy_pages", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        data = FIXTURE.encode()
        patched = module.patch_bundle(data, hashlib.sha256(data).hexdigest()).decode()
        harness = """
const mode = process.argv[1]; let calls = 0, posts = 0;
const core = {info(){}, debug(){}, warning(){}, error(){}};
const getArtifactsServiceOrigin = () => 'https://example.invalid';
const wrapTwirpResponseLikeOctokit = x => ({data:x});
const wrapTwirpErrorLikeOctokit = x => x;
const setTimeout = fn => fn();
const github = {context:{repo:{owner:'o',repo:'r'}},getOctokit(){return {request:async()=>{posts++;throw Error('HTTP 500')}}}};
class DefaultArtifactClient { async listArtifacts() {
  calls++;
  if(mode === 'error') throw Error('lookup failure');
  const one = {name:'github-pages',size:1,id:7};
  return {artifacts: mode === 'zero' ? [] : mode === 'duplicate' ? [one,one] : [one]};
} }
""" + patched + CREATE + """
(async()=>{try {const a=await getArtifactMetadata({artifactName:'github-pages'});
await createPagesDeployment({githubToken:'x',artifactId:a.id,buildVersion:'v',idToken:'x'});
} catch(e) {console.log(JSON.stringify({calls,posts,error:e.message}));}})();
"""
        for mode, calls, posts, message in [
            ("zero", 12, 0, "No artifacts"),
            ("duplicate", 1, 0, "Multiple artifacts"),
            ("error", 1, 0, "lookup failure"),
            ("post500", 1, 1, "HTTP 500"),
        ]:
            with self.subTest(mode=mode):
                run = subprocess.run(["node", "-e", harness, mode], capture_output=True, text=True, check=True)
                result = json.loads(run.stdout)
                self.assertEqual((result["calls"], result["posts"]), (calls, posts))
                self.assertIn(message, result["error"])

    def test_patch_rejects_changed_already_patched_or_nonunique_inputs(self):
        spec = importlib.util.spec_from_file_location("patch_deploy_pages", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        data = FIXTURE.encode()
        digest = hashlib.sha256(data).hexdigest()
        patched = module.patch_bundle(data, digest)
        for invalid, expected in [(data + b'x', digest), (patched, digest),
                                  (data + data, hashlib.sha256(data + data).hexdigest())]:
            with self.subTest(length=len(invalid)), self.assertRaises(ValueError):
                module.patch_bundle(invalid, expected)

    def test_patcher_changes_trigger_validation_and_main_deployment(self):
        workflow = (ROOT / '.github/workflows/pages.yml').read_text()
        validation = (ROOT / '.github/workflows/pages-checks.yml').read_text()
        self.assertIn('.github/scripts/patch_deploy_pages.py', workflow)
        self.assertEqual(validation.count('.github/scripts/patch_deploy_pages.py'), 2,
                         'Dev push and PR filters must both include the patcher')

    def test_workflow_pins_and_verifies_action_in_locked_job(self):
        workflow = (ROOT / '.github/workflows/pages.yml').read_text()
        self.assertEqual(workflow.count('  deploy:\n'), 1)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn('group: pages', workflow)
        self.assertIn('name: github-pages', workflow)
        self.assertIn('repository: actions/deploy-pages', workflow)
        self.assertIn('ref: 368f82528645a54fb793d4d04e342629a3f51346', workflow)
        self.assertIn('python3 production/.github/scripts/patch_deploy_pages.py deploy-pages-action', workflow)
        self.assertLess(workflow.index('name: Verify and patch artifact lookup'), workflow.index('uses: ./deploy-pages-action'))
