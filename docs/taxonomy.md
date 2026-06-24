# Skill Taxonomy

This repository uses a role-based skill taxonomy. Each category defines the skill's primary role in the pipeline.

## Categories

### interface
Shared contracts, schemas, protocols, or conventions used by other skills.
- Non-invocable by default (`disable-model-invocation: true` in frontmatter)
- Usually reference-only
- Defines how other skills should behave
- **Do NOT use if** the skill performs data transformation, retrieval, or output — it only defines contracts

### input
Retrieval skills that read or fetch source data.
- Returns raw or structured context
- Does not usually rewrite or persist
- **Do NOT use if** the skill transforms, analyzes, or persists the data — it only retrieves it

### enrich
Expansion skills that add context, associations, themes, implications, or candidate meaning.
- Increases informational richness
- Does not finalize decisions
- **Do NOT use if** the skill reduces information, makes a decision, or persists results — it only adds

### filter
Reduction skills that verify, rank, dedupe, select, or reject information.
- Decreases noise or uncertainty
- Can trace claims, apply rules, or enforce selection
- **Do NOT use if** the skill expands information, retrieves raw data, or writes final output — it only evaluates

### normalize
Canonicalization skills that reshape information into a standard form.
- Standardizes fields, naming, ordering, or structure
- Prepares content for storage or downstream use
- **Do NOT use if** the skill retrieves external data, makes decisions, or produces final deliverables — it only reformats

### output
Writing skills that persist, store, or deliver results outward.
- Writes files, records, logs, or artifacts
- Usually the final persistence step
- **Do NOT use if** the skill analyzes information, composes workflows, or just formats data — it writes final results

### map
Workflow composition skills that orchestrate multiple steps.
- Combines other skills and/or direct file operations
- Owns end-to-end execution of a process
- **Do NOT use if** the skill performs a single focused task — it only orchestrates others

### persona
Skills that encode a consistent perspective, tradeoff-awareness, or output style across any pipeline stage.
- Provides perspective, voice, or evaluation criteria independent of data flow
- **Modifies how information flows** through the system — a persona skill wraps or augments a data-flow category (e.g., input + persona produces filtered views; filter + persona applies review lens)
- Composable with any data-flow category
- Reduces total skill count by making each skill work across multiple viewpoints
- **Do NOT use if** the skill's primary role is data retrieval, transformation, or persistence — it only modifies perspective

## Composition Patterns

Personas modify how information is evaluated at any pipeline stage. Practical patterns:

- **Review + persona:security** — Run `/skill:review` and specify the security persona as the evaluation lens instead of (or in addition to) a generic perspective.
- **Grill + persona:adversarial** — Run `grill-me` on a design, then re-evaluate its output through the adversarial persona to surface residual risks the interview missed.
- **Collect + persona:security** — When collecting external resources, ask for security-relevant findings only (e.g., CVEs, exposure reports) rather than a general landscape scan.

The pattern is: [data-flow skill] → pass artifacts → [persona] as evaluation lens. The persona does not replace the data-flow skill; it sharpens what that skill looks for and how it presents findings.

## Notes

- Categories describe the skill's primary role. Skills may touch adjacent concerns, but their category reflects the dominant behavior.
- `interface` skills define shared contracts and should not be auto-invoked.
- Refer to [skill_template.md](skill_template.md) for frontmatter format.
