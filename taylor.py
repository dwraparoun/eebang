from typing import Optional
import symparser
import derivative
import math


def taylor(function: str, point: Optional[float] = 0.0, nterms: int = 2):
    x_sym, f_sym = symparser.parse_single_variable_function(function)
    taylor = f_sym.subs(x_sym, point)
    for i in range(1, nterms):
        taylor += (
            derivative.derivative(function, i).subs(x_sym, point)
            / math.factorial(i)
            * (x_sym - point) ** i
        )

    return taylor
