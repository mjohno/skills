---
name: prototype
description: Produces concrete proof-of-concept, mockup, or working-example artifacts to evaluate a solution concept.
metadata:
  category: output
  capabilities:
    - proof_of_concept
    - mockup_generation
---

# prototype

Goal: Make solution concepts tangible through proof-of-concepts, mockups, or working examples.
Non-Goals: Production implementation, final deployment, or comprehensive testing.
Use-When: You need to create a proof-of-concept, mockup, or working example to evaluate a solution.

## 0. Prerequisites
- Top solution concepts from `ideate` skill

## 1. Inputs
- Selected solution concept(s) from prompt
- Target platform or technology context (optional)

## 2. Processes
1. Parse solution concept to understand the core approach and scope
2. Determine the appropriate prototype fidelity (wireframe, mockup, code PoC, architecture diagram)
3. Build the prototype:
   - For code solutions: create minimal working implementation
   - For design solutions: create wireframes or mockups
   - For architecture solutions: create diagrams and data flow models
4. Document what the prototype demonstrates and what it deliberately omits
5. Identify risks and assumptions exposed by the prototype

## 3. Outputs
- Prototype description and key artifacts in the prompt
- Prototype files written if user specifies output paths
- Documented risks and assumptions

## 4. Next Steps
- `test` — evaluate prototype against requirements
- `define` — revisit requirements if prototype reveals gaps
- `ideate` — explore alternative approaches if prototype fails

## 5. Examples

### Example 1: Code PoC

**Prompt:** Build a PoC for the identity-first microsegmentation solution.

**Outcome:** Prompt output describing the PoC architecture plus `poC/` directory with minimal implementation code demonstrating core functionality.

### Example 2: Architecture mockup

**Prompt:** Create an architecture mockup for the zero-trust network design.

**Outcome:** Prompt output with architecture diagram description and `architecture.md` with data flow, component interactions, and security boundaries.
