"""
Control LEDs for christmas
"""

from subprocess import call


def restart_leds():
    call(["/etc/init.d/rainbow", "restart"])


def disable_leds():
    call(["rainbow", "all", "disable"])


def set_led(led_device, led_option):
    call(["rainbow", led_device, led_option])
