# Mode: Review

This mode is used to review an existing RFC from a domain-specific perspective.

## Workflow

### 1. Ingest
- Read the target `RFC-NNN-<name>.md` file.
- Accept the review persona name from the orchestrator.
- Load the corresponding persona from `references/` (e.g., `persona_review_security.md`).

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
