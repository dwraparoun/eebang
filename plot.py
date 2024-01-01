import argparse
import symparser
import sympy as sy
import utils

parser = argparse.ArgumentParser(description="Quick function plot.")
parser.add_argument(
    "function",
    type=str,
    help="single variable function, e.g. 'x**3-7+sin(x)-1/exp(4*x)'",
)
args = parser.parse_args()
x_sym, f_sym = symparser.parse_single_variable_function(args.function)
p = sy.plotting.plot(f_sym, show=False)
p.show()
