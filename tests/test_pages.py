"""Regression tests for the combined static Pages artefact (standard library only)."""

from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import urlopen


SCRIPT = Path(__file__).resolve().parents[1] / ".github/scripts/assemble_pages.py"


class PagesAssemblyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.main = self.root / "main"
        self.dev = self.root / "dev"
        self.output = self.root / "public"
        for source, label in ((self.main, "production"), (self.dev, "preview")):
            (source / "assets").mkdir(parents=True)
            (source / "index.html").write_text(f'<a href="page.html">{label}</a>')
            (source / "page.html").write_text(label)
            (source / "assets/logo.png").write_bytes(label.encode())
            (source / ".nojekyll").touch()

    def assemble(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.main), str(self.dev), str(self.output)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_combines_dist_trees_without_changing_their_bytes(self):
        result = self.assemble()
        self.assertEqual(result.returncode, 0, result.stderr)
        for source, destination in ((self.main, self.output), (self.dev, self.output / "dev")):
            for path in source.rglob("*"):
                if path.is_file():
                    self.assertEqual((destination / path.relative_to(source)).read_bytes(), path.read_bytes())
        self.assertNotEqual((self.output / "index.html").read_bytes(), (self.output / "dev/index.html").read_bytes())

    def test_actual_site_pages_and_assets_serve_at_both_url_prefixes(self):
        # The deployment changes must not require a base URL rewrite or build.
        self.main = self.dev = SCRIPT.parents[2] / "site/dist"
        self.output = self.root / "AI-PDLC"
        result = self.assemble()
        self.assertEqual(result.returncode, 0, result.stderr)
        handler = partial(SimpleHTTPRequestHandler, directory=str(self.root))
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            base = f"http://127.0.0.1:{server.server_port}/AI-PDLC/"
            files = sorted(path for path in self.main.rglob("*") if path.is_file())
            for prefix in ("", "dev/"):
                for path in files:
                    relative = path.relative_to(self.main).as_posix()
                    with self.subTest(url=prefix + relative):
                        with urlopen(base + prefix + relative, timeout=5) as response:
                            self.assertEqual(response.status, 200)
                            self.assertEqual(response.read(), path.read_bytes())
                with urlopen(base + prefix, timeout=5) as response:
                    self.assertEqual(response.read(), (self.main / "index.html").read_bytes())
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

    def assert_rejected_before_copy(self):
        result = self.assemble()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists(), result.stderr)

    def test_missing_dev_index_fails_before_creating_an_output(self):
        (self.dev / "index.html").unlink()
        self.assert_rejected_before_copy()

    def test_directory_index_fails_before_creating_an_output(self):
        (self.dev / "index.html").unlink()
        (self.dev / "index.html").mkdir()
        self.assert_rejected_before_copy()

    def test_symlink_fails_before_creating_an_output(self):
        (self.dev / "linked.html").symlink_to(self.main / "index.html")
        self.assert_rejected_before_copy()

    def test_reserved_dev_path_fails_before_creating_an_output(self):
        (self.main / "dev").mkdir()
        self.assert_rejected_before_copy()

    def test_existing_output_is_not_reused_or_modified(self):
        self.output.mkdir()
        (self.output / "stale.html").write_text("do not overwrite")
        result = self.assemble()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual([path.name for path in self.output.iterdir()], ["stale.html"])
        self.assertEqual((self.output / "stale.html").read_text(), "do not overwrite")


class DocumentReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        self.references.extend(
            value for name, value in attrs if name in ("href", "src") and value
        )


class PagesSiteLinksTests(unittest.TestCase):
    def test_navigation_and_assets_resolve_within_each_url_prefix(self):
        source = SCRIPT.parents[2] / "site/dist"
        for prefix in ("/AI-PDLC/", "/AI-PDLC/dev/"):
            for page in sorted(source.glob("*.html")):
                parser = DocumentReferences()
                parser.feed(page.read_text())
                for reference in parser.references:
                    target = urlsplit(urljoin("http://localhost" + prefix + page.name, reference))
                    if target.scheme != "http" or target.netloc != "localhost":
                        continue
                    with self.subTest(prefix=prefix, page=page.name, reference=reference):
                        self.assertTrue(target.path.startswith(prefix), "Link escapes branch prefix")
                        local = source / unquote(target.path[len(prefix):])
                        self.assertTrue(local.exists(), f"Missing local target: {local}")


class PagesWorkflowTests(unittest.TestCase):
    def test_rejected_events_cannot_displace_pending_deployments(self):
        workflow = (SCRIPT.parents[1] / "workflows/pages.yml").read_text()
        # A workflow-level lock is acquired even when deploy's `if` is false.
        # Only eligible deploy jobs may contend for the shared Pages queue.
        self.assertNotIn("\nconcurrency:", workflow)
        self.assertIn(
            "\n    concurrency:\n      group: pages\n      cancel-in-progress: false\n",
            workflow,
        )


if __name__ == "__main__":
    unittest.main()
