# Validation record — 2026-11-22

## Executed checks

- Full site generated with Jekyll 3.10.0 using the repository configuration, templates, collections, and configured plugins. A temporary portable Ruby 3.3.10 runtime was used; no global Ruby installation or publishing action was performed. The one-shot build called `Jekyll::Site#process`; live-reload/server native dependencies were not required. This is not a locked GitHub Pages deployment reproduction.
- 39 series pages checked in the generated site at 1360px and 390px: no broken body images, MathJax errors, residual dollar delimiters, or document-level horizontal overflow.
- Source frontmatter, route uniqueness, internal links, local assets, code fences, and SVG XML checked.
- Figures rendered in Chromium; key desktop and mobile page screenshots inspected. Inline restriction bars and escaped set braces were corrected after real Jekyll rendering exposed Markdown parsing errors.
- Eight workbench tests passed, covering alternatives, unsupported cycles, conditional scope, evidence policy, stale reviews, persistence and changed content, joint premises, and the explicit mathematical trust-boundary fixture.
- `ledger.py` and `workbench.py` demonstrations executed successfully. Relevant tracked changes pass `git diff --check`.

## What these checks do not establish

The code does not verify mathematics or authenticate reviewers. Fixture evidence is stipulated. No external mathematical referee or formalization pass was performed on the series. Primary-source records were checked for the architectural descriptions used; this is not an audit of every proof in the cited papers. Historical Danus/Rethlas endpoint descriptions are labelled as snapshot notes rather than current API guarantees.

## Reader entry points

Start with the series guide, design principles, three running cases, and the eight-stage laboratory. Keep source provenance, evidence category, and unresolved assumptions visible when extending the project.
