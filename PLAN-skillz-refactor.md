# PLAN-skillz-refactor

Goal: Update the `skillz` skill package to support the new universal skill format with category metadata, prerequisites, and no router support.

## GAP Map

| Gap ID | Current Problem | Target State |
|---|---|---|
| GAP-1 | `workflow_router_skill.md` creates router skills — routers are deprecated | Remove router workflow |
| GAP-2 | `assets/router_skill_template.md` templates router skills — no more routers | Remove router template |
| GAP-3 | `assets/router_checklist.md` checks router skills — no more routers | Remove router checklist |
| GAP-4 | `assets/skill_template.md` uses old format (Workflows heading, no numbered sections) | Replace with universal format (Goal/Non-Goals/Use-When flat, numbered sections 0-5) |
| GAP-5 | `assets/checklist.md` checks old format (metadata.type, Workflows heading) | Replace with checklist for universal format (category, numbered sections) |
| GAP-6 | `workflow_classic_skill.md` instructs creation using old format and metadata.type | Update to use universal format and metadata.category |
| GAP-7 | `workflow_comply.md` validates against type-based checklists (skill vs router) | Update to validate universal format, check category validity, verify prerequisites |
| GAP-8 | `skillz/SKILL.md` itself uses old format — needs to be the reference implementation | Update to conform to the new universal format |
| GAP-9 | No `type` field for classifying reference/asset files | Add optional `type` classification support for files in references/ and assets/ |

## Plan Items

### ITEM-1: Remove router workflow
**Closes:** GAP-1
**Description:** Delete `skillz/references/workflow_router_skill.md`. Routers are deprecated — all skills are composable transforms with soft coupling.
**Deliverable:** `references/workflow_router_skill.md` removed.
**Status:** done
**Committed:** `refactor(meta): remove router model from skillz`

### ITEM-2: Remove router template
**Closes:** GAP-2
**Description:** Delete `skillz/assets/router_skill_template.md`. No router skills will be created going forward.
**Deliverable:** `assets/router_skill_template.md` removed.
**Status:** done
**Committed:** `refactor(meta): remove router model from skillz`

### ITEM-3: Remove router checklist
**Closes:** GAP-3
**Description:** Delete `skillz/assets/router_checklist.md`. No router skills to check.
**Deliverable:** `assets/router_checklist.md` removed.
**Status:** done
**Committed:** `refactor(meta): remove router model from skillz`

### ITEM-4: Create universal skill template
**Closes:** GAP-4
**Description:** Replace `skillz/assets/skill_template.md` with the universal format:
```yaml
---
name: [name]
description: [description with use-when triggers]
metadata:
  category: [discover|extract|transform|load|orchestrate|meta]
---

# [Name]

Goal: [mandatory]
Non-Goals: [optional]
Use-When: [triggers for invoking this skill]

## 0. Prerequisites
- [what upstream skills or actions were expected to have run]

## 1. Inputs
- [inline description OR reference to input_*.md in references/ or assets/]

## 2. Processes
- [inline description OR reference to process_*.md in references/ or assets/]

## 3. Outputs
- [inline description OR reference to output_*.md in references/ or assets/]

## 4. Next Steps
- [Suggested follow-on actions or skills]

## 5. Examples
- [Usage examples]
```

**Naming convention for referenced files:**
- `references/input_<name>.md` or `assets/input_<name>.md` — input specification
- `references/process_<name>.md` or `assets/process_<name>.md` — process specification
- `references/output_<name>.md` or `assets/output_<name>.md` — output specification

Small skills keep Inputs/Processes/Outputs inline. Larger skills reference external files with the `input_`, `process_`, `output_` prefix.

**Deliverable:** `assets/skill_template.md` replaced with universal format.
**Status:** done
**Committed:** `feat(skillz): introduce universal skill format with category and numbered sections`

### ITEM-5: Create universal checklist
**Closes:** GAP-5
**Description:** Replace `skillz/assets/checklist.md` with checklist for universal format:
- [ ] `metadata.category` present (one of: discover, extract, transform, load, orchestrate, meta)
- [ ] Description includes "Use when..." triggers
- [ ] SKILL.md under 100 lines
- [ ] Under `# [Name]`: Goal (mandatory), Non-Goals (optional), Use-When (mandatory)
- [ ] Section 0: Prerequisites present (mandatory)
- [ ] Section 1: Inputs present (inline OR references/input_*.md / assets/input_*.md)
- [ ] Section 2: Processes present (inline OR references/process_*.md / assets/process_*.md)
- [ ] Section 3: Outputs present (inline OR references/output_*.md / assets/output_*.md)
- [ ] Section 4: Next Steps present (suggested downstream skills)
- [ ] Section 5: Examples present (at least one)
- [ ] Writing is information dense and concise
- [ ] No time-sensitive info
- [ ] Consistent terminology
- [ ] References one level deep
**Deliverable:** `assets/checklist.md` replaced with universal checklist.
**Status:** done
**Committed:** `feat(skillz): introduce universal skill format with category and numbered sections`

### ITEM-6: Update classic skill workflow
**Closes:** GAP-6
**Description:** Update `skillz/references/workflow_classic_skill.md` to:
- Use universal format (replacing old template reference)
- Use `metadata.category` instead of `metadata.type`
- Support inline or referenced Inputs/Processes/Outputs (input_, process_, output_ prefix convention)
- Remove router creation path
- Add category selection guidance (discover, extract, transform, load, orchestrate, meta)
- Update constraints to match new format
**Deliverable:** `references/workflow_classic_skill.md` updated.
**Status:** done
**Committed:** `feat(skillz): introduce universal skill format with category and numbered sections`

### ITEM-7: Update compliance workflow
**Closes:** GAP-7
**Description:** Update `skillz/references/workflow_comply.md` to:
- Remove type-based detection (no more skill vs router)
- Validate `metadata.category` is one of the six valid categories
- Validate all six numbered sections exist (0-5)
- Validate Inputs section exists (inline OR input_*.md reference)
- Validate Processes section exists (inline OR process_*.md reference)
- Validate Outputs section exists (inline OR output_*.md reference)
- Validate Next Steps present (suggested downstream skills)
- Validate Use-When is present under `# [Name]`
- Validate Goal is present under `# [Name]`
- Use `assets/checklist.md` for all compliance checks
**Deliverable:** `references/workflow_comply.md` updated.
**Status:** done
**Committed:** `feat(skillz): introduce universal skill format with category and numbered sections`

### ITEM-8: Update skillz SKILL.md to new format
**Closes:** GAP-8
**Description:** Update `skillz/SKILL.md` to conform to the universal format:
- Change `metadata.type: router` to `metadata.category: meta`
- Move Goal/Non-Goals/Use-When to flat key-value under `# skillz`
- Restructure sections to numbered 0-5 format
- Add Prerequisites, Inputs, Processes, Outputs (inline or referenced)

- Update examples to use new format
- Update description to mention category and universal format
**Deliverable:** `skillz/SKILL.md` updated to new format.
**Status:** done
**Committed:** `refactor(skillz): rewrite SKILL.md to universal format with inline routing`

### ITEM-9: Add type classification for reference/asset files
**Closes:** GAP-9
**Description:** Document the optional `type` field for classifying files in references/ and assets/:
- `type: template` — for .md templates
- `type: input` — for expected input formats
- `type: output` — for expected output formats
- `type: process` — for procedural reference docs
- `type: spec` — for specification documents
Add this as a note in `workflow_classic_skill.md` and the README.
**Deliverable:** `workflow_classic_skill.md` and `README.md` updated with type classification guidance.
**Status:** done
**Committed:** `refactor(skillz): rewrite SKILL.md to universal format with inline routing`
