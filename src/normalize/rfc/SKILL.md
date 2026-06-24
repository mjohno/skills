---
name: rfc
description: Normalizes a PRD and technical decisions into a structured RFC document.
metadata:
  category: normalize
  capabilities:
    - rfc_formatting
---

# rfc

Goal: Format information into a structured Request for Comments (RFC) document.
Non-Goals: Making final decisions, implementing the design, or managing the review process.
Use-When: You need to produce a structured RFC from a PRD and technical decisions.

## 0. Prerequisites
- PRD from `prd` skill
- Technical decisions and architecture details (from `analyze`, `ideate`, or `prototype`)

## 1. Inputs
- PRD content from prompt
- Technical decisions, architecture details, and trade-offs from prompt

## 2. Processes
1. Parse PRD to establish the RFC's context and problem statement
2. Structure the RFC: title, status, context, proposed change, design details
3. Document the problem and proposed solution with technical specifics
4. Include alternative considerations and trade-off analysis
5. Add implementation plan, migration strategy, and rollback plan
6. Add a review checklist and decision criteria

## 3. Outputs
- Structured RFC in the prompt
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `review` — have the `review` skill evaluate the RFC for completeness and clarity
- `code` — produce code artifacts based on the RFC decisions
- `prd` — revisit requirements if the RFC reveals gaps

## 5. Examples

### Example 1: RFC from PRD

**Prompt:** Write an RFC for migrating to zero-trust architecture based on the PRD.

**Outcome:** Prompt output with a structured RFC including status (proposed), context, problem statement, proposed solution, alternatives considered, implementation plan, and review checklist.

### Example 2: RFC with alternatives

**Prompt:** Write an RFC evaluating three database options for the project.

**Outcome:** Prompt output with RFC sections including detailed comparison of PostgreSQL, MongoDB, and CockroachDB with trade-off matrix and recommendation.
