# Engineering Workflow: The Convergent Feedback Network

This document outlines a non-linear, loop-based engineering workflow. Rather than a "Waterfall" sequence, this system functions as a **Convergent Feedback Network** where information flows between different levels of abstraction to reduce uncertainty and ensure alignment between business goals and technical execution.

---

## I. The Triple-Loop Architecture

The workflow is composed of three concentric, interacting feedback loops operating at different scales and cadences.

### 1. The Strategic Loop (Outer)
* **Focus:** Business Value & User Need.
* **Nodes:** `PRD` $\leftrightarrow$ `Observability`.
* **Cadence:** Monthly / Quarterly.
* **Goal:** Ensures we are solving the right problems for the right people.

### 2. The Tactical Loop (Middle)
* **Focus:** Technical Feasibility & Design.
* **Nodes:** `RFC` $\leftrightarrow$ `Plan` $\leftrightarrow$ `Task Packets` $\leftrightarrow$ `Implementation`.
* **Cadence:** Weekly / Bi-weekly.
* **Goal:** Ensures the technical approach is robust and documented.

### 3. The Operational Loop (Inner)
* **Focus:** Execution & Quality.
* **Nodes:** `Implementation` $\leftrightarrow$ `Verification` $\leftrightarrow$ `Release`.
* **Cadence:** Daily / Hourly.
* **Goal:** Ensures the code is high-quality and meets the defined requirements.

---

## II. Mode vs. Workflow Convention

Skills in this system use one of two interaction patterns. The pattern chosen reflects how the skill's capability is structured.

### Modes (`mode: <name>`)
* **Use when:** The skill has an injectable persona that changes the *style*, *focus*, or *cognitive bias* of execution while the domain stays the same.
* **Pattern:** `mode: <name>` $
ightarrow$ *Injects: Persona* (Focus: ...
* **Example:** `prd` skill with `mode: write` (Product Strategist) vs `mode: review` (Critical Analyst).
* **Reference:** See [workflow_skills.md](workflow_skills.md) §II for the full mode registry.

### Workflows
* **Use when:** The skill has fixed operational procedures — distinct steps that don't change based on persona, but rather on the *task* being performed.
* **Pattern:** `### <Workflow Name>` with numbered steps.
* **Example:** `plan` skill with Create Plan, Update Plan, Check Plan Shape.
* **Reference:** See [workflow_skills.md](workflow_skills.md) for which skills use workflows.

### Guideline
* **Capability-first, persona-driven** $
ightarrow$ use modes.
* **Capability-first, procedure-driven** $
ightarrow$ use workflows.

---

## III. Node-by-Node Deep Dive

### 1. PRD (Product Requirements Document) — *The Strategic Compass*
* **Purpose:** To define the "Problem Space" and the "Value Proposition."
* **Inputs:** Market research, user pain points, business goals, resource constraints.
* **Process:** Problem identification, user persona definition, feature scoping, success metric setting.
* **Outputs:** **PRD Document** (containing User Stories and Acceptance Criteria).
* **Verification Gates:**
    * **S.M.A.R.T. Check:** Are success metrics Specific, Measurable, Achievable, Relevant, and Time-bound?
    * **Stakeholder Alignment:** Do Product, Design, and Engineering agree on the "What"?

### 2. RFC (Request for Comments) — *The Technical Blueprint*
* **Purpose:** To define the "Solution Space" and ensure technical feasibility.
* **Inputs:** The `PRD`, existing architecture, security standards, and technical constraints.
* **Process:** Architectural design, prototyping, edge-case analysis, and peer review.
* **Outputs:** **RFC Document** (API specs, data models, system diagrams).
* **Verification Gates:**
    * **Feasibility Check:** Can this be built within current technical/time constraints?
    * **Alignment Check:** Does the design satisfy all `PRD` Acceptance Criteria?
    * **Consensus Check:** Has the engineering community identified/resolved breaking flaws?

### 3. Task Packets — *The Work Capsules*
* **Purpose:** To decompose approved design into portable, actionable units of work.
* **Inputs:** The `RFC` and plan items.
* **Process:** Breaking scope into stable task IDs, goals, targets, constraints, and verification hints.
* **Outputs:** **Task Packets** for implementation and review.
* **Verification Gates:**
    * **I.N.V.E.S.T. Check:** Are tasks Independent, Negotiable, Valuable, Estimable, Small, and Testable?
    * **Traceability Check:** Does each packet link back to source context?

### 4. Implementation — *The Engine*
* **Purpose:** To translate design into functional reality.
* **Inputs:** The `RFC` and `Task Packets` (decomposed from plan items and User Stories).
* **Process:** Coding, unit testing, and refactoring.
* **Outputs:** **Pull Requests (PRs)** and updated documentation.
* **Verification Gates:**
    * **Code Review:** Does implementation follow patterns in the `RFC`?
    * **CI/CD Check:** Do all automated tests and linters pass?

### 6. Verification — *The Quality Gate*
* **Purpose:** To ensure the "Implementation" meets the "Intent" and to close the loop on requirements.
* **Inputs:** The `Implemented Code`, the `PRD` (for AC), and the `RFC` (for Specs).
* **Process:** Integration testing, manual QA, and User Acceptance Testing (UAT).
* **Outputs:** **Validated Build** (on success) OR **Revision Requests** (on failure). Results are used to formally close requirements in the `PRD` or trigger revisions in the `RFC`/`PRD`.
* **Verification Gates:**
    * **Functional Check:** Does the feature satisfy all `PRD` Acceptance Criteria?
    * **Technical Check:** Does the system meet `RFC` performance/latency requirements?

### 7. Release — *The Delivery*
* **Purpose:** To transition the feature from "Development" to "Production" safely.
* **Inputs:** The `Verified Build` and a Deployment/Rollback Plan.
* **Process:** Deployment via Feature Flags, Canary releases, or Blue-Green deployments.
* **Outputs:** **Live Production Feature.**
* **Verification Gates:**
    * **Smoke Test:** Does the feature work in the production environment?
    * **Health Check:** Are there immediate spikes in errors or latency?

### 8. Observability — *The Radar*
* **Purpose:** To provide the feedback that drives the next loop.
* **Inputs:** Live production telemetry (logs, metrics, user interaction data).
* **Process:** Monitoring, dashboarding, and data analysis.
* **Outputs:** **Performance Data** and **User Behavior Insights.**
* **Verification Gates:**
    * **KPI Match:** Did we achieve the success metrics defined in the `PRD`?
    * **Stability Match:** Is the system performing within `RFC` technical bounds?

---

## IV. The Meta-Review Layer (Retrospectives)

Retrospectives are the highest level of feedback in the network. They do not verify the *product*; they verify the *process* and the *assumptions* that drove the product.

### 1. Business Retrospective (Strategic Review)
* **Scope:** The alignment between the **PRD** and the **Market/User**.
* **Trigger:** Completion of a product cycle or a significant shift in business KPIs.
* **Input:** `Observability` data vs. `PRD` success metrics.
* **Question:** *"Did we actually solve the problem we set out to solve, and was it worth the investment?"*
* **Output:** Updates to the Product Roadmap or revisions to the PRD framework.

### 2. Technical Retrospective (Tactical Review)
* **Scope:** The alignment between the **RFC** and the **System Reality**.
* **Trigger:** Major architectural shifts, significant production incidents, or end of a technical milestone.
* **Input:** `Observability` (performance/stability) vs. `RFC` design goals.
* **Question:** *"Did our architectural decisions hold up under load, and did our design patterns serve us well?"*
* **Output:** Revisions to the `RFC` technical templates.

### 3. Procedural Retrospective (Operational Review)
* **Scope:** The efficiency and health of the **Workflow** itself.
* **Trigger:** End of a sprint, a project completion, or a "process friction" event.
* **Input:** Team feedback on the friction/utility of the `PRD` $\rightarrow$ `RFC` $\rightarrow$ `Task Packets` flow.
* **Question:** *"Did our documentation and decision-making process accelerate delivery or create unnecessary overhead?"*
* **Output:** Refinements to the `workflow.md` and the team's operating model.

---

## V. Summary Mapping: Information Flow

| If you want to know... | Look at this Node... | By checking this... |
| :--- | :--- | :--- |
| **"Why are we doing this?"** | **PRD** | User Stories & Business Goals |
| **"How will it work?"** | **RFC** | Architecture & API Specs |

| **"What needs to be done?"** | **Task Packets** | Goals, Targets & Constraints |
| **"Is the code correct?"** | **Implementation** | Code Review & Unit Tests |
| **"Does it meet requirements?"** | **Verification** | Acceptance Criteria (AC) |
| **"Did it actually work?"** | **Observability** | Business KPIs & System Metrics |

---

## VI. The Golden Rule of Documentation
**Information must be promoted when it becomes a rule.**
If a discussion in a **Task**, **Plan**, or **Pull Request** results in a permanent change to the system's architecture or design principles, it **must** be updated in the **RFC**. Work breakdown and sequencing that do not change architecture should stay in **Plans** or **Task Packets**. Failure to do so leads to "Knowledge Drift," where the documentation no longer reflects the reality of the system.
