import ast
import sympy as sy
from typing import Optional
import utils

MATH_IDENTIFIERS = ("e", "exp", "pi", "sin", "cos", "tan")


def parse_single_variable_function(
    function: str, variable: Optional[str] = None, is_single_variable: bool = False
):
    return _parse_function(function, variable, True)


def _parse_function(
    function: str, variable: Optional[str] = None, is_single_variable: bool = False
):
    expr = ast.parse(function)
    identifiers = []
    for node in ast.walk(expr):
        if type(node) is ast.Name:
            # identifier like 'x' or 'my_var'
            if node.id in identifiers or node.id in MATH_IDENTIFIERS:
                continue
            identifiers.append(node.id)

    if not identifiers:
        utils.exit_error(f"{function} has no variables")

    if is_single_variable and len(identifiers) > 1:
        utils.exit_error(f"{function} has multiple variables: {', '.join(identifiers)}")

    if variable:
        if variable not in identifiers:
            utils.exit_error(f"{function} doesn't depend on {variable}")
        var = variable
    else:
        # pick the first identifier as function variable
        var = identifiers[0]

    for ident in identifiers:
        # create sy.Symbol, including var
        exec(f"{ident} = sy.Symbol('{ident}')")

    f = sy.sympify(function)
    return (
        eval(var),  # return var as sy.Symbol rather than string
        f,
    )
