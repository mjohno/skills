---
name: editor
description: Analyzes and optimizes technical writing for conciseness and information density by detecting wordiness, passive voice, and low lexical density.
---

# Editor Skill

The `editor` skill provides agents with the ability to perform density-driven proofreading of technical text. It focuses on lexical economy and the elimination of "fluff" to ensure every word contributes maximum value.

## Instructions for Agents

Use this skill when you are tasked with shortening a document, increasing its impact, or making technical specifications more direct and punchy.

### Workflow

1. **Analyze the Text**:
   Run the provided analysis script on the target text file:
   ```bash
   python editor/scripts/analyze_density.py <path_to_text_file>
   ```

2. **Parse the JSON Report**:
   Carefully examine the output. Pay specific attention to:
   - `summary.density_score`: A low score indicates the text relies too heavily on function words (the, is, of, etc.). Aim for a higher ratio of content words.
   - `summary.wordiness_score`: A high score suggests the text is filled with non-essential phrases.
   - `details.wordy_phrases`: Specific multi-word phrases that can be replaced by single words.
   - `details.passive_indices`: Instances of passive voice that could be converted to active voice for more impact.
   - `details.redundant_phrases`: Tautologies or redundant word pairings.

3. **Provide Constructive Feedback**:
   Do not just list errors. Provide actionable suggestions for improvement.

   #### Feedback Guidelines:

   | Issue Type | Observation | Suggested Action |
   | :--- | :--- | :--- |
   | **Low Density** | "The density score is low ($N$)." | "The writing is heavy on function words. Try converting noun phrases to verbs (e.g., 'perform an analysis' -> 'analyze') to increase density." |
   | **Wordy Phrase** | "Found '$PHRASE' at index X." | "Replace '$PHRASE' with a more direct word (e.g., replace 'in order to' with 'to') to reduce word count." |
   | **Passive Voice** | "Passive voice detected: '$PHRASE'." | "Convert to active voice to increase impact and clarity (e.g., 'The data was sent by the system' -> 'The system sent the data')." |
   | **Redundancy** | "Redundancy detected: '$PHRASE'." | "Remove the redundant word. (e.g., 'added bonus' -> 'bonus')." |

## Example

**Input Text**:
"In order to ensure that the system is working, it is important to note that an end result must be achieved by the process. The data was sent by the client."

**Analysis Output (Conceptual)**:
```json
{
  "summary": {
    "density_score": 0.8,
    "wordiness_score": 0.4,
    "passive_voice_count": 1,
    "redundancy_count": 1
  },
  "details": {
    "wordy_phrases": ["in order to (at 0)", "it is important to note that (at 15)"],
    "passive_indices": ["was sent by the client (at 110)"],
    "redundant_phrases": ["end result (at 65)"]
  }
}
```

**Agent Feedback**:
"Your text is quite wordy. I suggest the following edits:
1. Replace 'In order to' with 'To' and remove 'it is important to note that' to improve conciseness.
2. Remove the redundancy in 'end result' by just using 'result'.
3. Convert the passive 'The data was sent by the client' to active voice: 'The client sent the data'.
These changes will significantly increase your information density."
