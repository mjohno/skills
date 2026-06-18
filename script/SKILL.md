---
name: script
description: Generate well-defined, production-quality Python scripts from natural language descriptions. Use when you need to create a script with proper structure, error handling, logging, input validation, dry-run support, and tests — using only stdlib.
metadata:
  category: load
---

# script

Goal: Generate well-defined, production-quality scripts from user descriptions.
Non-Goals: Deploying scripts, managing virtual environments, or writing tests for external APIs.
Use-When: You need to produce a Python script from a natural language description or specification.

## 0. Prerequisites
- A clear description of what the script should do (from user prompt)
- Target file path (required — always write to file)

## 1. Inputs
- Script purpose and functionality from user prompt
- Target file path (required)
- Target language (optional, defaults to Python)
- Specific requirements or constraints (optional)

## 2. Processes
1. **Parse** the user's description to extract: purpose, inputs, outputs, side effects, and edge cases
2. **Select** language conventions — defaults to Python; apply `references/python_conventions.md`
3. **Apply** the standard script structure from `references/script_structure.md`
4. **Generate** the script ensuring all quality criteria from `references/quality_checks.md` are met
5. **Write** the script to the specified file path

## 3. Outputs
- A complete script file at the specified path

## 4. Next Steps
- `test` — validate the generated script
- `review` — have the `review` skill evaluate script quality
- `script` — iterate or generate companion scripts

## 5. Examples

### Example 1: File organizer

**Prompt:** Write a script to `organize_files.py` that takes a directory path, groups files by extension into subdirectories, and logs what it did.

**Outcome:** `organize_files.py` with CLI args, argparse, logging, dry-run support, error handling, stdlib-only, and inline test functions.

### Example 2: Config validator

**Prompt:** Write a script to `validate_config.py` that reads a JSON config file, checks required keys exist, validates types, and exits with appropriate codes.

**Outcome:** `validate_config.py` with structured error codes, logging, input validation, dry-run mode, and test harness.
