# PLAN: Create Review Skill

**Status:** Draft  
**Created:** 2026-06-15  
**Related:** [PRD-skill-routing.md](PRD-skill-routing.md)  

---

## Concept

The `review` skill is a **universal, domain-agnostic** skill that compares any output against any spec. The spec comes from one of two sources:

| Spec Source | When | How |
|-------------|------|-----|
| **Skill workflow** | "Review the PRD" | Load the skill's workflow that defines what a PRD should be |
| **Artifact** | "Review this code against this PRD" | Use the PRD artifact directly as the spec |

The review skill doesn't care what it's reviewing. It just: find the spec → compare → report gaps.

---

## Target Structure

```
review/
+-- SKILL.md                  -- router (<= 30 lines)
+-- references/
|   +-- workflow_default.md -- compare output against spec (also the default)
+-- assets/
    +-- template_report.md    -- review report template
```

---

## Gap Closing Items

### Item 1: Create `references/workflow_default.md`

**What:** The general-purpose review workflow that teaches the agent how to review anything against anything. This is also the default workflow for the skill.

**Content:**

```markdown
# Review Workflow

## Context
Compare an output against a spec to find gaps and report findings.

## Steps
### 1. Identify the output to review
   - Extract the artifact, document, or deliverable to be reviewed

### 2. Identify the spec to compare against
   - If the spec is a skill → load that skill's workflow file
   - If the spec is an artifact → use that artifact as the spec
   - If the spec is implicit (e.g. "review the PRD") → find the skill that
     created it and load its defining workflow

### 3. Compare output against spec
   - Go through the spec systematically
   - Check each requirement, constraint, and pattern
   - Note where the output matches, deviates, or omits

### 4. Categorize findings by severity
   - **P1**: Violates the spec (missing required elements, contradictions)
   - **P2-P5**: Could be improved (quality, completeness, clarity)

### 5. Report findings
   - Summary of overall compliance
   - List of findings with spec references
   - Specific, recommended changes needed

## Patterns
- Finding format: `P<n> - <issue> (source: <reference>)`
- Report structure: sources → targets → summary → findings (P1-P5) → recommended changes
- Compare section-by-section, not holistically

## Constraints
- Be specific: cite exact spec requirements
- Be actionable: each finding should suggest a concrete change
- Don't introduce new requirements beyond the spec
- Report both what's missing AND what's wrong

## Output
Use template: `assets/template_report.md`
```

**Acceptance:**
- Workflow covers all three review patterns (skill-based, artifact-based, implicit)
- Workflow is domain-agnostic (doesn't mention PRD, code, or any specific domain)
- Workflow follows the contract (context, steps, patterns, constraints, output)

---

### Item 2: Create `assets/template_report.md`

**What:** A template for review reports.

**Content:**

```markdown
# Review Report: [Artifact Name]

## Sources
- [Source 1: the spec(s) or workflow(s) used as the basis for comparison]
- [Source 2]

## Targets
- [Target 1: the output(s) being reviewed]
- [Target 2]

## Summary
[Overall assessment: e.g., "The target is mostly compliant with 3 P1 gaps and 2 P2 recommendations."]

## Findings

### P1
- [Finding 1: what's wrong, source reference, suggested fix]
- [Finding 2]

### P2
- [Finding 1: what could be better, source reference, suggested fix]
- [Finding 2]

### P3
- [Finding 1]

### P4
- [Finding 1]

### P5
- [Finding 1]

## Recommended Changes
1. [Change 1]
2. [Change 2]
3. [Change 3]
```

**Acceptance:**
- Template produces a clear, structured review report
- Template includes Sources and Targets sections (both plural)
- Template uses P1-P5 severity scale (P1 = critical, P2-P5 = recommended)
- Template includes Recommended Changes section

---

### Item 3: Create `SKILL.md` as a Router

**What:** The review skill's router — ≤ 30 lines, declares capability, use when, routing.

**Content:**

```markdown
---
name: review
description: Compare an output against a spec to find gaps. Use when you need to review anything against anything.
---

## Capability
Compare any output against any spec to find gaps and report findings.

## Use When
- "Review the PRD" → compare against design skill's workflow
- "Review the code" → compare against implement skill's workflow
- "Review this code against this PRD" → compare code against PRD artifact
- "Review anything against anything" → compare output against any spec

## Routing
When asked to review X against Y:
1. X = the output to review
2. Y = the spec to compare against
3. If Y is a skill → load that skill's workflow as the spec
4. If Y is an artifact → use that artifact as the spec
5. Load `references/workflow_default.md` and execute the review
```

**Acceptance:**
- SKILL.md is ≤ 30 lines
- SKILL.md covers all three review patterns in Use When
- SKILL.md routing instructions match the workflow file
- Frontmatter preserved (name and description)

---

## Verification Commands

```bash
# Verify SKILL.md is <= 30 lines
wc -l review/SKILL.md

# Verify all files exist
test -f review/SKILL.md && echo "SKILL.md OK"
test -f review/references/workflow_default.md && echo "workflow_default.md OK"
test -f review/assets/template_report.md && echo "template_report.md OK"
```

---

## Execution Order

1. **Item 1** — Create `references/workflow_default.md`
2. **Item 2** — Create `assets/template_report.md`
3. **Item 3** — Create `SKILL.md`

All items are independent.
