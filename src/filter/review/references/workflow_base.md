# Workflow: Base Review Logic

Shared comparison and reporting logic used by all review workflows. Each concrete workflow (diff, generic, spec, annotation) wraps this base with its unique concerns.

## Steps

### 1. Compare Target Against Spec
Go through the spec criteria systematically:
- **Completeness**: All required elements are present
- **Consistency**: No contradictions or conflicting requirements
- **Correctness**: Requirements are accurate and properly structured
- **Clarity**: Language is unambiguous and well-structured
- **Conciseness**: Avoid unnecessary verbosity or redundancy
- **Compliance**: Adherence to standards and conventions
- **Simplicity**: Avoid unnecessary complexity or over-engineering

### 2. Apply Lenses
For each loaded lens, apply its criteria on top of the spec:
- Combine spec criteria with lens criteria
- Note where the target matches, deviates, or omits

### 3. Categorize Findings by Severity
Use the severity scale defined in `assets/severity.md`.

### 4. Report Findings
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
