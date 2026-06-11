---
name: rfc
description: Capability to design technical solutions and ensure architectural alignment. Use when you need to write an RFC from a PRD, review an RFC from a domain-specific lens, validate RFC vs PRD compliance, or manage the RFC lifecycle.
---

# rfc

## Goal
Capability to design technical solutions and ensure architectural alignment.

Non-Goals: Do not manage product requirements, execute implementation tasks, or handle deployment operations.

## Use When
- You need to write or update an RFC (see [Write Mode](references/mode_write.md)).
- You need to review an RFC from a specific lens (see [Review Mode](references/mode_review.md)).
- You need to validate RFC vs PRD compliance (see [Validate Mode](references/mode_validate.md)).
- You need to manage the RFC index and lifecycle (see [Manager Mode](references/mode_manager.md)).

## Workflows

### [Write Mode](references/mode_write.md)
For scaffolding and updating RFCs from a PRD or technical goal.

### [Review Mode](references/mode_review.md)
For focused reviews from domain-specific personas (architecture, security, scalability, etc.).

### [Validate Mode](references/mode_validate.md)
For verifying RFC vs PRD compliance and structural integrity.

### [Manager Mode](references/mode_manager.md)
For maintaining the RFC index and tracking lifecycle status.

## Examples

### Example 1: Writing an RFC from a PRD
**Prompt**: "Write an RFC for the PRD in `PRD-001-user-auth.md`. This is a general technical RFC."

**Decisions**:
- No persona specified → defaults to `persona_write_system_architect.md`
- Ingests `PRD-001-user-auth.md`, extracts 3 User Stories and 7 Acceptance Criteria
- Anchors Context to the technical problem: implementing OAuth2 flow, not restating user stories
- Produces `RFC-001-user-auth.md` with 4 design decisions, API specs, and feasibility assessment
- Output recommends: review:security, review:alignment

**Outcome**:
```
RFC-001-user-auth.md
├── Context (references PRD-001)
├── Proposed Solution
├── Design Decisions (4 entries)
├── Architecture & Data Models
├── Feasibility Assessment
├── Alignment with PRD (7 AC mappings)
├── Open Questions (2 items)
└── Decision Log (summary table + detail entries)
```

### Example 2: Running a Security Review
**Prompt**: "Review RFC-001-user-auth.md from a security perspective."

**Decisions**:
- Loads `persona_review_security.md`
- Evaluates authN/Z design, token handling, and data protection
- Identifies 2 High-severity and 1 Medium-severity findings

**Outcome**:
```
RFC-001-user-auth.md (updated)
└── Review Comments
    └── Review Round 1: Security Review
        ├── Risk Level: High
        ├── Findings: 3 items (2 High, 1 Medium) with [ ] checkboxes
        └── Overall Assessment: 2-3 sentence summary
```
