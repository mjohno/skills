# Migration from TODO

The old `todo` skill mixed multiple artifact responsibilities. Migrate by classifying each existing artifact.

| Old artifact or mode | New owner |
| --- | --- |
| TODO list as ordered work | `plan` |
| TODO item as implementation context | `task` |
| Inline `TODO(...)`, `CHECK(...)`, `REVIEW(...)`, `DONE(...)` annotations | `annotate` for placement; `task` if converted into a packet |
| `mode:writer` | `plan` and/or `task` |
| `mode:annotator` | `annotate` |
| `mode:cleanup` | `annotate` or `plan`, depending on artifact |
| `mode:implementer` | out of scope |
| `mode:verifier` | out of scope |
| `mode:reviewer` | out of scope |

Rules:
- Preserve existing IDs when possible.
- Treat `TODO`, `CHECK`, `REVIEW`, and `DONE` as annotation kinds managed by `annotate`, not skill domains.
- Do not infer implementation completion from migrated status alone.
- Prefer incremental migration: plans first, task packets only where context is needed.
