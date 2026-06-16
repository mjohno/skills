---
name: review
description: Compare an output or result against a spec or goal to find gaps. Use when reviewing code, PRDs, designs, or any artifact against its specification.
metadata:
  type: skill
---

# Review

Goal: Compare any output against any spec to find gaps and report findings.
Non-Goals: Performing implementation, writing code, or executing remediation — only comparison and reporting.

Use When:
- Asked to review an object against another object.
- Asked to review anything against anything.

## Workflows

When asked to review X against Y:
1. X = target (the object that needs review)
2. Y = sources (the materials to review against)
3. If target or sources are not clear → ask the user to clarify before proceeding
4. Load `references/workflow_default.md` and execute the review

## Examples

### Example 1

**Prompt:**
> Review the PRD against the design skill's workflow.

**Decisions:**
- Target: PRD artifact
- Sources: design skill's workflow file
- Both are clear → proceed to review

**Outcome:**
Audit report comparing the PRD content against the design workflow's requirements, with findings categorized as Critical or Recommended.

### Example 2

**Prompt:**
> Review the code against the implement skill's workflow.

**Decisions:**
- Target: source code
- Sources: implement skill's workflow
- Both are clear → proceed to review

**Outcome:**
Audit report comparing the code against the implement workflow's standards, with findings categorized as Critical or Recommended.

### Example 3

**Prompt:**
> Review this code against this PRD.

**Decisions:**
- Target: code artifact
- Sources: PRD artifact
- Both are explicit → proceed to review

**Outcome:**
Audit report comparing the code against the PRD's requirements, with findings categorized as Critical or Recommended.

### Example 4

**Prompt:**
> Review the PRD.

**Decisions:**
- Target: PRD — clear
- Sources: unclear — which spec should it be reviewed against?
- Ask user to clarify sources before proceeding

**Outcome:**
Clarification request: "What should I review the PRD against? (e.g., the design skill's workflow, the PRD spec, a checklist, etc.)"
