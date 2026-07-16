---
name: outline
description: Use when you need to produce structure, skeletons, headings, file layouts, interfaces, or other low-detail artifact outlines before drafting.
metadata:
  category: output
  capabilities:
    - outlining
    - structure_generation
---

# outline

Goal: Produce a useful structure for a target artifact without filling in final content.
Non-Goals: Drafting complete content, polishing language, implementing code, or persisting durable records.
Use-When: You need an outline, skeleton, scaffold, section plan, file layout, API/interface sketch, test matrix, or other structure-first artifact.

## 0. Prerequisites
- A target artifact noun from the prompt or an interface skill, such as spec, script, rfc, plan, task, test, prose, code, or prototype
- Source material, goal, audience, constraints, or acceptance criteria when available

## 1. Inputs
- Raw request, notes, interface-shaped artifact, or existing content
- Target artifact type and desired fidelity
- Optional conventions, templates, examples, or file paths

## 2. Processes
1. Identify the artifact noun and the purpose the structure must serve.
2. Select or infer the appropriate canonical shape; use interface skills when a known noun needs stricter form.
3. Create the smallest structure that makes the next drafting step clear.
4. Mark unknowns, decisions, placeholders, and optional sections explicitly.
5. Avoid filling sections beyond brief intent notes unless the user asks for more detail.

## 3. Outputs
- An outline, skeleton, scaffold, section map, file layout, or interface sketch
- If user specifies an output file, write the outline to that path instead

## 4. Next Steps
- `draft` — fill the outline with first-pass content
- `modify` — adjust the outline before drafting
- `review` — check the structure against requirements or a persona lens

## 5. Examples

### Example 1: Script outline
**Prompt:** Outline a script that organizes files by extension.
**Outcome:** Produces a script skeleton with purpose, CLI arguments, main functions, error cases, dry-run behavior, and test placeholders.

### Example 2: Spec outline
**Prompt:** Outline a spec for team workspace permissions.
**Outcome:** Produces spec headings, traceable ID placeholders, future-state targets, scope boundaries, requirements, acceptance criteria, quality priorities, uncertainties, and decisions without drafting full prose.
