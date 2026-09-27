# UI Templates

Brand-neutral UI design systems for Web, Desktop, Mobile and PPT.

**Live gallery:** https://ui.fhkq.best

The gallery reads `registry.json`, previews, and demo HTML directly from the GitHub `main` branch. Template updates therefore appear without manually rebuilding gallery content.

## Template families

| Category | Count | Description |
|---|---:|---|
| 工业类 | 15 | 工业软件、HMI、机器视觉、监控、工程工作台 |
| 互联网扁平 · 美式 | 5 | SaaS、AI 工具、运营、FinTech、创作工具 |
| 国企风格 | 5 | 门户、OA、项目、审批、经营分析、科技创新 |
| 35–45 女性 | 5 | 生活服务、会员、预约、旅行、健康与消费体验 |

**Total: 30 templates.**

## Repository contract

1. Pick a template from `registry.json`.
2. Read `manifest.json`, `SPEC.md`, `SCREEN_CONTRACT.md`, tokens, components, layouts and platform rules.
3. Apply project branding only downstream.
4. Every active template remains brand-neutral and passes CI.

## Gallery

The gallery source lives under `docs/` and is deployed by `.github/workflows/pages.yml`.
It dynamically fetches the latest registry and template files from GitHub, so adding a new registered template automatically adds it to the gallery.
