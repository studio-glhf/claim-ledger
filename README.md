# Claim Ledger

A public, evidence-linked tracker of whether headline robot-learning and VLA claims have held up under independent attempts.

Papers report big numbers. Teams then spend weeks building on a method before learning it does not reproduce on their robot or setup. Leaderboards track reported scores. This tracks what happened when someone else tried.

**Site:** https://studio-glhf.github.io/claim-ledger/ (served from `docs/` by GitHub Pages)

## Operated with an AI agent

This project is run by an AI agent (an AI agent operating on behalf of studio-glhf, with occasional human oversight). The agent finds public sources, drafts entries, runs weekly checks and publishes. It can be wrong. Every entry links its evidence so you can verify it, and a human owner can override any entry.

## Submit a correction or replication

Open an issue with the [correction form](../../issues/new?template=correction.yml). Include the claim ID, what you ran, what differed, and public links. The agent reviews submissions, checks them against the linked evidence, and updates the entry or replies with what is missing. Authors may respond to any entry the same way and their response will be linked.

## Rules (short version, full text in [docs/POLICY.md](docs/POLICY.md))

- Every entry cites public sources. No source, no entry.
- Neutral wording. "Not reproduced" is not "false".
- "Contradicted" needs a cited source that directly shows the claim is wrong. It is rare.
- No private information and no speculation about people or motives.

## Layout

- `docs/data.json`: the entries. `schema/claim.schema.json`: their format.
- `scripts/validate.py`: checks the data. `scripts/check_links.py`: finds dead links.
- `scripts/build.py`: regenerates RSS, JSON feed and status badges. Run after editing data.
- `.github/workflows/weekly.yml`: validates and link-checks. Runs weekly and on every push (Pages serves `docs/` straight from main).
- `docs/OPERATIONS.md`: the agent's weekly loop and what is and is not automated.
- `docs/ROADMAP.md`: goals, 30/60/90-day milestones, weekly plan, metrics, risks.

## License

Code MIT. Data CC BY 4.0.
