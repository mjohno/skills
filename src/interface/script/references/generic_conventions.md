# Generic Script Conventions

These rules apply to all script domains unless a domain-specific profile narrows them.

1. A script has one clear purpose and avoids unrelated responsibilities.
2. The invocation surface is explicit: CLI args, environment variables, files, stdin, API, scheduler, or another trigger.
3. Machine-readable output and IPC data use stdout.
4. Human diagnostics, progress, warnings, errors, and logs use stderr.
5. Inputs are validated before irreversible side effects.
6. Side effects are explicit, documented, and dry-runnable when meaningful.
7. Failure behavior is predictable: errors explain what failed, why it failed, and how to fix it when possible.
8. Exit or status semantics are documented and stable for callers.
9. Dependencies are minimal, justified, and documented.
10. Verification is runnable and documented, including happy paths and meaningful failure cases.
