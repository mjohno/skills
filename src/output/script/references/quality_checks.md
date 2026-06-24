# Quality Checks

Before delivering a script, verify all of the following:

## Structure
- [ ] Header with description and examples
- [ ] Custom code lives in the `main` function at the top of the script
- [ ] Boilerplate (logging, `parse_args`) follows custom code
- [ ] Test harness at the bottom, before `__main__`
- [ ] `__main__` handler is the very last block in the script
- [ ] CLI entry point calls `sys.exit(main(args))` and `sys.exit(run_tests())`

## Functionality
- [ ] Script does exactly what the user asked — no more, no less
- [ ] All user-specified requirements are implemented
- [ ] Edge cases are handled (empty input, missing files, bad data)

## Error Handling
- [ ] Exceptions caught only when necessary — don't suppress them
- [ ] It is OK to expose stack traces when appropriate
- [ ] Exit codes are bare integers (0 for success, 1 for failure)

## Logging
- [ ] `logging` module used via the provided `log` object for stderr output
- [ ] Logging always goes to stderr; never use logging for stdout
- [ ] Log messages are specific and include relevant variable values
- [ ] Error messages explain what failed and why, suggest fixes when possible
- [ ] Log format: `%(asctime)s [%(levelname)s] [%(funcName)s]: %(message)s`
- [ ] Logging streams to `sys.stderr`

## CLI
- [ ] `argparse` used for argument parsing
- [ ] `--help` works (automatic via argparse)
- [ ] `--dry-run` flag supported
- [ ] `--log-level` flag with choices: DEBUG, INFO, WARNING, ERROR, CRITICAL (default: CRITICAL)
- [ ] `--test` flag supported
- [ ] `print()` is for CLI output, IPC, and shell pipelines (stdout)

## Dry-Run
- [ ] `--dry-run` flag parsed in `parse_args()`
- [ ] Dry-run behavior implemented in user logic (logged actions without side effects)

## Tests
- [ ] `run_tests()` function included
- [ ] Uses `unittest` with a `TestScript(unittest.TestCase)` class
- [ ] Tests cover happy path and error cases
- [ ] Tests runnable via `--test` flag
- [ ] Test assertions check both success and failure paths

## Dependencies
- [ ] Standard library only (third-party only if truly essential)
- [ ] Compatible with Python 3.13+

## Code Quality
- [ ] Type hints on all function signatures, including return types
- [ ] Docstrings on all public functions
- [ ] Consistent naming conventions (PEP 8, readability over strictness)
