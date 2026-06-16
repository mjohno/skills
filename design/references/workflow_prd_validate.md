# Workflow: PRD Validate

## Context
Programmatically and semantically verify that a PRD meets mandatory quality standards. This workflow loads the PRD workflow specification as the source and runs both programmatic and semantic checks.

## Steps

### 1. Identify Target
- Extract the PRD file to validate
- If unclear, ask the user to clarify before proceeding

### 2. Load Source Specification
- Load `references/workflow_prd.md` as the source specification
- Load `assets/prd_template.md` for structural reference
- Load `assets/user_story_template.md` for story/AC pattern reference

### 3. Run Programmatic Validation
Execute the validation script:
`python scripts/validate_prd.py <target_prd_file>`

Parse the JSON output for:
- **Passed**: Requirements that were met
- **Heuristics**: Programmatic findings (missing sections, vague words, syntax errors)
- **Semantic Pending**: Items requiring human judgment

### 4. Perform Semantic Audit
Perform a deep dive to verify:
- **Structural Integrity**: Adherence to `assets/prd_template.md` — all mandatory sections present
- **SMART Compliance**: Every goal in Strategic Goals is measurable and has a defined timeframe
- **User Story Syntax**: Every user story strictly follows: `As a [role], I want [action], so that [value]`
- **Gherkin Syntax**: All Acceptance Criteria follow Given/When/Then and describe observable outcomes
- **Cross-Reference Consistency**: User Story IDs in the table match the numbered detail sections; AC sections reference correct story IDs
- **Completeness**: No required sections or elements are missing

### 5. Produce Validation Scorecard
Report:
- **Passes**: Requirements that were met
- **Failures**: Requirements that were violated
- **Semantic Pending**: Items that require human judgment
- **Remediation Suggestions**: Actionable steps to fix each failure

## Patterns
- **Scorecard format**: Pass/Fail for each requirement
- **Semantic items**: Clearly marked as requiring human review
- **Remediation**: Specific, actionable, tied to source requirement

## Constraints
1. Programmatic checks are deterministic (pass/fail)
2. Semantic checks are marked as pending (require human judgment)
3. Do not perform remediation — only verification and reporting
4. Cite exact source requirements for each finding

## Outputs
- Validation scorecard with pass/fail status
- List of semantic items pending human review
- Remediation suggestions for each failure
