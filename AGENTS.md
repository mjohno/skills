# AGENTS

This directory is a managed ecosystem of skills. Use the operations defined below to manage your skill development lifecycle.

## Structure

- `src/`: Contains the source code for all skills.
- `docs/`: Contains documentation, specifications, templates and checklists for skills management.
- `docs/taxonomy.md`: Canonical definitions for skill categories and usage roles.

## Operations

- `create`: Scaffolds a new skill. See [process_classic_skill.md](docs/process_classic_skill.md) and [taxonomy.md](docs/taxonomy.md). Shared contract/interface skills must follow [non_invocable_skills.md](docs/non_invocable_skills.md).
- `comply`: Runs compliance checks. See [process_comply.md](docs/process_comply.md), [taxonomy.md](docs/taxonomy.md), and [non_invocable_skills.md](docs/non_invocable_skills.md). Shared contract/interface skills are also checked against [non_invocable_skills.md](docs/non_invocable_skills.md).
- `deploy`: Synchronizes a skill to a target directory. See [process_deploy.md](docs/process_deploy.md).
- `review`: Audits a skill for quality against the specs in `docs/*`. (Delegates to the `review` skill for implementation.)

## Usage Patterns

To perform an operation on a specific skill, use the pattern: **"Run [operation] on [skill]"**.

### Examples

**Scaffolding a new skill:**
> "Create a new skill called `amazing`"

**Checking compliance:**
> "Check the `grill-me` skill for compliance"

**Deploying a skill:**
> "`deploy` the `investigate` skill to `C:/Users/matjo/.pi/agent/skills/`"

**Reviewing a skill:**
> "/skill:review review the `investigate` skill against the docs/* as a specification"

For taxonomy-aware work, consult `docs/taxonomy.md` first.
