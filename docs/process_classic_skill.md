# Skill Creation Process

## Context
Create a new classic standalone skill or update an existing skill package.

Use `docs/taxonomy.md` as the canonical description of the skill categories.
If the skill is a shared contract/interface that should not be auto-invoked, follow `docs/non_invocable_skills.md` and set `disable-model-invocation: true`.

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
3. **Determine Category**: Choose one of seven categories defined in `docs/taxonomy.md`:
   - `interface` — shared contract or protocol for other skills
   - `input` — retrieve or read structured/raw source data
   - `enrich` — expand or elaborate data/context
   - `filter` — reduce, verify, rank, or select data
   - `normalize` — canonicalize structure or shape
   - `output` — persist, store, or deliver data
   - `map` — compose multi-step workflows
4. **Component Identification**: Determine if the skill requires:
   - `scripts/`: Executable logic.
   - `references/`: Detailed documentation or rules.
   - `assets/`: Templates or static resources.
   - `docs/non_invocable_skills.md`: for shared contract/interface skills that must not be model-invoked.
5. **Constraint Check**: Verify the `name` uses `kebab-case`.

### Phase 2: Scaffolding
1. **Directory Creation**: Create the root directory `<name>/`.
2. **Initialize SKILL.md**: Use the template in `assets/skill_template.md` to ensure structural compliance.
   - Set `metadata.type: skill`.
   - Set `metadata.category` (one of: interface, input, enrich, filter, normalize, output, map).
   - If the skill is a non-invocable shared contract, also set `disable-model-invocation: true` and follow `docs/non_invocable_skills.md`.
3. **Sub-directory Setup**: Create the `scripts/`, `references/`, and `assets/` directories as needed.

### Phase 3: Implementation & Refinement
- **Logic**: Develop self-contained, idempotent scripts in `scripts/`.
- **Documentation**: Populate `references/` with technical details or procedural specifics.
- **Resources**: Add necessary templates or data to `assets/`.
- **Quality Control**: Review the completed `SKILL.md` against `assets/checklist.md`.
   - Verify `metadata.type: skill` and `metadata.category` are set in frontmatter.



## Patterns
- **Naming**: kebab-case for skill names
- **Structure**: SKILL.md + optional scripts/, references/, assets/
- **Template**: Use `assets/skill_template.md` for SKILL.md scaffolding
- **Referenced files**: For larger skills, externalize Inputs/Processes/Outputs into `references/input_*.md`, `references/process_*.md`, or `references/output_*.md`



## Constraints
1. Frontmatter has `metadata.type: skill`
2. Frontmatter has `metadata.category` (one of: interface, input, enrich, filter, normalize, output, map)
3. Category meaning matches `docs/taxonomy.md`
4. Description includes triggers ("Use when...")
4. SKILL.md under 100 lines
5. Name uses `kebab-case`
6. No time-sensitive info
7. Consistent terminology
8. Concrete examples included
9. References one level deep
10. Shared contract/interface skills must follow `docs/non_invocable_skills.md`

## Outputs
- A complete classic skill package with SKILL.md, optional scripts/, references/, and assets/
