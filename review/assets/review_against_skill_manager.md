# Review Report: review/ skill package

## Sources
- **Spec**: `skillz/assets/skill_template.md` (skill template)
- **Spec**: `skillz/assets/router_checklist.md` (router checklist)
- **Spec**: `skillz/assets/checklist.md` (classic checklist)
- **Spec**: `skillz/assets/router_skill_template.md` (router template)
- **Spec**: `skillz/references/workflow_classic_skill.md` (workflow requirements)
- **Spec**: `skillz/references/workflow_router_skill.md` (workflow requirements)
- **Spec**: `skillz/SKILL.md` (skillz skill itself — reference implementation)

## Targets
- `review/SKILL.md` (139 lines)
- `review/references/` (16 files: specs, lenses, artifacts, workflows)
- `review/assets/template_report.md`

## Summary
The review skill is a well-structured router skill with comprehensive review workflows, lenses, and artifact specs. However, it has **one P1 finding** (referenced step that does not exist), **four P2 findings** (broken cross-skill references, structural deviation from router template, missing routing to a discovered workflow, and a line-count issue), and **three P3 findings** (severity scale inconsistencies, missing spec_prose.md artifact definition, and redundant severity definitions across workflow files).

---

## Findings

### P1
- **P1-1 — SKILL.md references "Step 7" which does not exist**
  - **Source**: `review/SKILL.md` lines 97, 108, 119, 131
  - **Issue**: Multiple workflow files (`workflow_generic.md`, `workflow_spec_review.md`, `workflow_annotation_review.md`) reference "the router's P1-P5 severity scale (defined in Step 7 of SKILL.md)". The SKILL.md has exactly 6 steps under "Workflow" (Gather Context, Route the Request, Execute the Workflow, then three sub-steps). There is no Step 7.
  - **Source reference**: `review/SKILL.md` — the severity scale is embedded within Step 6 ("Categorize Findings by Severity"), not in a separate step.
  - **Suggested fix**: Update all workflow files to reference "Step 6" instead of "Step 7", or extract the severity scale into a new Step 7 under the "Execute the Workflow" section of SKILL.md.

### P2
- **P2-1 — SKILL.md exceeds the 100-line limit**
  - **Source**: `review/SKILL.md` (139 lines)
  - **Issue**: The `checklist.md` requires "SKILL.md under 100 lines". The review skill is 139 lines, exceeding this by 39 lines (39% over).
  - **Suggested fix**: Move detailed workflow descriptions into referenced files (already partially done), consolidate the 5 examples into fewer, or split into focused sub-skills.

- **P2-2 — Broken cross-skill references in spec files**
  - **Source**: `review/references/spec_prd.md`, `review/references/spec_rfc.md`, `review/references/spec_skill.md`, `review/references/spec_code.md`, `review/references/spec_prose.md`
  - **Issue**: Multiple spec files reference files in other skills that do not exist in this workspace:
    - `spec_prd.md` → `design/references/workflow_prd.md` (does not exist)
    - `spec_prd.md` → `design/assets/prd_template.md` (does not exist)
    - `spec_prd.md` → `design/assets/user_story_template.md` (does not exist)
    - `spec_rfc.md` → `design/references/workflow_rfc.md` (does not exist)
    - `spec_rfc.md` → `design/assets/rfc_template.md` (does not exist)
    - `spec_skill.md` → `skillz/references/workflow_review.md` (does not exist)
    - `spec_prose.md` → `writing/references/readability_guidelines.md` (does not exist)
    - `spec_prose.md` → `writing/references/density_guidelines.md` (does not exist)
    - `spec_prose.md` → `writing/references/mode_review.md` (does not exist)
  - **Suggested fix**: Either create the referenced files, update references to point to existing paths, or remove the "Source References" section if the referenced files are unavailable.

- **P2-3 — SKILL.md does not conform to router_skill_template.md structure**
  - **Source**: `review/SKILL.md` vs `skillz/assets/router_skill_template.md`
  - **Issue**: The router template requires a specific section order:
    1. Frontmatter with `metadata.type: router`
    2. `# [Skill Name]`
    3. `Goal:` and `Non-Goals:` on root level (not under a heading)
    4. `## Use When`
    5. `## Inputs`
    6. `## Workflow` with subsections `### Gather Context`, `### Route the Request`, `### Execute the Workflow`
    7. `## Outputs`
    8. `## Examples`
    
    The review skill deviates: Goal/Non-Goals are under `# Review` heading (not root level), uses `## Workflow` with numbered steps at the top level rather than subsections, and the section structure does not match the template.
  - **Suggested fix**: Restructure SKILL.md to match the router_skill_template.md format exactly.

- **P2-4 — `workflow_annotation_review.md` exists but is not routed to**
  - **Source**: `review/SKILL.md` vs `review/references/workflow_annotation_review.md`
  - **Issue**: The SKILL.md describes discovering `REVIEW(<id>)` annotations in Step 5 and incorporating them as criteria in Step 6. However, the routing section (Step 5) only routes to `workflow_generic.md` or `workflow_spec_review.md`. The `workflow_annotation_review.md` file exists and is designed for annotation-focused reviews, but there is no routing path to use it.
  - **Suggested fix**: Add a routing rule: "User requests annotation-focused review → `references/workflow_annotation_review.md`".

### P3
- **P3-1 — Severity scale definitions are inconsistent across workflow files**
  - **Source**: `review/references/workflow_generic.md`, `review/references/workflow_spec_review.md`, `review/references/workflow_annotation_review.md`
  - **Issue**: Each workflow file independently defines the P1-P5 severity scale with slightly different wording. For example, P1 is defined as:
    - `workflow_generic.md`: "Violates the spec or lens (missing required elements, contradictions, syntax errors)"
    - `workflow_spec_review.md`: "Violates the spec (missing required elements, contradictions, syntax errors)"
    - `workflow_annotation_review.md`: "Violates the spec/lens/annotation requirement"
    
    This creates maintenance burden and potential confusion. The SKILL.md also defines the scale in Step 6, creating a third definition.
  - **Suggested fix**: Define the severity scale once (e.g., in a shared `references/severity_scale.md` or in the SKILL.md Step 6) and have all workflow files reference it.

- **P3-2 — Missing `artifact_prose.md` content for prose artifact type**
  - **Source**: `review/references/artifact_prose.md`
  - **Issue**: The `artifact_prose.md` file exists but only contains minimal content (structure and metadata). Compared to `artifact_skill.md` (which has a detailed target structure) and `artifact_prd.md` (which has sections and metadata), the prose artifact definition lacks detail about what constitutes valid prose content.
  - **Suggested fix**: Expand `artifact_prose.md` to include content criteria (e.g., readability markers, density indicators) consistent with the level of detail in other artifact definitions.

- **P3-3 — `spec_code.md` references `pi-subagents/agents/reviewer.md` (two levels deep)**
  - **Source**: `review/references/spec_code.md`
  - **Issue**: The `checklist.md` requires "References one level deep". The reference `pi-subagents/agents/reviewer.md` is two levels deep (`pi-subagents/` + `agents/` + `reviewer.md`).
  - **Suggested fix**: Either flatten the reference path or remove it if the referenced file is not accessible.

---

## Recommended Changes

1. **Fix the Step 7 reference** (P1-1): Update all workflow files to reference "Step 6" instead of "Step 7" — this is the only P1 and must be fixed first.

2. **Resolve broken cross-skill references** (P2-2): Audit all `## Source References` sections in spec files. Either create the referenced files, update paths to existing locations, or remove references to unavailable files.

3. **Restructure SKILL.md to match router template** (P2-3): Align the section order and formatting with `router_skill_template.md` — move Goal/Non-Goals to root level, use proper subsections under Workflow.

4. **Add annotation workflow routing** (P2-4): Add a routing rule for `workflow_annotation_review.md` when the user explicitly requests annotation-focused review or when REVIEW annotations are discovered.

5. **Consolidate severity scale definitions** (P3-1): Define P1-P5 once in the SKILL.md and have all workflow files reference it, rather than duplicating definitions.

6. **Reduce SKILL.md line count** (P2-1): Consider moving more content into referenced files or consolidating examples to get under 100 lines.

7. **Fix two-level-deep reference** (P3-3): Update `spec_code.md` to use a one-level-deep reference or remove it.

8. **Expand artifact_prose.md** (P3-2): Add content criteria to match the detail level of other artifact definitions.
