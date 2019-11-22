"""
Christmas main module
"""

from random import random
from time import sleep
import sys

from .config import Config
from .exceptions import ChristmasError
from .helpers import usage, trap_signals, cleanup
from .rainbow import disable_leds
from .router import router_factory


def get_router(conf):
    try:
        return router_factory(conf)
    except (FileNotFoundError, PermissionError, ChristmasError) as e:
        errprint("error: Can not get router type: {}".format(e))
        sys.exit(2)


def main():
    usage()
    conf = Config()
    router = get_router(conf)

    trap_signals()
    disable_leds()

    while True:
        router.blink()
        random_sleep = random() * conf.sleep_max
        sleep(random_sleep)

    cleanup()
