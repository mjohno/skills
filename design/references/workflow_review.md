# Workflow: Review

## Context
Audit a design artifact against a source specification to find gaps, inconsistencies, and quality issues. This is a general review workflow that accepts any source workflow path.

## Steps

### 1. Identify Target and Source
- Extract the target artifact (the document to review)
- Extract the source specification (workflow file path to review against)
- If either is unclear, ask the user to clarify before proceeding
- Suggested recommendations:
  - For unclear target: "Did you mean the PRD artifact, the RFC, or the codebase?"
  - For unclear sources: "Should I review against `references/workflow_prd.md`, `references/workflow_rfc.md`, or a checklist?"

### 2. Load Source Specification
- Load the source workflow file specified by the user or routed from the router
- Load the associated template from `assets/` if applicable

### 3. Compare Target Against Sources
Go through the source specification systematically:
- **Completeness**: All required elements are present
- **Consistency**: No contradictions or conflicting requirements
- **Correctness**: Requirements are accurate and properly structured
- **Clarity**: Language is unambiguous and well-structured
- **Compliance**: Adherence to standards and conventions (e.g., Gherkin syntax, SMART goals)

### 4. Categorize Findings by Severity
- **P1**: Violates the source specification (missing required elements, contradictions, syntax errors)
- **P2**: Could be improved (quality, completeness, clarity)
- **P3-P5**: Minor suggestions (formatting, consistency, style)

### 5. Report Findings
- Summary of overall compliance
- List of findings with source references
- Specific, recommended changes needed

## Patterns
- **Finding format**: `P<n> - <issue> (source: <reference>)`
- **Report structure**: sources → targets → summary → findings (P1-P5) → recommended changes
- **Compare section-by-section**, not holistically

## Constraints
1. Be specific: cite exact source requirements
2. Be actionable: each finding should suggest a concrete change
3. Don't introduce new requirements beyond the sources
4. Report both what's missing AND what's wrong
5. Do not perform remediation — only comparison and reporting

## Outputs
- Review report with findings categorized by severity (P1-P5)
- Summary of overall compliance
- Specific, recommended changes for each finding
