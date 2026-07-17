# Base Checklist

Shared compliance items for all skills — personas and data-flow skills alike. Included by each type-specific checklist.

## CRITICAL

- [ ] **CRITICAL** `metadata.category` is present and matches a category in `docs/taxonomy.md`
- [ ] **CRITICAL** Description includes "Use when..." triggers
- [ ] **CRITICAL** Interface skills define contract data only and do not perform retrieval, transformation, evaluation, persistence, or orchestration
- [ ] **CRITICAL** SKILL.md is under 100 lines

## QUALITY

- [ ] **QUALITY** Writing is information dense and concise — no filler, no repetition
- [ ] **QUALITY** No time-sensitive info
- [ ] **QUALITY** Consistent terminology throughout
- [ ] **QUALITY** References one level deep (no nested external links)
- [ ] **QUALITY** **Single responsibility** — Does the skill describe one clear goal or perspective with at least one explicit non-goal or acknowledged tradeoff?
- [ ] **QUALITY** **Human-aligned design** — Would a person naturally ask about this task? Does the prompt map directly to invoking it?

## Definition of Done

All CRITICAL items must pass for any skill to be considered compliant. A beautifully simple skill also passes all QUALITY items.
