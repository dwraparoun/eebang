import symparser
import sympy as sy
import utils
from typing import Optional


def newton(
    function: str,
    guess: Optional[float] = 0,
    tol: Optional[float] = 1e-6,
    nmax: Optional[int] = 50,
    verbose: bool = False,
):
    x_sym, f_sym = symparser.parse_single_variable_function(function)
    fprime_sym = f_sym.diff(x_sym)
    f = sy.lambdify(x_sym, f_sym, "numpy")
    fprime = sy.lambdify(x_sym, fprime_sym, "numpy")

    if verbose:
        print(f"f({x_sym}) = {f_sym}")
        print(f"f'({x_sym}) = {fprime_sym}")

    if verbose:
        print(f"Using {x_sym}={guess} as initial guess")
    i = 0
    while True:
        try:
            guess -= f(guess) / fprime(guess)
        except ZeroDivisionError as e:
            utils.exit_error(
                f"f({x_sym})/f'({x_sym})={f_sym}/{fprime_sym} results in division by zero at {x_sym}={guess}. Try different --guess"
            )
        curr_tol = abs(f(guess))
        if verbose:
            print(f"i={i}, {x_sym}={guess}, tol={curr_tol}")
        if curr_tol <= tol:
            return guess
        i += 1
        if i == nmax:
            utils.exit_error(
                f"Failed to converge after {i} iterations. |f({x_sym}={guess})| = {curr_tol} <= {tol}"
            )
