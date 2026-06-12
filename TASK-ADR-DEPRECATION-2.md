TASK_ID: ADR-DEPRECATION-2
Status: todo
Goal: Remove or rewrite all remaining ADR references in workflow.md.
Source:
- PLAN-adr-deprecation.md#ADR-DEPRECATION-2
Targets:
- workflow.md
Constraints:
- This task depends on ADR-DEPRECATION-1 (ADR node section must be removed first)
- Do not introduce new references or alter content unrelated to ADR
Specific changes:
1. RFC inputs line: remove "previous `ADRs`" from the inputs list
2. Task Packets inputs: remove "relevant `ADR`s" from the inputs list
3. Implementation inputs: change "The `RFC`, the `ADR`" to "The `RFC`"
4. Implementation code review gate: change "RFC`/`ADR`" to "RFC`"
5. Technical Retrospective scope: change "RFC/ADR" to "RFC"
6. Technical Retrospective output: remove "ADR library" mention from "Updates to the `ADR` library or revisions to the `RFC` technical templates"
7. Procedural Retrospective input: change "RFC → ADR → Task Packets" to "RFC → Task Packets"
8. Summary Mapping table: delete the entire ADR row ("Why did they choose X?")
9. Golden Rule: rewrite the sentence "it **must** be captured in an **ADR**" — since ADR rationale lives in RFC, change to "it **must** be updated in the **RFC**"
Verification:
- `rg -i "adr" workflow.md` returns zero matches
- All remaining cross-references are semantically correct
