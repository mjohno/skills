- [ ] **CRITICAL** `metadata.category` is present and matches a category in `docs/taxonomy.md`
- [ ] **CRITICAL** Description includes "Use when..." triggers
- [ ] **CRITICAL** Frontmatter: `disable-model-invocation: true` for shared contract/interface skills; absent otherwise
- [ ] **CRITICAL** SKILL.md is under 100 lines
- [ ] **CRITICAL** Under `# [Name]`: Goal (mandatory), Non-Goals (mandatory), Use-When (mandatory)
- [ ] **CRITICAL** Section 0: Prerequisites present
- [ ] **CRITICAL** Section 1: Inputs present (inline OR references/input_*.md / assets/input_*.md)
- [ ] **CRITICAL** Section 2: Processes present (inline OR references/process_*.md / assets/process_*.md)
- [ ] **CRITICAL** Section 3: Outputs present (inline OR references/output_*.md / assets/output_*.md)
- [ ] **CRITICAL** Section 4: Next Steps present (suggested downstream skills)
- [ ] **CRITICAL** Section 5: Examples present (at least one)
- [ ] **QUALITY** Writing is information dense and concise — no filler, no repetition
- [ ] **QUALITY** No time-sensitive info
- [ ] **QUALITY** Consistent terminology throughout
- [ ] **QUALITY** References one level deep (no nested external links)
- [ ] **QUALITY** Goals do not include multiple distinct objectives. If there are multiple, they should be split into separate skills.
- [ ] **QUALITY** Non-Goals do not invert the Goal. They add value by clarifying the scope of the Goal.
- [ ] **QUALITY** The list of processes is ideally 5 items. >=10 is a strong signal that the skill is doing too much and should be split.
- [ ] **QUALITY** **Single responsibility** — Does the skill describe one clear goal with at least one explicit non-goal?
- [ ] **QUALITY** **Human-aligned design** — Would a person naturally ask about this task? Does the prompt map directly to invoking it?
- [ ] **QUALITY** **Clear scope** — Fewest non-overlapping options, categories, or branches needed; no redundant logic
- [ ] **QUALITY** **Minimal default output** — Only essentials returned by default; detail is opt-in
- [ ] **QUALITY** **Graceful handoff** — When it can't solve something, does it suggest specific downstream skills (e.g., lookup, remember)?
- [ ] **QUALITY** **Structure matches purpose** — Sections flow logically (prerequisites → inputs → processes → outputs → next steps) and read like a contract

## Definition of Done

A skill passes compliance if all **CRITICAL** items pass. A beautifully simple skill also passes all **QUALITY** items.
