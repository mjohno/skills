# mode:verifier

Use this mode to check the implemented work behind a `DOIN` item.

See [State Machine](state_machine.md) for transitions.

## Responsibilities
- Convert `DOIN -> DONE` when verified.
- Convert `DOIN -> TODO` when verification fails or is incomplete.
- Keep the same ID, assignee, and priority.
- Update the list marker from `[.]` to `[x]` or `[ ]` accordingly.

## Notes
- Verification should be local to the requested TODO list or task.
- Check the actual work, not just the state marker.
- `[x]` means ready for review.
- `[ ]` means it needs more implementation.
- Keep the TODO list and nearby comment in sync.

## Examples
### Example 1: verified
```text
TODO_NAME: BLAH
[.] - BLAH-2 - check cleanup

DOIN(BLAH-2, reviewer, P2): check cleanup
> remove DONE comments only
```
becomes
```text
TODO_NAME: BLAH
[x] - BLAH-2 - check cleanup

DONE(BLAH-2, reviewer, P2): check cleanup
> remove DONE comments only
```
Expected: verification passed; the item is now ready for review.

### Example 2: not done
```text
DOIN(BLAH-2, reviewer, P2): check cleanup
```
becomes
```text
TODO(BLAH-2, reviewer, P2): check cleanup
```
Expected: verification failed or is incomplete; the item returns to implementation.
