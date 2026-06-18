# Skill Manager

The Skill Manager system turns skill packages into composable, spec-compliant workflows that AI agents can discover, invoke, and compose with predictable structure and behavior.

## System Model

```
    ┌──────────────┐
    │   Prompt     │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐     type       ┌───────────────┐
    │  Gather      │───────────────▶│   Router      │
    │  Context     │   metadata.type│               │
    └──────────────┘                └───────┬───────┘
                                            │
                    ┌───────────────────────┼──────────────────────┐
                    ▼                       ▼                      ▼
              ┌──────────┐          ┌──────────┐          ┌──────────┐
              │ Create   │          │ Review   │          │ Deploy   │
              │ Classic  │          │ Any      │          │ Any      │
              └──────────┘          └──────────┘          └──────────┘
              ┌──────────┐          │
              │ Create   │          │
              │ Router   │          │
              └──────────┘          │
                                    ▼
                              ┌──────────┐
                              │ Comply   │
                              │ Any      │
                              └──────────┘

    Router ──selects──▶ Checklist (auto-detected) ──validates──▶ Pass/Fail
    Router ──selects──▶ Template (by type) ────scaffolds───────▶ New SKILL.md
```

## Types (State Definitions)

| Type | `metadata.type` | Structure | Validation |
|------|-----------------|-----------|------------|
| Classic | `skill` | SKILL.md + optional scripts/references/assets | 9-item checklist |
| Router  | `router` | SKILL.md + references/workflow_*.md + optional templates | 13-item checklist |

Types are not just labels — they determine which checklist runs, which template scaffolds, and which structural invariants apply.

## Workflows (State Transitions)

Each workflow is a **directed transformation**: it takes an input state, applies constrained steps, and produces an output state.

| Workflow | Input State | Output State | Checklist |
|----------|-------------|--------------|-----------|
| Create Classic | nothing | `skill/` with SKILL.md | `checklist.md` |
| Create Router  | nothing | `skill/` with SKILL.md + workflows | `router_checklist.md` |
| Review         | existing `skill/` | audit report (Critical vs Recommended) | auto-detected |
| Comply         | existing `skill/` | pass/fail result | auto-detected |
| Deploy         | local `skill/` | synchronized target | N/A |

Create workflows are **generative** (nothing → package). Review/Comply are **diagnostic** (package → assessment). Deploy is **translational** (local → target).

## System Invariants

- `metadata.type` is the single source of truth — every workflow and checklist branches on it
- 100-line SKILL.md cap applies uniformly across both types
- Only `#` and `##` headings define the routing contract; deeper sections are implementation detail
- Workflow files are self-contained — no cross-skill references
- All `## Constraints` sections use numbered lists (no checkboxes)

## Data Flow

```
Prompt → Gather Context → Route → [Template | Checklist | Workflow] → Output
```

- **Template path**: Router selects the correct template → scaffolds new SKILL.md
- **Checklist path**: Router detects type → selects checklist → validates
- **Workflow path**: Router dispatches to workflow file → executes constrained steps

The router is the only component that makes routing decisions. Everything else is deterministic: given a type, the checklist, template, and workflow are fixed.

## Control Flow (Router Internal)

```
Operation ──┬── create ──┬── classic → workflow_classic_skill.md
            │            └── router  → workflow_router_skill.md
            ├── review ──┬── skill  → checklist.md
            │            └── router → router_checklist.md
            ├── comply ──┬── skill  → checklist.md
            │            └── router → router_checklist.md
            └── deploy ──────────────→ workflow_deploy.md
```

Review and Comply share the same routing logic (detect type → select checklist) but differ in output: Review produces a categorized report; Comply produces pass/fail.

## Error Handling

- Missing `metadata.type` → Critical failure in both Review and Comply
- Default Route → Gather more information (router asks for clarification)
- Non-`skill`/non-`router` type → Critical failure
