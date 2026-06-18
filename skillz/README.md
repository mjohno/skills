# skillz

The `skillz` system manages spec-compliant AgentSkills.io skill packages. Skills are stateless transforms that operate on raw context data with optional file I/O, chained implicitly via soft coupling (prerequisites → next steps).

## System Model

```
    ┌──────────────┐
    │   Prompt     │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │  Gather      │──operation──▶ [workflow]
    │  Context     │
    └──────────────┘
           │
    ┌──────┴───────┐
    ▼              ▼
┌────────┐    ┌────────┐
│ Create │    │ Comply │
└────────┘    └────────┘
┌────────┐    ┌────────┐
│ Review │    │ Deploy │
└────────┘    └────────┘
```

## Categories (State Definitions)

| Category | `metadata.category` | Description |
|----------|---------------------|-------------|
| discover | `discover` | Find, collect, or surface information |
| extract | `extract` | Pull structured data from unstructured sources |
| transform | `transform` | Restructure, analyze, or synthesize data |
| load | `load` | Persist, store, or deliver data |
| orchestrate | `orchestrate` | Coordinate multi-step workflows |
| meta | `meta` | Manage, validate, or describe other skills |

Category is the single source of truth for skill classification. It replaces the deprecated `metadata.type`.

## Workflows (State Transitions)

Each workflow is a **directed transformation**: it takes an input state, applies constrained steps, and produces an output state.

| Workflow | Input State | Output State | Checklist |
|----------|-------------|--------------|-----------|
| Create | nothing | `skill/` with SKILL.md | `checklist.md` |
| Review | existing `skill/` | audit report (Critical vs Recommended) | auto-detected |
| Comply | existing `skill/` | pass/fail result | `checklist.md` |
| Deploy | local `skill/` | synchronized target | N/A |

Create workflows are **generative** (nothing → package). Review/Comply are **diagnostic** (package → assessment). Deploy is **translational** (local → target).

## System Invariants

- `metadata.category` is the single source of truth — one of six valid categories
- 100-line SKILL.md cap applies uniformly
- Only `#` and `##` headings define the routing contract; deeper sections are implementation detail
- Workflow files are self-contained — no cross-skill references
- All `## Constraints` sections use numbered lists (no checkboxes)
- No router skills — skills chain implicitly via soft coupling (prerequisites → next steps)

## Data Flow

```
Prompt → Gather Context → [Template | Checklist | Workflow] → Output
```

- **Template path**: Use `assets/skill_template.md` → scaffolds new SKILL.md
- **Checklist path**: Use `assets/checklist.md` → validates
- **Workflow path**: Dispatch to workflow file → executes constrained steps

## File Classification

Files in `references/` and `assets/` can use an optional `type` field in their frontmatter:
- `type: template` — .md templates
- `type: input` — expected input formats
- `type: output` — expected output formats
- `type: process` — procedural reference docs
- `type: spec` — specification documents

## Error Handling

- Missing `metadata.category` → Critical failure in both Review and Comply
- Default Route → Gather more information (ask for clarification)
- Non-valid category → Critical failure
