---
name: script
description: Use when output, transform, or map skills need script-domain conventions, quality checks, and templates.
metadata:
  type: interface
  category: interface
---

# script

Goal: Define the minimal script artifact contract and optional domain-specific conventions, checks, and templates.
Non-Goals: Do not write, modify, execute, test, deploy, or persist scripts.
Use-When: Another skill needs the `script` interface before drafting, modifying, checking, reviewing, or orchestrating a script artifact.

## Selection

Default: return only the compact script contract.

Also select:
- `python_contract.md` when Python is selected from language, file extension, shebang, runtime clues, or unspecified language default.
- `python_template.py` when the caller asks to outline or draft a Python script.
- `script_checklist.md` when the caller asks to check script conformance.
- `script_quality.md` when the caller asks to review script quality.

If caller intent is unclear, assume default contract only and state the assumption.
If the script domain is unsupported, return the generic contract, state unavailable domain-specific refs/assets, and hand off to `output/modify` to add a domain reference.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `src/interface/script/references/script_contract.md`

Optional paths:
- `src/interface/script/references/python_contract.md`
- `src/interface/script/assets/python_template.py`
- `src/interface/script/references/script_checklist.md`
- `src/interface/script/references/script_quality.md`

## Next Steps

- `output/outline` — create a script skeleton using applicable template data.
- `output/draft` — produce a first-pass script.
- `output/modify` — update an existing script against the contract.
- `transform/check` — check script conformance with `script_checklist.md`.
- `transform/review` — review script quality with `script_quality.md`.
- `map/step` — run a bounded implementation or verification step.

## Minimal Example

Prompt: "Use the script interface for a file organizer script with dry-run support."
Return:

file_path: src/interface/script/references/script_contract.md
```markdown
[loaded compact script contract]
```
