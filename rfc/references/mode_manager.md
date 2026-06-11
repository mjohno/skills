# Mode: Manager

This mode is used to maintain the RFC index and track the lifecycle of RFCs.

## Workflow

### 1. Register
When a new RFC is written:
- Determine the next sequential RFC number (e.g., if `RFC-003-foo.md` is the highest, register as `RFC-004-<name>.md`).
- Create or update `RFC_INDEX.md` alongside the RFC files.
- Set initial status to **Draft**.

### 2. Update Status
Change an RFC's status in the index:
- Valid statuses: `Draft` → `Review` → `Approved` → `Superseded`
- Update the index entry immediately upon status change.

### 3. Supersede
When an RFC replaces a previous one:
- Mark the older RFC's status as **Superseded**.
- Record the superseding RFC number in the older entry.
- Update `RFC_INDEX.md` alongside the RFC files.

### 4. Validate
Check that the index is consistent:
- Verify every RFC listed in the index exists as a file.
- Flag orphaned entries (in the index but no file) or orphaned files (exist but not in the index).
- Report any status inconsistencies.

### 5. Audit
Generate a report of all RFCs:

```markdown
## RFC Index

| RFC ID | Name | Status | PRD Reference | Linked Reviews | Decision Count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RFC-001 | [Name] | Draft/Review/Approved/Superseded | [PRD reference] | [Count] | [Count] |
| RFC-002 | [Name] | Draft/Review/Approved/Superseded | [PRD reference] | [Count] | [Count] |
```

### RFC_INDEX.md Format
```markdown
# RFC Index

Last updated: [Timestamp]

| RFC ID | Name | Status | PRD Reference | Linked Reviews | Decision Count | File Exists |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RFC-001 | [Name] | [Status] | [PRD ref] | [N] | [N] | [Yes/No] |
| RFC-002 | [Name] | [Status] | [PRD ref] | [N] | [N] | [Yes/No] |
```
