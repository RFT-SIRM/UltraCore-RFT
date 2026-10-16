#!/usr/bin/env python3
"""Read-only latest-run monitor for public RFT-SIRM GitHub repositories."""
import argparse, json, os, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPOS = [
 ("UltraCore-RFT","RFT-SIRM/UltraCore-RFT","Docs, Pages, coordination"),
 ("Theory of Everything","RFT-SIRM/Evgeny-s-Theory-of-Everything","Dissertation and recurrence audit"),
 ("Evgeny Theorem","RFT-SIRM/Evgeny-Theorem","Lean 4 formalization"),
 ("Phi-Genesis","RFT-SIRM/Phi-Genesis","Spectral computation and Gate A"),
 ("Rift Network","RFT-SIRM/Rift-Network","Network engineering CI"),
 ("Rift-L1 Blockchain","RFT-SIRM/Rift-L1-Blockchain","Blockchain engineering CI"),
 ("Agave Rift Scheduler","RFT-SIRM/agave-rift-scheduler","Scheduler CI and fuzz"),
 ("Aave V4 Hub model review","RFT-SIRM/aave-v4-hub-model-review","Model review and regressions"),
]
def get(url):
 h={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"UltraCore-RFT-Ecosystem-Control"}
 if os.getenv("GITHUB_TOKEN"): h["Authorization"]="Bearer "+os.environ["GITHUB_TOKEN"]
 with urllib.request.urlopen(urllib.request.Request(url,headers=h),timeout=20) as r: return json.load(r)
def collect(label, repo, purpose):
 base="https://github.com/"+repo+"/actions"
 try:
  runs=get("https://api.github.com/repos/"+repo+"/actions/runs?per_page=10").get("workflow_runs",[])
  if not runs: return {"label":label,"repository":repo,"purpose":purpose,"state":"NOT RUN","detail":"No public workflow runs found","url":base}
  r=runs[0]; status=r.get("status"); c=r.get("conclusion")
  state="RUNNING" if status!="completed" else ("PASS" if c=="success" else "FAIL" if c in ("failure","timed_out","startup_failure","action_required") else c.upper() if c else "UNKNOWN")
  return {"label":label,"repository":repo,"purpose":purpose,"state":state,"workflow":r.get("name"),"branch":r.get("head_branch"),"sha":(r.get("head_sha") or "")[:7],"updated_at":r.get("updated_at"),"url":r.get("html_url",base),"detail":r.get("display_title") or r.get("name")}
 except urllib.error.HTTPError as e:
  state,detail=(("NOT FOUND","Repository/Actions endpoint unavailable") if e.code==404 else ("API LIMITED","GitHub API rate limit or access restriction") if e.code==403 else ("ERROR","GitHub API HTTP "+str(e.code)))
  return {"label":label,"repository":repo,"purpose":purpose,"state":state,"detail":detail,"url":base}
 except (urllib.error.URLError,TimeoutError,json.JSONDecodeError) as e:
  return {"label":label,"repository":repo,"purpose":purpose,"state":"ERROR","detail":str(e),"url":base}
def main():
 p=argparse.ArgumentParser(); p.add_argument("--json",default="ecosystem-status.json"); p.add_argument("--markdown",default="ecosystem-status.md"); a=p.parse_args()
 rows=[]
 for item in REPOS: rows.append(collect(*item)); time.sleep(.15)
 report={"generated_at":datetime.now(timezone.utc).isoformat(),"mode":"read-only latest-run monitor","note":"PASS applies only to the latest reported workflow run, not every test or the whole repository.","repositories":rows}
 Path(a.json).write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
 lines=["# UltraCore-RFT — Ecosystem CI status","",f"Generated (UTC): {report['generated_at']}",""," > PASS is scoped to one latest run. NOT RUN, NOT FOUND, API LIMITED and ERROR are not passes. This monitor does not dispatch tests.","","| Project | State | Latest run | Branch / SHA | Updated (UTC) |","|---|---|---|---|---|"]
 for r in rows:
  title=r.get("workflow",r.get("detail","Open Actions")); bs=f"`{r.get('branch','—')}` / `{r.get('sha','—')}`"
  lines.append(f"| [{r['label']}](https://github.com/{r['repository']}) | **{r['state']}** | [{title}]({r['url']}) | {bs} | {r.get('updated_at','—') or '—'} |")
 lines += ["","## Evidence scope","","This report monitors published workflow runs. Each repository remains responsible for executing its own tests. Missing runs are never interpreted as success.",""]
 Path(a.markdown).write_text("\n".join(lines),encoding="utf-8"); print("\n".join(lines))
 return 0
if __name__=="__main__": sys.exit(main())
