# Artifact: Skill Package

## Target Structure
A skill package has these components:
- `SKILL.md` — main skill definition (frontmatter, Goal, Use When, Examples)
- `scripts/` — optional executable scripts
- `references/` — optional reference documents
- `assets/` — optional templates and examples

## Target Metadata
- Lives in a skills directory
- SKILL.md has YAML frontmatter with `name`, `description`, `metadata.type`
- `metadata.type` is `skill` or `router`
