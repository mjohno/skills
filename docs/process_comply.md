# Skill Compliance Process

## Context
Assert a pass/fail test over an existing skill package against the universal format specification.

Use `docs/taxonomy.md` as the canonical category definition reference.

## Inputs
1. Subject skill directory

## Steps

### Phase 1: Category Detection
1. **Read Frontmatter**: Extract `metadata.category` from SKILL.md.
   - `metadata.category` must match `docs/taxonomy.md`
   - Missing or invalid → report as a Critical failure.
2. **Check Non-Invocable Contract Skills**: If the skill is a shared contract/interface skill, verify `disable-model-invocation: true` and compare against `docs/non_invocable_skills.md`.
3. **Load Checklist**: Use `assets/checklist.md` for all skill types.

### Phase 2: Compliance Test
1. Run each checklist item against the skill.
2. Record pass/fail for each item.
3. For failed items, note the specific violation.

### Phase 3: Reporting
1. **Pass**: All checklist items pass. Report: "Compliance passed."
2. **Fail**: One or more items fail. Report:
   - Items passed / Items failed
   - Each failed item with its specific violation

## Patterns
- **Category detection**: read `metadata.category` from frontmatter
- **Checklist**: single universal checklist for all categories
- **Reporting format**: structured pass/fail summary with violation details

## Constraints
1. Must use `assets/checklist.md` — no type-specific checklists
2. Must read `metadata.category` from frontmatter — never assume either
3. `metadata.category` must match `docs/taxonomy.md`

## Outputs
Compliance report with pass/fail result for each checklist item
