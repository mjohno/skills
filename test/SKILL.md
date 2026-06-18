---
name: test
description: Evaluates prototypes and solutions against requirements and hypotheses. Use when you need to validate whether a solution meets its target criteria.
metadata:
  category: transform
---

# test

Goal: Evaluate prototypes and solutions against requirements and hypotheses to determine pass/fail status.
Non-Goals: Fixing failures, implementing solutions, or making final go/no-go decisions.
Use-When: You need to validate whether a solution meets its target criteria.

## 0. Prerequisites
- Prototype from `prototype` skill
- Requirements from `define` skill

## 1. Inputs
- Prototype description and artifacts from prompt
- Requirements from prompt (or user can specify files)

## 2. Processes
1. Parse prototype to understand what was built and its scope
2. Map prototype features against each requirement
3. Evaluate against hypotheses from `hypothesize` (if available)
4. For each requirement: test coverage, correctness, edge cases
5. Score prototype against requirements (pass, partial, fail, not tested)
6. Document failures, gaps, and risks with severity and impact

## 3. Outputs
- Structured test results in the prompt (requirement-by-requirement evaluation with scores)
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `ideate` — if requirements fail, generate alternative solutions
- `prototype` — if prototype fixes are needed, build revised version
- `define` — if requirements need re-framing, revisit problem statement
- `collect` — if test results are ambiguous, gather more data

## 5. Examples

### Example 1: Requirements validation

**Prompt:** Test the zero-trust PoC against the requirements.

**Outcome:** Prompt output with requirement-by-requirement evaluation: 9 passed, 2 partial, 1 fail, with severity and impact documented for each.

### Example 2: Hypothesis validation

**Prompt:** Validate whether the prototype supports the core hypothesis about identity-based access.

**Outcome:** Prompt output with hypothesis evaluation: supported/not supported/insufficient evidence, plus confidence level and data needed for further validation.
