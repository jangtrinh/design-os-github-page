# design-os-github-page

> **Author-grade GitHub Presence, Pages & README Documentation Engine for builders and AI coding agents.**  
> Evolved from the production repositories of the `design:os` ecosystem into a universal, zero-dependency toolchain.

[![CI](https://img.shields.io/github/actions/workflow/status/jangtrinh/design-os-github-page/ci.yml?branch=main&style=for-the-badge&label=CI)](https://github.com/jangtrinh/design-os-github-page/actions)
[![License: MIT](https://img.shields.io/github/license/jangtrinh/design-os-github-page?style=for-the-badge)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/pages-live-202020?style=for-the-badge&logo=github)](https://jangtrinh.github.io/design-os-github-page/)
[![Architecture: Local-First](https://img.shields.io/badge/architecture-local--first-202020?style=for-the-badge)](#)
[![Telemetry: Zero](https://img.shields.io/badge/telemetry-zero-202020?style=for-the-badge)](#)

---

## What It Is

`design-os-github-page` transforms **any public GitHub repository or developer profile** into an author-grade, fast-indexing, high-converting presence on GitHub — unifying Pages, Profile README, and Repository README.

- **Zero External Dependencies**: Powered by standalone Python 3 standard library scripts. No `npm install`, no `cargo`, no pip packages.
- **Unified GitHub Presence Architecture**: Complete toolchain covering GitHub Pages marketing sites, Profile README, and Repository README.
- **Formal README Knowledge Base (`knowledge/readme/`)**: 5 UKMC.v1 audited modules detailing Profile README architecture, 9-tier repo structure, 2:1 isometric art direction, CI/CD automation, and anti-patterns.
- **Verified Production Templates (`templates/`)**: Zero-chroma B&W Profile README template and 9-tier Repo README template ready to deploy.
- **The 9-Tier Information Architecture**: Replaces "AI slop" and walls of text with structured, credible technical storytelling.
- **Mandatory Gallery & 3D Three.js Preview**: Dedicated visual gallery for all repos; embedded zero-dependency Three.js 3D viewer for 3D/CAD/hardware projects.
- **README & Pages Synchronization**: Standing parity rule keeping README and Pages in 100% lockstep across every feature and release.
- **Full Machine-Readability Pack**: Built-in Google SEO, XML Sitemap, `robots.txt`, `llms.txt` (GEO), and Schema.org `FAQPage` (AEO).
- **Built-in Monetization**: Native Buy Me a Coffee floating widget.
- **Ecosystem Cross-Sale**: Dedicated cross-promotional section connecting companion repositories.

---

## Quickstart

Scaffold an author-grade site in `./docs` in seconds:

```bash
# Clone the generator
git clone https://github.com/jangtrinh/design-os-github-page.git
cd design-os-github-page

# Scaffold for any repository
python3 scripts/scaffold-repo-pages.py \
  --owner <github-owner> \
  --repo <repo-name> \
  --name "<Display Name>" \
  --category "<Category / Ecosystem>" \
  --tagline "<Actionable Proposition Sentence>" \
  --desc "<160-char Meta Description for SEO/AEO>" \
  --accent "#2563eb" \
  --bmc "<buymeacoffee-id>" \
  --out-dir ./docs
```

### Generated Files

```text
docs/
├── index.html            # 9-tier author-grade landing page with Schema.org JSON-LD
├── _config.yml           # Jekyll configuration for GitHub Pages
├── _layouts/
│   └── default.html      # Canonical layout for Markdown deep-dive pages
├── assets/
│   └── site.css          # EaseUI design system token ladder (Inter, Mono, 0-chroma)
├── robots.txt            # RFC 9309 crawler permissions & sitemap declaration
├── sitemap.xml           # sitemaps.org XML 0.9 with dynamic lastmod
└── llms.txt              # llmstxt.org specification for AI search (ChatGPT, Perplexity)
```

---

## GitHub README Architecture & Templates

The engine includes the canonical **README Knowledge Base (`knowledge/readme/`)** and verified production templates:

| Module | Location | Purpose |
| :--- | :--- | :--- |
| **Profile README Spec** | [`knowledge/readme/profile-readme-architecture.md`](knowledge/readme/profile-readme-architecture.md) | Author-grade structure, hero ratio, B&W metrics, and zero-emoji discipline |
| **Repository README Spec** | [`knowledge/readme/repository-readme-architecture.md`](knowledge/readme/repository-readme-architecture.md) | 9-tier technical information architecture for libraries and CLIs |
| **Visual & Art Direction** | [`knowledge/readme/readme-visual-craft.md`](knowledge/readme/readme-visual-craft.md) | 2:1 isometric technical illustration standards, typography, and dark/light assets |
| **Dynamic Automation** | [`knowledge/readme/readme-dynamic-automation.md`](knowledge/readme/readme-dynamic-automation.md) | GitHub Actions snake animation, SVG telemetry, and cache-busting workflows |
| **Anti-Patterns Catalog** | [`knowledge/readme/readme-anti-patterns.md`](knowledge/readme/readme-anti-patterns.md) | The 10 prohibited anti-patterns (zebra striping, emoji inflation, fake stats) |
| **Profile Template** | [`templates/profile-readme.template.md`](templates/profile-readme.template.md) | Production-ready zero-chroma B&W Profile README template |
| **Repository Template** | [`templates/repository-readme.template.md`](templates/repository-readme.template.md) | 9-tier author-grade repository README template |

---

## The 9-Tier Layout Hierarchy

| Tier | Section | Architectural Purpose |
| :--- | :--- | :--- |
| **1** | **Hero & 3-Second Rule** | Eyebrow category · Proposition H1 (`clamp(30px,4.6vw,48px)`) · Meta description lede · Badges row (height 28px) · Primary solid button + secondary text link · Uncropped capture stage |
| **2** | **Facts Register** | `<dl class="facts">`: Repository, Requires, Interface, Transport/Protocol, Telemetry policy, License |
| **3** | **Honest Comparison** | 4-row advantage register · Honest aside box (`div.aside`) noting where existing alternatives win |
| **4** | **Install Once** | 3–4 line non-interactive terminal block |
| **5** | **Safe Use & Loop** | 3 numbered safe steps (`--version`, `status --json`, `run --dry-run`) · 4-row practical loop register |
| **6** | **Gallery & Deep Evidence** | **Mandatory Gallery Showcase**: Visual card grid (`ul.projects`), demo tiles, or dynamic canvas. **3D Project Rule**: Embedded zero-dependency Three.js 3D viewer (`OrbitControls`, explosion/slice slider, BOM catalog) is mandatory for 3D/CAD/hardware repos. |
| **7** | **AEO FAQ Engine** | 5 semantic `<details><summary>` Q&As matching Schema.org `FAQPage` word-for-word |
| **8** | **Ecosystem Section** | `<section id="ecosystem">`: Cross-sale links to author's companion repositories/tools |
| **9** | **Read Next & Footer** | 3–4 deep-dive documentation links · Minimal 3-tab footer (GitHub, License, Back to top) |

---

## Why This Tool, Compared with Alternatives

| Feature | `design-os-github-page` | Docusaurus / Nextra / Astro | Default GitHub Pages Themes |
| :--- | :--- | :--- | :--- |
| **Dependencies** | **0** (Python stdlib) | 1,000+ npm packages | Bundled Jekyll gems |
| **Build Time** | **< 100 ms** (instant) | 30–90 seconds | 10–30 seconds |
| **Layout Craft** | **9-Tier Author-Grade** | Generic doc shell | Dated 2014 blogs |
| **Machine-Readability** | **SEO + GEO (`llms.txt`) + AEO (`FAQPage`)** | Manual plugin setup | None |
| **Monetization & Ecosystem** | **Native BMC widget + cross-sale section** | Manual components | None |

---

## Live Case Studies (design:os Reference Suite)

The 6 production implementations of this architecture across different repository categories (each individually accessible and directly clickable):

| Preview | Repository | Category | Live Showcase & Documentation |
| :--- | :--- | :--- | :--- |
| [![CLI](images/eco_showcase_01_design_os_cli.png)](https://jangtrinh.github.io/design-os/) | **[design-os](https://github.com/jangtrinh/design-os)** | CLI Tool | [Live Pages ↗](https://jangtrinh.github.io/design-os/) · Terminal verb registers & automated workflows |
| [![Figma](images/eco_showcase_02_figma_plugin.png)](https://jangtrinh.github.io/design-os-figma-plugin/) | **[design-os-figma-plugin](https://github.com/jangtrinh/design-os-figma-plugin)** | Desktop Plugin | [Live Pages ↗](https://jangtrinh.github.io/design-os-figma-plugin/) · Live canvas bridge & bidirectional sync |
| [![SVG](images/eco_showcase_03_svg_animation.png)](https://jangtrinh.github.io/design-os-svg-animation/) | **[design-os-svg-animation](https://github.com/jangtrinh/design-os-svg-animation)** | Vector Engine | [Live Pages ↗](https://jangtrinh.github.io/design-os-svg-animation/) · Deterministic 1080p 60fps video generation |
| [![3D](images/eco_showcase_04_3d_blender.png)](https://jangtrinh.github.io/design-os-3d-blender/) | **[design-os-3d-blender](https://github.com/jangtrinh/design-os-3d-blender)** | 3D / CAD | [Live Pages ↗](https://jangtrinh.github.io/design-os-3d-blender/) · Three.js CAD viewer & BOM catalog |
| [![Drone](images/eco_showcase_05_drone_showcase.png)](https://jangtrinh.github.io/design-os-drone-showcase/) | **[design-os-drone-showcase](https://github.com/jangtrinh/design-os-drone-showcase)** | Hardware | [Live Pages ↗](https://jangtrinh.github.io/design-os-drone-showcase/) · 249g drone kinematics & teardown |
| [![Pedagogy](images/eco_showcase_06_pedagogy.png)](https://jangtrinh.github.io/design-os-pedagogy/) | **[design-os-pedagogy](https://github.com/jangtrinh/design-os-pedagogy)** | Curriculum | [Live Pages ↗](https://jangtrinh.github.io/design-os-pedagogy/) · Agent Teacher curriculum tree & logs |

---

## License

Released under the permissive [MIT License](LICENSE). Free for commercial and personal open-source projects.
