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
COMMENT(<ID>): <message>
```

Example:

```text
COMMENT(AUTH-EXPIRY-1): AC-3 does not define expired-session behavior.
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

Do not use comment status as an implementation workflow. Comments are annotations, not execution records.
