# Layout Recipes — Industrial Clean A

The template uses task-driven layout recipes rather than one universal screen.

## L1 — Engineering Workbench

Use for inspection configuration, calibration, parameter tuning, simulation, and debugging.

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Context / Product / Module / Object / State                         │
├───────────────┬───────────────────────────────┬──────────────────────┤
│ Navigation /  │                               │ Properties /         │
│ Task Tree     │       Main Workspace          │ Parameters           │
│ 220–280 px    │                               │ 300–360 px           │
│               │                               │                      │
├───────────────┴───────────────────────────────┴──────────────────────┤
│ Status / Log / Connection Summary                                  │
└──────────────────────────────────────────────────────────────────────┘
```

Primary task examples: configure a camera, tune an inspection tool, calibrate a robot.

## L2 — Operational HMI

Use for production running, station operation, alarms, and shift monitoring.

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Station / Recipe / State / Connectivity                             │
├──────────────────────────────────────────────────────────────────────┤
│ KPI       KPI       KPI       KPI       Alarm                       │
├────────────────────────────────┬─────────────────────────────────────┤
│ Current Result / Process       │ Context / Recent Exception         │
│                                │                                     │
├────────────────────────────────┴─────────────────────────────────────┤
│ Primary operation actions                                             │
└──────────────────────────────────────────────────────────────────────┘
```

Rules:
- Current state and active alarm are always visible.
- Start/Stop/Reset/Clear are visually separated according to risk.
- Do not force the operator to read engineering logs during normal running.

## L3 — Data / Quality Analysis

Use for yield, history, traceability, audit, reports.

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Page / Scope / Time Range / Filters / Export                        │
├──────────────────────────────────────────────────────────────────────┤
│ Summary KPI                 Trend / Distribution                    │
├──────────────────────────────────────────────────────────────────────┤
│ Primary Table / Traceability Results                                │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

Rules:
- Filters describe the current data scope.
- Summary values must agree with table filters.
- Export inherits the same scope by default.

## L4 — Catalog / Navigator

Use for tool selection, recipe selection, configuration entry points.

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Page context + search                                               │
├───────────────┬──────────────────────────────────────────────────────┤
│ Categories    │ Cards / compact list of available objects           │
│               │                                                      │
└───────────────┴──────────────────────────────────────────────────────┘
```

Rules:
- Group by user intent, not internal code module names.
- Each item should state purpose before implementation detail.

## L5 — Mobile Companion

Use for status checking, alarms, acknowledgement, approvals, concise inspection results.

```text
┌───────────────────────┐
│ Context + State       │
├───────────────────────┤
│ Critical KPI / Alarm  │
├───────────────────────┤
│ Primary task content  │
├───────────────────────┤
│ Primary action        │
└───────────────────────┘
```

Never shrink L1 desktop workbench into a phone screen. Recompose the task.
