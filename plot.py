import symparser
import sympy as sy


def plot(function: str):
    # TODO plot multiple functions
    x_sym, f_sym = symparser.parse_single_variable_function(function)
    p = sy.plotting.plot(f_sym, show=False)
    p.show()
