"""Give every language its own search index.

mkdocs-static-i18n merges all languages into one search/search_index.json, so a search in the
French site also returns English and Italian pages. After the build this hook splits that file:
the root index keeps only the default language, and each other language gets
<lang>/search/search_index.json with its locations relative to <lang>/.
overrides/main.html points the search of each language at its own index.
"""
import json
import os

from mkdocs.plugins import event_priority


@event_priority(-100)  # after the search plugin has written the merged index
def on_post_build(config):
    i18n = config.plugins.get("i18n")
    if not i18n:
        return
    languages = [(lang.locale, lang.default) for lang in i18n.config.languages]
    others = [loc for loc, default in languages if not default]

    path = os.path.join(config.site_dir, "search", "search_index.json")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as f:
        index = json.load(f)

    def language_of(doc):
        first = doc["location"].split("/", 1)[0]
        return first if first in others else None

    if not any(language_of(doc) for doc in index["docs"]):
        return  # already split, or a sub-build without the other languages

    for loc in others:
        docs = []
        for doc in index["docs"]:
            if language_of(doc) == loc:
                docs.append({**doc, "location": doc["location"].split("/", 1)[1] if "/" in doc["location"] else ""})
        out_dir = os.path.join(config.site_dir, loc, "search")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "search_index.json"), "w", encoding="utf-8") as f:
            json.dump({**index, "config": {**index["config"], "lang": [loc]}, "docs": docs}, f, ensure_ascii=False)

    default_docs = [doc for doc in index["docs"] if language_of(doc) is None]
    with open(path, "w", encoding="utf-8") as f:
        json.dump({**index, "config": {**index["config"], "lang": [next(l for l, d in languages if d)]}, "docs": default_docs}, f, ensure_ascii=False)
