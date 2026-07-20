---
name: change
description: Use when output, transform, or map skills need the temporary local change workspace contract.
metadata:
  type: interface
  category: interface
---

# change

Goal: Define the minimal temporary local workspace contract for work that concerns a target plus an intended or possible delta.
Non-Goals: Do not coordinate work, define a lifecycle, draft specs/plans/tasks/checks/reviews, implement changes, deploy, release, or create repository-level active-change state.
Use-When: Another skill needs the `change` interface contract before creating, using, checking, or coordinating temporary local change workspace artifacts.

## Selection

Default: return only the compact change contract.

Also select:
- `change_template.md` when the caller asks to create, scaffold, outline, or draft a `CHANGE.md` file.
- `change_checklist.md` when the caller asks to check change workspace conformance or skill compliance.

If caller intent is unclear, assume default contract only and state the assumption.
If requested change needs fall outside this interface, state the unsupported need and hand off to the appropriate skill.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `src/interface/change/references/change_contract.md`

Optional paths:
- `src/interface/change/assets/change_template.md`
- `src/interface/change/references/change_checklist.md`

## Next Steps

- `output/draft` — create a first-pass `CHANGE.md` from the template.
- `output/modify` — revise an existing change workspace artifact while preserving boundaries.
- `transform/check` — check change workspace conformance with `change_checklist.md`.
- `map/coordinate` — orchestrate local work using prompt coordinates or change-scoped `COORDS.md`.

## Minimal Example

Prompt: "Use the change interface for auth error cleanup."
Return:

file_path: src/interface/change/references/change_contract.md
```markdown
[loaded compact change contract]
```
