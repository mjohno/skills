# Skill Compliance Process

## Context
Assert a pass/fail test over an existing skill package against the universal format specification.

## Inputs
1. Subject skill directory

## Steps

### Phase 1: Category Detection
1. **Read Frontmatter**: Extract `metadata.category` from SKILL.md.
   - Valid categories: `discover`, `extract`, `transform`, `load`, `orchestrate`, `meta`
   - Missing or invalid → report as a Critical failure.
2. **Load Checklist**: Use `assets/checklist.md` for all skill types.

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
- **Category detection**: read `metadata.category` from frontmatter
- **Checklist**: single universal checklist for all categories
- **Reporting format**: structured pass/fail summary with violation details

## Constraints
1. Must use `assets/checklist.md` — no type-specific checklists
2. Must read `metadata.category` from frontmatter — never assume the category
3. `metadata.category` must be one of: discover, extract, transform, load, orchestrate, meta

## Outputs
Compliance report with pass/fail result for each checklist item
