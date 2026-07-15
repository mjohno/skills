---
name: modify
description: Use when you need to revise, fix, update, adapt, expand, shorten, refactor, or otherwise change existing content or files.
metadata:
  category: output
  capabilities:
    - revision
    - content_modification
---

# modify

Goal: Apply requested changes to existing content while preserving intent, useful structure, and unrelated material.
Non-Goals: Creating unrelated new artifacts, silently rewriting everything, persisting memory/KB records, or committing changes.
Use-When: You need to modify, revise, fix, update, change, adapt, polish, expand, shorten, refactor, or reconcile content such as code, scripts, specs, plans, tasks, tests, prose, or interface-shaped artifacts.

## 0. Prerequisites
- Existing content, file path, draft, or interface-shaped artifact to modify
- Requested change, target outcome, or acceptance criteria

## 1. Inputs
- Current content or target files
- Change request, constraints, style preferences, and invariants to preserve
- Optional interface contract, diff context, tests, or verification commands

## 2. Processes
1. Identify the target artifact, requested delta, and content that must be preserved.
2. Ask or flag ambiguity when the requested change conflicts with existing intent.
3. Make the smallest coherent change unless the user asks for a broad rewrite.
4. Preserve structure, IDs, references, tone, and conventions where still valid.
5. Summarize what changed and note any verification performed or still needed.

## 3. Outputs
- Modified content in the prompt or updated files when paths are provided
- Concise change summary, including assumptions and residual risks

## 4. Next Steps
- `review` — evaluate the modified artifact
- `check` — validate the result against acceptance criteria
- `git-commit` — commit file changes when staged and approved

## 5. Examples

### Example 1: Modify a script
**Prompt:** Fix this script so dry-run never writes files.
**Outcome:** Updates only the relevant control flow and reports the behavioral change plus tests to run.

### Example 2: Modify a task packet
**Prompt:** Update this task with verification hints and target files.
**Outcome:** Preserves the task ID and goal while adding concise Targets and Verification sections.
