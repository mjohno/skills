# Mode: Write

This mode is used to create a comprehensive RFC from a PRD, user story, or high-level technical goal.

## Default Persona: System Architect
When no persona is specified, the **System Architect** persona is used by default.

## Workflow

### 1. Ingest
- Read the provided PRD, user story, or technical goal.
- Extract User Stories and Acceptance Criteria.
- Identify the technical problem space that needs to be solved.

### 2. Context & Exploration
- If existing system documentation is available, read it to understand current architecture.
- Translate the PRD's problem space into a **technical problem statement** (do not repeat the user story).
- Anchor the RFC to the specific technical challenge: what needs to be built, changed, or integrated.
- Reference the source PRD in the Context section.

### 3. Persona Selection
- Ask: "What type of RFC is this?"
- Load the corresponding persona from `references/`:
  - Default: `persona_write_system_architect.md`
  - Extensible: add `persona_write_<name>.md` files as needed.
- The loaded persona shapes the design focus, depth, and priorities of the RFC.

### 4. Solution Design (Persona-Guided)
Produce the following sections, guided by the loaded persona's domain focus:
- **Proposed Solution** — High-level technical approach.
- **Design Decisions** — Key choices with rationale and alternatives.
- **Architecture & Data Models** — System diagrams, data flow, API specs, schema definitions.
- **Feasibility Assessment** — Technical constraints, resource requirements, timeline estimate.

### 5. Alignment & Open Questions
- Map each PRD Acceptance Criterion to the corresponding RFC section.
- List all open questions that need resolution before implementation.

### 6. Decision Log
- Capture all significant design decisions in the Decision Log format:
  - Numbered sequentially (DEC-001, DEC-002, ...).
  - Each includes: Decision, Rationale, Alternatives Considered, Author, Status.
  - Include a summary table at the top.

### 7. Output
- Produce a complete `RFC-NNN-<name>.md` file.
- Set status to **Draft**.
- Output a list of **recommended review personas** based on the RFC's scope:
  - Example: "This RFC touches infrastructure, auth, and data — recommend running review:architecture, review:security, and review:scalability."
- The orchestrator determines which review modes to invoke.
