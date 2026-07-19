---
name: prototype
description: Use when output or map skills need the prototype artifact contract for cheap mock-ups or validation methods.
metadata:
  type: interface
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

## 2. Process
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
- Minimal default output: selected prototype profile, assumptions, selected package-local paths, and loaded selected contents only.
- Always return selected file paths followed by loaded contents in fenced code blocks.
- Selected profile returns its matching template path and quality checklist path from the table above.

## 4. Next Steps
- `output/outline` — create the prototype skeleton from the selected template.
- `output/draft` — fill the selected template with first-pass content.
- `output/modify` — revise an existing prototype while preserving the selected quality checklist.
- `transform/review` — check the prototype before spending validation effort.

## 5. Examples

### Example 1: Tabletop/roleplay
**Prompt:** "Use the prototype interface to validate account recovery escalation support."
**Decision:** Select `tabletop-roleplay`.
**Outcome:** Return selected paths and loaded contents:

file_path: src/interface/prototype/assets/tabletop_roleplay_template.md
```markdown
# Tabletop Roleplay Prototype
[loaded tabletop template]
```

file_path: src/interface/prototype/references/tabletop_roleplay_quality_checklist.md
```markdown
# Tabletop Roleplay Quality Checklist
[loaded tabletop quality checklist]
```

### Example 2: API contract stub
**Prompt:** "Use the prototype interface to validate partner invite API integration."
**Decision:** Select `api-contract-stub`.
**Outcome:** Return selected paths and loaded contents:

file_path: src/interface/prototype/assets/api_contract_stub_template.yaml
```yaml
# API Contract Stub
[loaded API contract stub template]
```

file_path: src/interface/prototype/references/api_contract_stub_quality_checklist.md
```markdown
# API Contract Stub Quality Checklist
[loaded API quality checklist]
```
