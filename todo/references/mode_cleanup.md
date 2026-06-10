# mode:cleanup

Use this mode after the TODO list has been signed off.

See [State Machine](state_machine.md) for transitions.

## Responsibilities
- Remove all `[x]` items/comments for the TODO list.
- Leave `[ ]` and `[.]` items in place.
- Leave the source file itself in place.

## Notes
- Cleanup is only for completed items.
- Unfinished TODOs remain as open work.
- If review adds new work, cleanup is blocked until that work is done and signed off again.

## Examples
### Example 1: completed list
Prompt: `todo mode:cleanup BLAH`
Expected: remove all `[x]` items/comments and leave the rest.
```text
TODO_NAME: BLAH
[ ] - BLAH-1 - build parser
[.] - BLAH-2 - verify cleanup
[x] - BLAH-3 - merge rules
```

### Example 2: incomplete list
Prompt: `todo mode:cleanup BLAH` when some items are still TODO/DOIN
Expected: do not remove unfinished work; cleanup is not complete.
