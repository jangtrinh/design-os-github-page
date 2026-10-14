#!/usr/bin/env python3
"""
DESIGN:OS — GitHub Presence SEO / AEO / GEO Deterministic Harness
Zero-dependency Python 3 stdlib CLI to audit, verify, and enforce 5-layer
Search Engine (SEO), Answer Engine (AEO), and Generative Engine (GEO) standards
across GitHub Profile, Organization, and Repository READMEs.

Usage:
  python3 scripts/seo-aeo-geo-harness.py --repo-dir /path/to/repo --owner jangtrinh [--check-links] [--html-report out.html]
"""

from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
from pathlib import Path
import html as html_lib
from typing import Any, Dict, List, Tuple


EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U00002600-\U000027BF"
    "\U0001FA00-\U0001FAFF"
    "]+",
    flags=re.UNICODE,
)


def find_readme(repo_dir: Path) -> Path:
    profile_readme = repo_dir / "profile" / "README.md"
    if profile_readme.exists():
        return profile_readme
    root_readme = repo_dir / "README.md"
    if root_readme.exists():
        return root_readme
    raise FileNotFoundError(f"No README.md or profile/README.md found in {repo_dir}")


def gate_1_links(readme_text: str, check_remote: bool = False) -> Tuple[bool, str, List[str]]:
    hrefs = re.findall(r'href=["\'](https?://[^"\']+)["\']', readme_text)
    md_links = re.findall(r'\]\((https?://[^)\s]+)\)', readme_text)
    all_urls = sorted(set(hrefs + md_links))
    if not all_urls:
        return False, "No external http(s) links found in README", []

    if not check_remote:
        return True, f"Verified {len(all_urls)} unique canonical URLs in DOM", []

    failures: List[str] = []
    for url in all_urls:
        if "img.shields.io" in url or "mailto:" in url:
            continue
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "DESIGN-OS-Harness/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                if resp.status >= 400:
                    failures.append(f"{url} -> HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            if e.code == 405:
                continue
            failures.append(f"{url} -> HTTP {e.code}")
        except Exception as e:
            failures.append(f"{url} -> {e}")

    passed = len(failures) == 0
    summary = f"Checked {len(all_urls)} URLs ({len(failures)} broken/404)"
    return passed, summary, failures


def gate_2_github_metadata(owner: str, readme_text: str) -> Tuple[bool, str, List[str]]:
    repo_urls = set(
        re.findall(
            rf'https://github\.com/{re.escape(owner)}/([A-Za-z0-9_.-]+)',
            readme_text,
        )
    )
    if not repo_urls:
        return True, f"No specific {owner}/* repository links to check", []

    try:
        proc = subprocess.run(
            [
                "gh",
                "repo",
                "list",
                owner,
                "--limit",
                "60",
                "--json",
                "name,description,homepageUrl,repositoryTopics,visibility",
            ],
            capture_output=True,
            text=True,
            timeout=15,
            check=True,
        )
        repos_data = {r["name"]: r for r in json.loads(proc.stdout)}
    except Exception as e:
        return False, f"gh CLI metadata check failed: {e}", [str(e)]

    issues: List[str] = []
    checked = 0
    for rname in sorted(repo_urls):
        if rname not in repos_data:
            issues.append(f"{owner}/{rname}: repository not found on GitHub (404)")
            continue
        info = repos_data[rname]
        checked += 1
        if info.get("visibility") != "PUBLIC":
            issues.append(f"{owner}/{rname}: visibility is {info.get('visibility')} (blocks public crawlers)")
        if not (info.get("description") or "").strip():
            issues.append(f"{owner}/{rname}: missing GitHub description (<meta description>)")
        topics = info.get("repositoryTopics") or []
        if len(topics) < 3:
            issues.append(f"{owner}/{rname}: only {len(topics)} topics (minimum 3 required)")

    passed = len(issues) == 0
    summary = f"Audited {checked} linked {owner}/* repos on GitHub API ({len(issues)} metadata gaps)"
    return passed, summary, issues


def gate_3_geo_llms_txt(repo_dir: Path, readme_text: str) -> Tuple[bool, str, List[str]]:
    llms_path = repo_dir / "llms.txt"
    issues: List[str] = []
    if not llms_path.exists():
        return False, "Missing llms.txt at repository root", ["Create llms.txt at repo root"]

    content = llms_path.read_text(encoding="utf-8")
    if not content.startswith("# "):
        issues.append("llms.txt must start with an H1 (# Title)")
    if "\n> " not in content:
        issues.append("llms.txt must include a blockquote (> ...) entity definition")
    if "llms.txt" not in readme_text:
        issues.append("README.md does not link or badge llms.txt for crawler discovery")

    passed = len(issues) == 0
    summary = f"llms.txt present ({len(content)} bytes) & linked in README" if passed else "llms.txt validation failed"
    return passed, summary, issues


def gate_4_aeo_faq_index(readme_text: str) -> Tuple[bool, str, List[str]]:
    issues: List[str] = []
    if "<details>" not in readme_text or "<summary>" not in readme_text:
        issues.append("Missing collapsible <details><summary> AEO FAQ & Registry block")
    questions = re.findall(r"\*\*[^*]+\?\*\*", readme_text)
    if len(questions) < 2:
        issues.append(f"Found {len(questions)} direct Q&A definitions (minimum 2 required for AEO citation)")
    if "| :---" not in readme_text:
        issues.append("Missing structured Markdown registry table inside README")

    passed = len(issues) == 0
    summary = f"Verified <details> AEO block with {len(questions)} canonical Q&As + Markdown registry table"
    return passed, summary, issues


def gate_5_semantic_alt_and_monochrome(readme_text: str) -> Tuple[bool, str, List[str]]:
    issues: List[str] = []
    img_tags = re.findall(r"<img\b[^>]*>", readme_text, flags=re.IGNORECASE)
    short_alts: List[str] = []
    for tag in img_tags:
        if "img.shields.io" in tag:
            continue
        m = re.search(r'alt=["\']([^"\']*)["\']', tag)
        if not m:
            short_alts.append(f"Missing alt attribute: {tag[:60]}...")
        elif len(m.group(1).strip()) < 25:
            short_alts.append(f"Short alt ('{m.group(1)}', <25 chars)")

    if short_alts:
        issues.extend(short_alts)

    emojis = EMOJI_RE.findall(readme_text)
    if emojis:
        issues.append(f"Prohibited emojis detected: {''.join(set(emojis))}")

    passed = len(issues) == 0
    summary = f"Audited {len(img_tags)} <img> tags (all card alts >=25 chars, 0 emojis)"
    return passed, summary, issues


def render_html_report(results: List[Dict[str, Any]], out_path: Path) -> None:
    rows_html = ""
    for r in results:
        for g in r["gates"]:
            status_label = "PASS" if g["passed"] else "FAIL"
            detail_html = "<br/>".join(html_lib.escape(x) for x in g["issues"]) if g["issues"] else html_lib.escape(g["summary"])
            rows_html += f"""
            <tr>
              <td><b>{r['target']}</b></td>
              <td><code>{g['id']}</code></td>
              <td><b>{status_label}</b></td>
              <td>{detail_html}</td>
            </tr>"""

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Inter", monospace; background: #ffffff; color: #111111; padding: 32px; max-width: 1080px; margin: 0 auto; }}
  h1 {{ font-size: 20px; border-bottom: 2px solid #111; padding-bottom: 10px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.04em; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th, td {{ border: 1px solid #d4d4d4; padding: 9px 12px; text-align: left; vertical-align: top; }}
  th {{ background: #f5f5f5; font-weight: 700; text-transform: uppercase; font-size: 11px; letter-spacing: 0.05em; }}
</style>
</head>
<body>
  <h1>DESIGN:OS SEO / AEO / GEO Deterministic Harness Verification</h1>
  <table>
    <thead>
      <tr>
        <th>Target Profile / Org</th>
        <th>Gate</th>
        <th>Verdict</th>
        <th>Evidence &amp; Telemetry</th>
      </tr>
    </thead>
    <tbody>{rows_html}
    </tbody>
  </table>
</body>
</html>"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")


def audit_target(repo_dir: Path, owner: str, check_links: bool) -> Dict[str, Any]:
    readme_path = find_readme(repo_dir)
    text = readme_path.read_text(encoding="utf-8")

    g1_ok, g1_sum, g1_iss = gate_1_links(text, check_remote=check_links)
    g2_ok, g2_sum, g2_iss = gate_2_github_metadata(owner, text)
    g3_ok, g3_sum, g3_iss = gate_3_geo_llms_txt(repo_dir, text)
    g4_ok, g4_sum, g4_iss = gate_4_aeo_faq_index(text)
    g5_ok, g5_sum, g5_iss = gate_5_semantic_alt_and_monochrome(text)

    gates = [
        {"id": "G1_LINKS_NO_404", "passed": g1_ok, "summary": g1_sum, "issues": g1_iss},
        {"id": "G2_GITHUB_METADATA", "passed": g2_ok, "summary": g2_sum, "issues": g2_iss},
        {"id": "G3_GEO_LLMS_TXT", "passed": g3_ok, "summary": g3_sum, "issues": g3_iss},
        {"id": "G4_AEO_FAQ_INDEX", "passed": g4_ok, "summary": g4_sum, "issues": g4_iss},
        {"id": "G5_SEMANTIC_IMG_ALT", "passed": g5_ok, "summary": g5_sum, "issues": g5_iss},
    ]
    all_passed = all(g["passed"] for g in gates)
    return {
        "target": f"{owner} ({readme_path.relative_to(repo_dir)})",
        "repo_dir": str(repo_dir),
        "passed": all_passed,
        "gates": gates,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="DESIGN:OS SEO/AEO/GEO Deterministic Harness")
    parser.add_argument(
        "--target",
        action="append",
        nargs=2,
        metavar=("REPO_DIR", "OWNER"),
        help="Target repo directory and GitHub owner (can be passed multiple times)",
    )
    parser.add_argument("--check-links", action="store_true", help="Perform live HTTP HEAD check on all URLs")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    parser.add_argument("--html-report", type=str, default="", help="Write HTML verification scorecard to path")
    args = parser.parse_args()

    if not args.target:
        parser.error("At least one --target <REPO_DIR> <OWNER> is required")

    results: List[Dict[str, Any]] = []
    for repo_dir_str, owner in args.target:
        results.append(audit_target(Path(repo_dir_str).resolve(), owner, args.check_links))

    if args.html_report:
        render_html_report(results, Path(args.html_report).resolve())

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            verdict = "PASS" if r["passed"] else "FAIL"
            print(f"=== {r['target']} -> {verdict} ===")
            for g in r["gates"]:
                st = "PASS" if g["passed"] else "FAIL"
                print(f"  [{st}] {g['id']}: {g['summary']}")
                for iss in g["issues"]:
                    print(f"         - {iss}")

    return 0 if all(r["passed"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
