"""
Christmas main module
"""

from random import random
from time import sleep

from .config import Config
from .helpers import usage, trap_signals, cleanup
from .rainbow import disable_leds
from .router import router_factory


def main():
    usage()
    conf = Config()
    router = router_factory(conf)

    trap_signals()
    disable_leds()

    while True:
        router.blink()
        random_sleep = random() * conf.sleep_max
        sleep(random_sleep)

    cleanup()
