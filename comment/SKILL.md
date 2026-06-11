---
name: comment
description: Manage file-local comments in code and documents. Use when you need to add, update, find, normalize, or remove comments without deciding or executing work.
---

# comment

Goal: Manage comments inside files using the correct syntax for the target file type.

Non-Goals: Do not decide implementation strategy, execute tasks, verify correctness, own plan state, or own task packet state.

Use When:
- You need to add a human or agent note to a source file, markdown file, SQL file, config file, or script.
- You need to update, remove, find, or normalize existing comments.
- You need a comment anchor that points to a plan item, task packet, PRD, RFC, or review note.

## Workflows

### Add Comment
1. Identify the target file type and local context.
2. Choose the least surprising comment syntax for that file.
3. Add the comment as close as possible to the relevant line or section.
4. Preserve indentation, formatting, and surrounding content.

### Update or Remove Comment
1. Locate the exact comment by ID, text, or nearby context.
2. Change only the targeted comment block.
3. Preserve unrelated code and prose.

### Normalize Comment
1. Keep human-readable language first.
2. Add a stable ID only when the comment needs to be referenced later.
3. Use a purpose tag when the comment should guide later discussion, implementation, verification, or review.
4. Keep structured fields short and optional.

See [Comment Syntax](references/comment_syntax.md) and [Comment Format](references/comment_format.md).

## Examples

### Example 1: Markdown comment
Prompt: "Add a comment to PRD.md noting that AC-3 does not define expired-session behavior."
Decisions: Use an HTML comment because the target is markdown; include a stable ID because the note may become a task.
Outcome:
```md
<!-- COMMENT(AUTH-EXPIRY-1): AC-3 does not define expired-session behavior. -->
```

### Example 2: TypeScript comment
Prompt: "Mark this branch as needing clarification from RFC-AUTH#D2."
Decisions: Use `//` because the target is a TypeScript statement-level note; use `CHECK` because a verifier should confirm behavior.
Outcome:
```ts
// CHECK(AUTH-EXPIRY-2): Confirm this branch matches RFC-AUTH#D2.
```
