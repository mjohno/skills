# Workflow: Diff Review

Reviews the changes between a base ref and HEAD. Use when the review target is a git diff, pull request, branch delta, or "what changed" review.

## Context
Receives pre-built context from the router: repository/path, base ref, head ref, optional specs, lenses, and annotation hints.

## Steps

### 1. Establish Diff Range
- Determine the base ref from user input when provided.
- If no base is provided, use the repository default branch or ask when ambiguous.
- Prefer merge-base semantics for branch reviews: `git diff <base>...HEAD`.
- Record the exact command/ref range used in the report sources.

### 2. Collect Changed Targets
Inspect the diff and changed files:
- Added, modified, deleted, renamed files
- Behavioral changes and public API changes
- Tests added/changed/removed
- Migration/config/documentation changes

Review changed lines first, but inspect surrounding context when needed to judge correctness.

### 3. Apply Review Criteria
Apply, in order:
- User-provided specs or acceptance criteria, when present
- Loaded artifact specs, when relevant
- Loaded lenses, always including `lens_generic.md`
- Discovered `REVIEW(<id>)` annotations that are in or relevant to the diff

### 4. Categorize Findings by Severity
Use the severity scale defined in `assets/severity.md`.

### 5. Report Findings
Use template: `assets/template_report.md`.
Include:
- Diff range and command used
- Changed files reviewed
- Findings tied to changed files/lines where possible
- Spec/lens/annotation source for each finding
- Any unreviewed files or limits

## Patterns
- **Finding format**: `P<n> - <issue> (source: <spec/lens/annotation>, target: <file/range>)`
- **Scope rule**: Findings should be about introduced, removed, or exposed risk in the diff. Mention pre-existing issues only when the diff worsens them or depends on them.

## Constraints
1. Do not review the whole repository as if every issue is in scope.
2. Cite the diff range and changed targets.
3. Be specific and actionable.
4. Do not perform remediation — only comparison and reporting.

## Outputs
Review report using `assets/template_report.md` with findings categorized P1-P5.
