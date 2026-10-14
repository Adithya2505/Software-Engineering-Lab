import ast
import os
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE slots (id INTEGER PRIMARY KEY, show TEXT, host TEXT, start_hour INTEGER, minutes INTEGER)"
)
STUDIO_PASSWORD = os.environ.get("STUDIO_PASSWORD")


def addSlot(show, host, start_hour, minutes):
    conn.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) VALUES (?, ?, ?, ?)",
        (show, host, start_hour, minutes),
    )


def slotLabel(show, host):
    return f"{show} hosted by {host}"


def _evaluate_expression(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float, bool)):
            return node.value
        raise ValueError("Unsupported literal value")

    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return -_evaluate_expression(node.operand)
        raise ValueError("Unsupported unary operator")

    if isinstance(node, ast.BinOp):
        left = _evaluate_expression(node.left)
        right = _evaluate_expression(node.right)
        operator_map = {
            ast.Add: lambda a, b: a + b,
            ast.Sub: lambda a, b: a - b,
            ast.Mult: lambda a, b: a * b,
            ast.Div: lambda a, b: a / b,
            ast.Mod: lambda a, b: a % b,
        }
        for operator_type, operation in operator_map.items():
            if isinstance(node.op, operator_type):
                return operation(left, right)
        raise ValueError(f"Unsupported operator: {type(node.op).__name__}")

    if isinstance(node, ast.Compare):
        left = _evaluate_expression(node.left)
        for operator, comparator in zip(node.ops, node.comparators):
            right = _evaluate_expression(comparator)
            comparison_map = {
                ast.Lt: lambda a, b: a < b,
                ast.LtE: lambda a, b: a <= b,
                ast.Gt: lambda a, b: a > b,
                ast.GtE: lambda a, b: a >= b,
                ast.Eq: lambda a, b: a == b,
                ast.NotEq: lambda a, b: a != b,
            }
            for operator_type, comparison in comparison_map.items():
                if isinstance(operator, operator_type):
                    comparison_passed = comparison(left, right)
                    break
            else:
                raise ValueError(f"Unsupported comparison: {type(operator).__name__}")
            if not comparison_passed:
                return False
            left = right
        return True

    raise ValueError("Unsupported expression")


def overlapFree(formula):
    try:
        parsed_expression = ast.parse(formula, mode="eval")
        return bool(_evaluate_expression(parsed_expression.body))
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError):
        return False


def morningShows():
    rows = conn.execute("SELECT show FROM slots WHERE start_hour < 12 ORDER BY start_hour").fetchall()
    return [row[0] for row in rows]


def removeSlot(slot_id):
    conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    addSlot("Sunrise Beats", "Vik", 7, 60)
    addSlot("Midday Talk", "Anu", 13, 45)
    print(slotLabel("Sunrise Beats", "Vik"))
    print(overlapFree("7 + 1 <= 13"), morningShows())
    removeSlot(2)


if __name__ == "__main__":
    main()
