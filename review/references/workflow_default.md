# General Review Workflow

## Context
Compare an output against a spec to find gaps and report findings.

## Steps

### 1. Identify the output to review
   - Extract the artifact, document, or deliverable to be reviewed

### 2. Identify the spec to compare against
   - If the spec is a skill → load that skill's workflow file
   - If the spec is an artifact → use that artifact as the spec
   - If the spec is implicit (e.g. "review the PRD") → find the skill that
     created it and load its defining workflow

### 3. Compare output against spec
   - Go through the spec systematically
   - Check each requirement, constraint, and pattern
   - Note where the output matches, deviates, or omits

### 4. Categorize findings by severity
   - **P1**: Violates the spec (missing required elements, contradictions)
   - **P2-P5**: Could be improved (quality, completeness, clarity)

### 5. Report findings
   - Summary of overall compliance
   - List of findings with source references
   - Specific, recommended changes needed

## Patterns
- Finding format: `P<n> - <issue> (source: <reference>)`
- Report structure: sources → targets → summary → findings (P1-P5) → recommended changes
- Compare section-by-section, not holistically

## Constraints
- Be specific: cite exact spec requirements
- Be actionable: each finding should suggest a concrete change
- Don't introduce new requirements beyond the spec
- Report both what's missing AND what's wrong

## Output
Use template: `assets/template_report.md`
