import sys


def exit_error(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)
