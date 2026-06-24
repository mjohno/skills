---
name: prd
description: Normalizes problem statements, requirements, and solution concepts into a structured PRD document.
metadata:
  category: normalize
  capabilities:
    - prd_formatting
---

# prd

Goal: Format information into a structured Product Requirements Document (PRD).
Non-Goals: Technical design decisions, implementation details, or code generation.
Use-When: You need to produce a structured PRD from problem statements, requirements, and solution concepts.

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
- Structured PRD in the prompt
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `review` — have the `review` skill evaluate the PRD for completeness and clarity
- `rfc` — produce an RFC for technical decisions related to the PRD
- `define` — revisit requirements if the PRD reveals gaps

## 5. Examples

### Example 1: PRD from requirements

**Prompt:** Write a PRD for the zero-trust architecture project.

**Outcome:** Prompt output with a structured PRD including problem statement, 12 functional requirements with acceptance criteria, 5 non-functional requirements, success metrics, and open questions.

### Example 2: PRD with solution rationale

**Prompt:** Write a PRD incorporating the top solution concepts.

**Outcome:** Prompt output with PRD sections including solution rationale, trade-off analysis, and recommended approach.
