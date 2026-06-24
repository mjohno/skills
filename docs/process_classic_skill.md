# Skill Creation Process

## Context
Create or update an AgentSkills.io compliant skill package.

## Inputs
1. Skill name, description and category
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
4. - **Determine Non-Invocability**:
   - If the skill is a shared contract/interface, set `disable-model-invocation: true` in SKILL.md to prevent direct invocation by models.
4. **Component Identification**: Determine if the skill requires:
   - `scripts/`: Executable logic.
   - `references/`: Detailed documentation or rules.
   - `assets/`: Templates or static resources.
5. **Constraint Check**: Verify the `name` uses `kebab-case`.

### Phase 2: Scaffolding
1. **Directory Creation**: Create the root directory `<name>/`.
2. **Initialize SKILL.md**: Use the template in `docs/skill_template.md` to ensure structural compliance.
   - Set `metadata.category` (one of: interface, input, enrich, filter, normalize, output, map).
   - If the skill is a non-invocable shared contract, also set `disable-model-invocation: true`.
3. **Sub-directory Setup**: Create the `scripts/`, `references/`, and `assets/` directories as needed.

### Phase 3: Implementation & Refinement
- **Logic**: Develop self-contained, idempotent scripts in `scripts/`.
- **Documentation**: Populate `references/` with technical details or procedural specifics.
- **Resources**: Add necessary templates or data to `assets/`.
- **Quality Control**: Review the completed `SKILL.md` against `assets/checklist.md`.

## Patterns
- **Naming**: kebab-case for skill names
- **Structure**: SKILL.md + optional scripts/, references/, assets/
- **Template**: Use `assets/skill_template.md` for SKILL.md scaffolding
- **Referenced files**: For larger skills, externalize Inputs/Processes/Outputs into `references/input_*.md`, `references/process_*.md`, or `references/output_*.md`

## Constraints
See [docs/checklist.md](docs/checklist.md) for a comprehensive list of constraints.

## Outputs
- A complete AgentSkills.io skill package with SKILL.md, optional scripts/, references/, and assets/
