#!/usr/bin/env python3
"""
scaffold-repo-pages.py — Instant GitHub Pages Scaffolder (Generic Public Edition)

Generates an author-grade, high-converting marketing & docs site in docs/ (or specified directory)
for ANY public repository. Includes SEO, XML Sitemap, robots.txt, llms.txt (GEO),
Schema.org JSON-LD FAQPage (AEO), and optional Buy Me a Coffee widget.

Usage:
  python3 scaffold-repo-pages.py --owner <owner> --repo <repo> [options]

Examples:
  python3 scaffold-repo-pages.py --owner alice --repo fast-kv --name "FastKV" \
    --tagline "Sub-millisecond persistent key-value store in pure Go." \
    --desc "FastKV is a zero-dependency, crash-safe embedded key-value database." \
    --accent "#2563eb" --bmc "alicebuilds"
"""

import argparse
import os
import sys
from datetime import datetime

DEFAULT_ACCENT = "#0969da"

def get_templates_dir():
    # Relative to this script: ../templates
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, "..", "templates"))

def render_file(src_path, dst_path, replacements):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for key, val in replacements.items():
        content = content.replace(f"{{{{{key}}}}}", str(val))
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Created: {dst_path}")

def main():
    parser = argparse.ArgumentParser(description="Scaffold an author-grade GitHub Pages site for any repository.")
    parser.add_argument("--owner", required=True, help="GitHub owner / username / organization (e.g. alice)")
    parser.add_argument("--repo", required=True, help="Repository name (e.g. my-tool)")
    parser.add_argument("--name", help="Display name of the tool (default: title-cased repo)")
    parser.add_argument("--tagline", help="Proposition sentence for the hero h1 (e.g. 'Build UI faster with code.')")
    parser.add_argument("--category", default="Open Source", help="Category or ecosystem eyebrow (default: Open Source)")
    parser.add_argument("--desc", help="Meta description under 160 characters for SEO/AEO")
    parser.add_argument("--accent", default=DEFAULT_ACCENT, help=f"Hex accent color (default: {DEFAULT_ACCENT})")
    parser.add_argument("--bmc", default="", help="Buy Me A Coffee ID (e.g. jangtrinh). Leave empty to omit.")
    parser.add_argument("--wordmark", help="Wordmark brand name for footer/nav (default: UPPERCASE OWNER)")
    parser.add_argument("--wordmark-url", help="Wordmark target URL (default: https://github.com/OWNER)")
    parser.add_argument("--out-dir", default="./docs", help="Target output directory (default: ./docs)")
    parser.add_argument("--nojekyll", action="store_true", help="Add .nojekyll to disable Jekyll processing")

    args = parser.parse_args()

    owner = args.owner.strip()
    repo = args.repo.strip()
    name = args.name.strip() if args.name else repo.replace("-", " ").title()
    category = args.category.strip()
    tagline = args.tagline.strip() if args.tagline else f"{name} — High-performance, deterministic tool for developers."
    desc = args.desc.strip() if args.desc else f"{name}: open-source, production-ready toolchain built for modern engineering teams."
    accent = args.accent.strip()
    bmc_id = args.bmc.strip()
    wordmark = args.wordmark.strip() if args.wordmark else owner.upper()
    wordmark_url = args.wordmark_url.strip() if args.wordmark_url else f"https://github.com/{owner}"
    out_dir = os.path.abspath(args.out_dir)

    bmc_script = ""
    if bmc_id:
        bmc_script = f'<script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="{bmc_id}" data-description="Support me on Buy me a coffee!" data-message="" data-color="#FF813F" data-position="Right" data-x_margin="18" data-y_margin="18"></script>'

    now_date = datetime.now().strftime("%Y-%m-%d")
    replacements = {
        "OWNER": owner,
        "REPO": repo,
        "NAME": name,
        "CATEGORY": category,
        "EYEBROW": category,
        "LOGO_PATH": "/images/cover.png",
        "TAGLINE": tagline,
        "PROPOSITION_SENTENCE": tagline,
        "META_DESCRIPTION": desc,
        "ACCENT_COLOR": accent,
        "BMC_ID": bmc_id,
        "BMC_SCRIPT": bmc_script,
        "WORDMARK": wordmark,
        "WORDMARK_URL": wordmark_url,
        "DATE_TODAY": now_date,
        "LASTMOD": now_date,
    }

    templates_dir = get_templates_dir()
    if not os.path.isdir(templates_dir):
        print(f"Error: Templates directory not found at {templates_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"\n🚀 Scaffolding GitHub Pages for {owner}/{repo} into {out_dir}...\n")

    # Files to copy and replace
    files_to_render = [
        ("index.html", "index.html"),
        ("_config.yml", "_config.yml"),
        ("robots.txt", "robots.txt"),
        ("sitemap.xml", "sitemap.xml"),
        ("llms.txt", "llms.txt"),
        ("_layouts/default.html", "_layouts/default.html"),
        ("assets/site.css", "assets/site.css"),
    ]

    for rel_src, rel_dst in files_to_render:
        src = os.path.join(templates_dir, rel_src)
        dst = os.path.join(out_dir, rel_dst)
        if os.path.isfile(src):
            render_file(src, dst, replacements)
        else:
            print(f"  ⚠️ Warning: Source template missing: {src}")

    if args.nojekyll:
        nojekyll_path = os.path.join(out_dir, ".nojekyll")
        with open(nojekyll_path, "w", encoding="utf-8") as f:
            f.write("")
        print(f"  ✓ Created: {nojekyll_path}")

    print("\n✅ Scaffolding complete!")
    print("\nNext steps:")
    print(f"  1. Review and refine copy in: {os.path.join(out_dir, 'index.html')}")
    print(f"  2. Add your hero screenshot or diagram: {os.path.join(out_dir, 'assets/')}")
    print(f"  3. Commit and push: git add {args.out_dir} && git commit -m 'docs: scaffold GitHub Pages site'")
    print(f"  4. Enable GitHub Pages: gh api -X POST repos/{owner}/{repo}/pages -f 'source[branch]=main' -f 'source[path]=/{os.path.basename(out_dir)}'")
    print(f"  5. Site URL: https://{owner}.github.io/{repo}/\n")

if __name__ == "__main__":
    main()
