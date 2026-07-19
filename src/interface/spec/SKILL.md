---
name: spec
description: Use when output or map skills need a future-state specification.
metadata:
  type: interface
  category: interface
---

# spec

Goal: Define the minimal future-state specification contract for traceable artifacts.
Non-Goals: Do not investigate current state, draft spec content, review correctness, create plans, make technical decisions, or implement work.
Use-When: Another skill needs the `spec` interface contract before outlining, drafting, modifying, checking, reviewing, investigating toward, or planning from a spec artifact.

## Selection

Default: return only the compact spec contract.

Also select:
- `spec_template.md` when the caller asks to outline or draft a spec.
- `spec_checklist.md` when the caller asks to check spec conformance.
- `spec_quality.md` when the caller asks to review spec quality.

If caller intent is unclear, assume default contract only and state the assumption.
If requested spec needs fall outside this interface, state the unsupported need and hand off to the appropriate skill.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `src/interface/spec/references/spec_contract.md`

Optional paths:
- `src/interface/spec/assets/spec_template.md`
- `src/interface/spec/references/spec_checklist.md`
- `src/interface/spec/references/spec_quality.md`

## Next Steps

- `input/investigate` — gather current-state facts and uncertainty evidence.
- `output/outline` — create a spec skeleton using `spec_template.md`.
- `output/draft` — fill the spec from source material.
- `output/modify` — revise a spec while preserving stable IDs.
- `transform/check` — check spec conformance with `spec_checklist.md`.
- `transform/review` — review spec quality with `spec_quality.md`.
- `interface/plan` — create traceable gap-closing work from spec IDs.

## Minimal Example

Prompt: "Use the spec interface for replacing the authentication module."
Return:

file_path: src/interface/spec/references/spec_contract.md
```markdown
[loaded compact spec contract]
```
