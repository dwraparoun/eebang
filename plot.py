import symparser
import sympy as sy
from typing import List
import utils


def plot(functions: List[str]):
    functions_sym = []
    for function in functions:
        x_sym, f_sym = symparser.parse_single_variable_function(function)
        functions_sym.append(f_sym)
    try:
        p = sy.plotting.plot(*functions_sym)
        # p.show()
    except ValueError as e:
        utils.exit_error(str(e))
