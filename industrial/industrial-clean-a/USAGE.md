# Usage

## Human workflow

1. Pick a template from `registry.json`.
2. Read its `SPEC.md`.
3. Pick one layout recipe from `layouts/LAYOUTS.md`.
4. Fill a Screen Contract before drawing the screen.
5. Reuse tokens and component behavior.
6. Apply project branding only after the neutral interface is coherent.
7. Run the review checklist and validator before accepting the UI.

## AI / coding-agent instruction

When asked to implement a UI using **Industrial Clean A**:

1. Treat `industrial/industrial-clean-a/` as the design source of truth.
2. Read `manifest.json`, `SPEC.md`, `tokens/tokens.json`, and `components/COMPONENTS.md`.
3. Identify the user task and create or infer a Screen Contract.
4. Select the smallest appropriate layout recipe.
5. Preserve semantic state colors and interaction behavior.
6. Do not invent a new visual language unless the project explicitly requests a deviation.
7. Never copy company/vendor branding from screenshots or references into this base template.

## Project integration

A consuming project may copy tokens or map them into its own variables:

```css
:root {
  --project-accent: var(--ui-accent);
  --project-surface: var(--ui-bg-surface);
  --project-danger: var(--ui-danger);
}
```

Brand overrides should happen downstream. Status semantics remain stable.

## Acceptance gate

Do not mark a screen complete only because it "looks similar." It passes only when:
- the three-second questions are answerable;
- all required states exist;
- the primary action is obvious;
- exception information is visible;
- no base-template brand contamination exists.
