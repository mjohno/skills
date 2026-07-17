# Skill Lifecycle

Full lifecycle for creating, verifying, and deploying skills.

## Context

Create or update a skill package that is structurally valid and beautifully simple.

## Inputs

1. Skill name, description, and category
2. Core purpose and goal

## Phase 1: Create

### Step 1 — Planning & Specification

1. **Identify Intent**: Determine the core purpose and goal of the skill.
2. **Name & Description**:
   - Use `kebab-case` for the name (must match directory name).
   - Provide a concise description that includes "Use when..." triggers.
3. **Determine Category**: Choose one category from [taxonomy.md](taxonomy.md):
   - `interface` — shared contract, schema, artifact shape, or protocol
   - `input` — retrieve, read, or elicit source data
   - `transform` — derive, evaluate, restructure, prioritize, reduce, or convert existing context
   - `output` — create, revise, persist, store, or deliver
   - `map` — compose multi-step workflows
   - `persona` — encode perspective that modifies information flow
4. **Determine Interface Role**: If the skill is an interface contract, ensure it is a discoverable contract provider that defines artifact shape, schema, protocol, conventions, or quality criteria without performing work.
5. **Place the Skill**:
   - Interface nouns live under `src/interface/<name>/SKILL.md`.
   - Invocable verb skills live under their data-flow category.
   - Persona lenses live under `src/persona/<name>/SKILL.md`.
6. **Component Identification**: Determine if the skill requires `scripts/`, `references/`, or `assets/`.
7. **Constraint Check**: Verify the name uses `kebab-case`.

### Step 2 — Scaffolding

1. Create root directory `<category>/<name>/`.
2. Initialize SKILL.md:
   - **Data-flow/interface skills** (interface, input, transform, output, map): use [skill_template.md](skill_template.md)
   - **Persona skills** (persona): use [persona_template.md](persona_template.md)
3. Create sub-directories (`scripts/`, `references/`, `assets/`) as needed.

### Step 3 — Implementation & Refinement

#### Data-flow and interface skills

- **Interface skills**: Define the desired state of a noun/domain and supply applicable conventions, checks, templates, schemas, or protocol rules. They are discoverable, contract-only reference skills and should not perform retrieval, transformation, evaluation, persistence, or orchestration.
  - Artifact interfaces define what a good artifact looks like.
  - Protocol interfaces define valid interaction shape.
  - Storage interfaces define layout, invariants, and access expectations.
  - Interfaces may select a profile from context, such as a language or backend, then expose that profile's contract data to consuming skills.
- **Invocable skills**: Develop self-contained, idempotent behavior and scripts where needed.
- **Documentation**: Populate `references/` with technical details, contract rules, or procedural specifics. Use names such as `generic_conventions.md`, `<domain>_conventions.md`, and `<domain>_quality.md` for profiled interface materials.
- **Resources**: Add templates or data to `assets/`. Use profile-specific names such as `<domain>_template.<ext>` when a template is not generic.
- **Quality reminder**: Remember the six simplicity principles — single responsibility, clear scope, graceful handoff, etc.

#### Persona skills

- Persona skills are pure documentation — no `scripts/`, `references/`, or `assets/` needed.
- Focus on writing a sharp Perspective statement, distinct Values & Priorities, honest Tradeoffs, and non-overlapping Focus Areas.
- **Quality reminder**: A persona is a *lens*, not a checklist. It should guide how the evaluator thinks, not produce a rigid rubric to fill in.

#### Anti-patterns to Avoid

- X Goals that say "help users understand X and Y and Z" — pick one
- X Process steps numbered 1–20 — if it takes this many, consider breaking into sub-skills
- X Non-goals that just repeat the goal in negative form ("We do not fail")
- X Interface skill that performs work instead of defining a contract
- X Interface skill that produces a brief unless the noun itself is a brief
- X Invocable skill that only defines an artifact schema instead of consuming an interface
- X Persona encodes a narrow opinion rather than an established evaluation lens
- X Persona overlaps with another persona's focus areas
- X Persona becomes a full review rubric instead of a perspective

### Step 4 — Compliance Check

Run [compliance](#phase-2---comply) against the appropriate checklist:
- **Data-flow/interface skills** → [skill_checklist.md](skill_checklist.md)
- **Persona skills** → [persona_checklist.md](persona_checklist.md)

## Phase 2 — Comply

Assert a pass/fail test over an existing skill package against the appropriate checklist.

### Steps

1. **Read Frontmatter**: Extract `metadata.category` from SKILL.md.
   - Must match [taxonomy.md](taxonomy.md). Missing or invalid → Critical failure.
2. **Check Interface Contracts**: If the skill is an interface contract, verify it exposes contract data only and does not describe retrieval, transformation, evaluation, persistence, or orchestration behavior.
3. **Load Checklist**:
   - Data-flow/interface categories (interface, input, transform, output, map) → [skill_checklist.md](skill_checklist.md)
   - Persona category → [persona_checklist.md](persona_checklist.md)
4. **Run Checks**: Evaluate each item; record pass/fail with specific violations.
5. **Report**:
   - **Pass**: All CRITICAL items pass. Report "Compliance passed."
   - **Fail**: List passed/failed counts and each violation.

### Severity Classification

- **CRITICAL** — structural validity; must pass (category match, required sections, formatting)
- **QUALITY** — beautiful simplicity principles; should pass for excellence

A skill passes compliance if all CRITICAL items pass. A beautifully simple skill also passes QUALITY items.

## Phase 3 — Deploy

Synchronize a local skill directory to a `TARGET_DIRECTORY` for active use.

### Steps

1. **Pre-deploy Check**: Run compliance against the checklist. Do not deploy if any CRITICAL items fail.
2. **Identify Source**: Confirm the source skill directory.
3. **Identify Target**: Confirm the target directory.
4. **Choose Method**: Real-time Syncing (Symlinks/Junctions) or Manual Mirroring (Rsync/Robocopy).
5. **Confirm Plan**: State the source, target, and method to the user. Provide the exact command line.
   - *Windows Junction (CMD)*: `mklink /J "%USERPROFILE%\%TARGET_DIRECTORY%" "%CD%\src"`
   - *Windows Junction (PowerShell)*: `cmd /c mklink /J "%USERPROFILE%\%TARGET_DIRECTORY%" "%CD%\src"`
6. **User Approval**: Wait for explicit acceptance before executing.
7. **Execute & Verify**: Run the command; confirm files synchronized to target.

## Constraints

1. Must choose the correct checklist based on `metadata.category`: data-flow/interface → skill_checklist, persona → persona_checklist
2. Both checklists inherit shared rules from [base_checklist.md](base_checklist.md)
3. Must read `metadata.category` from frontmatter — never assume
4. Requires explicit user approval before deployment execution

## Outputs

- A complete skill package (create)
- Compliance report with pass/fail for each item (comply)
- Synchronized skill directory at target (deploy)
