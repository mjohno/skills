---
name: questionnaire
description: Return the canonical layout and question quality criteria for producing questionnaire contracts.
metadata:
  type: interface
  category: interface
---

# questionnaire

Goal: Provide the contract shape and criteria that define good questionnaire questions.
Non-Goals: Do not execute questionnaires, discover specs or personas, produce severity reports, remediate findings, or actually define questions for a specific artifact. Discovery and question-writing are upstream tasks performed by skills that consume this interface.
Use-When: Another skill needs the questionnaire contract template and quality criteria before producing evaluation questions for an artifact.

## References

Return selected package-local files in fenced code blocks. If caller intent is unclear, assume the default reference only.

| Reference | When |
|---|---|
| `references/questionnaire_contract.md` | Default — all cases |
| `references/questionnaire_checklist.md` | Caller asks to check contract conformance |
| `references/questionnaire_quality.md` | Caller asks to evaluate contract quality |

If requested needs fall outside this interface, state the unsupported need and hand off.

## Next Steps

- `transform/evaluate` (execution) — evaluate the artifact against each question, answer with reasoning, and produce severity-scored output via `assets/severity.md` + `assets/template_report.md`.
- `interface/plan` — create gap-closing work from unanswered or low-confidence questions.
- `transform/check` — validate that a revised artifact addresses prior questionnaire findings.
- `output/annotate` — add inline annotations for tracking findings (NOTE) and fixes (TODO).

## Minimal Example

**Prompt:** "Use the questionnaire interface for evaluating auth-module design against SPEC-auth using security and adversarial lenses."

**Return:**

file_path: src/interface/questionnaire/references/questionnaire_contract.md
```markdown
[contract contents: design rules + contract rules]
```

file_path: src/interface/questionnaire/assets/questionnaire_template.md
```markdown
[template contents]
```

**Instantiated example:** `QUESTIONNAIRE-auth-module` with security + adversarial lenses, 5 questions mapped to REQ-001, REQ-003, ACC-002, ACC-003, and internal consistency.
