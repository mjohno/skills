---
name: skiller
description: Generates spec-compliant AgentSkills.io skill packages. Use when you need to create a new skill or update an existing skill structure.
---

# Skiller

Goal: Generate skills which solve a provided goal.

Use When:
- You need to create a new skill.
- You need to update an existing skill's structure or components (scripts, references, assets).

## Standard Directory Structure

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Optional: Any additional files or directories
```

## Workflows

### Standard Skill Creation

1.  **Phase 1: Planning & Specification**
    - Determine the `name` (kebab-case, must match folder) and `description`.
    - Define the goal and identify required components (scripts, references, assets).
    - **Constraint Check**: Verify the `name` complies with the [Constraints & Rules](references/RULES.md).

2.  **Phase 2: Scaffolding**
    - Create the root directory `<name>/`.
    - Initialize `SKILL.md` by applying the template found in `assets/skill_template.md`.
    - Create required sub-directories: `scripts/`, `references/`, and `assets/`.

3.  **Phase 3: Implementation & Refinement**
    - **Logic**: Implement self-contained scripts in `scripts/`.
    - **Documentation**: Populate `references/` with technical details or detailed processes.
    - **Resources**: Add necessary templates or data to `assets/`.
    - **Quality Control**: Review the completed `SKILL.md` against `assets/checklist.md` to ensure compliance, conciseness, and correct formatting.

4.  **Phase 4: Final Validation**
    - Run `skills-ref validate <skill-dir>` to ensure the package is spec-compliant.

## Examples

### Example 1

**Prompt**: "Create a skill called 'weather-fetcher' that uses an API to get weather data. Include a python script for the API call and a JSON template for output formatting."

**Decisions**:
- Used kebab-case for the skill name: `weather-fetcher`.
- Created a standard directory structure with `scripts/` and `assets/`.
- Did not include a `references/` directory as it was not necessary for this particular skill.
- Implemented requested components: `fetch_weather.py` and `output_template.json`.

**Outcome**:

```
weather-fetcher/
├── SKILL.md
├── scripts/
│   └── fetch_weather.py
└── assets/
    └── output_template.json
```
