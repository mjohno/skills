# mode:writer

Use this mode to resolve source requirements into a TODO list and nearby TODO comments.

See [State Machine](state_machine.md) for transitions.

See [TODO list template](../assets/todo_list_template.md) for a canonical starting shape.

## Responsibilities
- Make `TODO_NAME:` explicit.
- Resolve requirements from chat, PRDs, RFCs, and plans into TODO items.
- Repair malformed list items and nearby TODO comments.
- Rewrite the TODO list as the desired final state.
- Merge existing canonical items and nearby TODO comments into the list.
- Fill gaps by writing the complete set of items that should exist.
- Sort by priority wave within the TODO list.

## Output shape
```text
TODO_NAME: <NAME>
[ ] - <NAME>-1 - <SUMMARY>
[.] - <NAME>-2 - <SUMMARY>
[x] - <NAME>-3 - <SUMMARY>

TODO(<ID>, <ASSIGNEE>, <PRIORITY>): <SUMMARY>
> detail line
```
Use the template for fuller examples and list layout. Nearby TODO comments use the canonical comment block.
- Keep details under the block as needed.
- Use `default` when the assignee is a hint and the implementer should choose.

## Notes
- If the input is only a chat prompt, infer the TODO list name when possible and make it explicit in the output.
- Writer mode is the only mode that should care about fixing malformed list structure.
- Prefer the asset template when generating a new list from scratch.
- Write nearby TODO comments for specific requirements when needed; this convention is for executing work, not just managing it.

## Examples
### Example 1: new list
Prompt: `write TODOs for parsing and cleanup`
Expected: infer a name if needed, then emit `TODO_NAME: <NAME>` and canonical list items sorted by priority wave, using `[ ]`, `[.]`, and `[x]` appropriately.

### Example 2: fix malformed list
Prompt: existing list with broken TODO lines
Expected: normalize into canonical list items and make the TODO list explicit; preserve or attach nearby TODO comments as needed.
