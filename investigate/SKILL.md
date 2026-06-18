---
name: investigate
description: Curious fact-finding skill for building an evidence map from local files and, when needed, web sources. Use when you need exhaustive discovery, evidence-backed facts, and clear gaps without remediation.
metadata:
  category: discover
---

# investigate

Goal: Gather facts exhaustively and turn them into a compact evidence-first YAML context summary.
Non-Goals: Remediation, implementation plans, or speculative conclusions.
Use-When: You need to investigate a codebase, docs, or other sources to build context.

## 0. Prerequisites
- Target scope: files, directories, or topics to investigate

## 1. Inputs
- Target scope from prompt (file paths, directories, or topics)
- Recursion or time limits (optional)

## 2. Processes
1. **Scope first**: confirm the objective, scope, and any recursion limit (default: unlimited) or time limit.
2. **Collect evidence**: prefer local files first; use web sources only when asked or when local evidence is insufficient.
3. **Track uncertainty**: if a claim is not fully supported, mark it `type: tentative`, add a confidence note, and keep gathering evidence.
4. **Resolve conflicts**: present conflicting readings side by side and record the gap needed to settle them.
5. **Stop when exhausted**: keep investigating until scope gaps are exhausted or the recursion limit is reached.
6. **Return YAML**: default output is YAML; do not write files unless explicitly asked.
7. **Produce Fact Summary**: include a concise and information dense summary of the main facts and unresolved gaps.

## 3. Outputs
- YAML output in the prompt with `summary`, `facts`, and `gaps`
- If user specifies an output file, write to that path instead

```yaml
summary: <compact evidence-backed summary>
facts:
  - fact: <fact>
    source: <file>:<line>
  - fact: <tentative fact>
    type: tentative
    confidence: <low|medium|high>
    note: <why this is tentative>
    source: <file>:<line>
gaps:
  - gap: <gap>
    next_steps: [<step>, <step>]
```

## 4. Next Steps
- `collect` — gather more data to resolve gaps
- `analyze` — find patterns and contradictions in the evidence
- `hypothesize` — form hypotheses from the evidence
- `synthesize` — combine findings into a coherent narrative

## 5. Examples

### Example 1
**Prompt:** Investigate `src/auth` and summarize how login works.
**Decisions:** Read local files first, cite every fact, and mark unclear behavior as tentative.
**Outcome:** YAML with `summary`, `facts` and `gaps`, no files written.

### Example 2
**Prompt:** Investigate the README and implementation for cache invalidation.
**Decisions:** Capture both readings when they conflict, then list the evidence needed to resolve them.
**Outcome:** YAML that surfaces both interpretations and the remaining gaps.
