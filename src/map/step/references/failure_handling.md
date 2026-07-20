# Failure Handling

When a step fails, keep recovery inside the current `step` loop and the same `STEP-<slug>.yaml` state file.

- **Simple failures** — Retry or correct within the current step; record evidence in `do.evidence`, validation result in `validate`, and any retry notes in `retro.issues` / `retro.actions`.
- **Unclear failures** — Add a shallow investigation-style next-step slug such as `inspect-failure` or `reproduce-failure`; do not route to another skill from this reference.
- **Blocked failures** — Record the blocker in `retro.issues`, add a concrete recovery or decision step to `next_steps`, and set `recommendation.next` to the best next slug.
- **Durable lessons** — If the failure reveals reusable guidance, append a concise top-level lesson.

Do not create retry state, task objects, status fields, or external routing instructions.
