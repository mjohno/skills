---
name: script
description: Use when output, transform, or map skills need script-domain conventions, quality checks, and templates.
metadata:
  type: interface
  category: interface
---

# script

Goal: Define the script artifact contract and return the applicable conventions, quality checks, and templates for the selected script domain.
Non-Goals: Writing, modifying, executing, testing, deploying, or persisting scripts.
Use-When: Another skill needs the `script` interface before drafting, modifying, checking, reviewing, or orchestrating a script artifact.

## 0. Prerequisites
- Script purpose, user request, target file path, or existing script content
- Target language/runtime when known; if missing, use Python by default

## 1. Inputs
- Purpose, invocation context, inputs, outputs, side effects, constraints, and target path when available
- Existing file extension, shebang, imports, runtime notes, or user-stated language for domain selection
- Safety requirements such as dry-run, validation, idempotency, logging, and error handling

## 2. Process
1. Select the script domain from explicit language, file extension, shebang, runtime clues, or default to Python.
2. Always include generic script conventions from `references/generic_conventions.md`.
3. For Python, include `references/python_conventions.md`, `references/python_quality.md`, and `assets/python_template.py`.
4. For unsupported domains, return generic conventions only, mark domain-specific contracts as unavailable, and suggest `output/modify` to add a domain reference.
5. Treat templates as canonical shapes or starting points for consuming verb skills, not as mandatory output.
6. Mark domain assumptions only when selection is ambiguous or materially affects the artifact contract.

## 3. Outputs
- Minimal default output: selected domain/language, assumptions, selected package-local paths, and loaded selected contents only.
- Always return selected file paths followed by loaded contents in fenced code blocks.
- Python selection returns:
  - `src/interface/script/references/generic_conventions.md`
  - `src/interface/script/references/python_conventions.md`
  - `src/interface/script/references/python_quality.md`
  - `src/interface/script/assets/python_template.py`
- Unsupported domain selection returns `src/interface/script/references/generic_conventions.md` and an assumption noting domain-specific references/assets are unavailable.

## 4. Next Steps
- `output/outline` — create a script skeleton or function layout using this interface data
- `output/draft` — produce a first-pass script using this interface data
- `output/modify` — update an existing script against this interface data
- `transform/check` — verify a script against this interface data

## 5. Examples

### Example 1: Python default
**Prompt:** "Use the script interface for a file organizer script with dry-run support."
**Decision:** Select Python by default; return generic conventions, Python conventions, Python quality checks, and Python template.
**Outcome:** The caller receives selected paths and loaded contents:

file_path: src/interface/script/references/generic_conventions.md
```markdown
# Generic Script Conventions
[loaded generic conventions]
```

file_path: src/interface/script/assets/python_template.py
```python
#!/usr/bin/env python3
[loaded Python template]
```

### Example 2: Existing shell script
**Prompt:** "Use the script interface for `cleanup.sh`."
**Decision:** Select shell from the extension; shell-specific contract is unavailable.
**Outcome:** Return generic conventions only and note `assumption: shell-specific references/assets are unavailable`.

file_path: src/interface/script/references/generic_conventions.md
```markdown
# Generic Script Conventions
[loaded generic conventions]
```
