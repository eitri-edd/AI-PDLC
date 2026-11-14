# Security policy

This repository holds a public, static documentation site published with GitHub Pages. It has no backend, accounts or user data. See [SECURITY_MODEL.md](SECURITY_MODEL.md) for the threat model.

## Reporting a vulnerability

Report suspected vulnerabilities privately through [GitHub private vulnerability reporting](https://github.com/eitri-edd/AI-PDLC/security/advisories/new). Do not open a public issue.

Relevant reports include:
- ways to change the published site without maintainer approval;
- issues in the GitHub Actions workflows or `.github/scripts/` that could expose deploy permissions;
- script injection in the site's pages or JavaScript.

We aim to acknowledge reports within five working days.
