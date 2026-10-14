#!/usr/bin/env python3
"""scaffold-repo-delivery.py — Deterministic AI-Ready Repository Delivery Scaffolder.

Generates or backfills the complete 5-layer DESIGN:OS + diagram-design AI-Ready
delivery package for any DESIGN:OS repository:
  1. Multi-host plugin manifests (.claude-plugin/, .codex-plugin/, .agents/plugins/, .factory-plugin/)
  2. Canonical agent skill (skills/<slug>/SKILL.md) if not already present
  3. Diagnostics & self-check (commands/doctor.md, prompts/doctor.md, scripts/self_check.py)
  4. 5-tab GitHub trust & governance files (PRIVACY.md, SECURITY.md, CONTRIBUTING.md,
     CODE_OF_CONDUCT.md, CHANGELOG.md, LICENSE, root llms.txt, docs/cookbook.md)
  5. 12-Section Editorial + AI-Ready README.md (when --write-readme is passed)
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ECOSYSTEM_TABLE = """| Engine | Live Docs | Repository | Layer |
| :--- | :--- | :--- | :--- |
| **DESIGN:OS CLI** | [jangtrinh.github.io/design-os](https://jangtrinh.github.io/design-os/) | [`jangtrinh/design-os`](https://github.com/jangtrinh/design-os) | `cli` |
| **Knowledge Builder** | [jangtrinh.github.io/design-os-knowledge-builder](https://jangtrinh.github.io/design-os-knowledge-builder/) | [`jangtrinh/design-os-knowledge-builder`](https://github.com/jangtrinh/design-os-knowledge-builder) | `compiler` |
| **Figma Plugin & CLI** | [jangtrinh.github.io/design-os-figma-plugin](https://jangtrinh.github.io/design-os-figma-plugin/) | [`jangtrinh/design-os-figma-plugin`](https://github.com/jangtrinh/design-os-figma-plugin) | `plugin` |
| **SVG Animation Engine** | [jangtrinh.github.io/design-os-svg-animation](https://jangtrinh.github.io/design-os-svg-animation/) | [`jangtrinh/design-os-svg-animation`](https://github.com/jangtrinh/design-os-svg-animation) | `engine` |
| **3D Blender Agent** | [jangtrinh.github.io/design-os-3d-blender](https://jangtrinh.github.io/design-os-3d-blender/) | [`jangtrinh/design-os-3d-blender`](https://github.com/jangtrinh/design-os-3d-blender) | `3d / cad` |
| **OPAH ONE Drone** | [jangtrinh.github.io/design-os-drone-showcase](https://jangtrinh.github.io/design-os-drone-showcase/) | [`jangtrinh/design-os-drone-showcase`](https://github.com/jangtrinh/design-os-drone-showcase) | `hardware` |
| **GitHub Pages Engine** | [jangtrinh.github.io/design-os-github-page](https://jangtrinh.github.io/design-os-github-page/) | [`jangtrinh/design-os-github-page`](https://github.com/jangtrinh/design-os-github-page) | `pages` |
| **Apple Design OS** | [jangtrinh.github.io/design-os-apple](https://jangtrinh.github.io/design-os-apple/) | [`jangtrinh/design-os-apple`](https://github.com/jangtrinh/design-os-apple) | `swiftui` |
| **Agent Teacher** | [jangtrinh.github.io/design-os-pedagogy](https://jangtrinh.github.io/design-os-pedagogy/) | [`jangtrinh/design-os-pedagogy`](https://github.com/jangtrinh/design-os-pedagogy) | `pedagogy` |
| **Origami CAD** | [jangtrinh.github.io/design-os-origami](https://jangtrinh.github.io/design-os-origami/) | [`jangtrinh/design-os-origami`](https://github.com/jangtrinh/design-os-origami) | `packaging` |
| **Voice UX Architecture** | [jangtrinh.github.io/design-os-voice-ux](https://jangtrinh.github.io/design-os-voice-ux/) | [`jangtrinh/design-os-voice-ux`](https://github.com/jangtrinh/design-os-voice-ux) | `voice-ai` |
| **Code2Flow** | [jangtrinh.github.io/design-os-code2flow](https://jangtrinh.github.io/design-os-code2flow/) | [`jangtrinh/design-os-code2flow`](https://github.com/jangtrinh/design-os-code2flow) | `ast / audit` |
| **Generative UI** | [jangtrinh.github.io/design-os-generative-ui](https://jangtrinh.github.io/design-os-generative-ui/) | [`jangtrinh/design-os-generative-ui`](https://github.com/jangtrinh/design-os-generative-ui) | `runtime` |"""


REPO_CATALOG: dict[str, dict] = {
    "design-os": {
        "title": "DESIGN:OS (`design-os`)",
        "display_name": "DESIGN:OS CLI",
        "skill_slug": "design-os",
        "one_line_hook": "Multi-runtime design operating system and CLI for Claude Code, OpenAI Codex, Gemini CLI, and Google Antigravity.",
        "elevator_pitch": "Install once to equip any AI coding agent with 12+ domain design skills, deterministic verification gates, 2:1 axonometric art direction, and live Figma / SVG / 3D / SwiftUI / packaging workflows.",
        "hero_image": "assets/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/design-os.png",
        "keywords": ["design-os", "ai-agents", "claude-code", "codex", "gemini-cli", "design-system", "cli"],
        "quickstart_cmd": "npx @easestart/design-os init",
        "cli_cmd": "npx @easestart/design-os doctor",
        "cli_desc": "Inspect active runtime adapters (Claude Code, Codex, Gemini CLI, Antigravity) and installed skill packs",
        "prompts": [
            "Initialize DESIGN:OS in this repo and wire our design tokens and verification gates for Claude Code and Codex.",
            "Audit our current frontend components against DESIGN:OS typography, spacing, and WCAG 2.2 AA contrast gates.",
            "Scaffold a new product landing page with 2:1 axonometric B&W technical illustrations and SEO/AEO/GEO metadata.",
        ],
        "why_intro": "AI coding agents write functional code quickly, but their default visual output suffers from inconsistent spacing, hallucinated tokens, rainbow badges, and zero verification gates. **DESIGN:OS** turns aesthetic taste and design systems engineering into deterministic, runtime-agnostic contracts.",
        "comparison": [
            ("Visual Quality", "Generic purple-gradient AI slop and ad-hoc CSS", "Token-locked typography, 8pt modular grid, and 2:1 axonometric art direction"),
            ("Context Budget", "Dumping massive style guides into every prompt", "Progressive skill disclosure (`SKILL.md` router + on-demand domain packs)"),
            ("Verification", "Visual eyeballing with zero automated checks", "Deterministic CLI gates (`self_check.py`, contrast, and anti-flop audits)"),
            ("Multi-Agent Parity", "Locked to a single IDE or proprietary prompt format", "One canonical skill tree across Claude Code, Codex, Gemini CLI & Antigravity"),
        ],
        "deliverables": [
            ("Multi-Runtime Skill Pack", "Wiring Claude Code, Codex, Gemini CLI, and Antigravity to one design standard", ".claude-plugin + skills/", "python3 scripts/self_check.py"),
            ("Design System Tokens & Gates", "Enforcing spacing, typography, and WCAG 2.2 AA contrast in CI", "JSON / CSS / CLI exit code", "Zero contrast or grid violations"),
            ("Cross-Engine Orchestration", "Routing tasks to Figma, SVG Animation, 3D Blender, Apple SwiftUI, or Origami CAD", "Verified domain artifacts", "13-engine ecosystem parity"),
        ],
        "when_not": [
            "Throwaway backend scripts with zero user-facing UI, CLI, or documentation surface.",
            "Teams looking for a hosted cloud SaaS design tool rather than a local-first, git-tracked engineering toolchain.",
            "Replacing human brand strategy — DESIGN:OS enforces and scales design systems, not customer discovery.",
        ],
    },
    "design-os-github-page": {
        "title": "DESIGN:OS GitHub Pages & README Engine (`design-os-github-page`)",
        "display_name": "DESIGN:OS GitHub Pages Engine",
        "skill_slug": "design-os-github-page",
        "one_line_hook": "Zero-dependency 9-tier GitHub Pages marketing scaffolder, AI-Ready repository delivery generator, and 10-gate SEO / AEO / GEO verification harness.",
        "elevator_pitch": "Turn any open-source repository, developer profile, or organization into a high-converting editorial publication with JSON-LD knowledge graphs, `llms.txt` discovery, multi-host agent plugin manifests, and 12-section `README.md` blueprints.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/github-page.png",
        "keywords": ["github-pages", "readme-template", "seo", "aeo", "geo", "llms-txt", "claude-plugin", "design-os"],
        "quickstart_cmd": "python3 scripts/verify-repo-delivery.py . && python3 scripts/seo-aeo-geo-harness.py",
        "cli_cmd": "python3 scripts/scaffold-repo-delivery.py --repo-root .",
        "cli_desc": "Scaffold or backfill `.claude-plugin`, `.codex-plugin`, `skills/`, `/doctor`, governance files, and 12-section `README.md`",
        "prompts": [
            "Scaffold a 9-tier editorial GitHub Pages site in docs/ with JSON-LD SoftwareSourceCode + FAQPage schemas and llms.txt.",
            "Upgrade this repository to the DESIGN:OS 12-section AI-Ready README and generate all plugin manifests and /doctor checks.",
            "Run the 10-gate SEO, AEO, and GEO verification harness across our ecosystem and fix any missing canonical or OG tags.",
        ],
        "why_intro": "Most open-source repositories ship with a barebones README, broken badges, zero AI agent plugin manifests, and no structured metadata for search or LLM answer engines. **`design-os-github-page`** codifies both the 9-tier GitHub Pages marketing site and the 5-layer AI-Ready repository delivery standard.",
        "comparison": [
            ("Repository Delivery", "Prose-only README with missing install manifests or governance files", "5-layer AI-Ready package (`.claude-plugin`, `.codex-plugin`, `skills/`, `/doctor`, 5-tab governance)"),
            ("README Architecture", "Unstructured wall of text or generic boilerplate", "12-Section Editorial Blueprint with jump nav, comparison table, and `What loads when`"),
            ("Search & AI Discovery", "Invisible to ChatGPT Search, Perplexity, and Claude web grounding", "10-gate SEO / AEO / GEO harness (`JSON-LD @graph`, `FAQPage`, `llms.txt`, `sitemap.xml`)"),
            ("Build Dependencies", "Heavy Node/React static-site generators that rot in 6 months", "Zero-dependency HTML/CSS + Python stdlib generators that run anywhere in <1s"),
        ],
        "deliverables": [
            ("9-Tier GitHub Pages Site", "Launching an editorial product landing page in `docs/` or `site/`", "HTML5 + CSS + JSON-LD + llms.txt", "scripts/seo-aeo-geo-harness.py (10/10 PASS)"),
            ("AI-Ready Repo Delivery Package", "Equipping any repo with multi-agent plugins, `/doctor`, and 5-tab GitHub governance", ".claude-plugin + skills/ + PRIVACY.md", "scripts/verify-repo-delivery.py (5/5 PASS)"),
            ("Profile & Org READMEs", "Upgrading `<user>/<user>` and `.github/profile/README.md` with B&W art direction", "Markdown + 2:1 Isometric PNGs", "UKMC.v1 knowledge contract verification"),
        ],
        "when_not": [
            "Dynamic multi-tenant web applications requiring server-side databases or authenticated user sessions.",
            "Private internal scratchpads that should never be indexed by search engines or AI answer engines.",
            "Heavy interactive 3D/video showcases where a dedicated runtime (`design-os-svg-animation` or `design-os-3d-blender`) is needed.",
        ],
    },
    "design-os-knowledge-builder": {
        "title": "DESIGN:OS Knowledge Builder (`design-os-knowledge-builder`)",
        "display_name": "DESIGN:OS Knowledge Builder",
        "skill_slug": "es-knowledge-forge",
        "one_line_hook": "Deterministic multimodal knowledge compiler with `UKMC.v1` schema enforcement, SHA-256 provenance, and a 6-validator epistemic gate.",
        "elevator_pitch": "Compile web documentation, PDFs, codebases, and videos into hallucination-free, token-budgeted knowledge packs (`SKILL.md` + `knowledge/**/*.md`) ready for Claude Code, Codex, Gemini CLI, and Antigravity.",
        "hero_image": "assets/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/knowledge-builder.png",
        "keywords": ["knowledge-compiler", "ukmc", "rag", "agent-skills", "epistemic-gate", "design-os"],
        "quickstart_cmd": "python3 scripts/verify-ukmc.py",
        "cli_cmd": "python3 scripts/verify-ukmc.py",
        "cli_desc": "Run the 6-validator UKMC.v1 epistemic gate across all compiled knowledge nodes",
        "prompts": [
            "Compile these technical RFCs into a UKMC.v1 knowledge pack with SHA-256 source attribution and failure-mode checklists.",
            "Audit our knowledge/ directory with the 6-validator epistemic gate and fix any missing frontmatter or untrusted quarantine flags.",
            "Generate a progressive-disclosure SKILL.md router and llms.txt index for our domain knowledge base.",
        ],
        "why_intro": "Raw RAG chunks and scraped markdown files pollute agent context windows with unverified claims, missing provenance, and prompt-injection risks. **`design-os-knowledge-builder`** compiles raw sources into structured `UKMC.v1` knowledge graphs guarded by a 6-validator epistemic gate.",
        "comparison": [
            ("Provenance & Trust", "Unattributed markdown scrapes with zero hash verification", "Mandatory `source_attribution` (`uri`, `sha256`, `license`, `trust_tier`) on every node"),
            ("Prompt-Injection Safety", "External web text mixed directly into system instructions", "Explicit `quarantine.is_external_untrusted` isolation and sanitization"),
            ("Failure Prevention", "Happy-path notes that omit edge cases", "Mandatory `## When to Use / When NOT` and `>= 5` concrete `## Failure Modes` per node"),
            ("Context Efficiency", "Monolithic dumps that blow the 200k context window", "Progressive disclosure (`SKILL.md` router -> domain index -> leaf node)"),
        ],
        "deliverables": [
            ("UKMC.v1 Knowledge Nodes", "Codifying domain standards with cryptographic source attribution", "Markdown + YAML Frontmatter + Mermaid", "6-validator epistemic gate PASS"),
            ("Agent Skill Routers", "Packaging domain knowledge into portable `skills/<slug>/SKILL.md` bundles", "Progressive-disclosure Skill Pack", "python3 scripts/self_check.py"),
            ("GEO & LLM Indexes", "Publishing machine-readable `llms.txt` and knowledge catalogs", "llms.txt + JSON manifest", "Zero broken local links"),
        ],
        "when_not": [
            "Unstructured creative brainstorming or freeform journaling where strict schema gates add unnecessary friction.",
            "Storing live credentials, secrets, or personally identifiable customer data (PII).",
            "Replacing a transactional SQL/vector database for millions of real-time user records.",
        ],
    },
    "design-os-figma-plugin": {
        "title": "DESIGN:OS Figma Plugin & CLI (`design-os-figma-plugin`)",
        "display_name": "DESIGN:OS Figma Plugin & CLI",
        "skill_slug": "figma-agent",
        "one_line_hook": "Zero-cost live Figma canvas bridge (`figma-agent` CLI + Ease Design Figma Agent plugin) for AI coding agents — works on Figma Free.",
        "elevator_pitch": "Inspect live selections, scan design systems, create frames, bind variables, mutate auto-layout traits, and export visual verification PNGs directly from Claude Code, Codex, Gemini CLI, and Antigravity.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/figma-plugin.png",
        "keywords": ["figma", "figma-plugin", "ai-agents", "claude-code", "codex", "design-tokens", "design-os"],
        "quickstart_cmd": "node bin/figma-agent.mjs status --peek",
        "cli_cmd": "node bin/figma-agent.mjs status --peek",
        "cli_desc": "Check live WebSocket bridge connection to the active Figma canvas without consuming queue commands",
        "prompts": [
            "Inspect the currently selected Figma frame, extract its auto-layout and variable tokens, and build the matching React component.",
            "Scan the active Figma file's design system tokens and create a new 1440x900 pricing section frame using our DLS components.",
            "Update the copy and spacing on the selected hero frame in Figma and export a 2x PNG snapshot to verify visual parity.",
        ],
        "why_intro": "Official read-only Figma MCPs dump 150k+ characters of noisy JSON into your context window and cannot write back to the canvas without expensive enterprise seats. **`design-os-figma-plugin`** pairs a local WebSocket relay with typed CLI commands (`inspect`, `scan-design-system`, `create-frame`, `set-text`, `export-png --assert`) that work on **Figma Free**.",
        "comparison": [
            ("Canvas Write Access", "Read-only REST APIs or enterprise-only beta bridges", "Full bidirectional read + write (`create-frame`, `set-text`, `clone-traits`, `exec-js`) on Figma Free"),
            ("Context Window Usage", "155K-character raw node dumps that overflow agent context", "Compact, depth-controlled `inspect` and `context` summaries"),
            ("Visual Verification", "Blindly mutating nodes without checking the rendered result", "Mandatory `export-png --assert` visual proof loop before and after mutations"),
            ("Privacy & Cost", "Cloud relay servers and paid Dev Mode seat requirements", "100% localhost WebSocket bridge (`127.0.0.1`) with zero external telemetry"),
        ],
        "deliverables": [
            ("Live Canvas Inspection", "Reading exact auto-layout, variables, and typography from the active Figma selection", "Compact JSON / CLI summary", "figma-agent inspect"),
            ("Typed Canvas Mutations", "Creating frames, binding tokens, and updating text/layout directly from the terminal", "Live Figma nodes", "Before/after inspect + export-png --assert"),
            ("Visual Proof Exports", "Rendering high-DPI PNG snapshots of any Figma node for PR/artifact review", "Retina PNG artifact", "Non-empty verified PNG on disk"),
        ],
        "when_not": [
            "Headless CI servers where the Figma Desktop or browser app is not open with the plugin connected.",
            "Converting arbitrary live HTML pages via third-party `html-to-figma` scrapers (use screenshot image fills or native typed frame builders instead).",
            "Editing vector mesh illustrations better suited for `design-os-svg-animation` or `design-os-3d-blender`.",
        ],
    },
    "design-os-svg-animation": {
        "title": "DESIGN:OS SVG Animation Engine (`design-os-svg-animation`)",
        "display_name": "DESIGN:OS SVG Animation Engine",
        "skill_slug": "motion-video-recreation",
        "one_line_hook": "Deterministic vector motion engine, virtual-clock studio player, and 1080p 60fps MP4/WebM launch-video compiler for AI agents.",
        "elevator_pitch": "Author frame-exact UI walkthroughs, decoupled camera/pointer choreography, and 2:1 axonometric vector animations governed by a 10-gate Anti-Flop verification suite.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/svg-animation.png",
        "keywords": ["svg-animation", "motion-design", "launch-video", "virtual-clock", "anti-flop-gate", "design-os"],
        "quickstart_cmd": "python3 scripts/anti-flop-gate.py",
        "cli_cmd": "python3 scripts/anti-flop-gate.py",
        "cli_desc": "Run all 10 Anti-Flop quality gates (Phosphor icons, SVGL brand marks, hotspot concentricity, 60fps frame determinism)",
        "prompts": [
            "Create a 60fps SaaS product launch walkthrough with decoupled camera punch-ins, concentric cursor click ripples, and StudioPlayer controls.",
            "Compile our SVG motion timeline into a self-contained HTML deliverable and run the 10-gate anti-flop verification audit.",
            "Verify that all cursor click hotspots align within <= 1.0px of target interactive bounds across 16:9 and 9:16 safe zones.",
        ],
        "why_intro": "When AI agents generate SVG animations or promo videos freehand, they produce jittery CSS keyframes, drifting cursor tips, fake emoji icons, and non-deterministic frame timing. **`design-os-svg-animation`** enforces a virtual clock (`window.__seekToTime`), decoupled camera/cursor kinematics, authentic Phosphor/SVGL vectors, and a 10-gate Anti-Flop verifier.",
        "comparison": [
            ("Frame Timing", "Wall-clock `requestAnimationFrame` drift and dropped frames", "Exact integer-frame virtual clock (`frame 60 == 1.000000s` at 60fps)"),
            ("Camera & Cursor Motion", "Dizzying simultaneous camera pans and cursor travel", "Strictly decoupled phases (camera settles before pointer travel begins)"),
            ("Icon & Brand Fidelity", "Raw emojis or hallucinated SVG paths", "100% verified Phosphor/Lucide glyphs and official SVGL brand marks"),
            ("Click Concentricity", "Cursor tips missing buttons by 15–40px", "Mathematically audited concentricity (`Δ <= 1.0px` to ripple center)"),
        ],
        "deliverables": [
            ("Universal StudioPlayer HTML", "Self-contained interactive promo player with transport dock and viewport auto-scaler", "Single HTML + JS/CSS runtime", "Gate 9 Universal Player PASS"),
            ("Motion IR & Walkthrough Timeline", "Declarative JSON/JS choreography for camera punches and pointer clicks", "Validated Motion IR JSON", "Gates 5, 6, 7, 8 PASS"),
            ("1080p 60fps Clean Export", "Headless browser frame capture via `?clean=1` virtual clock seeking", "MP4 / WebM / PNG sequence", "10/10 Anti-Flop Gate PASS"),
        ],
        "when_not": [
            "Photorealistic 3D rigid-body simulations or CAD mechanical assemblies (use `design-os-3d-blender`).",
            "Static packaging dielines and print PDFs (use `design-os-origami`).",
            "Quick one-line CSS hover transitions that do not require timeline choreography or video export.",
        ],
    },
    "design-os-3d-blender": {
        "title": "DESIGN:OS 3D Blender Agent (`design-os-3d-blender`)",
        "display_name": "DESIGN:OS 3D Blender Agent",
        "skill_slug": "design-os-3d-blender",
        "one_line_hook": "Parametric 3D mechanical parts generator, headless Blender Python (`bpy`) pipeline, and embedded Three.js CAD showcase engine.",
        "elevator_pitch": "Generate dimensionally accurate gears, enclosures, drone frames, and exploded mechanical assemblies from plain-English specs or JSON parameters, complete with glTF/STL exports and interactive browser inspection.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/3d-blender.png",
        "keywords": ["blender", "3d-cad", "threejs", "parametric-modeling", "gltf", "ai-agents", "design-os"],
        "quickstart_cmd": "python3 scripts/self_check.py",
        "cli_cmd": "python3 scripts/self_check.py",
        "cli_desc": "Verify 3D Blender skill contracts, CAD showcase assets, and repository delivery manifests",
        "prompts": [
            "Generate a parametric 24-tooth helical gear and mounting bracket in headless Blender and export glTF + STL artifacts.",
            "Build an interactive Three.js CAD viewer page with exploded-view scrubbing, wireframe toggle, and orthographic camera presets.",
            "Audit the exported mesh topology for non-manifold edges, zero-area faces, and bounding-box dimensional tolerances.",
        ],
        "why_intro": "Text-to-3D diffusion models produce melted, non-manifold blobs that cannot be 3D-printed, machined, or cleanly animated in web viewers. **`design-os-3d-blender`** drives Blender's Python API (`bpy`) and Three.js deterministically to produce crisp mechanical geometry and interactive CAD showcases.",
        "comparison": [
            ("Geometry Quality", "Melted AI diffusion meshes with non-manifold holes", "Clean parametric `bpy` booleans, bevels, and precision vertex topology"),
            ("Dimensional Accuracy", "Arbitrary unscaled units that fail in slicers", "Millimeter-locked parametric dimensions and bounding-box verification"),
            ("Web Inspection", "Static screenshots with no way to inspect hidden faces", "Embedded Three.js CAD viewer with orbit controls, wireframe, and exploded scrub"),
            ("Reproducibility", "Unrepeatable random seeds", "Git-tracked Python generator scripts and declarative JSON part specs"),
        ],
        "deliverables": [
            ("Parametric `bpy` Part Scripts", "Reproducible headless Blender generation for brackets, gears, and housings", "Python (.py) + JSON spec", "Zero non-manifold edges"),
            ("Print & Web 3D Assets", "Exporting production meshes for 3D printing and real-time web rendering", ".glb / .gltf / .stl / .obj", "Bounding-box & file integrity check"),
            ("Three.js CAD Showcase", "Interactive browser viewer with material switches and exploded assembly scrub", "Self-contained HTML + Three.js", "60fps WebGL render check"),
        ],
        "when_not": [
            "Sheet-metal or paperboard folding dielines where 2D crease patterns govern topology (use `design-os-origami`).",
            "Organic character sculpting or AAA rigged game characters requiring manual ZBrush artistry.",
            "2D vector UI motion walkthroughs (use `design-os-svg-animation`).",
        ],
    },
    "design-os-drone-showcase": {
        "title": "DESIGN:OS OPAH ONE Drone Showcase (`design-os-drone-showcase`)",
        "display_name": "DESIGN:OS OPAH ONE Drone Showcase",
        "skill_slug": "design-os-drone-showcase",
        "one_line_hook": "Reference hardware product showcase and scroll-scrub kinematic storytelling engine for the sub-249g OPAH ONE indoor cinewhoop drone.",
        "elevator_pitch": "Demonstrates how DESIGN:OS combines 2:1 axonometric CAD callouts, scroll-coupled explosion kinematics, acoustic/thrust telemetry tables, and zero-dependency GitHub Pages engineering for physical hardware launches.",
        "hero_image": "site/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/drone-showcase.png",
        "keywords": ["hardware-showcase", "drone", "scroll-kinematics", "industrial-design", "cad-callouts", "design-os"],
        "quickstart_cmd": "python3 scripts/self_check.py",
        "cli_cmd": "python3 scripts/self_check.py",
        "cli_desc": "Verify hardware showcase assets, telemetry specification tables, and AI-Ready delivery gates",
        "prompts": [
            "Scaffold a hardware launch showcase page with scroll-scrubbed exploded assembly stages and BOM specification tables.",
            "Generate 2:1 axonometric technical callout diagrams highlighting propulsion ducts, flight controller stack, and mass budget.",
            "Verify our hardware product page against the DESIGN:OS 10-gate SEO, AEO, and GEO discovery harness.",
        ],
        "why_intro": "Hardware and industrial design teams often struggle to present physical engineering rigor on the web without bloated 50MB WebGL bundles that crash mobile browsers. **`design-os-drone-showcase`** proves how lightweight scroll-coupled kinematics, technical isometric diagrams, and structured specification tables deliver Apple-grade hardware storytelling.",
        "comparison": [
            ("Page Load & Mobile Perf", "50MB unoptimized WebGL scenes that freeze mobile Safari", "Instant-loading progressive assets and 60fps scroll-scrubbed kinematics"),
            ("Engineering Credibility", "Vague marketing adjectives with zero measurable specs", "Exact mass budgets (249g), thrust-to-weight tables, and acoustic dB telemetry"),
            ("Visual Art Direction", "Inconsistent renders mixed with stock photos", "Unified 2:1 axonometric technical line art and high-contrast studio callouts"),
            ("AI & Search Indexing", "Canvas-only text invisible to search crawlers and LLMs", "Semantic HTML specification tables + `JSON-LD` + `llms.txt`"),
        ],
        "deliverables": [
            ("Scroll-Scrub Hardware Stage", "Coupling scroll progress to exploded mechanical assembly callouts", "Zero-dependency HTML/CSS/JS", "60fps scroll & reduced-motion fallback"),
            ("Technical Spec & BOM Ledger", "Presenting mass, power, propulsion, and sensor tolerances clearly", "Semantic HTML + Markdown tables", "100% unit consistency check"),
            ("AEO/GEO Hardware Index", "Making hardware specs citable by AI answer engines and engineering buyers", "site/llms.txt + JSON-LD", "10/10 SEO/AEO/GEO harness PASS"),
        ],
        "when_not": [
            "Flight-controller C++/Rust firmware development or real-time MAVLink ground-control station software.",
            "Purely text-based API libraries with no physical or visual product storytelling surface.",
            "Automated PCB autorouting or aerodynamic CFD simulation.",
        ],
    },
    "design-os-apple": {
        "title": "DESIGN:OS Apple (`design-os-apple`)",
        "display_name": "Apple Design OS",
        "skill_slug": "design-os-apple",
        "one_line_hook": "Native Swift 6.2 & SwiftUI component system, adaptive color engine, and multi-platform specimen verifier for iOS 26, iPadOS 26, and macOS 26.",
        "elevator_pitch": "Ship HIG-compliant SwiftUI interfaces with semantic tokens (`DesignOSAdaptiveColor`), Liquid Glass & tactile depth, Dynamic Type safety, and automated simulator specimen verification.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/apple.png",
        "keywords": ["swiftui", "ios", "macos", "apple-hig", "design-system", "swift-6", "design-os"],
        "quickstart_cmd": "python3 scripts/verify-quickstart-parity.py && python3 scripts/verify-layered-kit.py",
        "cli_cmd": "python3 scripts/verify-quickstart-parity.py",
        "cli_desc": "Verify that published Swift quickstart examples in docs and HTML remain 100% byte-identical and type-safe",
        "prompts": [
            "Build a native SwiftUI settings and telemetry screen using DesignOSApple semantic tokens, 44pt minimum hit targets, and Dynamic Type.",
            "Audit our SwiftUI views against the Apple HIG gate for hardcoded colors, missing accessibility labels, and Reduce Motion fallbacks.",
            "Run the portable contract verifiers for quickstart parity, app style registry, and layered UI-kit specimens.",
        ],
        "why_intro": "AI agents writing SwiftUI frequently hallucinate deprecated modifiers, hardcode hex colors that break in Dark Mode, ignore 44×44pt hit targets, and fail Swift 6 strict concurrency checks. **`design-os-apple`** provides a Swift 6.2 package (`DesignOSApple`) paired with portable Python/Node contract verifiers and native Xcode simulator gates.",
        "comparison": [
            ("Swift 6 Concurrency", "Data-race warnings and `@MainActor` compiler errors", "Strict Swift 6.2 concurrency compliance out of the box"),
            ("Color & Dark Mode", "Hardcoded `Color(hex:)` values that break high-contrast and Dark Mode", "Semantic `DesignOSAdaptiveColor` tokens verified across light/dark appearances"),
            ("Accessibility & HIG", "Tiny tap targets (<44pt) and missing VoiceOver labels", "Enforced >=44pt hit targets, Dynamic Type scaling, and Reduce Motion support"),
            ("Documentation Parity", "README Swift snippets that no longer compile against the library", "Automated `verify-quickstart-parity.py` + native `swiftc` typecheck in CI"),
        ],
        "deliverables": [
            ("`DesignOSApple` Swift Package", "Drop-in SwiftUI tokens, fields, cards, shells, and adaptive colors", "Package.swift + Sources/DesignOSApple", "swift test & verify-release-candidate.sh"),
            ("CalorieCam Reference App", "End-to-end iOS/iPadOS/macOS reference app + local Node analysis server", "Examples/CalorieCam", "scripts/verify-caloriecam.sh"),
            ("Portable Contract Verifiers", "Fast Linux/macOS CI checks for quickstart parity, style registry, and specimens", "scripts/verify-*.py", "Zero drift between code and docs"),
        ],
        "when_not": [
            "Cross-platform React Native, Flutter, or web-only applications (use `design-os` or `design-os-generative-ui`).",
            "Legacy UIKit/AppKit codebases targeting iOS versions below the SwiftUI 6 deployment baseline.",
            "Low-level Metal game engines with no standard HIG control surfaces.",
        ],
    },
    "design-os-pedagogy": {
        "title": "DESIGN:OS Agent Teacher (`design-os-pedagogy`)",
        "display_name": "DESIGN:OS Agent Teacher",
        "skill_slug": "design-os-pedagogy",
        "one_line_hook": "Evidence-graded pedagogy library, cognitive-load curriculum tree runtime, and interactive mastery assessment engine for AI tutoring agents.",
        "elevator_pitch": "Equip AI agents to teach complex technical subjects using Bloom's revised taxonomy, worked-example fading, spaced retrieval, Socratic diagnostic probes, and verifiable learner state machines.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/pedagogy.png",
        "keywords": ["pedagogy", "ai-tutor", "curriculum-design", "cognitive-load", "spaced-repetition", "design-os"],
        "quickstart_cmd": "python3 scripts/self_check.py",
        "cli_cmd": "python3 scripts/self_check.py",
        "cli_desc": "Verify pedagogy skill contracts, curriculum schema integrity, and repository delivery gates",
        "prompts": [
            "Design a 5-stage mastery curriculum tree for distributed consensus (Raft) with prerequisite DAGs and diagnostic transfer questions.",
            "Turn this codebase walkthrough into a worked-example fading sequence with interactive check-for-understanding probes.",
            "Audit our onboarding tutorial for cognitive load violations, missing prerequisite links, and passive wall-of-text explanations.",
        ],
        "why_intro": "When you ask a generic LLM to 'teach me X', it dumps a 2,000-word textbook summary that creates an illusion of competence without testing transfer or managing cognitive load. **`design-os-pedagogy`** gives AI agents a formal instructional design runtime grounded in cognitive science.",
        "comparison": [
            ("Instructional Flow", "Passive 2,000-word wall of text with zero learner checks", "Active worked-example fading, Socratic probes, and gated mastery nodes"),
            ("Curriculum Structure", "Flat bullet lists with hidden prerequisite gaps", "Explicit DAG of prerequisite concepts and Bloom taxonomy target levels"),
            ("Assessment Quality", "Trivial recall trivia ('What does API stand for?')", "Diagnostic misconception probes and near/far transfer challenges"),
            ("Evidence Grading", "Pop-psychology myths (e.g., VARK learning styles)", "Strictly evidence-graded cognitive science (Sweller, Bjork, Roediger, Chi)"),
        ],
        "deliverables": [
            ("Curriculum DAG Specs", "Decomposing a technical domain into prerequisite-ordered mastery nodes", "JSON / Markdown Curriculum Tree", "DAG acyclicity & rubric check"),
            ("Worked-Example Fading Loops", "Transitioning learners from full examples -> partial completion -> independent problem solving", "Interactive Lesson Prompts", "Cognitive-load gate PASS"),
            ("Diagnostic Rubrics", "Detecting specific mental-model bugs before advancing the learner", "Structured Assessment Spec", "python3 scripts/self_check.py"),
        ],
        "when_not": [
            "Pure reference API lookups where an experienced engineer just wants a one-line CLI flag answer.",
            "Clinical, medical, or accredited K-12 compliance grading requiring licensed human oversight.",
            "Automated code generation where the user wants the task finished rather than explained.",
        ],
    },
    "design-os-origami": {
        "title": "17 blanks. 15 with 3D.",
        "display_name": "DESIGN:OS Origami CAD",
        "skill_slug": "es-origami-cad",
        "one_line_hook": "Parametric packaging dielines, Kawasaki/Maekawa foldability verification, spot-color print PDFs/DXFs, and source-derived 3D fold previews.",
        "elevator_pitch": "Generate production-ready tuck boxes, mailers, sleeves, trays, and origami crease patterns with zero third-party Python dependencies and a 13-check mechanical validation gate.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/studio-hq.png",
        "keywords": ["packaging-cad", "dielines", "origami", "pdf", "dxf", "svg", "threejs", "design-os"],
        "quickstart_cmd": "PYTHONPATH=src python3 -B -m unittest discover -s tests -v",
        "cli_cmd": "python3 -B scripts/skill_contract.py --check && python3 -B scripts/sync_host_bundles.py --check",
        "cli_desc": "Verify canonical skill contract and portable host bundle synchronization across Claude Code, Codex, and Gemini",
        "prompts": [
            "Generate a reverse-tuck end carton (120x80x45mm, 0.45mm paperboard) with print bleed, spot-color PDF/DXF dielines, and 3D fold preview.",
            "Validate this packaging output directory across all 13 mechanical checks (topology, Kawasaki/Maekawa, DXF layers, and printer spots).",
            "Render a 9-panel visual inspection contact sheet for our sleeve-and-tray packaging spec and verify zero panel collisions.",
        ],
        "why_intro": "Asking a general LLM to draw a packaging dieline produces disconnected SVG lines that cannot fold in 3D, lack paperboard caliper allowances, and fail commercial die-cutting separation checks. **`design-os-origami`** is a pure-Python stdlib parametric CAD engine with topological graph verification, spot-color PDF/DXF generation, and source-derived 3D fold kinematics.",
        "comparison": [
            ("Fold Topology", "Hallucinated SVG rectangles with unattached flaps", "Mathematically verified planar face graph + Kawasaki/Maekawa flat-foldability checks"),
            ("Printer Exchange", "RGB screen drawings rejected by pre-press RIPs", "True `/Separation` spot-color PDF (`CUT`, `CREASE_VALLEY`, `CREASE_MOUNTAIN`, `BLEED`) + R2000 DXF"),
            ("3D Fold Preview", "Fake decorative mockups disconnected from the dieline", "Exact polygon faces and signed hinge angles derived directly from the 2D crease pattern"),
            ("Runtime Footprint", "Heavy CAD binaries or cloud subscriptions", "100% Python standard library runtime (`dependencies = []`)"),
        ],
        "deliverables": [
            ("Production Dieline Suite", "Generating cutter-ready vector files with caliper & bleed allowances", "SVG + Spot-Color PDF + AutoCAD DXF + FOLD JSON", "13-check validate.py gate PASS"),
            ("Interactive 3D Fold Viewer", "Inspecting flat-to-folded hinge progression in the browser", "Self-contained HTML + fold-model JSON", "preview_records_match parity check"),
            ("9-Panel Visual Evidence Sheet", "Headless Chromium inspection sheet (`L1`–`L9`) for human pre-press review", "evidence/look-sheet.png + receipt.json", "look.py 9-checkpoint verifier"),
        ],
        "when_not": [
            "Curved thermoformed plastic blisters, blow-molded bottles, or injection-molded enclosures (use `design-os-3d-blender`).",
            "Substituting for physical sample cutting on your target paperboard stock (`PHYSICAL_FOLD_FIT` always requires a real physical sample).",
            "Freeform artistic illustration unrelated to foldable sheet geometry.",
        ],
    },
    "design-os-voice-ux": {
        "title": "DESIGN:OS Voice UX & AI Agent Architecture (`design-os-voice-ux`)",
        "display_name": "DESIGN:OS Voice UX",
        "skill_slug": "design-os-voice-ux",
        "one_line_hook": "Production engineering handbook, full-duplex barge-in state machines, sub-500ms latency budgets, and 6-dimension audit rubric for real-time voice AI agents.",
        "elevator_pitch": "Design and audit voice AI experiences that handle interruptions gracefully, mask tool-call latency with natural earcons/fillers, and degrade cleanly across noisy mobile networks.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/voice-ux.png",
        "keywords": ["voice-ai", "voice-ux", "barge-in", "full-duplex", "latency-budget", "ai-agents", "design-os"],
        "quickstart_cmd": "python3 scripts/self_check.py",
        "cli_cmd": "python3 scripts/self_check.py",
        "cli_desc": "Verify Voice UX skill contracts, rubric references, and AI-Ready repository delivery files",
        "prompts": [
            "Audit our WebRTC voice agent architecture against the 6-dimension Voice UX rubric (latency, barge-in FSM, turn-taking, and error recovery).",
            "Design a full-duplex barge-in finite state machine with acoustic echo cancellation guards and <200ms TTS cut-off.",
            "Create a tool-call latency choreography spec for a voice banking agent when downstream API calls take 800ms–2500ms.",
        ],
        "why_intro": "Most voice AI demos work in a quiet room when the user speaks in complete sentences and waits politely, then collapse in production when users interrupt (`barge-in`), pause mid-thought, or trigger slow tool calls. **`design-os-voice-ux`** codifies the systems engineering and interaction design required for sub-500ms full-duplex voice agents.",
        "comparison": [
            ("Turn-Taking & Barge-In", "Half-duplex walkie-talkie pipelines that talk over the user", "Full-duplex FSM with VAD debounce and <200ms TTS cancellation"),
            ("Latency Budgeting", "Unbounded 3-second silences while waiting for LLM + TTS", "Stage-by-stage p50/p95 latency budgets (VAD + STT + LLM TTFT + TTS first byte < 500ms)"),
            ("Tool-Call Handling", "Dead air while an external API executes", "Tiered acoustic fillers, progress earcons, and async state confirmation"),
            ("Modality Handoff", "Forcing voice to read out 16-digit URLs or tables", "Multimodal voice + visual card synchronization for high-density data"),
        ],
        "deliverables": [
            ("Full-Duplex Barge-In FSM", "Specifying exact state transitions across `LISTENING`, `THINKING`, `SPEAKING`, and `INTERRUPTED`", "State Machine Spec + Mermaid", "Zero deadlocks or double-talk states"),
            ("Sub-500ms Latency Budget", "Allocating millisecond budgets across transport, VAD, ASR, LLM, and streaming TTS", "Latency Budget Table", "p50 <= 500ms / p95 <= 900ms gate"),
            ("6-Dimension Voice UX Audit", "Scoring an existing voice agent across turn-taking, prosody, repair, and safety", "Scored Audit Report", "6-dimension rubric verification"),
        ],
        "when_not": [
            "Asynchronous voice-note transcription apps where real-time conversational turn-taking is not required.",
            "Training raw acoustic speech-to-text (ASR) neural network weights from scratch.",
            "Purely text-based chat interfaces with no audio/speech modality.",
        ],
    },
    "design-os-code2flow": {
        "title": "DESIGN:OS Code2Flow (`design-os-code2flow`)",
        "display_name": "DESIGN:OS Code2Flow",
        "skill_slug": "design-os-code2flow",
        "one_line_hook": "Local-first AST codebase-to-user-flow mapper and 11-heuristic UX gap auditor across 7 frontend and mobile frameworks.",
        "elevator_pitch": "Statically analyze Next.js, React Router, TanStack Router, Expo Router, SwiftUI, Flutter, and Jetpack Compose repositories to generate Mermaid user-flow graphs and catch dead-end screens, missing error boundaries, and unguarded auth routes.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/jangtrinh/assets/art-direction/code2flow.png",
        "keywords": ["code2flow", "user-flow", "ux-audit", "static-analysis", "nextjs", "swiftui", "mermaid", "design-os"],
        "quickstart_cmd": "npm test",
        "cli_cmd": "node bin/code2flow.mjs audit .",
        "cli_desc": "Scan a frontend or mobile repository, emit Mermaid user-flow diagrams, and run the 11-heuristic UX gap audit",
        "prompts": [
            "Scan this Next.js App Router repository with code2flow, generate the Mermaid user-flow diagram, and list all high-severity UX gaps.",
            "Audit our SwiftUI navigation stack for dead-end screens, missing loading/error states, and unguarded destructive actions.",
            "Export a JSON + Markdown user-flow topology report for our PR review gate.",
        ],
        "why_intro": "Product teams rarely keep user-flow diagrams in sync with production code, and AI agents frequently ship screens with missing loading states, dead-end routes, or unauthenticated pages. **`design-os-code2flow`** parses your actual source files locally to extract the real route graph and audit it against 11 structural UX heuristics.",
        "comparison": [
            ("Source of Truth", "Outdated Figma flowcharts that drifted from code months ago", "Directly extracted from live route files, AST navigation calls, and layouts"),
            ("Framework Coverage", "Single-framework scripts that break on mobile or monorepos", "Unified analyzer for Next.js, React Router, TanStack, Expo, SwiftUI, Flutter & Compose"),
            ("UX Defect Detection", "Manual QA clicking through every screen after deployment", "Automated 11-heuristic static audit (dead ends, missing error/loading states, auth leaks)"),
            ("Privacy & Speed", "Uploading proprietary source code to third-party SaaS scanners", "100% local execution in milliseconds with zero network calls"),
        ],
        "deliverables": [
            ("Mermaid User-Flow Graph", "Visualizing every route, modal, redirect, and navigation edge in the codebase", "Mermaid (.mmd / Markdown)", "100% route discovery parity"),
            ("11-Heuristic UX Audit Report", "Flagging dead ends, orphan screens, missing error boundaries, and auth gaps", "Markdown + JSON Diagnostics", "Exit code gate for CI/CD"),
            ("Programmatic AST SDK", "Embedding route-graph extraction and UX auditing inside custom agent workflows", "TypeScript / ESM SDK", "npm test suite PASS"),
        ],
        "when_not": [
            "Pure backend microservices or CLI tools with no screen/route navigation graph.",
            "Visual pixel-level contrast or typography inspection (pair with `design-os` or `design-os-figma-plugin`).",
            "Runtime profiling of database query latency.",
        ],
    },
    "design-os-generative-ui": {
        "title": "DESIGN:OS Generative UI (`design-os-generative-ui`)",
        "display_name": "DESIGN:OS Generative UI",
        "skill_slug": "design-os-generative-ui",
        "one_line_hook": "Stream-first interactive visual runtime for AI agents — 60fps `morphdom` DOM reconciliation, streaming HTML sanitizer, and WebGL/Canvas widget bridge.",
        "elevator_pitch": "Render live-streaming interactive calculators, 3D scenes, charts, and explorable explanations inside Claude Artifacts, ChatGPT Canvas, Gemini, and custom agent webviews with zero flicker.",
        "hero_image": "docs/images/cover.png",
        "source_image": "/Users/jang/Products/easestart-.github/assets/art-direction/ease-ui.png",
        "keywords": ["generative-ui", "morphdom", "streaming-html", "claude-artifacts", "webgl", "ai-agents", "design-os"],
        "quickstart_cmd": "npm test",
        "cli_cmd": "npm test",
        "cli_desc": "Run the streaming sanitizer, morphdom reconciliation, and DesignOSBridge test suite",
        "prompts": [
            "Build a stream-safe interactive compound-interest and Monte Carlo simulator widget using DesignOSBridge and Chart.js.",
            "Wrap our LLM token stream in createStreamRenderer so incomplete HTML tags reconcile at 60fps via morphdom without resetting canvas state.",
            "Audit this generative UI widget against the DESIGN:OS interactive widget guidelines (zero raw emojis, dark-mode adaptive tokens, and XSS sanitization).",
        ],
        "why_intro": "Naively setting `innerHTML` on an LLM token stream causes severe layout thrashing, destroys active `<canvas>` / `<input>` state on every chunk, and opens XSS vectors. **`design-os-generative-ui`** provides a stream-healer, sanitizer, and 60fps `morphdom` reconciler (`createStreamRenderer` + `DesignOSBridge`) purpose-built for AI agent artifacts.",
        "comparison": [
            ("Streaming DOM Updates", "`element.innerHTML = chunk` flashes white and resets inputs on every token", "60fps `morphdom` diffing that preserves `<canvas>`, WebGL, and focused input state"),
            ("Incomplete Tag Healing", "Broken layout while `<svg>` or `<table>` tags are mid-stream", "Deterministic tag auto-healing and script execution deferral until stream completion"),
            ("Security & XSS", "Unsanitized LLM output executing inline `onerror=` payloads", "Strict streaming sanitizer stripping dangerous attributes and untrusted scripts"),
            ("Host Communication", "Isolated iframes that cannot send user actions back to the agent", "Bidirectional `DesignOSBridge` (`sendPrompt`, state sync, theme adaptation)"),
        ],
        "deliverables": [
            ("Streaming DOM Reconciler", "Rendering partial LLM HTML/SVG chunks smoothly at 60fps", "createStreamRenderer (ESM/Browser)", "Zero layout thrash or state loss"),
            ("Bidirectional Host Bridge", "Connecting interactive widget controls back to the host AI agent conversation", "DesignOSBridge SDK", "Full unit & integration test PASS"),
            ("Generative Widget Guidelines", "Teaching agents how to compose Charts, KaTeX, Mermaid, and Three.js widgets", "skills/design-os-generative-ui/SKILL.md", "python3 scripts/self_check.py"),
        ],
        "when_not": [
            "Static marketing landing pages that are not streamed or dynamically generated by an AI agent (use `design-os-github-page`).",
            "Native iOS/macOS SwiftUI applications (use `design-os-apple`).",
            "Server-side batch PDF generation (use `design-os-origami`).",
        ],
    },
}


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_plugin_manifests(root: Path, slug: str, cfg: dict, preserve_claude_agents: bool = False) -> None:
    base_plugin = {
        "name": slug,
        "description": cfg["one_line_hook"],
        "version": "1.0.0",
        "author": {
            "name": "Jang Trinh",
            "url": "https://github.com/jangtrinh",
        },
        "homepage": f"https://jangtrinh.github.io/{slug}/",
        "repository": f"https://github.com/jangtrinh/{slug}",
        "license": "MIT",
        "keywords": cfg["keywords"],
    }
    base_marketplace = {
        "name": slug,
        "metadata": {
            "description": cfg["one_line_hook"],
        },
        "owner": {
            "name": "Jang Trinh",
        },
        "plugins": [
            {
                "name": slug,
                "source": "./",
            }
        ],
    }

    if not preserve_claude_agents:
        write_json(root / ".claude-plugin/plugin.json", base_plugin)
        write_json(root / ".claude-plugin/marketplace.json", base_marketplace)
        write_json(
            root / ".agents/plugins/marketplace.json",
            {
                "name": slug,
                "interface": {
                    "displayName": cfg["display_name"],
                },
                "plugins": [
                    {
                        "name": slug,
                        "source": {
                            "source": "local",
                            "path": "./",
                        },
                        "policy": {
                            "installation": "AVAILABLE",
                            "authentication": "ON_INSTALL",
                        },
                        "category": "Developer Tools",
                    }
                ],
            },
        )

    codex_plugin = {
        **base_plugin,
        "skills": "./skills/",
        "interface": {
            "displayName": cfg["display_name"],
            "shortDescription": cfg["one_line_hook"],
            "longDescription": cfg["elevator_pitch"],
            "developerName": "DESIGN:OS",
            "category": "Developer Tools",
            "capabilities": ["Read", "Write"],
            "websiteURL": f"https://jangtrinh.github.io/{slug}/",
            "privacyPolicyURL": f"https://github.com/jangtrinh/{slug}/blob/main/PRIVACY.md",
            "defaultPrompt": cfg["prompts"],
            "brandColor": "#202020",
            "logo": f"./{cfg['hero_image']}",
        },
    }
    write_json(root / ".codex-plugin/plugin.json", codex_plugin)
    write_json(root / ".factory-plugin/plugin.json", base_plugin)
    write_json(root / ".factory-plugin/marketplace.json", base_marketplace)


def ensure_skill(root: Path, slug: str, cfg: dict) -> str:
    skills_dir = root / "skills"
    existing = sorted(skills_dir.glob("*/SKILL.md")) if skills_dir.is_dir() else []
    if existing:
        # Ensure YAML frontmatter exists on all existing SKILL.md files
        for sf in existing:
            text = sf.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                skill_name = sf.parent.name
                fm = (
                    f"---\n"
                    f"name: {skill_name}\n"
                    f'description: "{cfg["one_line_hook"]}"\n'
                    f"---\n\n"
                )
                sf.write_text(fm + text, encoding="utf-8")
        return existing[0].parent.name

    skill_slug = cfg["skill_slug"]
    skill_path = root / "skills" / skill_slug / "SKILL.md"
    skill_path.parent.mkdir(parents=True, exist_ok=True)
    prompts_md = "\n".join(f'- `"{p}"`' for p in cfg["prompts"])
    content = f"""---
name: {skill_slug}
description: "Use when working with {cfg['display_name']} — {cfg['one_line_hook']}"
---

# {cfg['display_name']} (`{skill_slug}`)

{cfg['elevator_pitch']}

## When to Use

Activate this skill when the user asks to:
{prompts_md}

## Progressive Disclosure Routing (`What loads when`)

1. **Always Loaded**: `skills/{skill_slug}/SKILL.md` (this router — keeps context lean).
2. **On Demand — Prompt Recipes**: Load `docs/cookbook.md` when selecting multi-step workflows or copy-paste prompt templates.
3. **On Demand — Diagnostics**: Load `commands/doctor.md` or run `python3 scripts/self_check.py` when verifying installation or troubleshooting.
4. **On Demand — Ecosystem Discovery**: Load `llms.txt` when cross-referencing companion `DESIGN:OS` engines.

## Core Execution Workflow

1. **Inspect Context**: Read the target repository or workspace constraints before mutating files.
2. **Execute Deterministically**: Run `{cfg['quickstart_cmd']}` or `{cfg['cli_cmd']}` rather than guessing outputs freehand.
3. **Verify Quality Gates**: Run `python3 scripts/self_check.py` and confirm zero errors before reporting completion.

## Quality Bar & Anti-Scope

### It's working if...
- `python3 scripts/self_check.py` exits `0`.
- Outputs match the `DESIGN:OS` 2:1 axonometric B&W art direction and deterministic verification gates.
- Execution remains 100% local with zero external telemetry (`PRIVACY.md`).

### When NOT to use
- {cfg['when_not'][0]}
- {cfg['when_not'][1]}
- {cfg['when_not'][2]}
"""
    skill_path.write_text(content, encoding="utf-8")
    return skill_slug


def write_doctor_and_self_check(root: Path, slug: str, skill_slug: str, cfg: dict) -> None:
    doctor_md = f"""---
description: Diagnose {cfg['display_name']} installation, plugin manifests, skill files, and local verification gates
allowed-tools: Bash, Read, Glob
---

# `{slug}` `/doctor` Diagnostics

Run a read-only diagnostic check of the `{slug}` installation and repository health. Do **not** modify, create, or delete any files during this check.

## Steps

1. **Run the deterministic self-check script** when inside a `{slug}` checkout:
   ```bash
   python3 scripts/self_check.py
   ```
2. **Check installed skill locations** across active agent harnesses:
   - Claude Code: `~/.claude/skills/{skill_slug}/SKILL.md` or `.claude-plugin/marketplace.json`
   - OpenAI Codex: `~/.codex/skills/{skill_slug}/SKILL.md` or `.codex-plugin/plugin.json`
   - Gemini CLI / Antigravity: `~/.gemini/skills/{skill_slug}/SKILL.md`
   - Cross-agent `.agents`: `~/.agents/skills/{skill_slug}/SKILL.md`
3. **Report a concise health table** covering:
   - Manifest integrity (`.claude-plugin`, `.codex-plugin`, `.agents/plugins`, `.factory-plugin`)
   - Canonical skill (`skills/{skill_slug}/SKILL.md`)
   - Trust & privacy governance (`PRIVACY.md`, `SECURITY.md`, `LICENSE`)
   - Domain command readiness (`{cfg['cli_cmd']}`)
"""
    for rel in ("commands/doctor.md", "prompts/doctor.md"):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(doctor_md, encoding="utf-8")

    self_check_py = f'''#!/usr/bin/env python3
"""self_check.py — Deterministic offline self-check for {slug}."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_JSON = (
    ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    ".factory-plugin/plugin.json",
    ".factory-plugin/marketplace.json",
)

REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "PRIVACY.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "llms.txt",
    "docs/cookbook.md",
    "commands/doctor.md",
    "prompts/doctor.md",
)


def main() -> int:
    issues: list[str] = []
    for rel in REQUIRED_JSON:
        p = ROOT / rel
        if not p.is_file():
            issues.append(f"missing JSON manifest: {{rel}}")
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                issues.append(f"manifest is not a JSON object: {{rel}}")
        except Exception as exc:
            issues.append(f"invalid JSON in {{rel}}: {{exc}}")

    for rel in REQUIRED_FILES:
        p = ROOT / rel
        if not p.is_file() or p.stat().st_size == 0:
            issues.append(f"missing or empty required file: {{rel}}")

    skills = list((ROOT / "skills").glob("*/SKILL.md")) if (ROOT / "skills").is_dir() else []
    if not skills:
        issues.append("missing skills/<slug>/SKILL.md")

    if issues:
        for item in issues:
            print(f"FAIL: {{item}}", file=sys.stderr)
        return 1

    print("ok: {slug} self-check passed ({skill_slug})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''
    sc_path = root / "scripts/self_check.py"
    sc_path.parent.mkdir(parents=True, exist_ok=True)
    sc_path.write_text(self_check_py, encoding="utf-8")
    sc_path.chmod(0o755)


def write_governance_and_cookbook(root: Path, slug: str, skill_slug: str, cfg: dict) -> None:
    privacy_md = f"""# Privacy Policy (`{slug}`)

`{slug}` (`{cfg['display_name']}`) is a local-first open-source engineering tool and AI agent skill in the **DESIGN:OS** ecosystem.

## Zero Telemetry Guarantee

- **No network calls by the skill or CLI**: `{slug}` does not phone home, collect analytics, or transmit source code, prompts, or generated artifacts to any external server.
- **No third-party tracking**: There are no embedded telemetry beacons, crash reporters, or usage trackers in `skills/`, `scripts/`, or plugin manifests.
- **100% local execution**: All file reads, validations, and builds happen inside your local workspace and under your active AI coding agent's permission model.
- **Auditable source**: Every script and prompt in this repository is plain-text Markdown, Python, or JavaScript/Swift under the [MIT License](LICENSE).

## Contact

For privacy or security questions, see [`SECURITY.md`](SECURITY.md) or open an issue on [`jangtrinh/{slug}`](https://github.com/jangtrinh/{slug}).
"""
    (root / "PRIVACY.md").write_text(privacy_md, encoding="utf-8")

    security_path = root / "SECURITY.md"
    if not security_path.is_file():
        security_path.write_text(
            f"""# Security Policy (`{slug}`)

## Supported Versions

| Version | Supported |
| :--- | :--- |
| `1.x` / `main` | Yes |

## Security Model

- `{slug}` executes locally with **zero external telemetry** (see [`PRIVACY.md`](PRIVACY.md)).
- Diagnostic commands (`/doctor` and `python3 scripts/self_check.py`) are strictly read-only verification checks.

## Reporting a Vulnerability

Please report suspected vulnerabilities via [GitHub Security Advisories](https://github.com/jangtrinh/{slug}/security/advisories/new) rather than public issues. We acknowledge reports within 48 hours.
""",
            encoding="utf-8",
        )

    contributing_path = root / "CONTRIBUTING.md"
    if not contributing_path.is_file():
        contributing_path.write_text(
            f"""# Contributing to `{slug}`

Thank you for contributing to **{cfg['display_name']}** (`DESIGN:OS`).

## Verification Gate Before Submitting a PR

Every pull request must pass the local self-check and repository test suite before merge:

```bash
python3 scripts/self_check.py
{cfg['quickstart_cmd']}
```

## Guidelines

1. **Zero Telemetry**: Never introduce external network calls, analytics, or unpinned runtime dependencies.
2. **Progressive Context Disclosure**: Keep `skills/{skill_slug}/SKILL.md` concise (~150 lines) and place detailed recipes in `docs/cookbook.md`.
3. **Conventional Commits**: Use `feat:`, `fix:`, `docs:`, or `chore:` commit prefixes.
""",
            encoding="utf-8",
        )

    coc_path = root / "CODE_OF_CONDUCT.md"
    if not coc_path.is_file():
        coc_path.write_text(
            """# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, caste, color, religion, or sexual identity and orientation.

## Our Standards

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Focusing on what is best for the overall community

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the maintainers via GitHub repository issues or security advisories. All complaints will be reviewed and investigated promptly and fairly.

## Attribution

Adapted from the [Contributor Covenant](https://www.contributor-covenant.org), version 2.1.
""",
            encoding="utf-8",
        )

    changelog_path = root / "CHANGELOG.md"
    if not changelog_path.is_file():
        changelog_path.write_text(
            f"""# Changelog (`{slug}`)

All notable changes to `{slug}` are documented in this file.

## [1.0.0] - 2026-10-14

### Added
- Standardized **AI-Ready Repository Delivery Package** (`.claude-plugin`, `.codex-plugin`, `.agents/plugins`, `.factory-plugin`).
- Added `/doctor` diagnostic command (`commands/doctor.md`, `prompts/doctor.md`) and offline `scripts/self_check.py`.
- Added 12-Section Editorial `README.md`, `PRIVACY.md`, `docs/cookbook.md`, and 13-engine `DESIGN:OS` ecosystem cross-links.
""",
            encoding="utf-8",
        )

    license_path = root / "LICENSE"
    if not license_path.is_file():
        license_path.write_text(
            """MIT License

Copyright (c) 2026 Jang Trinh (DESIGN:OS)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
            encoding="utf-8",
        )

    cookbook_path = root / "docs/cookbook.md"
    cookbook_path.parent.mkdir(parents=True, exist_ok=True)
    if not cookbook_path.is_file():
        cookbook_path.write_text(
            f"""# `{slug}` Prompt & CLI Cookbook

Copy-paste recipes for **{cfg['display_name']}** (`skills/{skill_slug}/SKILL.md`).

---

## 1. Generate & Scaffold

> "{cfg['prompts'][0]}"

## 2. Audit & Verify

> "{cfg['prompts'][1]}"

## 3. Export & Automate

> "{cfg['prompts'][2]}"

---

## 4. CLI & Diagnostic Commands

```bash
# Run deterministic offline self-check
python3 scripts/self_check.py

# Run primary domain verification / workflow
{cfg['quickstart_cmd']}

# Run primary CLI command
{cfg['cli_cmd']}
```
""",
            encoding="utf-8",
        )

    llms_path = root / "llms.txt"
    docs_llms = root / "docs/llms.txt"
    site_llms = root / "site/llms.txt"
    if not llms_path.is_file():
        if docs_llms.is_file():
            shutil.copyfile(docs_llms, llms_path)
        elif site_llms.is_file():
            shutil.copyfile(site_llms, llms_path)
        else:
            llms_path.write_text(
                f"""# {cfg['display_name']} ({slug})

> {cfg['one_line_hook']}

- Live Documentation: https://jangtrinh.github.io/{slug}/
- Repository: https://github.com/jangtrinh/{slug}
- Canonical Skill: `skills/{skill_slug}/SKILL.md`
- Diagnostics: `python3 scripts/self_check.py` / `/doctor`
- Privacy Policy: `PRIVACY.md` (Zero telemetry, 100% local execution)
""",
                encoding="utf-8",
            )


def ensure_hero_image(root: Path, cfg: dict) -> None:
    target = root / cfg["hero_image"]
    if target.is_file():
        return
    src = Path(cfg["source_image"])
    if src.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, target)


def render_readme(slug: str, skill_slug: str, cfg: dict) -> str:
    c1, c2, c3, c4 = cfg["comparison"]
    d1, d2, d3 = cfg["deliverables"]
    p1, p2, p3 = cfg["prompts"]
    w1, w2, w3 = cfg["when_not"]

    subtitle_line = ""
    if slug == "design-os-origami":
        # Preserve exact # 17 blanks. 15 with 3D. heading required by test_public_products.py
        subtitle_line = "\n### DESIGN:OS Origami CAD (`design-os-origami`)\n"

    return f"""# {cfg['title']}
{subtitle_line}
**{cfg['one_line_hook']}**

{cfg['elevator_pitch']}

<p align="center">
  <img src="{cfg['hero_image']}" alt="{cfg['display_name']} — 2:1 Axonometric Technical Architecture" width="840">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-202020?style=flat-square&labelColor=202020&color=444444" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Claude_Code_%C2%B7_Codex_%C2%B7_Gemini_%C2%B7_Antigravity-skill-202020?style=flat-square&labelColor=202020&color=444444" alt="Compatible agents">
  <a href="commands/doctor.md"><img src="https://img.shields.io/badge/diagnostics-%2Fdoctor-202020?style=flat-square&labelColor=202020&color=444444" alt="Doctor command"></a>
  <a href="https://jangtrinh.github.io/{slug}/"><img src="https://img.shields.io/badge/live_docs-GitHub_Pages-202020?style=flat-square&labelColor=202020&color=444444" alt="Live GitHub Pages"></a>
  <a href="https://buymeacoffee.com/jangtrinh"><img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> · <a href="#what-it-makes">What it makes</a> · <a href="#installation">Install</a> · <a href="#how-it-works">How it works</a> · <a href="#commands--diagnostics">Commands</a> · <a href="#quality-bar--limitations">Limits</a>
</p>

---

## Why this exists

{cfg['why_intro']}

| Dimension | Generic AI / Manual Workflow | {cfg['display_name']} (`DESIGN:OS`) |
| :--- | :--- | :--- |
| **{c1[0]}** | {c1[1]} | {c1[2]} |
| **{c2[0]}** | {c2[1]} | {c2[2]} |
| **{c3[0]}** | {c3[1]} | {c3[2]} |
| **{c4[0]}** | {c4[1]} | {c4[2]} |
| **Privacy & Telemetry** | Opaque cloud telemetry or unverified third-party APIs | **Zero telemetry** — 100% local execution ([`PRIVACY.md`](PRIVACY.md) audited) |

---

## Quickstart

### 1. Install the plugin or CLI

**In Claude Code:**

```text
/plugin marketplace add jangtrinh/{slug}
/plugin install {slug}@{slug}
```

**Or from your terminal (Codex, Gemini CLI, Antigravity, OpenCode, or standalone CLI):**

```bash
git clone https://github.com/jangtrinh/{slug}.git
cd {slug}
{cfg['quickstart_cmd']}
```

### 2. Ask in plain English

Open your project in your AI coding agent and describe what you need:

> "{p1}"

> "{p2}"

> "{p3}"

### 3. Verify your setup

```bash
python3 scripts/self_check.py
```

---

## What it makes

Every deliverable produced by `{slug}` is backed by a deterministic verification gate rather than freehand AI guesswork.

<p align="center">
  <img src="{cfg['hero_image']}" alt="{cfg['display_name']} Output Specimen" width="840"><br>
  <sub>Prompt: <code>"{p1}"</code></sub>
</p>

| Deliverable / Mode | Best for | Output Format | Verification Gate |
| :--- | :--- | :--- | :--- |
| **{d1[0]}** | {d1[1]} | `{d1[2]}` | `{d1[3]}` |
| **{d2[0]}** | {d2[1]} | `{d2[2]}` | `{d2[3]}` |
| **{d3[0]}** | {d3[1]} | `{d3[2]}` | `{d3[3]}` |

---

## Installation

Choose the setup that matches your AI coding agent. Every option installs the same canonical skill (`skills/{skill_slug}/SKILL.md`) and `/doctor` diagnostic suite.

### Claude Code

Run these two commands inside Claude Code:

```text
/plugin marketplace add jangtrinh/{slug}
/plugin install {slug}@{slug}
```

### OpenAI Codex

Install to your personal Codex skills directory:

```bash
git clone https://github.com/jangtrinh/{slug}.git /tmp/{slug}
mkdir -p ~/.codex/skills/{skill_slug} ~/.codex/prompts
cp -R /tmp/{slug}/skills/{skill_slug}/* ~/.codex/skills/{skill_slug}/
cp /tmp/{slug}/prompts/doctor.md ~/.codex/prompts/{skill_slug}-doctor.md
rm -rf /tmp/{slug}
```

### Gemini CLI & Google Antigravity

```bash
git clone https://github.com/jangtrinh/{slug}.git /tmp/{slug}
mkdir -p ~/.gemini/skills/{skill_slug}
cp -R /tmp/{slug}/skills/{skill_slug}/* ~/.gemini/skills/{skill_slug}/
rm -rf /tmp/{slug}
```

### OpenCode, Cursor, Windsurf & Other Agent Harnesses

```bash
git clone https://github.com/jangtrinh/{slug}.git /tmp/{slug}
mkdir -p ~/.agents/skills/{skill_slug}
cp -R /tmp/{slug}/skills/{skill_slug}/* ~/.agents/skills/{skill_slug}/
rm -rf /tmp/{slug}
```

<details>
<summary>Verify or uninstall</summary>

**Verify installation:**

```bash
python3 scripts/self_check.py
```

Or run `/doctor` inside Claude Code / Codex to inspect installed skill paths, plugin manifests, and gate health.

**Uninstall:**

```bash
rm -rf ~/.claude/skills/{skill_slug} ~/.codex/skills/{skill_slug} ~/.gemini/skills/{skill_slug} ~/.agents/skills/{skill_slug}
```

</details>

---

## Usage & Prompt Cookbook

Once installed, `skills/{skill_slug}/SKILL.md` activates automatically when your prompt matches its domain triggers. Browse [`docs/cookbook.md`](docs/cookbook.md) for copy-paste prompt recipes.

**Generate & Scaffold**

```text
"{p1}"
```

**Audit & Verify**

```text
"{p2}"
```

**Export & Automate**

```text
"{p3}"
```

---

## Commands & Diagnostics

| Command | Environment | What it does |
| :--- | :--- | :--- |
| `/doctor` | Claude Code / Codex | Read-only diagnostic check of installed skill paths, plugin manifests, and runtime prerequisites |
| `python3 scripts/self_check.py` | Terminal / CI | Deterministic offline verification of manifests, skill contracts, and governance files |
| `{cfg['cli_cmd']}` | Terminal / CI | {cfg['cli_desc']} |

---

## How it works

1. **Intent Routing** — Your AI agent matches your request against `skills/{skill_slug}/SKILL.md` frontmatter triggers.
2. **Progressive Context Loading** — Only the entry-point `SKILL.md` router loads initially; detailed recipes and scripts load on demand.
3. **Deterministic Execution** — Domain scripts and contracts execute locally with reproducible inputs and outputs.
4. **Gate Verification** — `scripts/self_check.py` and domain verifiers (`{cfg['quickstart_cmd']}`) validate the artifact before completion.
5. **Zero-Telemetry Delivery** — Verified files are written directly to your workspace with zero external network calls.

```text
User Prompt / CLI Invocation
            │
            ▼
┌───────────────────────────────────────────────┐
│ skills/{skill_slug}/SKILL.md
│ Progressive disclosure router & hard rules    │
└───────────┬───────────────────────────────────┘
            │ loads on demand
            ▼
┌───────────────────────────────────────────────┐
│ {cfg['cli_cmd']}
│ Deterministic build & contract enforcement    │
└───────────┬───────────────────────────────────┘
            │ verifies
            ▼
┌───────────────────────────────────────────────┐
│ python3 scripts/self_check.py + /doctor       │
│ Zero-telemetry local verification gate        │
└───────────────────────────────────────────────┘
```

### What loads when

`{slug}` uses progressive context disclosure so your agent's context window stays fast and focused:

| File | Loaded when |
| :--- | :--- |
| `skills/{skill_slug}/SKILL.md` | Always (~100–150 lines) — routing rules, triggers, and execution workflow |
| `docs/cookbook.md` | When selecting multi-step prompt recipes or domain patterns |
| `commands/doctor.md` / `prompts/doctor.md` | Only when running `/doctor` diagnostics |
| `llms.txt` | When indexed by AI answer engines, RAG pipelines, or repo crawlers |

---

## File structure

```text
{slug}/
├── .claude-plugin/
│   ├── plugin.json                 # Claude Code plugin manifest
│   └── marketplace.json            # Claude Code marketplace catalog
├── .codex-plugin/
│   └── plugin.json                 # OpenAI Codex plugin & interface manifest
├── .agents/
│   └── plugins/marketplace.json    # Cross-agent local plugin registry
├── .factory-plugin/
│   ├── plugin.json                 # Factory / Droid plugin manifest
│   └── marketplace.json            # Factory marketplace metadata
├── skills/
│   └── {skill_slug}/
│       └── SKILL.md                # Canonical agent skill entrypoint
├── commands/
│   └── doctor.md                   # /doctor diagnostic slash command
├── prompts/
│   └── doctor.md                   # Codex diagnostic prompt mirror
├── scripts/
│   └── self_check.py               # Deterministic repository & skill self-check
├── docs/
│   ├── cookbook.md                 # Copy-paste prompt recipes by job
│   └── llms.txt                    # GEO / LLM discovery index
├── PRIVACY.md                      # Zero-telemetry & local-first privacy commitment
├── SECURITY.md                     # Vulnerability disclosure & security policy
├── CONTRIBUTING.md                 # Contribution workflow & verification rules
├── CODE_OF_CONDUCT.md              # Contributor Covenant code of conduct
├── CHANGELOG.md                    # Release history
├── llms.txt                        # Root LLM indexing manifest
├── LICENSE                         # MIT License
└── README.md
```

---

## Quality bar & Limitations

### It's working if...

- `python3 scripts/self_check.py` prints `ok: {slug} self-check passed ({skill_slug})` and exits `0`.
- `{cfg['quickstart_cmd']}` passes with zero contract or test regressions.
- Your AI coding agent loads `skills/{skill_slug}/SKILL.md` automatically when given any prompt from [`docs/cookbook.md`](docs/cookbook.md).
- Network traffic during execution remains zero (guaranteed by [`PRIVACY.md`](PRIVACY.md)).

### When not to use

- {w1}
- {w2}
- {w3}

---

## DESIGN:OS Ecosystem

`{slug}` is one of the 13 open-source engines in the **`DESIGN:OS`** ecosystem:

{ECOSYSTEM_TABLE}

---

## Contributing, Governance & License

- **Contributing**: See [`CONTRIBUTING.md`](CONTRIBUTING.md) for pull request guidelines and verification gates (`python3 scripts/self_check.py`).
- **Code of Conduct**: Governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
- **Security & Privacy**: Zero telemetry — see [`SECURITY.md`](SECURITY.md) and [`PRIVACY.md`](PRIVACY.md).
- **Changelog & LLM Index**: Track releases in [`CHANGELOG.md`](CHANGELOG.md) and machine-readable index in [`llms.txt`](llms.txt).
- **License**: [MIT](LICENSE) © [Jang Trinh](https://github.com/jangtrinh).

---

If `{slug}` saves you time, a star on GitHub helps other engineers and AI agents find it.

<p align="left">
  <a href="https://buymeacoffee.com/jangtrinh">
    <img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee">
  </a>
</p>
"""


def scaffold_repo(root: Path, slug: str, write_readme: bool = True) -> None:
    root = root.resolve()
    if slug not in REPO_CATALOG:
        raise ValueError(f"Unknown repository slug {slug!r}; expected one of {sorted(REPO_CATALOG)}")
    cfg = REPO_CATALOG[slug]
    ensure_hero_image(root, cfg)
    preserve_claude_agents = slug == "design-os-origami"
    build_plugin_manifests(root, slug, cfg, preserve_claude_agents=preserve_claude_agents)
    skill_slug = ensure_skill(root, slug, cfg)
    write_doctor_and_self_check(root, slug, skill_slug, cfg)
    write_governance_and_cookbook(root, slug, skill_slug, cfg)
    if write_readme:
        readme_text = render_readme(slug, skill_slug, cfg)
        (root / "README.md").write_text(readme_text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True, help="Target repository checkout root")
    parser.add_argument("--slug", type=str, help="Canonical DESIGN:OS repo slug (defaults to directory name)")
    parser.add_argument("--no-readme", action="store_true", help="Do not overwrite README.md")
    args = parser.parse_args()

    root = args.repo_root.resolve()
    slug = args.slug or root.name
    if slug == "ease-design":
        slug = "design-os"
    elif slug == "code2flow":
        slug = "design-os-code2flow"

    scaffold_repo(root, slug, write_readme=not args.no_readme)
    print(f"Scaffolded AI-Ready Delivery Package for {slug} at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
