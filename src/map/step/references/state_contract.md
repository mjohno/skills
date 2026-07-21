# STEP State Contract

`step_cli.py` is the authoritative contract and validator for `STEP-<slug>.yaml`. This reference is explanatory only; agents should operate through the CLI.

## Initialized State

```yaml
goal: "<overall goal>"
lessons:
  - "<numbered durable behavior-shaping lesson prose>"
steps: []
```

## Completed Step Shape

```yaml
goal: "<overall goal>"
lessons:
  - "<numbered durable behavior-shaping lesson prose>"
steps:
  - slug: "<kebab-case-step-slug>"
    intent: "<what this step is meant to achieve>"
    criteria:
      - "<observable acceptance criterion>"
    do: {summary: "<what was done>", evidence: ["<provenance>"]}
    validate: {result: "success | partial | failure", evidence: ["<proof>"]}
    retro: {wins: [], issues: [], actions: []}
    next_steps: ["<slug-only>"]
    recommendation: "<slug from next_steps>"
```

Terminal/no-follow-up state:

```yaml
next_steps: []
recommendation: null
```

## Rules

- Persisted state remains `steps`; current state is derived from `steps[-1]`.
- Do not add `current_step`, approval metadata, status fields, task objects, iteration objects, retry state, or sidecar proposal state.
- A step exists in `steps` only after exact user approval of the chat-only proposed step.
- Every step requires criteria.
- `validate.result` is only `success`, `partial`, or `failure`.
- `next_steps` are slug-only choices.
- `recommendation` is either one slug listed in `next_steps` or `null`; object-shaped recommendations are invalid.
- Lessons are ordered durable prose derived from wins, issues, and actions; merge newly learned durable lessons through `approve --lessons`.
