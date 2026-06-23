# Skill Compliance Process

## Context
Assert a pass/fail test over an existing skill package against the universal format specification.

Use `docs/taxonomy.md` as the canonical category definition reference.
If the subject is a shared contract/interface skill, also apply `docs/non_invocable_skills.md` and check that `disable-model-invocation: true` is set.

## Inputs
1. Subject skill directory

## Steps

### Phase 1: Category Detection
1. **Read Frontmatter**: Extract `metadata.type` and `metadata.category` from SKILL.md.
   - `metadata.type` must be `skill`
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
2. Must read `metadata.type` and `metadata.category` from frontmatter — never assume either
3. `metadata.type` must be `skill`
4. `metadata.category` must match `docs/taxonomy.md`
5. Shared contract/interface skills should be checked against `docs/non_invocable_skills.md`

## Outputs
Compliance report with pass/fail result for each checklist item
