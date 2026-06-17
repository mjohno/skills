# Spec: Skill Package

This spec defines criteria for reviewing skill packages.

## Source References
- **Skill review workflow**: `skill-manager/references/workflow_review.md`

## Additional Criteria

### Frontmatter
1. Valid YAML frontmatter present
2. `metadata.type` is `skill` or `router`
3. `name` is present
4. `description` includes "Use when..." triggers

### Structure
1. SKILL.md exists at root
2. Directory structure follows convention: scripts/, references/, assets/ (optional)

### Content
1. Clear Goal section exists
2. Use When clauses present
3. Writing is information-dense and concise
4. No time-sensitive information
5. Consistent terminology
6. Concrete examples included under ## Examples
7. References are one level deep only

### Quality
1. SKILL.md under 100 lines
2. Template compliance (matches skill_template.md or router_skill_template.md)
3. Checklist verification passes
