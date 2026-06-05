---
name: writer
description: Analyzes and proofreads technical writing for readability using a Truncated Log-normal sentence length model.
---

# Writer Skill

The `writer` skill provides agents with the ability to perform statistically-driven proofreading of technical text. It focuses on sentence length distribution to ensure clarity and optimal cognitive load for the reader.

## Instructions for Agents

Use this skill when you are tasked with reviewing, editing, or proofreading technical documentation, manuals, or academic papers.

### Workflow

1. **Analyze the Text**:
   Run the provided analysis script on the target text file:
   ```bash
   python writer/scripts/analyze_length.py <path_to_text_file>
   ```

2. **Parse the JSON Report**:
   Carefully examine the output. Pay specific attention to:
   - `summary`: Check if `mean_length` is close to the target of 15.
   - `outliers.too_short`: Sentences that may be too abrupt or lack necessary context.
   - `outliers.too_long`: Sentences that exceed the 30-word threshold and likely need splitting.
   - `high_density_clusters`: Areas where several sentences in a row are longer than average, potentially causing cognitive overload.

3. **Provide Constructive Feedback**:
   Do not just list errors. Provide actionable suggestions for improvement.

   #### Feedback Guidelines:

   | Issue Type | Observation | Suggested Action |
   | :--- | :--- | :--- |
   | **Too Long** | "Sentence at index X is very long ($N$ words)." | "Split this sentence into two or more shorter sentences at [suggested point] to improve clarity." |
   | **Too Short** | "Sentence at index X is very short ($N$ words)." | "Consider combining this sentence with the preceding or following one to provide better context, or expand it to include more detail." |
   | **High Density** | "A cluster of long sentences was detected between indices X and Y." | "This section is dense. Vary your sentence length here to improve rhythm and prevent reader fatigue." |
   | **Low Mean** | "The average sentence length is significantly below 15." | "The writing style feels staccato. Try combining some short sentences to create a smoother flow." |
   | **High Mean** | "The average sentence length is significantly above 15." | "The writing is dense. Aim for shorter, more direct sentences to increase readability." |

## Example

**Input Text**:
"The system initializes. It checks the database. Then, it proceeds to verify the credentials of the user, ensuring that the encryption keys are valid and that the connection is secure before any data is exchanged between the client and the server. This is important. The process continues."

**Analysis Output (Conceptual)**:
```json
{
  "summary": { "mean_length": 10.0, ... },
  "outliers": {
    "too_long": [
      { "index": 2, "length": 35, "text": "Then, it proceeds to..." }
    ]
  }
}
```

**Agent Feedback**:
"Your text is generally clear, but the sentence at index 2 is quite long (35 words), which may overwhelm the reader. I suggest splitting it: 'Then, it proceeds to verify the user's credentials. It ensures that the encryption keys are valid and the connection is secure before exchanging data.' Additionally, the first few sentences are a bit abrupt; consider combining them for better flow."
