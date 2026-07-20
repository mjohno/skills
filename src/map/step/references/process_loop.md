# Step Loop Process

The `step` skill is an explicit approval-gated loop. The step boundary is the user's exact sign-off message:

```text
approved
```

Any additional text is a revision request, not approval.

## Canonical Loop

1. **Resume or init context** — Read `show continuation`, or create the file with `goal`, ordered/numbered `lessons`, and `steps: []`.
2. **Propose next step in chat** — When there is no approved executable step pending, present a chat-only `proposed_next_step` with `slug`, `intent`, and ordered/numbered `criteria`.
3. **Wait for exact approval** — Do not append or execute unless the user's whole message is exactly `approved`.
4. **Append approved step** — Use the normal `append step` command. If append fails, do not execute; report the error, revise the chat-only proposal, and require approval again.
5. **Execute one current step** — The appended step is now the current step. Execute exactly that one step.
6. **Record work** — Update current `do`, `validate`, `retro`, ordered/numbered lessons when useful, slug-only `next_steps`, and `recommendation` or `null`.
7. **Lint persisted state** — Run complete lint for the current step. Use deterministic fixes only when safe.
8. **Show approval gate** — Output CLI `show continuation` YAML for persisted state, followed by a separate YAML block for chat-only `proposed_next_step` when a next step exists.
9. **Wait again** — The user may type exact `approved`, revise the proposal, revise lessons/criteria, request more work on the current step, stop, or sign off final state when no next step exists.

## Approval Gate Output

Default persisted view:

```bash
python scripts/step_cli.py --file STEP-<slug>.yaml show continuation
```

Then show the chat-only proposal separately when there is a next step:

```yaml
proposed_next_step:
  slug: "<slug>"
  intent: "<intent>"
  criteria:
    - "<criterion>"
```

The proposed next step is never persisted before approval. If chat context no longer contains the proposal, `approved` is invalid; regenerate and show the proposal for review again.

## CLI Gate Check

Before showing any approval gate, verify you called `show continuation` immediately before this step. If there's a gap between when state changed and when you showed it, re-run `show continuation`. Never show stale YAML.

## Human Review Gate

At the gate, the user may:

- type exactly `approved` to approve the displayed packet;
- revise the proposed slug, intent, or criteria;
- add or update lessons;
- revise current criteria and rerun the current step;
- request more validation or recovery inside the current step;
- stop.

When there is no proposed next step, exact `approved` signs off the completed current step only. No append or execution happens, and approval is not persisted.

## Lesson Capture

- Treat phrases like `lesson:`, `learn lesson`, and equivalent explicit feedback as instructions to update top-level `lessons`.
- Lessons are ordered/numbered prose derived from wins, issues, and actions.
- Add lessons whenever they become useful; the usual point is review before continuation.
- Keep ordinary attempt details in `retro`; promote only durable guidance to top-level `lessons`.

## Criteria Revisions and Reruns

Criteria are approved targets. If the user explicitly changes criteria after execution has started, update current criteria and rerun the current step as needed. Keep attempt history in the same packet: `do.evidence`, `validate.evidence`, `retro.issues`, and `retro.actions`. Do not create retry/rerun state.
