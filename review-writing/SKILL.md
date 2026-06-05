---
name: review-writing
description: A unified skill for reviewing and improving English language prose. Use when you need to enhance the readability, conciseness, or information density of technical writing.
---

# Review Writing Skill

Goal: Improve the quality of English prose by optimizing for readability, conciseness, and information density.

Use When:
- You are tasked with reviewing, editing, or improving English prose, documentation, or technical writing.
- You need to ensure optimal sentence length distribution for clarity and rhythm.
- You need to maximize lexical economy and eliminate "fluff" from text.

## Workflows

### Workflow 1: Improve Readability & Conciseness
**Goal**: Ensure optimal sentence length distribution for clarity and rhythm.

1. **Analyze the Text**:
   Run the readability analysis script on the target text file:
   ```bash
   python review-writing/scripts/analyze_readability.py <path_to_text_file>
   ```

2. **Parse the JSON Report**:
   Carefully examine the output. Pay specific attention to:
   - `summary`: Check if `mean_length` is close to the target of 15.
   - `outliers.too_short`: Sentences that may be too abrupt or lack necessary context.
   - `outliers.too_long`: Sentences that exceed the 30-word threshold and likely need splitting.
   - `high_density_clusters`: Areas where several sentences in a row are longer than average.

3. **Provide Feedback**:
   Consult [READABILITY_GUIDELINES.md](references/READABILITY_GUIDELINES.md) to provide actionable suggestions for improvement.

---

### Workflow 2: Increase Information Density & Impact
**Goal**: Maximize lexical economy and eliminate "fluff" to ensure every word adds value.

1. **Analyze the Text**:
   Run the density analysis script on the target text file:
   ```bash
   python review-writing/scripts/analyze_density.py <path_to_text_file>
   ```

2. **Parse the JSON Report**:
   Carefully examine the output. Pay specific attention to:
   - `summary.density_score`: A low score indicates heavy reliance on function words.
   - `summary.wordiness_score`: A high score suggests the text is filled with non-essential phrases.
   - `details.wordy_phrases`: Specific multi-word phrases that can be replaced by single words.
   - `details.passive_indices`: Instances of passive voice that could be converted to active voice.
   - `details.redundant_phrases`: Tautologies or redundant word pairings.

3. **Provide Feedback**:
   Consult [DENSITY_GUIDELINES.md](references/DENSITY_GUIDELINES.md) to provide actionable suggestions for improvement.

## Examples

### Example 1

**Prompt**: "Review the following technical documentation for readability and conciseness: [text]"

**Decisions**:
- Identified that the goal is to improve readability and rhythm.
- Selected Workflow 1: Improve Readability & Conciseness.
- Executed `analyze_readability.py` and identified several sentences exceeding the 30-word threshold.
- Consulted `READABILITY_GUIDELINES.md` to formulate splitting suggestions.

**Outcome**:
Provided a revised version of the text with improved sentence length distribution and specific notes on why certain sentences were split.
