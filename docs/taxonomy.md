# Skill Taxonomy

This repository uses a role-based skill taxonomy.

## Categories

### interface
Shared contracts, schemas, protocols, or conventions used by other skills.
- Non-invocable by default (`disable-model-invocation: true` in frontmatter)
- Usually reference-only
- Defines how other skills should behave

### input
Retrieval skills that read or fetch source data.
- Returns raw or structured context
- Does not usually rewrite or persist

### enrich
Expansion skills that add context, associations, themes, implications, or candidate meaning.
- Increases informational richness
- Does not finalize decisions

### filter
Reduction skills that verify, rank, dedupe, select, or reject information.
- Decreases noise or uncertainty
- Can trace claims, apply rules, or enforce selection

### normalize
Canonicalization skills that reshape information into a standard form.
- Standardizes fields, naming, ordering, or structure
- Prepares content for storage or downstream use

### output
Writing skills that persist, store, or deliver results outward.
- Writes files, records, logs, or artifacts
- Usually the final persistence step

### map
Workflow composition skills that orchestrate multiple steps.
- Combines other skills and/or direct file operations
- Owns end-to-end execution of a process

### persona
Skills that encode a consistent perspective, tradeoff-awareness, or output style
across any pipeline stage.
- Provides perspective, voice, or evaluation criteria independent of data flow
- Composable with any other category (input, enrich, filter, etc.)
- Reduces total skill count by making each skill work across multiple viewpoints

## Notes

- Categories describe the skill's primary role in the pipeline.
- Skills may touch adjacent concerns, but their category should reflect the dominant behavior.
- `interface` skills define shared contracts and should not be auto-invoked.
- Refer to `docs/skill_template.md` for frontmatter format.
