---
name: knowledge-entry
description: Use when raw knowledge needs canonical KB entry structure.
metadata:
  type: skill
  category: normalize
  capabilities:
    - knowledge-base
---
# knowledge-entry

Goal: Canonicalize durable knowledge base content into a stable Markdown-plus-frontmatter structure.
Non-Goals: Selecting roots, searching entries, or writing files directly.
Use-When: Raw or partially structured knowledge needs a consistent entry shape before record/update.

## 0. Prerequisites
- Raw knowledge text or an existing KB entry
- The `knowledge-base-interface` contract when KB rules matter

## 1. Inputs
- Title, type, summary, tags, source refs, and body content when available
- Raw notes that need normalization

## 2. Processes
1. Preserve or infer the required fields: `title`, `type`, `summary`, and `tags`.
2. Use optional fields when available: `id`, `sources`, `related`, `confidence`, `created`, `updated`.
3. Render the entry as Markdown with YAML frontmatter.
4. Keep the Markdown body as the durable human-readable content.
5. Keep frontmatter searchable and compact.
6. Prefer one idea per entry unless the source clearly represents a bundled concept.

## 3. Outputs
- Canonical KB entry structure

## 4. Canonical Shape
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
- `output/record` — write the normalized KB entry
- `input/lookup` — retrieve entries for comparison

## 5. Examples

### Example 1

**Prompt:** Turn these notes into a KB entry.
**Outcome:** Produces title, type, summary, tags, and body in canonical form.
