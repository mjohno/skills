---
name: code
description: Use when output or map skills need the code artifact contract for implementation briefs.
disable-model-invocation: true
metadata:
  category: interface
  capabilities:
    - code_shape
    - implementation_brief
---

# code

Goal: Define the code artifact contract for responsibilities, boundaries, files, interfaces, tests, and constraints.
Non-Goals: Implementing code, choosing unrelated architecture, polishing documentation, deploying, or committing changes.
Use-When: Another skill needs the `code` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- Source request, task packet, spec, RFC, issue, design note, or existing code context
- Target language, framework, repository conventions, or affected files when known

## 1. Inputs
- Goal, source references, target files, expected behavior, and acceptance criteria
- Existing interfaces, constraints, dependency limits, security or performance concerns
- Optional verification commands, tests, fixtures, and migration notes

## 2. Processes
1. Identify the smallest coherent implementation unit and its responsibility.
2. Define affected files, public interfaces, data flow, dependencies, and invariants.
3. Capture behavior, edge cases, tests, and verification hints.
4. Separate required changes from optional improvements and unknowns.
5. Keep architecture references by link or summary instead of embedding large specs.

## 3. Outputs
- Interface-defined code brief contract consumed by `output/outline`, `output/draft`, or `output/modify`

Interface-defined shape:
```text
CODE:
Goal: Define the code artifact contract for responsibilities, boundaries, files, interfaces, tests, and constraints.
Sources:
Targets:
Interfaces:
Behavior:
Data Flow:
Constraints:
Edge Cases:
Tests:
Verification:
Risks:
Open Questions:
```

## 4. Next Steps
- `output/outline` — create file layout, interfaces, or implementation skeleton using this contract
- `output/draft` — produce first-pass implementation code using this contract
- `output/modify` — change existing code with a bounded delta

## 5. Examples

### Example 1: Code from RFC
**Prompt:** Define the code work for the auth middleware from this RFC.
**Outcome:** Produces a code brief naming targets, interfaces, behavior, constraints, tests, and verification.

### Example 2: Bug fix brief
**Prompt:** Shape this bug report into a code artifact brief.
**Outcome:** Produces the failing behavior, target files, expected fix boundary, edge cases, and tests to run.
