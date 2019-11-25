"""
Router classes and factory
"""

from random import random, choice

from .exceptions import ChristmasError
from .helpers import first_line_of_file
from .rainbow import set_led

SYSINFO_MODEL_FILE = "/tmp/sysinfo/model"

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
    def __init__(self, conf, leds):
        self.conf = conf
        self.leds = leds

    def blink(self):
        random_led = choice(self.leds)
        dev_name_for_color = self._get_dev_name_for_color(random_led)
        random_state = self._get_random_state()
        random_color = choice(self.conf.colors)

        set_led(random_led, random_state)
        set_led(dev_name_for_color, random_color)

    def _get_random_state(self):
        if random() < self.conf.enable_probability:
            return "enable"
        return "disable"

    def _get_dev_name_for_color(self, led):
        """
        By default, device name to set color is the same
        """
        return led


class OmniaRouter(Router):
    def __init__(self, conf):
        super().__init__(conf, OMNIA_LEDS)


class TurrisRouter(Router):
    """
    Rainbow utility on Turris 1.x router does not support to set color for LAN
    leds indenpendently. A color can be set to all LAN leds at once using 'lan'
    device name.
    """
    def __init__(self, conf):
        super().__init__(conf, TURRIS_LEDS)

    def _get_dev_name_for_color(self, led):
        if led.startswith("lan"):
            return "lan"
        return led


def router_factory(conf):
    routers = {
        "Turris Omnia": OmniaRouter,
        "Turris": TurrisRouter,
    }

    model_name = first_line_of_file(SYSINFO_MODEL_FILE)
    try:
        return routers[model_name](conf)
    except KeyError:
        raise ChristmasError("Device not supported")
