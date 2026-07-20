# Step CLI Usage

Preferred helper:

```bash
python src/map/step/scripts/step_cli.py --file STEP-<slug>.yaml <operation> <resource>
```

Without `--file`, the helper reads `STEP_FILE`.

Common commands:
- `show continuation` — preferred resume path; returns only `goal`, `lessons`, and `last_step`.
- `show all` — use only when full history is needed.
- `init --goal ... --slug ... --intent ... [--lesson ...]` — create a new step file.
- `append step --slug ... --intent ...` — append the selected next step.
- `append lessons <value>` — add an explicit or inferred durable lesson.
- `update lessons <yaml-list>` — replace lessons with a normalized YAML list.
- `update last --do|--validate|--next-steps|--recommendation <yaml-or->` — replace explicit last-step fields.
- `append last --retro|--next-steps <yaml-or-value>` — merge retro fields or next-step slugs.
- `lint basic` — check resumability shape.
- `lint complete [--all] [--fix]` — check completed-step quality; `--fix` only applies deterministic safe fixes.
- `patch lessons` and `patch last` — escape hatches; prefer explicit commands.

CLI contract:
- Structured values are YAML strings; `-` reads YAML from stdin.
- Machine-readable results go to stdout.
- Warnings and diagnostics go to stderr.
- Use `lint` for schema/shape checks; do not confuse it with the loop's validation phase.
