---
name: step
description: Use when you need a persistent, human-reviewed loop over next-best local steps toward a goal, backed by one STEP-<slug>.yaml file.
metadata:
  type: skill
  category: map
---

# step

Goal: Run a user-invoked, YAML-backed step loop that advances one goal through bounded step packets, validation, retro learning, recommendation, user decision, and saved continuation state.
Non-Goals: Do not manage task state, replace `coordinate`, create full plans/specs/tasks, run broad orchestration, continue without human review, or require model-level reinvocation each loop.
Use-When: You have a goal plus an initial or selected next step, and want repeated local progress recorded in `STEP-<slug>.yaml`.

## 0. Prerequisites

- A goal and either a new step seed or an existing `STEP-<slug>.yaml`.
- Use exactly one step file as state; do not create task, iteration, status, or `current_step` state.
- Must use `src/map/step/scripts/step_cli.py` when available; otherwise edit YAML directly with the same contract.
- Read `references/state_contract.md` before creating or changing step state.

## 1. Inputs

- Goal, selected step, or step file path.
- References for the selected step: plans, specs, review findings, files, docs, or user feedback.
- Optional explicit lessons from phrases like `lesson:` or `learn lesson`.
- Optional user decision to continue, redirect, insert an operational step, or stop.

## 2. Processes

Use these references as needed:
- `references/state_contract.md` — required YAML state shape and state-churn constraints.
- `references/process_loop.md` — required loop actions: do, validate, retro, summarize/review, expand/recommend, decide/save.
- `references/cli_usage.md` — helper command surface for safe state updates.
- `references/failure_handling.md` — recovery rules when validation fails or work blocks.

Default loop:
1. Resume or seed the single `STEP-<slug>.yaml` file.
2. Execute the selected/latest step and record `do` evidence.
3. Validate with evidence; keep retries/recovery inside the same step.
4. Record retro wins/issues/actions and concise durable lessons.
5. Report progress, next-step candidates, and recommendation; stop for user review/decision unless the user already selected the next step.

## 3. Outputs

- Updated `STEP-<slug>.yaml` only.
- Brief report: goal, step slug, result, evidence, retro issues/actions, lessons added, next-step slugs, recommendation, and decision needed.
- Stop prompt for user review/decision unless the user already supplied the next selected step.

## 4. Next Steps

- `check` — separate validation against criteria.
- `review` — structured critique of the result or step file.
- `investigate` — unknown failure root cause.
- `git-commit` — user-inserted commit step.

## 5. Examples

- Start: `/skill:step Goal: Refactor step. First step: define-step-schema.` creates `STEP-refactor-step.yaml`.
- Continue: `Continue STEP-refactor-step.yaml.` reads continuation context, executes/validates the last step, records retro, recommends next slugs, and asks the user to decide.
