"""Published source-list and citation contracts; no third-party dependencies."""

from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "site/dist"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
# Orientation-only pages are an explicit exception, not an implicit bypass for
# newly added pages. Every other published page must satisfy the source contract.
ORIENTATION_ONLY_PAGES = {"index.html"}
MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


class Element:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag = tag
        self.attrs = dict(attrs)
        self.parent = parent
        self.children = []

    def elements(self, tag=None):
        for child in self.children:
            if isinstance(child, Element):
                if tag is None or child.tag == tag:
                    yield child
                yield from child.elements(tag)

    def text(self, exclude=None):
        if self is exclude:
            return ""
        return " ".join(child.text(exclude) if isinstance(child, Element) else child for child in self.children)

    def has_class(self, name):
        return name in self.attrs.get("class", "").split()


class Document(HTMLParser):
    def __init__(self, raw):
        super().__init__(convert_charrefs=True)
        self.root = Element("document")
        self.stack = [self.root]
        self.feed(raw)
        self.close()

    def handle_starttag(self, tag, attrs):
        element = Element(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(element)
        if tag not in VOID:
            self.stack.append(element)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def normalise(text):
    return " ".join(text.split())


def bibliography_label(text):
    """Recognise bibliography labels, not prose that merely mentions sources."""
    label = normalise(re.sub(r"[-_]", " ", text)).casefold().rstrip(":")
    if label == "section attribution and adaptations":
        return True
    return re.fullmatch(
        r"(?:(?:additional|selected|research|external|further|learning|supporting) )?"
        r"(?:sources?|references?|bibliography|bibliographies|further reading|reading list)"
        r"(?: (?:list|listing|and references|and sources|and further reading|and scope"
        r"|and learning references|and maintenance records))?",
        label,
    ) is not None


def statically_hidden(node):
    """Reject explicit hiding only; computed CSS visibility is a browser check."""
    while node is not None:
        attrs = node.attrs
        if ("hidden" in attrs or attrs.get("aria-hidden", "").strip().casefold() == "true"
                or attrs.get("aria-expanded", "").strip().casefold() == "false"
                or (node.tag == "details" and "open" not in attrs)):
            return True
        style = re.sub(r"/\*.*?\*/", "", attrs.get("style", ""), flags=re.S)
        for declaration in style.split(";"):
            property_name, separator, value = declaration.partition(":")
            if not separator:
                continue
            property_name = property_name.strip().casefold()
            value = re.sub(r"\s*!important\s*$", "", value, flags=re.I).strip().casefold()
            if ((property_name == "display" and value == "none")
                    or (property_name == "visibility" and value in {"hidden", "collapse"})
                    or (property_name == "content-visibility" and value == "hidden")
                    or (property_name == "opacity" and re.fullmatch(r"(?:0+(?:\.0*)?|\.0+)", value))):
                return True
        node = node.parent
    return False


class SourceListingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.documents = {
            path.relative_to(DIST).as_posix(): Document(path.read_text())
            for path in sorted(DIST.rglob("*.html"))
        }
        cls.source_pages = set(cls.documents) - ORIENTATION_ONLY_PAGES

    def test_one_final_sources_section_and_one_complete_numbered_list(self):
        for name in sorted(self.source_pages):
            with self.subTest(page=name):
                doc = self.documents[name]
                sections = [node for node in doc.root.elements("section") if node.attrs.get("id") == "sources"]
                self.assertEqual(len(sections), 1)
                section = sections[0]
                canonical_nodes = {section, *section.elements()}
                for node in canonical_nodes:
                    self.assertFalse(statically_hidden(node), "Sources must not be explicitly hidden or collapsed")
                for node in doc.root.elements():
                    if node in canonical_nodes:
                        continue
                    if node.tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
                        self.assertFalse(bibliography_label(node.text()), "Parallel bibliography heading outside Sources")
                    if node.tag in {"section", "div", "aside", "ol", "ul", "table", "nav"}:
                        labels = [node.attrs.get("id", ""), node.attrs.get("aria-label", "")]
                        labels += node.attrs.get("class", "").split()
                        self.assertFalse(any(bibliography_label(label) for label in labels),
                                         "Parallel bibliography container outside Sources")
                headings = [node for node in section.elements() if node.tag in {"h1", "h2", "h3", "h4", "h5", "h6"}]
                self.assertEqual([(node.tag, normalise(node.text())) for node in headings], [("h2", "Sources")])
                lists = [node for node in doc.root.elements() if node.has_class("source-list")]
                self.assertEqual(len(lists), 1)
                self.assertIn(lists[0], canonical_nodes)
                self.assertEqual(lists[0].tag, "ol")
                self.assertNotIn("reversed", lists[0].attrs, "Bibliography numbering must run forwards")
                self.assertTrue(any(child.tag == "li" for child in lists[0].elements("li")))
                structure = [node for node in section.children if isinstance(node, Element)]
                self.assertEqual([node.tag for node in structure], ["h2", "p", "ol"])
                self.assertTrue(structure[1].has_class("source-check-date"))
                self.assertEqual([node.tag for node in section.elements() if node.tag in ("ol", "ul")], ["ol"])
                self.assertFalse(any(node.has_class("source-attribution-notes") for node in doc.root.elements()))
                parent = section.parent
                assert parent is not None
                siblings = [node for node in parent.children if isinstance(node, Element)]
                later = siblings[siblings.index(section) + 1:]
                self.assertFalse(any(node.tag == "section" for node in later), "Sources must be the final content section")
                self.assertTrue(any(node.tag == "footer" for node in later), "Sources belongs before the article footer")
                for nav in doc.root.elements("nav"):
                    if nav.attrs.get("aria-label") == "On this page":
                        links = [node for node in nav.elements("a") if node.attrs.get("href") == "#sources"]
                        self.assertEqual([normalise(node.text()) for node in links], ["Sources"])

    def test_one_recorded_reference_check_date_without_per_source_dates(self):
        month = "(?:" + "|".join(name[:3] + "(?:" + name[3:] + ")?" for name in MONTHS) + ")"
        calendar_date = (
            r"(?:\d{4}[-/.]\d{1,2}[-/.]\d{1,2}"
            r"|\d{1,2}[-/.\s]+(?:\d{1,2}|" + month + r")[-/.\s,]+\d{4}"
            r"|" + month + r"\s+\d{1,2},?\s+\d{4})"
        )
        punctuation = r"[\s:;,.()\[\]–—-]*"
        check_date = re.compile(
            r"\b(?:checked|rechecked|accessed|retrieved|referenced)\b" + punctuation
            + r"(?:(?:on|as of)\b" + punctuation + r")?" + calendar_date + r"\b", re.I,
        )
        for name in sorted(self.source_pages):
            with self.subTest(page=name):
                doc = self.documents[name]
                dates = [node for node in doc.root.elements("p") if node.has_class("source-check-date")]
                self.assertEqual(len(dates), 1)
                paragraph = dates[0]
                parent = paragraph.parent
                assert parent is not None
                self.assertEqual(parent.attrs.get("id"), "sources")
                self.assertTrue(normalise(paragraph.text()).startswith("References last checked:"))
                times = list(paragraph.elements("time"))
                if normalise(paragraph.text()).rstrip(".") == "References last checked: not recorded":
                    self.assertEqual(times, [])
                else:
                    self.assertEqual(len(times), 1)
                    self.assertRegex(times[0].attrs.get("datetime", ""), r"^\d{4}-\d{2}-\d{2}$")
                    try:
                        recorded = date.fromisoformat(times[0].attrs["datetime"])
                    except ValueError:
                        self.fail("Reference-check datetime must be a real calendar date")
                    displayed = f"{recorded.day} {MONTHS[recorded.month - 1]} {recorded.year:04d}"
                    self.assertEqual(normalise(times[0].text()), displayed,
                                     "Displayed reference-check date must match datetime (D Month YYYY)")
                self.assertIsNone(check_date.search(normalise(doc.root.text(exclude=paragraph))),
                                  "Remove individual reference-check dates, not publication dates")

    def test_citation_numbers_and_aria_labels_match_their_canonical_entry(self):
        for name in sorted(self.source_pages):
            with self.subTest(page=name):
                doc = self.documents[name]
                sources = next((node for node in doc.root.elements() if node.attrs.get("id") == "sources"), None)
                if sources is None:
                    self.fail("Missing Sources section")
                listing = next((node for node in sources.elements("ol") if node.has_class("source-list")), None)
                if listing is None:
                    self.fail("Missing ordered source list")
                self.assertNotIn("reversed", listing.attrs, "Bibliography numbering must run forwards")
                targets = {}
                number = int(listing.attrs.get("start", 1))
                for entry in [child for child in listing.children if isinstance(child, Element) and child.tag == "li"]:
                    number = int(entry.attrs.get("value", number))
                    for node in [entry, *entry.elements()]:
                        if "id" in node.attrs:
                            targets[node.attrs["id"]] = number
                    number += 1
                for link in doc.root.elements("a"):
                    fragment = link.attrs.get("href", "")
                    if fragment.startswith("#source-"):
                        self.assertIn(fragment[1:], targets, fragment)
                        number = targets[fragment[1:]]
                        for displayed in re.findall(r"\[(\d+)\]", link.text()):
                            self.assertEqual(int(displayed), number, f"{fragment}: {link.text()}")
                        label = re.match(r"Source (\d+):", link.attrs.get("aria-label", ""))
                        if label:
                            self.assertEqual(int(label[1]), number, fragment)

    def test_each_source_url_has_one_canonical_list_entry(self):
        for name in sorted(self.source_pages):
            with self.subTest(page=name):
                doc = self.documents[name]
                listing = next((node for node in doc.root.elements("ol") if node.has_class("source-list")), None)
                self.assertIsNotNone(listing)
                assert listing is not None
                owners = {}
                for entry in [node for node in listing.children if isinstance(node, Element) and node.tag == "li"]:
                    for link in entry.elements("a"):
                        url = link.attrs.get("href", "")
                        if url.startswith(("https://", "http://")):
                            self.assertIs(owners.setdefault(url, entry), entry, f"Duplicate bibliography entry: {url}")

    def test_moved_source_aliases_have_desktop_and_mobile_header_offsets(self):
        styles = (DIST / "styles.css").read_text()
        self.assertIn(".source-list [id] { scroll-margin-top: 5rem; }", styles)
        self.assertRegex(
            styles,
            r"@media \(max-width: 1099px\)\s*\{[^}]*\}[^}]*\.source-list \[id\] \{ scroll-margin-top: 9rem; \}",
        )

    def test_all_page_ids_and_local_fragments_remain_unambiguous(self):
        targets = {}
        for name, doc in self.documents.items():
            ids = [node.attrs["id"] for node in doc.root.elements() if "id" in node.attrs]
            self.assertEqual(len(ids), len(set(ids)), f"Duplicate ID on {name}")
            targets[name] = set(ids)
        for name, doc in self.documents.items():
            for node in doc.root.elements():
                for attribute in ("aria-labelledby", "aria-describedby"):
                    for identifier in node.attrs.get(attribute, "").split():
                        self.assertIn(identifier, targets[name], f"{name}: {attribute}={identifier}")
            for link in doc.root.elements("a"):
                target = urlsplit(link.attrs.get("href", ""))
                if target.scheme or target.netloc or not target.fragment:
                    continue
                path = unquote(target.path)
                page = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)).lstrip("/") if path else name
                if path.endswith("/"):
                    page = posixpath.join(page, "index.html")
                if page.endswith(".html"):
                    self.assertIn(page, targets, f"{name}: unknown local page {link.attrs.get('href')}")
                if page in targets:
                    self.assertIn(unquote(target.fragment), targets[page], f"{name}: {link.attrs.get('href')}")


if __name__ == "__main__":
    unittest.main()
