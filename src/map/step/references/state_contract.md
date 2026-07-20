# STEP State Contract

Use exactly one YAML file named `STEP-<slug>.yaml` as step-loop state.

## Initialized State

Before the first approval, a valid file contains only the loop context and an empty step list:

```yaml
goal: "<overall goal>"
lessons:
  - "<numbered durable behavior-shaping lesson prose>"
steps: []
```

`lessons` is an ordered/numbered top-level prose list. Refer to lessons by their 1-based list position when useful.

## Step Packet

After the user explicitly types exactly `approved`, the approved chat-only proposed step is appended to `steps`:

```yaml
goal: "<overall goal>"
lessons:
  - "<numbered durable behavior-shaping lesson prose>"
steps:
  - slug: "<kebab-case-step-slug>"
    intent: "<what this step is meant to achieve>"
    criteria:
      - "<numbered observable acceptance criterion>"
    do: {summary: "<what was done>", evidence: ["<provenance>"]}
    validate: {result: "success | partial | failure", evidence: ["<proof>"]}
    retro: {wins: [], issues: [], actions: []}
    next_steps: ["<slug-only>"]
    recommendation: {next: "<slug from next_steps>", rationale: "<why>"}
```

For terminal/no-follow-up states, use:

```yaml
next_steps: []
recommendation: null
```

## Rules

- Persisted state remains `steps`; current state is derived from `steps[-1]`.
- `current_step` is a derived CLI continuation view: `steps[-1]` or `null` when no step has been approved/appended.
- Do not add `current_step`, approval metadata, status fields, task objects, iteration objects, retry state, or sidecar proposal state to YAML.
- A step exists in `steps` only after exact user approval of the chat-only proposed step.
- Every step requires `criteria`, including implementation, investigation, recovery, and operational steps.
- `criteria` is an ordered/numbered list of observable acceptance conditions; validation checks the current step against these criteria.
- Criteria are approved targets. Do not change them silently. If the user explicitly changes criteria, rerun the current step as needed and record the history in existing fields.
- `validate.result` is only `success`, `partial`, or `failure`.
- `next_steps` are slug-only candidates; elaborate only the chat-only proposed next step before approval.
- `recommendation` is either `{next, rationale}` or `null`; when present, `recommendation.next` must be listed in `next_steps`.
- Lessons are ordered/numbered durable prose derived from wins, issues, and actions. They may be added at any point during the current step.
- Retries and reruns belong in `do.evidence`, `validate.evidence`, `retro.issues`, and/or `retro.actions`.
