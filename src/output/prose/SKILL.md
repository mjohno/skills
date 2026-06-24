---
name: prose
description: Produces polished prose-style content — articles, essays, narratives, and blog posts.
metadata:
  category: output
  capabilities:
    - prose_generation
---

# prose

Goal: Format information into polished prose (articles, essays, narratives, blog posts).
Non-Goals: Creating structured documents (PRDs, RFCs), generating code, or producing data outputs.
Use-When: You need to write articles, essays, narratives, blog posts, or any prose-style content.

## 0. Prerequisites
- Raw information, notes, or context to format into prose

## 1. Inputs
- Source material (raw information, notes, outlines, or context from prompt)
- Target format (article, essay, narrative, blog post, etc.)
- Tone and audience (optional: formal, casual, technical, general)

## 2. Processes
1. Parse source material to identify key themes, arguments, and narrative arc
2. Structure the prose: introduction, body sections, conclusion
3. Draft the content with appropriate tone, flow, and transitions
4. Refine for clarity, conciseness, and engagement
5. Self-edit: check for repetition, ambiguity, and logical flow

## 3. Outputs
- Polished prose in the prompt
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `review` — have the `review` skill evaluate the prose for quality and clarity
- `collect` — gather more information if the prose needs additional context

## 5. Examples

### Example 1: Blog post

**Prompt:** Write a blog post about zero-trust architecture for a technical audience.

**Outcome:** Prompt output with a 1500-word blog post explaining zero-trust principles, benefits, and implementation challenges in a conversational tone.

### Example 2: Executive summary

**Prompt:** Turn the analysis into an executive summary.

**Outcome:** Prompt output with a concise 500-word executive summary highlighting key findings and recommendations.
