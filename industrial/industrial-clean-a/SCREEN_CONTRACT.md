# Screen Contract

Every production screen derived from this template should define its information contract before visual implementation.

## Required fields

| Field | Meaning |
|---|---|
| Screen ID | Stable machine-readable identifier |
| Platform | desktop / web / mobile / ppt |
| Primary user | Who makes a decision or performs an action here |
| User task | The single primary job this screen exists to support |
| Location context | What tells the user where they are |
| Current state | What operational/system state is visible |
| L1 information | 1–6 critical items that dominate first-glance attention |
| L2 information | Main working content |
| L3 information | Supporting evidence, history, trends, parameters |
| L4 metadata | IDs, version, operator, time, audit fields |
| Exceptions | What can go wrong and how it is surfaced |
| Primary action | The most likely next action |
| Secondary actions | Supporting actions |
| Dangerous actions | Actions requiring stronger separation/confirmation |
| Required states | Loading, Empty, Error, Offline, etc. |
| Exit / back behavior | How the user safely leaves the screen |
| Acceptance criteria | How the screen is objectively verified |

## Rules

- If the primary user or primary task cannot be written in one sentence, the screen scope is probably too broad.
- L1 is capped at six visible focal items.
- A screen may have many actions, but only one dominant primary action per operation region.
- Alarm/NG/error information must not be visually buried under trends or configuration details.
- Metadata must remain available without competing with the task.
- Every asynchronous operation must expose in-progress, success, and failure outcomes.
- Brand identity is not part of the base screen contract.
