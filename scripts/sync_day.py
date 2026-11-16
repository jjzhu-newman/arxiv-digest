#!/usr/bin/env python3
"""Copy one day's digest/PDF into this repo, refresh README, commit and push."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIGEST = Path("/workspace/arxiv-digest")
SRC_JINGDU = Path("/workspace/arxiv-jingdu")
SENSITIVE_KEYS = {"machine_id", "machineId", "machine_uuid"}

README_HEADER = "# \u5de5\u4f5c\u65e5 arXiv \u5bfc\u8bfb\n\n\u8fd9\u662f\u4e00\u4efd\u9762\u5411\u51dd\u805a\u6001\u4e0e\u91cf\u5b50\u65b9\u5411\u7684\u4e2a\u4eba\u9605\u8bfb\u7b14\u8bb0\uff0c\u6309\u5de5\u4f5c\u65e5\u6536\u5f55\uff1a\n\n- `YYYY-MM-DD/report.md`\uff1a\u5f53\u65e5\u5174\u8da3\u6458\u8981\uff08\u4e2d\u6587\uff09\n- `YYYY-MM-DD/final_picks.json`\uff1a\u5165\u9009\u8bba\u6587\u7684\u7ed3\u6784\u5316\u8bb0\u5f55\n- `YYYY-MM-DD/arxiv-jingdu-YYYY-MM-DD.pdf`\uff1a\u7cbe\u8bfb\u5361\u5408\u96c6\uff08\u901a\u5e38\u5728\u6458\u8981\u4e4b\u540e\u7684\u65e9\u6668\u751f\u6210\uff09\n\n\u626b\u63cf\u8303\u56f4\u5305\u62ec `cond-mat`\u3001`quant-ph`\u3001`hep-th`\u3001`math-ph`\uff0c\u4ee5\u53ca `cs.LG` / `stat.ML` \u4e2d\u504f\u7269\u7406\u4fe1\u606f\u6216\u91cf\u5b50\u7684\u6761\u76ee\u3002\u5174\u8da3\u951a\u70b9\u5927\u81f4\u662f\uff1a\u975e\u5384\u7c73\u62d3\u6251\u4e0e\u5f00\u653e\u7cfb\u7edf\u3001\u4ea4\u9519\u78c1\u4e0e\u81ea\u65cb\u7535\u5b50\u5b66\u3001\u7ea0\u7f20\u4e0e\u91cf\u5b50\u5173\u8054\u3001Floquet \u7cfb\u7edf\u3001\u7269\u7406\u4fe1\u606f\u795e\u7ecf\u7f51\u7edc\u4e0e\u795e\u7ecf\u7f51\u7edc\u91cf\u5b50\u6001\u3001\u91cf\u5b50\u673a\u5668\u5b66\u4e60\uff0c\u4ee5\u53ca\u91cf\u5b50\u4f20\u611f\u3002\n\n\u5de5\u4f5c\u65e5\u5348\u591c\u5de6\u53f3\u66f4\u65b0\u6458\u8981\uff0c\u65e9\u6668\u66f4\u65b0\u7cbe\u8bfb\u5361\u3002arXiv \u56e0\u5047\u671f\u987a\u5ef6\u516c\u544a\u65f6\uff0c\u5f53\u5929\u53ef\u80fd\u53ea\u6709\u7a7a\u7a97\u8bf4\u660e\u3001\u6ca1\u6709\u65b0\u7684\u5165\u9009\u6216\u7cbe\u8bfb\u5361\u3002\u8bba\u6587\u7248\u6743\u4ecd\u5f52\u539f\u4f5c\u8005\uff0c\u8bf7\u4ee5 [arXiv](https://arxiv.org) \u539f\u6587\u4e3a\u51c6\u3002\n\n## \u76ee\u5f55\n\n| \u65e5\u671f | \u5174\u8da3\u6458\u8981 | \u5165\u9009 | \u7cbe\u8bfb\u5361 |\n| --- | --- | ---: | --- |\n"


def sanitize(obj):
    if isinstance(obj, dict):
        return {k: sanitize(v) for k, v in obj.items() if k not in SENSITIVE_KEYS}
    if isinstance(obj, list):
        return [sanitize(x) for x in obj]
    return obj


def pick_count(data):
    if isinstance(data, list):
        return len(data)
    if not isinstance(data, dict):
        return None
    if "selected_count" in data:
        return data["selected_count"]
    for k in ("picks", "papers", "items", "selected", "final_picks"):
        if isinstance(data.get(k), list):
            return len(data[k])
    return None


def build_readme(root: Path) -> str:
    rows = []
    date_dirs = [
        p
        for p in root.iterdir()
        if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name)
    ]
    for d in sorted(date_dirs, reverse=True):
        date = d.name
        has_report = (d / "report.md").exists()
        has_pdf = (d / f"arxiv-jingdu-{date}.pdf").exists()
        n = "—"
        picks = d / "final_picks.json"
        if picks.exists():
            try:
                c = pick_count(json.loads(picks.read_text(encoding="utf-8")))
                if c is not None:
                    n = str(c)
            except Exception:
                pass
        report_cell = f"[摘要]({date}/report.md)" if has_report else "—"
        pdf_cell = f"[PDF]({date}/arxiv-jingdu-{date}.pdf)" if has_pdf else "—"
        rows.append(f"| {date} | {report_cell} | {n} | {pdf_cell} |")
    return README_HEADER + "\n".join(rows) + "\n"


def git(*args, check=True):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=check,
        text=True,
        capture_output=True,
    )


def copy_day(date: str) -> list[str]:
    dest = REPO_ROOT / date
    dest.mkdir(exist_ok=True)
    copied = []
    src_dir = SRC_DIGEST / date
    report = src_dir / "report.md"
    if not report.exists() and date == "2026-09-17":
        report = SRC_DIGEST / "2026-09-17-report.md"
    if report.exists():
        shutil.copy2(report, dest / "report.md")
        copied.append("report.md")
    picks = src_dir / "final_picks.json"
    if not picks.exists() and date == "2026-09-17":
        picks = SRC_DIGEST / "2026-09-17-final.json"
    if picks.exists():
        data = json.loads(picks.read_text(encoding="utf-8"))
        (dest / "final_picks.json").write_text(
            json.dumps(sanitize(data), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        copied.append("final_picks.json")
    pdf = SRC_JINGDU / f"arxiv-jingdu-{date}.pdf"
    if pdf.exists():
        shutil.copy2(pdf, dest / pdf.name)
        copied.append(pdf.name)
    return copied


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        print(f"invalid date: {args.date}", file=sys.stderr)
        return 2
    copied = copy_day(args.date)
    (REPO_ROOT / "README.md").write_text(build_readme(REPO_ROOT), encoding="utf-8")
    if not copied:
        print(f"no digest or PDF found for {args.date}")
        # still allow README-only refresh if something else changed
    print("copied:", ", ".join(copied) if copied else "(none)")
    if args.dry_run:
        return 0
    git("pull", "--rebase", "--autostash", check=False)
    git("add", args.date, "README.md")
    status = git("status", "--porcelain")
    if not status.stdout.strip():
        print("nothing to commit")
        return 0
    has_report = "report.md" in copied
    has_pdf = any(name.endswith(".pdf") for name in copied)
    if has_report and has_pdf:
        msg = f"Add {args.date} arXiv digest and close-reading cards"
    elif has_pdf:
        msg = f"Add {args.date} arXiv close-reading cards"
    elif has_report:
        msg = f"Add {args.date} arXiv interest digest"
    else:
        msg = f"Update {args.date} arXiv guide"
    git("commit", "-m", msg)
    push = git("push", "origin", "HEAD", check=False)
    if push.returncode != 0:
        print(push.stdout)
        print(push.stderr, file=sys.stderr)
        return push.returncode
    print("pushed", args.date)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
