# Workflow: PRD

## Context
Create a comprehensive Product Requirement Document (PRD) from high-level business goals or ideas. The PRD defines the problem space, user value, and behavioral contracts.

## Steps

### 1. Ingest Context
Read the provided business context, high-level goals, or stakeholder requirements. If none provided, ask the user for:
- The product/feature being defined
- The target user or customer
- The core problem being solved

### 2. Structure
Create the document with all mandatory sections:
- Section 1: Executive Summary
- Section 2: Strategic Goals (S.M.A.R.T. table + detailed descriptions)
- Section 3: User Stories (table + numbered detail with Acceptance Criteria)
- Section 4: Risks & Mitigations
- Section 5: Assumptions & Dependencies
- Section 6: Constraints
- Section 7: Out of Scope

### 3. Define Strategic Goals
- Define 3-7 strategic goals using the S.M.A.R.T. framework
- Each goal must be Specific, Measurable, Achievable, Relevant, and Time-bound
- Focus on impact and outcomes, not features
- S.M.A.R.T. criteria: Specific (clearly defined), Measurable (quantifiable), Achievable (realistic), Relevant (aligned with business), Time-bound (has deadline)

### 4. Write User Stories
- Generate user stories following the pattern: `As a [role], I want [action], so that [value]`
- Each story must have a clear role, a concrete action, and articulated value
- Number stories sequentially (US-001, US-002, etc.)
- Include a summary table with ID, Role, Requirement, and Value columns

### 5. Define Acceptance Criteria
- For each user story, define acceptance criteria using strict Gherkin syntax
- Cover both the happy path and critical edge cases
- Gherkin pattern:
  - `Given` [precondition/context]
  - `When` [action/event occurs]
  - `Then` [expected outcome/observable result]
- One Given/When/Then per scenario; cover happy path first, then edge cases

### 6. Add Supporting Sections
- **Risks & Mitigations**: Identify key risks and proposed mitigations
- **Assumptions & Dependencies**: Document explicit assumptions and external dependencies
- **Constraints**: Note technical, temporal, or resource constraints
- **Out of Scope**: Explicitly state what is not included

### 7. Output
Produce a complete, professionally formatted PRD document. Save to the specified path or `PRD.md` if no path given.

## Patterns
- **Strategic Goals**: Use the SMART table format from the template, then detailed descriptions below
- **User Stories**: One story per row in the table, full detail in the numbered section
- **Acceptance Criteria**: Group by user story ID, each with at least one scenario
- **Gherkin**: One Given/When/Then per scenario; cover happy path first, then edge cases

## Constraints
1. No vague language (avoid: fast, easy, robust, efficient, seamless, optimized, user-friendly)
2. All goals must have measurable outcomes with timeframes
3. All user stories must follow the exact pattern: `As a [role], I want [action], so that [value]`
4. All acceptance criteria must use Given/When/Then syntax
5. No implementation details — this is the problem space, not the solution space
6. No time-sensitive information (no dates that will expire)

## Outputs
- Complete PRD document with all mandatory sections
- Strategic Goals (SMART format with detailed descriptions)
- User Stories (numbered, with roles, actions, and values)
- Acceptance Criteria (Gherkin-formatted, per user story)
- Supporting sections: Risks, Assumptions, Constraints, Out of Scope
