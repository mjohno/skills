---
name: lookup
description: Use when the user explicitly asks for a knowledge base or KB lookup.
metadata:
  type: skill
  category: input
  capabilities:
    - knowledge-base
---
# lookup

Goal: Retrieve structured knowledge base matches without synthesizing a final answer.
Non-Goals: Writing entries, cleaning entries, or turning matches into advice.
Use-When: The user explicitly asks to look up KB content or retrieve durable contextual knowledge.

## 0. Prerequisites
- A selected knowledge base root or explicit path
- The `knowledge-base-interface` contract

## 1. Inputs
- User query text
- Root selector(s), file selectors, or path selectors
- Optional tags, type filters, or root names

## 2. Processes
1. Read and follow the `knowledge-base-interface` contract.
2. Parse the user query and identify the selected root(s).
3. Search recursively inside the selected root by default.
4. Treat folder/path matches and filename matches as the same first tier.
5. Use tiered lexical search in this order: filename/path, then YAML frontmatter, then Markdown body.
6. Stop at the first tier that returns matches; if filename/path matches exist, return only those, otherwise check frontmatter, otherwise body.
7. If nothing matches across all tiers, try light query expansion such as singular/plural, hyphen/space variants, and obvious query-context synonyms.
8. Return the top 10 results by default; return all results only when explicitly requested.
9. Group results by root when multiple roots are selected.
10. Return structured raw context only.

## 3. Outputs
- Match records with path, root, matching field, and relevant excerpt or structured fields
- Empty result only when no useful knowledge exists

## 4. Next Steps
- `normalize/knowledge-entry` — shape raw knowledge into canonical form
- `output/record` — save or update durable KB content

## 5. Examples

### Example 1

**Prompt:** Look up the KB decision about folder semantics.
**Outcome:** Returns matching KB entries from the selected root.
