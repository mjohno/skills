---
name: vocab
description: Use when terms like study, simplify, lean, propose need definition.
disable_model_invocations: true
metadata:
  type: vocabulary
  category: interface
---

# vocab

Goal: Define compact project vocabulary for human-loaded context before prompting.
Non-Goals: Do not define skill-owned verbs, domain glossary terms, inputs, outputs, procedures, routing, or verification.

## Terms

- `study`: Read content to gather context. Do not modify files or execute files. Acknowledge completion of study with a minimal response. Do not summarize.
- `simplify`: Reduce complexity while preserving required meaning, behavior, and useful structure.
- `lean`: Reduce overhead, waste, duplication, ceremony, or maintenance burden.
- `propose`: Write a response back to the user via chat only. Do not execute or change anything.
