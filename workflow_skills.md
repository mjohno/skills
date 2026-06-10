# Engineering Workflow: Skill Specifications

## Architectural Philosophy: Capability-First vs. Persona-First

This system utilizes a **Capability-First** architecture. A **Skill** is not defined by a persona (the "How"), but by its **Domain Capability** (the "What").

### The Mechanism: Capability + Injectable Persona
* **The Skill (The Capability):** Acts as a specialized sandbox. It is pre-bound to a specific domain's tools, data access, file permissions, and technical constraints (e.g., the `prd` skill has access to requirements templates and stakeholder docs).
* **The Persona (The Intent):** Injected at runtime via **Progressive Disclosure**. The orchestrator selects a persona (a set of reference materials) to shape the *style*, *focus*, and *cognitive bias* of the capability.

### Why not "Persona-First"?
The alternative—a "Persona-First" model (e.g., a generic `writer` skill that accepts a `prd_capability` input)—was rejected for the following reasons:

1.  **The Tooling & Permission Gap:** A persona-first model requires either a "God-Skill" with broad, unsafe permissions (violating the Principle of Least Privilege) or a highly complex orchestrator capable of dynamically granting tools and data access to a generic skill.
2.  **Complexity Shift:** In a persona-first model, the complexity of the system is pushed into the **Orchestrator** (managing tool-injection logic). In a capability-first model, the complexity is localized within the **Skill**, making the orchestrator simpler and the overall system more robust.
3.  **Sandbox Integrity:** Capability-based skills provide a natural boundary. It is easier to ensure a `prd` skill stays within its domain than to ensure a generic `writer` skill doesn't overstep its bounds.

---

## II. Skill Registry

Each skill below represents a technical capability. The `mode` indicates the **Injectable Persona** used to guide the execution.

### 1. `prd` (Product Requirements Domain)
* **Description:** Capability to manage, manipulate, and reason about product requirement artifacts.
* **Engagement Modes:**
    * **`mode: write`** $\rightarrow$ *Injects: Product Strategist* (Focus: Creation, Empathy, S.M.A.R.T. structure)
    * **`mode: review`** $\rightarrow$ *Injects: Critical Analyst* (Focus: Skepticism, Edge cases, Ambiguity)
    * **`mode: validate`** $\rightarrow$ *Injects: Compliance Auditor* (Focus: Strict S.M.A.R.T. verification)
* **Primary Artifacts:** `PRD.md`, User Stories, Acceptance Criteria (AC).

### 2. `rfc` (Technical Design Domain)
* **Description:** Capability to design technical solutions and ensure architectural alignment.
* **Engagement Modes:**
    * **`mode: write`** $\rightarrow$ *Injects: System Architect* (Focus: Design, API specs, Data models)
    * **`mode: review`** $\rightarrow$ *Injects: Peer Reviewer* (Focus: Scalability, Security, Edge cases)
    * **`mode: validate`** $\rightarrow$ *Injects: Alignment Specialist* (Focus: RFC vs. PRD compliance)
* **Primary Artifacts:** `RFC.md`, System Diagrams, API Specs.

### 3. `adr` (Architectural Decision Domain)
* **Description:** Capability to capture and preserve the rationale behind significant architectural choices.
* **Engagement Modes:**
    * **`mode: write`** $\rightarrow$ *Injects: Decision Recorder* (Focus: Context, Rationale, Alternatives)
    * **`mode: review`** $\rightarrow$ *Injects: Historian* (Focus: Consistency with previous ADRs)
    * **`mode: validate`** $\rightarrow$ *Injects: Auditor* (Focus: Permanence and Clarity)
* **Primary Artifacts:** `ADR_XXX.md`.

### 4. `task` (Work Decomposition Domain)
* **Description:** Capability to break down high-level designs into granular engineering work.
* **Engagement Modes:**
    * **`mode: decompose`** $\rightarrow$ *Injects: Task Planner* (Focus: I.N.V.E.S.T. decomposition)
    * **`mode: review`** $\rightarrow$ *Injects: Scoping Specialist* (Focus: Task independence and size)
    * **`mode: validate`** $\rightarrow$ *Injects: Scope Auditor* (Focus: Coverage of the RFC)
* **Primary Artifacts:** Task Lists, Jira/Linear Tickets, GitHub Issues.

### 5. `implementation` (Engineering Domain)
* **Description:** Capability to translate technical designs into high-quality code.
* **Engagement Modes:**
    * **`mode: write`** $\rightarrow$ *Injects: Software Engineer* (Focus: Implementation, Unit tests)
    * **`mode: review`** $\rightarrow$ *Injects: Code Reviewer* (Focus: Patterns, Style, Logic)
    * **`mode: validate`** $\rightarrow$ *Injects: CI/CD Runner* (Focus: Automated test/lint pass)
* **Primary Artifacts:** Source Code, Unit Tests, Pull Requests (PRs).

### 6. `verification` (Quality Assurance Domain)
* **Description:** Capability to confirm the implementation meets functional and technical intent.
* **Engagement Modes:**
    * **`mode: test`** $\rightarrow$ *Injects: QA Engineer* (Focus: Integration, Manual, UAT)
    * **`mode: review`** $\rightarrow$ *Injects: Bug Analyst* (Focus: Failure logs, bug reports)
    * **`mode: validate`** $\rightarrow$ *Injects: Requirements Validator* (Focus: Formal AC sign-off)
* **Primary Artifacts:** Test Reports, Bug Reports, Validation Sign-offs.

### 7. `deployment` (Infrastructure Delivery Domain)
* **Description:** The technical act of moving verified code into the production environment.
* **Engagement Modes:**
    * **`mode: plan`** $\rightarrow$ *Injects: DevOps Engineer* (Focus: Deployment strategies)
    * **`mode: execute`** $\rightarrow$ *Injects: Release Orchestrator* (Focus: Technical rollout)
    * **`mode: monitor`** $\rightarrow$ *Injects: SRE* (Focus: Infrastructure smoke tests/health)
* **Primary Artifacts:** Deployment Plans, CI/CD Pipelines, Infrastructure Logs.

### 8. `release` (Feature Delivery Domain)
* **Description:** The business-controlled act of making features available to users.
* **Engagement Modes:**
    * **`mode: control`** $\rightarrow$ *Injects: Product Owner* (Focus: Feature flags, user segments)
    * **`mode: schedule`** $\rightarrow$ *Injects: Release Manager* (Focus: Market timing, coordination)
    * **`mode: manage`** $\rightarrow$ *Injects: Rollout Specialist* (Focus: Canary/Gradual rollouts)
* **Primary Artifacts:** Feature Flag Configs, Release Notes, Rollout Schedules.

### 9. `observability` (Telemetry Domain)
* **Description:** Capability to monitor system health and user behavior for ground truth.
* **Engagement Modes:**
    * **`mode: collect`** $\rightarrow$ *Injects: Data Aggregator* (Focus: Logs, metrics, traces)
    * **`mode: analyze`** $\rightarrow$ *Injects: Data Scientist* (Focus: KPI vs. RFC/PRD targets)
    * **`mode: report`** $\rightarrow$ *Injects: Insights Generator* (Focus: Retrospective-ready reports)
* **Primary Artifacts:** Dashboards, Performance Reports, User Behavior Analytics.

### 10. `retrospective` (Meta-Review Domain)
* **Description:** Capability to facilitate high-level reviews of the business, technical, or procedural processes.
* **Engagement Modes:**
    * **`mode: facilitate`** $\rightarrow$ *Injects: Facilitator* (Focus: Business, Technical, or Procedural review)
    * **`mode: update`** $\rightarrow$ *Injects: Process Engineer* (Focus: Workflow/Template refinement)
* **Primary Artifacts:** Retrospective Reports, Updated Workflow/Templates.
