---
name: skill-manager
description: Generates spec-compliant AgentSkills.io skill packages. Use when you need to create a new skill, review an existing skill, or deploy a skill to a target directory.
metadata:
  type: router
---

# Skill Manager

Goal: Generate, review, comply and deploy spec-compliant AgentSkills.io skill packages.
Non-Goals: Managing non-skill resources, CI/CD pipelines, or version control operations.

## Use When
- Creating skills (classic or router-based)
- Reviewing skills against their source specifications
- Complying skills to meet spec requirements
- Deploying skills to a target directory

## Inputs
1. Operation type (create, comply, review, deploy)
2. Subject skill name (for create, review, comply, deploy)
3. Source specification (for create, review)

## Workflow
1. Gather Context
2. Route the Request
3. Execute the Workflow

### Gather Context
1. Collect Inputs
2. Identify the requested operation (create, comply, review, deploy).
3. Identify the skill which is the object of the operation.

### Route the Request
- Create classic skill → `references/workflow_classic_skill.md`
- Create router skill → `references/workflow_router_skill.md`
- Review skill → delegate to review skill
- Comply skill → `references/workflow_comply.md`
- Deploy skill → `references/workflow_deploy.md`
- Default → Gather more information and clarify the request.

### Execute the Workflow
- Read and follow the steps outlined in the routed workflow file to complete the requested operation.

## Outputs
- See outputs in each workflow.

## Examples

### Example 1: Create a skill

**Prompt:**
> Create a new skill called `code-review` that helps review code for quality and best practices.

**Routing:**
- Operation: create
- Type: skill (classic standalone skill)
- → Read and follow `references/workflow_classic_skill.md`
- See examples in `workflow_classic_skill.md` for results.

### Example 2: Create a router skill

**Prompt:**
> Create a new router skill called `design-manager` that dispatches to design workflows.

**Routing:**
- Operation: create
- Type: router
- → Read and follow `references/workflow_router_skill.md`
- See examples in `workflow_router_skill.md` for results.

### Example 3: Review a skill

**Prompt:**
> Review the `git-commit` skill for compliance and quality.

**Routing:**
- Operation: review
- → Delegate to review skill with the skill package as target
- See examples in the review skill for results.

### Example 4: Comply (pass/fail test)

**Prompt:**
> Run compliance checks on the `grill-me` skill.

**Routing:**
- Operation: comply
- → Read and follow `references/workflow_comply.md`
- See examples in `workflow_comply.md` for results.

### Example 5: Deploy a skill

**Prompt:**
> Deploy the `investigate` skill to `C:\Users\matjo\.pi\agent\skills\`.

**Routing:**
- Operation: deploy
- → Read and follow `references/workflow_deploy.md`
- See examples in `workflow_deploy.md` for results.
