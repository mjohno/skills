---
name: record
description: Use when durable knowledge base content needs to be saved or updated.
metadata:
  type: skill
  category: output
  capabilities:
    - knowledge-base
---
# record

Goal: Save or update durable knowledge base entries explicitly.
Non-Goals: Opportunistic recording, memory writes, or answer synthesis.
Use-When: The user explicitly asks to record knowledge or a workflow step explicitly triggers KB recording.

## 0. Prerequisites
- A selected knowledge base root
- The `knowledge-base-interface` contract
- Preferably a normalized `knowledge-entry`

## 1. Inputs
- Normalized knowledge-entry content or raw source material
- Target root and optional folder selector
- Optional provenance/source references

## 2. Processes
1. Read and follow the `knowledge-base-interface` contract.
2. Require a target knowledge base root; ask when missing or ambiguous.
3. Prefer normalized `knowledge-entry` input and check whether the entry is already normalized.
4. If raw input is provided, infer missing required fields where practical before writing.
5. Update an existing similar entry rather than creating a duplicate when appropriate.
6. For new entries, write to the selected root/folder using a filename slug generated from the title.
7. If no folder is specified, write to `uncategorized/` under the selected root.
8. Ask the user how to proceed on filename collisions instead of auto-choosing a variant.
9. Preserve source references and avoid duplicate entries when possible.

## 3. Outputs
- A created or updated KB file path
- A concise write summary

## 4. Next Steps
- `normalize/knowledge-entry` — canonical KB entry format
- `input/lookup` — retrieve existing KB content before writing

## 5. Examples

### Example 1

**Prompt:** Persist this KB decision.
**Outcome:** Writes or updates a KB markdown entry.
