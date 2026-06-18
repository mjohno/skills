# Spec: PRD

This spec defines what makes a PRD correct.

## Source References
- **PRD skill**: `prd/SKILL.md`

## Additional Criteria

### Structural Criteria
1. Executive Summary present and concise
2. Strategic Goals section with SMART table and detailed descriptions
3. User Stories section with table and numbered detail
4. Acceptance Criteria section with Gherkin scenarios

### Content Criteria

#### SMART Compliance
- Each strategic goal must be Specific, Measurable, Achievable, Relevant, and Time-bound

#### User Story Syntax
- Every story must follow: `As a [role], I want [action], so that [value]`

#### Gherkin Syntax
- All acceptance criteria must use Given/When/Then
- Must describe observable outcomes

#### Edge Case Analysis
- Gherkin scenarios should cover: invalid input, out-of-state conditions, error paths

#### Strategic Alignment
- The "Value" in User Stories must align directly with defined Strategic Goals

#### Logical Consistency
- No contradictions between requirements
- No gaps between user stories and acceptance criteria

#### Ambiguity Detection
- Flag vague language: fast, easy, robust, efficient, seamless, optimized, user-friendly
