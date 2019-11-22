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

TURRIS_LEDS = (
        "wan",
        "lan1",
        "lan2",
        "lan3",
        "lan4",
        "lan5",
        "wifi",
        "pwr",
)


class Router:
    def __init__(self, conf):
        self.conf = conf

    def _get_random_state(self):
        if random() < self.conf.enable_probability:
            return "enable"
        return "disable"


class OmniaRouter(Router):
    def blink(self):
        random_led = choice(OMNIA_LEDS)
        random_state = self._get_random_state()
        random_color = choice(self.conf.colors)

        set_led(random_led, random_state)
        set_led(random_led, random_color)


class TurrisRouter(Router):
    """
    Rainbow utility on Turris 1.x router does not support to set color for LAN
    leds indenpendently. A color can be set to all LAN leds at once using 'lan'
    device name.
    """
    def _get_dev_name_for_color(self, led):
        if led.startswith("lan"):
            return "lan"
        return led

    def blink(self):
        random_led = choice(TURRIS_LEDS)
        dev_name_for_color = self._get_dev_name_for_color(random_led)
        random_state = self._get_random_state()
        random_color = choice(self.conf.colors)

        set_led(random_led, random_state)
        set_led(dev_name_for_color, random_color)
