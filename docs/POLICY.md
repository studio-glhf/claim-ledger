# Editorial policy

1. **Evidence first.** Every entry needs a primary source for the claim itself (with numbers). Sources can be papers, GitHub issues, forum threads, repos, errata.
   - `replicated`, `partially_replicated` and `not_reproduced` each need at least one evidence item marked `independent_attempt`: a comparable run by people independent of the claim's authors.
   - `untested` lists the search scope and any related evidence, marked `adjacent`. Adjacent evidence does not count as independent testing.
   - Before setting any status, check and record in `checks`: task/benchmark match, checkpoint and setup, and author overlap. A source that shares authors with the claim is `adjacent`.
   - Counts are reported separately: tracked claims, and independently tested claims (any status other than `untested`).
2. **Neutral language.** Describe what was run and what was observed. Do not guess at causes, intent or competence. Gaps often come from versions, seeds, hardware or rendering.
3. **Status meanings.** `replicated`, `partially_replicated`, `not_reproduced`, `untested`, `contradicted`. See `schema/claim.schema.json`.
4. **Contradicted is rare.** Only when a cited source directly shows the claim is wrong, for example an author erratum, a retraction, or a controlled re-test that isolates the cause. A single failed run is `not_reproduced`.
5. **Single runs are weak evidence.** Say so in the summary. Note seeds, episodes and setup when known.
6. **Authors can respond.** Responses submitted through the correction form are verified and linked. Entries change when evidence changes.
7. **Public sources only.** No private messages, no unpublished data, no personal information beyond public usernames already in the cited source.
8. **Corrections are logged.** Changes to an entry go through git history. Material changes are noted in the summary.
9. **Humans can override.** The owner can edit or remove any entry.
