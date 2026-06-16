# Workflow: PRD Review

## Context
Audit an existing PRD for ambiguity, gaps, and logical inconsistencies. This workflow loads the PRD workflow specification as the source and applies PRD-specific review criteria.

## Steps

### 1. Identify Target
- Extract the PRD file to review
- If unclear, ask the user to clarify before proceeding

### 2. Load Source Specification
- Load `references/workflow_prd.md` as the source specification
- Load `assets/prd_template.md` for structural reference
- Load `assets/user_story_template.md` for story/AC pattern reference

### 3. Analyze Structure
Verify the PRD adheres to the template structure:
- Executive Summary present and concise
- Strategic Goals section with SMART table and detailed descriptions
- User Stories section with table and numbered detail
- Acceptance Criteria section with Gherkin scenarios

### 4. Evaluate Content
Perform a deep dive focusing on:
- **Ambiguity Detection**: Identify vague language in goals and stories that would be difficult for an engineer to implement (e.g., fast, easy, robust, efficient, seamless, optimized, user-friendly)
- **SMART Compliance**: Verify each strategic goal is Specific, Measurable, Achievable, Relevant, and Time-bound
- **User Story Syntax**: Verify every story follows the pattern: `As a [role], I want [action], so that [value]`
- **Gherkin Syntax**: Verify all acceptance criteria use Given/When/Then and describe observable outcomes
- **Edge Case Analysis**: Look for missing edge cases in Gherkin scenarios (e.g., invalid input, out-of-state conditions, error paths)
- **Strategic Alignment**: Ensure the "Value" in User Stories aligns directly with the defined Strategic Goals
- **Logical Consistency**: Check for contradictions between requirements or gaps between user stories and acceptance criteria

### 5. Report Findings
Provide a structured critique highlighting:
- **The Issue**: A clear description of what is wrong
- **The Impact**: Why this ambiguity or gap is a risk
- **Remediation**: A suggested way to rewrite or expand the requirement

## Patterns
- **Finding format**: `P<n> - <issue> (source: <reference>)`
- **Report structure**: structure → content → findings → recommended changes
- **Compare section-by-section**, not holistically

## Constraints
1. Be specific: cite exact source requirements
2. Be actionable: each finding should suggest a concrete change
3. Don't introduce new requirements beyond the sources
4. Report both what's missing AND what's wrong
5. Do not perform remediation — only comparison and reporting

## Outputs
- Review report with findings categorized by severity (P1-P5)
- Structural compliance assessment
- Content quality assessment (ambiguity, SMART, Gherkin, alignment)
- Specific, recommended changes for each finding
