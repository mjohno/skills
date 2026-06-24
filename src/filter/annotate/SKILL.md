---
name: annotate
description: Filters work items from source via inline task markers (TODO, NOTE, CHECK, REVIEW, DONE) embedded as structured annotations.
metadata:
  category: filter
  capabilities:
    - annotation_management
    - inline_task_carriers
---

# annotate

Goal: Create structured, actionable annotations in files. Annotations are inline task carriers with embedded status — not passive notes.
Non-Goals: Executing annotation work, managing task packet files, or modifying non-annotation content.
Use-When: You need to add TODOs, NOTEs, CHECKs, REVIEWs, or DONE marks directly into source files.

## 0. Prerequisites
- Target file and local context for the annotation

## 1. Inputs
- Target file path and local context from prompt
- Annotation kind: NOTE, TODO, CHECK, REVIEW, or DONE
- Message content and any refs (optional)

## 2. Processes
1. **Add Annotation**: Identify the target file type and local context. Choose the annotation kind. Generate a stable ID. Choose the native comment syntax for the file type. Add the annotation as close as possible to the relevant line or section. Include `refs:` when the annotation links to source material. Preserve indentation, formatting, and surrounding content.
2. **Update or Remove Annotation**: Locate the exact annotation by ID, text, or nearby context. Change only the targeted annotation block. Preserve unrelated code and prose.
3. **Extract Annotation**: Read the annotation and its message. For TODO/CHECK/REVIEW kinds, the annotation itself is the actionable artifact — it can be used directly as input to a task packet. For NOTE/DONE kinds, the annotation is informational or completion-marked.
4. **Normalize Annotation**: Keep the message concise and implementation-oriented. Use a stable ID that can be referenced later. Preserve the kind when the purpose stays the same; change the kind when the purpose changes, but keep the ID stable. Include refs when the annotation links to source material.

## 3. Outputs
- Annotation text in the prompt with the appropriate comment syntax
- If user specifies an output file, write the annotation to that path instead

## 4. Next Steps
- `task` — extract a task packet from a TODO/CHECK/REVIEW annotation
- `plan` — link annotation findings to a parent plan
- `step` — execute the work indicated by an annotation
- `annotate` — update or remove existing annotations

## 5. Examples

### Example 1: Add a NOTE annotation
**Prompt:**
> Add a NOTE to auth/config.py documenting the token refresh strategy.
**Decisions:**
- Kind: NOTE (knowledge/information)
- ID: AUTH-SESSION-1
- Syntax: `#` (Python)
- Refs: [auth/config.py:15]
**Outcome:**
```python
# NOTE(AUTH-SESSION-1): Token refresh uses sliding window, not fixed expiry
# refs: [auth/config.py:15]
TOKEN_WINDOW = 300
```

### Example 2: Mark completion with DONE
**Prompt:**
> Mark the token refresh TODO as complete.
**Decisions:**
- Kind: DONE (completion mark)
- ID: AUTH-SESSION-2 (preserved from original TODO)
- Syntax: `//` (TypeScript)
- Refs: [auth/flows.ts:128, RFC-AUTH.md#D-2]
**Outcome:**
```ts
// DONE(AUTH-SESSION-2): Token refresh implemented per RFC-AUTH#D-2
// refs: [auth/flows.ts:128, RFC-AUTH.md#D-2]
function refreshToken() { ... }
```
