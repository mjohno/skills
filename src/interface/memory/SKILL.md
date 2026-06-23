---
name: memory-interface
description: Use when remember, memorize, or dream needs the shared memory interface contract. Reference-only; not normally invoked directly.
metadata:
  type: skill
  category: interface
  capabilities:
    - memory
---
# memory-interface

Goal: Define the shared contract for memory file selection, sections, append/update safety, and compression rules.
Non-Goals: Writing or synthesizing memory directly.
Use-When: Another skill needs to resolve a memory file or follow memory write and cleanup conventions.

## 0. Prerequisites
- A prompt-provided memory file path or `MEMORY_FILE` environment variable when available

## 1. Inputs
- Prompt-provided memory file path
- `MEMORY_FILE` environment variable
- Optional task-specific file names such as `.memory.md` or `skill-memories.md`

## 2. Processes
1. Resolve the memory file from prompt-provided path first, then `MEMORY_FILE`, then `.memory.md` in the current working directory.
2. Do not introduce `MEMORY_ROOT`, named memory locations, or project/global config files yet.
3. Treat the file as Markdown with a `# Summary` section at the top and a `# Memory Log` section below.
4. Treat `# Summary` as the durable memory record.
5. Use UTC ISO-8601 timestamps with `Z` for log headings.
6. If multiple writes occur in the same second, append under the existing timestamp heading rather than creating a duplicate heading.
7. If the file is missing and a write is explicitly requested, initialize the standard skeleton.
8. Keep compression and deletion safety explicit: routine compression may happen later, but destructive summary rewrites require user approval.

## 3. Outputs
- Memory file resolution rules
- Append/update safety rules for `remember`, `memorize`, and `dream`

## 4. Next Steps
- `input/remember` — retrieve structured memory context
- `output/memorize` — append memory log entries
- `map/dream` — compact and rewrite memory summary/log

## 5. Examples

### Example 1

**Prompt:** Define shared memory file rules.
**Outcome:** Contract file fixes memory-file resolution and summary safety.
