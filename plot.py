import symparser
import sympy as sy
from typing import List
import utils


def plot(
    functions: List[str],
    xmin: float = None,
    xmax: float = None,
):
    functions_sym = []
    for function in functions:
        x_sym, f_sym = symparser.parse_single_variable_function(function)
        functions_sym.append(f_sym)
    try:
        if xmin and xmax:
            p = sy.plotting.plot(
                *functions_sym, (x_sym, xmin, xmax)
            )  # , xlim=(xmin, xmax), ylim=(ymin, ymax))
        else:
            p = sy.plotting.plot(
                *functions_sym
            )  # , xlim=(xmin, xmax), ylim=(ymin, ymax))
        # p.show()
    except ValueError as e:
        utils.exit_error(str(e))
