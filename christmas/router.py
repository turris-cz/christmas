"""
Router classes and factory
"""

from random import random, choice

from .rainbow import set_led

OMNIA_LEDS = (
        "pwr",
        "lan0",
        "lan1",
        "lan2",
        "lan3",
        "lan4",
        "wan",
        "pci1",
        "pci2",
        "pci3",
        "usr1",
        "usr2",
)


class OmniaRouter:
    def __init__(self, conf):
        self.conf = conf

    def _get_random_state(self):
        if random() < self.conf.enable_probability:
            return "enable"
        return "disable"

    def blink(self):
        random_led = choice(OMNIA_LEDS)
        random_state = self._get_random_state()
        random_color = choice(self.conf.colors)

        set_led(random_led, random_state)
        set_led(random_led, random_color)
