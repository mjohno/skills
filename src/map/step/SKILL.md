---
name: step
description: Use when you need a persistent, human-reviewed protocol over local next-best steps towards a goal, backed by one STEP-<slug>.yaml file.
disable_model_invocation: true
metadata:
  type: protocol
  category: map
---

# step

Goal: Orchestrate the local next best step protocol using the `scripts/step_cli.py` to; Start a STEP protocol, execute a STEP, propose the next STEPs and gate for user approval.
Non-Goals: Manually modifications of the STEP state file. Bypassing the CLI
Use-When: You have a goal and want repeated local progress recorded, with explicit user approval at each step boundary.

## 1. Protocol

Overview:
- Start: is the first process which prepares the execute-gate loop
- Execute: is the main process you do all your work.
- Gate: is the review process where the user does their approval.

You follow this protocol (mandatory CLI commands are omitted):
```yaml
start:  # The start process
  - initialize: You initialize the STEP-<slug>.yaml file with the goal.
  - propose: You propose the next step in chat only, with a unique slug, intent, and observable criteria.
  - gate:  # The gate process.
    - approved: You await the user's exact `approved` message. goto `loop`.
    - revise: The goal, lessons, or next step proposal require revision. goto `propose`.
loop:
  - execute:  # The execute process
    - do: You make the changes to meet the intent and criteria.
    - validate: You validate the changes against the intent and criteria; and progress towards the goal.
    - retro: You do a retrospective to identify lessons to learn to improve the approach for future steps.
    - record: You record the do and validate evidence and retro results.
    - propose_next: You propose what the next step should be based on the results, intent and goal.
  - gate:  # The gate process
    - approved: execution and next step are `approved` by the user
    - revise: execution requires revision or next step is not `approved` by the user
    - break: The user `break`s the loop. There are no more next steps, the user has `approved` the final step. The protocol is complete.
  - goto: `loop`
```

## 2. Processes

### 2.1. Start a STEP

Inputs:
1. A goal from context.
2. A name for the `STEP-<slug>.yaml` file from context or `STEP_FILE` environment variable.

Process:
1. Create the file with a goal: `python scripts/step_cli.py --file STEP-<slug>.yaml start --goal "..."`
2. Show the current context: `python scripts/step_cli.py --file STEP-<slug>.yaml context`
3. From context, propose exactly one next step in chat only:

```yaml
proposed:
  slug: "<slug>"
  intent: "<intent>"
  criteria:
    - "<criterion>"
```

4. Await for the user gate. Requires explicit and exact `approved` response. Any other response is a revision, not approval.

Outputs:
1. An initialized `STEP-<slug>.yaml` file on disk
2. The proposed next step in chat.
3. A requested user gate for approval.

### 2.2. Execute a STEP

Inputs:
1. The context from `python scripts/step_cli.py --file STEP-<slug>.yaml context`.

Process:
1. Understand the goal, lessons, intent and criteria from the context.
2. Do the work to meet the intent and criteria, driving towards the goal, following the lessons.
3. Record the work done with `python scripts/step_cli.py --file STEP-<slug>.yaml record --do '{summary: "<work done>", evidence: ["<evidence>"]}'`
4. Validate the work meets the intent and criteria.
5. Record the validation results with `python scripts/step_cli.py --file STEP-<slug>.yaml record --validate '{result: "success|partial|failure", evidence: ["<proof>"]}'`
6. Retrospect on the work done, identifying lessons which could improve execution towards the goal.
7. Record the retrospective results with `python scripts/step_cli.py --file STEP-<slug>.yaml record --retro '{wins: [], issues: [], actions: []}'`
8. Display the results in chat `python scripts/step_cli.py --file STEP-<slug>.yaml context`.
9. Propose the next steps with `python scripts/step_cli.py --file STEP-<slug>.yaml record --next-steps '[<next-slug>]' --recommendation <next-slug-or-null>`.
10. Await for the user gate. Requires explicit and exact `approved` response. Any other response is a revision, not approval.

Batch Recording Example:
```bash
python scripts/step_cli.py --file STEP-<slug>.yaml record \
  --do '{summary: "<work done>", evidence: ["<evidence>"]}' \
  --validate '{result: "success|partial|failure", evidence: ["<proof>"]}' \
  --retro '{wins: [], issues: [], actions: []}' \
  --next-steps '[<next-slug>]' \
  --recommendation <next-slug-or-null>
```

Outputs:
1. The recorded outcome of the step in the STEP-<slug>.yaml file.
2. The outcome of the step in chat.
3. The proposed next step in chat.
4. A requested user gate for approval.

### 2.3. Gate a STEP

Inputs:
1. The requested user gate from `python scripts/step_cli.py --file STEP-<slug>.yaml gate`.

Process:
1. Await for the user gate - either `approved`, `revise`, or `break`.
2. If an exact `approved` response is received, continue to the next step using:

```bash
python scripts/step_cli.py --file STEP-<slug>.yaml approve \
  --slug <exact-approved-slug> \
  --intent "<exact-approved-intent>" \
  --criteria "<exact-approved-criterion>" \
  [--lessons "<durable-lesson>"]
```

3. If an exact `break` response is received, stop the protocol.
4. If any other response is received, treat it as a revision request for the current step and update the step using the batch record command with `python scripts/step_cli.py --file STEP-<slug>.yaml record --do '{summary: "<work done>", evidence: ["<evidence>"]}' --validate '{result: "success|partial|failure", evidence: ["<proof>"]}' --retro '{wins: [], issues: [], actions: []}' --next-steps '[<next-slug>]' --recommendation <next-slug-or-null>`.
5. Loop back to Execute a STEP.

Outputs:
1. If `approved`: `python scripts/step_cli.py --file STEP-<slug>.yaml approve --slug <exact-approved-slug> --intent "<exact-approved-intent>" --criteria "<exact-approved-criterion>" [--lessons "<durable-lesson>"]`
2. If `break`: Final context of the step using `python scripts/step_cli.py --file STEP-<slug>.yaml context` and stop the protocol.
3. If `revise`: Updated context of the step using `python scripts/step_cli.py --file STEP-<slug>.yaml context` and loop back to Execute a STEP.

## 3. Examples

### 3.1. Golden Path
**Prompt:** `/skill:step Goal: Refactor step skill. Lesson: PLAN-refactor-step.md has the plan.`
**Decisions:** Start a new STEP protocol.

```bash
# Start the protocol
python scripts/step_cli.py --file STEP-refactor-step.yaml start --goal "Refactor step skill" --lessons "PLAN-refactor-step.md has the plan."
# Display the context
python scripts/step_cli.py --file STEP-refactor-step.yaml context
```
**Output:** The YAML context from the CLI command, including the goal and any lessons learned and the proposed next step.

**Prompt:** `approved`

**Decisions:**: Execute the STEP.
```bash
# Approve the proposed next step
python scripts/step_cli.py --file STEP-refactor-step.yaml approve --slug define-cli-protocol-commands --intent "Define CLI protocol commands for step" --criteria "CLI exposes start, context, approve, record, gate, and lint commands"

# <Assistant/Agent does the work to meet the intent and criteria and drive towards the goal>

# Record the result of the work done
python scripts/step_cli.py --file STEP-refactor-step.yaml record --do '{summary: "Defined the step CLI protocol command surface", evidence: ["scripts/step_cli.py"]}'

# <Assistant/Agent validates the work against the intent and criteria and goal progress>

# Record the validation results
python scripts/step_cli.py --file STEP-refactor-step.yaml record --validate '{result: success, evidence: ["CLI help shows the protocol workflow"]}'

# <Assistant/Agent retrospects the approach it took to improve execution for futures steps>

# Record the retrospective results
python scripts/step_cli.py --file STEP-refactor-step.yaml record --retro '{wins: ["Protocol command names match the goal"], issues: ["Did not use --test immediately to validate CLI shape"], actions: ["Ensure unittests run by --test catch CLI shape issues"]}'

# Propose the next step based on the results, intent and goal
python scripts/step_cli.py --file STEP-refactor-step.yaml record --next-steps '[simplify-step-docs]' --recommendation simplify-step-docs

# Gate the results and await user approval
python scripts/step_cli.py --file STEP-refactor-step.yaml gate
```
**Output:** The YAML context from the gate CLI command, including the recorded results of the work done, validation, and retrospective, and the proposed next step.

**Prompt:** `approved`
**Decisions:**: Execute the next STEP.
```bash
# Approve the proposed next step
python scripts/step_cli.py --file STEP-refactor-step.yaml approve --slug simplify-step-docs --intent "Simplify the step skill documentation" --criteria "Documentation is clear, concise, and easy to follow"

# loop until `break`.
```
