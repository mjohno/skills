# Router Skill Creation Workflow

## Context
Create a new router-based skill following the router pattern from PRD-skill-routing.md.

## Inputs
1. Skill name and description
2. List of workflows the skill should dispatch to
3. Default behavior specification

## Steps

### Phase 1: Planning
1. Determine the skill's capability (one sentence).
2. Identify the workflows this skill will dispatch to.
3. Determine available actions for each workflow.
4. Define default behavior.

### Phase 2: Router Scaffolding
1. Create the skill directory `<name>/`.
2. Create SKILL.md router using `assets/router_skill_template.md`.
   - Set `metadata.type: router` in the frontmatter.
3. Create `references/` and `assets/` directories.

### Phase 3: Workflow File Creation
1. For each workflow, create `references/workflow_<name>.md`.
2. Each workflow must contain: context, steps, patterns, constraints, outputs.
3. Create a `Default Route:` section in the SKILL.md for fallback behavior.
4. Each workflow is self-contained (no cross-skill references).

### Phase 4: Template Creation
1. For each workflow, create `assets/template_<name>.md` if a template is needed.
2. Templates are scoped to the parent skill (not shared).

### Phase 5: Compliance
1. Verify each workflow has context, steps, patterns, constraints, outputs.
2. Verify a `Default Route:` section exists in the SKILL.md.
3. Verify no cross-skill workflow references.
4. Review against `assets/router_checklist.md`.

## Patterns
- **SKILL.md**: only # and ## headings are required for the routing contract; ### and deeper are implementation detail
- **Workflow files**: context → steps → patterns → constraints → outputs
- **Naming**: `references/workflow_<name>.md`, `assets/template_<name>.md`
- **Default**: `Default Route:` for fallback behavior

## Outputs
- A complete router-based skill package with SKILL.md, workflow files, and templates
