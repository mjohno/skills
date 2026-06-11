---
name: skill-manager
description: Generates spec-compliant AgentSkills.io skill packages. Use when you need to create a new skill or update an existing skill structure.
---

# Skill Manager

Goal: Generate skills which solve a provided goal.

Non-Goals: Do not implement skills directly, deploy skills to target directories, or execute skill validation code.

Use When:
- You need to create a new skill (see [Create Mode](references/mode_create.md)).
- You need to update an existing skill (see [Create Mode](references/mode_create.md)).
- You need to review a skill's quality or compliance (see [Review Mode](references/mode_review.md)).
- You need to deploy a skill to a target directory (see [Deploy Mode](references/mode_deploy.md)).

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

### [Create Mode](references/mode_create.md)
For scaffolding new skills or adding/updating components in existing ones.

### [Review Mode](references/mode_review.md)
For auditing a skill for compliance, structure, and information density.

### [Deploy Mode](references/mode_deploy.md)
For synchronizing your local skill directory to a target directory.

## Examples

### Example 1: Creating a Skill
**Prompt**: "Create a skill called 'weather-fetcher' that uses an API to get weather data. Include a python script for the API call and a JSON template for output formatting."

**Decisions**:
- Used kebab-case for the skill name: `weather-fetcher`.
- Created a standard directory structure with `scripts/` and `assets/`.
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
