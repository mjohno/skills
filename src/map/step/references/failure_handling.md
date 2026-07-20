# Failure Handling

When a step fails, keep recovery inside the current `step` loop and the same `STEP-<slug>.yaml` state file.

- **Simple failures** — Retry or correct within the current step; record evidence in `do.evidence`, validation result in `validate`, and retry notes in `retro.issues` / `retro.actions`.
- **Unclear failures** — Add a shallow investigation-style next-step slug such as `inspect-failure` or `reproduce-failure`; do not append or execute it until the user approves the chat-only proposed step with exact `approved`.
- **Blocked failures** — Record the blocker in `retro.issues`, add a concrete recovery or decision slug to `next_steps`, and set `recommendation.next` to the best next slug when one exists.
- **Append/execution split** — If exact approval is received and append succeeds but execution then fails unexpectedly, record the attempt in current `do` / `validate` / `retro` as best as possible before the next approval gate.
- **Approval after failure** — The approval gate still occurs when `validate.result` is `failure`. The proposed next step may be recovery, investigation, redirect, or absent.
- **Durable lessons** — If the failure reveals reusable guidance, append or update a top-level numbered prose lesson.

`validate.result` remains only `success`, `partial`, or `failure`; do not add `skipped`.

Do not create retry state, task objects, status fields, approval metadata, sidecar proposals, or external routing instructions.
