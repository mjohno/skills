---
name: design
description: Route design artifact requests to the appropriate workflow (PRD, RFC, System Design, BRD, RFP). Use when you need to write, review, or validate a design artifact.
metadata:
  type: router
---

# design

Goal: Route design artifact requests to the appropriate workflow and execute the routed workflow.
Non-Goals: Execute implementation, manage deployment, or perform strategic analysis.

## Use When
- You need to write or update a design artifact (PRD, RFC, System Design, BRD, RFP).
- You need to review a design artifact against its workflow specification.
- You need to validate a design artifact against mandatory quality standards.

## Inputs
1. Target artifact (file path or content)
2. Action (write, review, validate)
3. Context (business goals, existing docs, constraints)

## Workflow

### Gather Context
1. Identify the artifact type (PRD, RFC, System Design, BRD, RFP).
2. Identify the action (write, review, validate).
3. Load any provided context (existing docs, business goals, constraints).

### Route the Request
- **PRD + write** → `references/workflow_prd.md`
- **PRD + review** → `references/workflow_prd_review.md`
- **PRD + validate** → `references/workflow_prd_validate.md`
- **RFC + write** → `references/workflow_rfc.md`
- **RFC + review** → `references/workflow_rfc_review.md`
- **RFC + validate** → `references/workflow_rfc_validate.md`
- **System Design + write** → `references/workflow_system_design.md`
- **BRD + write** → `references/workflow_brd.md`
- **RFP + write** → `references/workflow_rfp.md`
- **Default Route:** Ask the user to specify the artifact type and action.

### Execute the Workflow
Follow the execution instructions provided by the routed workflow.
Load referenced templates from `assets/` and scripts from `scripts/`.

## Outputs
- Design artifact (PRD, RFC, System Design, BRD, or RFP) in the appropriate template format.
- Review report with findings categorized by severity.
- Validation scorecard with pass/fail status and remediation suggestions.

## Examples

### Example 1
**Prompt:** Write a PRD for a user authentication feature.
**Decisions:** Route to `workflow_prd.md`. Ingest business context. Produce `PRD.md`.
**Outcome:** Complete PRD with Strategic Goals, User Stories, and Acceptance Criteria.

### Example 2
**Prompt:** Review the PRD in `PRD-001.md`.
**Decisions:** Route to `workflow_prd_review.md`. Load PRD workflow as source specification. Audit for ambiguity, gaps, and consistency.
**Outcome:** Review report with findings categorized as P1-P5.

### Example 3
**Prompt:** Write an RFC for the PRD in `PRD-001-user-auth.md`. This is a general technical RFC.
**Decisions:** Route to `workflow_rfc.md`. Load default persona (`persona_write_system_architect.md`). Ingest PRD, extract User Stories and Acceptance Criteria. Produce RFC with Context, Proposed Solution, Design Decisions, Architecture, Feasibility, Alignment, Open Questions, Decision Log.
**Outcome:**
```
RFC-001-user-auth.md
├── Context (references PRD-001)
├── Proposed Solution
├── Design Decisions (4 entries)
├── Architecture & Data Models
├── Feasibility Assessment
├── Alignment with PRD (7 AC mappings)
├── Open Questions (2 items)
└── Decision Log (summary table + detail entries)
```

### Example 4
**Prompt:** Review RFC-001-user-auth.md from a security perspective.
**Decisions:** Route to `workflow_rfc_review.md`. Load persona (`persona_review_security.md`). Evaluate authN/Z, token handling, data protection.
**Outcome:** Review report with findings categorized by severity.

### Example 5
**Prompt:** Validate RFC-001.md against the RFC workflow specification.
**Decisions:** Route to `workflow_rfc_validate.md`. Load RFC workflow as source. Run programmatic validation.
**Outcome:** Validation scorecard with pass/fail and remediation suggestions.
