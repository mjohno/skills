# Skill Checklist

## Base Checklist

Inherits all items from [base_checklist.md](base_checklist.md). Apply base items before these skill-specific ones.

## Skill-Specific CRITICAL

- [ ] **CRITICAL** Under `# [Name]`: Goal (mandatory), Non-Goals (mandatory), Use-When (mandatory)
- [ ] **CRITICAL** Section 0: Prerequisites present
- [ ] **CRITICAL** Section 1: Inputs present (inline OR references/input_*.md / assets/input_*.md)
- [ ] **CRITICAL** Section 2: Processes present (inline OR references/process_*.md / assets/process_*.md)
- [ ] **CRITICAL** Section 3: Outputs present (inline OR references/output_*.md / assets/output_*.md)
- [ ] **CRITICAL** Section 4: Next Steps present (suggested downstream skills)
- [ ] **CRITICAL** Section 5: Examples present (at least one)

## Skill-Specific QUALITY

- [ ] **QUALITY** Goals do not include multiple distinct objectives. If there are multiple, they should be split into separate skills.
- [ ] **QUALITY** Non-Goals do not invert the Goal. They add value by clarifying the scope of the Goal.
- [ ] **QUALITY** The list of processes is ideally 5 items. >=10 is a strong signal that the skill is doing too much and should be split.
- [ ] **QUALITY** **Clear scope** — Fewest non-overlapping options, categories, or branches needed; no redundant logic
- [ ] **QUALITY** **Minimal default output** — Only essentials returned by default; detail is opt-in
- [ ] **QUALITY** **Graceful handoff** — When it can't solve something, does it suggest specific downstream skills (e.g., lookup, remember)?
- [ ] **QUALITY** **Structure matches purpose** — Sections flow logically (prerequisites → inputs → processes → outputs → next steps) and read like a contract

## Interface-Specific QUALITY

Apply these when `metadata.category: interface`.

- [ ] **QUALITY** Interface defines a noun/domain desired state, not production behavior.
- [ ] **QUALITY** Interface exposes conventions, quality checks, templates, schemas, or protocol rules for consumers.
- [ ] **QUALITY** Interface does not claim to create, modify, evaluate, persist, retrieve, or orchestrate artifacts.
- [ ] **QUALITY** Generic rules are separated from language/platform-specific profiles when profiles exist.
- [ ] **QUALITY** Profile-specific assets are clearly named.
- [ ] **QUALITY** Templates are examples or canonical shapes consumed by verb skills, not mandatory generation behavior unless explicitly stated.

## Definition of Done

A skill passes compliance if all base CRITICAL items and all skill-specific CRITICAL items pass. A beautifully simple skill also passes all QUALITY items.
