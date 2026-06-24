# Workflow: Generic Review

Default review workflow. See `workflow_base.md` for shared comparison and reporting logic.

## Context
Receives pre-built context from the router: target, spec (built-in or user-swap), lenses, and annotation hints.

## Steps
See `workflow_base.md` for the standard 5-step process.

### Unique Behavior
- Load built-in spec for detected artifact type (e.g., `spec_rfc.md`)
- If user provides a custom spec path, swap in that file instead
- Always apply `lens_generic.md`; add domain/persona lenses from hints
- Enrich criteria with any discovered `REVIEW(<id>)` annotations

## Finding Format
`P<n> - <issue> (source: <reference>)`
