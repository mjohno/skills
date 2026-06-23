---
name: memory-entry
description: Use when raw memory needs canonical log-entry structure.
metadata:
  type: skill
  category: normalize
  capabilities:
    - memory
---
# memory-entry

Goal: Canonicalize memory so it can be rendered as clear bullets in the memory log.
Non-Goals: Writing memory files or rewriting the summary directly.
Use-When: Raw memory needs a consistent shape before memorization or dreaming.

## 0. Prerequisites
- Raw memory notes or existing memory bullets
- The `memory-interface` contract when file behavior matters

## 1. Inputs
- Content to retain in memory
- Optional actor/source, kind, tags, date, confidence, expiry, and provenance hints

## 2. Processes
1. Preserve or infer the required field `content`.
2. Use optional fields when available: `id`, `date`, `kind`, `source`, `confidence`, `expires`, `tags`, `promote_to_kb`.
3. Render the entry for later storage as bullet content under a timestamp heading.
4. Keep the normalized result lightweight and clear rather than transcript-like.
5. Preserve actor/source labels when known.

## 3. Outputs
- Canonical memory-entry payload

## 4. Canonical Shape
```yaml
content:
id:
date:
kind: preference | fact | decision | reminder | thread | temporary | project-context
source:
confidence:
expires:
tags:
promote_to_kb:
```

## 4. Next Steps
- `output/memorize` — append the normalized entry to the memory log
- `map/dream` — compress and summarize memory later

## 5. Examples

### Example 1

**Prompt:** Shape this memory note before memorize.
**Outcome:** Produces a lightweight content-focused memory payload.
