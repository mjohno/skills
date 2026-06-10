---
name: todo
description: Manage grepable TODO lists and comments. Use when you need to write, implement, verify, review, or clean TODO items in chat, docs, or code.
---

# todo

Goal: Keep implementation local and fast by using a TODO list plus nearby TODO comments to execute work instead of a separate task system.

Success:
- Each role advances the requirement toward completion.
- The TODO list and nearby comments stay aligned with the real work.

Failure:
- The TODO machinery changes, but the requirement does not.
- The repository gains churn without reducing open work.

Non-Goals: General project management, time tracking, or replacing PR review.

Use When:
- You need to create or normalize a TODO list from a PRD, RFC, chat prompt, or plan and use nearby TODO comments to track execution.
- You need to write, implement, verify, review, or clean TODO comments.

## Workflow

1. Select Mode
2. Identify TODOs to work on
3. Complete the Mode for the TODO List(s)

### 1. Select Mode

The user should provide some kind of mode hint in their prompt. Choose the mode which best fits.
If no mode is specified, ask the user and suggest what makes the most sense.

- `mode:writer` - Resolve source requirements into TODO lists and nearby TODO comments. See [Writer](references/mode_writer.md).
- `mode:implementer` - Actually execute TODO items and nearby TODO comments. See [Implementer](references/mode_implementer.md)
- `mode:verifier` - Check the implemented work behind TODO items and nearby TODO comments. See [Verifier](references/mode_verifier.md)
- `mode:reviewer` - Review TODO items and nearby TODO comments. See [Reviewer](references/mode_reviewer.md)
- `mode:cleanup` - Clean up TODO comments. [Cleanup](references/mode_cleanup.md)

### 2. Identify TODOs to work on

The user should provide a TODO list with a priority wave or TODO IDs in their prompt.
- A TODO list has `TODO_NAME: <NAME>`.
- A TODO list is a list of TODO items, for example `[ ] - AAAA-1 - Some summary`.
- `[ ]` means TODO, `[.]` means DOIN, and `[x]` means DONE.
- A priority wave is a priority level like `P1` or `P2` which is assigned to TODOs.
- TODO IDs are unique identifiers for TODO items, typically in the format `<NAME>-<NUM>`.

### 3. Complete the Mode for the TODO List(s)

- Follow the instructions for the selected mode to operate on the TODO items and nearby TODO comments from the specified sources.
- See [State Machine](references/state_machine.md) for lifecycle transitions.

### TODO list item

```text
TODO_NAME: <NAME>
[ ] - <NAME>-1 - Some summary
[.] - <NAME>-2 - In progress summary
[x] - <NAME>-3 - Done summary.
```
- The TODO list is a list of TODOs.
- IDs are immutable and gaps are preserved forever.
- The item list may be in chat or in a file.

### TODO comment block

```text
TODO(<ID>, <ASSIGNEE>, <PRIORITY>): <SUMMARY>
> detail line
> ...
```
- Use `DOIN(...)` and `DONE(...)` with the same field order.
- `ASSIGNEE` is freeform; `default` means the implementer chooses.
- Priorities are `P#` values and sort numerically within a TODO list.
- For non-writer modes, only the grepable line is required; details may be messy.

### Searchability
- `rg -n '^TODO_NAME:\s*' .`
- `rg -n '^\[( |\.|x)\] - [A-Za-z0-9_-]+-[0-9]+ -' .`
- `rg -n '^(TODO|DOIN|DONE)\([^)]+\):' .`
- `rg -n '^TODO_SIGNOFF:\s*' .`
- `rg -n "^(TODO|DOIN|DONE)\(${NAME}-" .`  # replace NAME with the TODO list name
- `rg -n "\b${NAME}-[0-9]+\b" .`  # replace NAME with the TODO list name

## Examples

### Example 1

Prompt: `todo mode:writer BLAH`
Decisions: wrote `TODO_NAME: BLAH`, normalized the list, and sorted by priority wave.
Outcome:
```text
TODO_NAME: BLAH
[ ] - BLAH-1 - ...
[ ] - BLAH-2 - ...
```

### Example 2

Prompt: `todo mode:implementer BLAH P1, ASDF P3`
Decisions: processed each TODO list in the explicit order given by the caller.
Outcome: nearby `TODO(...)` comments became `DOIN(...)` comments for the requested priority wave. Implementer actioned the DOIN items.
