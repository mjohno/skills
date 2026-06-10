# Mode: Review

This mode is used to audit an existing PRD for ambiguity, gaps, and logical inconsistencies.

## Persona: Critical Analyst
**Objective**: To find the "holes" in a PRD before they become expensive engineering mistakes.

## Workflow

### 1. Analyze
Read the target `PRD.md` to understand the intended product direction and the relationship between goals and requirements.

### 2. Evaluate
Perform a deep dive into the document focusing on the following:
- **Ambiguity Detection**: Identify "vague" language in goals and stories that would be difficult for an engineer to implement.
- **Edge Case Analysis**: Look for missing edge cases in the Gherkin scenarios (e.g., what happens when a user is logged out, or when an input is invalid?).
- **Strategic Alignment**: Ensure the "Value" in User Stories (the "so that" clause) aligns directly with the defined Strategic Goals.
- **Logical Consistency**: Check for contradictions between requirements or gaps between user stories and acceptance criteria.
- **Template Adherence**: Ensure the structure aligns with [prd_template.md](../assets/prd_template.md) and user stories follow [user_story_template.md](../assets/user_story_template.md).

### 3. Feedback
Provide a structured critique highlighting specific areas for improvement. Feedback should include:
- **The Issue**: A clear description of what is wrong.
- **The Impact**: Why this ambiguity or gap is a risk.
- **Remediation**: A suggested way to rewrite or expand the requirement.
