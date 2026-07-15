# Skill Taxonomy

This repository uses a role-based skill taxonomy. Each category defines the skill's primary role in the system.

## Mental Model

- **Nouns are interfaces** — artifact schemas, storage contracts, protocols, and canonical shapes.
- **Verbs are invocable skills** — skills that retrieve, expand, reduce, produce, persist, or orchestrate work.
- **Personas are lenses** — perspectives that modify how another skill evaluates or presents information.

## Categories

### interface
Shared contracts, schemas, protocols, artifact shapes, or conventions used by other skills.
- Non-invocable by default (`disable-model-invocation: true` in frontmatter)
- Lives as direct skill packages under `src/interface/<name>/SKILL.md`
- Examples: `interface/prd`, `interface/rfc`, `interface/plan`, `interface/task`, `interface/code`, `interface/prose`, `interface/script`, `interface/prototype`, `interface/memory`, `interface/knowledge-base`
- Defines how other skills should shape content or interact with storage
- **Do NOT use if** the skill performs retrieval, transformation, evaluation, persistence, or orchestration — it only defines contracts

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

### output
Verb-shaped production skills that create, revise, persist, store, or deliver results outward.
- Performs production actions such as outline, draft, modify, record, memorize, or commit
- Consumes interface-defined artifact nouns and storage contracts when structure matters
- May write files, records, logs, or artifacts when requested
- **Do NOT use if** the skill only defines an artifact schema or canonical form — use an interface skill for nouns

### map
Workflow composition skills that orchestrate multiple steps.
- Combines other skills and/or direct file operations
- Owns end-to-end execution of a process
- **Do NOT use if** the skill performs a single focused task — it only orchestrates others

### persona
Skills that encode a consistent perspective, tradeoff-awareness, or output style across any pipeline stage.
- Provides perspective, voice, or evaluation criteria independent of data flow
- **Modifies how information flows** through the system — a persona skill wraps or augments a data-flow category
- Composable with any invocable skill
- Reduces total skill count by making each skill work across multiple viewpoints
- **Do NOT use if** the skill's primary role is data retrieval, transformation, persistence, orchestration, or contract definition — it only modifies perspective

## Composition Patterns

Interfaces define shapes that invocable skills consume:

- **interface/prd + output/draft** — Draft a PRD using the PRD contract.
- **interface/code + output/modify** — Modify code while preserving code-brief boundaries and verification hints.
- **interface/knowledge-base + output/record** — Record durable knowledge using the KB root and entry contract.
- **interface/memory + output/memorize** — Append memory using the memory file and entry contract.

Personas modify how information is evaluated at any pipeline stage:

- **review + persona/security** — Run `review` with the security persona as the evaluation lens.
- **grill-me + persona/adversarial** — Stress-test a design, then re-evaluate residual risks through the adversarial persona.
- **collect + persona/security** — Collect security-relevant findings only, such as CVEs or exposure reports.

## Notes

- Categories describe the skill's primary role. Skills may touch adjacent concerns, but their category reflects the dominant behavior.
- `interface` skills define shared contracts and should not be auto-invoked.
- Refer to [skill_template.md](skill_template.md) for frontmatter format.
