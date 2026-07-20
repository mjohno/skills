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

## 1. Inputs

- Goal, selected step, or step file path.
- References for the selected step: plans, specs, review findings, files, docs, or user feedback.
- Optional explicit lessons from phrases like `lesson:` or `learn lesson`.
- Optional user decision to continue, redirect, insert an operational step, or stop.

## 2. STEP YAML Contract

State file: `STEP-<slug>.yaml`.

```yaml
goal: "<overall goal>"
lessons:
  - "<durable behavior-shaping lesson>"
steps:
  - slug: "<kebab-case-step-slug>"
    intent: "<what this step is meant to achieve>"
    do: {summary: "<what was done>", evidence: ["<provenance>"]}
    validate: {result: "success | partial | failure", evidence: ["<proof>"]}
    retro: {wins: [], issues: [], actions: []}
    next_steps: ["<slug-only>"]
    recommendation: {next: "<slug from next_steps>", rationale: "<why>"}
```

Rules:
- Current state is the last item in `steps`; never add `current_step`, status fields, task objects, or iteration objects.
- `next_steps` are slug-only candidates; elaborate only the selected next step when appending it.
- `recommendation` is a field on the step packet, not a separate step or type.
- `lessons` are top-level durable memory for continuation; keep them concise and reusable.

## 3. Processes

1. **Resume or seed**: Read `show continuation` or create the file with goal, lessons, and first step.
2. **Do**: Execute the selected/latest step using appropriate local tools or bounded delegation.
3. **Validate**: Check success with evidence; if validation fails, retry/recover within the same step when useful.
4. **Retro**: Record wins, issues, retries, user corrections, and actions; promote durable guidance to `lessons` when needed.
5. **Summarize and review**: Report progress, evidence, validation result, retro, and lessons; stop for user review or feedback.
6. **Expand and recommend**: Add shallow slug-only `next_steps`, sort/prioritize them, and set `recommendation.next` with rationale.
7. **Decide and save**: User chooses or inserts the next step; append only `slug` and `intent`, then loop from Do.

## 4. CLI Usage

Preferred helper: `python src/map/step/scripts/step_cli.py --file STEP-<slug>.yaml <operation> <resource>`; without `--file`, it uses `STEP_FILE`.

- `show continuation` preferred; `show all` only when full history is needed.
- `init --goal ... --slug ... --intent ... [--lesson ...]` creates a new file.
- `append step --slug ... --intent ...` appends the selected next step.
- `append lessons <value>` saves an explicit or inferred durable lesson.
- `update last --do|--validate|--next-steps|--recommendation <yaml-or->` replaces explicit last-step fields.
- `append last --retro|--next-steps <yaml-or-value>` merges retro fields or next-step slugs.
- `lint basic` / `lint complete [--all] [--fix]` checks resumability or completed-step quality.
- `patch lessons` and `patch last` are escape hatches; prefer explicit commands.

## 5. Outputs

- Updated `STEP-<slug>.yaml` only.
- Brief report: goal, step slug, result, evidence, retro issues/actions, lessons added, next-step slugs, recommendation, and decision needed.
- Stop prompt for user review/decision unless the user already supplied the next selected step.

## 6. Next Steps

- `check` — separate validation against criteria.
- `review` — structured critique of the result or step file.
- `investigate` — unknown failure root cause.
- `git-commit` — user-inserted commit step.

## 7. Examples

- Start: `/skill:step Goal: Refactor step. First step: define-step-schema.` creates `STEP-refactor-step.yaml`.
- Continue: `Continue STEP-refactor-step.yaml.` reads continuation context, executes/validates the last step, records retro, recommends next slugs, and asks the user to decide.
