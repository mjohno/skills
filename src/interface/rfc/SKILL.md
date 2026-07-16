---
name: rfc
description: Use when output or map skills need the RFC artifact contract for technical proposals and decisions.
disable-model-invocation: true
metadata:
  category: interface
  capabilities:
    - rfc_formatting
---

# rfc

Goal: Define the Request for Comments (RFC) contract.
Non-Goals: Making final decisions, implementing the design, or managing the review process.
Use-When: Another skill needs the `rfc` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- Future-state spec content shaped by `interface/spec`
- Technical decisions and architecture details (from prompt, source context, or `interface/prototype`)

## 1. Inputs
- Spec content from prompt
- Technical decisions, architecture details, and trade-offs from prompt

## 2. Processes
1. Parse the spec to establish the RFC's context, target state, and problem statement
2. Structure the RFC: title, status, context, proposed change, design details
3. Document the problem and proposed solution with technical specifics
4. Include alternative considerations and trade-off analysis
5. Add implementation plan, migration strategy, and rollback plan
6. Add a review checklist and decision criteria

## 3. Outputs
- RFC section and field contract for output skills

## 4. Next Steps
- `transform/review` — evaluate the RFC for completeness and clarity
- `interface/code` — code brief contract for RFC implementation decisions
- `output/draft` — produce first-pass implementation artifacts from the code brief
- `interface/spec` — future-state spec contract for revisiting requirements if the RFC reveals gaps

## 5. Examples

### Example 1: RFC from spec

**Prompt:** Write an RFC for migrating to zero-trust architecture based on the spec.

**Outcome:** Prompt output with a structured RFC including status (proposed), context, problem statement, proposed solution, alternatives considered, implementation plan, and review checklist.

### Example 2: RFC with alternatives

**Prompt:** Write an RFC evaluating three database options for the project.

**Outcome:** Prompt output with RFC sections including detailed comparison of PostgreSQL, MongoDB, and CockroachDB with trade-off matrix and recommendation.
