# Workflow: RFC Review

## Context
Review an existing RFC from a domain-specific perspective. Load a persona to guide the review criteria and depth.

## Inputs
1. Target RFC file (`RFC-NNN-<name>.md`)
2. Review persona name (e.g., `security`, `architecture`, `scalability`) — defaults to System Architect if not specified
3. Source workflow path (for reference): `references/workflow_rfc.md`

## Steps

### 1. Ingest
- Read the target RFC file (`RFC-NNN-<name>.md`)
- Accept the review persona name from the orchestrator
- Load the corresponding persona from `references/` (e.g., `persona_review_security.md`)

### 2. Execute Review (Persona-Guided)
Apply the loaded persona's focused lens to the RFC. Each persona defines its own review criteria and depth.

### 3. Output Review Round
Append the review findings to the RFC under the `## Review Comments` section as a new round:

```markdown
### Review Round [N]: [Persona Name]
- **Risk Level**: High / Medium / Low
- **Findings**:
  - [ ] **[Issue Title]** (High/Medium/Low) — [Description] — [Suggestion]
- **Overall Assessment**: [2-3 sentence summary]
```

- **Risk Level**: Overall risk assessment of the RFC from this persona's perspective (High / Medium / Low).
- **Findings**: Each finding is triaged by severity (High / Medium / Low) and includes a `[ ]` checkbox for resolution tracking.
- **Overall Assessment**: A concise 2-3 sentence summary of the review.

### 4. Append, Don't Replace
- If review rounds already exist, increment the round number and append.
- Never overwrite existing review rounds.

### 5. Output
- The updated RFC file with the new review round appended.
- The orchestrator may invoke additional review personas as needed.

## Patterns
- **Persona-Guided**: Each persona defines its own review criteria and depth
- **Append-Only**: Review rounds are appended, never replaced
- **Severity Triage**: Every finding is triaged as High/Medium/Low
- **Resolution Tracking**: Checkbox format for tracking which findings are resolved

## Constraints
1. Never overwrite existing review rounds
2. Always increment the round number
3. Include `[ ]` checkbox for each finding
4. Risk Level is an overall assessment, not per-finding
5. Overall Assessment must be 2-3 sentences

## Outputs
- Updated RFC file with new review round appended
- Review round with Risk Level, Findings (with checkboxes), and Overall Assessment
