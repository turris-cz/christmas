"""
Christmas main module
"""

from random import random, choice
from time import sleep

from .helpers import usage, trap_signals, cleanup
from .rainbow import disable_leds, set_led

from .default_settings import COLORS, ENABLE_PROBABILITY, LEDS, SLEEP_MAX


def blink():
    if random() < ENABLE_PROBABILITY:
        random_state = "enable"
    else:
        random_state = "disable"

    random_led = choice(LEDS)
    random_color = choice(COLORS)

    set_led(random_led, random_state)
    set_led(random_led, random_color)


def main():
    usage()
    trap_signals()
    disable_leds()

    while True:
        blink()
        random_sleep = random() * SLEEP_MAX
        sleep(random_sleep)

    cleanup()
