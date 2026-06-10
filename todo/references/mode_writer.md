# mode:writer

Use this mode to resolve source requirements into a TODO list.

See [State Machine](state_machine.md) for transitions.

See [TODO list template](../assets/todo_list_template.md) for a canonical starting shape.

## Responsibilities
- Make `TODO_NAME:` explicit.
- Resolve requirements from chat, PRDs, RFCs, and plans into TODO items.
- Repair malformed list items and list metadata.
- Rewrite the TODO list as the desired final state.
- Merge existing canonical items into the list.
- Fill gaps by writing the complete set of items that should exist.
- Sort by priority wave within the TODO list.

## Output shape
```text
TODO_NAME: <NAME>
[ ] - <NAME>-1 - <SUMMARY>
[.] - <NAME>-2 - <SUMMARY>
[x] - <NAME>-3 - <SUMMARY>
```
Use the template for fuller examples and list layout.
- Inline TODO comments are owned by `mode:commentor`.
- Use `default` when the assignee is a hint and the implementer should choose.

## Notes
- If the input is only a chat prompt, infer the TODO list name when possible and make it explicit in the output.
- Writer mode is the only mode that should care about fixing malformed list structure.
- Prefer the asset template when generating a new list from scratch.
- Do not author inline TODO comments; hand off to `mode:commentor`.

## Examples
### Example 1: new list
Prompt: `write TODOs for parsing and cleanup`
Expected: infer a name if needed, then emit `TODO_NAME: <NAME>` and canonical list items sorted by priority wave, using `[ ]`, `[.]`, and `[x]` appropriately.

### Example 2: fix malformed list
Prompt: existing list with broken TODO lines
Expected: normalize into canonical list items and make the TODO list explicit.
