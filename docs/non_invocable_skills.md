# Non-Invocable Skills

Non-invocable skills are `interface`-category skill packages defined by `docs/taxonomy.md`. They provide shared contracts, interfaces, schemas, or reference behavior for other skills, but should not compete for automatic model invocation.

Use a non-invocable skill when the package needs the structure and relative assets of a skill directory, but the user should normally invoke a concrete input, output, enrich, filter, normalize, or map skill instead.

## Frontmatter

Set `disable-model-invocation: true` in the skill frontmatter:

```yaml
---
name: knowledge-base-interface
description: Use when a lookup or record skill needs the shared knowledge base interface contract. Reference-only; not normally invoked directly.
disable-model-invocation: true
metadata:
  type: skill
  category: interface
  capabilities:
    - knowledge-base
---
```

## Expected behavior

- The skill is hidden from automatic model invocation.
- The skill may still be loaded explicitly when another skill references it.
- The skill should describe a contract, schema, protocol, or shared interface.
- Concrete user-facing behavior should live in invocable skills.
- Its category should be `interface`.

## Good uses

- `interface/knowledge-base` — shared root, search, citation, and write-safety contract for `lookup` and `record`.
- `interface/memory` — shared memory location, section, backup, and update-safety contract for `remember`, `memorize`, and `dream`.
- Shared schemas or protocols that multiple skills consume.

## Avoid

Do not make a skill non-invocable if users should call it directly for a concrete task. For example, `lookup`, `record`, `remember`, and `memorize` should remain invocable because they represent user-facing actions.
