# UI Template Standard

This document defines the repository-level contract for every reusable UI template.

## 1. Naming

Every template has:

- a stable machine ID in lowercase kebab-case, e.g. `industrial-clean-a`;
- a human display name, which may be Chinese, English, or bilingual;
- a semantic version;
- one concise positioning sentence.

The machine ID is permanent. Renaming the display name must not change the ID.

## 2. Required directory structure

```text
<category>/<template-id>/
├── README.md
├── manifest.json
├── SPEC.md
├── SCREEN_CONTRACT.md
├── CHECKLIST.md
├── CHANGELOG.md
├── BRAND_LAYER.md
├── USAGE.md
├── preview/
│   └── overview.svg
├── tokens/
│   ├── tokens.json
│   └── tokens.css
├── components/
│   └── COMPONENTS.md
├── layouts/
│   └── LAYOUTS.md
├── platforms/
│   ├── DESKTOP.md
│   ├── WEB.md
│   ├── MOBILE.md
│   └── PPT.md
├── prompts/
│   ├── UI_GENERATION.md
│   └── NEGATIVE_PROMPT.md
├── schema/
│   └── screen-contract.schema.json
├── scenes/
│   ├── SCENES.md
│   └── scenes.json
└── examples/
    ├── demo.html
    └── screen-contract.example.json
```

A template may omit a platform file only when `manifest.json` explicitly marks that platform unsupported.

## 3. What SPEC.md must define

At minimum:

- background;
- goals and non-goals;
- target users/tasks;
- information hierarchy;
- first-screen comprehension rules;
- color semantics;
- typography;
- spacing;
- borders/radius/elevation;
- status model;
- data-display rules;
- form/editing rules;
- feedback states;
- dangerous-action behavior;
- accessibility/robustness;
- acceptance criteria.

## 4. Design tokens

`tokens/tokens.json` is the canonical machine-readable source.

Tokens should cover:

- background/surface/border/text;
- accent and semantic status colors;
- spacing scale;
- typography scale and weights;
- corner radius;
- control and layout dimensions;
- interaction target sizes.

Do not encode a company brand as a base semantic token.

## 5. Brand neutrality

Reusable base templates must not contain:

- company/customer names;
- logos or trademarks;
- real domains, email addresses, phone numbers, accounts;
- vendor-specific style-cloning instructions;
- confidential project screenshots or data.

Project branding is applied downstream.

## 6. Preview

Every active template must contain `preview/overview.svg`.

The preview must:

- be brand-neutral;
- demonstrate the visual grammar, not a real customer screen;
- show enough structure to distinguish the template from other templates;
- avoid hidden dependencies such as external fonts or remote images.

## 7. Screen Contract

Every template must define a Screen Contract that forces the implementer to identify:

- primary user;
- primary task;
- location context;
- current state;
- L1–L4 information;
- exceptions;
- primary/secondary/dangerous actions;
- loading/empty/error/offline states;
- acceptance criteria.

A screen without a clear task contract is not ready for implementation.

## 8. Cross-platform rule

“Same design system” does not mean “same layout.”

Desktop, Web, Mobile, and PPT inherit:

- visual grammar;
- semantic colors;
- typography hierarchy;
- spacing rhythm;
- component family resemblance.

They may use different composition rules appropriate to the platform.

## 9. Versioning

Use semantic versions:

- PATCH: wording, examples, non-breaking token clarification;
- MINOR: new components/scenes/layouts that do not invalidate existing use;
- MAJOR: breaking changes to tokens, semantics, interaction rules, or template identity.

Every version change updates `CHANGELOG.md` and `manifest.json`.

## 10. Acceptance gate

Before a template becomes `active` in `registry.json`:

- required structure exists;
- preview exists;
- manifest declares `brand_neutral=true`;
- validator passes;
- no forbidden identity contamination exists;
- at least one working example exists;
- supported-platform rules are documented.
