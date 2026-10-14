# Reflection on Static Code Analysis

1. What is static code analysis and why is it important?

   Static code analysis is the process of inspecting source code without executing it to find issues such as bugs, vulnerabilities, style problems, and maintainability problems. It is important because it helps developers catch problems early, reduce future defects, and improve security before the code is deployed.

2. What did the three tools help you find?

   Pylint helped identify naming issues, missing docstrings, and poor code structure. Flake8 helped with formatting problems such as line length and multi-statement lines. Bandit highlighted security issues, including unsafe SQL construction and use of `eval`.

3. Which issues were the most critical, and how did you fix them?

   The most critical issues were the SQL injection risk and the unsafe use of `eval`, because they could allow malicious code to run or manipulate the database. I fixed them by using parameterized SQL and a safe AST-based expression validator. I also removed the hardcoded password and cleaned the code style.

4. What did you learn from the lab?

   I learned that even a small script can contain hidden security and quality defects. Static analysis tools are valuable because they provide fast, objective feedback and help produce code that is safer, cleaner, and easier to maintain.
