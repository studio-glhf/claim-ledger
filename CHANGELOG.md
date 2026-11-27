# Changelog

## 2026-11-27 (night)
- Removed the page-view counter wording and code from the site; traffic is read from GitHub traffic stats only. Earlier changelog wording on approval was changed to plain factual terms.

## 2026-11-27 (later)
- Added CL-0006 (ACT sim Cube Transfer and Bimanual Insertion, human demonstrations, partially replicated), sourced from the ACT paper Table I, the LeRobot model card, and lerobot issues #2605 and #4168. The summary says the runs are not like-for-like.

## 2026-11-27
- POLICY.md: every status needs a primary claim source; replicated, partially_replicated and not_reproduced need independent comparable-attempt evidence; untested lists scope and adjacent evidence only. Before any status, task/benchmark match, setup and author overlap are recorded.
- Evidence items now carry a role (independent_attempt or adjacent) and claims carry a checks block. validate.py enforces both in CI and prints tracked vs independently tested counts.

## 2026-11-26
- CL-0005 (Octo): reclassified from partially replicated to untested. SIMPLER shares authors with Octo (Pertsch, Mees, Walke, Levine, Finn, Vuong, Xiao on both papers) and evaluates different tasks in paired sim/real experiments, so it is not an independent rerun; the entry now says no independent reproduction of the exact three-setup comparison was found. Status pill, feeds and badge regenerated.
- Page-view counter removed: the site no longer makes any count request, and the footer, README, roadmap and operations notes now say there is no on-site analytics.
- Added CL-0005 (Octo zero-shot multi-robot claim, partially replicated), sourced from the Octo paper, the SIMPLER real-to-sim evaluation of the released checkpoints, and octo-models/octo issues #151 and #157.
- Repository deleted and recreated to retire old commit URLs that exposed a personal name. Git history, file contents, site URL, feeds and badges are unchanged.
- Added a cookieless page-view counter (Abacus, no account, no cookies). Disclosed in the site footer and README; the count is public. Disclosure wording corrected the same day: the counter request goes to a third party that sees the visitor's IP address for rate limiting, and its log retention is unverified.

## 2026-11-24
- v1 published: site, schema, policy, correction form, weekly link check.
- Added CL-0001 (OpenVLA LIBERO, partially replicated), CL-0002 (LeRobot Pi0.5 LIBERO, replicated), CL-0003 (LeRobot Pi0 LIBERO, not reproduced).
- Added RSS (`feed.xml`), JSON Feed (`feed.json`) and per-claim status badges.

## 2026-11-24 (later)
- Added docs/ROADMAP.md.

## 2026-11-25
- CL-0003: added a second observation (lerobot #2156, LIBERO-Goal only, setting-dependent), marked the four-suite target as unverified because no primary score table for this checkpoint was found, and kept the status as not reproduced with clearer limits.
- CL-0002: reworded to say one evaluator reported 96.75% against the documented 97.5% (a near match), not that one run confirms the recipe.
- README: attribution changed to studio-glhf.

## 2026-11-25 (evening)
- Added CL-0004 (OpenVLA-OFT LIBERO, partially replicated), sourced from the authors' LIBERO.md, a LeRobot port's evaluation, and issues #128 and #150.
- History rewritten to remove a personal name from early README versions (approved by the owner).
