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
parser.add_argument("--guess", "-g", type=float, default=0.0, help="initial guess")
parser.add_argument("--niter", "-n", type=int, default=5, help="number of iterations")
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
for i in range(args.niter):
    if args.verbose:
        print(f"i={i}, {x_sym}={guess}")
    try:
        guess -= f(guess) / fprime(guess)
    except ZeroDivisionError as e:
        utils.exit_error(
            f"f({x_sym})/f'({x_sym})={f_sym}/{fprime_sym} results in division by zero at {x_sym}={guess}. Try different --guess"
        )

print(f"{x_sym} = {guess}")
