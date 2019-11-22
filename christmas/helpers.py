"""
Miscellaneous helpers for christmas
"""

import signal
import sys

from .rainbow import restart_leds


USAGE = """USAGE:
    {}""".format(sys.argv[0])


def errprint(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def usage():
    if len(sys.argv) != 1:
        errprint(USAGE)
        exit(1)


def cleanup():
    restart_leds()


def signal_handler(signal, frame):
    cleanup()
    sys.exit(0)


def trap_signals():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


def first_line_of_file(filename):
    with open(filename, "r") as f:
        line = f.readline()
    return line.rstrip("\n")
