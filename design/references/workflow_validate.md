# Workflow: Validate

## Context
Programmatically and semantically verify that a design artifact meets mandatory quality standards. This is a general validation workflow that accepts any source workflow path.

## Steps

### 1. Identify Target and Source
- Extract the target artifact (the document to validate)
- Extract the source specification (workflow file path to validate against)
- If either is unclear, ask the user to clarify

### 2. Load Source Specification
- Load the source workflow file specified by the user or routed from the router
- Load the associated template from `assets/` if applicable

### 3. Run Programmatic Validation
Execute the validation script specified by the user or routed from the router.
- PRD → `python scripts/validate_prd.py <target_file>`
- Parse the JSON output for heuristic failures

### 4. Perform Semantic Audit
Perform a deep dive to verify:
- **Structural Integrity**: Adherence to the template structure
- **Source Compliance**: Every requirement in the source workflow is satisfied
- **Cross-Reference Consistency**: Internal references are valid and consistent
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
