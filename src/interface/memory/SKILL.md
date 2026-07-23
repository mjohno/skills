---
name: memory
description: Use when remember, memorize, learn, or dream needs the shared memory file and content contract.
metadata:
  type: interface
  category: interface
  capabilities:
    - memory
---
# memory

Goal: Define the shared memory artifact contract for file selection, sections, entry shape, summary shape, and safety rules.
Non-Goals: Do not retrieve, write, synthesize, clean, compress, or persist memory directly.
Use-When: Another skill needs the `memory` interface contract before remembering, memorizing, learning from, or cleaning memory.

## Selection

Default: return only the compact memory contract.

If caller intent is unclear, assume default contract only and state the assumption.
If requested memory needs fall outside this interface, state the unsupported need and hand off to the appropriate skill.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `references/memory_contract.md`

## Next Steps

- `input/remember` — retrieve structured memory context.
- `output/memorize` — append memory log entries.
- `transform/learn` — reduce memory into stable summary updates.
- `map/dream` — compact and rewrite memory summary/log with approval where required.

## Minimal Example

Prompt: "Use the memory interface to define shared memory rules."
Return:

file_path: references/memory_contract.md
```markdown
[loaded compact memory contract]
```
