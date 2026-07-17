---
name: spec
description: Use when output or map skills need a future-state specification.
metadata:
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

## 2. Processes
1. Select the generic spec contract unless an explicit domain profile is provided.
2. Use `assets/generic_template.md` as the canonical section shape for new specs or major rewrites.
3. Require stable IDs for all referenceable claims, not every sentence, so downstream plans can trace to specific spec data points.
4. Keep future-state definition separate from implementation planning, technical decision records, review execution, and current-state investigation.
5. Use `references/generic_checklist.md` to evaluate completeness, section quality, and traceability.

## 3. Outputs
- Spec interface contract for consuming skills
- Canonical generic markdown template at `assets/generic_template.md`
- Generic spec quality checklist at `references/generic_checklist.md`

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
**Prompt:** Outline a spec for replacing the authentication module.
**Decisions:** Read `assets/generic_template.md`; create IDs for referenceable purpose, current-state, future-state, requirement, acceptance, quality, uncertainty, and decision claims.
**Outcome:** The outline skill produces a generic spec outline with sections for current state, future state, scope, requirements, acceptance, quality, expectations, uncertainties, and decisions as produced by the spec skill's generic template.

### Example 2: Review a spec
**Prompt:** Review `SPEC-auth-refresh.md` against the generic spec contract.
**Decisions:** Use `references/generic_checklist.md` as the evaluation checklist.
**Outcome:** The review skill reports CRITICAL failures and QUALITY issues, including missing sections, weak acceptance, untraced claims, or unclear uncertainties based upon the spec skill's `references/generic_checklist.md`.
