# Threat model: eitri-edd/AI-PDLC

## System overview and trust boundaries
AI-PDLC is a static documentation handbook (the EDS AI-SDLC knowledge site): hand-written HTML/CSS/JS in `site/dist/`, published to GitHub Pages. It has no backend, no authentication, no forms that submit anywhere, no user accounts, and no stored user data.

Publishing (`.github/workflows/pages.yml`):
- A push to `main` deploys `main:site/dist` to the Pages root.
- When `Validate Pages` passes on a push to `dev`, a `workflow_run` deploy publishes `dev:site/dist` under `/dev/`. The deploy job runs only from `main`'s workflow and `main`'s `assemble_pages.py`, checks out `dev` sparsely (`site/dist` only), and never executes dev scripts or downloads dev artifacts.
- The `github-pages` environment is restricted to `main`. The deploy job holds `pages: write` and `id-token: write`.

Validation (`.github/workflows/pages-checks.yml`): runs on pushes to `dev` and on PRs to `main`, with `contents: read` and `persist-credentials: false`. It runs `python3 -m unittest` over `tests/` and runs `assemble_pages.py` without deploying.

Trust boundaries:
1. Outside contributors (fork PRs) → the CI that runs their code.
2. The `dev` / `main` branch content → the public Pages site.
3. The public site → visitors' browsers, which load third-party Google Fonts.

## Components
| Component | Covers |
|---|---|
| Site content | `site/dist/*.html`, `*.css`, `assets/`, `favicon.svg` |
| Client JS | `site/dist/site.js`, `product-discovery.js`, `product-implementation.js`, `transformation.js` |
| Publishing pipeline | `.github/workflows/pages.yml`, `.github/workflows/pages-checks.yml`, `.github/scripts/assemble_pages.py` |
| Tests and editorial tooling | `tests/`, `site/reference-checks.json` |
| Repo docs | root `*.md`, `site/*.md`, `scratch/` |

## Entry points and who can reach them
- **Public site URLs** (anyone): pages served by GitHub Pages. The client JS reads `location.hash` (`decodeURIComponent` → `getElementById`, which is used as an element lookup, not as HTML) and builds a skills filter. The `innerHTML` / `insertAdjacentHTML` calls in `site.js` use static strings in the code we've read so far.
- **Pushes to `dev` / `main`** (maintainers): publish to `/dev/` and to the root.
- **Pull requests to `main`**: run `pages-checks.yml` with the PR's code (tests and the assemble script) under a read-only token.
- **Workflow triggers**: `workflow_run` from `Validate Pages` on `dev`, and `workflow_dispatch` (both gated to `refs/heads/main`).

## Assets and data sensitivity
- **Integrity of the published site** (root and `/dev/`): the main asset, because defacement or injected script would run in visitors' browsers under the Pages origin.
- **The Pages deploy capability**: `pages: write` and the OIDC `id-token` in the deploy job, plus the `main`-only `github-pages` environment protection.
- **Repository integrity**: branches and workflows.
- **Content confidentiality: none.** *(User: the site and repo are public; nothing in them is confidential.)*

## Attacker profiles
- **Outside contributors via fork PRs: untrusted.** *(User: outside fork PRs are not trusted.)* They can get their code run in `pages-checks.yml`. What matters is whether that can get a write token, secrets, a deploy, or a cache/artifact that a trusted job later consumes.
- **Maintainers who push to `dev` / `main`: trusted, equally.** *(User: maintainers only; dev and main pushes are equally trusted.)* So a finding whose only attacker is someone who can already push to `dev`, such as "dev publishes to /dev/ without review", is within the trust the user grants.
- **Anonymous site visitors / link crafters**: can control the URL hash and query string, for example to attempt DOM XSS through the hash handling.
- **Supply chain**: third-party GitHub Actions pinned by tag (`actions/checkout@v4`, `upload-pages-artifact@v3`, `deploy-pages@v4`) and Google Fonts CSS/fonts loaded on every page.

## Existing controls
- Least-privilege workflow permissions (`contents: read` by default; deploy-only `pages`/`id-token`), with `persist-credentials: false` on every checkout.
- The deploy runs only `main`'s trusted script and copies only dev's `site/dist` static files. `assemble_pages.py` rejects symlinks, requires a regular `index.html`, reserves `/dev/`, and refuses to overwrite existing output.
- The deploy job's `if:` requires `refs/heads/main`, plus a successful push-event `workflow_run` from `dev` in the same repository (which excludes forks). Deploys are serialized by `concurrency: pages`.
- No external scripts: only same-origin JS. External `target="_blank"` links have no unsafe `rel` gaps (none found without `noopener`).

## Out of scope / accepted risk
- *(User: nothing is ruled out. Every finding counts, including Google Fonts / no CSP, the review markdown and `scratch/`, and `tests/`.)*
- No separate infrastructure repository exists. *(User: the GitHub Pages config in `.github/` is all of it.)*

## Open questions
- Branch protection on `main` / `dev` and the repo's Actions settings (fork-PR approval, default `GITHUB_TOKEN` permissions) aren't in the code. Their state is unknown.
