# AGENTS.md

## Repository contract

This repository is the canonical source for reusable UI templates.

When a task requests UI work using a named template:
1. Read `registry.json`.
2. Open the matching template `manifest.json` and `SPEC.md`.
3. Reuse its tokens, hierarchy, component rules, states, and platform rules before inventing new patterns.
4. Keep the base template brand-neutral.
5. Do not add company names, logos, trademarks, real domains, customer names, real email addresses, or other project-specific identity into a base template.
6. Put project-specific branding only in the consuming project, not here.

## Quality gate

A screen is not complete unless a first-time user can answer within roughly three seconds:
- Where am I?
- What is the current state?
- What matters most?
- Is anything abnormal?
- What can I do next?

For industrial interfaces, prefer operational clarity over decorative novelty.
