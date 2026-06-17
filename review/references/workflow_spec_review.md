# Workflow: Spec Review

Spec-focused review. User-specified specs override built-in specs.

## Context
Receives pre-built context from the router: target, user-specified specs, lenses, and annotation hints.

## Steps

### 1. Load User-Specified Specs
Use the user-provided spec files instead of built-in specs.
If user-provided specs are insufficient, fall back to built-in specs for the artifact type.

### 2. Compare Target Against Specs
Same process as workflow_generic.md:
- Go through spec criteria systematically
- Apply loaded lenses
- Incorporate annotation hints

### 3. Categorize Findings by Severity
Use the severity scale defined in `assets/severity.md`.

### 4. Report Findings
Use template: `assets/template_report.md`
- Note which findings come from user-specified specs vs. built-in fallbacks

## Patterns
- Same as workflow_generic.md
- Highlight spec provenance in findings (user-specified vs. built-in)

## Constraints
1. Same as workflow_generic.md
2. Prioritize user-specified specs over built-in specs
3. Note when built-in specs are used as fallback
## Output
Review report using `assets/template_report.md` with findings categorized P1-P5 and spec provenance noted.
