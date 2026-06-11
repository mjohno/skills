# Comment Format

Comments should be natural collaboration notes first and structured artifacts only when useful.

## Lightweight comment

Use when no later reference is expected.

```text
COMMENT: This acceptance criterion does not define expired-session behavior.
```

## Referencable comment

Use when the note may be discussed, resolved, converted into a task, or linked from a plan.

```text
<KIND>(<ID>): <message>
```

Use the purpose tag that best describes who should act on the note:

- `COMMENT` — general feedback, clarification, or discussion.
- `TODO` — implementer-facing work.
- `CHECK` — verifier-facing behavior, test, or condition to check.
- `REVIEW` — reviewer-facing design, code, or prose review note.
- `DONE` — completion claim or implementation note for reviewer/verifier analysis.

The ID is the stable traceable anchor. The kind may change if the note's purpose changes, but the ID should remain stable.

Examples:

```text
COMMENT(AUTH-EXPIRY-1): AC-3 does not define expired-session behavior.
TODO(AUTH-EXPIRY-2): Implement redirect-to-login for expired sessions.
CHECK(AUTH-EXPIRY-3): Verify expired API sessions return 401, not redirect.
DONE(AUTH-EXPIRY-4): Implementation claims RFC-AUTH#D2 is satisfied.
```

## Optional detail lines

Use native comment syntax for every line.

```ts
// COMMENT(AUTH-EXPIRY-1): AC-3 does not define expired-session behavior.
// Source: PRD-AUTH#AC-3
// Suggestion: Define redirect vs 401 behavior.
```

## Status words

If a status is needed, keep it simple:

- `open`
- `resolved`
- `wontfix`

Prefer changing the purpose tag over adding workflow-heavy status fields. Comments are annotations and context anchors, not execution records.
