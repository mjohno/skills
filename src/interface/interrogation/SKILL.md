---
name: interrogation
description: Define the minimal evaluation-contract interface for producing prioritized evaluation questions from an artifact, its spec(s), and persona lenses.
metadata:
  type: interface
  category: interface
---

# interrogation

Goal: Produce a prioritized set of evaluative questions (an interrogation contract) derived from an artifact's spec(s) and persona lenses, for subsequent execution by an evaluation skill.
Non-Goals: Do not execute evaluations, discover specs or personas, produce severity reports, or remediate findings. Discovery is upstream (orchestrator/investigate/lookup).
Use-When: Another skill needs the `interrogation` interface contract before evaluating, executing an evaluation pass, or planning gap-closing work from evaluation findings.

## Selection

Default: return only the compact [`interrogation_contract.md`](references/interrogation_contract.md).

Also select:
- [`interrogation_checklist.md`](references/interrogation_checklist.md) when the caller asks to check interrogation contract conformance.
- [`interrogation_quality.md`](references/interrogation_quality.md) when the caller asks to evaluate interrogation contract quality.

If caller intent is unclear, assume default contract only and state the assumption.
If requested interrogation needs fall outside this interface, state the unsupported need and hand off to the appropriate skill.

## Return

Always return selected package-local paths followed by loaded contents in fenced code blocks.

Default path:
- `src/interface/interrogation/references/interrogation_contract.md`

Optional paths:
- `src/interface/interrogation/references/interrogation_checklist.md`
- `src/interface/interrogation/references/interrogation_quality.md`

---

## Interrogation Contract Shape (`references/interrogation_contract.md`)

```text
# Interrogation Contract: <artifact-name>

Lenses:
- <persona-name>: <role description used to frame questions>
- <persona-name>: <role description used to frame questions>

Base Criteria (always applied):
- Internal consistency: no contradictions within the artifact
- Clarity: precise language, unambiguous intent

Evaluation Questions (prioritized by expected impact if unaddressed):
1. As a <role>, I want to know <question> so that <justification>.
2. As a <role>, I want to know <question> so that <justification>.
N. As a <role>, I want to know <question> so that <justification>.

Source Criteria:
- <spec ID or source ref>: maps to which question(s) above (e.g., REQ-001 → Q3, Q7)
```

### Question Design Rules

- Each question probes a specific judgment area derived from spec requirements + persona criteria.
- Avoid binary phrasing. Favor questions that invite nuanced analysis (how, why, to what extent, what trade-offs, under what conditions).
- Include at least one question per persona lens.
- Prioritize: P1-equivalent areas first (structural/spec violations), then P2/P3 (quality/clarity).
- Base criteria (consistency, clarity) should appear as early questions when the artifact's quality is a review target.
- Each question should map to at least one spec requirement or persona criterion.

### Contract Rules

- Questions are **evaluable by an LLM** — they ask for reasoning anchored in the artifact content + loaded criteria, not external research.
- The number of questions should be bounded (aim for 8–15) to keep execution tractable.
- If a persona adds no meaningful perspective beyond another already-loaded lens, do not create a separate section.
- Source criteria mapping is required: every question must trace back to at least one spec ID or persona criterion so findings can cite sources.

## Next Steps

- `transform/evaluate` (execution) — evaluate the artifact against each question, answer with reasoning, and produce severity-scored output via `assets/severity.md` + `assets/template_report.md`.
- `interface/plan` — create gap-closing work from unanswered or low-confidence questions.
- `transform/check` — validate that a revised artifact addresses prior interrogation findings.
- `output/annotate` — add inline annotations for tracking findings (NOTE) and fixes (TODO).

## Minimal Example

**Prompt:** "Use the interrogation interface for evaluating auth-module design against SPEC-auth using security and adversarial lenses."

**Return:**

file_path: src/interface/interrogation/references/interrogation_contract.md
```markdown
# Interrogation Contract: auth-module

Lenses:
- security: Security analyst evaluating authentication and data protection
- adversarial: Attacker probing for edge cases, abuse patterns, and hidden failure modes

Base Criteria (always applied):
- Internal consistency: no contradictions within the artifact
- Clarity: precise language, unambiguous intent

Evaluation Questions (prioritized by expected impact if unaddressed):
1. As a security analyst, I want to know what password storage mechanisms are specified and whether they align with current NIST guidelines so that credential compromise risk is minimized.
2. As an adversarial attacker, I want to know under what conditions rate limiting could be bypassed or manipulated so that abuse surfaces can be identified early.
3. As a security analyst, I want to know how session state is managed across auth flows so that session fixation and hijacking vectors are covered.
4. As an adversarial attacker, I want to know what error messages are revealed during failed authentication attempts so that information leakage paths are identified.
5. As a reviewer, I want to know whether the spec defines consistent terminology for auth states (e.g., authenticated, verified, logged in) so that implementation ambiguity is eliminated.

Source Criteria:
- REQ-001 (hashing algorithm): maps to Q1
- REQ-003 (rate limiting): maps to Q2
- ACC-002 (session security): maps to Q3
- ACC-003 (error handling): maps to Q4
- Internal consistency: maps to Q5
```
