---
name: knowledge-base
description: Use when lookup or record needs the shared knowledge base root, search, storage, and entry contract.
disable-model-invocation: true
metadata:
  type: skill
  category: interface
  capabilities:
    - knowledge-base
---
# knowledge-base

Goal: Define the shared contract for knowledge base roots, selectors, storage format, entry shape, search scope, and write safety.
Non-Goals: Performing lookup, recording entries, or synthesizing answers directly.
Use-When: Another skill needs to resolve a knowledge base root, read entry format rules, or follow knowledge base write conventions.

## 0. Prerequisites
- A prompt-provided root selector, environment selector, or explicit path

## 1. Inputs
- Root names or explicit paths from the prompt
- Optional subfolder selectors such as `project/decisions/` or `~/folder/structure/`
- Environment-based selectors when present
- Raw or partially structured knowledge when entry shape matters

## 2. Processes
1. Resolve roots from prompt selectors first, then environment variables, then ask for an explicit root or path when ambiguous.
2. Accept configured root names or explicit paths as valid selectors.
3. Treat folder/path matches and filename matches as a shared first-tier path selector concept.
4. Support multiple named roots and group results by root when more than one root is selected.
5. Search recursively inside the selected root by default.
6. Use Markdown files with YAML frontmatter as the durable knowledge base format.
7. Treat YAML frontmatter as searchable metadata and the Markdown body as durable human-readable content.
8. Required entry fields are `title`, `type`, `summary`, and `tags`; optional fields include `id`, `sources`, `related`, `confidence`, `created`, `updated`.
9. Prefer one idea per entry unless the source clearly represents a bundled concept.
10. Require explicit confirmation before overwriting existing content; create filenames from title slugs and handle collisions safely.

## 3. Outputs
- Root-selection and storage guidance for KB skills
- Shared read/write/search behavior
- Canonical Markdown-plus-frontmatter entry contract

Canonical entry shape:
```yaml
---
id:
title:
type: decision | convention | concept | pattern | gotcha | reference | note
summary:
tags:
sources:
related:
confidence:
created:
updated:
---

# Title

## Summary

## Content

## Sources
```

## 4. Next Steps
- `input/lookup` — retrieve knowledge base matches
- `output/record` — save or update knowledge base entries

## 5. Examples

### Example 1

**Prompt:** Define a shared KB contract.
**Outcome:** Contract documents roots, search tiers, entry shape, and write safety.
