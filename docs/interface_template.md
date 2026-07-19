---
name: [interface-name]
description: ["Use when..." triggers for loading this interface]
metadata:
  type: interface
  category: interface
---

# [Interface Name]

Goal: [one clear contract this interface exposes]
Non-Goals: [work this interface does NOT perform — at least one]
Use-When: [triggers for loading this interface as passive contract context]

## 0. Prerequisites
- [context needed to select the applicable domain, references, or assets]

## 1. Inputs
- [selection clues such as artifact type, path, extension, backend, domain, or constraints]

## 2. Process
1. [select the default/generic domain when no specific domain is known]
2. [select domain-specific references/assets from explicit context when available]
3. [return only package-local references/assets needed to define the selected contract]
4. [mark missing domains or materially uncertain selections as assumptions]

## 3. Outputs
- Selected domain and assumptions
- Required reference file paths
- Required asset file paths
- Loaded reference contents in fenced code blocks
- Loaded asset/template contents in fenced code blocks

Output shape for each selected file:

file_path: src/interface/[interface-name]/references/[file].md
```markdown
[loaded contents of the selected reference file]
```

file_path: src/interface/[interface-name]/assets/[file]
```text
[loaded contents of the selected asset file]
```

## 4. Next Steps
- [downstream skill] — [how it consumes this interface]

## 5. Examples

### Example 1: Return contract path and contents

**Prompt:** Use the `[interface-name]` interface for `[artifact/context]`.
**Decision:** Select `[domain]`; return `src/interface/[interface-name]/references/[file].md` and `src/interface/[interface-name]/assets/[file]`.
**Outcome:** The caller receives each selected file path followed by loaded contents:

file_path: src/interface/[interface-name]/references/[file].md
```markdown
[Reference contract contents returned here.]
```

file_path: src/interface/[interface-name]/assets/[file]
```text
[Asset or template contents returned here.]
```
