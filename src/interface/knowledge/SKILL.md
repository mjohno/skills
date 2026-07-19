---
name: knowledge
description: Use when lookup or record needs the passive MKF contract.
metadata:
  type: interface
  category: interface
  capabilities:
    - knowledge
    - mkf
disable_model_invocation: true
---
# knowledge

Goal: Define the shared Matt's Knowledge Format (MKF) bundle and concept contract for operational skills.
Non-Goals: Do not perform lookup, write concepts, rebuild indexes, rank matches, or synthesize answers directly.
Use-When: `input/lookup` or `output/record` needs the shared MKF contract before reading or writing knowledge.

## 0. Prerequisites
- An MKF bundle selector, explicit bundle path, or concept document to interpret

## 1. Inputs
- Bundle names from `MKF_BUNDLES` or prompt selectors
- Explicit filesystem paths that should be treated as bundle roots
- MKF concept Markdown files when validating shared structure

## 2. Process
1. Apply bundle discovery from `references/bundle_discovery.md`.
2. Apply concept structure and frontmatter rules from `references/mkf_contract.md`.
3. Treat `index.md` as an MKF concept with `type: index`.
4. Give `log.md` no special MKF semantics.
5. Preserve unknown frontmatter keys when operational skills update existing concepts.
6. Keep lookup-specific search/ranking behavior in `../../input/lookup/`.
7. Keep record-specific write, validation, template, and index-rebuild behavior in `../../output/record/`.

## 3. Outputs
- Minimal default output: selected MKF domain, assumptions, selected package-local paths, and loaded selected contents only.
- Always return selected file paths followed by loaded contents in fenced code blocks.
- MKF selection returns:
  - `src/interface/knowledge/references/mkf_contract.md`
  - `src/interface/knowledge/references/bundle_discovery.md`
  - `src/interface/knowledge/assets/concept_frontmatter_template.md`

## 4. Next Steps
- `../../input/lookup/SKILL.md` — retrieve MKF metadata matches and load selected concepts
- `../../output/record/SKILL.md` — create or update MKF concepts safely

## 5. Examples

### Example 1: Shared contract use

**Prompt:** "Use the knowledge interface to resolve `general`."
**Decision:** Select MKF bundle discovery and MKF concept contract.
**Outcome:** Return selected paths and loaded contents:

file_path: src/interface/knowledge/references/bundle_discovery.md
```markdown
# Bundle Discovery
[loaded bundle discovery contract]
```

file_path: src/interface/knowledge/references/mkf_contract.md
```markdown
# MKF Contract
[loaded MKF contract]
```

### Example 2: Concept contract use

**Prompt:** "Use the knowledge interface before recording a new concept."
**Decision:** Select MKF concept contract and frontmatter template.
**Outcome:** Return selected paths and loaded contents:

file_path: src/interface/knowledge/assets/concept_frontmatter_template.md
```markdown
---
[loaded concept frontmatter template]
---
```
