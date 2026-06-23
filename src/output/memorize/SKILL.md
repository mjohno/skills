---
name: memorize
description: Use when memory log entries need to be appended or updated.
metadata:
  type: skill
  category: output
  capabilities:
    - memory
---
# memorize

Goal: Append explicit memory entries to the memory log.
Non-Goals: Updating the durable summary directly, deduplicating memory, or opportunistic memory capture.
Use-When: The user explicitly asks to memorize something or a workflow step explicitly triggers memorization.

## 0. Prerequisites
- A resolved memory file
- The `memory-interface` contract
- Preferably a normalized `memory-entry`

## 1. Inputs
- Normalized memory-entry content or raw source material
- Optional memory file path or `MEMORY_FILE`
- Optional actor/source context

## 2. Processes
1. Read and follow the `memory-interface` contract.
2. Resolve the memory file from prompt path first, then `MEMORY_FILE`, then `.memory.md` in the current working directory.
3. If the resolved memory file does not exist and a write is explicitly requested, initialize the standard memory skeleton.
4. Prefer normalized `memory-entry` input and infer missing fields where practical before writing.
5. Append only to `# Memory Log`; do not update `# Summary`.
6. Write lightly normalized, clear memory bullets rather than raw transcript text by default.
7. Include actor/source labels when known, such as `User prefers`, `User chose`, `Agent observed`, or `Workflow completed`.
8. Allow multiple bullets in one invocation under the same timestamp heading.
9. Do not deduplicate against existing Summary or Memory Log content; `dream` handles deduplication later.
10. Avoid silently overwriting memory.

## 3. Outputs
- Updated memory file path
- Appended bullet content or initialization summary

## 4. Next Steps
- `normalize/memory-entry` — canonicalize the incoming memory entry
- `map/dream` — compact and rewrite memory later

## 5. Examples

### Example 1

**Prompt:** Store this new memory bullet.
**Outcome:** Appends a timestamped bullet to the Memory Log.
