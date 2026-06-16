---
name: task
description: Manage portable task packets. Use when you need to create, update, extract, normalize, summarize, or link implementation context without performing the work.
---

# task

Goal: Manage task packets as portable units of context that future implementers or agents can consume.

Non-Goals: Do not implement tasks, verify tasks, manage whole plans except by reference, or place comments directly in files.

Use When:
- You need to extract a task packet from a plan item, comment, PRD, RFC, or user instruction.
- You need to normalize task context into stable fields.
- You need to update source links, targets, constraints, or verification hints for a task.

## Workflows

### Create Task Packet
1. Identify the smallest useful unit of work context.
2. Assign or preserve a stable task ID.
3. Capture goal, sources, targets, constraints, and verification hints when available.
4. Keep the packet portable: it should make sense outside its original file.

### Extract Task Packet
1. Read the source plan item, comment, PRD, RFC, or instruction.
2. Copy only context relevant to the task.
3. Preserve source references rather than duplicating large documents.
4. Leave unknown fields blank or mark them as unknown; do not invent false certainty.

### Update or Normalize Task Packet
1. Preserve the task ID.
2. Keep fields concise and implementation-oriented.
3. Do not mark the task verified or complete based on formatting alone.

See [Task Packet Format](references/task_packet_format.md) and [Extraction Rules](references/extraction_rules.md).

## Examples

### Example 1: From plan item
Prompt: "Create a task packet for plan item AUTH-2."
Decisions: Preserve `AUTH-2`; copy PRD/RFC links; include target files and verification hints only if known.
Outcome:
```text
TASK_ID: AUTH-2
Status: todo
Goal: Enforce expiry in auth middleware.
Source:
- PRD-AUTH#AC-3
- RFC-AUTH#D-2
Targets:
- src/auth/middleware.ts
```

### Example 2: From annotation
Prompt: "Turn TODO(AUTH-SESSION-1) into a task packet."
Decisions: Reference the annotation as source and state unknown fields explicitly.
Outcome: A task packet whose `Source` includes `COMMENT(AUTH-EXPIRY-1)`.
