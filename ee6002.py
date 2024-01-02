import argparse
import newton
import plot
import derivative
import taylor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Various utilities for studying MIT EE6002 at edx."
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)
    parser.add_argument("--verbose", "-v", action="store_true")

    # Newton–Raphson
    newton_parser = subparsers.add_parser("newton")
    newton_parser.add_argument(
        "function",
        type=str,
        help="single variable function, e.g. 'x**3-7+sin(x)-1/exp(4*x)'",
    )
    newton_parser.add_argument("--guess", type=float, default=0.0, help="initial guess")
    newton_parser.add_argument(
        "--nmax", type=int, default=100, help="max number of iterations"
    )
    newton_parser.add_argument(
        "--tol", type=float, default=1e-6, help="absolute error of the root's value"
    )

    # Taylor
    taylor_parser = subparsers.add_parser("taylor")
    taylor_parser.add_argument(
        "function",
        type=str,
        help="single variable function, e.g. 'x**3-7+sin(x)-1/exp(4*x)'",
    )
    taylor_parser.add_argument(
        "--point",
        "-p",
        type=float,
        default=0.0,
        help="point where Taylor expansion occurs (0 is Maclaurin)",
    )
    taylor_parser.add_argument("-n", type=int, default=5, help="number of terms")

    # Derivative
    derivative_parser = subparsers.add_parser("derivative")
    derivative_parser.add_argument(
        "function",
        type=str,
        help="single variable function, e.g. 'x**3-7+sin(x)-1/exp(4*x)'",
    )
    derivative_parser.add_argument("-n", type=int, default=1, help="derivative order")

    # Plotter
    plot_parser = subparsers.add_parser("plot")
    plot_parser.add_argument(
        "function",
        type=str,
        help="single variable function, e.g. 'x**3-7+sin(x)-1/exp(4*x)'",
    )

    args = parser.parse_args()
    if args.cmd == "newton":
        print(
            newton.newton(
                function=args.function,
                guess=args.guess,
                tol=args.tol,
                nmax=args.nmax,
                verbose=args.verbose,
            )
        )
    elif args.cmd == "plot":
        plot.plot(args.function)
    elif args.cmd == "derivative":
        print(
            derivative.derivative(
                function=args.function, order=args.n, verbose=args.verbose
            )
        )
    elif args.cmd == "taylor":
        print(taylor.taylor(function=args.function, point=args.point, nterms=args.n))
