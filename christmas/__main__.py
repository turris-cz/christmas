"""
Christmas main module
"""

from random import random, choice
from time import sleep

from .config import Config
from .helpers import usage, trap_signals, cleanup
from .rainbow import disable_leds, set_led


def blink(conf):
    if random() < conf.enable_probability:
        random_state = "enable"
    else:
        random_state = "disable"

    random_led = choice(conf.leds)
    random_color = choice(conf.colors)

    set_led(random_led, random_state)
    set_led(random_led, random_color)


def main():
    usage()
    conf = Config()
    trap_signals()
    disable_leds()

    while True:
        blink(conf)
        random_sleep = random() * conf.sleep_max
        sleep(random_sleep)

    cleanup()
