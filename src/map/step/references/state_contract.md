# STEP State Contract

Use exactly one YAML file named `STEP-<slug>.yaml` as step-loop state.

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
- Current state is the last item in `steps`.
- Do not add `current_step`, status fields, task objects, iteration objects, or retry state.
- `next_steps` are slug-only candidates; elaborate only the selected next step when appending it.
- `recommendation` is a field on the step packet, not a separate step or type.
- `lessons` are top-level durable memory for continuation; keep them concise, reusable, and behavior-shaping.
- Retries belong in `do.evidence`, `retro.issues`, and/or `retro.actions`.
