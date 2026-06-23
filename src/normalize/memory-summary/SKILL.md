---
name: memory-summary
description: Use when memory summary material needs canonical durable summary structure.
metadata:
  type: skill
  category: normalize
  capabilities:
    - memory
---
# memory-summary

Goal: Canonicalize durable memory summary content for the top-of-file `# Summary` section.
Non-Goals: Memory log appends, retrieval, or knowledge-base promotion.
Use-When: Dream workflow needs a clean summary section to write back.

## 0. Prerequisites
- Reduced summary material from `learn`
- The `memory-interface` contract

## 1. Inputs
- Stable summary updates
- Candidate replacements or deletions for existing summary lines
- Optional approval context for destructive changes

## 2. Processes
1. Read and follow the `memory-interface` contract.
2. Convert stable memory conclusions into concise summary prose or bullets.
3. Preserve durable facts, decisions, and preferences.
4. Remove log-specific noise and keep the summary compact.
5. Mark contradictions or replacement candidates when approval is required.
6. Produce a write-ready `# Summary` section for `dream`.

## 3. Outputs
- Canonical Summary section content
- Optional rewrite candidates for approval

## 4. Next Steps
- `map/dream` — compose the summary/log update workflow

## 5. Examples

### Example 1

**Prompt:** Summarize these durable memory decisions.
**Outcome:** Produces a compact write-ready Summary section.
