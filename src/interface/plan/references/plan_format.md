# Plan Format

A plan is a gap-closing artifact. It should make the path from current problem to target state obvious and readable end to end for review.

## Minimal shape

```text
PLAN_ID: <ID>
Source: <source artifact or prompt>
Purpose: <target outcome>

## Source Summary

Summarize only the source details needed to understand and review this plan without re-reading the full source artifact. Sources may be specs, prompts, comments, investigations, reviews, task sets, or other context.

- <source ref or topic>: <short embedded summary>

## Gap Map

| Gap ID | Source Summary | Current Problem | Target State |
| --- | --- | --- | --- |
| GAP-1 | <source ref/topic plus short summary> | <problem> | <target> |

## Work Plan

### <PLAN_ID>-1 — <item title>

Closes: GAP-1
Source refs: <source refs/topics or none>
Status: todo
Depends on: none
Outcome: <artifact, decision, or state this item should produce>

Deliverables:
- <deliverable>

Done when:
- <condition>
```

## Status values

Use the standard lifecycle states:

- `todo`
- `doing`
- `verifying`
- `reviewing`
- `done`

`done` means the plan artifact says the item is no longer planned work. It is not verification evidence by itself.

## Rules

- Prefer gap closure over checklist phrasing.
- Preserve stable IDs.
- Include enough source summary for the plan to be understood without loading the full source artifact.
- Gaps can be closed by multiple items.
- Items can close multiple gaps when the coupling is real.
- A plan should make sense without tasks; plan items are not task packets.
- Plans may embed task summaries, but the plan skill does not create tasks.
- Full task packets should be external. Do not embed tasks.
