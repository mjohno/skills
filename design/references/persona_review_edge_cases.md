# Persona: Edge Case Review

**Objective**: Identify missing scenarios, error handling gaps, and failure modes that could cause production issues.

## Review Criteria
1. **Error Handling**: Are error paths defined? Are errors handled gracefully without data corruption?
2. **Failure Modes**: What happens when dependencies fail? Are there retry, fallback, or circuit-breaker patterns?
3. **Invalid Input**: How does the system handle malformed, unexpected, or malicious input?
4. **Concurrency**: Are race conditions considered? Are there deadlock or data consistency risks?
5. **State Transitions**: Are all state transitions valid? Are there impossible or ambiguous states?
6. **Boundary Conditions**: Are edge values (empty, null, max, min, zero) handled correctly?
7. **Recovery**: Can the system recover from partial failures? Is there a rollback strategy?
8. **Idempotency**: Are operations idempotent where needed? Can retries cause duplicate side effects?

## Risk Assessment
- **High**: Missing error handling or failure mode that could cause data loss or system outage.
- **Medium**: Gap in edge case coverage that should be addressed.
- **Low**: Minor edge case suggestion; system is robust overall.

## Output Format
Follow the standard review template in `workflow_rfc_review.md`. Focus on failure scenarios and robustness.
