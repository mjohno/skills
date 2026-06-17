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
Use the router's P1-P5 severity scale (defined in Step 7 of SKILL.md).

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
4. Severity scale: P1-P5
   - **P1**: Violates the spec (missing required elements, contradictions, syntax errors)
   - **P2**: Could be improved (quality, completeness, clarity)
   - **P3**: Minor suggestion (formatting, consistency)
   - **P4**: Cosmetic suggestion
   - **P5**: Nice-to-have suggestion

## Output
Review report using `assets/template_report.md` with findings categorized P1-P5 and spec provenance noted.
