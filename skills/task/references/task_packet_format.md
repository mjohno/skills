# Task Packet Format

A task packet is a portable context bundle. It is not an execution log.

## Minimal shape

```text
TASK_ID: <ID>
Status: todo
Goal: <one clear task goal>
Source:
- <PRD/RFC/plan/comment/user source>
Targets:
- <file, module, section, or unknown>
Constraints:
- <constraint or unknown>
Verification:
- <hint or unknown>
```

## Fields

- `TASK_ID`: stable identifier.
- `Status`: lightweight task state, usually `todo`, `blocked`, or `done`.
- `Goal`: concise description of the desired change or investigation.
- `Source`: links to plan items, comments, PRDs, RFCs, or direct prompts.
- `Targets`: likely files, modules, sections, or domains.
- `Constraints`: compatibility, design, style, non-goals, or safety limits.
- `Verification`: test commands, checks, or evidence hints when known.

## Rules

- Preserve IDs.
- Prefer links over copying large context.
- Mark unknowns honestly.
- Do not implement or verify from inside the task skill.
- A task packet should be useful as input to a future implementer, verifier, or reviewer.
