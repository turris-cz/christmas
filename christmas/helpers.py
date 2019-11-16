"""
Miscellaneous helpers for christmas
"""

import sys
import signal

from .exceptions import ChristmasError
from .rainbow import restart_leds, device_leds_list


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


def get_leds_list():
    try:
        return device_leds_list()
    except (FileNotFoundError, PermissionError, ChristmasError) as e:
        errprint("error: Can not determine LED list: {}".format(e))
        sys.exit(2)
