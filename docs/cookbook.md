# `design-os-github-page` Prompt & CLI Cookbook

Copy-paste recipes for **DESIGN:OS GitHub Pages Engine** (`skills/design-os-github-page/SKILL.md`).

---

## 1. Generate & Scaffold

> "Scaffold a 9-tier editorial GitHub Pages site in docs/ with JSON-LD SoftwareSourceCode + FAQPage schemas and llms.txt."

## 2. Audit & Verify

> "Upgrade this repository to the DESIGN:OS 12-section AI-Ready README and generate all plugin manifests and /doctor checks."

## 3. Export & Automate

> "Run the 10-gate SEO, AEO, and GEO verification harness across our ecosystem and fix any missing canonical or OG tags."

---

## 4. CLI & Diagnostic Commands

```bash
# Run deterministic offline self-check
python3 scripts/self_check.py

# Run primary domain verification / workflow
python3 scripts/verify-repo-delivery.py . && python3 scripts/seo-aeo-geo-harness.py

# Run primary CLI command
python3 scripts/scaffold-repo-delivery.py --repo-root .
```
