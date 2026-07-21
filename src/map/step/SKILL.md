---
name: step
description: Use when you need a persistent, human-reviewed protocol over next-best local steps toward a goal, backed by one STEP-<slug>.yaml file.
disable_model_invocation: true
metadata:
  type: protocol
  category: map
---

# step

Goal: Govern one approval-gated local progress loop where exact user approval promotes a chat-only proposed step into CLI-managed STEP state before execution.
Non-Goals: Do not manage broad task state, replace `coordinate`, create full plans/specs/tasks, continue without exact approval, hand-edit STEP YAML, or persist unapproved proposals.
Use-When: You have a goal and want repeated local progress recorded in one `STEP-<slug>.yaml`, with explicit user approval at each step boundary.

## 0. Prerequisites

- A goal and either a new proposed step or an existing `STEP-<slug>.yaml`.
- Use exactly one step file as protocol state.
- Use `scripts/step_cli.py` as the authoritative protocol interface and state authority.

## 1. Protocol Interface

Primary commands:

```bash
# Relative to this SKILL.md file
python scripts/step_cli.py --file STEP-<slug>.yaml start --goal "..."
python scripts/step_cli.py --file STEP-<slug>.yaml context
python scripts/step_cli.py --file STEP-<slug>.yaml approve --slug ... --intent ... --criteria ... [--lessons ...]
python scripts/step_cli.py --file STEP-<slug>.yaml record --do ... --validate ... --retro ... --next-steps ... --recommendation ...
python scripts/step_cli.py --file STEP-<slug>.yaml gate
python scripts/step_cli.py --file STEP-<slug>.yaml lint complete
```

Run `python scripts/step_cli.py --help` for the protocol workflow. Legacy low-level CLI commands are escape hatches; prefer the primary commands.

## 2. Invariants

- The exact approval token is the whole user message `approved`.
- After exact approval, the first state-changing action is `step_cli.py approve`; do not execute before it succeeds.
- `approve` must preserve the exact approved slug and requires a complete current step when one exists.
- Mutate STEP state only through the CLI; never hand-edit STEP YAML.
- Pending proposed next steps are chat-only until exact approval.
- If a pending proposal is unavailable, rebuild it from context and the STEP file, then request approval again.
- Merge durable top-level lessons through `approve --lessons`; keep step-local observations in `retro`.
- Persist slug-only `next_steps` and `recommendation: <slug|null>`; recommendation rationale belongs in chat only.

## 3. Outputs

- Updated `STEP-<slug>.yaml` only through the CLI.
- At approval gates, output CLI `gate` YAML directly.
- When a next step is proposed, output a separate chat-only YAML block:

```yaml
proposed:
  slug: "<slug>"
  intent: "<intent>"
  criteria:
    - "<criterion>"
```

## 4. Next Steps

- `check` — separate validation against criteria.
- `review` — structured critique of the result or protocol state.
- `investigate` — unknown failure root cause.
- `git-commit` — user-inserted commit step.

## 5. Examples

### Example 1

**Prompt:** `/skill:step Goal: Refactor step. Proposed first step: define CLI protocol commands.`
**Outcome:** The agent starts or resumes `STEP-refactor-step.yaml`, proposes one chat-only step, waits for exact `approved`, then uses the CLI to approve, record, gate, and stop again.

```bash
python scripts/step_cli.py --file STEP-refactor-step.yaml start --goal "Refactor step"
python scripts/step_cli.py --file STEP-refactor-step.yaml context

# after the user approves the proposed `define-cli-protocol-commands` step with exactly `approved`:
python scripts/step_cli.py --file STEP-refactor-step.yaml approve --slug define-cli-protocol-commands --intent "Define CLI protocol commands for step" --criteria "CLI exposes start, context, approve, record, gate, and lint commands" --lessons '[Keep protocol operations explicit]'

python scripts/step_cli.py --file STEP-refactor-step.yaml record \
  --do '{summary: "Defined the step CLI protocol command surface", evidence: ["scripts/step_cli.py"]}' \
  --validate '{result: success, evidence: ["python scripts/step_cli.py --help shows the protocol workflow"]}' \
  --retro '{wins: ["Protocol command names match the step goal"], issues: [], actions: []}' \
  --next-steps '[simplify-step-docs]' \
  --recommendation simplify-step-docs

python scripts/step_cli.py --file STEP-refactor-step.yaml gate
```

Terminal state uses `--next-steps '[]' --recommendation null` when no further refactor step is needed.
