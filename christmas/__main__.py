"""
Christmas main module
"""

from random import random, choice
from time import sleep

from .helpers import usage, trap_signals, cleanup, get_leds_list
from .rainbow import disable_leds, set_led

from .default_settings import COLORS, ENABLE_PROBABILITY, SLEEP_MAX


def blink(leds):
    if random() < ENABLE_PROBABILITY:
        random_state = "enable"
    else:
        random_state = "disable"

    random_led = choice(leds)
    random_color = choice(COLORS)

    set_led(random_led, random_state)
    set_led(random_led, random_color)


def main():
    usage()
    led_list = get_leds_list()
    trap_signals()
    disable_leds()

    while True:
        blink(led_list)
        random_sleep = random() * SLEEP_MAX
        sleep(random_sleep)

    cleanup()
