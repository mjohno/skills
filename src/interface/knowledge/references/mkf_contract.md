# MKF Contract

## Basis

Matt's Knowledge Format (MKF) is expected to remain compliant with [Google Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), with local conventions for this skills ecosystem.

When MKF and OKF appear to conflict, preserve OKF compliance unless a future explicit decision updates this contract.

## Bundle Structure

```text
bundle-root/
├── index.md
├── concept.md
└── group/
    ├── index.md
    └── nested-concept.md
```

- A bundle is a filesystem directory tree.
- MKF concepts are Markdown files with YAML frontmatter.
- Concept ID is the bundle-relative file path without `.md`.
- `index.md` is a generated concept with `type: index`; `output/record` rebuilds generated indexes, while this interface only defines their shared contract.
- `log.md` is explicitly omitted and should be avoided in MKF. OKF treats it as optional, but MKF does not use it.

## Required Frontmatter

```yaml
---
type: undefined
title: Example Concept
description: A short description.
tags: []
---
```

Required fields:

- `type`
- `title`
- `description`
- `tags`

Rules:

- `tags: []` is valid.
- `resource` is optional.
- `timestamp` is not required and should not be auto-maintained. MKF omits it.
- Unknown frontmatter keys are allowed and should be preserved on update.

## Body Conventions

Concept bodies are Markdown. Structure depends on `type`.

Known types:

- `undefined`: free-form Markdown; include `# Citations` only when citations exist.
- `index`: generated directory listing for progressive disclosure, owned and rebuilt by `output/record`.
- `checklist`: quality checklist for reviews; may use headings and Markdown checkboxes.
- `template`: reusable LLM/agent processing template with placeholders and usage notes.

Unknown types are allowed; consumers should tolerate them.

## Links and Citations

- Use standard Markdown links.
- Prefer stable bundle-relative links when possible.
- Use a bottom `# Citations` section when source-backed claims need attribution.

## Shared Boundary

This contract is shared by lookup and record. Search ranking belongs to lookup. Writing, duplicate handling, validation scripts, templates, and index rebuilding belong to record.
