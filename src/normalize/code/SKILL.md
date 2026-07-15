---
name: code
description: Use when implementation intent needs a normalized code artifact brief before outlining, drafting, or modifying code.
metadata:
  category: normalize
  capabilities:
    - code_shape
    - implementation_brief
---

# code

Goal: Normalize implementation context into a code artifact brief with responsibilities, boundaries, files, interfaces, tests, and constraints.
Non-Goals: Implementing code, choosing unrelated architecture, polishing documentation, deploying, or committing changes.
Use-When: You need to turn a PRD, RFC, plan, task, bug report, or raw request into a consistent code shape before `outline`, `draft`, or `modify`.

## 0. Prerequisites
- Source request, task packet, PRD, RFC, issue, design note, or existing code context
- Target language, framework, repository conventions, or affected files when known

## 1. Inputs
- Goal, source references, target files, expected behavior, and acceptance criteria
- Existing interfaces, constraints, dependency limits, security or performance concerns
- Optional verification commands, tests, fixtures, and migration notes

## 2. Processes
1. Identify the smallest coherent implementation unit and its responsibility.
2. Normalize affected files, public interfaces, data flow, dependencies, and invariants.
3. Capture behavior, edge cases, tests, and verification hints.
4. Separate required changes from optional improvements and unknowns.
5. Keep architecture references by link or summary instead of embedding large specs.

## 3. Outputs
- Canonical code brief ready for `outline`, `draft`, or `modify`

Canonical shape:
```text
CODE:
Goal:
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
- `outline` — create file layout, interfaces, or implementation skeleton
- `draft` — produce first-pass implementation code
- `modify` — change existing code with a bounded delta

## 5. Examples

### Example 1: Code from RFC
**Prompt:** Normalize the code work for the auth middleware from this RFC.
**Outcome:** Produces a code brief naming targets, interfaces, behavior, constraints, tests, and verification.

### Example 2: Bug fix brief
**Prompt:** Shape this bug report into a code artifact brief.
**Outcome:** Produces the failing behavior, target files, expected fix boundary, edge cases, and tests to run.
