---
name: step
description: Execute one step toward a high-level goal, verify the result, and report outcomes along with the next step. Use when you need to iterate on a set of references (plans, tasks, files, docs) until the goal is complete, with human review between steps.
metadata:
  category: orchestrate
---

# step

Goal: Execute one step toward a high-level goal, verify the result, and report: (1) the high-level goal, (2) what happened during execution, and (3) the next step to work on.
Non-Goals: Creating or breaking down plans, long-term state management, fully autonomous execution, or operating without human oversight.
Use-When: You have a high-level goal and references to iterate on.

## 0. Prerequisites
- A high-level goal and a specific step to execute
- References (plans, tasks, files, docs) to guide iteration

## 1. Inputs
- High-level goal from prompt
- Next step to execute from prompt
- References (plans, tasks, files, docs) from prompt

## 2. Processes
1. **Execute**: Carry out the step using available tools (shell, file ops, git, subagents, etc.).
2. **Verify**: Check that the step succeeded. Run tests, inspect outputs, confirm artifacts exist.
3. **Report**: Return the high-level goal, what happened (success/failure/partial), and evidence of what was done.
4. **Propose next step**: If the refs indicate more work, suggest the next step. If the goal appears achieved, signal completion. If the step failed, decide whether to suggest recovery directly or delegate to a sub-skill.

## 3. Outputs
- Structured report in the prompt with: Goal, Step executed, Result (Success/Failure/Partial), Next step, Notes
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `step` — continue with the next step
- `plan` — update plan status for completed steps
- `task` — extract a task packet for the next step
- `investigate` — if the step failed with unknown root cause
- `step` — if the step failed with a simple recovery

## 5. Examples

### Example 1

**Prompt:**
> Goal: Implement user authentication with JWT.
> Refs: [plan.md, auth-tasks.md, jwt-docs.md]
> Next step: Set up JWT package

**Decisions:**
- Step is clear and actionable → execute directly
- No failure detected → no delegation needed

**Outcome:**
- Goal: Implement user authentication with JWT
- Step executed: Set up JWT package
- Result: Success — installed `jsonwebtoken`, added to `package.json`, created `config/jwt.js`
- Next step: Create auth middleware
- Notes: None

### Example 2

**Prompt:**
> Goal: Add database migration for user table.
> Refs: [plan.md, migration-tasks.md]
> Next step: Install migration tool

**Decisions:**
- Step failed due to network timeout → assess failure type
- Failure is simple (transient) → suggest direct recovery, no delegation

**Outcome:**
- Goal: Add database migration for user table
- Step executed: Install migration tool
- Result: Failure — `npm install` failed due to network timeout
- Next step: Retry `npm install` or check network connectivity
- Notes: Simple failure — direct recovery suggested

### Example 3

**Prompt:**
> Goal: Implement OAuth2 login with Google.
> Refs: [plan.md, oauth-tasks.md, google-api-docs.md]
> Next step: Set up OAuth2 config

**Decisions:**
- Step failed due to invalid credentials → assess failure type
- Failure is complex (root cause unknown) → delegate to `step: investigate`

**Outcome:**
- Goal: Implement OAuth2 login with Google
- Step executed: Set up OAuth2 config
- Result: Failure — Google API credentials are invalid; the client secret is rejected
- Next step: Delegated to `step: investigate` to determine whether to regenerate credentials in Google Cloud Console or check if the project has the correct OAuth consent screen configured
- Notes: Complex failure — root cause unknown, investigation needed before proceeding
