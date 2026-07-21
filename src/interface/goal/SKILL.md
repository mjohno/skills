---
name: goal
description: Use when output or transform skills need a SMART goal contract, template, or checklist.
metadata:
  type: interface
  category: interface
---

# goal

Goal: Define the minimal SMART goal contract for a clear, assessable intended outcome.
Non-Goals: Do not elicit goals, choose priorities, draft goal content, execute work, or evaluate achievement.
Use-When: Another skill needs the `goal` interface contract before drafting, modifying, checking, or reviewing a goal.

## Selection

Default: return only the compact SMART goal contract.

Also select:
- `goal_template.md` when the caller asks to outline or draft a goal.
- `goal_checklist.md` when the caller asks to check goal conformance or completeness.

If caller intent is unclear, assume the default contract only and state the assumption.
If the requested need falls outside this interface, state the unsupported need and hand off to the appropriate skill.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `src/interface/goal/references/goal_contract.md`

Optional paths:
- `src/interface/goal/assets/goal_template.md`
- `src/interface/goal/references/goal_checklist.md`

## Next Steps

- `draft` — create a first-pass goal from supplied context.
- `modify` — revise an existing goal while preserving its intended outcome.
- `transform/check` — check a goal against `goal_checklist.md`.
- `transform/review` — review goal clarity and feasibility.
- `map/step` — turn an approved goal into recorded, user-gated next-best-step progress.

## Minimal Example

Prompt: "Use the goal interface to draft a goal for reducing response times."
Return:

file_path: src/interface/goal/references/goal_contract.md
```markdown
[loaded compact SMART goal contract]
```
