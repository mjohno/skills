# PLAN-dikw-etl-refactor

Goal: Restructure the skills repository from the old `design`-centric model into the Dikw ETL skill taxonomy (discover, extract, transform, load, orchestrate, meta).

## GAP Map

| Gap ID | Current Problem | Target State |
|---|---|---|
| GAP-1 | `design` skill is a PRD/RFC router that skips the entire design lifecycle | Remove `design`; replace with 6 composable transform skills (analyze, hypothesize, define, ideate, prototype, test) |
| GAP-2 | `writing` skill only does prose polishing; doesn't cover PRD, RFC, or code output types | Remove `writing`; replace with 4 load skills (prose, prd, rfc, code) |
| GAP-3 | `skill-manager` name is clunky and doesn't reflect meta role | Rename `skill-manager` → `skillz` |
| GAP-4 | No `collect` skill in extract category | Create `collect` skill |
| GAP-5 | No transform skills exist (analyze, hypothesize, define, ideate, prototype, test) | Create all 6 transform skills |
| GAP-6 | Load skills only have prose (from writing); no prd, rfc, or code load skills | Create prd, rfc, code load skills (prose comes from writing replacement) |
| GAP-7 | Existing skills (investigate, grill-me, review, plan, task, annotate, git-commit, step) need taxonomy alignment — descriptions and metadata updated to reflect new category model | Update all existing skill SKILL.md files with correct taxonomy category, descriptions, and push hints |
| GAP-8 | No push-hint mechanism — skills don't suggest next steps to downstream consumers | Add `## Next Steps` push hints to new skills; update existing skills where relevant |
| GAP-9 | `design` directory has legacy assets, references, and scripts that are orphaned after removal | Clean up design directory artifacts that are absorbed or replaced |
| GAP-10 | No skillz workflows for creating router/classic skills under the new taxonomy | Update skillz reference workflows to reflect 6-category taxonomy |

## Plan Items

### ITEM-1: Remove `design` skill directory
**Closes:** GAP-1
**Description:** Delete the `design/` directory (SKILL.md, assets/, references/, scripts/). The design skill's PRD/RFC routing is absorbed into the new transform and load skills.
**Deliverable:** `design/` directory removed from repository.
**Status:** planned

### ITEM-2: Rename `skill-manager` → `skillz`
**Closes:** GAP-3
**Description:** Rename directory `skill-manager/` to `skillz/`. Update all internal references, workflow files, and the SKILL.md frontmatter `name` field to `skillz`.
**Deliverable:** `skillz/SKILL.md` with `name: skillz`, all internal references updated.
**Status:** done
**Committed:** `refactor(meta): rename skill-manager to skillz and update references`

### ITEM-3: Create `collect` skill (extract)
**Closes:** GAP-4
**Description:** Use `skillz` operation `create` to scaffold `collect/SKILL.md` — gathers resources, landscape scan, competitive data. Outputs structured resource inventory to prompt (pipeline-style). If user specifies an output file, write to that path instead. Pushes next: analyze, ideate, define. Category: `extract`.
**Deliverable:** `collect/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: extract`).
**Status:** planned

### ITEM-4: Create `analyze` skill (transform)
**Closes:** GAP-5
**Description:** Use `skillz` operation `create` to scaffold `analyze/SKILL.md` — finds patterns, contradictions, gaps in collected resources. Reads resource inventory from prompt (pipeline-style). Outputs structured analysis to prompt. If user specifies an output file, write to that path instead. Pushes next: hypothesize, report, ideate. Category: `transform`.
**Deliverable:** `analyze/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: transform`).
**Status:** planned

### ITEM-5: Create `hypothesize` skill (transform)
**Closes:** GAP-5
**Description:** Use `skillz` operation `create` to scaffold `hypothesize/SKILL.md` — extracts meaning, forms hypotheses. Reads analysis from prompt (pipeline-style). Outputs synthesis to prompt. If user specifies an output file, write to that path instead. Pushes next: ideate, define, collect. Category: `transform`.
**Deliverable:** `hypothesize/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: transform`).
**Status:** done
**Committed:** `feat(transform): create hypothesize skill`

### ITEM-6: Create `define` skill (transform)
**Closes:** GAP-5
**Description:** Use `skillz` operation `create` to scaffold `define/SKILL.md` — frames problem, defines requirements. Reads synthesis from prompt (pipeline-style). Outputs problem statement and requirements to prompt. If user specifies output files, write to those paths. Pushes next: ideate, prototype. Category: `transform`.
**Deliverable:** `define/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: transform`).
**Status:** done
**Committed:** `feat(transform): create define skill`

### ITEM-7: Create `ideate` skill (transform)
**Closes:** GAP-5
**Description:** Use `skillz` operation `create` to scaffold `ideate/SKILL.md` — generates and narrows solutions. Reads problem statement + requirements from prompt (pipeline-style). Outputs solution concepts to prompt. If user specifies an output file, write to that path. Pushes next: prototype, define (loop-back). Category: `transform`.
**Deliverable:** `ideate/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: transform`).
**Status:** done
**Committed:** `feat(transform): create ideate skill`

### ITEM-8: Create `prototype` skill (transform)
**Closes:** GAP-5
**Description:** Use `skillz` operation `create` to scaffold `prototype/SKILL.md` — makes concepts tangible. Reads solution concepts from prompt (pipeline-style). Outputs prototype description to prompt. If user specifies output files, write to those paths. Category: `transform`.
**Deliverable:** `prototype/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: transform`).
**Status:** done
**Committed:** `feat(transform): create prototype skill`

### ITEM-9: Create `test` skill (transform)
**Closes:** GAP-5
**Description:** Use `skillz` operation `create` to scaffold `test/SKILL.md` — evaluates against hypotheses + requirements. Reads prototype + requirements from prompt (pipeline-style). Outputs test results to prompt. If user specifies an output file, write to that path. Pushes next: ideate (fail), prototype (fix), define (re-frame), research (ambiguous). Category: `transform`.
**Deliverable:** `test/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: transform`).
**Status:** done
**Committed:** `feat(transform): create test skill`

### ITEM-10: Create `prose` skill (load)
**Closes:** GAP-6
**Description:** Use `skillz` operation `create` to scaffold `prose/SKILL.md` — formats information into prose (articles, essays, narratives, blog posts). Reads raw information/context from prompt. Outputs polished prose to prompt. If user specifies an output file, write to that path. Pushes next: review. Category: `load`.
**Deliverable:** `prose/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: load`).
**Status:** planned

### ITEM-11: Create `prd` skill (load)
**Closes:** GAP-6
**Description:** Use `skillz` operation `create` to scaffold `prd/SKILL.md` — formats information into PRD structure. Reads problem statement + requirements + solution concepts from prompt. Outputs structured PRD to prompt. If user specifies an output file, write to that path. Pushes next: review, rfc. Category: `load`.
**Deliverable:** `prd/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: load`).
**Status:** planned

### ITEM-12: Create `rfc` skill (load)
**Closes:** GAP-6
**Description:** Use `skillz` operation `create` to scaffold `rfc/SKILL.md` — formats information into RFC structure. Reads PRD + technical decisions from prompt. Outputs structured RFC to prompt. If user specifies an output file, write to that path. Pushes next: review, code. Category: `load`.
**Deliverable:** `rfc/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: load`).
**Status:** planned

### ITEM-13: Create `code` skill (load)
**Closes:** GAP-6
**Description:** Use `skillz` operation `create` to scaffold `code/SKILL.md` — formats information into code structure. Reads specs/designs from prompt. Outputs code artifacts to prompt. If user specifies output files, write to those paths. Pushes next: review, git-commit. Category: `load`.
**Deliverable:** `code/SKILL.md` conforming to universal format (sections 0-5, `metadata.category: load`).
**Status:** planned

### ITEM-14: Update existing skill SKILL.md files for taxonomy alignment
**Closes:** GAP-7
**Description:** Use `skillz` operation `comply` to validate each existing skill, then update to reflect the new 6-category taxonomy:
- `investigate` — confirm category: `discover`
- `grill-me` — confirm category: `extract`
- `review` — confirm category: `transform`
- `plan` — confirm category: `load`
- `task` — confirm category: `load`
- `annotate` — confirm category: `load`
- `git-commit` — confirm category: `load`
- `step` — confirm category: `orchestrate`
Each SKILL.md should conform to universal format (sections 0-5, `metadata.category`, push hints in Section 4).
**Deliverable:** All 8 existing SKILL.md files updated and compliant.
**Status:** planned

### ITEM-15: Remove `writing` skill directory
**Closes:** GAP-2
**Description:** Delete the `writing/` directory. Its functionality is replaced by `prose` (load) and the review→edit loop.
**Deliverable:** `writing/` directory removed from repository.
**Status:** planned

### ITEM-16: Clean up orphaned design assets and references
**Closes:** GAP-9
**Description:** Review and remove artifacts from the deleted `design/` directory that are no longer needed:
- `assets/prd_template.md` — replace with `prd/` skill's internal template or reference
- `assets/rfc_template.md` — replace with `rfc/` skill's internal template or reference
- `assets/user_story_template.md` — move to `define/` references if still needed
- `references/workflow_prd.md`, `workflow_rfc.md`, `workflow_prd_validate.md`, `workflow_rfc_validate.md`, `workflow_validate.md` — absorbed into new skills
- `references/smart_framework.md` — evaluate if needed elsewhere
- `scripts/validate_prd.py` — evaluate if needed elsewhere
**Deliverable:** Design directory fully cleaned up or removed.
**Status:** planned

### ITEM-17: Update skillz for new taxonomy
**Closes:** GAP-10
**Description:** Update `skillz/` to fully support the 6-category taxonomy:
- Remove router model (no `workflow_router_skill.md` or router template)
- Replace router template with universal format template (`assets/skill_template.md`)
- Replace router checklist with universal checklist (`assets/checklist.md`)
- Rename `workflow_*.md` to `process_*.md` (classic, comply, deploy)
- Update `SKILL.md` to universal format with `metadata.category: meta`
- Add inline routing in Section 2 (create, comply, deploy, review → delegate)
- Add category selection guidance in `process_classic_skill.md`
- Update compliance to validate `metadata.category` and universal format sections
**Deliverable:** `skillz/` fully refactored — universal format enforced, router model removed, process files renamed.
**Status:** done
**Committed:** `refactor(skillz): remove router model and introduce universal skill format`
**Committed:** `refactor(skillz): rename workflow_ to process_ and remove README`
