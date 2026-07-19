# Task Packet Format

A task packet is a portable context bundle. It may include a concise `Log` for evidence, comments, and handoff notes, but it is not a full execution journal.

## Minimal shape

```text
TASK_ID: <ID>
Status: todo
Goal: <one clear task goal>
Source:
- <spec/RFC/plan/comment/user source>
Targets:
- <file, module, section, or unknown>
Constraints:
- <constraint or unknown>
Verification:
- <hint or unknown>
Log:
- <evidence, comment, handoff note, or unknown>
```

## Fields

- `TASK_ID`: stable identifier.
- `Status`: lightweight task state, usually `todo`, `blocked`, or `done`.
- `Goal`: concise description of the desired change or investigation.
- `Source`: links to plan items, comments, specs, RFCs, or direct prompts.
- `Targets`: likely files, modules, sections, or domains.
- `Constraints`: compatibility, design, style, non-goals, or safety limits.
- `Verification`: test commands, checks, or evidence hints when known.
- `Log`: concise evidence, comments, and handoff notes accumulated while the task moves between agents or stages.

## Rules

- Preserve IDs.
- Prefer links over copying large context.
- Mark unknowns honestly.
- Do not implement or verify from inside the task skill.
- Log entries may record evidence supplied by execution or review, but the task skill itself must not treat formatting as proof.
- Keep log entries concise, dated or attributed when useful, and oriented toward handoff.
- A task packet should be useful as input to a future implementer, verifier, or reviewer.
