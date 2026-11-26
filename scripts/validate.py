#!/usr/bin/env python3
"""Validate docs/data.json. Stdlib only. Exit 1 on any problem."""
import json, re, sys
STATUS = {"untested","replicated","partially_replicated","not_reproduced","contradicted"}
REQ = ["id","title","claim","method","benchmark","source","status","summary","evidence","last_checked","checked_by"]
d = json.load(open("docs/data.json"))
errs, ids = [], set()
for c in d["claims"]:
    cid = c.get("id", "?")
    for k in REQ:
        if k not in c: errs.append(f"{cid}: missing {k}")
    if not re.fullmatch(r"CL-\d{4}", cid): errs.append(f"{cid}: bad id")
    if cid in ids: errs.append(f"{cid}: duplicate id")
    ids.add(cid)
    if c.get("status") not in STATUS: errs.append(f"{cid}: bad status")
    ev = c.get("evidence", [])
    if not ev: errs.append(f"{cid}: no evidence")
    for e in ev + [c.get("source", {})]:
        if not str(e.get("url", "")).startswith("https://"): errs.append(f"{cid}: bad url {e.get('url')}")
    if c.get("status") == "contradicted" and not any(e.get("type") in ("erratum", "paper", "repo", "issue", "forum", "other") for e in ev):
        errs.append(f"{cid}: contradicted needs a cited source")
    n_ind = sum(1 for e in ev if e.get("role") == "independent_attempt")
    for e in ev:
        if e.get("role") not in ("independent_attempt", "adjacent"): errs.append(f"{cid}: evidence needs role independent_attempt or adjacent ({e.get('url')})")
    if c.get("status") in ("replicated", "partially_replicated", "not_reproduced") and n_ind == 0:
        errs.append(f"{cid}: {c.get('status')} needs at least one independent_attempt evidence item")
    if c.get("status") == "untested" and n_ind:
        errs.append(f"{cid}: untested cannot cite independent_attempt evidence")
    if c.get("status") != "untested":
        ck = c.get("checks", {})
        for k in ("task_match", "setup", "author_overlap"):
            if not ck.get(k): errs.append(f"{cid}: checks.{k} required before setting a status")
    if c.get("status") != "untested" and not c.get("summary"): errs.append(f"{cid}: empty summary")
tested = sum(1 for c in d["claims"] if c.get("status") != "untested")
print("OK" if not errs else "\n".join(errs), f"({len(d['claims'])} claims)")
print(f"tracked: {len(d['claims'])}, independently tested: {tested}")
sys.exit(1 if errs else 0)
