# Python Script Conventions

1. Assume Python 3.13+ unless the user or project specifies otherwise.
2. Use the standard library unless a third-party package is essential and justified.
3. Follow PEP 8 for style, prioritizing readability and local consistency over strictness.
4. Use type hints for function signatures, including return types.
5. Use `argparse` for CLI argument parsing.
6. Use `logging` through a module-level `log` object for diagnostics; logging must stream to stderr.
7. Use `print()` only for intentional stdout output: IPC, shell pipelines, or user-requested CLI data.
8. Catch exceptions only when adding context, cleanup, fallback behavior, or a clearer user-facing error.
9. Do not suppress exceptions without adding value; stack traces are acceptable when useful.
10. Be specific in log and error messages, including relevant values and suggested fixes when possible.
11. `main()` owns orchestration and returns an integer exit code; reusable logic belongs in typed helper functions.
12. When inline tests are used, place them near the bottom of the script before the `__main__` handler.
13. The `__main__` handler is the final block and wires parsing, logging configuration, tests, and `main()` execution.
