---
name: synthesize
description: Enriches raw analysis by extracting meaning, forming hypotheses, and distilling patterns into actionable insights.
metadata:
  category: enrich
  capabilities:
    - hypothesis_formation
    - insight_distillation
---

# synthesize

Goal: Enrich analysis output with extracted meaning, formed hypotheses, and distilled actionable insights.
Non-Goals: Gathering new data, producing implementation plans, or making final decisions.
Use-When: You need to distill patterns and contradictions into actionable insights and testable hypotheses.

## 0. Prerequisites
- Analysis from `analyze` skill (patterns, contradictions, gaps)

## 1. Inputs
- Analysis output from prompt (patterns, contradictions, gaps with confidence scores)
- Domain context (optional: additional background to inform synthesis)

## 2. Processes
1. Parse analysis to identify the strongest patterns and most critical contradictions
2. Synthesize patterns into coherent themes or narratives
3. Form hypotheses that explain contradictions or fill gaps
4. Prioritize hypotheses by confidence, impact, and actionability
5. Flag where more data is needed to validate or refute hypotheses

## 3. Outputs
- Structured synthesis in the prompt (themes, hypotheses, priorities, data gaps)
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `ideate` — generate solutions informed by synthesized hypotheses
- `define` — frame problem statement from synthesized insights
- `collect` — gather more data to validate key hypotheses

## 5. Examples

### Example 1: Hypothesis formation

**Prompt:** Synthesize the zero-trust architecture analysis.

**Outcome:** Prompt output with 3 themes (e.g., "identity is the new perimeter"), 5 hypotheses (e.g., "microsegmentation reduces breach impact by 60%+"), and 2 data gaps flagged.

### Example 2: Insight distillation

**Prompt:** Distill the competitive analysis into actionable hypotheses.

**Outcome:** Prompt output with key themes, hypotheses about market positioning, and recommendations for further research.
