---
name: rank
description: Use when a collection of information requires ranking and prioritization based upon user-defined scoring criteria.
metadata:
  category: filter
---
# rank

<!-- TODO(compliance): Change this description to use Goals, Non-Goals and Use-When sections. -->

## Pre-requisites
- Information exists which is rank-able.
- Clear criteria for ranking which may be qualitative or quantitative.

## Inputs
- A collection of semi-structured information.
- Queries or methods for selecting the information for ranking.
- Criteria for ranking which may be qualitative or quantitative, and may include weights to indicate importance.

## Processes
1. Gather the data which needs to be ranked.
2. Clean the information which is not relevant for ranking.
3. Ask the user for more information when information is missing or the criteria is not able to be ranked.
4. Apply the user‑defined criteria to each item, respecting the prioritization of the criteria.
   - When multiple criteria exist, aggregate the scores by prioritizing the criteria in order of listed importance.
   - When a single criterion is used, apply it directly to each item to determine its score.
5. Sort the items based upon their scores according to the criteria, with the most important items first.
6. Capture decisions used for ranking to provide transparency and justification for trade-offs.

## Rules
- It is OK to be fuzzy if the criteria is qualitative. Be as accrurate as possible.
- A justification is mandatory when criteria is qualitative or when there are conflicts or trade-offs made.
- Assume the first listed criteria is more important than the second, and so on, unless the user specifies otherwise.

## Outputs
- A clean and ordered list of items ranked according to the user‑defined criteria, with the most important items first.
- A justification for the ranking decisions, including any trade-offs made when criteria conflict.

## Next Steps
- Suggest other ranking criteria which may achieve the user's goals.
- Offer to move forward with the top ranked items.

## Example

### Example 1: Ranking Solution Concepts

**Prompt**: "I have a list of solution concepts for a problem. I want to rank them based on their feasibility, cost, and potential impact. Can you help me with that?"
**Outcome**:
- Asked the user for the list of solutions as it was not in the context.
- For each, determined feasibility, cost and impact.
- Applied an aggregate score weighting feasibility > cost > impact.
- Presented the ranked list of solutions with a justification for ranking decisions.
