# Generic Spec Checklist

## Spec-Level CRITICAL

- [ ] **CRITICAL** Spec has a title and stable `SPEC-<slug>` ID.
- [ ] **CRITICAL** Spec includes all required sections: Purpose, Current State Summary, Future State, Scope, Requirements, Acceptance, Quality, Expectations, Uncertainties, Decisions.
- [ ] **CRITICAL** Referenceable claims use stable IDs.
- [ ] **CRITICAL** Scope includes both `In Scope` and `Out of Scope`.
- [ ] **CRITICAL** Quality includes both `Constraints / Non-Negotiables` and `Priorities`.
- [ ] **CRITICAL** Uncertainties includes `Risks`, `Questions`, `Assumptions`, and `Pre-Work Needed`.

## Spec-Level QUALITY

- [ ] **QUALITY** The spec defines a future state, not an implementation plan.
- [ ] **QUALITY** The spec is generic-domain unless an explicit profile is selected.
- [ ] **QUALITY** IDs are used for referenceable claims, not every sentence.
- [ ] **QUALITY** Plan items can trace to relevant spec IDs without copying full spec text.
- [ ] **QUALITY** Open uncertainty is visible rather than hidden in requirements.

## Section-Specific QUALITY

### Purpose

- [ ] **QUALITY** Explains why the spec exists.
- [ ] **QUALITY** Identifies the motivating problem, objective, opportunity, or threat.
- [ ] **QUALITY** Avoids solution details unless they are already settled constraints or decisions.

### Current State Summary

- [ ] **QUALITY** Captures relevant current facts needed to understand the gap.
- [ ] **QUALITY** Distinguishes observed facts from assumptions.
- [ ] **QUALITY** Avoids premature remediation.

### Future State

- [ ] **QUALITY** Describes the desired end condition, not just activity.
- [ ] **QUALITY** Includes diagrams, mockups, examples, or interaction descriptions where they reduce ambiguity.
- [ ] **QUALITY** Is concrete enough for a plan to target.

### Scope

- [ ] **QUALITY** In-scope items define included work, behavior, artifacts, or responsibilities.
- [ ] **QUALITY** Out-of-scope items capture non-goals and rejected boundaries.
- [ ] **QUALITY** Boundaries are clear enough to reject unrelated work.

### Requirements

- [ ] **QUALITY** Requirements use the form most natural for the domain: user stories, key tasks, required behaviors, or required properties.
- [ ] **QUALITY** Requirements are testable, reviewable, or otherwise judgeable.
- [ ] **QUALITY** Requirements avoid duplicating scope, acceptance, or plan items.

### Acceptance

- [ ] **QUALITY** Acceptance criteria define observable, reviewable, or measurable signals.
- [ ] **QUALITY** Gherkin, KPIs, heuristics, or another explicit acceptance format is used where helpful.
- [ ] **QUALITY** Acceptance avoids prematurely mandating implementation artifacts as proof.

### Quality

- [ ] **QUALITY** Constraints are separated from priorities.
- [ ] **QUALITY** Non-negotiables are stated as hard limits.
- [ ] **QUALITY** Priorities are ordered so downstream decisions can follow them.
- [ ] **QUALITY** Vague quality claims are paired with concrete implications.

### Expectations

- [ ] **QUALITY** Expectations focus on metadata of evidence and actions.
- [ ] **QUALITY** Expected review, validation, reporting, or handoff behavior is clear.
- [ ] **QUALITY** Expectations do not duplicate acceptance criteria.

### Uncertainties

- [ ] **QUALITY** Risks, questions, assumptions, and pre-work are separated.
- [ ] **QUALITY** Each uncertainty explains why it matters when not obvious.
- [ ] **QUALITY** Pre-work identifies investigation, prototype, decision, or validation needs.

### Decisions

- [ ] **QUALITY** Settled choices are recorded with IDs.
- [ ] **QUALITY** Decision status is included where useful.
- [ ] **QUALITY** Rationale or source is included where it prevents repeated debate.
- [ ] **QUALITY** Decisions are distinct from assumptions and open questions.

## Definition of Done

A generic spec passes if all CRITICAL items pass. A high-quality spec also passes the QUALITY items relevant to its domain and maturity.
