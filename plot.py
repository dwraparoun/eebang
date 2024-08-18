import symparser
import sympy as sy
from typing import List


def plot(
    functions: List[str],
    xmin: float = None,
    xmax: float = None,
):
    functions_sym = []
    for function in functions:
        x_sym, f_sym = symparser.parse_parameterless_function(function)
        functions_sym.append(f_sym)
    if xmin and xmax:
        p = sy.plotting.plot(*functions_sym, (x_sym, xmin, xmax))
    else:
        p = sy.plotting.plot(*functions_sym)
