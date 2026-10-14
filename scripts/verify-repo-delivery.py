#!/usr/bin/env python3
"""verify-repo-delivery.py — 5-Gate AI-Ready Repository Delivery Verifier.

Verifies that a target repository complies with the DESIGN:OS + diagram-design
AI-Ready Delivery Standard:
  [D1_PLUGIN_MANIFESTS] .claude-plugin, .codex-plugin, .agents/plugins, .factory-plugin JSON manifests
  [D2_SKILL_AND_DOCTOR] skills/<slug>/SKILL.md + commands/doctor.md + prompts/doctor.md + scripts/self_check.py
  [D3_TRUST_GOVERNANCE] PRIVACY.md, SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md, LICENSE, llms.txt, docs/cookbook.md
  [D4_README_12_SECTIONS] 12-section editorial README with jump nav, comparison table, What loads when, It's working if, When not to use, 13-engine ecosystem
  [D5_IMAGE_PATHS_VALID] All local image paths in README.md exist on disk
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ECOSYSTEM_REPOS = (
    "design-os",
    "design-os-knowledge-builder",
    "design-os-figma-plugin",
    "design-os-svg-animation",
    "design-os-3d-blender",
    "design-os-drone-showcase",
    "design-os-github-page",
    "design-os-apple",
    "design-os-pedagogy",
    "design-os-origami",
    "design-os-voice-ux",
    "design-os-code2flow",
    "design-os-generative-ui",
)


def check_json_file(path: Path) -> tuple[bool, str]:
    if not path.is_file():
        return False, f"missing {path.name}"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return False, f"{path.name} is not a JSON object"
        return True, "ok"
    except Exception as exc:
        return False, f"invalid JSON in {path.name}: {exc}"


def gate_d1_plugin_manifests(root: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    required_direct = [
        root / ".claude-plugin/marketplace.json",
        root / ".codex-plugin/plugin.json",
        root / ".agents/plugins/marketplace.json",
        root / ".factory-plugin/plugin.json",
        root / ".factory-plugin/marketplace.json",
    ]
    for path in required_direct:
        ok, msg = check_json_file(path)
        if not ok:
            issues.append(f"{path.relative_to(root)}: {msg}")

    claude_plugin = root / ".claude-plugin/plugin.json"
    claude_bundle = root / "bundles/claude-code/.claude-plugin/plugin.json"
    if claude_plugin.is_file():
        ok, msg = check_json_file(claude_plugin)
        if not ok:
            issues.append(f".claude-plugin/plugin.json: {msg}")
    elif claude_bundle.is_file():
        ok, msg = check_json_file(claude_bundle)
        if not ok:
            issues.append(f"bundles/claude-code/.claude-plugin/plugin.json: {msg}")
    else:
        issues.append("missing .claude-plugin/plugin.json")

    return len(issues) == 0, issues


def gate_d2_skill_and_doctor(root: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    skills_dir = root / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md")) if skills_dir.is_dir() else []
    if not skill_files:
        issues.append("missing skills/<slug>/SKILL.md")
    else:
        for sf in skill_files:
            text = sf.read_text(encoding="utf-8")
            if not text.startswith("---\n") or "name:" not in text or "description:" not in text:
                issues.append(f"{sf.relative_to(root)}: missing YAML frontmatter (name/description)")

    for rel in ("commands/doctor.md", "prompts/doctor.md", "scripts/self_check.py"):
        p = root / rel
        if not p.is_file() or p.stat().st_size == 0:
            issues.append(f"missing or empty {rel}")

    self_check = root / "scripts/self_check.py"
    if self_check.is_file():
        proc = subprocess.run(
            [sys.executable, "-B", str(self_check)],
            cwd=root,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            issues.append(f"scripts/self_check.py exited {proc.returncode}: {proc.stderr.strip() or proc.stdout.strip()}")

    return len(issues) == 0, issues


def gate_d3_trust_governance(root: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    required = (
        "PRIVACY.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "CHANGELOG.md",
        "LICENSE",
        "llms.txt",
        "docs/cookbook.md",
    )
    for rel in required:
        p = root / rel
        if not p.is_file() or p.stat().st_size < 40:
            issues.append(f"missing or stub {rel}")
    return len(issues) == 0, issues


def gate_d4_readme_12_sections(root: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    readme_path = root / "README.md"
    if not readme_path.is_file():
        return False, ["missing README.md"]
    text = readme_path.read_text(encoding="utf-8")
    lower = text.casefold()

    required_markers = [
        ("202020", "monochrome #202020 badge strip"),
        ("#quickstart", "top jump-nav #quickstart anchor"),
        ("#what-it-makes", "top jump-nav #what-it-makes anchor"),
        ("## why this exists", "## Why this exists section"),
        ("## quickstart", "## Quickstart section"),
        ("## what it makes", "## What it makes section"),
        ("## installation", "## Installation section"),
        ("## how it works", "## How it works section"),
        ("### what loads when", "### What loads when context table"),
        ("## file structure", "## File structure section"),
        ("### it's working if", "### It's working if... verification checklist"),
        ("### when not to use", "### When not to use boundary list"),
        ("## design:os ecosystem", "## DESIGN:OS Ecosystem section"),
        ("privacy.md", "PRIVACY.md reference"),
        ("security.md", "SECURITY.md reference"),
        ("contributing.md", "CONTRIBUTING.md reference"),
        ("code_of_conduct.md", "CODE_OF_CONDUCT.md reference"),
        ("docs/cookbook.md", "docs/cookbook.md reference"),
        ("scripts/self_check.py", "scripts/self_check.py reference"),
    ]
    for needle, label in required_markers:
        if needle not in lower:
            issues.append(f"README.md missing {label} ({needle!r})")

    missing_eco = [
        slug for slug in ECOSYSTEM_REPOS
        if f"https://jangtrinh.github.io/{slug}/" not in text
    ]
    if missing_eco:
        issues.append(f"README.md missing ecosystem Pages links: {', '.join(missing_eco)}")

    return len(issues) == 0, issues


def gate_d5_image_paths_valid(root: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    readme_path = root / "README.md"
    if not readme_path.is_file():
        return False, ["missing README.md"]
    text = readme_path.read_text(encoding="utf-8")
    # Strip fenced code blocks before scanning for image tags
    stripped = re.sub(r"(?ms)^```.*?^```", "", text)
    html_imgs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', stripped)
    md_imgs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", stripped)
    all_imgs = html_imgs + md_imgs
    if not all_imgs:
        issues.append("README.md has no images")
    local_imgs = [
        src for src in all_imgs
        if not src.startswith(("http://", "https://", "data:"))
    ]
    if not local_imgs:
        issues.append("README.md has no local hero/specimen image")
    for src in local_imgs:
        clean = src.split("#")[0].split("?")[0]
        target = (root / clean).resolve()
        if not target.is_file():
            issues.append(f"broken local image in README.md: {src}")
    return len(issues) == 0, issues


def verify_repo(root: Path) -> dict:
    root = root.resolve()
    gates = [
        ("D1_PLUGIN_MANIFESTS", gate_d1_plugin_manifests),
        ("D2_SKILL_AND_DOCTOR", gate_d2_skill_and_doctor),
        ("D3_TRUST_GOVERNANCE", gate_d3_trust_governance),
        ("D4_README_12_SECTIONS", gate_d4_readme_12_sections),
        ("D5_IMAGE_PATHS_VALID", gate_d5_image_paths_valid),
    ]
    results = {}
    all_passed = True
    for name, fn in gates:
        ok, issues = fn(root)
        results[name] = {"passed": ok, "issues": issues}
        if not ok:
            all_passed = False
    return {"repo": root.name, "path": str(root), "passed": all_passed, "gates": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repos", nargs="+", type=Path, help="Repository root paths to verify")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    args = parser.parse_args()

    reports = [verify_repo(r) for r in args.repos]
    if args.json:
        print(json.dumps(reports, indent=2))
    else:
        for rep in reports:
            status = "PASS" if rep["passed"] else "FAIL"
            print(f"[{status}] {rep['repo']} ({rep['path']})")
            for gname, gres in rep["gates"].items():
                gstatus = "OK" if gres["passed"] else "FAIL"
                print(f"  - {gname}: {gstatus}")
                for issue in gres["issues"]:
                    print(f"      * {issue}")
    return 0 if all(r["passed"] for r in reports) else 1


if __name__ == "__main__":
    raise SystemExit(main())
