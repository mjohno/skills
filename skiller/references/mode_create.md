# Mode: Create/Update Skill

This mode is used to scaffold a new skill from scratch or to add/update components in an existing skill directory.

## Workflow

### Phase 1: Planning & Specification
- **Identify Intent**: Determine the core purpose and goal of the skill.
- **Name & Description**: 
    - Use `kebab-case` for the `name` (must match the directory name).
    - Provide a concise `description` that includes "Use when..." triggers.
- **Component Identification**: Determine if the skill requires:
    - `scripts/`: Executable logic.
    - `references/`: Detailed documentation/rules.
    - `assets/`: Templates or static resources.
- **Constraint Check**: Verify the `name` complies with [Rules](references/RULES.md).

### Phase 2: Scaffolding
1. **Directory Creation**: Create the root directory `<name>/`.
2. **Initialize SKILL.md**: Use the template in `assets/skill_template.md` to ensure structural compliance.
3. **Sub-directory Setup**: Create the `scripts/`, `references/`, and `assets/` directories as needed.

### Phase 3: Implementation & Refinement
- **Logic**: Develop self-contained, idempotent scripts in `scripts/`.
- **Documentation**: Populate `references/` with technical details or procedural specifics.
- **Resources**: Add necessary templates or data to `assets/`.
- **Quality Control**: Review the completed `SKILL.md` against `assets/checklist.md`.

### Phase 4: Final Validation
- Run `skills-ref validate <skill-dir>` to ensure the package is spec-compliant.
