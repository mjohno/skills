---
name: writing
description: A unified writing skill for reviewing and drafting English prose. Use when you need to critique prose for readability, density, and style, or generate polished prose from notes, drafts, or rough ideas.
---

# Writing

Goal: Improve or generate clear, dense, human-sounding English prose.
Non-Goals: Project management, factual research, or literary criticism.

Use When:
- You need to review prose for quality.
- You need to draft or rewrite prose from notes or rough text.
- You need to make technical writing clearer without making it sound templated.

## Workflows

### mode:review
Use when the user wants critique or feedback.
- Infer review mode when the intent is clear; ask if confidence is below 90%.
- Produce one ranked list of findings, not separate readability/density sections.
- Tag findings lightly (`readability`, `density`, `style`) and label severity (`high`, `medium`, `low`).
- Lead with findings, then give concise suggested changes.

### mode:write
Use when the user wants prose generated or polished.
- Infer write mode when the intent is clear; ask if confidence is below 90%.
- Work in passes when useful.
- Output a draft, notes, and optional alternatives.
- Preserve the user's voice when possible; remove AI-sounding filler.

## References
- See [mode_review](references/mode_review.md).
- See [mode_write](references/mode_write.md).
- See [readability_guidelines](references/readability_guidelines.md).
- See [density_guidelines](references/density_guidelines.md).

## Examples

### Example 1
Prompt: `writing mode:review`.
Decisions: Identified the prompt as a critique request, ran one unified review pass, ranked findings, and suggested concise changes.
Outcome: Returned a tagged list of issues with severity and a short follow-up of recommended edits.

### Example 2
Prompt: `writing mode:write`.
Decisions: Identified the prompt as generative, drafted in multiple passes, and kept alternatives only where tone or structure could vary.
Outcome: Returned polished prose with notes and a few useful options.

### Example 3
Prompt: `writing: tighten this abstract and make it sound less robotic`.
Decisions: Inferred write mode from the drafting intent, then produced a polished revision with notes and an alternate opening where useful.
Outcome: Returned a draft plus a small set of options instead of asking for a mode flag.

### Example 4
Prompt: `writing: review this paragraph or rewrite it if needed`.
Decisions: The intent was ambiguous, so the skill asked which mode the user wanted instead of guessing.
Outcome: Requested clarification because confidence was below 90%.
