---
name: analyze
description: Finds patterns, contradictions, and gaps in collected resources. Use when you need to identify insights and deficiencies in a resource inventory or research data.
metadata:
  category: filter
  capabilities:
    - pattern_detection
    - contradiction_identification
    - gap_analysis
    - confidence_scoring
---

# analyze

Goal: Find patterns, contradictions, and gaps in collected resources to produce actionable insights.
Non-Goals: Gathering new data, writing final reports, or making implementation decisions.
Use-When: You need to identify insights and deficiencies in a resource inventory or research data.

## 0. Prerequisites
- `resources.md` from `collect` skill (or equivalent resource inventory)

## 1. Inputs
- Resource inventory (`resources.md` or inline data)
- Analysis focus (optional: specific domain, theme, or question)

## 2. Processes
1. Parse resource inventory and categorize entries by type, source, and topic
2. Identify recurring patterns, themes, and consensus points
3. Detect contradictions, conflicts, or inconsistencies across sources
4. Flag gaps: missing perspectives, under-researched areas, data holes
5. Score each pattern/gap by confidence and relevance

## 3. Outputs
- Structured analysis in the prompt (patterns, contradictions, gaps with confidence scores)
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `synthesize` — extract meaning and form hypotheses from analysis
- `ideate` — generate solutions informed by identified gaps
- `define` — frame problem statement from analysis findings

## 5. Examples

### Example 1: Pattern analysis

**Prompt:** Analyze the resources collected about zero-trust architecture.

**Outcome:** Prompt output with 5 patterns (e.g., "microsegmentation is consistently recommended"), 3 contradictions, and 2 gaps.

### Example 2: Gap detection

**Prompt:** Find contradictions in the competitive intelligence data and save to `analysis.md`.

**Outcome:** `analysis.md` highlighting conflicting claims across competitors and missing data on pricing transparency.
