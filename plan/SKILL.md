---
name: plan
description: Manage ordered, gap-closing work plans. Use when you need to create, update, reorder, split, merge, status, or link plan items without executing the work.
---

# plan

Goal: Manage plans as ordered artifacts that close explicit gaps between a current state and a target state.

Non-Goals: Do not implement plan items, verify completed work, manage inline comments directly, or require full task packet detail inside every item.

Use When:
- You need to turn a PRD, RFC, comment set, task set, or user request into an ordered work plan.
- You need to track what gap each plan item closes.
- You need to reorder, split, merge, or update plan items while preserving stable IDs.

## Workflows

### Create Plan
1. Identify the source artifact and target outcome.
2. Write a Gap Map: gap ID, current problem, target state.
3. Write plan items that each close one or more gaps.
4. Add dependencies, deliverables, and done criteria only when they reduce ambiguity.

### Update Plan
1. Preserve existing plan IDs unless explicitly asked to rename them.
2. Add, split, merge, or reorder items to improve gap closure.
3. Keep plan status as planning metadata, not execution evidence.

### Check Plan Shape
1. Every gap should have at least one closing item.
2. Every item should name the gap it closes or the source it serves.
3. Plan items may reference task packets but should not embed full task packets by default.

See [Plan Format](references/plan_format.md) and [Migration](references/migration_from_todo.md).

## Examples

### Example 1: Gap-closing plan
Prompt: "Write a plan to split the todo skill into comment, plan, and task skills."
Decisions: Use a Gap Map first, then plan items that explicitly close those gaps.
Outcome:
```text
PLAN_ID: TODO-REFACTOR
GAP-1: todo mixes artifact management with execution -> artifact skills only manage artifacts
ITEM TODO-REFACTOR-1: Define artifact boundaries
Closes: GAP-1
Status: planned
```

### Example 2: Plan item update
Prompt: "Split TODO-REFACTOR-3 into format design and examples."
Decisions: Preserve the parent ID as a reference and create stable child IDs.
Outcome: `TODO-REFACTOR-3A` and `TODO-REFACTOR-3B` replace the oversized item.
