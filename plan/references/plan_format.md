# Plan Format

A plan is a gap-closing artifact. It should make the path from current problem to target state obvious.

## Minimal shape

```text
PLAN_ID: <ID>
Source: <source artifact or prompt>
Purpose: <target outcome>

## Gap Map

| Gap ID | Current Problem | Target State |
| --- | --- | --- |
| GAP-1 | <problem> | <target> |

## Work Plan

### <PLAN_ID>-1 — <item title>

Closes: GAP-1
Status: planned
Depends on: none
Outcome: <artifact or decision this item should produce>

Deliverables:
- <deliverable>

Done when:
- <condition>
```

## Status values

Use simple planning states:

- `planned`
- `blocked`
- `deferred`
- `done`

`done` means the plan artifact says the item is no longer planned work. It is not verification evidence by itself.

## Rules

- Prefer gap closure over checklist phrasing.
- Preserve stable IDs.
- Gaps can be closed by multiple items.
- Items can close multiple gaps when the coupling is real.
- Keep task packet detail out of the plan unless embedding it reduces handoff ambiguity.
