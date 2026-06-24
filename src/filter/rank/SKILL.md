---
name: rank
description: Ranks a collection of items based on user-defined scoring criteria, producing an ordered list of candidates.
metadata:
  type: skill
  category: filter
  capabilities:
    - ranking
    - scoring
    - selection
---
# rank

## Overview
`rank` is a filter skill that accepts a list of candidate items (e.g., solution concepts, documents, knowledge entries) and returns the same list sorted according to one or more user‑defined criteria. The skill is intentionally lightweight: it does not modify content beyond ordering, and it does not persist the result.

## Inputs
- `items`: an array of objects, each containing at least an `id` and `content` field.
- `criteria`: an array of ranking rules. Each rule is an object with:
  - `field`: the property to evaluate.
  - `order`: `asc` or `desc`.
  - `weight`: optional numeric weight.
  - `selector`: optional function or static value used for scoring.

## Processes
1. Parse the `criteria` list and build a composite scoring function.
2. For each `item`, compute a score by applying the criteria in order, respecting weights.
3. Sort the items by their composite score (higher is better for `desc` rules).
4. Return the sorted array.

## Outputs
- `ranked`: array of items sorted by the ranking.

## Next Steps
- `plan` — create a plan to act on top‑ranked items.
- `prototype` — iterate prototypes for high‑rank candidates.

## Example
```text
Input:
items: [
  {id: 1, cost: 100, impact: 8},
  {id: 2, cost: 80, impact: 9},
  {id: 3, cost: 120, impact: 7},
]
criteria: [
  {field: "cost", order: "asc", weight: 0.4},
  {field: "impact", order: "desc", weight: 0.6},
]
Output:
ranked: [2, 1, 3]
```
```
