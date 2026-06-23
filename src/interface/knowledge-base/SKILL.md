---
name: knowledge-base-interface
description: Use when a lookup or record skill needs the shared knowledge base interface contract. Reference-only; not normally invoked directly.
metadata:
  type: skill
  category: interface
  capabilities:
    - knowledge-base
---
# knowledge-base-interface

Goal: Define the shared contract for knowledge base roots, selectors, storage format, search scope, and write safety.
Non-Goals: Performing lookup or record operations directly.
Use-When: Another skill needs to resolve a knowledge base root, read entry format rules, or follow knowledge base write conventions.

## 0. Prerequisites
- A prompt-provided root selector, environment selector, or explicit path

## 1. Inputs
- Root names or explicit paths from the prompt
- Optional subfolder selectors such as `project/decisions/` or `~/folder/structure/`
- Environment-based selectors when present

## 2. Processes
1. Resolve roots from prompt selectors first, then environment variables, then ask for an explicit root or path when ambiguous.
2. Accept either configured root names or explicit paths as valid selectors.
3. Treat folder/path matches and filename matches as a shared first-tier path selector concept.
4. Support multiple named roots and group results by root when more than one root is selected.
5. Search recursively inside the selected root by default.
6. Use Markdown files with YAML frontmatter as the durable knowledge base format.
7. Treat YAML frontmatter as searchable metadata and the Markdown body as the durable human-readable content.
8. Require explicit confirmation before overwriting existing content.
9. Create new filenames from title slugs and handle collisions safely.
10. Support human-meaningful folder structures inside each root.

## 3. Outputs
- Root-selection and storage guidance for invocable KB skills
- Shared conventions for read/write/search behavior

## 4. Next Steps
- `input/lookup` — retrieve knowledge base matches
- `output/record` — save or update knowledge base entries
- `normalize/knowledge-entry` — canonicalize KB entry structure

## 5. Examples

### Example 1

**Prompt:** Define a shared KB contract.
**Outcome:** Contract file documents roots, search tiers, and write safety.
