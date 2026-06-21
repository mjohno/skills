---
name: review
description: Centralized review skill. Detects artifact type, discovers specs, suggests lenses, and routes to the appropriate review workflow. Use when reviewing any artifact against its specifications.
metadata:
  category: transform
---

# review

Goal: Detect artifact type, build review context (spec + lens + annotations + optional diff refs), and route to the appropriate review workflow.
Non-Goals: Execute review logic (that's the workflow's job), manage task packets, perform remediation, or treat personas/lenses as workflows.
Use-When: You need to review any artifact against its specifications.

## 0. Prerequisites
- Target artifact to review (file path or content)
- Specification to review against (optional; built-in specs used if none provided)

## 1. Inputs
- Target artifact from prompt or file path
- Lens hints (optional: named lenses like "from a security perspective")
- Workflow hints (optional: generic, spec, annotation, or diff)
- Custom specs (optional: user-provided spec files)
- Diff refs (optional: base/head refs for diff review)

## 2. Processes
1. **Gather Context**: Parse input to extract target, lens hints, workflow hints, custom specs, and diff refs.
2. **Detect Artifact Type**: Classify as prd, rfc, code, skill, prose, or generic. User override always wins.
3. **Discover Specs**: Load `spec_<type>.md` for the detected type. User-provided specs override built-in.
4. **Suggest Lenses**: Always apply `lens_generic.md`. If user specifies domain/persona lenses, load `lens_*.md`. Suggest relevant lenses based on the artifact's content and context.
5. **Discover Annotations**: Scan for `REVIEW(<id>)` annotations. Each becomes a targeted criterion.
6. **Route the Request**: Route to the appropriate workflow file (see routing table below).
7. **Execute the Workflow**: Pass target, specs, lenses, annotation hints, diff refs, and routed workflow file to the workflow.

**Routing table:**
- Diff review → `references/workflow_diff_review.md` when user asks for PR/branch/diff/change review
- Annotation review → `references/workflow_annotation_review.md` when user explicitly asks to review `REVIEW(<id>)` annotations
- Spec review → `references/workflow_spec_review.md` when user provides custom specs
- Generic review → `references/workflow_generic.md` by default (including lens-only reviews)
- Workflow override → Only honor explicit overrides to generic, spec, annotation, or diff
- Insufficient input → Ask user with recommendations

## 3. Outputs
- Review report via the routed workflow, using `assets/template_report.md`
- Report contains: sources → targets → summary → findings (P1-P5) → recommended changes
- Severity scale: `assets/severity.md`
- Pipeline-style: output to prompt by default; write to file if user specifies output path

## 4. Next Steps
- `comply` — have the `skillz` skill fix identified violations
- `review` — re-review after fixes are applied
- `annotate` — add inline annotations for tracking findings
- `plan` — create a plan to address findings

## 5. Constraints
1. Be specific: cite exact source requirements
2. Be actionable: each finding should suggest a concrete change
3. Don't introduce new requirements beyond the specs
4. Report both what's missing AND what's wrong
5. Do not perform remediation — only comparison and reporting
6. Router builds context; workflows execute comparison and produce reports

## 5. Examples

### Example 1
**Prompt:** Review RFC-001.md from a security perspective.
**Decisions:** Detect artifact type = rfc, load spec_rfc.md, suggest lens_security.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.

### Example 2
**Prompt:** Review the PRD in PRD-001.md.
**Decisions:** Detect artifact type = prd, load spec_prd.md, apply lens_generic.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.

### Example 3
**Prompt:** Review the diff from main to HEAD with the adversarial lens.
**Decisions:** Detect diff review, collect `git diff main...HEAD`, load `lens_generic.md` and `lens_adversarial.md`, include any supplied spec, route to workflow_diff_review.md.
**Outcome:** Diff-scoped review report with changed files and findings categorized P1-P5.
