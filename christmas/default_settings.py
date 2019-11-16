"""
Default parameters for christmas
"""

# LED would be enabled with given probability (and disabled with 1-p)
ENABLE_PROBABILITY = 0.7

# maximum delay between 2 blinks
SLEEP_MAX = 3

# list of used colors
COLORS = (
        "00FF00", # green
        "0000AA", # blue
        "FF6600", # yellow
        "FF0000", # red
)

# list of Turris Omnia leds
LEDS = (
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
