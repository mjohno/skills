---
name: script
description: Use when output or map skills need the script artifact contract for structure, conventions, or implementation briefs.
disable-model-invocation: true
metadata:
  category: interface
  capabilities:
    - script_shape
    - stdlib_python_conventions
---

# script

Goal: Define the script artifact contract for purpose, interface, behavior, safety expectations, and test hints.
Non-Goals: Writing the full script, executing it, managing environments, or persisting generated files.
Use-When: Another skill needs the `script` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- Script purpose, user request, task packet, bug report, or existing script content
- Target runtime or language when known; default conventions may use Python stdlib guidance

## 1. Inputs
- Purpose, inputs, outputs, side effects, constraints, and target file path when available
- Safety requirements such as dry-run, logging, validation, idempotency, and error handling
- Optional conventions from `references/python_conventions.md` and `references/quality_checks.md`

## 2. Processes
1. Extract the script's purpose, trigger, users, and operating context.
2. Define inputs, outputs, side effects, failure modes, and safety controls.
3. Identify CLI/API shape, dependencies, file layout, and test strategy.
4. Use `assets/script_template.py` only as structural guidance, not as a drafting obligation.
5. Mark unknowns and decisions needed before implementation.

## 3. Outputs
- Interface-defined script brief contract consumed by `output/outline`, `output/draft`, or `output/modify`

Interface-defined shape:
```text
SCRIPT:
Purpose:
Runtime:
Interface:
Inputs:
Outputs:
Side Effects:
Safety:
Errors:
Tests:
Dependencies:
Target Files:
Open Questions:
```

## 4. Next Steps
- `output/outline` — create a script skeleton or function layout using this contract
- `output/draft` — produce a first-pass script from this contract
- `output/modify` — update an existing script against this contract

## 5. Examples

### Example 1: File organizer
**Prompt:** Define a script that organizes files by extension with dry-run support.
**Outcome:** Produces a script brief with CLI args, filesystem side effects, logging, dry-run behavior, errors, and tests.

### Example 2: Existing script request
**Prompt:** Shape this bug report into a script update brief.
**Outcome:** Produces the target behavior, invariants to preserve, failure cases, and verification hints.
