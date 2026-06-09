# Skill: prd

## Metadata
- **Name**: `prd`
- **Description**: Capability to manage the lifecycle of Product Requirement Documents (PRDs), including Strategic Goals, User Stories, and Gherkin-formatted Acceptance Criteria.

## Overview
The `prd` skill is responsible for translating business intent into structured, testable documentation. It operates via a **Capability-First** model where the agent's behavior is shaped by injecting specific personas and reference materials at runtime.

## Engagement Modes

### 1. `mode: write`
**Persona**: Product Strategist
**Objective**: Create a comprehensive PRD from high-level ideas or business goals.
**Process**:
1.  **Ingest**: Read the provided business context/goals.
2.  **Structure**: Utilize `assets/prd_template.md` as the structural foundation.
3.  **Synthesize**:
    *   Define **Strategic Goals** using the S.M.A.R.T. framework (refer to `references/smart_framework.md`).
    *   Generate **User Stories** following the `As a... I want... so that...` pattern.
    *   Define **Acceptance Criteria** using strict Gherkin syntax (`Given/When/Then`).
4.  **Output**: A complete, formatted `PRD.md`.

### 2. `mode: review`
**Persona**: Critical Analyst
**Objective**: Audit an existing PRD for ambiguity, gaps, and logical inconsistencies.
**Process**:
1.  **Analyze**: Read the target `PRD.md`.
2.  **Evaluate**:
    *   Check for "vague" language in goals and stories.
    *   Look for missing edge cases in the Gherkin scenarios.
    *   Ensure the "Value" in User Stories aligns with the Strategic Goals.
3.  **Feedback**: Provide a structured critique highlighting specific areas for improvement.

### 3. `mode: validate`
**Persona**: Compliance Auditor
**Objective**: Programmatically and semantically verify that a PRD meets the mandatory quality standards.
**Process**:
1.  **Automated Check**: Run `scripts/validate_prd.py` against the target file.
2.  **Semantic Audit**: Use `references/compliance_auditor.md` to perform a deep dive into S.M.A.R.T. and Gherkin compliance.
3.  **Report**: Produce a **Compliance Scorecard** detailing passes, failures, and remediation suggestions.

## Tool Access
- `read`: To ingest business context and existing PRDs.
- `write`: To create and update PRD files.
- `web_search`: To research market trends, user patterns, or technical constraints.
- `bash`: To execute `scripts/validate_prd.py`.

## Reference Materials
- `references/product_strategist.md`
- `references/critical_analyst.md`
- `references/compliance_auditor.md`
- `references/smart_framework.md`

## Assets
- `assets/prd_template.md`
- `assets/user_story_template.md`
