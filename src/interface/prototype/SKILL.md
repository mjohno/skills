---
name: prototype
description: Use when output or map skills need the prototype artifact contract for cheap mock-ups or validation methods.
disable-model-invocation: true
metadata:
  category: interface
  capabilities:
    - prototype_shape
    - validation_method_selection
---

# prototype

Goal: Define the prototype artifact contract for what to mock, how to validate it, and what evidence matters.
Non-Goals: Building the prototype, producing production implementation, running experiments, or polishing final deliverables.
Use-When: Another skill needs the `prototype` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- Idea, solution concept, requirement, risk, or assumption to validate
- Target audience, environment, or decision to inform when available

## 1. Inputs
- Concept summary and the riskiest assumption
- Constraints such as time, fidelity, tools, audience, data, and safety limits
- Optional success criteria, failure criteria, and follow-up decision

## 2. Processes
1. Identify the decision the prototype must inform and the assumption being tested.
2. Select the cheapest adequate mock-up method for that assumption.
3. Define scope, fidelity, inputs, steps, and deliberately omitted work.
4. Specify observable validation signals and failure signals.
5. Format the result as a compact prototype brief contract consumed by `output/outline`, `output/draft`, or `output/modify`.

## 3. Outputs
- Prototype brief contract with method, assumption, scope, validation signals, and next decision

Interface-defined shape:
```text
PROTOTYPE:
Decision:
Assumption:
Method:
Audience/Context:
Scope:
Omitted:
Validation Signals:
Failure Signals:
Next Decision:
```

## 4. Next Steps
- `output/outline` — create the mock-up structure or experiment outline using this contract
- `output/draft` — produce first-pass prototype materials using this contract
- `transform/review` — stress-test the prototype design before spending effort

## 5. Examples

### Example 1: Fake-door test
**Prompt:** Define a prototype for validating whether admins want bulk invite templates.
**Outcome:** Produces a prototype brief using a fake-door UI or clickable mock-up, with validation and failure signals.

### Example 2: Technical spike
**Prompt:** Shape a prototype for testing whether local embeddings are fast enough.
**Outcome:** Produces a bounded spike brief with dataset size, timing signals, omitted production concerns, and next decision.
