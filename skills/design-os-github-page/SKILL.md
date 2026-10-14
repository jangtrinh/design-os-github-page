---
name: design-os-github-page
description: "Use when working with DESIGN:OS GitHub Pages Engine — Zero-dependency 9-tier GitHub Pages marketing scaffolder, AI-Ready repository delivery generator, and 10-gate SEO / AEO / GEO verification harness."
---

# DESIGN:OS GitHub Pages Engine (`design-os-github-page`)

Turn any open-source repository, developer profile, or organization into a high-converting editorial publication with JSON-LD knowledge graphs, `llms.txt` discovery, multi-host agent plugin manifests, and 12-section `README.md` blueprints.

## When to Use

Activate this skill when the user asks to:
- `"Scaffold a 9-tier editorial GitHub Pages site in docs/ with JSON-LD SoftwareSourceCode + FAQPage schemas and llms.txt."`
- `"Upgrade this repository to the DESIGN:OS 12-section AI-Ready README and generate all plugin manifests and /doctor checks."`
- `"Run the 10-gate SEO, AEO, and GEO verification harness across our ecosystem and fix any missing canonical or OG tags."`

## Progressive Disclosure Routing (`What loads when`)

1. **Always Loaded**: `skills/design-os-github-page/SKILL.md` (this router — keeps context lean).
2. **On Demand — Prompt Recipes**: Load `docs/cookbook.md` when selecting multi-step workflows or copy-paste prompt templates.
3. **On Demand — Diagnostics**: Load `commands/doctor.md` or run `python3 scripts/self_check.py` when verifying installation or troubleshooting.
4. **On Demand — Ecosystem Discovery**: Load `llms.txt` when cross-referencing companion `DESIGN:OS` engines.

## Core Execution Workflow

1. **Inspect Context**: Read the target repository or workspace constraints before mutating files.
2. **Execute Deterministically**: Run `python3 scripts/verify-repo-delivery.py . && python3 scripts/seo-aeo-geo-harness.py` or `python3 scripts/scaffold-repo-delivery.py --repo-root .` rather than guessing outputs freehand.
3. **Verify Quality Gates**: Run `python3 scripts/self_check.py` and confirm zero errors before reporting completion.

## Quality Bar & Anti-Scope

### It's working if...
- `python3 scripts/self_check.py` exits `0`.
- Outputs match the `DESIGN:OS` 2:1 axonometric B&W art direction and deterministic verification gates.
- Execution remains 100% local with zero external telemetry (`PRIVACY.md`).

### When NOT to use
- Dynamic multi-tenant web applications requiring server-side databases or authenticated user sessions.
- Private internal scratchpads that should never be indexed by search engines or AI answer engines.
- Heavy interactive 3D/video showcases where a dedicated runtime (`design-os-svg-animation` or `design-os-3d-blender`) is needed.
