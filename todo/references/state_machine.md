# State Machine

Use this as the canonical TODO list lifecycle.

## Checklist
- [ ] TODO: implementer picks it up.
- [.] DOIN: verifier picks it up.
- [x] DONE: ready for review.

## Transitions
- `TODO -> DOIN` in `mode:implementer`.
- `DOIN -> [x]` in `mode:verifier` when verified.
- `DOIN -> [ ]` in `mode:verifier` when not verified.
- `[x] -> cleanup` after explicit `TODO_SIGNOFF: <NAME>`.
- `cleanup` removes `[x]` items and any completed inline TODO comments.

## Notes
- Keep the TODO list and inline TODO comments in sync.
- Commentor creates and repairs the inline comment instances.
- Implementer executes the work.
- Verifier checks the work.
- Unfinished work stays visible.
