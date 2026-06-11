# Migration from TODO

The old `todo` skill mixed multiple artifact responsibilities. Migrate by classifying each existing artifact.

| Old artifact or mode | New owner |
| --- | --- |
| TODO list as ordered work | `plan` |
| TODO item as implementation context | `task` |
| Inline `TODO(...)`, `DOIN(...)`, `DONE(...)` comments | `comment` for placement; `task` if converted into a packet |
| `mode:writer` | `plan` and/or `task` |
| `mode:commentor` | `comment` |
| `mode:cleanup` | `comment` or `plan`, depending on artifact |
| `mode:implementer` | out of scope |
| `mode:verifier` | out of scope |
| `mode:reviewer` | out of scope |

Rules:
- Preserve existing IDs when possible.
- Treat `TODO`, `DOIN`, and `DONE` as legacy status words, not skill domains.
- Do not infer implementation completion from migrated status alone.
- Prefer incremental migration: plans first, task packets only where context is needed.
