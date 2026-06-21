---
name: ideate
description: Generates and narrows solutions. Use when you need to brainstorm and evaluate potential approaches against defined requirements.
metadata:
  category: transform
---

# ideate

Goal: Generate and narrow solutions against defined requirements.
Non-Goals: Building prototypes, making final decisions, or implementing solutions.
Use-When: You need to brainstorm and evaluate potential approaches against defined requirements.

## 0. Prerequisites
- Problem statement and requirements from `define` skill

## 1. Inputs
- Problem statement and prioritized requirements from prompt
- Constraints and context (optional: budget, timeline, technical constraints)

## 2. Processes
1. Parse problem statement and requirements to understand the solution space
2. Brainstorm diverse solution approaches (divergent thinking)
3. Evaluate each approach against requirements and constraints
4. Narrow to top candidates using scoring or elimination
5. Document trade-offs, risks, and assumptions for each candidate
6. Flag where additional prototyping or research is needed

## 3. Outputs
- Structured output in the prompt with solution concepts, evaluation scores, and trade-offs
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `prototype` — make top solution concepts tangible
- `define` — revisit requirements if prototyping reveals gaps
- `collect` — gather more data to resolve uncertainty

## 5. Examples

### Example 1: Solution generation

**Prompt:** Generate solution concepts for the zero-trust problem statement.

**Outcome:** Prompt output with 5 solution concepts (e.g., "identity-first microsegmentation", "network-level policy engine"), each scored against requirements with trade-offs documented.

### Example 2: Solution narrowing

**Prompt:** Narrow the project management tool solutions to top 3 candidates.

**Outcome:** Prompt output with top 3 candidates ranked by requirement coverage, cost, and implementation risk.
