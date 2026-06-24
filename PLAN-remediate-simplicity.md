# PLAN-remediate-simplicity

## Goal

Simplify the skill management system (AGENTS.md + docs/*), improve clarity, reduce confusion, and embed "beautifully simple" quality standards so that process and compliance actively produce — not just check — well-designed skills.

---

## Problem Statement

The current documents teach a **process** but lack a **standard of quality**. A skill can follow every instruction, pass all checklist items, and still be bloated, unfocused, or ambiguous — because the beautifully simple principles live in one place (checklist.md) without teaching, examples, or enforcement elsewhere. Cross-cutting inconsistencies (path references, category counts, section naming) create real friction.

---

## Full Issue Inventory

All 25 issues identified across the documents:

### AGENTS.md (#1–#4)
1. **"Review" operation is undefined** — says it "audits against specs in docs/*" but doesn't clarify *which* specs, making review subjective and inconsistent
2. **Quality is entirely implicit** — no mention of single responsibility, clear scope, graceful handoffs, or any beautiful simplicity principle
3. **Operations lack decision criteria** — no triggers or thresholds for when to `create`, `comply`, or `review` vs just shipping
4. **"Taxonomy-aware work" is vague** — tells you to consult taxonomy first but doesn't define what "taxonomy-aware" means

### process_classic_skill.md (#5–#10)
5. **Typo / numbering error** — two items labeled `4.` in Phase 1, confusing and unprofessional
6. **Checklist path inconsistency** — references `docs/checklist.md` at the top but `assets/checklist.md` at the bottom
7. **No guidance on choosing between similar categories** — no tiebreaker when a skill might fit two categories (e.g., enrich vs filter)
8. **"Concise description" without definition** — says to be concise but doesn't say what concision looks like
9. **Quality principles from the checklist are never reinforced** — living in checklist.md but never referenced during creation; a creator can pass compliance while writing a bloated skill
10. **No anti-patterns** — nothing warns against common failures (scope creep, over-engineering structure, unnecessary sub-file references)

### process_comply.md (#11–#13)
11. **Purely structural — quality is invisible** — checks format but not whether a skill *is* beautiful or simple; new principles are checkboxes with no rubric for *how* to evaluate them
12. **Checklist path inconsistency** — references `assets/checklist.md` here, which may differ from the path used in process_classic_skill.md
13. **No severity or classification of failures** — a missing section 0 is treated the same as failing "single responsibility"; no way to distinguish critical defects from cosmetic issues

### process_deploy.md (#14–#15)
14. **No pre-deploy quality gate** — deploys any skill directory without checking if it passed compliance
15. **No post-deploy verification** — confirms files copied but doesn't verify the deployed skill works or matches the source

### taxonomy.md (#16–#19)
16. **Inconsistent count** — says "seven categories" but defines eight (interface, input, enrich, filter, normalize, output, map, persona)
17. **"Adjacent concerns" undefined** — note says skills may touch adjacent concerns but doesn't define what they are
18. **Persona category has no clear integration rule** — says "composable with any other category" but gives no guidance on how that works
19. **No exclusion criteria** — every category says what it *does*, but not when you should *not* use it

### skill_template.md (#20–#22)
20. **Non-Goals is optional but critical for simple skills** — the single-responsibility principle depends on explicit non-goals; making them optional undermines that quality goal
21. **No examples of good vs bad instantiation** — template teaches structure but not style; a perfectly structured skill can still be unfocused
22. **Doesn't reinforce quality principles** — template is purely structural; doesn't prompt the creator to think about clear scope, graceful handoffs, etc.

### Cross-cutting (#23–#25)
23. **Beautiful simplicity lives in one place only** — principles exist solely in checklist.md but aren't referenced or taught elsewhere (template, processes, taxonomy). Checkboxes alone are poor teaching instruments.
24. **No "definition of done" for a well-written skill** — passing compliance ≠ having a good skill; no final gate asking "is this beautifully simple?" with rubric criteria
25. **Inconsistent file path references throughout** — `docs/checklist.md` vs `assets/checklist.md`, `references/` vs `assets/references/`; signals immaturity and creates real friction

---

## Remediation Actions

### 1. Consolidate AGENTS.md — Single source of truth

**Issues addressed:** #1 (undefined review), #2 (implicit quality), #3 (no operation triggers), #4 (vague taxonomy-aware)

| Action | Change |
|--------|--------|
| Merge operations into a single unified lifecycle table: `create → comply → deploy` with clear entry/exit criteria per operation | One view of the skill lifecycle instead of scattered prose |
| Define explicit **trigger** for each operation (e.g., "use `comply` before every `deploy`") | No ambiguity about when to run what |
| Move quality standards into AGENTS.md as a dedicated section: **"What Makes a Skill Beautiful"** — list the six simplicity principles with one-line descriptions and link to checklist | Quality lives next to process, not hidden in a separate file |
| Define `review` as a valid operation that delegates to the external review skill | Keep the delegation model; make it explicit |

**Outcome:** AGENTS.md becomes 30-40 lines — one page that answers: what operations exist, when to use them, and what quality looks like.

---

### 2. Unify all file path references under `docs/`

**Issues addressed:** #6, #12, #25 (path inconsistencies)

| Action | Change |
|--------|--------|
| Standardize on `docs/checklist.md` everywhere — update all references in `process_classic_skill.md`, `process_comply.md` | No more `assets/` vs `docs/` ambiguity |
| Remove references to `docs/non_invocable_skills.md` (file doesn't exist) and fold the non-invocability rule into `taxonomy.md` or checklist | Eliminate phantom file reference |

**Outcome:** One authoritative docs directory. No broken paths.

---

### 3. Merge process files — eliminate duplication

**Issues addressed:** #7, #14 (process fragmentation)

| Action | Change |
|--------|--------|
| Combine `process_classic_skill.md` and `process_comply.md` into a single `docs/skill_lifecycle.md` with two phases: **Create**, **Comply**. Phase 3 (Deploy) is kept in `process_deploy.md` because it contains platform-specific commands. | One unified doc for creation logic, deploy stays separate for its CLI commands |

**Rationale:** The create and comply processes already share 60% of their content (category selection, checklist loading, taxonomy reference). Merging removes redundancy and gives a creator a single reference.

---

### 4. Fix taxonomy — clarity and consistency

**Issues addressed:** #16 (count mismatch: says 7 but lists 8), #17 (adjacent concerns undefined), #19 (no exclusion criteria)

| Action | Change |
|--------|--------|
| Fix the category count from "seven" to "eight" in the taxonomy intro | Corrects factual inconsistency |
| Clarify **persona** as a first-class category alongside the other seven — mark it explicitly as modifying how information flows through the system, not replacing a data-flow category. Document how a persona skill composes with input/enrich/filter/output (e.g., "input + persona" produces filtered views of raw data) | Resolves composability confusion (#18), gives persona clear boundaries |
| Add an **exclusion rule** per category: "Do NOT use this category if..." for all eight categories | Prevents guessing — creators now have clear decision trees |

**Outcome:** A taxonomy that distinguishes each category clearly, resolves the persona composability model, and prevents guessing.

---

### 5. Make checklist actionable — add evaluation rubrics

**Issues addressed:** #13 (no severity/classification), checklist quality principles are un-evaluated checkboxes

| Action | Change |
|--------|--------|
| Add severity labels to checklist items: `CRITICAL` (structural validity, must pass), `QUALITY` (beautiful simplicity principles, should pass) | Compliance reports now distinguish "broken" from "could be better" |
| Add a **one-line evaluation criterion** for each quality principle so compliance is deterministic: | The checklist becomes self-evaluating rather than hand-wavy |

  - **Single responsibility**: Does the skill describe one goal with at least one non-goal? ✓
  - **Human-aligned design**: Would a person naturally ask about this task? Does the prompt map directly to it? ✓
  - **Clear scope**: Fewest options/categories needed — no redundant branches? ✓
  - **Minimal default output**: Only essentials returned; detail is opt-in? ✓
  - **Graceful handoff**: When unsolved, suggests specific skills (lookup/remember/etc.)? ✓
  - **Structure matches purpose**: Sections flow prerequisites → inputs → processes → outputs → next steps? ✓

| Add a "Definition of Done" section: "A skill passes compliance if all CRITICAL items pass. A beautifully simple skill also passes all QUALITY items." | Clear distinction between structural validity and quality excellence |

**Outcome:** The checklist is no longer a to-do list — it's a scoring rubric.

---

### 6. Enhance the skill template — embed simplicity during creation

**Issues addressed:** #20 (Non-Goals optional but critical), #21 (no good/bad examples), #22 (no quality scaffolding)

| Action | Change |
|--------|--------|
| Make **Non-Goals mandatory** in the template | The single-responsibility principle needs structural support |
| Add an **"Anti-patterns to Avoid"** section below the template with 3-5 examples: | Teaching by warning is faster than teaching by abstraction |

  - ❌ Goals that say "help users understand X and Y and Z" — pick one
  - ❌ Process steps numbered 1-20 — if it takes this many, consider breaking into sub-skills
  - ❌ Non-goals section that just repeats the goal in negative form ("We do not fail")

| Add a "Good Example" snippet showing what concise, single-responsibility prose looks like | Template now teaches style, not just structure |

**Outcome:** Creators see quality standards *while* writing, not after.

---

### 7. Enhance process_classic_skill.md — fix errors, add anti-patterns

**Issues addressed:** #5 (duplicate numbering), #9 (quality principles not reinforced), #10 (no anti-patterns)

| Action | Change |
|--------|--------|
| Fix duplicate `4.` numbering in Phase 1 steps | Correctness |
| Add an **anti-patterns section** at the bottom: common mistakes new creators make | Prevents rework |
| Reference the simplicity principles explicitly during implementation: "Remember: single responsibility, clear scope, graceful handoff" | Quality is reinforced during creation |

---

### 8. Add pre-deploy compliance gate to deploy process

**Issues addressed:** #14 (no quality gate before deploy)

| Action | Change |
|--------|--------|
| Add a **Pre-deploy Check** step (Phase 0) in `skill_lifecycle.md` Phase 3: "Run compliance against the checklist. Do not deploy if any CRITICAL items fail." Remove standalone `process_deploy.md`. | Prevents broken deployments, eliminates duplication |

---

## Summary of File Changes

| File | What changes | Result |
|------|-------------|--------|
| `AGENTS.md` | Rewrite — lifecycle table, quality section, triggers, simplify to ~40 lines | One-page overview |
| `docs/checklist.md` | Add severity labels, evaluation criteria for each quality principle, Definition of Done | Self-evaluating rubric |
| `docs/process_classic_skill.md` | Removed — content merged into `skill_lifecycle.md` with anti-patterns and fixed numbering |
| `docs/process_comply.md` | Removed — content merged into `skill_lifecycle.md` |
| `docs/process_deploy.md` | Removed — content merged into `skill_lifecycle.md` Phase 3 with pre-deploy compliance gate
| `docs/skill_template.md` | Make Non-Goals mandatory, add anti-patterns + good example section, simplify language | Teaches quality during creation |
| `docs/taxonomy.md` | Fix count error, remove persona (or clarify as modifier), add exclusion rules, add adjacency map | Decisive category selection |

---

## Expected Outcome

After remediation:
- **Fewer files** — 4 docs files (checklist, skill_lifecycle, template, taxonomy) plus one PLAN doc
- **Every file reinforces quality** — beautiful simplicity is taught everywhere, not just in checklist checkboxes
- **No ambiguous references** — one docs directory, consistent paths, no phantom files
- **Deterministic compliance** — CRITICAL vs QUALITY distinction makes pass/fail meaningful
- **Creators are guided during creation** — template and process teach quality standards upfront
- **AGENTS.md is a single page** — anyone can understand the ecosystem in under 2 minutes
