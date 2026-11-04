#!/usr/bin/env python3
"""Check every internal link and image of the built site, including links in raw HTML.

`mkdocs build --strict` only validates Markdown links. Run this after a build:

    mkdocs build && python tools/check-links.py [site-dir]

Exit code 1 when a link points to a missing page, image or #anchor.
"""
import os
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urldefrag, urlparse

SITE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "site")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs = set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        for key in ("href", "src"):
            if a.get(key) and tag in ("a", "img", "source", "video", "audio"):
                self.refs.append(a[key])


pages = {}
for root, _, files in os.walk(SITE):
    for name in files:
        if name.endswith(".html"):
            path = os.path.join(root, name)
            parser = Page()
            with open(path, encoding="utf-8") as f:
                parser.feed(f.read())
            pages[path] = parser

broken = 0
for path, page in sorted(pages.items()):
    for ref in page.refs:
        parsed = urlparse(ref)
        if parsed.scheme or parsed.netloc or ref.startswith(("mailto:", "tel:", "javascript:", "data:")):
            continue
        url, fragment = urldefrag(ref)
        if url:
            if url.startswith("/"):  # root-relative (language switcher)
                target = os.path.normpath(os.path.join(SITE, unquote(url).lstrip("/")))
            else:
                target = os.path.normpath(os.path.join(os.path.dirname(path), unquote(url)))
            if os.path.isdir(target):
                target = os.path.join(target, "index.html")
        else:
            target = path
        problem = None
        if not os.path.isfile(target):
            problem = "missing file"
        elif fragment and target.endswith(".html") and unquote(fragment) not in pages[target].ids:
            problem = "missing anchor"
        if problem:
            broken += 1
            print(f"{os.path.relpath(path, SITE)}: {problem}: {ref}")

print(f"{sum(len(p.refs) for p in pages.values())} links checked in {len(pages)} pages, {broken} broken")
sys.exit(1 if broken else 0)
