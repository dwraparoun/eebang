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
parser.add_argument("--niter", type=int, default=5, help="number of iterations")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
var, f_sym = symparser.parse_single_variable_function(args.function)
fprime_sym = f_sym.diff(var)
f = sy.lambdify(var, f_sym, "numpy")
fprime = sy.lambdify(var, fprime_sym, "numpy")

if args.verbose:
    print(f"f({var}) = {f_sym}")
    print(f"f'({var}) = {fprime_sym}")

guess = args.guess
for i in range(args.niter):
    if args.verbose:
        print(f"i={i}, {var}={guess}")
    try:
        guess -= f(guess) / fprime(guess)
    except ZeroDivisionError as e:
        utils.exit_error(
            f"Division by zero ({fprime_sym} at {guess}). Try different --guess"
        )

print(f"{var} = {guess}")
