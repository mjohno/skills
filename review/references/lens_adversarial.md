# Lens: Adversarial

Persona/lens for skeptical review. Apply this lens when the user asks for an adversarial, hostile, red-team, skeptical, or assumption-challenging review.

This is not a workflow or orchestration mode. It can be applied by generic, spec, diff, annotation, or council-style review execution.

## Criteria

### 1. Challenge Assumptions
- Identify unstated assumptions the artifact depends on.
- Check whether those assumptions are justified by the spec, code, data, or surrounding context.
- Flag places where the artifact appears correct only under narrow or undocumented conditions.

### 2. Find Abuse and Misuse Cases
- Look for ways users, callers, attackers, or operators could misuse the behavior.
- Check whether invalid, malicious, concurrent, partial, or repeated inputs are handled safely.
- Flag places where happy-path behavior hides unsafe edge cases.

### 3. Probe Edge Cases and Failure Modes
- Test boundaries, empty states, missing data, malformed data, ordering issues, and rollback/retry paths.
- Look for race conditions, resource leaks, data loss, silent failure, and inconsistent state.
- Check whether failure handling preserves user trust and system invariants.

### 4. Attack Spec Loopholes
- Look for implementations that satisfy the wording but violate the likely intent.
- Identify ambiguous requirements that permit risky interpretations.
- Flag missing acceptance criteria that would allow a defective result to pass review.

### 5. Resist False Confidence
- Treat green tests, plausible prose, or clean structure as insufficient by themselves.
- Check whether evidence actually supports the claim being made.
- Flag untested claims, misleading examples, and conclusions that overreach the evidence.

## Output Guidance
- Prefer concrete failure scenarios over abstract skepticism.
- Cite the assumption, loophole, or failure path that creates the risk.
- Separate confirmed defects from plausible risks that need verification.
