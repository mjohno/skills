# Workflow: Generic Review

Default review workflow. Compares target against spec + lens criteria and produces a report.

## Context
Receives pre-built context from the router: target, spec, lenses, and annotation hints.

## Steps

### 1. Compare Target Against Spec
Go through the spec criteria systematically:
- **Completeness**: All required elements are present
- **Consistency**: No contradictions or conflicting requirements
- **Correctness**: Requirements are accurate and properly structured
- **Clarity**: Language is unambiguous and well-structured
- **Compliance**: Adherence to standards and conventions

### 2. Apply Lenses
For each loaded lens, apply its criteria on top of the spec:
- Combine spec criteria with lens criteria
- Note where the target matches, deviates, or omits

### 3. Incorporate Annotation Hints
For each discovered `REVIEW(<id>)` annotation:
- Treat the annotation as a targeted review criterion
- Verify the specific concern raised in the annotation

### 4. Categorize Findings by Severity
Use the severity scale defined in `assets/severity.md`.

### 5. Report Findings
Use template: `assets/template_report.md`
- Summary of overall compliance
- List of findings with source references
- Specific, recommended changes needed

## Patterns
- **Finding format**: `P<n> - <issue> (source: <reference>)`
- **Report structure**: sources → targets → summary → findings (P1-P5) → recommended changes
- Compare section-by-section, not holistically

## Constraints
1. Be specific: cite exact source requirements
2. Be actionable: each finding should suggest a concrete change
3. Don't introduce new requirements beyond the specs
4. Report both what's missing AND what's wrong
5. Do not perform remediation — only comparison and reporting
## Outputs
Review report using `assets/template_report.md` with findings categorized P1-P5.
