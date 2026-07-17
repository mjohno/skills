---
name: lookup
description: Use when the user explicitly asks for an MKF knowledge lookup.
metadata:
  type: skill
  category: input
  capabilities:
    - knowledge
    - mkf
---
# lookup

Goal: Retrieve best MKF metadata matches so selected concept files can be loaded as context.
Non-Goals: Do not write concepts, rebuild indexes, validate writes, or synthesize final advice from matches.
Use-When: The user explicitly asks to look up durable knowledge or retrieve MKF context.

## 0. Prerequisites
- User query text
- Bundle selector(s), all-bundle request, or explicit bundle path
- Shared contract: `../../interface/knowledge/SKILL.md`
- Bundle discovery: `../../interface/knowledge/references/bundle_discovery.md`
- MKF contract: `../../interface/knowledge/references/mkf_contract.md`
- Lookup process: `references/lookup_process.md`

## 1. Inputs
- Query text
- Optional bundle names or filesystem bundle paths
- Optional type/tag filters
- Optional result limit

## 2. Processes
1. Read the shared `knowledge` references only as needed.
2. Resolve selected bundle roots using the shared bundle discovery contract.
3. Use `scripts/search_mkf.py` for MKF search instead of ad hoc grep.
4. Search in deterministic order: resolved bundle path order, directory/file/concept-name matches, frontmatter metadata, then body content.
5. Return best metadata matches grouped by bundle.
6. Load full concept files only after the user or workflow selects matches that need full context.
7. Return structured raw context only.

## 3. Outputs
- Metadata match records with bundle, path, concept ID, type, title, description, tags, match tier, score, and excerpt when useful
- Empty result only when no useful MKF matches exist

## 4. Next Steps
- `../../output/record/SKILL.md` — create or update durable MKF concepts
- `../../interface/knowledge/references/mkf_contract.md` — interpret selected concept structure

## 5. Examples

### Example 1

**Prompt:** Look up checklist concepts in general.
**Outcome:** Runs `scripts/search_mkf.py`, returns matching concept metadata from the resolved `GENERAL` bundle, and does not synthesize advice.
