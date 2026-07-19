# Interface Checklist

## Base Checklist

Inherits all items from [base_checklist.md](base_checklist.md). Apply base items before these interface-specific items.

## Interface-Specific CRITICAL

- [ ] **CRITICAL** `metadata.type: interface`
- [ ] **CRITICAL** `metadata.category: interface`
- [ ] **CRITICAL** Under `# [Name]`: Goal (mandatory), Non-Goals (mandatory), Use-When (mandatory)
- [ ] **CRITICAL** Section 0: Prerequisites present
- [ ] **CRITICAL** Section 1: Inputs present
- [ ] **CRITICAL** Section 2: Process present
- [ ] **CRITICAL** Section 3: Outputs present
- [ ] **CRITICAL** Section 4: Next Steps present
- [ ] **CRITICAL** Section 5: Examples present, including a prompt and returned file path/content blocks
- [ ] **CRITICAL** Outputs identify selected reference and asset paths when package-local references/assets are required
- [ ] **CRITICAL** Outputs require loaded reference/asset contents to be returned in fenced code blocks
- [ ] **CRITICAL** Interface defines contract data only and does not create, modify, evaluate, persist, retrieve external data, or orchestrate work

## Interface-Specific QUALITY

- [ ] **QUALITY** Interface defines a noun/domain desired state, not production behavior.
- [ ] **QUALITY** Interface exposes conventions, quality checks, templates, schemas, protocol rules, artifact shapes, or storage rules for consumers.
- [ ] **QUALITY** Generic rules are separated from language/platform-specific domains when domains exist.
- [ ] **QUALITY** Domain-specific assets are clearly named.
- [ ] **QUALITY** Templates are examples or canonical shapes consumed by verb skills, not mandatory generation behavior unless explicitly stated.
- [ ] **QUALITY** Minimal default output includes only selected domain, assumptions, paths, and loaded selected contents.
- [ ] **QUALITY** Missing or unsupported domains are stated as assumptions/unknowns with a concrete handoff.
- [ ] **QUALITY** Examples show both the returned path block and the returned file-content block.

## Definition of Done

An interface passes compliance if all base CRITICAL items and all interface-specific CRITICAL items pass. A beautifully simple interface also passes all QUALITY items.
