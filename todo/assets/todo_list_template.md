# TODO list template

Use this as a canonical starting point for a TODO list.

```text
TODO_NAME: BLAH
[ ] - BLAH-1 - define the parser
[.] - BLAH-2 - verify cleanup behavior
[x] - BLAH-3 - document merge rules
```

Near an item that needs updating, use a TODO comment:
```text
TODO(BLAH-1, default, P1): define the parser
> support chat and files
> keep grepable output
```

Notes:
- `TODO_NAME:` names the TODO list.
- IDs are immutable once assigned.
- Priority waves sort within the list.
- `default` means the implementer picks the assignee.
