---
name: provenance
description: Use when a skill output or claim needs source tracing or provenance checking.
metadata:
  type: skill
  category: filter
  capabilities:
    - provenance
    - knowledge-base
    - memory
---
# provenance

Goal: Trace factual claims back to source locations or best available provenance.
Non-Goals: Normal lookup, normal memory retrieval, or synthesis.
Use-When: The user asks where information came from or wants claim verification.

## 0. Prerequisites
- A claim, excerpt, or structured output to examine
- Any available source paths, timestamps, or tool output

## 1. Inputs
- Skill output that contains claims
- Local files, Markdown files, web URLs, tool output, user statements, memory, or KB entries

## 2. Processes
1. Work with any skill output that makes factual claims.
2. Use only when asked to prove a fact or answer provenance questions.
3. Support the best available provenance for the source type:
   - local file: path and line number where practical
   - Markdown: path plus heading/section when line number is not practical
   - web: URL and title
   - tool output: command and relevant output excerpt
   - user: user-provided statement or context
   - memory: memory file plus timestamp section or summary section
   - knowledge base: root plus file path and heading/line where practical
4. Return source information only by default.
5. Provide excerpts or more detail only when the user asks.
6. Categorize claims as `sourced`, `inferred`, `unsupported`, or `contradicted` when provenance is not plain.

## 3. Outputs
- Provenance notes or claim classifications
- Optional excerpts when explicitly requested

## 4. Next Steps
- `input/lookup` and `input/remember` — retrieve the original material
- `map/dream` — inspect memory claims during cleanup

## 5. Examples

### Example 1

**Prompt:** Trace the source for this claim.
**Outcome:** Returns source location and claim status.
