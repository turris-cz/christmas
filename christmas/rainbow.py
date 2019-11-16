"""
Control LEDs for christmas
"""

from subprocess import call

from .exceptions import ChristmasError


SYSINFO_MODEL_FILE = "/tmp/sysinfo/model"

LEDS_OMNIA = (
        'pwr',
        'lan0',
        'lan1',
        'lan2',
        'lan3',
        'lan4',
        'wan',
        'pci1',
        'pci2',
        'pci3',
        'usr1',
        'usr2',
)

LEDS_TURRIS = (
        'wan',
        'lan',
        'wifi',
        'pwr',
)


def restart_leds():
    call(["/etc/init.d/rainbow", "restart"])


def disable_leds():
    call(["rainbow", "all", "disable"])


def set_led(led_device, led_option):
    call(["rainbow", led_device, led_option])


def first_line_of_file(filename):
    with open(filename, "r") as f:
        line = f.readline()
    return line.rstrip("\n")


def device_leds_list():
    model_name = first_line_of_file(SYSINFO_MODEL_FILE)

    if model_name == "Turris Omnia":
        return LEDS_OMNIA
    elif model_name == "Turris":
        return LEDS_TURRIS
    else:
        raise ChristmasError("Device not supported")
