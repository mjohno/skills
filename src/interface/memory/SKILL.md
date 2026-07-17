---
name: memory
description: Use when remember, memorize, learn, or dream needs the shared memory file and content contract.
metadata:
  type: skill
  category: interface
  capabilities:
    - memory
---
# memory

Goal: Define the shared contract for memory file selection, sections, entry shape, summary shape, append/update safety, and compression rules.
Non-Goals: Retrieving, writing, synthesizing, or cleaning memory directly.
Use-When: Another skill needs to resolve a memory file or follow memory structure, write, or cleanup conventions.

## 0. Prerequisites
- A prompt-provided memory file path or `MEMORY_FILE` environment variable when available

## 1. Inputs
- Prompt-provided memory file path
- `MEMORY_FILE` environment variable
- Optional task-specific file names such as `.memory.md` or `skill-memories.md`
- Raw memory entries or reduced summary material when content shape matters

## 2. Processes
1. Resolve the memory file from prompt-provided path first, then `MEMORY_FILE`, then `.memory.md` in the current working directory.
2. Do not introduce `MEMORY_ROOT`, named memory locations, or project/global config files yet.
3. Treat the file as Markdown with a `# Summary` section at the top and a `# Memory Log` section below.
4. Treat `# Summary` as the durable memory record; destructive summary rewrites require user approval.
5. Use UTC ISO-8601 timestamps with `Z` for log headings; append under an existing same-second heading.
6. If the file is missing and a write is explicitly requested, initialize the standard skeleton.
7. Keep entry payloads lightweight: preserve `content`; optionally include `id`, `date`, `kind`, `source`, `confidence`, `expires`, `tags`, `promote_to_kb`.
8. Render memory entries as clear bullets under timestamp headings, not raw transcripts.
9. Convert durable summary material into concise prose or bullets; mark contradictions or replacement candidates when approval is required.
10. Routine compression may happen later, but destructive summary rewrites require user approval.

## 3. Outputs
- Memory file resolution rules
- Memory log entry contract
- Durable summary section contract
- Append/update and compression safety rules

Canonical memory-entry shape:
```yaml
content:
id:
date:
kind: preference | fact | decision | reminder | thread | temporary | project-context
source:
confidence:
expires:
tags:
promote_to_kb:
```

Canonical summary output:
```text
# Summary

- <durable fact, decision, preference, or project context>
```

## 4. Next Steps
- `input/remember` — retrieve structured memory context
- `output/memorize` — append memory log entries
- `map/dream` — compact and rewrite memory summary/log

## 5. Examples

### Example 1

**Prompt:** Define shared memory file rules.
**Outcome:** Contract documents file resolution, entry shape, summary shape, and write safety.
