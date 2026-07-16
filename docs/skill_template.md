---
name: [skill-name]
description: [concise overview with "Use when..." triggers]
disable-model-invocation: [true for interface contract skills — omit otherwise]
metadata:
  category: [interface|input|transform|output|map]
---

# [Skill Name]

Goal: [one clear outcome the skill achieves, or contract it defines for interface skills]
Non-Goals: [what this skill does NOT do — at least one]
Use-When: [triggers for invoking this skill, or for referencing this interface]

## 0. Prerequisites
- [upstream skills, actions, or context expected]

## 1. Inputs
- [information this skill reads or receives; reference input_*.md or keep inline]

## 2. Processes / Contract Rules
- [for invocable skills: transformations or steps this skill performs]
- [for interface skills: profile selection rules, desired-state rules, invariants, valid structure, or protocol rules]

## 3. Outputs / Exposed Contract
- [for invocable skills: information this skill creates/writes]
- [for interface skills: contract data exposed to consuming skills, such as conventions, checks, templates, schemas, or protocol rules]

## 4. Next Steps
- [suggested follow-on actions or skills]

## 5. Examples

### Example 1

**Prompt:** [prompt used to invoke the skill or reference the interface]
**Outcome:** [result of executing the skill or applying the contract]
