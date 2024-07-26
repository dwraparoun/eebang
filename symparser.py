import ast
import sympy as sy
from typing import Optional

MATH_IDENTIFIERS = ("exp", "pi", "sin", "cos", "tan")


def parse_single_variable_function(
    function: str, variable: Optional[str] = None, is_single_variable: bool = False
):
    return _parse_function(function, variable, True)


def _parse_function(
    function: str, variable: Optional[str] = None, is_single_variable: bool = False
):
    try:
        expr = ast.parse(function)
    except SyntaxError:
        raise RuntimeError(f"Invalid python syntax: {function}")
    identifiers = []
    for node in ast.walk(expr):
        if type(node) is ast.Name:
            if node.id in identifiers or node.id in MATH_IDENTIFIERS:
                continue
            identifiers.append(node.id)

    if not identifiers:
        raise RuntimeError(f"{function} has no variables")

    if is_single_variable and len(identifiers) > 1:
        raise RuntimeError(
            f"Function of one variable expected. Got {', '.join(identifiers)}"
        )

    if variable:
        if variable not in identifiers:
            raise RuntimeError(f"{function} doesn't depend on {variable}")
        var = variable
    else:
        # pick the first identifier as function variable
        var = identifiers[0]

    for ident in identifiers:
        # create sy.Symbol, including var
        exec(f"{ident} = sy.Symbol('{ident}')")

    try:
        f = sy.sympify(function)
    except TypeError as e:
        raise RuntimeError(
            f"Failed to convert {function} to a symbolic equation, likely due to a syntax error: {str(e)}"
        )
    return (
        eval(var),  # return var as sy.Symbol rather than string
        f,
    )
