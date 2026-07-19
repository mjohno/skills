# Task Packet Format

A task packet is a portable context bundle. It may include a concise `Log` for evidence, comments, and handoff notes, but it is not a full execution journal.

## Minimal shape

```text
TASK_ID: <ID>
Status: todo
Goal: <one clear task goal>
Source:
- <spec/plan/comment/review/prompt/other source>
Targets:
- <file, module, section, or unknown>
Constraints:
- <constraint or unknown>
Verification:
- <hint or unknown>
next_tasks:
- <candidate next task ID or none>
Log:
- <evidence, comment, handoff note, or unknown>
```

## Fields

- `TASK_ID`: stable identifier.
- `Status`: standard lifecycle state: `todo`, `doing`, `verifying`, `reviewing`, or `done`.
- `Goal`: concise description of the desired change or investigation.
- `Source`: links to plan items, comments, specs, review findings, direct prompts, or other originating context.
- `Targets`: likely files, modules, sections, or domains.
- `Constraints`: compatibility, design, style, non-goals, or safety limits.
- `Verification`: test commands, checks, or evidence hints when known.
- `next_tasks`: candidate follow-up task IDs to avoid missing branches during step-by-step execution; this is navigation metadata, not a complete dependency graph.
- `Log`: concise evidence, comments, and handoff notes accumulated while the task moves between agents or stages.

## Rules

- Preserve IDs.
- Prefer links over copying large context.
- Mark unknowns honestly.
- Do not implement or verify from inside the task skill.
- Use `next_tasks` to list likely branch continuations after this task; use `none` or `unknown` when there is no known follow-up.
- The parent plan or coordinator remains responsible for reconstructing full progress and dependency order.
- Log entries may record evidence supplied by execution or review, but the task skill itself must not treat formatting as proof.
- Keep log entries concise, dated or attributed when useful, and oriented toward handoff.
- A task packet should be useful as input to a future implementer, verifier, or reviewer.
