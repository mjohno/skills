---
name: annotate
description: Create structured, actionable annotations in files as inline task carriers. Use when you need to add TODOs, NOTEs, CHECKs, REVIEWs, or DONE marks directly into source files.
metadata:
  type: skill
---

# annotate

Goal: Create structured, actionable annotations in files. Annotations are inline task carriers with embedded status — not passive notes.
Non-Goals: Executing annotation work, managing task packet files, or modifying non-annotation content.

## Use When
- Embedding an actionable task directly into a source file
- Adding knowledge, context, or information as a permanent note
- Marking verification or test requirements inline
- Flagging a review or comparison against a source reference
- Marking work as complete inline
- Updating, removing, or extracting existing annotations

## Workflows

### Add Annotation
1. Identify the target file type and local context.
2. Choose the annotation kind: NOTE, TODO, CHECK, REVIEW, or DONE.
3. Generate a stable ID for the annotation.
4. Choose the native comment syntax for the file type (see [Annotation Syntax](references/annotation_syntax.md)).
5. Add the annotation as close as possible to the relevant line or section.
6. Include `refs:` when the annotation links to source material (see [Annotation Format](references/annotation_format.md) for format details).
7. Preserve indentation, formatting, and surrounding content.

### Update or Remove Annotation
1. Locate the exact annotation by ID, text, or nearby context.
2. Change only the targeted annotation block.
3. Preserve unrelated code and prose.

### Extract Annotation
1. Read the annotation and its message.
2. For TODO/CHECK/REVIEW kinds, the annotation itself is the actionable artifact — it can be used directly as input to a task packet without creating a separate task file.
3. For NOTE/DONE kinds, the annotation is informational or completion-marked.

### Normalize Annotation
1. Keep the message concise and implementation-oriented.
2. Use a stable ID that can be referenced later.
3. Preserve the kind when the purpose stays the same; change the kind (e.g., TODO → DONE) when the purpose changes, but keep the ID stable.
4. Include refs when the annotation links to source material.

See [Annotation Syntax](references/annotation_syntax.md) and [Annotation Format](references/annotation_format.md).

## Examples

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

See [Annotation Examples](assets/annotation_examples.md) for more.
