---
name: step
description: Execute one step toward a high-level goal, verify the result, and report outcomes along with the next step. Use when you need to iterate on a set of references (plans, tasks, files, docs) until the goal is complete, with human review between steps.
metadata:
  type: skill
---

# step

Goal: Execute one step toward a high-level goal, verify the result, and report: (1) the high-level goal, (2) what happened during execution, and (3) the next step to work on.

Non-Goals: Creating or breaking down plans, long-term state management, fully autonomous execution, or operating without human oversight.

Use When:
- You have a high-level goal and references (plans, tasks, files, docs) to iterate on.
- You need to execute one step, verify it, and determine what comes next.
- You need to iterate repeatedly until a goal is complete with human review between steps.

## Inputs

1. **High-level goal** — What you're ultimately trying to achieve.
2. **Next step** — The specific step to execute right now.
3. **Refs** — A list of references used to iterate on. These may include plans, tasks, files, docs, or any other context. The skill uses them to determine what comes after this step.

## Workflows

1. **Execute** — Carry out the step using available tools (shell, file ops, git, subagents, etc.).
2. **Verify** — Check that the step succeeded. Run tests, inspect outputs, confirm artifacts exist.
3. **Report** — Return:
   - The high-level goal
   - What happened (success, failure, partial)
   - Evidence of what was done
4. **Propose next step** — If the refs indicate more work, suggest the next step. If the goal appears achieved, signal completion. If the step failed, decide whether to suggest recovery directly or delegate to a sub-skill (see `references/failure_handling.md`).

## Output

Always return (aligned with `assets/skill_template.md`):
- **Goal:** The high-level goal
- **Step executed:** Which step was run
- **Result:** Success / Failure / Partial — with evidence
- **Next step:** The recommended next step (or "goal complete" if done)
- **Notes:** Any issues, blockers, or human decisions needed

## Examples

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
