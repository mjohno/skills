TASK_ID: ADR-DEPRECATION-3
Status: todo
Goal: Remove the `adr` skill section from workflow_skills.md and renumber remaining skills.
Source:
- PLAN-adr-deprecation.md#ADR-DEPRECATION-3
Targets:
- workflow_skills.md
Constraints:
- Delete the entire `adr` skill section: "### 3. `adr` (Architectural Decision Domain)" through its Primary Artifacts line
- After deletion, renumber remaining skills: plan becomes "### 4.", task becomes "### 5.", implementation becomes "### 6.", verification becomes "### 7.", deployment becomes "### 8.", release becomes "### 9.", observability becomes "### 10.", retrospective becomes "### 11."
- Do not modify any other content in the file
Verification:
- Skill numbering is sequential (1-10) with no gaps
- `adr` skill text is fully removed
- Total skill count is 10 (down from 11)
- No orphaned blank lines or formatting artifacts left behind
