---
name: design
description: Route design artifact requests to the appropriate workflow (PRD, RFC). Use when you need to write, review, or validate a design artifact.
metadata:
  type: router
---

# design

Goal: Route design artifact requests to the appropriate workflow and execute the routed workflow.
Non-Goals: Execute implementation, manage deployment, or perform strategic analysis.

## Use When
- You need to write or update a design artifact (PRD, RFC).
- You need to review a design artifact against its workflow specification.
- You need to validate a design artifact against mandatory quality standards.

## Inputs
1. Target artifact (file path or content)
2. Action (write, review, validate)
3. Context (business goals, existing docs, constraints)

## Workflow

### Gather Context
1. Identify the artifact type (PRD, RFC).
2. Identify the action (write, review, validate).
3. Load any provided context (existing docs, business goals, constraints).

### Route the Request
- **PRD + write/create** → `references/workflow_prd.md`
- **PRD + review** → `references/workflow_prd_review.md`
- **PRD + validate** → `references/workflow_prd_validate.md`
- **RFC + write/create** → `references/workflow_rfc.md`
- **RFC + review** → `references/workflow_rfc_review.md`
- **RFC + validate** → `references/workflow_rfc_validate.md`
- **General review** → `references/workflow_review.md`
- **General validate** → `references/workflow_validate.md`
- **Default Route:** Ask the user to specify the artifact type (PRD/RFC) and action (write/create/review/validate).

### Execute the Workflow
Follow the execution instructions provided by the routed workflow.
Load referenced templates from `assets/` and scripts from `scripts/`.
Load referenced personas from `references/`.

## Outputs
- Design artifact (PRD or RFC) in the appropriate template format.
- Review report with findings categorized by severity.
- Validation scorecard with pass/fail status and remediation suggestions.

## Examples

### Example 1
**Prompt:** Write a PRD for a user authentication feature.
**Decisions:** Route to `workflow_prd.md`. Ingest business context. Produce `PRD.md`.
**Outcome:** Complete PRD with Strategic Goals, User Stories, and Acceptance Criteria.

### Example 2
**Prompt:** Review the PRD in `PRD-001.md`.
**Decisions:** Route to `workflow_prd_review.md`. Load PRD workflow as source specification. Compare the PRD against the workflow requirements section by section.
**Outcome:** Review report with findings categorized by severity.

### Example 3
**Prompt:** Write an RFC for the PRD in `PRD-001-user-auth.md`. This is a general technical RFC.
**Decisions:** Route to `workflow_rfc.md`. Ingest PRD, extract User Stories and Acceptance Criteria. Apply system architect persona to shape design focus. Produce RFC document with all mandatory sections.
**Outcome:** Complete RFC document with Context, Proposed Solution, Design Decisions, Architecture, Feasibility, Alignment with PRD, Open Questions, and Decision Log.

### Example 4
**Prompt:** Review RFC-001-user-auth.md from a security perspective.
**Decisions:** Route to `workflow_rfc_review.md`. Load persona (`persona_review_security.md`). Evaluate authN/Z, token handling, data protection.
**Outcome:** Review report with findings categorized by severity.

### Example 5
**Prompt:** Validate RFC-001.md against the RFC workflow specification.
**Decisions:** Route to `workflow_rfc_validate.md`. Load RFC workflow as source specification. Run structural and semantic validation checks.
**Outcome:** Validation scorecard with pass/fail results and remediation suggestions.
