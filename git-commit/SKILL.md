---
name: git-commit
description: Generates and executes a git commit message adhering to the Conventional Commits specification. Use when you need to commit staged changes.
metadata:
  type: skill
---

# Git Commit

Goal: Generate and execute a git commit message that adheres strictly to the [Conventional Commits](git-commit/references/CONVENTIONAL_COMMITS.md) specification.

Use When:
- You need to commit staged changes with automated analysis.

Non-Goals:
- Committing unstaged changes (requires manual staging first)
- Creating merge commits, amends, or rebases
- Bypassing commit message standards

## Workflow

1. **Pre-flight Check**:
   - Run `git status --porcelain` to check the state of the repository.
   - If no changes are staged: Inform the user. Offer to stage all changes (`git add .`) or exit.
   - If changes are present but not staged: Inform the user and ask if they wish to stage them before proceeding.

2. **Analyze Changes**:
   - If the agent is in a "fresh" context or no specific change description is provided, run `git diff --cached` to analyze the staged changes.
   - Determine the **Type** (e.g., `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`).
   - Determine the **Scope** (optional, e.g., a module or directory).
   - Detect **Breaking Changes**: Look for API removals, significant structural shifts, or explicit indicators in the diff.

3. **Draft Message**:
   - **Header**: Construct as `<type>(<scope>): <subject>`. If a breaking change is detected, append `!` to the header (e.g., `feat(api)!: <subject>`).
   - **Subject**: Write a concise subject line in the imperative mood (< 50 characters).
   - **Body**: If the change is complex, provide a summary of *what* changed and *why* based on the diff analysis. Omit when the subject sufficiently describes the change.
   - **Footer**: 
     - If a breaking change was detected, include `BREAKING CHANGE: <description>`.
     - If an issue key (e.g., `ABC-123`) is provided or detected, include it as `Refs: <key>` or within the subject if space permits.

4. **Review & Approval**:
   - Present the complete drafted message to the user.
   - Ask for confirmation: `Proceed with this commit? [Y/n/edit]`.
   - **Auto-Approval**: If the user's initial request implies immediate execution (e.g., "commit these changes now"), skip the manual prompt.

5. **Execute Commit**:
   - Use `git commit -F <temp_file>` or multiple `-m` flags to ensure the full message (Header, Body, Footer) is correctly preserved with proper line breaks.
   - Verify success with `git log -1`.

## Constraints
- Follow the [Conventional Commits](git-commit/references/CONVENTIONAL_COMMITS.md) standard strictly.
- The header subject line should be <= 50 characters.
- Always ensure breaking changes are clearly marked in both the header (`!`) and the footer.
- Do not attempt to commit if no changes are staged.

## Examples

### Example 1: Basic commit
**Prompt**: "commit my changes"
**Decisions**: Analyzed `git diff --cached` and identified the change as a `feat` type with no scope or breaking changes.
**Outcome**:
```
feat: add user authentication logic
```

### Example 2: Basic commit with issue key
**Prompt**: "commit my changes for ABC-123"
**Decisions**: Identified the issue key `ABC-123` and applied it to the footer using the `Refs:` prefix.
**Outcome**:
```
fix(ui): resolve button alignment in header
Refs: ABC-123
```

### Example 3: Advanced commit (Breaking Change)
**Prompt**: "commit my changes. I'm breaking the API by removing the old login method."
**Decisions**: Detected a breaking change in the diff; appended `!` to the header and added a `BREAKING CHANGE` footer.
**Outcome**: `refactor(auth)!: remove deprecated login method` with body and `BREAKING CHANGE` footer.
