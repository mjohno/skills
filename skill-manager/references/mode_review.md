# Mode: Review Skill

This mode is used to audit an existing skill package to ensure it is spec-compliant, well-structured, and high-quality.

## Workflow

### Phase 1: Structure Audit
Verify the skill follows the standard directory structure:
- `SKILL.md` (Required)
- `scripts/` (Optional)
- `references/` (Optional)
- `assets/` (Optional)

### Phase 2: Metadata & Intent Review
- **Frontmatter**: Ensure `SKILL.md` uses valid YAML frontmatter for `name` and `description`.
- **Goal**: Verify a clear `Goal:` section exists.
- **Triggers**: Check that the `description` includes "Use when..." triggers.

### Phase 3: Quality & Compliance Audit
Perform a deep review using the following tools:
- **Checklist Verification**: Run through every item in `assets/checklist.md`.
- **Template Compliance**: Compare the `SKILL.md` structure against `assets/skill_template.md`.
- **Content Density**: Ensure writing is information-dense, concise, and lacks time-sensitive information.
- **Reference Integrity**: Ensure references are only one level deep.

### Phase 4: Reporting
- Provide a summary of findings, categorizing issues by:
    - **Critical**: Violations of the core specification (e.g., missing `SKILL.md`, invalid YAML).
    - **Recommended**: Improvements for density, readability, or documentation quality.
- Provide a list of specific, actionable changes needed to reach compliance.
