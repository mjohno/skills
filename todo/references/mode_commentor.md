# mode:commentor

Use this mode to create, update, and repair inline TODO comment instances for a specific comment ID.

See [State Machine](state_machine.md) for lifecycle transitions.

## Responsibilities
- Turn a source requirement, TODO list, or plan into inline comments.
- Target a specific comment ID in the form `<NAME>-<NUM>`.
- Use `rg`/`grep` to discover existing inline instances for that exact ID.
- Support fan-out: the same comment ID may appear in multiple files or multiple locations in one file.
- Create new nearby instances when needed, or update existing instances when explicitly targeted.
- Preserve existing body lines unless the user explicitly asks to rewrite them.
- Allow explicit state repair for `TODO`, `DOIN`, and `DONE` when requested.
- Leave the TODO list itself read-only.
- Report same-line conflicts and partial failures without guessing.

## Input expectations
- The user may provide a file, line, symbol, or definition as an explicit nearby target.
- The user may also request a specific comment state transition or repair.
- If an update touches a batch of instances, continue processing the remaining instances after a conflict and report the failures.

## Output shape
```text
TODO(<ID>, <ASSIGNEE>, <PRIORITY>): <SUMMARY>
> detail line
> detail line
```
- Use `DOIN(...)` and `DONE(...)` with the same field order.
- The headline is fixed.
- Each new body line begins with `>`.
- Body text may vary by location; rewrite body lines only when explicitly requested.

## Notes
- `ASSIGNEE` is freeform; `default` means the implementer chooses.
- `PRIORITY` is a `P#` value used for the comment batch.
- A comment instance can remain partially complete until the batch is finished.
- The batch is done only when all instances for the same comment ID are complete.

## Examples
### Example 1: create nearby instance
Prompt: `commentor TDCM-1 file=todo/SKILL.md`
Expected: write a nearby `TODO(TDCM-1, default, P1): ...` comment next to the requested location.

### Example 2: update existing instance
Prompt: `commentor TDCM-3 todo/references/mode_commentor.md`
Expected: locate the matching inline comment instance and update its body or state in place.
