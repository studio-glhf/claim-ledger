#!/usr/bin/env python3
"""Generate docs/feed.xml, docs/feed.json and docs/badges/*.svg from docs/data.json. Stdlib only."""
import json, os, html
BASE = "https://studio-glhf.github.io/claim-ledger/"
COL = {"replicated":("#0a6b3b","replicated"),"partially_replicated":("#8a5a00","partial"),
       "not_reproduced":("#a24500","not reproduced"),"contradicted":("#a01c1c","contradicted"),"untested":("#4a5560","untested")}
d = json.load(open("docs/data.json"))
os.makedirs("docs/badges", exist_ok=True)
def badge(label, val, color):
    lw, vw = 7*len(label)+14, 7*len(val)+14
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{lw+vw}" height="20" role="img" aria-label="{label}: {val}">'
            f'<rect width="{lw}" height="20" fill="#555"/><rect x="{lw}" width="{vw}" height="20" fill="{color}"/>'
            f'<g fill="#fff" font-family="Verdana,sans-serif" font-size="11" text-anchor="middle">'
            f'<text x="{lw/2}" y="14">{label}</text><text x="{lw+vw/2}" y="14">{val}</text></g></svg>')
for c in d["claims"]:
    col, txt = COL[c["status"]]
    open(f"docs/badges/{c['id']}.svg", "w").write(badge("claim ledger", txt, col))
items = sorted(d["claims"], key=lambda c: c["last_checked"], reverse=True)
json.dump({"version":"https://jsonfeed.org/version/1.1","title":"Claim Ledger","home_page_url":BASE,
  "feed_url":BASE+"feed.json","items":[{"id":c["id"],"url":BASE+"#"+c["id"],"title":f"[{COL[c['status']][1]}] {c['title']}",
  "content_text":c["summary"],"date_modified":c["last_checked"]+"T00:00:00Z"} for c in items]},
  open("docs/feed.json","w"), indent=1)
x = ['<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Claim Ledger</title>',
     f'<link>{BASE}</link><description>Reproduction status of headline robot-learning claims</description>']
for c in items:
    x.append(f'<item><title>{html.escape("["+COL[c["status"]][1]+"] "+c["title"])}</title><link>{BASE}#{c["id"]}</link>'
             f'<guid isPermaLink="false">{c["id"]}-{c["last_checked"]}</guid><description>{html.escape(c["summary"])}</description></item>')
x.append("</channel></rss>")
open("docs/feed.xml","w").write("".join(x))
print("built", len(items), "entries")
