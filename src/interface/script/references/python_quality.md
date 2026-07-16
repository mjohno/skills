# Python Script Quality Checks

Before delivering a Python script, verify the applicable checks.

## Structure
- [ ] Header docstring includes description and usage examples.
- [ ] `main()` orchestrates the script and returns an integer exit code.
- [ ] Reusable logic lives in typed helper functions, not only inline in `main()`.
- [ ] Boilerplate for parsing, logging configuration, tests, and `__main__` is easy to locate.
- [ ] `__main__` handler is the final block.

## Functionality
- [ ] Script does exactly what the user asked — no more, no less.
- [ ] User-specified requirements are implemented.
- [ ] Edge cases are handled: empty input, missing files, bad data, repeated runs.

## Error Handling
- [ ] Exceptions are caught only when adding value; failures are not silently suppressed.
- [ ] Error messages explain what failed and why, suggesting fixes when possible.
- [ ] Exit codes are bare integers, with `0` for success and nonzero for failure.

## IO and Logging
- [ ] Machine-readable output, IPC, and shell-pipeline data use stdout.
- [ ] Diagnostics, progress, warnings, errors, and logs use stderr.
- [ ] `logging` is configured through the module-level `log` object.
- [ ] Log format is `%(asctime)s [%(levelname)s] [%(funcName)s]: %(message)s`.
- [ ] `--log-level` controls the configured logging level when present.

## CLI
- [ ] `argparse` is used for command-line parsing when the script has a CLI.
- [ ] `--help` works automatically via `argparse`.
- [ ] `--dry-run` is supported when side effects are meaningful.
- [ ] `--log-level` choices are DEBUG, INFO, WARNING, ERROR, CRITICAL; default is CRITICAL.
- [ ] `--test` is supported when using the inline test pattern.

## Dry Run
- [ ] Dry-run behavior logs intended side effects without performing them.
- [ ] Dry-run output is explicit enough for the user to trust what would happen.

## Tests
- [ ] Tests cover happy paths and meaningful failure cases.
- [ ] Tests are runnable with `--test` when using the inline test pattern.
- [ ] Test assertions check both successful and failing behavior.

## Dependencies
- [ ] Standard library only unless a third-party dependency is essential and justified.
- [ ] Compatible with Python 3.13+ unless otherwise specified.

## Code Quality
- [ ] Function signatures include type hints and return types.
- [ ] Public functions have docstrings.
- [ ] Naming is consistent, readable, and PEP 8-aligned.
