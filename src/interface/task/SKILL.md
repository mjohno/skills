---
name: task
description: Use when output or map skills need the task packet contract for portable implementation context.
metadata:
  type: interface
  category: interface
---

# task

Goal: Define the task packet contract for portable, self-contained implementation context.
Non-Goals: Implementing tasks, verifying tasks, managing whole plans except by reference, or placing comments directly in files. Note: task is cross-cutting — it operates across pipeline stages rather than being anchored to a single phase.
Use-When: Another skill needs the `task` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- A source to extract from: plan item, comment, spec, review finding, prompt, or other actionable context

## 1. Inputs
- Source artifact from prompt (plan item, comment, spec, review finding, prompt, or other actionable context)
- Target fields to capture (optional: goal, sources, targets, constraints, verification hints, `next_tasks`, log entries)

## 2. Process
1. **Create Task Packet**: Identify the smallest useful unit of work context. Assign or preserve a stable task ID. Capture goal, sources, targets, constraints, verification hints, candidate `next_tasks`, and initial log entries when available. Keep the packet portable: it should make sense outside its original file.
2. **Extract Task Packet**: Read the source context. Copy only context relevant to the task. Preserve source references rather than duplicating large documents. Leave unknown fields blank or mark them as unknown; do not invent false certainty.
3. **Update or Define Task Packet**: Preserve the task ID. Keep fields concise and implementation-oriented. Use `next_tasks` for candidate follow-up task IDs so branch continuations are not missed. Use `Log` for evidence, comments, and handoff notes. Do not mark the task verified or complete based on formatting alone.

## 3. Outputs
- Minimal default output: selected task contract, assumptions, selected package-local paths, and loaded selected contents only.
- Always return selected file paths followed by loaded contents in fenced code blocks.
- Task packet selection returns:
  - `src/interface/task/references/task_packet_format.md`
  - `src/interface/task/references/extraction_rules.md`
  - `src/interface/task/assets/task_packet_template.md`

## 4. Next Steps
- `output/modify` with `interface/plan` — link task packets back to a parent plan
- `map/step` — execute the task
- `output/annotate` — add inline annotations related to the task
- `output/modify` or `output/draft` with `interface/task` — update or extract additional task packets

## 5. Examples

### Example 1: From plan item
**Prompt:** "Use the task interface to create a packet for plan item AUTH-2."
**Decision:** Select task packet format, extraction rules, and template.
**Outcome:** Return selected paths and loaded contents:

file_path: src/interface/task/references/task_packet_format.md
```markdown
# Task Packet Format
[loaded task packet format]
```

file_path: src/interface/task/assets/task_packet_template.md
```markdown
# Task Packet
[loaded task packet template]
```

### Example 2: From annotation
**Prompt:** "Use the task interface for TODO(AUTH-SESSION-1)."
**Decision:** Select extraction rules and task packet template.
**Outcome:** Return selected paths and loaded contents, including:

file_path: src/interface/task/references/extraction_rules.md
```markdown
# Extraction Rules
[loaded extraction rules]
```
