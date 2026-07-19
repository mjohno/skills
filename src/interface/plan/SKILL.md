---
name: plan
description: Use when output or map skills need the plan artifact contract for ordered gap-closing work.
metadata:
  type: interface
  category: interface
---

# plan

Goal: Define the plan artifact contract for closing gaps between current and target states.
Non-Goals: Do not implement plan items, create task packets, verify completed work, manage inline comments directly, or embed full task packets.
Use-When: Another skill needs the `plan` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- A source artifact or context (spec, prompt, comment set, review findings, task set, investigation, or user request) to convert into a plan

## 1. Inputs
- Source artifact or context from prompt (spec, prompt, comment set, review findings, task set, investigation, or user request)
- Target outcome or goal (optional)

## 2. Process
1. **Create Plan**: Identify the source artifact or context and target outcome. Write a Source Summary that embeds the source details needed to understand and review the plan without re-reading the full source. Write a Gap Map: gap ID, source summary, current problem, target state. Write plan items that each close one or more gaps and reference relevant source IDs or topics when available. Add dependencies, deliverables, and done criteria only when they reduce ambiguity.
2. **Update Plan**: Preserve existing plan IDs unless explicitly asked to rename them. Add, split, merge, or reorder items to improve gap closure. Use standard lifecycle statuses: `todo`, `doing`, `verifying`, `reviewing`, `done`. Keep plan status as planning metadata, not execution evidence.
3. **Check Plan Shape**: Every gap should have at least one closing item. Every item should name the gap it closes or the source it serves. The plan should make sense without tasks and be readable end to end for review. Plans may embed task summaries, but the plan skill does not create tasks. Full task packets should be external; do not embed tasks.

## 3. Outputs
- Minimal default output: selected plan contract, assumptions, selected package-local paths, and loaded selected contents only.
- Always return selected file paths followed by loaded contents in fenced code blocks.
- Plan selection returns:
  - `src/interface/plan/references/plan_format.md`
  - `src/interface/plan/assets/plan_template.md`

## 4. Next Steps
- `output/draft` with `interface/task` — create external task packets when a plan item needs portable execution context
- `map/step` — execute a task packet or a small plan item when no separate task is needed
- `output/annotate` — add inline annotations to track findings
- `output/modify` with `interface/plan` — revisit and update the plan as items complete

## 5. Examples

### Example 1: Gap-closing plan
**Prompt:** "Use the plan interface to shape a todo refactor plan."
**Decision:** Select the standard plan format and template.
**Outcome:** Return selected paths and loaded contents:

file_path: src/interface/plan/references/plan_format.md
```markdown
# Plan Format
[loaded plan format contract]
```

file_path: src/interface/plan/assets/plan_template.md
```markdown
# Plan
[loaded plan template]
```
