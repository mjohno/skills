---
name: task
description: Normalizes portable task packets — creating, updating, extracting, summarizing, and linking implementation context without performing the work.
metadata:
  category: normalize
  capabilities:
    - packet_creation
    - packet_extraction
    - packet_normalization
    - cross_cutting_context
---

# task

Goal: Normalize implementation context into portable, self-contained task packets that future implementers or agents can consume.
Non-Goals: Implementing tasks, verifying tasks, managing whole plans except by reference, or placing comments directly in files. Note: task is cross-cutting — it operates across pipeline stages rather than being anchored to a single phase.
Use-When: You need to extract a task packet from a plan item, comment, PRD, RFC, or user instruction.

## 0. Prerequisites
- A source to extract from: plan item, comment, PRD, RFC, or user instruction

## 1. Inputs
- Source artifact from prompt (plan item, comment, PRD, RFC, or user instruction)
- Target fields to capture (optional: goal, sources, targets, constraints, verification hints)

## 2. Processes
1. **Create Task Packet**: Identify the smallest useful unit of work context. Assign or preserve a stable task ID. Capture goal, sources, targets, constraints, and verification hints when available. Keep the packet portable: it should make sense outside its original file.
2. **Extract Task Packet**: Read the source plan item, comment, PRD, RFC, or instruction. Copy only context relevant to the task. Preserve source references rather than duplicating large documents. Leave unknown fields blank or mark them as unknown; do not invent false certainty.
3. **Update or Normalize Task Packet**: Preserve the task ID. Keep fields concise and implementation-oriented. Do not mark the task verified or complete based on formatting alone.

## 3. Outputs
- Task packet in the prompt with stable fields (TASK_ID, Status, Goal, Source, Targets, etc.)
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `plan` — link task packets back to a parent plan
- `step` — execute the task
- `annotate` — add inline annotations related to the task
- `task` — update or extract additional task packets

## 5. Examples

### Example 1: From plan item
**Prompt:** "Create a task packet for plan item AUTH-2."
**Decisions:** Preserve `AUTH-2`; copy PRD/RFC links; include target files and verification hints only if known.
**Outcome:**
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
**Prompt:** "Turn TODO(AUTH-SESSION-1) into a task packet."
**Decisions:** Reference the annotation as source and state unknown fields explicitly.
**Outcome:** A task packet whose `Source` includes `COMMENT(AUTH-EXPIRY-1)`.
