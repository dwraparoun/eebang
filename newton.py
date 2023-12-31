import argparse
import symparser
import sympy as sy
import utils

parser = argparse.ArgumentParser(description="Newton–Raphson root finding algorithm.")
parser.add_argument(
    "function",
    type=str,
    help="single variable function, e.g. 'x**3-7+sin(x)-1/exp(4*x)'",
)
parser.add_argument("--guess", type=float, default=0.0, help="initial guess")
parser.add_argument("--nmax", type=int, default=100, help="max number of iterations")
parser.add_argument(
    "--tol", type=float, default=1e-6, help="absolute convergence criterion"
)
parser.add_argument("--verbose", "-v", action="store_true")
args = parser.parse_args()
x_sym, f_sym = symparser.parse_single_variable_function(args.function)
fprime_sym = f_sym.diff(x_sym)
f = sy.lambdify(x_sym, f_sym, "numpy")
fprime = sy.lambdify(x_sym, fprime_sym, "numpy")

if args.verbose:
    print(f"f({x_sym}) = {f_sym}")
    print(f"f'({x_sym}) = {fprime_sym}")

guess = args.guess
if args.verbose:
    print(f"Using {x_sym}={guess} as initial guess")
i = 0
while True:
    try:
        guess -= f(guess) / fprime(guess)
    except ZeroDivisionError as e:
        utils.exit_error(
            f"f({x_sym})/f'({x_sym})={f_sym}/{fprime_sym} results in division by zero at {x_sym}={guess}. Try different --guess"
        )
    tol = abs(f(guess))
    if args.verbose:
        print(f"i={i}, {x_sym}={guess}, tol={tol}")
    if tol <= args.tol:
        break
    i += 1
    if i == args.nmax:
        utils.exit_error(
            f"Failed to converge after {i} iterations. |f({x_sym}={guess})| = {tol} <= {args.tol}"
        )

print(f"{x_sym} = {guess}")
