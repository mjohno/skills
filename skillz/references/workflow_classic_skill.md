# Skill Creation Workflow

## Context
Create a new classic standalone skill or update an existing skill package.

## Inputs
1. Skill name and description
2. Core purpose and goal
3. Optional components (scripts, references, assets)

## Steps

### Phase 1: Planning & Specification
1. **Identify Intent**: Determine the core purpose and goal of the skill.
2. **Name & Description**:
   - Use `kebab-case` for the `name` (must match the directory name).
   - Provide a concise `description` that includes "Use when..." triggers.
3. **Component Identification**: Determine if the skill requires:
   - `scripts/`: Executable logic.
   - `references/`: Detailed documentation or rules.
   - `assets/`: Templates or static resources.
4. **Constraint Check**: Verify the `name` uses `kebab-case`.

### Phase 2: Scaffolding
1. **Directory Creation**: Create the root directory `<name>/`.
2. **Initialize SKILL.md**: Use the template in `assets/skill_template.md` to ensure structural compliance.
   - Set `metadata.type: skill` in the frontmatter.
3. **Sub-directory Setup**: Create the `scripts/`, `references/`, and `assets/` directories as needed.

### Phase 3: Implementation & Refinement
- **Logic**: Develop self-contained, idempotent scripts in `scripts/`.
- **Documentation**: Populate `references/` with technical details or procedural specifics.
- **Resources**: Add necessary templates or data to `assets/`.
- **Quality Control**: Review the completed `SKILL.md` against `assets/checklist.md`.
   - Verify `metadata.type: skill` is set in frontmatter.

### Phase 4: Final Compliance
- Run `skills-ref validate <skill-dir>` to ensure the package is spec-compliant.

## Patterns
- **Naming**: kebab-case for skill names
- **Structure**: SKILL.md + optional scripts/, references/, assets/
- **Template**: Use `assets/skill_template.md` for SKILL.md scaffolding

## Constraints
1. Frontmatter has `metadata.type: skill`
2. Description includes triggers ("Use when...")
3. SKILL.md under 100 lines
4. Name uses `kebab-case`
5. No time-sensitive info
6. Consistent terminology
7. Concrete examples included
8. References one level deep

## Outputs
- A complete classic skill package with SKILL.md, optional scripts/, references/, and assets/
- Use template: `assets/skill_template.md`
- Use checklist: `assets/checklist.md`
