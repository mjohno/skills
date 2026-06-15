---
name: review
description: Compare an output or result against a spec or goal to find gaps. Use when you need to review anything against anything.
---

# Review

## Capability
Compare any output against any spec to find gaps and report findings.

## Use When
- "Review the PRD" → compare against design skill's workflow
- "Review the code" → compare against implement skill's workflow
- "Review this code against this PRD" → compare code against PRD artifact
- "Review anything against anything" → compare output against any spec

## Routing
When asked to review X against Y:
1. X = the output to review
2. Y = the spec to compare against
3. If Y is a skill → load that skill's workflow as the spec
4. If Y is an artifact → use that artifact as the spec
5. Load `references/workflow_default.md` and execute the review
