---
name: review
description: Centralized review skill. Detects artifact type, discovers specs, suggests lenses, and routes to the appropriate review workflow. Use when reviewing any artifact against its specifications.
metadata:
  type: router
---

# Review

Goal: Detect artifact type, build review context (spec + lens), and route to the appropriate review workflow.
Non-Goals: Execute review logic (that's the workflow's job), manage task packets, or perform remediation.

## Use When
- Asked to review any artifact against specifications.
- Asked to compare an output against a spec or goal.
- Asked to audit a document, code, skill, or prose.

## Inputs
1. **Target** — the artifact to review (file path or content)
2. **Lens hints** — any named lenses the user specifies (e.g., "from a security perspective")
3. **Workflow hints** — any named workflow overrides (e.g., "using spec_review")
4. **Custom specs** — any user-provided spec files

## Workflow
1. Gather Context
2. Route the Request
3. Execute the Workflow

### Gather Context

#### 1. Build Context from Input
Parse the user's natural language input. Extract:
- **Target**: the artifact to review (file path or content)
- **Lens hints**: any named lenses the user specifies (e.g., "from a security perspective")
- **Workflow hints**: any named workflow overrides (e.g., "using spec_review")
- **Custom specs**: any user-provided spec files

#### 2. Detect Artifact Type
Read the target artifact and analyze its content via LLM to classify:
- `prd` — contains Strategic Goals, User Stories, Acceptance Criteria, Gherkin scenarios
- `rfc` — contains Proposed Solution, Design Decisions, Architecture, Feasibility
- `code` — source files, tests, diffs
- `skill` — contains SKILL.md with frontmatter, Goal, Use When, Examples
- `prose` — documents, comments, documentation text
- `generic` — cannot be classified; treat as generic

If confidence is below threshold, ask the user to confirm.

**User override always wins** — if the user specifies an artifact type explicitly, use it.

### Route the Request

#### 3. Discover Specs
Load the built-in `spec_<type>.md` file for the detected artifact type. This contains:
- References to source files that define correctness for this artifact type
- Additional criteria not captured by source files

If the user provides custom spec files, they override built-in specs.

#### 4. Suggest Lenses
Always apply **lens_generic.md** (base lens) — universal critical thinking:
1. Internal consistency — no contradictions within the artifact
2. Completeness — no missing required elements (from the spec)
3. Clarity — no ambiguous language or vague requirements

If the user specifies domain lenses (e.g., "security"), load the corresponding `lens_*.md` files.
Domain lenses are **additive** on top of lens_generic.md.

If the user does not specify lenses, suggest relevant ones based on artifact type:
- PRD → no automatic lens suggestions
- RFC → suggest lens_system_architect.md, lens_security.md
- Code → suggest lens_security.md
- Skill → no automatic lens suggestions
- Prose → no automatic lens suggestions

#### 5. Discover Annotate REVIEW Hints
Scan the target artifact and its surrounding directory for `REVIEW(<id>)` annotations.
Use lightweight pattern matching — only match `REVIEW(<id>)` format (do not import full annotation format).
Each discovered REVIEW annotation becomes a targeted review criterion.

#### 6. Route
If inputs are insufficient (no target, no spec, no lens), ask the user with helpful recommendations:
- For unclear target: suggest likely candidates
- For unclear specs: suggest built-in spec files or ask for custom specs
- For unclear lenses: suggest relevant lenses based on artifact type

Otherwise, route to the appropriate workflow:
- **Default Route:** → `references/workflow_generic.md` (base lens only)
- **User specifies workflow** → `references/workflow_<name>.md`
- **User provides custom specs** → `references/workflow_spec_review.md`

### Execute the Workflow

#### 7. Build Context for Workflow
Pass to the workflow:
- **Target**: the artifact to review
- **Spec**: loaded spec criteria (from spec_ file + custom specs)
- **Lenses**: lens_generic.md + any domain lenses
- **Annotation hints**: discovered REVIEW(<id>) annotations
- **Workflow**: the routed workflow file

## Outputs
- Review report via the routed workflow, using `assets/template_report.md`
- Report contains: sources → targets → summary → findings (P1-P5) → recommended changes

## Constraints
1. Be specific: cite exact source requirements
2. Be actionable: each finding should suggest a concrete change
3. Don't introduce new requirements beyond the specs
4. Report both what's missing AND what's wrong
5. Do not perform remediation — only comparison and reporting
6. Router builds context; workflows execute comparison and produce reports

## Examples

### Example 1
**Prompt:** Review RFC-001.md from a security perspective.
**Decisions:** Detect artifact type = rfc, load spec_rfc.md, suggest lens_security.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.

### Example 2
**Prompt:** Review the PRD in PRD-001.md.
**Decisions:** Detect artifact type = prd, load spec_prd.md, apply lens_generic.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.

### Example 3
**Prompt:** Review this code.
**Decisions:** Detect artifact type = code, load spec_code.md, apply lens_generic.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.

### Example 4
**Prompt:** Review this document.
**Decisions:** Detect artifact type = generic (or prose if content suggests), load spec for type, apply lens_generic.md, route to workflow_generic.md.
**Outcome:** Review report with findings categorized P1-P5.

### Example 5
**Prompt:** Review this PRD.
**Decisions:** Target clear, but no lens specified. Suggest relevant lenses based on PRD type.
**Outcome:** Clarification: "What lens should I use? (e.g., security, system architect, or just the default critical thinking lens?)"
