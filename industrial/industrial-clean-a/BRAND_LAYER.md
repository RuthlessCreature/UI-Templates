# Brand Layer Boundary

The base template is intentionally brand-neutral.

## Base template owns

- layout
- spacing
- information hierarchy
- component behavior
- system/status semantics
- typography scale
- interaction states
- data-display rules
- cross-platform adaptation
- accessibility and operational safety patterns

## Consuming project may override

- company/product name
- logo
- brand accent color, if semantic contrast remains valid
- approved brand font
- marketing illustration
- customer-specific terminology

## Consuming project must not override casually

- success / warning / danger meaning
- alarm prominence
- dangerous-action behavior
- minimum interaction target size
- focus/error/disabled states
- information hierarchy rules

Brand application is a downstream transformation. A project should be able to remove its branding and still retain a coherent, usable Industrial Clean A interface.
