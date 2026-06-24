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
Single workflow path — detect artifact type, load spec and lenses, compare against criteria, report findings:

1. Detect artifact type (auto-detect or use hint)
2. Load matching spec (`spec_*.md`) or user-provided custom spec
3. Attach lenses (`lens_generic.md` + domain hints from input)
4. Compare target against combined spec+lens criteria
5. Score findings P1–P5 and produce structured report

## 3. Outputs
Review report via `assets/template_report.md` with findings at P1-P5 severity (`assets/severity.md`). Output to prompt by default; write to file when an output path is specified.

## 4. Next Steps
- `check` — run a check on the artifact against requirements, checklists, acceptance or target criteria
- `review` — re-review after fixes are applied
- `annotate` — add inline annotations for tracking findings and fixes
- `plan` — create a plan to address findings

### Constraints
1. Cite exact source requirements for every finding
2. Every finding suggests a concrete change
3. Never introduce requirements beyond the loaded specs
4. Report both missing AND incorrect elements
5. No remediation — only comparison and reporting

## 5. Examples

### Example 1
**Prompt:** Review RFC-001.md from a security perspective.
→ Detects `rfc` type → loads `spec_rfc.md` + `lens_security.md` → generic workflow → P1-P5 report.

### Example 2
**Prompt:** Review diff from main to HEAD with the adversarial lens.
→ Target = `git diff main...HEAD` output → loads `lens_adversarial.md` → generic workflow → scoped P1–P5 report on changed lines only.
