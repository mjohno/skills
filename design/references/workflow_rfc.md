# Workflow: RFC

## Context
Create a comprehensive Request for Comments (RFC) that defines the technical solution to a PRD's problem space. The RFC translates product requirements into architectural design, design decisions, and implementation guidance.

## Steps

### 1. Ingest PRD
- Read the provided PRD file
- Extract User Stories and Acceptance Criteria
- Identify the technical problem space that needs to be solved

### 2. Context & Exploration
- If existing system documentation is available, read it to understand current architecture
- Translate the PRD's problem space into a **technical problem statement** (do not repeat the user story)
- Anchor the RFC to the specific technical challenge: what needs to be built, changed, or integrated
- Reference the source PRD in the Context section

### 3. Persona Selection
- Ask: "What type of RFC is this?"
- Load the corresponding persona from `references/`:
  - Default: `persona_write_system_architect.md`
  - Extensible: add `persona_write_<name>.md` files as needed.
- The loaded persona shapes the design focus, depth, and priorities of the RFC.

### 4. Solution Design
Produce the following sections, guided by the loaded persona's domain focus:
- **Proposed Solution** — High-level technical approach
- **Design Decisions** — Key choices with rationale and alternatives
- **Architecture & Data Models** — System diagrams, data flow, API specs, schema definitions
- **Feasibility Assessment** — Technical constraints, resource requirements, timeline estimate

### 5. Alignment & Open Questions
- Map each PRD Acceptance Criterion to the corresponding RFC section
- List all open questions that need resolution before implementation

### 6. Decision Log
- Capture all significant design decisions in the Decision Log format:
  - Numbered sequentially (DEC-001, DEC-002, ...)
  - Each includes: Decision, Rationale, Alternatives Considered, Author, Status
  - Include a summary table at the top

### 7. Output
- Produce a complete `RFC-NNN-<name>.md` file using `assets/rfc_template.md`
- Set status to **Draft**
- Output a list of **recommended review personas** based on the RFC's scope:
  - Example: "This RFC touches infrastructure, auth, and data — recommend running review:architecture, review:security, and review:scalability."

## Patterns
- **Context**: Reference the PRD but do not repeat user stories — translate to technical problem
- **Design Decisions**: Each decision must include rationale and alternatives considered
- **Alignment Table**: One row per PRD Acceptance Criterion, mapped to RFC section
- **Decision Log**: Summary table + detailed entries; track status and superseding decisions
- **Review Recommendations**: Based on RFC scope (infrastructure → architecture, auth → security, etc.)

## Constraints
1. No implementation details — this is the design, not the code
2. All design decisions must include alternatives considered
3. Every PRD Acceptance Criterion must have an RFC mapping
4. No time-sensitive information (no dates that will expire)
5. Architecture diagrams should be described in text (ASCII/mermaid)
6. API specs must include request/response examples

## Outputs
- Complete RFC document with all mandatory sections
- Context (anchored to PRD, not repeating it)
- Proposed Solution
- Design Decisions (with rationale and alternatives)
- Architecture & Data Models
- Feasibility Assessment
- Alignment with PRD (Acceptance Criterion mapping table)
- Open Questions
- Decision Log (summary table + detail entries)
- Recommended review personas
