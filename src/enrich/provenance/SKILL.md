---
name: provenance
description: Use when a claim needs source tracing or provenance checking.
metadata:
  category: enrich
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
1. Work with any information that makes factual claims.
2. Use only when asked to prove a fact or answer provenance questions.
3. Support the best available provenance for the source type:
   - local file: path and line number where practical
   - Markdown: path plus heading/section when line number is not practical
   - web: URL and title
   - tool output: command and relevant output excerpt
   - user: user-provided statement or context
   - memory: memory file plus timestamp section or summary section
   - knowledge base: root plus file path and heading/line where practical
4. Return information sources only by default.
5. Provide excerpts or more detail only when the user asks.
6. Categorize claims as `sourced`, `inferred`, `unsupported`, or `contradicted` when provenance is not plain.

## 3. Outputs
- Provenance notes or claim classifications
- Optional excerpts when explicitly requested

## 4. Next Steps
- Offer to provide an excerpt or more detail if the user wants it
- Suggest to use `lookup` or `remember` if source information was not found

## 5. Examples

### Example 1

**Prompt:** Prove where you got the claim that X is true.
**Outcome:** The local file `data.txt` and line number 42 where X is true. Would you like an excerpt?

### Example 2

**Prompt:** Prove where you got the claim that Y is false.
**Outcome:** I could not find any reference to support that claim. Should I attempt a `lookup` or try to `remember` it?
