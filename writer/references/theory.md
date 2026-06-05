# Mathematical Rationale for Sentence Length Distribution in Technical Writing

## The Log-normal Distribution in Linguistics

Natural language phenomena, including word frequency and sentence length, rarely follow a Normal (Gaussian) distribution. Instead, they typically exhibit a **Log-normal distribution**.

A variable $X$ is log-normally distributed if its natural logarithm $\ln(X)$ is normally distributed.

### Why Log-normal?
1. **Positive-only values**: Sentence length cannot be zero or negative.
2. **Right-skewness**: Most sentences in a corpus are short to medium in length, but there is a "long tail" of complex, multi-clause sentences.
3. **Multiplicative processes**: Sentence length is often the result of several additive linguistic factors (prepositional phrases, subordinate clauses, etc.) that, when modeled, tend to produce a log-normal shape.

## Optimizing for Technical Readability: The Truncated Model

While a standard log-normal distribution accurately models general human language, it is not optimal for **technical writing**. Technical documentation prioritizes clarity, precision, and reduced cognitive load.

To achieve this, we apply a **Truncated Log-normal Model**.

### 1. Target Parameters
For this skill, we target the following arithmetic properties for sentence length (measured in words):
* **Mean ($\mu_X$):** 15 words
* **Standard Deviation ($\sigma_X$):** 5 words
* **Upper Bound (Truncation):** 30 words

### 2. The Truncation Effect
By truncating the distribution at 30 words, we mathematically enforce a "readability ceiling." In technical contexts, sentences exceeding this length often contain too many nested ideas, forcing the reader to hold too much information in their working memory.

### 3. Parameter Conversion
Since most statistical libraries work with the parameters of the underlying normal distribution ($\mu_{\text{log}}$ and $\sigma_{\text{log}}$), the script performs the following transformations:

$$\sigma_{\text{log}} = \sqrt{\ln\left(1 + \frac{\sigma_X^2}{\mu_X^2}\right)}$$
$$\mu_{\text{log}} = \ln(\mu_X) - \frac{1}{2}\sigma_{\text{log}}^2$$

## Implementation Details and Limitations

### Sentence Tokenization
The `analyze_length.py` script uses regular expressions to split text into sentences. 
* **Current Approach**: Splitting on punctuation marks followed by whitespace.
* **Limitations**: This may incorrectly split on abbreviations (e.g., "e.g.", "Dr.", "vs."). While not a perfect solution, it provides a zero-dependency, lightweight method suitable for rapid automated analysis.

### Cluster Detection
Readability is not just about individual sentences, but also about the **rhythm** of the text. A sequence of several medium-length sentences can feel monotonous, while a sequence of long sentences creates "density spikes." The script uses a sliding window to detect these areas of high local density.
