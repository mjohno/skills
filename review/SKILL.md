---
name: review
description: Centralized review skill. Detects artifact type, discovers specs, suggests lenses, and routes to the appropriate review workflow. Use when reviewing any artifact against its specifications.
metadata:
  type: router
---

# Review

Goal: Detect artifact type, build review context (spec + lens + annotations + optional diff refs), and route to the appropriate review workflow.
Non-Goals: Execute review logic (that's the workflow's job), manage task packets, perform remediation, or treat personas/lenses as workflows.

## Use When
- Asked to review any artifact against specifications.
- Asked to compare an output against a spec or goal.
- Asked to audit a document, code, skill, or prose.

## Inputs
1. **Target** — the artifact to review (file path or content)
2. **Lens hints** — any named lenses the user specifies (e.g., "from a security perspective")
3. **Workflow hints** — named workflow override: generic, spec, annotation, or diff
4. **Custom specs** — any user-provided spec files
5. **Diff refs** — optional base/head refs for diff review

## Workflow

### Gather Context
1. **Build Context from Input** — Parse input to extract target, lens hints, workflow hints, custom specs, and diff refs.
2. **Detect Artifact Type** — Classify as prd, rfc, code, skill, prose, or generic. User override always wins.
3. **Discover Specs** — Load `spec_<type>.md` for the detected type. User-provided specs override built-in.
4. **Suggest Lenses** — Always apply `lens_generic.md`. If user specifies domain/persona lenses, load `lens_*.md` (for example, `lens_adversarial.md` for adversarial/skeptical review). Suggest relevant lenses based on the artifact's content and context. Avoid hard-mapping artifact types to specific lenses.
5. **Discover Annotations** — Scan for `REVIEW(<id>)` annotations. Each becomes a targeted criterion.

### Route the Request
- **Diff review** → `references/workflow_diff_review.md` when the user asks for PR/branch/diff/change review, provides base/head refs, or asks to compare base branch and HEAD.
- **Annotation review** → `references/workflow_annotation_review.md` when the user explicitly asks to review `REVIEW(<id>)` annotations.
- **Spec review** → `references/workflow_spec_review.md` when the user provides custom specs or explicitly asks for spec review.
- **Generic review** → `references/workflow_generic.md` by default, including lens-only reviews.
- **Workflow override** → Only honor explicit overrides to generic, spec, annotation, or diff. Treat adversarial as `lens_adversarial.md`, not as a workflow.
- **Insufficient input** → Ask user with recommendations (suggest candidates, specs, lenses).

### Execute the Workflow
1. **Build Context** — Pass target, specs, lenses, annotation hints, diff refs, and routed workflow file.
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

### Example 3
**Prompt:** Review the diff from main to HEAD with the adversarial lens.
**Decisions:** Detect diff review, collect `git diff main...HEAD`, load `lens_generic.md` and `lens_adversarial.md`, include any supplied spec, route to workflow_diff_review.md.
**Outcome:** Diff-scoped review report with changed files and findings categorized P1-P5.
