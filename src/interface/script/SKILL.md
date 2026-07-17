---
name: script
description: Use when output, transform, or map skills need script-domain conventions, quality checks, and templates.
metadata:
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

## 2. Processes
1. Select the script domain from explicit language, file extension, shebang, runtime clues, or default to Python.
2. Always include generic script conventions from `references/generic_conventions.md`.
3. For Python, include `references/python_conventions.md`, `references/python_quality.md`, and `assets/python_template.py`.
4. Treat templates as canonical shapes or starting points for consuming verb skills, not as mandatory output.
5. Mark domain assumptions only when selection is ambiguous or materially affects the artifact contract.

## 3. Outputs
- Script interface data for consuming skills:
  - selected domain/language and assumptions
  - generic conventions
  - domain-specific conventions
  - domain-specific quality checks
  - applicable template paths

## 4. Next Steps
- `output/outline` — create a script skeleton or function layout using this interface data
- `output/draft` — produce a first-pass script using this interface data
- `output/modify` — update an existing script against this interface data
- `transform/check` — verify a script against this interface data

## 5. Examples

### Example 1: Python default
**Prompt:** "Create a script that organizes files by extension with dry-run support."
**Outcome:** Selects Python by default and supplies generic conventions, Python conventions, Python quality checks, and `assets/python_template.py`.

### Example 2: Existing shell script
**Prompt:** "Review `cleanup.sh` against the script interface."
**Outcome:** Selects the shell-script domain from the extension; supplies generic conventions and marks shell-specific references as needed if unavailable.
