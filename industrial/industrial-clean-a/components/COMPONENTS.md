# Component Specification

## Core controls

| Component | Required states | Notes |
|---|---|---|
| Button | default, hover, focus, pressed, disabled, loading | Primary action per region should be unique |
| Icon Button | same as Button | Tooltip required when icon meaning is not universal |
| Input | default, focus, disabled, readonly, error | Show unit and validation near field |
| Numeric Input | same as Input | Support min/max/step and unit |
| Select | default, open, focus, disabled, error | Large option sets require search |
| Checkbox / Radio | unchecked, checked, indeterminate, disabled | Do not rely on color only |
| Switch | on, off, disabled | Use for immediate binary settings, not form submission |
| Tabs | default, active, hover, disabled | Avoid more than 6 primary tabs |
| Tooltip | open/closed | Supplemental only; never hide required information |

## Data components

- **KPI Card:** large value + concise label + optional unit + state delta; 3–6 per first screen.
- **Data Table:** sortable/filterable columns, explicit empty/loading/error states, stable status column.
- **Tree / Tree Table:** hierarchical equipment, workflow, recipe, or configuration objects.
- **Trend Chart:** time series with clear unit and interval; abnormal threshold can be overlaid.
- **Status Indicator:** icon/shape + text + semantic color.
- **Progress:** determinate where possible; indeterminate only when progress cannot be measured.

## Industrial components

### Machine / Station Card
Must show: station name, operational state, connectivity summary, current recipe/task, primary KPI, alarm count.

### Alarm Card / Alarm Row
Must show: severity, code, timestamp, source, concise cause, acknowledgement/recovery state, next action.

### Recipe Card
Must show: name, version, status, last modified metadata, compatibility/target scope, activate action.

### Device Connection Row
Must show: device role, endpoint, connection state, last heartbeat, test/reconnect action.

### PLC / IO Mapping Row
Must show: logical name, direction, address, data type, live value/state, quality, test action where safe.

### Image Inspection View
Must support: zoom, pan, fit, coordinates, ROI, overlays, result annotations, display toggles, selected-object emphasis.

### Parameter Group
Must show: group title, value, unit, valid range, changed state, validation, restore/default behavior.

## Containers

- Panel: flat surface, 1 px border, compact title bar.
- Modal: only for blocking decisions or compact edits.
- Drawer: contextual detail that should not destroy main workspace context.
- Bottom Log: collapsible; normal operation should not require it to stay expanded.

## Required system states

Every complex component should define where applicable:
`Loading`, `Empty`, `Disconnected`, `Error`, `Timeout`, `Partial Failure`, `Offline`, `No Results`, `Permission Denied`.
