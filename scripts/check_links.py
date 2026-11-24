#!/usr/bin/env python3
"""Report evidence links that no longer resolve. Writes link_report.md. Never edits data."""
import json, urllib.request
d = json.load(open("site/data.json"))
bad = []
for c in d["claims"]:
    for e in c["evidence"] + [c["source"]]:
        try:
            r = urllib.request.Request(e["url"], headers={"User-Agent": "claim-ledger-linkcheck"})
            urllib.request.urlopen(r, timeout=20)
        except Exception as ex:
            bad.append(f"- {c['id']}: {e['url']} ({ex})")
open("link_report.md", "w").write("# Link check\n\n" + ("\n".join(bad) if bad else "All links resolved.") + "\n")
print(open("link_report.md").read())
