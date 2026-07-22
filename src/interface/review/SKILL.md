---
name: review
description: Define the minimal evaluation-contract interface for producing prioritized review questions from an artifact, its spec(s), and persona lenses.
metadata:
  type: interface
  category: interface
---

# review

Goal: Produce a prioritized set of evaluative questions (a review contract) derived from an artifact's spec(s) and persona lenses, for subsequent execution by an evaluation skill.
Non-Goals: Do not execute reviews, discover specs or personas, produce severity reports, or remediate findings. Discovery is upstream (orchestrator/investigate/lookup).
Use-When: Another skill needs the `review` interface contract before evaluating, executing a review pass, or planning gap-closing work from evaluation findings.

## Selection

Default: return only the compact [`review_contract.md`](references/review_contract.md).

Also select:
- [`review_checklist.md`](references/review_checklist.md) when the caller asks to check review contract conformance.
- [`review_quality.md`](references/review_quality.md) when the caller asks to review review contract quality.

If caller intent is unclear, assume default contract only and state the assumption.
If requested review needs fall outside this interface, state the unsupported need and hand off to the appropriate skill.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

<!-- TODO: Address the duplication of returned content in Selection and Return sections. -->


<!-- TODO: Address the duplication between the question design rules, and the checklist and quality docs. -->

<!-- TODO: Include a findings template under `assets/findings_template.md` which captures how findings should be presented.
        Priority headings
        Numbered findings for easy identification
        Mapped to Questions - Perhaps Q), A).
-->

### Question Design Rules

- Each question probes a specific judgment area derived from spec requirements + persona criteria.
- Avoid binary phrasing. Favor questions that invite nuanced analysis (how, why, to what extent, what trade-offs, under what conditions).
- Include at least one question per persona lens.
- Prioritize: P1-equivalent areas first (structural/spec violations), then P2/P3 (quality/clarity).
- Base criteria (consistency, clarity) should appear as early questions when the artifact's quality is a review target.
- Each question should map to at least one spec requirement or persona criterion.

### Contract Rules

- Questions are **evaluable by an LLM** — they ask for reasoning anchored in the artifact content + loaded criteria, not external research.
- If a persona adds no meaningful perspective beyond another already-loaded lens, do not create a separate section.
- Source criteria mapping is required: every question must trace back to at least one spec ID or persona criterion so findings can cite sources.

## Next Steps

- `interface/plan` — create gap-closing work from unanswered or low-confidence questions.
- `transform/check` — validate that a revised artifact addresses prior review findings.
- `output/annotate` — add inline annotations for tracking findings (NOTE) and fixes (TODO).

## Minimal Example

**Prompt:** "Use the review interface for reviewing auth-module design against SPEC-auth using security and adversarial lenses."

file_path: references/review_contract.md
```markdown
[loaded compact spec contract]
```
