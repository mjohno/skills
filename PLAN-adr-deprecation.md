PLAN_ID: ADR-DEPRECATION
Source: workflow.md, workflow_skills.md
Purpose: Remove ADR from the engineering workflow and clean up all references, since ADR rationale is already captured in RFC.

## Gap Map

| Gap ID | Current Problem | Target State |
| --- | --- | --- |
| GAP-1 | `workflow.md` contains a full ADR node section (section 3) that duplicates RFC content | ADR node removed from deep dive; remaining sections renumbered |
| GAP-2 | ADR referenced in 8 locations across `workflow.md` (inputs, retrospectives, mapping table, golden rule) | All ADR references cleaned up contextually; no broken or dangling references |
| GAP-3 | `workflow_skills.md` contains a full `adr` skill section with 3 engagement modes | `adr` skill removed; remaining skills renumbered |
| GAP-4 | No other files in the repository reference ADR, creating false confidence that removal is safe | Verified: ADR appears only in workflow.md and workflow_skills.md; no breaking changes |

## Work Plan

### ADR-DEPRECATION-1 — Remove ADR node from workflow.md

Closes: GAP-1
Status: planned
Depends on: none
Outcome: ADR section deleted from workflow.md deep dive

Deliverables:
- workflow.md with ADR node (lines 52-60) removed
- Remaining deep-dive sections renumbered (Task Packets → 3, Implementation → 4, Verification → 5, Release → 6, Observability → 7)

Done when:
- ADR node section is fully removed
- Section numbering is sequential with no gaps
- No orphaned "### 3." or "### 4." numbering issues

### ADR-DEPRECATION-2 — Clean up ADR references in workflow.md

Closes: GAP-2
Status: planned
Depends on: ADR-DEPRECATION-1
Outcome: All ADR references removed or rewritten in workflow.md

Deliverables:
- RFC inputs: remove "previous `ADRs`" from the inputs list
- Task Packets inputs: remove "relevant `ADR`s" from the inputs list
- Implementation inputs: "The `RFC`, the `ADR`" → "The `RFC`"; "RFC`/`ADR`" → "RFC`"
- Technical Retrospective scope: "RFC/ADR" → "RFC"; output: remove "ADR library" mention
- Procedural Retrospective input: "RFC → ADR → Task Packets" → "RFC → Task Packets"
- Summary Mapping table: delete the ADR row entirely
- Golden Rule: rewrite to remove ADR reference (the rule about promoting architectural decisions — since rationale lives in RFC, this rule becomes: "If a discussion in a Task, Plan, or Pull Request results in a permanent change to the system's architecture or design principles, update the RFC.")

Done when:
- `rg -i "adr" workflow.md` returns zero matches
- All remaining references are semantically correct (no broken cross-references)

### ADR-DEPRECATION-3 — Remove adr skill from workflow_skills.md

Closes: GAP-3
Status: planned
Depends on: none
Outcome: `adr` skill section removed from workflow_skills.md

Deliverables:
- workflow_skills.md with `adr` skill section deleted
- Remaining skills renumbered (plan → 3, task → 4, implementation → 5, verification → 6, deployment → 7, release → 8, observability → 9, retrospective → 10)

Done when:
- `adr` skill section is fully removed
- Skill numbering is sequential with no gaps
- Total skill count reduced from 11 to 10

### ADR-DEPRECATION-4 — Verify no other ADR references exist

Closes: GAP-4
Status: planned
Depends on: ADR-DEPRECATION-1, ADR-DEPRECATION-2, ADR-DEPRECATION-3
Outcome: Full repository scan confirms no remaining ADR references

Deliverables:
- Verification command output showing zero ADR matches across all files

Done when:
- `rg -i "adr" .` returns zero matches (excluding .git/)
- Both workflow.md and workflow_skills.md are clean
