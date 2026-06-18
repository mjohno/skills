# Python Script Conventions

1. Use standard library only unless a third-party package is essential.
2. Follow PEP 8 for style, but prioritize readability and consistency over strict adherence.
3. Use Type Hints for all functions, including return types.
4. Catch and log exceptions only when necessary.
5. Don't catch exceptions just to suppress them. It is OK to expose stack traces.
6. Use the provided `log` object for all logging, and avoid print statements.
7. Be specific and informative in log messages, including relevant variable values.
8. Be specific about what failed and why in error messages, and suggest fixes when possible.
9. Custom code goes at the top of the script in the `main` function.
10. Custom tests go at the bottom of the script, in the test handler.
11. the __main__ handler is at the very bottom of the script, after all functions and tests.
12. Assume python 3.13 is the minimum version.
