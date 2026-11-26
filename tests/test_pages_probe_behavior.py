"""Execute the real Pages artifact probe with deterministic Node API doubles."""

import json
from pathlib import Path
import subprocess
import textwrap
import unittest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/pages.yml"


def run_probe(scenario):
    workflow = WORKFLOW.read_text()
    script = workflow.split("          script: |\n", 1)[1].split("\n      - id: deployment", 1)[0]
    script = textwrap.dedent(script)
    harness = r'''
const script = JSON.parse(process.argv[1]);
const scenario = process.argv[2];
const secret = 'sensitive-test-token';
process.env.ACTIONS_RUNTIME_TOKEN = 'header.' + Buffer.from(JSON.stringify({scp:'Actions.Results:run:job'})).toString('base64url') + '.' + secret;
process.env.ACTIONS_RESULTS_URL = 'https://results.example.test/path';
const logs = [], timeouts = [], sleeps = [];
let calls = 0;
const originalLog = console.log;
console.log = (...args) => logs.push(args.join(' '));
globalThis.AbortSignal = {timeout(ms) {
  timeouts.push(ms);
  const controller = new AbortController();
  queueMicrotask(() => controller.abort());
  return controller.signal;
}};
globalThis.setTimeout = (fn, ms) => { sleeps.push(ms); queueMicrotask(fn); };
globalThis.fetch = async (url, options) => {
  calls++;
  if (!options.signal) throw new Error('MISSING_ABORT_SIGNAL');
  if (scenario === 'hung') {
    return new Promise((resolve, reject) => {
      options.signal.addEventListener('abort', () => reject(Object.assign(new Error(secret), {name:'TimeoutError'})));
    });
  }
  if (scenario === 'eventual') {
    if (calls === 1) return {status:503, ok:false};
    return {status:200, ok:true, json:async () => ({artifacts: calls === 2 ? [] : [{name:'github-pages'}]})};
  }
  if (scenario === 'duplicates') {
    return {status:200, ok:true, json:async () => ({artifacts:[{name:'github-pages'}, {name:'github-pages'}]})};
  }
  if (scenario === 'body-hung') {
    return {status:200, ok:true, json:() => new Promise((resolve, reject) => {
      if (options.signal.aborted) reject(Object.assign(new Error(secret), {name:'TimeoutError'}));
      else options.signal.addEventListener('abort', () => reject(Object.assign(new Error(secret), {name:'TimeoutError'})));
    })};
  }
  throw new Error('unexpected scenario');
};
(async () => {
  let error = null;
  try { await new (Object.getPrototypeOf(async function(){}).constructor)(script)(); }
  catch (e) { error = e.message; }
  originalLog(JSON.stringify({calls, timeouts, sleeps, logs, error, token:process.env.ACTIONS_RUNTIME_TOKEN}));
})();
'''
    result = subprocess.run(
        ["node", "-e", harness, json.dumps(script), scenario],
        capture_output=True, text=True, timeout=5, check=True,
    )
    return json.loads(result.stdout)


class PagesProbeBehaviorTests(unittest.TestCase):
    def test_hung_requests_abort_on_each_attempt_and_eventually_fail(self):
        result = run_probe("hung")
        self.assertEqual(result["timeouts"], [10000] * 12)
        self.assertEqual(result["calls"], 12)
        self.assertEqual(result["sleeps"], [5000] * 11)
        self.assertIn("175 seconds", result["error"])
        self.assertNotIn(result["token"], json.dumps(result["logs"]))
        self.assertNotIn("sensitive-test-token", json.dumps(result["logs"]))

    def test_transient_http_error_and_absence_then_success(self):
        result = run_probe("eventual")
        self.assertIsNone(result["error"])
        self.assertEqual(result["calls"], 3)
        self.assertEqual(result["timeouts"], [10000] * 3)
        self.assertEqual(result["sleeps"], [5000] * 2)
        self.assertIn("HTTP 503", result["logs"][0])
        self.assertIn("0 matching artifact(s)", result["logs"][1])
        self.assertNotIn(result["token"], json.dumps(result["logs"]))

    def test_duplicate_artifacts_never_allow_deployment(self):
        result = run_probe("duplicates")
        self.assertEqual(result["calls"], 12)
        self.assertEqual(result["timeouts"], [10000] * 12)
        self.assertEqual(result["sleeps"], [5000] * 11)
        self.assertIn("175 seconds", result["error"])
        self.assertTrue(all("2 matching artifact(s)" in log for log in result["logs"]))
        self.assertNotIn(result["token"], json.dumps(result["logs"]))

    def test_stalled_response_body_is_aborted_too(self):
        result = run_probe("body-hung")
        self.assertEqual(result["calls"], 12)
        self.assertEqual(result["timeouts"], [10000] * 12)
        self.assertEqual(result["sleeps"], [5000] * 11)
        self.assertIn("175 seconds", result["error"])
        self.assertNotIn("sensitive-test-token", json.dumps(result["logs"]))


if __name__ == "__main__":
    unittest.main()
