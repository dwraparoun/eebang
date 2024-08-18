import symparser


def derivative(function: str, var: str, order: int = 1, verbose: bool = False):
    x_sym, f_sym = symparser.parse_function(function, var)
    fprime_sym = f_sym
    for i in range(abs(order)):
        if verbose:
            print(fprime_sym)
        fprime_sym = fprime_sym.diff(x_sym)

    return fprime_sym
