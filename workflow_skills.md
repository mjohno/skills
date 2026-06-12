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
    * **`mode: write`** $
ightarrow$ *Injects: Product Strategist* (Focus: Creation, Empathy, S.M.A.R.T. structure)
    * **`mode: review`** $
ightarrow$ *Injects: Critical Analyst* (Focus: Skepticism, Edge cases, Ambiguity)
    * **`mode: validate`** $
ightarrow$ *Injects: Compliance Auditor* (Focus: Strict S.M.A.R.T. verification)
* **Primary Artifacts:** `PRD.md`, User Stories, Acceptance Criteria (AC).

### 2. `rfc` (Technical Design Domain)
* **Description:** Capability to design technical solutions and ensure architectural alignment.
* **Engagement Modes:**
    * **`mode: write`** $
ightarrow$ *Injects: System Architect* (Focus: Design, API specs, Data models)
    * **`mode: review`** $
ightarrow$ *Injects: Peer Reviewer* (Focus: Scalability, Security, Edge cases)
    * **`mode: validate`** $
ightarrow$ *Injects: Alignment Specialist* (Focus: RFC vs. PRD compliance)
    * **`mode: manager`** $
ightarrow$ *Injects: RFC Curator* (Focus: RFC index maintenance, lifecycle status tracking)
* **Primary Artifacts:** `RFC.md`, System Diagrams, API Specs.

### 3. `plan` (Work Planning Domain)
* **Description:** Capability to turn approved intent into ordered, gap-closing work plans.
* **Workflows:**
    * **Create Plan** $
ightarrow$ *Injects: Planner* (Focus: Gap mapping, ordering, dependencies)
    * **Update Plan** $
ightarrow$ *Injects: Planner* (Focus: Preserve IDs, add/split/merge/reorder, gap closure)
    * **Check Plan Shape** $
ightarrow$ *Injects: Plan Auditor* (Focus: Every gap has a closing item, items name their gap)
* **Primary Artifacts:** Plans, Gap Maps, Ordered Work Items.

### 4. `task` (Work Decomposition Domain)
* **Description:** Capability to break down plans and high-level designs into portable task packets and granular engineering work.
* **Workflows:**
    * **Create Task Packet** $
ightarrow$ *Injects: Task Planner* (Focus: I.N.V.E.S.T. decomposition, stable IDs)
    * **Extract Task Packet** $
ightarrow$ *Injects: Task Planner* (Focus: Copy relevant context, preserve source references)
    * **Update or Normalize Task Packet** $
ightarrow$ *Injects: Scope Auditor* (Focus: Preserve ID, keep fields concise, no false certainty)
* **Primary Artifacts:** Task Packets, Task Lists, Jira/Linear Tickets, GitHub Issues.

### 5. `implementation` (Engineering Domain)
* **Description:** Capability to translate technical designs into high-quality code.
* **Engagement Modes:**
    * **`mode: write`** $
ightarrow$ *Injects: Software Engineer* (Focus: Implementation, Unit tests)
    * **`mode: review`** $
ightarrow$ *Injects: Code Reviewer* (Focus: Patterns, Style, Logic)
    * **`mode: validate`** $
ightarrow$ *Injects: CI/CD Runner* (Focus: Automated test/lint pass)
* **Primary Artifacts:** Source Code, Unit Tests, Pull Requests (PRs).

### 6. `verification` (Quality Assurance Domain)
* **Description:** Capability to confirm the implementation meets functional and technical intent.
* **Engagement Modes:**
    * **`mode: test`** $
ightarrow$ *Injects: QA Engineer* (Focus: Integration, Manual, UAT)
    * **`mode: review`** $
ightarrow$ *Injects: Bug Analyst* (Focus: Failure logs, bug reports)
    * **`mode: validate`** $
ightarrow$ *Injects: Requirements Validator* (Focus: Formal AC sign-off)
* **Primary Artifacts:** Test Reports, Bug Reports, Validation Sign-offs.

### 7. `deployment` (Infrastructure Delivery Domain)
* **Description:** The technical act of moving verified code into the production environment.
* **Engagement Modes:**
    * **`mode: plan`** $
ightarrow$ *Injects: DevOps Engineer* (Focus: Deployment strategies)
    * **`mode: execute`** $
ightarrow$ *Injects: Release Orchestrator* (Focus: Technical rollout)
    * **`mode: monitor`** $
ightarrow$ *Injects: SRE* (Focus: Infrastructure smoke tests/health)
* **Primary Artifacts:** Deployment Plans, CI/CD Pipelines, Infrastructure Logs.

### 8. `release` (Feature Delivery Domain)
* **Description:** The business-controlled act of making features available to users.
* **Engagement Modes:**
    * **`mode: control`** $
ightarrow$ *Injects: Product Owner* (Focus: Feature flags, user segments)
    * **`mode: schedule`** $
ightarrow$ *Injects: Release Manager* (Focus: Market timing, coordination)
    * **`mode: manage`** $
ightarrow$ *Injects: Rollout Specialist* (Focus: Canary/Gradual rollouts)
* **Primary Artifacts:** Feature Flag Configs, Release Notes, Rollout Schedules.

### 9. `observability` (Telemetry Domain)
* **Description:** Capability to monitor system health and user behavior for ground truth.
* **Engagement Modes:**
    * **`mode: collect`** $
ightarrow$ *Injects: Data Aggregator* (Focus: Logs, metrics, traces)
    * **`mode: analyze`** $
ightarrow$ *Injects: Data Scientist* (Focus: KPI vs. RFC/PRD targets)
    * **`mode: report`** $
ightarrow$ *Injects: Insights Generator* (Focus: Retrospective-ready reports)
* **Primary Artifacts:** Dashboards, Performance Reports, User Behavior Analytics.

### 10. `retrospective` (Meta-Review Domain)
* **Description:** Capability to facilitate high-level reviews of the business, technical, or procedural processes.
* **Engagement Modes:**
    * **`mode: facilitate`** $
ightarrow$ *Injects: Facilitator* (Focus: Business, Technical, or Procedural review)
    * **`mode: update`** $
ightarrow$ *Injects: Process Engineer* (Focus: Workflow/Template refinement)
* **Primary Artifacts:** Retrospective Reports, Updated Workflow/Templates.

---

## III. Utility Skills

The following skills are not part of the core workflow but support it. They operate on whatever input they are given and do not create cross-skill coupling.

### 1. `comment` (Inline Annotation Domain)
* **Description:** Manage file-local comments in code and documents. Use when you need to add, update, find, normalize, or remove comments without deciding or executing work.
* **Workflows:** Add Comment, Update or Remove Comment, Normalize Comment.
* **Primary Artifacts:** Inline comments with stable IDs and purpose tags.

### 2. `writing` (Prose Quality Domain)
* **Description:** A unified writing skill for reviewing and drafting English prose. Use when you need to critique prose for readability, density, and style, or generate polished prose from notes, drafts, or rough ideas.
* **Engagement Modes:**
    * **`mode: review`** $
ightarrow$ *Injects: Prose Critic* (Focus: Readability, density, style, ranked findings)
    * **`mode: write`** $
ightarrow$ *Injects: Prose Polisher* (Focus: Drafting, polishing, voice preservation)
* **Primary Artifacts:** Reviewed prose, polished drafts.

### 3. `git-commit` (Version Control Domain)
* **Description:** Generates and executes a git commit adhering to the Conventional Commits specification. Used when you need to make a commit.
* **Workflows:** Pre-flight check, analyze changes, draft message, review & approval, execute commit.
* **Primary Artifacts:** Git commits with Conventional Commits formatted messages.

### 4. `grill-me` (Design Stress-Test Domain)
* **Description:** Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
* **Workflows:** Sequential questioning, codebase exploration for facts, recommendation per question.
* **Primary Artifacts:** Shared understanding, resolved decision branches.

### 5. `skill-manager` (Skill Creation Domain)
* **Description:** Generates spec-compliant AgentSkills.io skill packages. Use when you need to create a new skill or update an existing skill structure.
* **Engagement Modes:**
    * **`mode: create`** $
ightarrow$ *Injects: Skill Architect* (Focus: Scaffolding, directory structure, component generation)
    * **`mode: review`** $
ightarrow$ *Injects: Skill Auditor* (Focus: Compliance, structure, information density)
    * **`mode: deploy`** $
ightarrow$ *Injects: Deployment Operator* (Focus: Synchronization to target directory)
* **Primary Artifacts:** Skill packages, updated skill structures.
