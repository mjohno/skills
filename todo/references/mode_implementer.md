# mode:implementer

Use this mode to actually execute the work described by a named TODO list.

See [State Machine](state_machine.md) for transitions.

## Responsibilities
- Convert `TODO -> DOIN`.
- Process items in the caller's explicit order.
- Within one list, follow priority waves.
- For `BLAH`, operate on the whole list.
- For `BLAH-1`, operate only on that task.
- Update the list marker from `[ ]` to `[.]`.

## Expected behavior
- Execute the work described by the TODO item, comment, and nearby source material.
- Leave malformed detail alone unless writer mode is requested.
- Keep the grepable header line intact.
- Update the state in place.

## Examples
### Example 1: whole list
Prompt: `todo mode:implementer BLAH`
Expected: process all open items in `BLAH` by priority wave.
```text
TODO_NAME: BLAH
[ ] - BLAH-1 - build parser
[ ] - BLAH-2 - verify cleanup

TODO(BLAH-1, default, P1): build parser
> support chat and files
```
becomes
```text
TODO_NAME: BLAH
[.] - BLAH-1 - build parser
[ ] - BLAH-2 - verify cleanup

DOIN(BLAH-1, default, P1): build parser
> support chat and files
```

### Example 2: one task
Prompt: `todo mode:implementer BLAH-1`
Expected: only the requested task state changes.
