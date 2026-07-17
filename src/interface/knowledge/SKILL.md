---
name: knowledge
description: Use when lookup or record needs the passive MKF contract.
metadata:
  type: skill
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

## 2. Processes
1. Apply bundle discovery from `references/bundle_discovery.md`.
2. Apply concept structure and frontmatter rules from `references/mkf_contract.md`.
3. Treat `index.md` as an MKF concept with `type: index`.
4. Give `log.md` no special MKF semantics.
5. Preserve unknown frontmatter keys when operational skills update existing concepts.
6. Keep lookup-specific search/ranking behavior in `../../input/lookup/`.
7. Keep record-specific write, validation, template, and index-rebuild behavior in `../../output/record/`.

## 3. Outputs
- Shared MKF contract guidance for operational skills
- Relative links to shared references/assets

Shared references:
- `references/mkf_contract.md`
- `references/bundle_discovery.md`

Shared assets:
- `assets/concept_frontmatter_template.md`

## 4. Next Steps
- `../../input/lookup/SKILL.md` — retrieve MKF metadata matches and load selected concepts
- `../../output/record/SKILL.md` — create or update MKF concepts safely

## 5. Examples

### Example 1: Shared contract use

**Prompt:** Lookup needs to resolve `general`.
**Decision:** Use `references/bundle_discovery.md`; normalize `general` to `GENERAL`, then resolve `MKF_GENERAL_BUNDLE`.

### Example 2: Concept contract use

**Prompt:** Record needs to write a new concept.
**Decision:** Use `references/mkf_contract.md`; require `type`, `title`, `description`, and `tags`, and do not add `timestamp`.
