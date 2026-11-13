"""Runtime checks for the shared script's Tech Scan sidebar state."""
import subprocess
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'site/dist/site.js'

HARNESS = r'''
const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const [path, initial, scenario] = process.argv.slice(1);
const ids = ['models-access', 'agent-environment', 'agents-workflows', 'verification-delivery'];
function link(hash, current = null) {
  return {hash, current, getAttribute(name) { return name === 'href' ? 'tech-scan.html' + this.hash : this.current; },
    setAttribute(name, value) { if (name === 'aria-current') this.current = value; },
    removeAttribute(name) { if (name === 'aria-current') this.current = null; }};
}
const groups = ids.map((id, i) => link('#' + id, scenario === 'spoke' && i === 1 ? 'location' : null));
const contents = link('#purpose');
const parent = link('', 'page');
const section = {id:'purpose', getBoundingClientRect: () => ({top:0})};
const listeners = {};
const location = {pathname:path, hash:initial};
const document = {
  querySelector: selector => selector === '#purpose' ? section : null,
  querySelectorAll: selector => selector === '.page-contents a' ? [contents] :
    selector === '.sidebar a[href^="tech-scan.html#"]' ? groups : [],
  documentElement:{scrollHeight:2000}
};
const window = {location, innerHeight:800, scrollY:0,
  matchMedia: () => ({matches:true}),
  addEventListener: (type, callback) => (listeners[type] ||= []).push(callback)};
const context = {document, window, location, ResizeObserver: class { observe() {} }, setTimeout, clearTimeout};
vm.runInNewContext(fs.readFileSync(process.env.SITE_SCRIPT, 'utf8'), context);
function expect(expected) {
  assert.deepStrictEqual(groups.filter(g => g.current === 'location').map(g => g.hash), expected ? [expected] : []);
  assert.strictEqual(parent.current, 'page');
  assert.strictEqual(contents.current, 'location');
}
function change(hash) { location.hash = hash; for (const fn of listeners.hashchange || []) fn(); }
if (scenario === 'spoke') { expect('#agent-environment'); change('#models-access'); expect('#agent-environment'); }
else {
  expect(initial);
  for (const id of ids) { change('#' + id); expect('#' + id); }
  change('#purpose'); expect(null);
  change(''); expect(null);
}
'''

class HubActiveRuntimeTests(unittest.TestCase):
    def run_harness(self, path, initial, scenario):
        import os
        result = subprocess.run(['node', '-e', HARNESS, path, initial, scenario],
                                env={**os.environ, 'SITE_SCRIPT': str(SCRIPT)},
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_hub_deep_link_and_hash_changes(self):
        for path in ['/tech-scan.html', '/dev/tech-scan.html']:
            with self.subTest(path=path):
                self.run_harness(path, '#models-access', 'hub')

    def test_spokes_preserve_static_selection(self):
        for path in ['/tech-scan-harness.html', '/dev/not-tech-scan.html']:
            with self.subTest(path=path):
                self.run_harness(path, '#models-access', 'spoke')

if __name__ == '__main__':
    unittest.main()
