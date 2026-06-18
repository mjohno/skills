---
name: skillz
description: Generates spec-compliant AgentSkills.io skill packages. Use when you need to create a new skill, review an existing skill, or deploy a skill to a target directory.
metadata:
  category: meta
---

# skillz

Goal: Generate, review, comply and deploy spec-compliant AgentSkills.io skill packages.
Non-Goals: Managing non-skill resources, CI/CD pipelines, or version control operations.
Use-When: Creating skills, reviewing skills against specifications, complying skills to meet requirements, or deploying skills.

## 0. Prerequisites
- User has a skill package directory or wants to create a new one

## 1. Inputs
- Operation type (create, review, comply, deploy)
- Subject skill name or directory
- Source specification (for create, review)

## 2. Processes
1. Gather context: identify the requested operation and skill target
2. Route to the appropriate process file:
   - create → `references/process_classic_skill.md`
   - comply → `references/process_comply.md`
   - deploy → `references/process_deploy.md`
   - review → delegate to the `review` skill (external)
3. Execute the process steps
4. Report results

## 3. Outputs
- create → skill package (SKILL.md + optional scripts/, references/, assets/)
- review → audit report from the `review` skill
- comply → pass/fail compliance report
- deploy → synchronized target directory

## 4. Next Steps
- After creating a skill: review it with the `review` skill
- After reviewing: fix violations and re-comply
- After deploying: verify the target directory

## 5. Examples

### Example 1: Create a skill

**Prompt:**
> Create a new skill called `code-review` that helps review code for quality and best practices.

**Execution:**
- Operation: create
- → Read and follow `references/process_classic_skill.md`
- Category: `transform` (analyzing code)

### Example 2: Review a skill

**Prompt:**
> Review the `git-commit` skill for compliance and quality.

**Execution:**
- Operation: review
- → Delegate to the `review` skill with the skill package as target

### Example 3: Comply (pass/fail test)

**Prompt:**
> Run compliance checks on the `grill-me` skill.

**Execution:**
- Operation: comply
- → Read and follow `references/process_comply.md`

### Example 4: Deploy a skill

**Prompt:**
> Deploy the `investigate` skill to `C:/Users/matjo/.pi/agent/skills/`.

**Execution:**
- Operation: deploy
- → Read and follow `references/process_deploy.md`
