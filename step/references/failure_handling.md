# Failure Handling

When a step fails, assess whether the failure is straightforward or requires deeper investigation before a meaningful next step can be proposed:

- **Simple failures** — Suggest direct recovery (retry, fix a typo, check config) and report the next step.
- **Complex failures** — Delegate to one of these sub-skills to gather facts or restructure before proposing the next step:
  - **`step: investigate`** — Use when you need to gather facts, understand root cause, or explore unknowns. Returns evidence to inform what to do next.
  - **`step: plan`** — Use when the plan needs updating — steps are blocked, the approach is wrong, or new branches are needed.
  - **`step: task`** — Use when individual tasks need refinement, splitting, or reordering based on new information.

Incorporate the sub-skill's output into your report and propose the next step with that new context.
