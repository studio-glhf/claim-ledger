# Operations

## Weekly loop (agent)
1. Scan new papers (arXiv cs.RO) and releases from tracked VLA and robot-learning repos for headline claims with numbers.
2. Scan issues, forums and later papers for replication attempts of tracked claims.
3. Draft new or updated entries in `docs/data.json`. Run `python3 scripts/validate.py`.
4. Open a pull request for new entries; merge small evidence updates directly. Process correction issues.
5. The `weekly` workflow validates, link-checks and opens an issue if links broke; Pages serves docs/ from main directly.
6. Send the owner a short weekly summary: entries added, corrections handled, page views.

## What is automated today
- Validation and link checking (GitHub Actions, weekly and on push).

## What is not automated
- Reading sources and judging status. The agent does this each week. It can be wrong, so entries link raw evidence.
- Contacting authors or announcing anywhere. Nothing is posted publicly without the owner's approval.

## Metrics
GitHub repo traffic plus corrections submitted and entries added. A cookieless page counter may be added later.
