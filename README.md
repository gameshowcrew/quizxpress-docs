# QuizXpress documentation

The QuizXpress user manual as a website, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
Every page is a Markdown file in `docs/`; the menu is defined in `mkdocs.yml`.

## Preview on your own computer

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000. The preview reloads as soon as you save a file.

## Editing

| You want to…            | Do this |
|-------------------------|---------|
| Fix or update text      | Edit the `.md` file in `docs/`. |
| Add a screenshot        | Put it in `docs/assets/images/` (WebP or PNG) and reference it: `![Alt text](../assets/images/my-shot.webp){ width="600" }` |
| Add a page              | Create the `.md` file and add it to `nav:` in `mkdocs.yml`. |
| Add a note / tip box    | `!!! note` or `!!! tip` on its own line, then the text indented by 4 spaces. |

Before pushing, `mkdocs build --strict` catches broken links and missing images.

## Publishing

Every push to `main` builds the site and publishes it to GitHub Pages
(`.github/workflows/deploy.yml`). One-time setup in the GitHub repo:
**Settings → Pages → Source: GitHub Actions**.

For a custom domain such as `docs.quizxpress.com`: add a file `docs/CNAME` containing just that
domain, set the same domain under Settings → Pages, and add a CNAME DNS record pointing to
`<your-account>.github.io`. Then set `site_url` in `mkdocs.yml`.

GitHub Pages from a **private** repo needs a paid GitHub plan. With a free plan, either make the
repo public or connect it to Cloudflare Pages instead (build command `pip install -r requirements.txt && mkdocs build`, output folder `site`).

## Source

Converted from *User Manual QuizXpress 8.6.docx*. Images were converted to WebP and resized for the
web (134 MB → 13 MB).
