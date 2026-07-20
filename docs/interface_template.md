---
name: [interface-name]
description: ["Use when..." triggers for loading this interface]
metadata:
  type: interface
  category: interface
---

<!-- For context-only project terms, use vocab_template.md instead. -->

# [interface-name]

Goal: [one clear noun/domain contract this interface exposes]
Non-Goals: [work this interface does not perform]
Use-When: [triggers for loading this interface as passive contract context]

## Selection

Default: return only the minimal contract reference needed for common use.

Also select:
- `[optional_reference].md` when [explicit caller intent/domain condition].
- `[optional_asset]` when [explicit caller intent/domain condition].

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `src/interface/[interface-name]/references/[minimal_contract].md`

Optional paths:
- `src/interface/[interface-name]/references/[optional_reference].md`
- `src/interface/[interface-name]/assets/[optional_asset]`

## Next Steps

- [downstream skill] — [how it consumes this interface]

## Minimal Example

Prompt: "Use the `[interface-name]` interface for `[artifact/context]`."
Return:

file_path: src/interface/[interface-name]/references/[minimal_contract].md
```markdown
[loaded minimal contract contents]
```
