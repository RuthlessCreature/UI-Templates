# Adding a New UI Template

## Workflow

1. Choose a category and stable template ID.
2. Create the required structure defined in `TEMPLATE_STANDARD.md`.
3. Keep the base template brand-neutral.
4. Add a neutral SVG preview.
5. Define tokens before writing example screens.
6. Define components and layout recipes.
7. Define cross-platform behavior.
8. Add one or more Screen Contract examples.
9. Register the template in `registry.json`.
10. Run repository validation.

## Rule of thumb

Do not create a new template only because one project changed its logo, accent color, or copy. That is a **brand layer**, not a new design system.

Create a separate template only when its underlying visual/interaction grammar materially differs, such as:

- industrial dense workbench vs consumer mobile card UI;
- executive presentation system vs operational HMI;
- dark monitoring control room vs light engineering editor.

## Naming examples

Good:
- `industrial-clean-a`
- `industrial-dark-monitoring-a`
- `enterprise-minimal-a`
- `consumer-mobile-soft-a`
- `presentation-technical-a`

Bad:
- `client-x-ui`
- `company-y-blue`
- `final-v7-new`
- `copy-of-some-vendor`
