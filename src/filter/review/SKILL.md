---
name: review
description: Use when reviewing any artifact against its specifications.
metadata:
  category: filter
---

# review

Goal: Route review requests to the correct workflow by detecting artifact type, loading specs and lenses, and building context.
Non-Goals: Execute comparison logic (delegated to workflows), remediate artifacts, manage tasks, or transform data.
Use-When: You need to review any artifact against its specifications.

## 0. Prerequisites
- Target artifact (file path, content or diff)
- Specification(s), lens(es) or other criteria

## 1. Inputs
| Input | Required | Example |
|---|---|---|
| Target artifact | Yes | `PRD-001.md` or pasted content |
| Artifact type hint | No | "This is an RFC" (auto-detected otherwise) |
| Lens hints | No | "from a security perspective" |
| Custom spec path | No | "use my-spec.md as the spec" |
| Diff refs | No | "main to HEAD" for diff review |

## 2. Processes
Detect artifact type → load the matching spec → attach lenses → route:

| User intent | Route |
|---|---|
| Diff/PR request | `references/workflow_diff_review.md` |
| Everything else | `references/workflow_generic.md` (with custom spec swapped in or annotations enriched into criteria) |

## 3. Outputs
Review report via `assets/template_report.md` with findings at P1-P5 severity (`assets/severity.md`). Output to prompt by default; write to file when an output path is specified.

## 4. Next Steps
- `check` — run a check on the artifact against requirements, checklists, acceptance or target criteria
- `review` — re-review after fixes are applied
- `annotate` — add inline annotations for tracking findings and fixes
- `plan` — create a plan to address findings

Constraints (also enforced in `references/workflow_base.md`):
1. Cite exact source requirements for every finding
2. Every finding suggests a concrete change
3. Never introduce requirements beyond the loaded specs
4. Report both missing AND incorrect elements
5. No remediation — only comparison and reporting
6. Context is built here; workflows execute comparison

## 5. Examples

### Example 1
**Prompt:** Review RFC-001.md from a security perspective.
→ Detects `rfc` type → loads `spec_rfc.md` + `lens_security.md` → generic workflow → P1-P5 report.

### Example 2
**Prompt:** Review the diff from main to HEAD with the adversarial lens.
→ Diff review → collects `git diff main...HEAD` → loads `lens_adversarial.md` → diff workflow → P1-P5 report scoped to changed lines only.
