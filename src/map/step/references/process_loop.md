# Step Loop Process

Follow this loop after the initial user invocation:

1. **Resume or seed** — Read `show continuation` or create the file with `goal`, `lessons`, and the first step.
2. **Do** — Execute the selected/latest step using appropriate local tools or bounded delegation.
3. **Validate** — Check success with evidence; if validation fails, retry or recover within the same step when useful.
4. **Retro** — Record wins, issues, retries, user corrections, and actions; promote durable guidance to `lessons` when needed.
5. **Summarize and review** — Report progress, evidence, validation result, retro, and lessons; stop for user review or feedback.
6. **Expand and recommend** — Add shallow slug-only `next_steps`, sort/prioritize them, and set `recommendation.next` with rationale.
7. **Decide and save** — User chooses or inserts the next step; append only `slug` and `intent`, then loop from Do.

Human review gate:
- Do not silently continue past the report/recommendation point unless the user has already supplied the next selected step.
- The user may redirect, insert an operational step such as commit/cleanup, choose a different next step, or stop.

Lesson capture:
- Treat phrases like `lesson:`, `learn lesson`, and equivalent explicit feedback as instructions to update top-level `lessons`.
- Add inferred lessons only when they are durable enough to guide future continuation.
