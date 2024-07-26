import numpy as np
import argparse


def make_f(vi):
    def f_inner(va):
        return vi - 20 * (1 - np.exp(-va / 5)) - va

    return f_inner


def make_fprime(vi):
    def fprime_inner(va):
        return -4 * np.exp(-va / 5) - 1

    return fprime_inner


parser = argparse.ArgumentParser()
parser.add_argument("--guess", type=float, default=0)
parser.add_argument("--niter", type=int, default=5)
parser.add_argument("--log", action="store_true")
parser.add_argument("--vi", type=float, default=5.0)
args = parser.parse_args()

f = make_f(args.vi)
fprime = make_fprime(args.vi)
guess = args.guess
print(f"Initial guess:{guess}")
for i in range(args.niter):
    guess = guess - f(guess) / fprime(guess)
    if args.log:
        print(f"iter:{i}, root:{guess}")

print(f"Root:{guess}")
