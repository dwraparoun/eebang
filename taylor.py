from typing import Optional
import symparser
import derivative
import math


def taylor(function: str, var: str, point: Optional[float] = 0.0, nterms: int = 2):
    x_sym, f_sym = symparser.parse_function(function, var)
    taylor = f_sym.subs(x_sym, point)
    for i in range(1, nterms):
        taylor += (
            derivative.derivative(function, i).subs(x_sym, point)
            / math.factorial(i)
            * (x_sym - point) ** i
        )

    return taylor
