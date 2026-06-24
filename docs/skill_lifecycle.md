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
   - `interface` — shared contract or protocol
   - `input` — retrieve or read source data
   - `enrich` — expand or elaborate context
   - `filter` — reduce, verify, rank, or select
   - `normalize` — canonicalize structure
   - `output` — persist, store, or deliver
   - `map` — compose multi-step workflows
   - `persona` — encode perspective that modifies information flow
4. **Determine Non-Invocability**: If the skill is a shared contract/interface, set `disable-model-invocation: true` in SKILL.md frontmatter.
5. **Component Identification**: Determine if the skill requires `scripts/`, `references/`, or `assets/`.
6. **Constraint Check**: Verify the name uses `kebab-case`.

### Step 2 — Scaffolding

1. Create root directory `<name>/`.
2. Initialize SKILL.md:
   - **Data-flow skills** (interface, input, enrich, filter, normalize, output, map): use [skill_template.md](skill_template.md)
   - **Persona skills** (persona): use [persona_template.md](persona_template.md)
3. Create sub-directories (`scripts/`, `references/`, `assets/`) as needed.

### Step 3 — Implementation & Refinement

#### Data-flow skills

- **Logic**: Develop self-contained, idempotent scripts in `scripts/`.
- **Documentation**: Populate `references/` with technical details or procedural specifics.
- **Resources**: Add templates or data to `assets/`.
- **Quality reminder**: Remember the six simplicity principles — single responsibility, clear scope, graceful handoff, etc.

#### Persona skills

- Persona skills are pure documentation — no `scripts/`, `references/`, or `assets/` needed.
- Focus on writing a sharp Perspective statement, distinct Values & Priorities, honest Tradeoffs, and non-overlapping Focus Areas.
- **Quality reminder**: A persona is a *lens*, not a checklist. It should guide how the evaluator thinks, not produce a rigid rubric to fill in.

#### Anti-patterns to Avoid

- X Goals that say "help users understand X and Y and Z" — pick one (data-flow)
- X Process steps numbered 1–20 — if it takes this many, consider breaking into sub-skills (data-flow)
- X Non-goals that just repeat the goal in negative form ("We do not fail") (data-flow)
- X Persona encodes a narrow opinion rather than an established evaluation lens — personas should represent recognizable roles or perspectives
- X Persona overlaps with another persona's focus areas — e.g., `security` and `adversarial` should not duplicate the same checks; each should own distinct ground
- X Persona becomes a full review rubric instead of a perspective — if it reads like a checklist, it's doing evaluation work, not providing viewpoint

### Step 4 — Compliance Check

Run [compliance](#phase-2---comply) against the appropriate checklist:
- **Data-flow skills** → [skill_checklist.md](skill_checklist.md)
- **Persona skills** → [persona_checklist.md](persona_checklist.md)

## Phase 2 — Comply

Assert a pass/fail test over an existing skill package against the appropriate checklist.

### Steps

1. **Read Frontmatter**: Extract `metadata.category` from SKILL.md.
   - Must match [taxonomy.md](taxonomy.md). Missing or invalid → Critical failure.
2. **Check Non-Invocable Contracts**: If the skill is a shared contract/interface, verify `disable-model-invocation: true`.
3. **Load Checklist**:
   - Data-flow categories (interface, input, enrich, filter, normalize, output, map) → [skill_checklist.md](skill_checklist.md)
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

1. Must choose the correct checklist based on `metadata.category`: data-flow → skill_checklist, persona → persona_checklist
2. Both checklists inherit shared rules from [base_checklist.md](base_checklist.md)
3. Must read `metadata.category` from frontmatter — never assume
4. Requires explicit user approval before deployment execution

## Outputs

- A complete skill package (create)
- Compliance report with pass/fail for each item (comply)
- Synchronized skill directory at target (deploy)
