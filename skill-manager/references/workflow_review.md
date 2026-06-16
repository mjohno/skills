# Skill Review Workflow

## Context
Audit an existing skill package for compliance, structure, and quality.

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

### Phase 2: Structure Audit
Verify the skill follows the standard directory structure:
- `SKILL.md` (Required)
- `scripts/` (Optional)
- `references/` (Optional)
- `assets/` (Optional)

### Phase 3: Metadata & Intent Review
- **Frontmatter**: Ensure `SKILL.md` uses valid YAML frontmatter for `name`, `description`, and `metadata.type`.
- **Goal**: Verify a clear `Goal:` section exists.
- **Triggers**: Check that the `description` includes "Use when..." triggers.

### Phase 4: Quality & Compliance Audit
Perform a deep review using the following tools:
- **Checklist Verification**: Run through every item in the selected checklist.
- **Template Compliance**: Compare the `SKILL.md` structure against the appropriate template (`assets/skill_template.md` for classic, `assets/router_skill_template.md` for router).
- **Content Density**: Ensure writing is information-dense, concise, and lacks time-sensitive information.
- **Reference Integrity**: Ensure references are only one level deep.

### Phase 5: Reporting
- Provide a summary of findings, categorizing issues by:
  - **Critical**: Violations of the core specification (e.g., missing `SKILL.md`, invalid YAML).
  - **Recommended**: Improvements for density, readability, or documentation quality.
- Provide a list of specific, actionable changes needed to reach compliance.

## Patterns
- **Finding categories**: Critical (spec violations) vs Recommended (quality)
- **Audit depth**: one level deep references only
- **Reporting format**: summary + actionable change list

## Constraints
1. Frontmatter has `metadata.type: skill` or `metadata.type: router`
2. Frontmatter description includes triggers ("Use when...")
3. SKILL.md under 100 lines
4. Root level has a Goal and Use When clauses
5. Writing is information dense and concise
6. No time-sensitive info
7. Consistent terminology
8. Concrete examples included under ## Examples
9. References one level deep

## Outputs
Audit report with categorized findings and actionable changes
