# Extraction Rules

Use these rules when creating task packets from other artifacts.

## From a plan item

- Preserve the plan item ID when it is suitable as a task ID.
- Copy the item title into `Goal` and refine only for clarity.
- Copy `Closes`, `Source`, or dependency references into `Source` or `Constraints`.
- Do not copy the full Gap Map unless the gap text is required to understand the task.

## From a comment

- Reference the comment ID in `Source`.
- Use the comment message as the initial `Goal` or `Constraint`.
- Include the file path and nearby symbol/section as `Targets` when known.
- Do not remove or edit the comment; that belongs to the `comment` skill.

## From a PRD or RFC

- Preserve artifact IDs such as acceptance criteria, decisions, or sections.
- Extract the smallest actionable slice.
- Keep product intent and technical constraints separate when possible.

## From direct instruction

- Infer an ID only if the caller did not provide one.
- Record the user prompt or chat summary in `Source`.
- Mark missing targets, constraints, and verification hints as unknown.
