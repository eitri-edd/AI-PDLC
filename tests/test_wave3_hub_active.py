"""Runtime checks for the shared script's contents highlighting.

The Tech Scan sidebar group links were removed (they all pointed at anchors
on the hub page itself), along with the script block that synced their
``aria-current`` state. The "On this page" contents highlighting stays, and
the script must no longer query for the removed sidebar links.
"""
import subprocess
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'site/dist/site.js'

HARNESS = r'''
const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const [path, initial] = process.argv.slice(1);
function link(hash, current = null) {
  return {hash, current, getAttribute(name) { return name === 'href' ? 'tech-scan.html' + this.hash : this.current; },
    setAttribute(name, value) { if (name === 'aria-current') this.current = value; },
    removeAttribute(name) { if (name === 'aria-current') this.current = null; }};
}
const contents = link('#purpose');
const section = {id:'purpose', getBoundingClientRect: () => ({top:0})};
const queried = [];
const listeners = {};
const location = {pathname:path, hash:initial};
const document = {
  querySelector: selector => selector === '#purpose' ? section : null,
  querySelectorAll: selector => { queried.push(selector); return selector === '.page-contents a' ? [contents] : []; },
  documentElement:{scrollHeight:2000}
};
const window = {location, innerHeight:800, scrollY:0,
  matchMedia: () => ({matches:true}),
  addEventListener: (type, callback) => (listeners[type] ||= []).push(callback)};
const context = {document, window, location, ResizeObserver: class { observe() {} }, setTimeout, clearTimeout};
vm.runInNewContext(fs.readFileSync(process.env.SITE_SCRIPT, 'utf8'), context);
assert.strictEqual(contents.current, 'location');
assert.ok(!queried.includes('.sidebar a[href^="tech-scan.html#"]'));
function change(hash) { location.hash = hash; for (const fn of listeners.hashchange || []) fn(); }
change('#models-access');
assert.strictEqual(contents.current, 'location');
change('#purpose');
assert.strictEqual(contents.current, 'location');
'''

class HubActiveRuntimeTests(unittest.TestCase):
    def run_harness(self, path, initial):
        import os
        result = subprocess.run(['node', '-e', HARNESS, path, initial],
                                env={**os.environ, 'SITE_SCRIPT': str(SCRIPT)},
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_hub_deep_link_and_hash_changes(self):
        for path in ['/tech-scan.html', '/dev/tech-scan.html']:
            with self.subTest(path=path):
                self.run_harness(path, '#models-access')

    def test_spoke_pages_keep_contents_highlight(self):
        for path in ['/tech-scan-harness.html', '/dev/not-tech-scan.html']:
            with self.subTest(path=path):
                self.run_harness(path, '#models-access')

if __name__ == '__main__':
    unittest.main()
