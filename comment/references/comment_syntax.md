# Comment Syntax

Choose the native comment style for the target file and local context.

| File/context | Preferred syntax | Notes |
| --- | --- | --- |
| JavaScript/TypeScript/C/Go/Rust line note | `// ...` | Prefer for short local comments. |
| JavaScript/TypeScript/C/CSS block note | `/* ... */` | Use for multi-line comments where block comments are idiomatic. |
| Python/Ruby/Shell/YAML/TOML | `# ...` | Preserve indentation near the commented line. |
| Markdown/HTML/XML | `<!-- ... -->` | Use hidden comments when the note is for maintainers/agents, not readers. |
| SQL | `-- ...` | Prefer line comments near the relevant query clause. |

Rules:
- Prefer the smallest comment block that is clear.
- Preserve indentation and formatting.
- Do not change executable code unless explicitly asked.
- If the file already has a local comment convention, follow it.
- If no safe syntax is known, ask before editing.
