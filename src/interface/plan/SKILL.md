---
name: plan
description: Use when output or map skills need the plan artifact contract for ordered gap-closing work.
metadata:
  type: interface
  category: interface
  capabilities:
    - gap_analysis
    - ordered_artifact_creation
---

# plan

Goal: Define the plan artifact contract for closing gaps between current and target states.
Non-Goals: Do not implement plan items, verify completed work, manage inline comments directly, or require full task packet detail inside every item.
Use-When: Another skill needs the `plan` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- A source artifact (spec, RFC, comment set, task set, or user request) to convert into a plan

## 1. Inputs
- Source artifact from prompt (spec, RFC, comment set, task set, or user request)
- Target outcome or goal (optional)

## 2. Process
1. **Create Plan**: Identify the source artifact and target outcome. Write a Gap Map: gap ID, current problem, target state. Trace plan items to relevant spec IDs when the source is shaped by `interface/spec`. Write plan items that each close one or more gaps. Add dependencies, deliverables, and done criteria only when they reduce ambiguity.
2. **Update Plan**: Preserve existing plan IDs unless explicitly asked to rename them. Add, split, merge, or reorder items to improve gap closure. Keep plan status as planning metadata, not execution evidence.
3. **Check Plan Shape**: Every gap should have at least one closing item. Every item should name the gap it closes or the source it serves. Plan items may reference task packets but should not embed full task packets by default.

## 3. Outputs
- Minimal default output: selected plan contract, assumptions, selected package-local paths, and loaded selected contents only.
- Always return selected file paths followed by loaded contents in fenced code blocks.
- Plan selection returns:
  - `src/interface/plan/references/plan_format.md`
  - `src/interface/plan/assets/plan_template.md`
- Migration requests may also return `src/interface/plan/references/migration_from_todo.md`.

## 4. Next Steps
- `output/draft` with `interface/task` — extract task packets from plan items
- `map/step` — execute plan items one step at a time
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

### Example 2: Migration from todo
**Prompt:** "Use the plan interface to migrate an old todo artifact."
**Decision:** Select the standard plan contract plus migration reference.
**Outcome:** Return selected paths and loaded contents, including:

file_path: src/interface/plan/references/migration_from_todo.md
```markdown
# Migration From Todo
[loaded migration guidance]
```
