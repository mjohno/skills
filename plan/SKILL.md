---
name: plan
description: Manage ordered, gap-closing work plans. Use when you need to create, update, reorder, split, merge, status, or link plan items without executing the work.
metadata:
  category: load
---

# plan

Goal: Manage plans as ordered artifacts that close explicit gaps between a current state and a target state.
Non-Goals: Do not implement plan items, verify completed work, manage inline comments directly, or require full task packet detail inside every item.
Use-When: You need to turn a PRD, RFC, comment set, task set, or user request into an ordered work plan.

## 0. Prerequisites
- A source artifact (PRD, RFC, comment set, task set, or user request) to convert into a plan

## 1. Inputs
- Source artifact from prompt (PRD, RFC, comment set, task set, or user request)
- Target outcome or goal (optional)

## 2. Processes
1. **Create Plan**: Identify the source artifact and target outcome. Write a Gap Map: gap ID, current problem, target state. Write plan items that each close one or more gaps. Add dependencies, deliverables, and done criteria only when they reduce ambiguity.
2. **Update Plan**: Preserve existing plan IDs unless explicitly asked to rename them. Add, split, merge, or reorder items to improve gap closure. Keep plan status as planning metadata, not execution evidence.
3. **Check Plan Shape**: Every gap should have at least one closing item. Every item should name the gap it closes or the source it serves. Plan items may reference task packets but should not embed full task packets by default.

## 3. Outputs
- Structured plan in the prompt (PLAN_ID, gaps, items with status)
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `task` — extract task packets from plan items
- `step` — execute plan items one step at a time
- `annotate` — add inline annotations to track findings
- `plan` — revisit and update the plan as items complete

## 5. Examples

### Example 1: Gap-closing plan
**Prompt:** "Write a plan to split the todo skill into comment, plan, and task skills."
**Decisions:** Use a Gap Map first, then plan items that explicitly close those gaps.
**Outcome:**
```text
PLAN_ID: TODO-REFACTOR
GAP-1: todo mixes artifact management with execution -> artifact skills only manage artifacts
ITEM TODO-REFACTOR-1: Define artifact boundaries
Closes: GAP-1
Status: planned
```

### Example 2: Plan item update
**Prompt:** "Split TODO-REFACTOR-3 into format design and examples."
**Decisions:** Preserve the parent ID as a reference and create stable child IDs.
**Outcome:** `TODO-REFACTOR-3A` and `TODO-REFACTOR-3B` replace the oversized item.
