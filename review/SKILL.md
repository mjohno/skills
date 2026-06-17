---
name: review
description: Centralized review skill. Detects artifact type, discovers specs, suggests lenses, and routes to the appropriate review workflow. Use when reviewing any artifact against its specifications.
metadata:
  type: router
---

# Review

Goal: Detect artifact type, build review context (spec + lens), and route to the appropriate review workflow.
Non-Goals: Execute review logic (that's the workflow's job), manage task packets, or perform remediation.

## Use When
- Asked to review any artifact against specifications.
- Asked to compare an output against a spec or goal.
- Asked to audit a document, code, skill, or prose.

## Inputs
1. **Target** — the artifact to review (file path or content)
2. **Lens hints** — any named lenses the user specifies (e.g., "from a security perspective")
3. **Workflow hints** — any named workflow overrides (e.g., "using spec_review")
4. **Custom specs** — any user-provided spec files

## Workflow

### Gather Context
1. **Build Context from Input** — Parse input to extract target, lens hints, workflow hints, custom specs.
2. **Detect Artifact Type** — Classify as prd, rfc, code, skill, prose, or generic. User override always wins.
3. **Discover Specs** — Load `spec_<type>.md` for the detected type. User-provided specs override built-in.
4. **Suggest Lenses** — Always apply `lens_generic.md`. If user specifies domain lenses, load `lens_*.md`. Suggest RFC → system_architect + security, Code → security.
5. **Discover Annotations** — Scan for `REVIEW(<id>)` annotations. Each becomes a targeted criterion.

### Route the Request
- **Annotation review** → `references/workflow_annotation_review.md`
- **Custom specs** → `references/workflow_spec_review.md`
- **User specifies workflow** → `references/workflow_<name>.md`
- **Default Route:** → `references/workflow_generic.md`
- **Insufficient input** → Ask user with recommendations (suggest candidates, specs, lenses).

### Execute the Workflow
1. **Build Context** — Pass target, spec, lenses, annotation hints, and routed workflow file.
2. **Follow Workflow** — Read and follow the steps in the routed workflow file.

## Outputs
- Review report via the routed workflow, using `assets/template_report.md`
- Report contains: sources → targets → summary → findings (P1-P5) → recommended changes
- Severity scale: `assets/severity.md`

## Constraints
1. Be specific: cite exact source requirements
2. Be actionable: each finding should suggest a concrete change
3. Don't introduce new requirements beyond the specs
4. Report both what's missing AND what's wrong
5. Do not perform remediation — only comparison and reporting
6. Router builds context; workflows execute comparison and produce reports

## Examples

### Example 1
**Prompt:** Review RFC-001.md from a security perspective.
**Decisions:** Detect artifact type = rfc, load spec_rfc.md, suggest lens_security.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.

### Example 2
**Prompt:** Review the PRD in PRD-001.md.
**Decisions:** Detect artifact type = prd, load spec_prd.md, apply lens_generic.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.
