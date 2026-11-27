# Roadmap

Last updated: 2026-11-27 (6 entries, 5 independently tested and 1 untested; next: Diffusion Policy, RT-2-style, more Pi0/OpenVLA-family claims). The agent updates this file at least weekly.

## Goal
Be the first place a robotics engineer checks before building on a published method: what was claimed, what independent attempts found, with links to the evidence. Quality over volume. A small ledger that is right beats a large one that is not.

## Strategy
1. Narrow first: VLA and imitation-learning manipulation claims, where replication evidence already exists in public issues and papers.
2. Evidence from public sources only, neutral wording, status rules in POLICY.md.
3. Be easy to cite: permalinks, badges, RSS and JSON feeds.
4. Earn trust with authors and maintainers: corrections are fast and visible, authors can respond.
5. Grow by being useful, not by promotion. Outreach is drafted for the owner's approval.

## Milestones
**30 days (by 2026-12-24)**
- 15 to 20 verified entries (Diffusion Policy, RT-2-style, more OpenVLA-family and Pi0 claims, other benchmarks beyond LIBERO; Octo done as CL-0005, ACT as CL-0006).
- Each entry has at least two independent sources where possible, or says it has one.
- First correction handled end to end. Weekly changelog kept.
- Maintainer outreach drafts ready for owner approval.

**60 days (by 2027-01-23)**
- 40 entries across at least 4 benchmarks. Per-method pages and a status summary table.
- Intake workflow for replication submissions with a checklist.
- Badge adopted by at least one third-party README (counted from referrer searches, not tracked users).

**90 days (by 2027-02-22)**
- 75 entries. Documented methodology and a small set of standard replication protocols linked from entries.
- Review of what was useful: which entries get traffic, which corrections came in, whether to broaden beyond VLA.

## Weekly plan (agent)
- Mon to Fri: research and add 1 to 3 verified entries or evidence updates per day, push with validation.
- Sun: link check runs automatically. Review issues, update CHANGELOG.md and this roadmap, report metrics to the owner.
- Daily: one meaningful contribution, committed and reported by 21:45 KST.

## Metrics
- Entries (verified) and share with 2+ independent sources.
- Corrections submitted and median time to respond.
- Repo traffic (views, unique visitors, clones) from GitHub Insights, stars, badge and feed requests where visible.
- Link health (weekly check).
Page-view counting (Abacus, a cookieless third-party counter) is paused as of 2026-11-26 while the owner reviews the provider; the site makes no count request from visitors' browsers. If re-enabled, the request goes from the visitor's browser to Abacus, which sees the visitor's IP address for rate limiting, and its log retention is unverified by us. Until then, traffic comes from GitHub Insights only.

## Automated vs needs approval
Automated: research and drafting entries, validation, feeds and badges build, weekly link check, commits to this repo, changelog, roadmap updates.
Needs the owner's approval: any public post, announcement or message to people; comments, issues or PRs on other people's repos; third-party accounts or services (analytics, domains); anything that spends money; moving or deleting the project.

## Risks
- Wrong or stale entries. Mitigation: source links on every entry, last-checked dates, correction form, neutral wording.
- Reputational harm to named researchers. Mitigation: "contradicted" only with a direct cited source; single failed runs are "not reproduced".
- Nobody uses it. Mitigation: narrow focus on real pain, easy citing, a review at 90 days.
- Agent errors or drift. Mitigation: validation script, human owner can override, history in git.
- Source churn (dead links, moved repos). Mitigation: weekly link check.
