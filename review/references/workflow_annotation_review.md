# Workflow: Annotation Review

Discovers and incorporates REVIEW(<id>) annotations as targeted review criteria.

## Context
Receives pre-built context from the router: target, specs, lenses. Annotation discovery is the primary focus.

## Steps

### 1. Discover REVIEW Annotations
Scan the target artifact and its surrounding directory for `REVIEW(<id>)` annotations.
Use lightweight pattern matching — only match `REVIEW(<id>)` format.
Do not import the full annotation format from the annotate skill.

### 2. Incorporate Annotations as Criteria
For each discovered annotation:
- Extract the annotation ID and message
- Treat the message as a targeted review criterion
- Add to the review criteria alongside spec and lens criteria

### 3. Compare Target Against All Criteria
- Spec criteria (from loaded spec_ file)
- Lens criteria (from loaded lenses)
- Annotation criteria (from discovered REVIEW annotations)

### 4. Categorize Findings by Severity
Use the severity scale defined in `assets/severity.md`.

### 5. Report Findings
Use template: `assets/template_report.md`
- Note which findings come from annotations vs. spec/lens criteria
- Include annotation ID in finding references

## Patterns
- **Finding format**: `P<n> - <issue> (source: <reference>, annotation: REVIEW(<id>))`
- Annotation findings are prioritized — they represent explicit reviewer concerns

## Constraints
1. Same as workflow_generic.md
2. Lightweight pattern matching only (REVIEW(<id>) format)
3. Do not import full annotation format from annotate skill
## Output
Review report using `assets/template_report.md` with findings categorized P1-P5, annotation references included.
