# AGENTS

This directory is a managed ecosystem of skills. Use the operations below to manage the full skill lifecycle.

## Structure

- `src/`: Source code for all skills.
- `docs/`: Specifications, templates, checklists, and process guides.

## Operations

Use the pattern **"Run [operation] on [skill]"**.

| Operation | What it does | Trigger | Exit Criteria |
|-----------|-------------|---------|---------------|
| `create` | Scaffolds a new skill using the template and taxonomy | New capability or gap identified | Skill directory exists with valid SKILL.md |
| `comply` | Checks a skill against the checklist in `docs/checklist.md` | Before deploy, or after edits | All CRITICAL items pass |
| `deploy` | Syncs a skill to a target directory (with compliance gate) | After compliance passes | Files verified at target |
| `review` | Audits quality — delegates to the external review skill | When you need an outside perspective | Review report received |

## What Makes a Skill Beautiful

A beautifully simple skill has these properties:

1. **Single responsibility** — one clear goal, with explicit non-goals
2. **Human-aligned design** — maps directly to an intuitive user mental model
3. **Clear scope** — fewest non-overlapping options needed; no redundancy
4. **Minimal default output** — essentials only; detail is opt-in
5. **Graceful handoff** — suggests concrete next skills when it can't solve something
6. **Structure matches purpose** — flows logically and reads like a contract

See [checklist.md](docs/checklist.md) for evaluation criteria.

## Usage Examples

| Scenario | Command |
|----------|---------|
| Scaffolding | "Create a new skill called `amazing`" |
| Checking compliance | "Check the `grill-me` skill for compliance" |
| Deploying | "Deploy `investigate` to `C:/Users/matjo/.pi/agent/skills/`" |
| Reviewing | "/skill:review review the `investigate` skill" |

For category selection, consult [taxonomy.md](docs/taxonomy.md).
