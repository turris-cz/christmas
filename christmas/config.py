"""
Config handler for christmas
"""

import euci

from .default_settings import COLORS, ENABLE_PROBABILITY, LEDS, SLEEP_MAX
from .helpers import errprint


def get_value_from_uci(euci_context, option, **kwargs):
    try:
        return euci_context.get("christmas", "christmas", option, **kwargs)
    except euci.UciExceptionNotFound:
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
        with euci.EUci() as euci_context:
            self._set_list_from_uci(euci_context, "colors")
            self._set_option_from_uci(euci_context, "enable_probability")
            self._set_option_from_uci(euci_context, "sleep_max")

    def _set_list_from_uci(self, euci_context, option):
        uci_value = get_value_from_uci(euci_context, option, list=True)
        if uci_value:
            setattr(self, option, uci_value)

    def _set_option_from_uci(self, euci_context, option):
        try:
            uci_value = get_value_from_uci(euci_context, option, list=False)
            if uci_value:
                value = float(uci_value)
                setattr(self, option, value)
        except ValueError:
            errprint(
                    "warning: Invalid value of UCI option {} (should be float, got {})"
                    "".format(option, uci_value)
            )
