---
name: prd
description: Use when output or map skills need the PRD artifact contract for problem statements, requirements, and solution concepts.
disable-model-invocation: true
metadata:
  category: interface
  capabilities:
    - prd_formatting
---

# prd

Goal: Define the Product Requirements Document (PRD) contract.
Non-Goals: Technical design decisions, implementation details, or code generation.
Use-When: Another skill needs the `prd` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- Problem statement and requirements from `define` skill
- Solution concepts from `ideate` skill (optional)

## 1. Inputs
- Problem statement, requirements, and solution concepts from prompt
- Target audience and document conventions (optional)

## 2. Processes
1. Parse problem statement to establish the PRD's context and motivation
2. Structure the PRD: overview, problem statement, goals, non-goals, requirements
3. Document functional requirements with acceptance criteria
4. Document non-functional requirements (performance, security, usability)
5. Include solution rationale and trade-offs (if solution concepts available)
6. Add metrics for success and open questions

## 3. Outputs
- PRD section and field contract for output skills

## 4. Next Steps
- `filter/review` — evaluate the PRD for completeness and clarity
- `output/draft` with `interface/rfc` — produce an RFC for technical decisions related to the PRD
- `enrich/define` — revisit requirements if the PRD reveals gaps

## 5. Examples

### Example 1: PRD from requirements

**Prompt:** Write a PRD for the zero-trust architecture project.

**Outcome:** Prompt output with a structured PRD including problem statement, 12 functional requirements with acceptance criteria, 5 non-functional requirements, success metrics, and open questions.

### Example 2: PRD with solution rationale

**Prompt:** Write a PRD incorporating the top solution concepts.

**Outcome:** Prompt output with PRD sections including solution rationale, trade-off analysis, and recommended approach.
