---
name: step
description: Use when you need a persistent, human-reviewed protocol over local next-best steps toward a goal, backed by one STEP-<slug>.yaml file.
disable_model_invocation: true
metadata:
  type: protocol
  category: map
---

# step

Goal: Orchestrate local next-best-step progress through `scripts/step_cli.py`: start a STEP workflow, promote an approved step, execute it, record its result, and gate the next step for user review.
Non-Goals: Do not modify a STEP state file manually, bypass the CLI, execute an unapproved proposal, or manage broad task state.
Use-When: You have a goal and want repeated local progress recorded with explicit user approval at each step boundary.

## 1. Protocol

The CLI is authoritative for STEP state. Proposals exist in chat only. The required cycle is:

```yaml
start:
  - initialize_or_resume
  - propose
  - gate
  - approved: approve_then_execute
loop:
  - execute
  - record
  - gate
  - approved: approve_then_execute
  - revise: revise_then_gate
  - break: stop_terminal_workflow
```

Only the whole user message `approved` promotes the currently displayed chat proposal. After it, `approve` is the first state-changing action and must succeed before execution. `break` is a terminal instruction only: accept it only after `gate` succeeds and the current step has `next_steps: []` and `recommendation: null`; it changes no state. Any other response is a revision request.

## 2. Processes

### 2.1 Start a STEP

**Inputs:** a goal and a `STEP-<slug>.yaml` path from context or `STEP_FILE`.

1. Start the workflow. This creates a missing file; for an existing file it returns `changed: false` and preserves its state.
   ```bash
   python scripts/step_cli.py --file STEP-<slug>.yaml start --goal "..." [--lesson "..."]
   ```
2. Read the current state.
   ```bash
   python scripts/step_cli.py --file STEP-<slug>.yaml context
   ```
3. Propose exactly one unique kebab-case step in chat only. Do not execute or persist it.
   ```yaml
   proposed:
     slug: "<slug>"
     intent: "<intent>"
     criteria:
       - "<observable criterion>"
   ```
4. Request a gate and wait. On exact `approved`, run `approve` with that exact displayed packet, then continue with **Execute a STEP**. On revision, revise the chat proposal and gate it again. A changed persisted goal must use the CLI: `update goal "..."`.

**Outputs:** unchanged or initialized STEP state, one chat-only proposal, and a requested user gate.

### 2.2 Execute a STEP

**Input:** a step that `approve` has already promoted into current STEP state.

1. Read `context`, understand its goal, lessons, intent, and criteria, then do only that current step's work.
2. Record work evidence, validate the result against the intent and criteria, retrospect, and record next-step choices. These may be separate `record` calls or one batch call:
   ```bash
   python scripts/step_cli.py --file STEP-<slug>.yaml record \
     --do '{summary: "<work done>", evidence: ["<evidence>"]}' \
     --validate '{result: "success|partial|failure", evidence: ["<proof>"]}' \
     --retro '{wins: [], issues: [], actions: []}' \
     --next-steps '[<next-slug>]' \
     --recommendation <next-slug-or-null>
   ```
3. For simple failure, retry within this step and record the attempt. For unclear or blocked failure, record the blocker in `retro`, set `validate.result: failure` or `partial`, and propose one recovery or investigation slug in `next_steps`. Do not create retry, task, status, or sidecar state.
4. Run the approval gate. If it returns errors, correct and re-record the current step; do not propose or promote another step.
   ```bash
   python scripts/step_cli.py --file STEP-<slug>.yaml gate
   ```
5. When `gate` succeeds, output its YAML directly, then separately propose the selected next step in chat only. If no next step remains, record `--next-steps '[]' --recommendation null`, gate, and offer final sign-off.

**Outputs:** recorded current-step outcome, fresh successful gate YAML, and either one chat-only proposal or a terminal state.

### 2.3 Gate a STEP

**Inputs:** fresh successful `gate` YAML and either its separate chat-only proposal or terminal state.

1. Present the gate result and request review.
2. On exact `approved` with a displayed proposal, promote exactly that proposal before doing any work:
   ```bash
   python scripts/step_cli.py --file STEP-<slug>.yaml approve \
     --slug <exact-approved-slug> \
     --intent "<exact-approved-intent>" \
     --criteria "<exact-approved-criterion>" \
     [--lessons "<durable-lesson>"]
   ```
   `approve` may reject duplicate slugs, an incomplete current step, or a slug absent from prior `next_steps`. Report the error, revise the chat-only proposal, and gate again; never execute after a failed approval. On success, return to **Execute a STEP**.
3. On exact `approved` or `break` with terminal state, stop. Neither action writes state.
4. On another response, treat it as a revision. Revise a proposed next step only in chat. For more current-step work, execute and record it, then gate again. For an explicit current-criteria change, use `update current --criteria ...`, rerun as needed, record the attempt, and gate again. Merge durable lessons only through the next successful `approve --lessons`.

## 3. Example: Golden Path

**Prompt:** `/skill:step Goal: Refactor step skill. Lesson: PLAN-refactor-step.md has the plan.`

```bash
python scripts/step_cli.py --file STEP-refactor-step.yaml start \
  --goal "Refactor step skill" \
  --lesson "PLAN-refactor-step.md has the plan."
python scripts/step_cli.py --file STEP-refactor-step.yaml context

# Show a chat-only define-cli-protocol-commands proposal. After exactly `approved`:
python scripts/step_cli.py --file STEP-refactor-step.yaml approve \
  --slug define-cli-protocol-commands \
  --intent "Define CLI protocol commands for step" \
  --criteria "CLI exposes start, context, approve, record, gate, and lint commands"

# Do the approved work, then record and gate it:
python scripts/step_cli.py --file STEP-refactor-step.yaml record \
  --do '{summary: "Defined the step CLI protocol command surface", evidence: ["scripts/step_cli.py"]}' \
  --validate '{result: success, evidence: ["CLI help shows the protocol workflow"]}' \
  --retro '{wins: ["Protocol command names match the goal"], issues: [], actions: []}' \
  --next-steps '[simplify-step-docs]' \
  --recommendation simplify-step-docs
python scripts/step_cli.py --file STEP-refactor-step.yaml gate
```

The agent outputs the gate YAML and separately proposes `simplify-step-docs`; exact `approved` promotes it before its execution.
