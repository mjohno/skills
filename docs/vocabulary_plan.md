# Plan: Add Vocabulary Interface Type

PLAN_ID: PLAN-vocabulary-interface
Source: User decisions on replacing glossary with vocab/vocabulary semantics
Purpose: Align docs and add a non-model-invocable vocabulary interface pattern without overlapping verb skills.

## Source Summary
- User decisions: `glossary` pivots to `vocab`; frontmatter uses `metadata.type: vocabulary` and `metadata.category: interface` only, with no extra metadata.
- User decisions: vocabulary loads definitions into context when human-invoked and uses `disable_model_invocations: true` convention from AgentSkills.io.
- User decisions: vocabulary terms must not overlap with existing skill names/descriptions; skill descriptions remain the authoritative definitions for verb skills.
- User decisions: vocabulary terms are included in the `description` trigger, not separate frontmatter fields.
- User decisions: knowledge bases may have their own domain `glossary`; project-level `vocab` remains separate and clean.

## Gap Map
| Gap ID | Source Summary | Current Problem | Target State |
| --- | --- | --- | --- |
| GAP-1 | Taxonomy only allows `interface`, `skill`, and `persona` metadata types. | `metadata.type: vocabulary` would fail current taxonomy/compliance rules. | Taxonomy explicitly allows `type: vocabulary`, `category: interface` as a passive, human-loadable context contract. |
| GAP-2 | Interface docs assume all interface packages are model-selectable passive contracts. | Vocabulary requires a stricter non-invocable convention. | Interface docs distinguish normal interfaces from vocabulary interfaces using `disable_model_invocations: true`. |
| GAP-3 | Base/interface checklists validate only existing types and do not prevent term/skill overlap. | A vocab package could duplicate `modify`, `review`, or other verb skills. | Checklists require vocabulary terms not to duplicate existing skill names or skill-defined trigger meanings. |
| GAP-4 | Templates only cover normal interfaces, skills, and personas. | There is no canonical `vocab` SKILL.md shape. | Add a vocabulary template that contains no process behavior and keeps definitions in body content. |
| GAP-5 | No actual vocabulary package exists. | Users cannot human-load a project vocabulary before first prompt. | Add `src/interface/vocab/SKILL.md` with context-only terms and no overlap with skill names. |
| GAP-6 | Knowledge-base glossary and project vocab are not differentiated in docs. | Future authors may conflate global operational vocabulary with domain glossary content. | Docs state that KB glossaries are domain-local while `vocab` is project operational vocabulary. |

## Work Plan

### PLAN-vocabulary-interface-1 — Update taxonomy for vocabulary type
Closes: GAP-1, GAP-2
Source refs: `docs/taxonomy.md`
Status: done
Depends on: none
Outcome: Taxonomy recognizes vocabulary as a special interface-category package.

Deliverables:
- Add `vocabulary` to metadata type descriptions.
- Update valid pairs to include `type: vocabulary`, `category: interface`.
- Add a short `vocabulary` subsection or interface note: human-loadable, context-injecting, model-non-invocable, no process/output behavior.
- Clarify that vocabulary terms define words not already owned by skills; skills own their own trigger semantics.

Done when:
- `docs/taxonomy.md` makes `vocabulary/interface` valid.
- The taxonomy does not require extra metadata beyond `type`, `category`, and `disable_model_invocations: true`.

### PLAN-vocabulary-interface-2 — Add vocabulary compliance rules
Closes: GAP-3
Source refs: `docs/base_checklist.md`, `docs/interface_checklist.md`, `docs/vocab_checklist.md`
Status: done
Depends on: PLAN-vocabulary-interface-1
Outcome: Compliance checks support vocabulary packages and reject overlap with verb skills.

Deliverables:
- Update base checklist allowed `metadata.type` values to include `vocabulary`.
- Update valid pair rule to include `vocabulary/interface`.
- Add vocabulary-specific critical and quality checks in `docs/vocab_checklist.md`.
- Required checks: `disable_model_invocations: true`; description includes terms; no frontmatter term list; no overlap with existing skill package names or skill descriptions; no Inputs/Processes/Outputs sections.
- Required quality checks: terms are non-overlapping, stable project vocabulary, not synonyms for existing skills, and domain-local terms stay in KB glossaries.

Done when:
- A future `src/interface/vocab/SKILL.md` can pass compliance.
- A vocab term named `modify` would fail compliance because `modify` is already a skill-defined operation.

### PLAN-vocabulary-interface-3 — Add vocabulary template
Closes: GAP-4
Source refs: `docs/interface_template.md`, `docs/vocab_checklist.md`, `docs/vocab_template.md`
Status: done
Depends on: PLAN-vocabulary-interface-1
Outcome: Authors have a canonical minimal shape for vocabulary packages.

Deliverables:
- Add `docs/vocab_template.md` with frontmatter:
  - `name: vocab`
  - `description: Use when terms like x, y, z need definition.`
  - `disable_model_invocations: true`
  - `metadata.type: vocabulary`
  - `metadata.category: interface`
- Body sections should be minimal, for example: Goal, Non-Goals, Terms, Boundaries.
- Do not include Selection, Return, Next Steps, Inputs, Processes, or Outputs unless docs decide vocabulary should still use normal interface loading mechanics.

Done when:
- The template demonstrates context-only definition loading.
- The template contains no operational workflow language.

### PLAN-vocabulary-interface-4 — Document vocabulary vs KB glossary boundary
Closes: GAP-6
Source refs: `docs/taxonomy.md`, `docs/skill_lifecycle.md`, `docs/interface_template.md`
Status: done
Depends on: PLAN-vocabulary-interface-1
Outcome: Authors know when to use project vocab versus a knowledge-base glossary.

Deliverables:
- Add guidance: `vocab` is project operational vocabulary loaded before prompting; KB `glossary` is domain-local terminology inside a knowledge base.
- Add anti-examples: do not put `modify`, `review`, `draft`, or other skill-owned verbs in vocab.
- Add examples of valid vocab terms that are not skill names, such as `lean` if no `lean` skill exists.

Done when:
- Docs clearly separate project-level vocabulary from domain glossary content.

### PLAN-vocabulary-interface-5 — Add initial vocab package
Closes: GAP-5
Source refs: `src/interface/vocab/SKILL.md`, existing skill names under `src/*/*/SKILL.md`
Status: done
Depends on: PLAN-vocabulary-interface-2, PLAN-vocabulary-interface-3
Outcome: A human-loadable vocabulary package exists and follows the new rules.

Deliverables:
- Create `src/interface/vocab/SKILL.md` from the vocabulary template.
- Include only terms not already defined as skills.
- Candidate initial terms after overlap check:
  - `study`: read content to gather context; do not modify files; minimal/no response unless findings are requested.
  - `simplify`: reduce complexity while preserving required meaning/behavior.
  - `lean`: reduce overhead, waste, duplication, ceremony, or maintenance burden.
- Exclude `modify` because `src/output/modify/SKILL.md` already owns that operation.
- Consider excluding `refactor` unless no dedicated refactor skill exists and docs decide it is not already adequately owned by `modify` or another skill description.

Done when:
- `src/interface/vocab/SKILL.md` exists.
- Its description lists included terms.
- It has `disable_model_invocations: true`.
- It has no term that matches an existing skill name.

### PLAN-vocabulary-interface-6 — Verify consistency
Closes: GAP-1, GAP-2, GAP-3, GAP-4, GAP-5, GAP-6
Source refs: `docs/`, `src/interface/vocab/SKILL.md`, `src/*/*/SKILL.md`
Status: done
Depends on: PLAN-vocabulary-interface-5
Outcome: The repository consistently treats vocabulary as passive, human-loaded context.

Deliverables:
- Run a repository search for `glossary`, `vocab`, `vocabulary`, and `metadata.type` references.
- Compare vocab terms against skill names and descriptions.
- Run existing compliance process once updated.

Done when:
- No docs call vocab a normal invocable skill.
- No vocab term duplicates a skill-owned operation.
- KB glossary guidance remains separate from project vocab guidance.
