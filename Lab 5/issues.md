# Static Analysis Issues Identified and Fixed

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL injection in slot insertion | Security / Bug | 10-12 | The code used a string-formatted SQL query with user-controlled values, making the statement vulnerable to injection. | Replaced string interpolation with parameterized SQLite queries using `?` placeholders. |
| Unsafe use of `eval` | Security / Bug | 19-23 | `eval(formula)` allowed arbitrary code execution and made validation impossible. | Replaced evaluation with a restricted AST-based expression checker that only allows safe arithmetic and comparison operations. |
| Broad exception handling | Bug | 20-23 | `except Exception:` masked all errors and hid the real cause of invalid formulas. | Narrowed the exception handling to the specific invalid-expression cases that are expected in this function. |
| Hardcoded password | Security | 5 | A literal password string was stored in the source code. | Removed the embedded credential and loaded the password from the environment instead. |
| Naming and style violations | Code quality | 8, 15, 19, 26, 31 | Functions used camelCase names and several violations were flagged by Pylint/Flake8. | Renamed functions to snake_case, added docstrings, and cleaned formatting. |
| Multiple statements and long lines | Style | 4, 11, 27 | The file contained line-length violations and a multi-statement line. | Broke long statements across lines and separated logic into readable blocks. |

## Summary

The corrected script keeps the same behaviour while removing the security issues and improving readability, maintainability, and compliance with linting standards.
