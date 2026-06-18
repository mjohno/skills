---
name: code
description: Generates code artifacts from specifications and designs. Use when you need to produce implementation code from RFCs, PRDs, or technical specs.
metadata:
  category: load
---

# code

Goal: Generate code artifacts from specifications and designs.
Non-Goals: Designing architecture, writing documentation, or managing deployment infrastructure.
Use-When: You need to produce implementation code from RFCs, PRDs, or technical specs.

## 0. Prerequisites
- RFC, PRD, or task/plan from `rfc`, `prd`, `plan`, or `task` skill
- Technical decisions and architecture details (optional)

## 1. Inputs
- RFC, PRD, task packet, or plan from prompt
- Specifications, designs, and technical decisions from prompt
- Target language, framework, and conventions (optional)

## 2. Processes
1. Parse specifications to understand the required functionality and constraints
2. Determine the appropriate code structure and file layout
3. Generate code artifacts:
   - Core implementation files
   - Tests and test fixtures
   - Configuration files
4. Ensure code follows the specified conventions and standards
5. Document code structure and dependencies

## 3. Outputs
- Code artifacts in the prompt
- If user specifies output files, write code to those paths instead

## 4. Next Steps
- `review` — have the `review` skill evaluate the code for quality and correctness
- `git-commit` — commit the code artifacts
- `code` — iterate on additional modules or features

## 5. Examples

### Example 1: Code from RFC

**Prompt:** Generate code for the zero-trust identity service from the RFC.

**Outcome:** Prompt output with implementation code files (e.g., `auth.py`, `config.yaml`, `test_auth.py`) demonstrating the core identity validation service.

### Example 2: Code from task packet

**Prompt:** Generate code from the task packet for the auth module.

**Outcome:** Prompt output with implementation code files derived from the task's requirements and acceptance criteria.
