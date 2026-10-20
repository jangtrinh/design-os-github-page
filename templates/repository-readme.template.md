# {{REPO_TITLE}}

**{{ONE_LINE_HOOK}}**

{{ELEVATOR_PITCH}}

<p align="center">
  <img src="{{HERO_IMAGE_PATH}}" alt="{{REPO_TITLE}} — 2:1 Axonometric Technical Architecture" width="840">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-PolyForm_Shield_1.0.0-202020?style=flat-square&labelColor=202020&color=444444" alt="PolyForm Shield 1.0.0 License"></a>
  <img src="https://img.shields.io/badge/Claude_Code_%C2%B7_Codex_%C2%B7_Gemini_%C2%B7_Antigravity-skill-202020?style=flat-square&labelColor=202020&color=444444" alt="Compatible agents">
  <a href="commands/doctor.md"><img src="https://img.shields.io/badge/diagnostics-%2Fdoctor-202020?style=flat-square&labelColor=202020&color=444444" alt="Doctor command"></a>
  <a href="https://{{GITHUB_OWNER}}.github.io/{{REPO_SLUG}}/"><img src="https://img.shields.io/badge/live_docs-GitHub_Pages-202020?style=flat-square&labelColor=202020&color=444444" alt="Live GitHub Pages"></a>
  <a href="https://buymeacoffee.com/{{GITHUB_OWNER}}"><img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> · <a href="#what-it-makes">What it makes</a> · <a href="#installation">Install</a> · <a href="#how-it-works">How it works</a> · <a href="#commands--diagnostics">Commands</a> · <a href="#quality-bar--limitations">Limits</a>
</p>

---

## Why this exists

{{WHY_THIS_EXISTS_INTRO}}

| Dimension | Generic AI / Manual Workflow | {{REPO_TITLE}} (`DESIGN:OS`) |
| :--- | :--- | :--- |
| **Determinism** | {{BEFORE_ROW_1}} | {{AFTER_ROW_1}} |
| **Context Efficiency** | {{BEFORE_ROW_2}} | {{AFTER_ROW_2}} |
| **Verification Gate** | {{BEFORE_ROW_3}} | {{AFTER_ROW_3}} |
| **Agent Portability** | {{BEFORE_ROW_4}} | {{AFTER_ROW_4}} |
| **Privacy & Telemetry** | {{BEFORE_ROW_5}} | **Zero telemetry** — 100% local execution (`PRIVACY.md` audited) |

---

## Quickstart

### 1. Install the plugin or CLI

**In Claude Code:**

```text
/plugin marketplace add {{GITHUB_OWNER}}/{{REPO_SLUG}}
/plugin install {{REPO_SLUG}}@{{REPO_SLUG}}
```

**Or from your terminal (Codex, Gemini CLI, Antigravity, OpenCode, or standalone CLI):**

```bash
git clone https://github.com/{{GITHUB_OWNER}}/{{REPO_SLUG}}.git
cd {{REPO_SLUG}}
{{QUICKSTART_COMMAND}}
```

### 2. Ask in plain English

Open your project in your AI coding agent and describe the outcome you need:

> "{{EXAMPLE_PROMPT_1}}"

> "{{EXAMPLE_PROMPT_2}}"

> "{{EXAMPLE_PROMPT_3}}"

### 3. Verify your setup

```bash
python3 scripts/self_check.py
```

---

## What it makes

{{WHAT_IT_MAKES_INTRO}}

<p align="center">
  <img src="{{HERO_IMAGE_PATH}}" alt="{{REPO_TITLE}} Output Specimen" width="840"><br>
  <sub>Prompt: <code>"{{EXAMPLE_PROMPT_1}}"</code></sub>
</p>

| Deliverable / Mode | Best for | Output Format | Verification Gate |
| :--- | :--- | :--- | :--- |
| **{{DELIVERABLE_1_NAME}}** | {{DELIVERABLE_1_USE}} | `{{DELIVERABLE_1_FORMAT}}` | {{DELIVERABLE_1_GATE}} |
| **{{DELIVERABLE_2_NAME}}** | {{DELIVERABLE_2_USE}} | `{{DELIVERABLE_2_FORMAT}}` | {{DELIVERABLE_2_GATE}} |
| **{{DELIVERABLE_3_NAME}}** | {{DELIVERABLE_3_USE}} | `{{DELIVERABLE_3_FORMAT}}` | {{DELIVERABLE_3_GATE}} |

---

## Installation

Choose the setup that matches your AI coding agent. Every option installs the same canonical skill (`skills/{{SKILL_SLUG}}/SKILL.md`) and diagnostics (`commands/doctor.md`).

### Claude Code

Run these two commands inside Claude Code:

```text
/plugin marketplace add {{GITHUB_OWNER}}/{{REPO_SLUG}}
/plugin install {{REPO_SLUG}}@{{REPO_SLUG}}
```

### OpenAI Codex

Install to the personal skills directory:

```bash
git clone https://github.com/{{GITHUB_OWNER}}/{{REPO_SLUG}}.git /tmp/{{REPO_SLUG}}
mkdir -p ~/.codex/skills/{{SKILL_SLUG}} ~/.codex/prompts
cp -R /tmp/{{REPO_SLUG}}/skills/{{SKILL_SLUG}}/* ~/.codex/skills/{{SKILL_SLUG}}/
cp /tmp/{{REPO_SLUG}}/prompts/doctor.md ~/.codex/prompts/{{SKILL_SLUG}}-doctor.md
rm -rf /tmp/{{REPO_SLUG}}
```

### Gemini CLI & Google Antigravity

```bash
git clone https://github.com/{{GITHUB_OWNER}}/{{REPO_SLUG}}.git /tmp/{{REPO_SLUG}}
mkdir -p ~/.gemini/skills/{{SKILL_SLUG}}
cp -R /tmp/{{REPO_SLUG}}/skills/{{SKILL_SLUG}}/* ~/.gemini/skills/{{SKILL_SLUG}}/
rm -rf /tmp/{{REPO_SLUG}}
```

### OpenCode, Cursor, Windsurf & Other Agent Harnesses

```bash
git clone https://github.com/{{GITHUB_OWNER}}/{{REPO_SLUG}}.git /tmp/{{REPO_SLUG}}
mkdir -p ~/.agents/skills/{{SKILL_SLUG}}
cp -R /tmp/{{REPO_SLUG}}/skills/{{SKILL_SLUG}}/* ~/.agents/skills/{{SKILL_SLUG}}/
rm -rf /tmp/{{REPO_SLUG}}
```

<details>
<summary>Verify or uninstall</summary>

**Verify installation:**

```bash
python3 scripts/self_check.py
```

Or run `/doctor` inside Claude Code / Codex to inspect installed skill paths, runtime dependencies, and gate health.

**Uninstall:**

```bash
rm -rf ~/.claude/skills/{{SKILL_SLUG}} ~/.codex/skills/{{SKILL_SLUG}} ~/.gemini/skills/{{SKILL_SLUG}} ~/.agents/skills/{{SKILL_SLUG}}
```

</details>

---

## Usage & Prompt Cookbook

Once installed, the skill triggers automatically when you ask for tasks in its domain. See [`docs/cookbook.md`](docs/cookbook.md) for copy-paste prompt recipes.

**Generate & Scaffold**

```text
"{{EXAMPLE_PROMPT_1}}"
```

**Audit & Verify**

```text
"{{EXAMPLE_PROMPT_2}}"
```

**Export & Automate**

```text
"{{EXAMPLE_PROMPT_3}}"
```

---

## Commands & Diagnostics

| Command | Environment | What it does |
| :--- | :--- | :--- |
| `/doctor` | Claude Code / Codex | Inspects plugin manifests, skill installation, runtime prerequisites, and read-only safety |
| `python3 scripts/self_check.py` | Terminal / CI | Deterministic offline self-check of manifests, skill contracts, and governance files |
| `{{PRIMARY_CLI_COMMAND}}` | Terminal / CI | {{PRIMARY_CLI_DESCRIPTION}} |

---

## How it works

1. **Intent Routing** — Your AI agent matches your request against `skills/{{SKILL_SLUG}}/SKILL.md` frontmatter triggers.
2. **Progressive Context Loading** — Only the entry-point `SKILL.md` loads first; specialized references load on demand.
3. **Deterministic Execution** — The engine executes through reproducible scripts and explicit schema contracts rather than freehand guesswork.
4. **Epistemic & Visual Verification** — Outputs are checked against `scripts/self_check.py` and domain quality gates before completion.
5. **Zero-Telemetry Artifact Delivery** — Clean files are written directly to your workspace with zero external tracking.

```text
User Prompt / CLI Invocation
            │
            ▼
┌───────────────────────────────────────────────┐
│ skills/{{SKILL_SLUG}}/SKILL.md                │
│ Progressive disclosure router & hard rules    │
└───────────┬───────────────────────────────────┘
            │ loads on demand
            ▼
┌───────────────────────────────────────────────┐
│ Core Engine / Scripts / Templates             │
│ Deterministic build & schema enforcement      │
└───────────┬───────────────────────────────────┘
            │ verifies
            ▼
┌───────────────────────────────────────────────┐
│ scripts/self_check.py + /doctor               │
│ Zero-telemetry local verification gate        │
└───────────────────────────────────────────────┘
```

### What loads when

The skill uses progressive disclosure so your agent's context window stays lean:

| File | Loaded when |
| :--- | :--- |
| `skills/{{SKILL_SLUG}}/SKILL.md` | Always (~150 lines) — routing rules, triggers, and execution workflow |
| `commands/doctor.md` / `prompts/doctor.md` | Only when running `/doctor` diagnostics |
| `docs/cookbook.md` | When selecting multi-step prompt recipes or domain patterns |
| `llms.txt` | When indexed by AI answer engines, RAG pipelines, or repo crawlers |

---

## File structure

```text
{{REPO_SLUG}}/
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
│   └── {{SKILL_SLUG}}/
│       └── SKILL.md                # Canonical agent skill entrypoint
├── commands/
│   └── doctor.md                   # /doctor diagnostic slash command
├── prompts/
│   └── doctor.md                   # Codex diagnostic prompt mirror
├── scripts/
│   └── self_check.py               # Deterministic repository & skill self-check
├── docs/
│   ├── index.html                  # Live GitHub Pages marketing & docs site
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

- `python3 scripts/self_check.py` exits `0` with all plugin manifests, skill files, and governance checks passing.
- Your AI coding agent loads `skills/{{SKILL_SLUG}}/SKILL.md` automatically when given any prompt from [`docs/cookbook.md`](docs/cookbook.md).
- Every generated artifact passes deterministic validation without manual post-editing or cloud dependencies.
- Network traffic during execution remains zero (verified by [`PRIVACY.md`](PRIVACY.md)).

### When not to use

- {{WHEN_NOT_TO_USE_1}}
- {{WHEN_NOT_TO_USE_2}}
- {{WHEN_NOT_TO_USE_3}}

---

## DESIGN:OS Ecosystem

`{{REPO_SLUG}}` is one of the 13 source-available engines in the **`DESIGN:OS`** ecosystem:

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

- **Contributing**: See [`CONTRIBUTING.md`](CONTRIBUTING.md) for PR requirements and verification gates (`python3 scripts/self_check.py`).
- **Code of Conduct**: Governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
- **Security & Privacy**: Zero telemetry — see [`SECURITY.md`](SECURITY.md) and [`PRIVACY.md`](PRIVACY.md).
- **Changelog & LLM Index**: Track releases in [`CHANGELOG.md`](CHANGELOG.md) and machine-readable index in [`llms.txt`](llms.txt).
- **License**: [PolyForm Shield 1.0.0](LICENSE) © [Jang Trinh](https://github.com/jangtrinh). Free to use and modify, including for paid client work; you may not resell it or build a competing product from it.

---

If `{{REPO_SLUG}}` saves you time, a star on GitHub helps other engineers and AI agents find it.

<p align="left">
  <a href="https://buymeacoffee.com/{{GITHUB_OWNER}}">
    <img src="https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee">
  </a>
</p>
