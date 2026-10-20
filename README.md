# DESIGN:OS GitHub Pages & README Engine (`design-os-github-page`)

**Zero-dependency 9-tier GitHub Pages marketing scaffolder, AI-Ready repository delivery generator, and 10-gate SEO / AEO / GEO verification harness.**

Turn any open-source repository, developer profile, or organization into a high-converting editorial publication with JSON-LD knowledge graphs, `llms.txt` discovery, multi-host agent plugin manifests, and 12-section `README.md` blueprints.

<p align="center">
  <img src="docs/images/cover.png" alt="DESIGN:OS GitHub Pages Engine — 2:1 Axonometric Technical Architecture" width="840">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-PolyForm_Shield_1.0.0-202020?style=flat-square&labelColor=202020&color=444444" alt="PolyForm Shield 1.0.0 License"></a>
  <img src="https://img.shields.io/badge/Claude_Code_%C2%B7_Codex_%C2%B7_Gemini_%C2%B7_Antigravity-skill-202020?style=flat-square&labelColor=202020&color=444444" alt="Compatible agents">
  <a href="commands/doctor.md"><img src="https://img.shields.io/badge/diagnostics-%2Fdoctor-202020?style=flat-square&labelColor=202020&color=444444" alt="Doctor command"></a>
  <a href="https://jangtrinh.github.io/design-os-github-page/"><img src="https://img.shields.io/badge/live_docs-GitHub_Pages-202020?style=flat-square&labelColor=202020&color=444444" alt="Live GitHub Pages"></a>
  <a href="https://buymeacoffee.com/jangtrinh"><img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> · <a href="#what-it-makes">What it makes</a> · <a href="#installation">Install</a> · <a href="#how-it-works">How it works</a> · <a href="#commands--diagnostics">Commands</a> · <a href="#quality-bar--limitations">Limits</a>
</p>

---

## Why this exists

Most open-source repositories ship with a barebones README, broken badges, zero AI agent plugin manifests, and no structured metadata for search or LLM answer engines. **`design-os-github-page`** codifies both the 9-tier GitHub Pages marketing site and the 5-layer AI-Ready repository delivery standard.

| Dimension | Generic AI / Manual Workflow | DESIGN:OS GitHub Pages Engine (`DESIGN:OS`) |
| :--- | :--- | :--- |
| **Repository Delivery** | Prose-only README with missing install manifests or governance files | 5-layer AI-Ready package (`.claude-plugin`, `.codex-plugin`, `skills/`, `/doctor`, 5-tab governance) |
| **README Architecture** | Unstructured wall of text or generic boilerplate | 12-Section Editorial Blueprint with jump nav, comparison table, and `What loads when` |
| **Search & AI Discovery** | Invisible to ChatGPT Search, Perplexity, and Claude web grounding | 10-gate SEO / AEO / GEO harness (`JSON-LD @graph`, `FAQPage`, `llms.txt`, `sitemap.xml`) |
| **Build Dependencies** | Heavy Node/React static-site generators that rot in 6 months | Zero-dependency HTML/CSS + Python stdlib generators that run anywhere in <1s |
| **Privacy & Telemetry** | Opaque cloud telemetry or unverified third-party APIs | **Zero telemetry** — 100% local execution ([`PRIVACY.md`](PRIVACY.md) audited) |

---

## Quickstart

### 1. Install the plugin or CLI

**In Claude Code:**

```text
/plugin marketplace add jangtrinh/design-os-github-page
/plugin install design-os-github-page@design-os-github-page
```

**Or from your terminal (Codex, Gemini CLI, Antigravity, OpenCode, or standalone CLI):**

```bash
git clone https://github.com/jangtrinh/design-os-github-page.git
cd design-os-github-page
python3 scripts/verify-repo-delivery.py . && python3 scripts/seo-aeo-geo-harness.py
```

### 2. Ask in plain English

Open your project in your AI coding agent and describe what you need:

> "Scaffold a 9-tier editorial GitHub Pages site in docs/ with JSON-LD SoftwareSourceCode + FAQPage schemas and llms.txt."

> "Upgrade this repository to the DESIGN:OS 12-section AI-Ready README and generate all plugin manifests and /doctor checks."

> "Run the 10-gate SEO, AEO, and GEO verification harness across our ecosystem and fix any missing canonical or OG tags."

### 3. Verify your setup

```bash
python3 scripts/self_check.py
```

---

## What it makes

Every deliverable produced by `design-os-github-page` is backed by a deterministic verification gate rather than freehand AI guesswork.

<p align="center">
  <img src="docs/images/cover.png" alt="DESIGN:OS GitHub Pages Engine Output Specimen" width="840"><br>
  <sub>Prompt: <code>"Scaffold a 9-tier editorial GitHub Pages site in docs/ with JSON-LD SoftwareSourceCode + FAQPage schemas and llms.txt."</code></sub>
</p>

| Deliverable / Mode | Best for | Output Format | Verification Gate |
| :--- | :--- | :--- | :--- |
| **9-Tier GitHub Pages Site** | Launching an editorial product landing page in `docs/` or `site/` | `HTML5 + CSS + JSON-LD + llms.txt` | `scripts/seo-aeo-geo-harness.py (10/10 PASS)` |
| **AI-Ready Repo Delivery Package** | Equipping any repo with multi-agent plugins, `/doctor`, and 5-tab GitHub governance | `.claude-plugin + skills/ + PRIVACY.md` | `scripts/verify-repo-delivery.py (5/5 PASS)` |
| **Profile & Org READMEs** | Upgrading `<user>/<user>` and `.github/profile/README.md` with B&W art direction | `Markdown + 2:1 Isometric PNGs` | `UKMC.v1 knowledge contract verification` |

---

## Installation

Choose the setup that matches your AI coding agent. Every option installs the same canonical skill (`skills/design-os-github-page/SKILL.md`) and `/doctor` diagnostic suite.

### Claude Code

Run these two commands inside Claude Code:

```text
/plugin marketplace add jangtrinh/design-os-github-page
/plugin install design-os-github-page@design-os-github-page
```

### OpenAI Codex

Install to your personal Codex skills directory:

```bash
git clone https://github.com/jangtrinh/design-os-github-page.git /tmp/design-os-github-page
mkdir -p ~/.codex/skills/design-os-github-page ~/.codex/prompts
cp -R /tmp/design-os-github-page/skills/design-os-github-page/* ~/.codex/skills/design-os-github-page/
cp /tmp/design-os-github-page/prompts/doctor.md ~/.codex/prompts/design-os-github-page-doctor.md
rm -rf /tmp/design-os-github-page
```

### Gemini CLI & Google Antigravity

```bash
git clone https://github.com/jangtrinh/design-os-github-page.git /tmp/design-os-github-page
mkdir -p ~/.gemini/skills/design-os-github-page
cp -R /tmp/design-os-github-page/skills/design-os-github-page/* ~/.gemini/skills/design-os-github-page/
rm -rf /tmp/design-os-github-page
```

### OpenCode, Cursor, Windsurf & Other Agent Harnesses

```bash
git clone https://github.com/jangtrinh/design-os-github-page.git /tmp/design-os-github-page
mkdir -p ~/.agents/skills/design-os-github-page
cp -R /tmp/design-os-github-page/skills/design-os-github-page/* ~/.agents/skills/design-os-github-page/
rm -rf /tmp/design-os-github-page
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
rm -rf ~/.claude/skills/design-os-github-page ~/.codex/skills/design-os-github-page ~/.gemini/skills/design-os-github-page ~/.agents/skills/design-os-github-page
```

</details>

---

## Usage & Prompt Cookbook

Once installed, `skills/design-os-github-page/SKILL.md` activates automatically when your prompt matches its domain triggers. Browse [`docs/cookbook.md`](docs/cookbook.md) for copy-paste prompt recipes.

**Generate & Scaffold**

```text
"Scaffold a 9-tier editorial GitHub Pages site in docs/ with JSON-LD SoftwareSourceCode + FAQPage schemas and llms.txt."
```

**Audit & Verify**

```text
"Upgrade this repository to the DESIGN:OS 12-section AI-Ready README and generate all plugin manifests and /doctor checks."
```

**Export & Automate**

```text
"Run the 10-gate SEO, AEO, and GEO verification harness across our ecosystem and fix any missing canonical or OG tags."
```

---

## Commands & Diagnostics

| Command | Environment | What it does |
| :--- | :--- | :--- |
| `/doctor` | Claude Code / Codex | Read-only diagnostic check of installed skill paths, plugin manifests, and runtime prerequisites |
| `python3 scripts/self_check.py` | Terminal / CI | Deterministic offline verification of manifests, skill contracts, and governance files |
| `python3 scripts/scaffold-repo-delivery.py --repo-root .` | Terminal / CI | Scaffold or backfill `.claude-plugin`, `.codex-plugin`, `skills/`, `/doctor`, governance files, and 12-section `README.md` |

---

## How it works

1. **Intent Routing** — Your AI agent matches your request against `skills/design-os-github-page/SKILL.md` frontmatter triggers.
2. **Progressive Context Loading** — Only the entry-point `SKILL.md` router loads initially; detailed recipes and scripts load on demand.
3. **Deterministic Execution** — Domain scripts and contracts execute locally with reproducible inputs and outputs.
4. **Gate Verification** — `scripts/self_check.py` and domain verifiers (`python3 scripts/verify-repo-delivery.py . && python3 scripts/seo-aeo-geo-harness.py`) validate the artifact before completion.
5. **Zero-Telemetry Delivery** — Verified files are written directly to your workspace with zero external network calls.

```text
User Prompt / CLI Invocation
            │
            ▼
┌───────────────────────────────────────────────┐
│ skills/design-os-github-page/SKILL.md
│ Progressive disclosure router & hard rules    │
└───────────┬───────────────────────────────────┘
            │ loads on demand
            ▼
┌───────────────────────────────────────────────┐
│ python3 scripts/scaffold-repo-delivery.py --repo-root .
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

`design-os-github-page` uses progressive context disclosure so your agent's context window stays fast and focused:

| File | Loaded when |
| :--- | :--- |
| `skills/design-os-github-page/SKILL.md` | Always (~100–150 lines) — routing rules, triggers, and execution workflow |
| `docs/cookbook.md` | When selecting multi-step prompt recipes or domain patterns |
| `commands/doctor.md` / `prompts/doctor.md` | Only when running `/doctor` diagnostics |
| `llms.txt` | When indexed by AI answer engines, RAG pipelines, or repo crawlers |

---

## File structure

```text
design-os-github-page/
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
│   └── design-os-github-page/
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
├── LICENSE                         # PolyForm Shield 1.0.0
└── README.md
```

---

## Quality bar & Limitations

### It's working if...

- `python3 scripts/self_check.py` prints `ok: design-os-github-page self-check passed (design-os-github-page)` and exits `0`.
- `python3 scripts/verify-repo-delivery.py . && python3 scripts/seo-aeo-geo-harness.py` passes with zero contract or test regressions.
- Your AI coding agent loads `skills/design-os-github-page/SKILL.md` automatically when given any prompt from [`docs/cookbook.md`](docs/cookbook.md).
- Network traffic during execution remains zero (guaranteed by [`PRIVACY.md`](PRIVACY.md)).

### When not to use

- Dynamic multi-tenant web applications requiring server-side databases or authenticated user sessions.
- Private internal scratchpads that should never be indexed by search engines or AI answer engines.
- Heavy interactive 3D/video showcases where a dedicated runtime (`design-os-svg-animation` or `design-os-3d-blender`) is needed.

---

## DESIGN:OS Ecosystem

`design-os-github-page` is one of the 13 source-available engines in the **`DESIGN:OS`** ecosystem:

| Engine | Live Docs | Repository | Layer |
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
| **Generative UI** | [jangtrinh.github.io/design-os-generative-ui](https://jangtrinh.github.io/design-os-generative-ui/) | [`jangtrinh/design-os-generative-ui`](https://github.com/jangtrinh/design-os-generative-ui) | `runtime` |

---

## Contributing, Governance & License

- **Contributing**: See [`CONTRIBUTING.md`](CONTRIBUTING.md) for pull request guidelines and verification gates (`python3 scripts/self_check.py`).
- **Code of Conduct**: Governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
- **Security & Privacy**: Zero telemetry — see [`SECURITY.md`](SECURITY.md) and [`PRIVACY.md`](PRIVACY.md).
- **Changelog & LLM Index**: Track releases in [`CHANGELOG.md`](CHANGELOG.md) and machine-readable index in [`llms.txt`](llms.txt).
- **License**: [PolyForm Shield 1.0.0](LICENSE) © [Jang Trinh](https://github.com/jangtrinh). Free to use and modify, including for paid client work; you may not resell it or build a competing product from it.

---

If `design-os-github-page` saves you time, a star on GitHub helps other engineers and AI agents find it.

<p align="left">
  <a href="https://buymeacoffee.com/jangtrinh">
    <img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee">
  </a>
</p>
