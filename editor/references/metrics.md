# Editor Metrics Methodology

The `editor` skill uses heuristic-based analysis to evaluate text density and conciseness. Because it relies on regex and word lists rather than a full NLP model (like spaCy), users should be aware of potential false positives and negatives.

## 1. Information Density Score

**Definition**: The ratio of "Content Words" to "Function Words".

- **Content Words**: Words that carry semantic weight (Nouns, Verbs, Adjectives, Adverbs).
- **Function Words**: Words that provide grammatical structure (Articles, Prepositions, Conjunctions, Pronouns, Auxiliary Verbs).

**Calculation**:
$$\text{Density Score} = \frac{\text{Count of Content Words}}{\text{Count of Function Words}}$$

*A higher score indicates more information-dense writing. A lower score suggests the text is "wordy" or relies heavily on grammatical scaffolding.*

## 2. Wordiness (Fluff Detection)

**Definition**: The identification of multi-word phrases that can be replaced by a single word or removed entirely without changing the meaning.

**Detection Method**: Regex matching against a predefined list of common filler phrases.

**Examples**:
- `"in order to"` -> `"to"`
- `"due to the fact that"` -> `"because"`
- `"it is important to note that"` -> (Remove)

## 3. Passive Voice Detection

**Definition**: A grammatical construction where the subject of the sentence is the recipient of the action.

**Detection Method**: A heuristic regex pattern looking for forms of the verb "to be" followed by a past participle (typically ending in `-ed`).

**Pattern**: `(is|are|was|were|been|being)\s+\w+ed`

*Note: This is a heuristic and may flag words like "the heated blanket" (adjective) as passive voice.*

## 4. Redundancy (Tautology)

**Definition**: Using two or more words that mean the same thing, creating unnecessary repetition.

**Detection Method**: Regex matching for common redundant pairs.

**Examples**:
- `"added bonus"`
- `"end result"`
- `"past history"`
- `"summarize briefly"`
