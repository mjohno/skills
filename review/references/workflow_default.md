# General Review Workflow

## Context
Compare a target against sources to find gaps and report findings.

## Steps

### 1. Identify the target
   - Extract the object that needs review (artifact, document, deliverable)

### 2. Identify the sources
   - Extract the materials to review against (spec, standard, checklist, workflow)

### 3. Clarify ambiguous inputs
   - If the target or sources are unclear → ask the user to clarify before proceeding
   - Offer suggested recommendations:
     - For an unclear target: suggest likely candidates (e.g., "Did you mean the PRD artifact, or the codebase?")
     - For unclear sources: suggest likely candidates (e.g., "Should I review against the design skill's workflow, the PRD spec, or a checklist?")

### 4. Compare target against sources
   - Go through the sources systematically:
     - **Completeness**: All required elements are present
     - **Consistency**: No contradictions or conflicting requirements
     - **Correctness**: Requirements are accurate and properly implemented
     - **Clarity**: Language is unambiguous and well-structured
     - **Compliance**: Adherence to standards and conventions
   - Note where the target matches, deviates, or omits

### 5. Categorize findings by severity
   - **P1**: Violates the sources (missing required elements, contradictions)
   - **P2-P5**: Could be improved (quality, completeness, clarity)

### 6. Report findings
   - Summary of overall compliance
   - List of findings with source references
   - Specific, recommended changes needed

## Patterns
- Finding format: `P<n> - <issue> (source: <reference>)`
- Report structure: sources → targets → summary → findings (P1-P5) → recommended changes
- Compare section-by-section, not holistically

## Constraints
- Be specific: cite exact source requirements
- Be actionable: each finding should suggest a concrete change
- Don't introduce new requirements beyond the sources
- Report both what's missing AND what's wrong

## Output
Use template: `assets/template_report.md`
