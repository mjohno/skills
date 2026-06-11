# Mode: Validate

This mode is used to verify that an RFC meets structural and compliance requirements against its source PRD.

## Purpose
To verify that an RFC is structurally complete, properly aligned with its source PRD, and ready for implementation.

## Workflow

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

### 3. Acceptance Criteria Coverage
- For each PRD Acceptance Criterion, verify there is a corresponding RFC section that addresses it.
- Flag any PRD requirement that has no RFC mapping.

### 4. Decision Log Completeness
- Verify all significant decisions are logged.
- Each decision must have: Decision, Rationale, Alternatives Considered, Author, Status.
- Check for superseded decisions and verify they reference the superseding decision.

### 5. Open Questions Resolution
- Verify that open questions are documented.
- Flag any critical open questions that should be resolved before moving to "Approved."

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
