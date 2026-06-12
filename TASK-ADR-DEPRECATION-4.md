TASK_ID: ADR-DEPRECATION-4
Status: todo
Goal: Verify zero ADR references remain across the entire skills directory.
Source:
- PLAN-adr-deprecation.md#ADR-DEPRECATION-4
Targets:
- Entire skills directory (C:/Users/matjo/Documents/mjohno/workspace/skills/)
Constraints:
- This task depends on ADR-DEPRECATION-1, ADR-DEPRECATION-2, and ADR-DEPRECATION-3 (all must be completed first)
- Exclude .git/ directory from search
- Case-insensitive search for "adr"
Verification:
- `rg -i "adr" .` returns zero matches (excluding .git/)
- Both workflow.md and workflow_skills.md confirmed clean
- No ADR references in any SKILL.md, assets/, or references/ files
