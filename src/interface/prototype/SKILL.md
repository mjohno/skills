---
name: prototype
description: Use when output or map skills need the prototype artifact contract for cheap mock-ups or validation methods.
metadata:
  category: interface
---

# prototype

Goal: Define prototype artifact contracts for cheap validation methods: what to mock, what template to use, how to check quality, and what evidence matters.
Non-Goals: Building the prototype, running validation sessions, producing production implementation, or polishing final deliverables.
Use-When: Another skill needs the `prototype` interface contract before outlining, drafting, modifying, reviewing, or orchestrating a validation artifact.

## 0. Prerequisites
- Idea, solution concept, requirement, risk, or assumption to validate
- Target audience, environment, system boundary, or decision to inform when available

## 1. Inputs
- Concept summary and riskiest assumption
- Prototype type or uncertainty to test
- Constraints such as time, fidelity, tools, audience, data, and safety limits
- Optional success criteria, failure criteria, and follow-up decision

## 2. Processes
1. Identify the decision the prototype must inform and the assumption being tested.
2. Select the cheapest adequate profile from this table.

| Profile | Use When | Template | Quality Checklist |
|---------|----------|----------|-------------------|
| `tabletop-roleplay` | Validate human coordination, service interactions, incident response, support flows, policy, or operational readiness. | `assets/tabletop_roleplay_template.md` | `references/tabletop_roleplay_quality_checklist.md` |
| `ui-mockup` | Validate UI comprehension, task flow, information architecture, visual hierarchy, or interaction expectations. | `assets/ui_mockup_template.html` | `references/ui_mockup_quality_checklist.md` |
| `process-scenario` | Validate process logic, handoffs, states, run-through scenarios, system boundaries, or operational sequence. | `assets/process_scenario_template.md` | `references/process_scenario_quality_checklist.md` |
| `api-contract-stub` | Validate integration shape, request/response semantics, error behavior, auth expectations, or consumer/provider alignment. | `assets/api_contract_stub_template.yaml` | `references/api_contract_stub_quality_checklist.md` |
| `data-layout-structure` | Validate data shape, fields, relationships, constraints, examples, imports/exports, or downstream usability. | `assets/data_layout_structure_template.md` | `references/data_layout_structure_quality_checklist.md` |

3. Provide the selected template and quality checklist to the consuming skill.
4. Provide the validation framing to include in the artifact: decision, assumption, audience/context, scope, omitted work, validation signals, failure signals, and next decision.
5. Keep fidelity intentionally low.

## 3. Outputs
- Selected profile
- Template path
- Quality checklist path
- Validation framing for the prototype artifact

## 4. Next Steps
- `output/outline` — create the prototype skeleton from the selected template.
- `output/draft` — fill the selected template with first-pass content.
- `output/modify` — revise an existing prototype while preserving the selected quality checklist.
- `transform/review` — check the prototype before spending validation effort.

## 5. Examples

### Example 1: Tabletop/roleplay
**Prompt:** Define a prototype for validating whether support can handle account recovery escalations.
**Outcome:** Selects `tabletop-roleplay`, points to the Markdown template and checklist, and frames scenario roles, prompts, validation signals, and failure signals.

### Example 2: API contract stub
**Prompt:** Shape a prototype for validating whether partner systems can integrate with our invite API.
**Outcome:** Selects `api-contract-stub`, points to the YAML template and checklist, and frames endpoint semantics, sample payloads, error cases, and next integration decision.
