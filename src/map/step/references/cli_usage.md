# Step CLI Usage

Preferred helper:

```bash
python src/map/step/scripts/step_cli.py --file STEP-<slug>.yaml <protocol-command>
```

Without `--file`, the helper reads `STEP_FILE`.

## Primary Protocol Commands

- `start --goal ... [--lesson ...]` — create a STEP file with no approved steps.
- `context` — show resumable state before proposing or approving.
- `approve --slug ... --intent ... --criteria ... [--lessons ...]` — merge durable lessons and persist the exactly-approved chat proposal before execution.
- `record --do ... --validate ... --retro ... --next-steps ... --recommendation ...` — record current-step results and next choices.
- `gate` — lint current state and show approval-gate context.
- `lint basic|complete [--all] [--fix]` — validate resumable shape or completed current-step quality.

Run `step_cli.py --help` for workflow guidance. Legacy `init`, `show`, `append`, `update`, and `patch` commands are escape hatches.

See `../SKILL.md` Example 1 for the golden path.
