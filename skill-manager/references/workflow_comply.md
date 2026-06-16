# Skill Compliance Workflow

## Context
Assert a pass/fail test over an existing skill package against its type's specification.

## Inputs
1. Subject skill directory

## Steps

### Phase 1: Skill Type Detection
1. **Read Frontmatter**: Extract `metadata.type` from SKILL.md.
   - `metadata.type: router` → router skill
   - `metadata.type: skill` → classic skill
   - Missing or invalid → report as a Critical failure.
2. **Select Checklist**: Load the appropriate checklist.
   - `skill` → `assets/checklist.md`
   - `router` → `assets/router_checklist.md`

### Phase 2: Compliance Test
1. Run each checklist item against the skill.
2. Record pass/fail for each item.
3. For failed items, note the specific violation.

### Phase 3: Reporting
1. **Pass**: All checklist items pass. Report: "Compliance passed."
2. **Fail**: One or more items fail. Report:
   - Total items tested
   - Items passed / Items failed
   - Each failed item with its specific violation
   - Pass rate percentage

## Patterns
- **Type detection**: read `metadata.type` from frontmatter
- **Checklist selection**: one checklist per skill type
- **Reporting format**: structured pass/fail summary with violation details

## Constraints
1. Must use the correct checklist for the detected skill type
2. Must read `metadata.type` from frontmatter — never assume the type
3. `metadata.type` must be exactly `skill` or `router`

## Outputs
Compliance report with pass/fail result for each checklist item
