---
name: define
description: Frames problems and defines requirements. Use when you need to produce a clear problem statement and structured requirements from synthesized insights.
metadata:
  category: transform
---

# define

Goal: Frame the problem and define structured requirements from synthesized insights.
Non-Goals: Generating solutions, implementing features, or making final design decisions.
Use-When: You need to produce a clear problem statement and structured requirements from synthesized insights.

## 0. Prerequisites
- Synthesis from `hypothesize` skill (themes, hypotheses, priorities)

## 1. Inputs
- Synthesis output from prompt (themes, hypotheses, data gaps)
- Domain context and constraints (optional)

## 2. Processes
1. Parse synthesis to identify the core problem being addressed
2. Frame a problem statement: who, what, why, and the impact of not solving it
3. Derive requirements from hypotheses and identified gaps
4. Categorize requirements (functional, non-functional, constraints, assumptions)
5. Prioritize requirements (must-have, should-have, nice-to-have)
6. Flag ambiguous or conflicting requirements for resolution

## 3. Outputs
- Structured output in the prompt with problem statement and prioritized requirements
- If user specifies output files, write to those paths instead

## 4. Next Steps
- `ideate` — generate solutions against defined requirements
- `collect` — gather more data to resolve ambiguous requirements
- `hypothesize` — revisit hypotheses if requirements reveal new gaps

## 5. Examples

### Example 1: Problem definition

**Prompt:** Define the problem and requirements from the zero-trust synthesis.

**Outcome:** Prompt output with a clear problem statement (e.g., "Current perimeter-based security allows lateral movement post-breach") and 12 prioritized requirements (7 must-have, 3 should-have, 2 nice-to-have).

### Example 2: Requirements specification

**Prompt:** Define requirements for a new project management tool for remote teams.

**Outcome:** Prompt output with problem statement, categorized requirements (functional, non-functional, constraints), and priority matrix.
