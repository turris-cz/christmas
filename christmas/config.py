"""
Config handler for christmas
"""

import uci

from .default_settings import COLORS, ENABLE_PROBABILITY, LEDS, SLEEP_MAX


def get_value_from_uci(uci_context, option):
    try:
        return uci_context.get("christmas", "christmas", option)
    except uci.UciExceptionNotFound:
        return None


class Config:
    def __init__(self):
        self._prepare_defaults()
        self._load_uci()

    def _prepare_defaults(self):
        self.colors = COLORS
        self.enable_probability = ENABLE_PROBABILITY
        self.leds = LEDS
        self.sleep_max = SLEEP_MAX

    def _load_uci(self):
        with uci.Uci() as uci_context:
            self._set_colors_from_uci(uci_context)
            self._set_probability_from_uci(uci_context)
            self._set_sleep_from_uci(uci_context)

    def _set_colors_from_uci(self, uci_context):
        value = get_value_from_uci(uci_context, "colors")
        if value:
            self.colors = value

    def _set_probability_from_uci(self, uci_context):
        value = get_value_from_uci(uci_context, "enable_probability")
        if value:
            self.enable_probability = float(value)

    def _set_sleep_from_uci(self, uci_context):
        value = get_value_from_uci(uci_context, "sleep_max")
        if value:
            self.sleep = int(value)
