# Static Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| B324: Weak MD5 hash | Security - High | 47 | MD5 was used without indicating that the hash is not used for security. | Explicitly set `usedforsecurity=False` because the member hash is only an identifier. |
| B605: Shell execution | Security - High | 58 | `os.system()` executed a shell command using a filename value. | Removed shell execution and used Python's `print()` function for the status message. |
| B307: Use of eval | Security - Medium | 42 | `eval()` evaluated a caller-provided discount expression, allowing arbitrary code execution. | Replaced the expression argument with a numeric discount rate and calculated the fee directly. |
| B110: Bare exception with pass | Reliability - Low | 26-27 | A bare `except` silently ignored every possible exception while cancelling a membership. | Replaced the `try`/`except` block with `members.pop(m_id, None)`. |
| B311: Insecure random generator | Security - Low | 51 | The standard `random` module was used to generate a locker PIN. | Replaced it with `secrets.randbelow()` for security-oriented random generation. |
| B105: Hardcoded password string | Security - Low | 70 | A portal secret was hardcoded directly in the source code. | Removed the unused hardcoded secret from the program. |
| C0116: Missing function docstrings | Pylint - Convention | 15, 23, 30, 40, 46, 50, 54, 61, 69 | Public functions did not explain their purpose. | Add concise docstrings to each function. |
| C0103: Invalid function names | Pylint - Convention | 15, 23, 30, 40 | Function names used camelCase instead of the project's required snake_case style. | Rename functions using snake_case and update their call sites. |
| W0102: Dangerous default value | Pylint - Warning | 15 | `registerMember()` used a mutable list as a default argument. | Use `None` as the default and create a new list inside the function. |
| W0612/F841: Unused variables | Pylint/Flake8 - Warning | 31, 41, 63 | `locker_deposit`, `base_fee`, and the loop variable `m` were assigned but unused. | Remove unused assignments and use meaningful loop variables. |
| C0209: Old-style string formatting | Pylint - Convention | 19 | A percent-format string was used where an f-string was clearer. | Replace percent formatting with an f-string. |
| C0121/E711: Comparison with `None` | Pylint/Flake8 - Convention | 32 | Membership lookup used `== None` instead of identity comparison. | Use `is None`. |
| R1703/R1705: Simplifiable conditional | Pylint - Refactoring | 34 | An `if`/`else` returned boolean values with an unnecessary `else`. | Return the boolean expression directly. |
| W1514: Unspecified file encoding | Pylint - Warning | 55 | The roster file was opened without an explicit encoding. | Open the file with `encoding="utf-8"`. |
| R1732: Resource allocation without context manager | Pylint - Refactoring | 55 | The output file was manually opened and closed. | Use a `with open(...)` context manager. |
| W0621: Redefined outer name | Pylint - Warning | 61 | `get_active_summary()` reused the global name `members` as a parameter. | Rename the parameter to avoid shadowing the global. |
| W0611/F401: Unused import | Pylint/Flake8 - Warning | 6 | The `math` module was imported but never used. | Remove the unused import. |
| E501: Lines too long | Flake8 - Formatting | 10-11, 18 | Several source lines exceeded the 79-character limit. | Wrap the lines to comply with the configured line length. |
| E722/Bare except | Flake8 - Error | 26 | A bare `except` caught every exception type. | Catch only expected exceptions or use a safe dictionary operation. |
| W292/C0304: Missing final newline | Flake8/Pylint - Formatting | 73, 82 | The source file did not end with a newline. | Add a final newline to the file. |
