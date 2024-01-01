import argparse
import symparser
import sympy as sy

parser = argparse.ArgumentParser(description="Quick function plot.")
parser.add_argument(
    "function",
    type=str,
    help="single variable function, e.g. 'x**3-7+sin(x)-1/exp(4*x)'",
)
parser.add_argument("-n", type=int, default=1, help="derivative order")
parser.add_argument("--verbose", "-v", action="store_true")
args = parser.parse_args()
x_sym, f_sym = symparser.parse_single_variable_function(args.function)
fprime_sym = f_sym
for i in range(abs(args.n)):
    if args.verbose:
        print(fprime_sym)
    fprime_sym = fprime_sym.diff(x_sym)

print(fprime_sym)
