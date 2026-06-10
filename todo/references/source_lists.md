# TODO List

Use this when a request mentions a plan, RFC, prompt, or file with TODOs.

See [State Machine](state_machine.md) for lifecycle transitions.

## Canonical source header
```text
TODO_NAME: <NAME>
```
- `<NAME>` is the namespace for IDs.
- A TODO list may live in chat or in a file.
- The name may be inferred from context, but writer mode must make it explicit.
- 4-character names are recommended when inferring from context.
- Multiple lists may exist in one artifact.

## TODO list shape
```text
TODO_NAME: AAAA
[ ] - AAAA-1 - Some summary
[.] - AAAA-2 - Other summary
[x] - AAAA-3 - Finished summary.
```
- The TODO list is a list of TODO items, not a comment block.
- Each item keeps its ID in the list.
- Inline comments are separate from the list structure.
- Use `mode:commentor` for inline comment instances.

## IDs
- Use `<NAME>-<NUM>`.
- Numbers start at 1.
- IDs are immutable.
- Gaps are preserved forever.
- On merge, renumber into the target list and update the comment ID.

## Targeting
- `BLAH` means operate on the whole list in priority-wave order.
- `BLAH-1` means operate on one task.
- If multiple lists are present and the target is unclear, ask for an explicit ordered worklist.
- Fuzzy ordering is allowed if the intent is still unambiguous.
- For inline comment IDs, use `mode:commentor`.

## Searchability
- `rg -n '^TODO_NAME:\s*' .`
- `rg -n '^\[( |\.|x)\] - [A-Za-z0-9_-]+-[0-9]+ -' .`
- `rg -n '^(TODO|DOIN|DONE)\([^)]+\):' .`
- `rg -n '^TODO_SIGNOFF:\s*' .`
- `rg -n "^(TODO|DOIN|DONE)\(${NAME}-" .`  # replace NAME with the TODO list name
- `rg -n "\b${NAME}-[0-9]+\b" .`  # replace NAME with the TODO list name

## Examples

### Example 1: canonical list

Prompt: `TODO_NAME: BLAH`
Expected: a list namespace exists and tasks are named `BLAH-<NUM>`.
```text
TODO_NAME: BLAH
[ ] - BLAH-1 - define parser
[.] - BLAH-2 - verify cleanup
[x] - BLAH-3 - merge rules
```

### Example 2: inferred name

Prompt: `write TODOs for parser cleanup`
Expected: infer a short `TODO_NAME` when context is unambiguous, then make it explicit in writer mode.
E.g: `TODO_NAME: PACU`

### Example 3: state markers
Prompt: `[ ]`, `[.]`, `[x]`
Expected: `[ ]` = TODO, `[.]` = DOIN, `[x]` = DONE.

### Example 4: targeting

Prompt: `BLAH-1`
Expected: operate on only task 1 of the `TODO_NAME: BLAH` list.
