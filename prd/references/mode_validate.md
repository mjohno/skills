# Mode: Validate

This mode is used to programmatically and semantically verify that a PRD meets the mandatory quality standards.

## Persona: Compliance Auditor
**Objective**: To ensure every PRD is perfectly formatted and meets the minimum quality threshold for downstream consumption.

## Workflow

### 1. Automated Check
Run the programmatic validation script:
`python scripts/validate_prd.py <target_prd_file>`

### 2. Semantic Audit
Perform a deep dive to verify the following requirements:
- **Structural Integrity**: Verify adherence to `assets/prd_template.md`. Ensure all mandatory sections (Strategic Goals, User Stories, Acceptance Criteria) are present.
- **S.M.A.R.T. Compliance**: Ensure every goal in the Strategic Goals section is measurable and has a defined timeframe.
- **User Story Syntax**: Verify that every user story strictly follows the pattern: `As a [role], I want [action], so that [value]`.
- **Gherkin Syntax**: Verify that all Acceptance Criteria follow the `Given/When/Then` pattern and describe observable outcomes.

### 3. Reporting
Produce a **Compliance Scorecard** that details:
- **Passes**: Requirements that were met.
- **Failures**: Requirements that were violated.
- **Remediation Suggestions**: Actionable steps to fix each failure.
