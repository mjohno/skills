# mode:review

Use this mode to critique prose as a single writing-quality workflow.

## Output
- One ranked list of findings.
- Light tags such as `readability`, `density`, and `style`.
- Severity labels: `high`, `medium`, `low`.
- A short follow-up with concise suggested changes.

## Behavior
- Infer review mode when the intent is clear.
- Ask for clarification when confidence is below 90%.
- Treat heuristics as fuzzy signals, not hard rules.
- Keep the report dense and easy to scan.
- Avoid separate readability and density sections.

## Heuristics
- Use `scripts/analyze_readability.py` and `scripts/analyze_density.py` as needed.
- Keep the signals practical; do not overstate precision.
