#!/usr/bin/env python3
"""Validate site/data.json. Stdlib only. Exit 1 on any problem."""
import json, re, sys
STATUS = {"untested","replicated","partially_replicated","not_reproduced","contradicted"}
REQ = ["id","title","claim","method","benchmark","source","status","summary","evidence","last_checked","checked_by"]
d = json.load(open("site/data.json"))
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
    if c.get("status") != "untested" and not c.get("summary"): errs.append(f"{cid}: empty summary")
print("OK" if not errs else "\n".join(errs), f"({len(d['claims'])} claims)")
sys.exit(1 if errs else 0)
