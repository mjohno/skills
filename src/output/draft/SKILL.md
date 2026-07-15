---
name: draft
description: Use when you need to get first-pass content down for an artifact, complete enough to review or revise but not treated as final polish.
metadata:
  category: output
  capabilities:
    - drafting
    - content_generation
---

# draft

Goal: Produce first-pass artifact content from source material, optimized for completeness and editability over perfection.
Non-Goals: Creating only a skeleton, final polish, durable persistence, or making unstated product/technical decisions with false certainty.
Use-When: You need to write, compose, generate, fill, or create an initial version of content such as a script, code, PRD, RFC, plan, task, test, prose, or prototype.

## 0. Prerequisites
- Source material, outline, normalized artifact, or user request that states the desired artifact
- Target artifact noun from the prompt or a normalize skill when structure matters

## 1. Inputs
- Raw notes, requirements, outline, normalized structure, existing content, or examples
- Target audience, constraints, conventions, and desired level of completeness
- Optional output path or file layout

## 2. Processes
1. Identify the artifact noun, intended reader/runtime, and success criteria.
2. Use the supplied or inferred structure; call out missing inputs rather than inventing certainty.
3. Fill the artifact with coherent first-pass content at the requested fidelity.
4. Preserve placeholders for unresolved choices, risks, tests, or citations.
5. Prefer readable, reviewable output over exhaustive polish or premature optimization.

## 3. Outputs
- First-pass artifact content in the prompt
- If user specifies output files, write the draft to those paths instead
- Brief notes on assumptions, placeholders, and recommended follow-up

## 4. Next Steps
- `modify` — revise, fix, polish, expand, or adapt the draft
- `review` — evaluate the draft against requirements or persona criteria
- `record`, `memorize`, or `git-commit` — persist durable outputs when explicitly requested

## 5. Examples

### Example 1: Draft a script
**Prompt:** Draft a Python script from this outline.
**Outcome:** Produces a runnable first-pass script with clear TODOs for unresolved edge cases.

### Example 2: Draft a PRD
**Prompt:** Draft the PRD from these requirements.
**Outcome:** Produces a complete-enough PRD with goals, non-goals, requirements, metrics, risks, and open questions.
