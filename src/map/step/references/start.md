# Start a STEP

**Inputs:** a goal and a `STEP-<slug>.yaml` path from context or `STEP_FILE`.

1. Start the workflow. This creates a missing file; for an existing file it returns `changed: false` and preserves its state.
   ```bash
   python scripts/step_cli.py --file STEP-<slug>.yaml start --goal "..." [--lesson "..."]
   ```
2. Read the current state.
   ```bash
   python scripts/step_cli.py --file STEP-<slug>.yaml context
   ```
3. Propose exactly one unique kebab-case step in chat only. Do not execute or persist it. Use the [`asset/proposed_next_template.md`](asset/proposed_next_template.md) packet.
4. Request a gate and wait. On exact `approved`, read [`gate.md`](references/gate.md), then run `approve` with that exact displayed packet before doing any execution. On revision, revise the chat proposal and gate it again. A changed persisted goal must use the CLI: `update goal "..."`.

**Outputs:** unchanged or initialized STEP state, one chat-only proposal, and a requested user gate.

**Next mandatory phase:** After successful `approve`, proceed to [`references/execute.md`](references/execute.md).
