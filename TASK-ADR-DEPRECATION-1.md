TASK_ID: ADR-DEPRECATION-1
Status: todo
Goal: Remove the ADR node section (lines 52-60) from workflow.md and renumber remaining deep-dive sections.
Source:
- PLAN-adr-deprecation.md#ADR-DEPRECATION-1
Targets:
- workflow.md
Constraints:
- Delete the entire ADR section: "### 3. ADR (Architecture Decision Record) — *The Decision Memory*" through the scope note (lines 52-60)
- After deletion, renumber: Task Packets becomes "### 3.", Implementation becomes "### 4.", Verification becomes "### 5.", Release becomes "### 6.", Observability becomes "### 7."
- Do not modify any other content in the file
Verification:
- Section numbering is sequential (3 through 7) with no gaps
- ADR node text is fully removed
- No orphaned blank lines or formatting artifacts left behind
