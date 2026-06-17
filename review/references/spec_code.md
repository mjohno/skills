# Spec: Code

This spec defines criteria for reviewing code, source files, tests, and diffs.

## Additional Criteria

### Implementation Correctness
1. Implementation matches intent and requirements
2. Code is correct, coherent, and handles edge cases
3. No unintended side effects or regressions
4. Change is minimal and readable

### Test Coverage
1. Tests cover the change
2. Tests still pass
3. Test assertions are meaningful (not just exercising code paths)
4. Tests cover edge cases

### Architecture Fit
1. Changes align with existing codebase patterns
2. No architecture drift or tech debt introduced
3. Consistent naming and patterns with surrounding code

### Quality
1. No obvious bugs or fragile code
2. Opportunities to simplify or consolidate identified
3. No unnecessary complexity or duplicate structure
