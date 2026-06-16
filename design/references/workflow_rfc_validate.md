# Workflow: RFC Validation

## Context
Verify that an RFC meets structural and compliance requirements against its source PRD. Produce a human-readable risk scorecard.

## Steps

### 1. Structural Integrity Check
Verify that the RFC contains all required sections:
- [ ] Context
- [ ] Proposed Solution
- [ ] Design Decisions
- [ ] Architecture & Data Models
- [ ] Feasibility Assessment
- [ ] Alignment with PRD
- [ ] Open Questions
- [ ] Decision Log (with summary table)

### 2. PRD Cross-Reference Check
- Verify that the Context section references a valid PRD.
- Ensure the technical problem is clearly anchored to (not repeating) the PRD's user story.
- Confirm the problem is narrowed down to a specific technical challenge.
- If no PRD is provided, note this as a structural concern.

### 3. Acceptance Criteria Coverage
- For each PRD Acceptance Criterion, verify there is a corresponding RFC section that addresses it.
- Flag any PRD requirement that has no RFC mapping.
- If no PRD is provided, note this as a validation concern.

### 4. Decision Log Completeness
- Verify all significant decisions are logged.
- Each decision must have: Decision, Rationale, Alternatives Considered, Author, Status.
- Check for superseded decisions and verify they reference the superseding decision.
- Verify the Decision Log includes a summary table at the top.

### 5. Open Questions Resolution
- Verify that open questions are documented.
- Flag any critical open questions that should be resolved before moving to "Approved."
- Check that each open question has a clear owner or resolution path.

### 6. Output: Risk Scorecard
Produce a **human-readable risk scorecard**:

```
## Validation Risk Scorecard

| Check | Result | Risk Level |
| :--- | :--- | :--- |
| Structural Integrity | [Pass / Partial / Fail] | [High / Medium / Low] |
| PRD Cross-Reference | [Pass / Partial / Fail] | [High / Medium / Low] |
| AC Coverage | [Pass / Partial / Fail] | [High / Medium / Low] |
| Decision Log Completeness | [Pass / Partial / Fail] | [High / Medium / Low] |
| Open Questions | [Pass / Partial / Fail] | [High / Medium / Low] |
| **Overall Risk** | | **[High / Medium / Low]** |

### Notes
[Brief summary of findings and recommended actions.]
```

## Patterns
- **Structured Validation**: Each check produces a Pass/Partial/Fail result
- **Risk Scorecard**: Human-readable summary with per-check and overall risk levels
- **Actionable Notes**: Each scorecard includes a summary of findings and recommended actions

## Constraints
1. All checks must produce a Pass/Partial/Fail result
2. Each check must have an associated risk level
3. Overall Risk is derived from the individual check results
4. Notes must provide actionable recommendations

## Outputs
- Validation Risk Scorecard with per-check results and overall risk level
- Notes with findings summary and recommended actions
