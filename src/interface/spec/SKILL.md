---
name: spec
description: Use when output or map skills need a future-state specification.
metadata:
  type: interface
  category: interface
---

# spec

Goal: Define the generic specification structure and quality checks for traceable future-state artifacts.
Non-Goals: Investigating current state, drafting the spec content, reviewing correctness, creating plans, making technical decisions, or implementing work.
Use-When: Another skill needs the `spec` interface contract before outlining, drafting, modifying, reviewing, investigating toward, or planning from a future-state artifact.

## 0. Prerequisites
- A need to define or revise a future state across any domain
- Current-state findings, goals, requirements, examples, constraints, decisions, or uncertainty when available

## 1. Inputs
- Source context from prompt, files, investigation, conversation, or existing artifacts
- Target domain and desired fidelity when known
- Optional current-state findings from `input/investigate`
- Optional existing spec content to preserve or revise
- Generic markdown template: `assets/generic_template.md`
- Generic quality checklist: `references/generic_checklist.md`

## 2. Process
1. Select the generic spec contract unless an explicit domain profile is provided.
2. Use `assets/generic_template.md` as the canonical section shape for new specs or major rewrites.
3. Require stable IDs for all referenceable claims, not every sentence, so downstream plans can trace to specific spec data points.
4. Keep future-state definition separate from implementation planning, technical decision records, review execution, and current-state investigation.
5. Use `references/generic_checklist.md` to evaluate completeness, section quality, and traceability.

## 3. Outputs
- Minimal default output: selected spec contract, assumptions, selected package-local paths, and loaded selected contents only.
- Always return selected file paths followed by loaded contents in fenced code blocks.
- Generic spec selection returns:
  - `src/interface/spec/assets/generic_template.md`
  - `src/interface/spec/references/generic_checklist.md`

## 4. Next Steps
- `input/investigate` — gather current-state facts and uncertainty evidence for the spec
- `output/outline` — create a spec skeleton from the generic template
- `output/draft` — fill the spec from source material
- `output/modify` — revise an existing spec while preserving stable IDs unless renaming is requested
- `transform/review` — check the spec against the generic checklist
- `interface/plan` — create traceable gap-closing work from spec IDs
- `interface/rfc` — record technical proposal details when the spec requires technical decisions

## 5. Examples

### Example 1: Coding project spec outline
**Prompt:** "Use the spec interface for replacing the authentication module."
**Decision:** Select the generic spec template and checklist.
**Outcome:** Return selected paths and loaded contents:

file_path: src/interface/spec/assets/generic_template.md
```markdown
# Spec
[loaded generic spec template]
```

file_path: src/interface/spec/references/generic_checklist.md
```markdown
# Generic Spec Checklist
[loaded generic checklist]
```

### Example 2: Review a spec
**Prompt:** "Use the spec interface to review `SPEC-auth-refresh.md`."
**Decision:** Select the generic spec checklist.
**Outcome:** Return selected path and loaded contents:

file_path: src/interface/spec/references/generic_checklist.md
```markdown
# Generic Spec Checklist
[loaded generic checklist]
```
