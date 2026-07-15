---
name: prose
description: Use when output or map skills need the prose artifact contract for articles, essays, summaries, or narrative text.
disable-model-invocation: true
metadata:
  category: interface
  capabilities:
    - prose_shape
    - content_brief
---

# prose

Goal: Define the prose artifact contract for audience, purpose, message, structure, tone, and source constraints.
Non-Goals: Drafting final prose, polishing language, fact-checking claims, or producing structured specs like PRDs/RFCs.
Use-When: Another skill needs the `prose` interface contract before outlining, drafting, modifying, reviewing, or orchestrating this artifact.

## 0. Prerequisites
- Raw notes, research, idea, outline, existing prose, or communication goal
- Target audience, format, or channel when available

## 1. Inputs
- Purpose, audience, desired action, key points, sources, and constraints
- Format such as article, essay, memo, narrative, blog post, summary, or announcement
- Optional tone, length, reading level, stance, and claims requiring provenance

## 2. Processes
1. Identify the reader, purpose, message, and desired effect.
2. Define format, tone, length, structure, and evidence expectations.
3. Distinguish must-include points from optional supporting material.
4. Flag claims that need provenance, examples, or user confirmation.
5. Preserve voice and style constraints without drafting full paragraphs.

## 3. Outputs
- Interface-defined prose brief contract consumed by `output/outline`, `output/draft`, or `output/modify`

Interface-defined shape:
```text
PROSE:
Purpose:
Audience:
Format:
Core Message:
Key Points:
Tone/Voice:
Length:
Sources/Evidence:
Must Include:
Avoid:
Open Questions:
```

## 4. Next Steps
- `output/outline` — create the prose structure or section plan using this contract
- `output/draft` — produce first-pass prose using this contract
- `output/modify` — revise, polish, shorten, expand, or adapt existing prose

## 5. Examples

### Example 1: Blog post brief
**Prompt:** Define these notes into a prose brief for a technical blog post.
**Outcome:** Produces audience, core message, tone, key points, source needs, and open questions.

### Example 2: Executive summary brief
**Prompt:** Shape this analysis into a prose brief for executives.
**Outcome:** Produces a concise content brief focused on decision context, message, tone, and must-include findings.
