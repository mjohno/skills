---
name: plan
description: Use when output, transform, or map skills need the plan artifact contract for ordered gap-closing work.
metadata:
  type: interface
  category: interface
---

# plan

Goal: Define the minimal plan artifact contract for closing gaps between current and target states.
Non-Goals: Do not draft, update, execute, verify, persist, or embed full task packets.
Use-When: Another skill needs the `plan` interface contract before drafting, modifying, checking, reviewing, or stepping through a plan artifact.

## Selection

Default: return only the compact plan contract.

Also select:
- `plan_checklist.md` when the caller asks to check plan conformance.
- `plan_quality.md` when the caller asks to review plan quality.

If caller intent is unclear, assume default contract only and state the assumption.
If requested plan needs fall outside this interface, state the unsupported need and hand off to the appropriate skill.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `src/interface/plan/references/plan_contract.md`

Optional paths:
- `src/interface/plan/references/plan_checklist.md`
- `src/interface/plan/references/plan_quality.md`

## Next Steps

- `draft` — create a first-pass plan from source context.
- `modify` — revise an existing plan while preserving stable IDs.
- `transform/check` — check plan conformance with `plan_checklist.md`.
- `transform/review` — review plan quality with `plan_quality.md`.
- `map/step` — execute one plan item or task packet.

## Minimal Example

Prompt: "Use the plan interface to draft a refactor plan."
Return:

file_path: src/interface/plan/references/plan_contract.md
```markdown
[loaded compact plan contract]
```
