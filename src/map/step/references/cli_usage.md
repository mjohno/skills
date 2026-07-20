# Step CLI Usage

Preferred helper:

```bash
python src/map/step/scripts/step_cli.py --file STEP-<slug>.yaml <operation> <resource>
```

Without `--file`, the helper reads `STEP_FILE`.

## Common Commands

- `show continuation` — preferred resume and approval-gate path; returns `goal`, `lessons`, and derived `current_step` (`null` when no step exists).
- `show all` — use only when full history is needed.
- `init --goal ... [--lesson ...]` — create a new step file with `goal`, lessons, and `steps: []`; does not create the first step.
- `append step --slug ... --intent ... --criteria ...` — append an approved step. `--criteria` may repeat and may also contain a YAML list.
- `append lessons <value>` — add an explicit or inferred durable lesson.
- `update lessons <yaml-list>` — replace lessons with a normalized YAML list.
- `update current --criteria ...` — replace current step criteria after explicit user revision.
- `update current --do|--validate|--next-steps|--recommendation <yaml-or->` — replace explicit current-step fields.
- `append current --retro|--next-steps <yaml-or-value>` — merge retro fields or next-step slugs.
- `lint basic` — check resumable shape; allows empty `steps`.
- `lint complete [--all] [--fix]` — check completed-step quality; requires a current step; `--fix` only applies deterministic safe fixes.
- `patch lessons` and `patch current` — escape hatches; prefer explicit commands.

Legacy `last` command resources are not supported; use `current`.

CLI contract:
- Structured values are YAML strings; `-` reads YAML from stdin.
- Machine-readable results go to stdout.
- Warnings and diagnostics go to stderr.
- Use `lint` for schema/shape checks; do not confuse it with the loop's validation phase.
- Use CLI YAML output directly at the approval gate; do not invent a separate report format.

## Example Golden Path

```bash
# Initialize context:
python src/map/step/scripts/step_cli.py --file STEP-work.yaml init --goal "Improve step consistency" --lesson "Keep proposed steps chat-only until approval."

# Show approval-gate context:
python src/map/step/scripts/step_cli.py --file STEP-work.yaml show continuation

# After the user types exactly `approved`, append the approved step:
python src/map/step/scripts/step_cli.py --file STEP-work.yaml append step --slug update-contract --intent "Update the state contract" --criteria "State allows empty steps at init" --criteria "Every appended step includes criteria"

# Record execution and validation:
python src/map/step/scripts/step_cli.py --file STEP-work.yaml update current --do '{summary: "Updated contract", evidence: ["src/map/step/references/state_contract.md"]}'
python src/map/step/scripts/step_cli.py --file STEP-work.yaml update current --validate '{result: success, evidence: ["lint complete passed"]}'
python src/map/step/scripts/step_cli.py --file STEP-work.yaml append current --retro '{wins: ["Contract is explicit"], issues: [], actions: []}'

# Record next-step candidates and recommendation:
python src/map/step/scripts/step_cli.py --file STEP-work.yaml update current --next-steps '[update-cli, update-docs]'
python src/map/step/scripts/step_cli.py --file STEP-work.yaml update current --recommendation '{next: update-cli, rationale: "CLI must support the contract."}'

# Terminal/no-next-step state:
python src/map/step/scripts/step_cli.py --file STEP-work.yaml update current --next-steps '[]'
python src/map/step/scripts/step_cli.py --file STEP-work.yaml update current --recommendation 'null'

# Lint and show review context:
python src/map/step/scripts/step_cli.py --file STEP-work.yaml lint complete
python src/map/step/scripts/step_cli.py --file STEP-work.yaml show continuation
```
