---
name: envision
description: Use when memory context needs expansion into themes, connections, questions, or implications.
metadata:
  type: skill
  category: enrich
  capabilities:
    - memory
---
# envision

Goal: Increase entropy from memory context so later cleanup can find themes and candidate summary updates.
Non-Goals: Final cleanup decisions, knowledge-base promotion, or direct file writes.
Use-When: Memory needs expansion into higher-level meaning before reduction.

## 0. Prerequisites
- Raw memory context from `remember` or related workflow input
- The `memory-interface` contract

## 1. Inputs
- Memory bullets, notes, or raw memory excerpts
- Optional thread, project, or time context

## 2. Processes
1. Read and follow the `memory-interface` contract.
2. Expand messy memory into themes, associations, open questions, and implications.
3. Identify possible summary candidates without committing to cleanup.
4. Surface repeated signals, tensions, and context that might matter later.
5. Avoid deciding what to delete, compress, or promote.
6. Do not make knowledge-base promotion decisions; memory and knowledge base remain uncoupled.

## 3. Outputs
- Themes, connections, open questions, and candidate summary material

## 4. Next Steps
- `filter/learn` — reduce the expanded memory into stable summary updates
- `normalize/memory-summary` — format the summary material

## 5. Examples

### Example 1

**Prompt:** Expand these raw notes into themes and implications.
**Outcome:** Produces candidate themes and open questions.
