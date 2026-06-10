# mode:reviewer

Use this mode after every task in a TODO list has reached `[x]`.

See [State Machine](state_machine.md) for transitions.

## Responsibilities
- Confirm all `[x]` items exist for the TODO list.
- Require explicit sign-off: `TODO_SIGNOFF: <NAME>`.
- Treat review feedback like PR feedback.
- Review feedback may add new TODOs and reopen the list.

## Notes
- Sign-off is explicit in chat or in the file.
- `[x]` means ready for review, not final cleanup.
- If review adds work, the TODO list is no longer ready for cleanup.

## Examples
### Example 1: sign-off after all `[x]`
Prompt: `TODO_NAME: BLAH` with every item already `[x]`
Expected: require explicit `TODO_SIGNOFF: BLAH` for cleanup review.
```text
TODO_NAME: BLAH
[x] - BLAH-1 - build parser
[x] - BLAH-2 - verify cleanup

TODO_SIGNOFF: BLAH
```

### Example 2: review feedback
Prompt: reviewer adds a new TODO to the list
Expected: the list reopens and cleanup is blocked until the new work is DONE and signed off again.
