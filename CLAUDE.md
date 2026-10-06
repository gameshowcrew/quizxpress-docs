# QuizXpress online documentation

This repo is the QuizXpress user manual, published at **https://docs.quizxpress.com**.
It replaced the Word manual (User Manual QuizXpress 8.6.docx). The Word file is no longer maintained:
this repo is the single source of truth.

- GitHub: `gameshowcrew/quizxpress-docs` (public, branch `main`)
- Local clone on Bart's PC: `C:\Users\bart_\source\repos\quizxpress-docs`
- Built with MkDocs Material. Pages are Markdown in `docs/`, menu in `mkdocs.yml` (`nav:`).

## Publishing

Every push to `main` builds and publishes the site through `.github/workflows/deploy.yml`
(GitHub Actions → GitHub Pages, about a minute). **A push is immediately public**: confirm the
change with the user before pushing unless they already asked for it.

Before pushing, run `mkdocs build --strict` (needs `pip install -r requirements.txt`). It fails on
broken links, broken anchors and missing images, which is the main safety net. Always
`git pull` first; the user and Claude sessions both push to `main`.

## Where things go

| Area of the product | Folder | Menu tab |
|---|---|---|
| Installation, licensing, updates | `docs/installation/` | Getting started |
| Quiz Studio (designing quizzes) | `docs/studio/` | Studio |
| Slide / game types (Question, Wager, Bingo, Trivia Feud…) | `docs/studio/slide-and-game-formats/` | Studio |
| Mini games (Horse race, Rope Rumble, Auction…) | `docs/studio/mini-games/` | Studio |
| Multimedia (pictures, sound, video, charts, word game) | `docs/studio/adding-multimedia-content/` | Studio |
| Ribbon, property grid, other Studio UI | `docs/studio/user-interface-overview/`, `docs/studio/other-functionality/` | Studio |
| Quiz Setup (buzzers, mobile, teams, sounds, screens, advanced) | `docs/setup/` | Setup |
| Quiz Live (running the show, screens, keyboard control) | `docs/live/` | Live |
| Mobile keypads, Smart Buzzer app, buzzerpad website | `docs/live/using-mobile-keypads/` | Live |
| QuizXpress Director | `docs/live/quizxpress-director/` | Live |
| Message Broker (MIDI/DMX, IP inbound/outbound) | `docs/advanced/message-broker/` | Advanced |
| Scripting (JavaScript engine) | `docs/advanced/scripting/` | Advanced |
| Other advanced features: recovery mode, custom data fields, skinning | `docs/advanced/` | Advanced |
| Solo, Analyzer, troubleshooting, hardware, legal | `docs/solo.md`, `docs/analyzer/`, `docs/troubleshooting/`, `docs/hardware-installation/`, `docs/legal/` | More |

Find the existing page for a feature with a search before creating a new one:
`grep -ril "wager" docs/`.

New advanced features or converted feature documents get their own group under the **Advanced**
tab: a folder `docs/advanced/<feature>/` with an `index.md` overview, listed in `nav:` under
`- Advanced:`.

## Writing conventions

- One page per task or feature; the page's `# Heading` is its title. Use `##`/`###` inside.
- **New page** → also add it to `nav:` in `mkdocs.yml` at the right place, or it won't appear in the menu.
- Links between pages are relative to the `.md` file: `[Bingo round](../slide-and-game-formats/bingo-round.md#claim-handling)`.
  Anchors are the heading in lowercase with hyphens.
- External links open in a new tab automatically (`docs/javascripts/external-links.js`); write them normally.
- Notes and tips: an admonition, body indented 4 spaces:

  ```
  !!! note
      Bingo requires the optional Bingo module.
  ```

  (`!!! tip`, `!!! warning` also work.)
- Keyboard keys and UI labels: put UI labels in quotes ('Question Type'), as the existing pages do.
- Write for quizmasters, not developers: what the feature does and how to use it, not how it's coded.

## Screenshots

- Store in `docs/assets/images/` as **WebP at full resolution, quality ~95**. Readability matters more
  than file size. Use a descriptive name for new ones (`bingo-claim-dialog.webp`), not `imageNNN`.
- Full-window screenshots: no width, so they fill the column: `![Bingo claim dialog](../../assets/images/bingo-claim-dialog.webp){ loading=lazy }`
- Small dialogs/buttons: give a display width: `![...](...){ width="300" loading=lazy }`
- Readers can click any screenshot to enlarge it (`docs/javascripts/image-zoom.js`).
- Claude can't take screenshots of the app itself. When a new screenshot is needed, write the text,
  and tell the user exactly which screenshot to make and where it goes. Don't publish placeholder text
  like "screenshot here".

## Don't

- Don't add `repo_url`/`edit_uri` or the `content.action.edit` feature: customers must not see
  edit links.
- Don't upgrade to MkDocs 2.x (`requirements.txt` pins `mkdocs<2`); it breaks Material.
- Don't put files in `docs/` that aren't meant to be public.
