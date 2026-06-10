---
name: todo
description: Manage grepable TODO lists and comments. Use when you need to write, implement, verify, review, or clean TODO items in chat, docs, or code.
---

# todo

Goal: Keep implementation local and fast by using a TODO list plus separate inline TODO comments instead of a separate task system.

Success:
- Each role advances the requirement toward completion.
- The TODO list and inline comments stay aligned with the real work.

Failure:
- The TODO machinery changes, but the requirement does not.
- The repository gains churn without reducing open work.

Non-Goals: General project management, time tracking, or replacing PR review.

Use When:
- You need to create or normalize a TODO list from a PRD, RFC, chat prompt, or plan.
- You need to write, implement, verify, review, or clean inline TODO comments.

## Workflow

1. Select Mode
2. Identify TODOs to work on
3. Complete the Mode for the TODO List(s)

### Select Mode

If no mode hint is provided, ask which mode fits best.
- `mode:writer` - Resolve source requirements into TODO lists. See [Writer](references/mode_writer.md).
- `mode:commentor` - Create, update, and repair inline TODO comments. See [Commentor](references/mode_commentor.md).
- `mode:implementer` - Execute TODO items and inline TODO comments. See [Implementer](references/mode_implementer.md)
- `mode:verifier` - Check the implemented work behind TODO items and inline TODO comments. See [Verifier](references/mode_verifier.md)
- `mode:reviewer` - Review TODO items and inline TODO comments. See [Reviewer](references/mode_reviewer.md)
- `mode:cleanup` - Clean up TODO comments. [Cleanup](references/mode_cleanup.md)

### Identify TODOs

- A TODO list has `TODO_NAME: <NAME>` and items like `[ ] - AAAA-1 - Summary`.
- `[ ]` means TODO, `[.]` means DOIN, `[x]` means DONE.
- Use a priority wave like `P1` or `P2`, or explicit TODO IDs.

### Complete the Mode

- Follow the selected mode’s instructions for the TODO items and inline TODO comments.
- See [State Machine](references/state_machine.md) for lifecycle transitions.

### TODO list item

```text
TODO_NAME: <NAME>
[ ] - <NAME>-1 - Some summary
[.] - <NAME>-2 - In progress summary
[x] - <NAME>-3 - Done summary.
```
- IDs are immutable and gaps are preserved forever.
- The item list may be in chat or in a file.

### Inline TODO comment block

```text
TODO(<ID>, <ASSIGNEE>, <PRIORITY>): <SUMMARY>
> detail line
> ...
```
- Use `DOIN(...)` and `DONE(...)` with the same field order.
- `ASSIGNEE` is freeform; `default` means the implementer chooses.
- Priorities are `P#` values and sort numerically within a TODO list.
- Commentor mode owns creation and repair of this structure.
- For non-writer modes, only the grepable line is required.

### Searchability
- `rg -n '^TODO_NAME:\s*' .`
- `rg -n '^\[( |\.|x)\] - [A-Za-z0-9_-]+-[0-9]+ -' .`
- `rg -n '^(TODO|DOIN|DONE)\([^)]+\):' .`
- `rg -n '^TODO_SIGNOFF:\s*' .`
- `rg -n "^(TODO|DOIN|DONE)\(${NAME}-" .`
- `rg -n "\b${NAME}-[0-9]+\b" .`

## Examples

### Example 1
Prompt: `todo mode:writer BLAH`
Decisions: wrote `TODO_NAME: BLAH` and normalized the list.
Outcome:
```text
TODO_NAME: BLAH
[ ] - BLAH-1 - ...
[ ] - BLAH-2 - ...
```
