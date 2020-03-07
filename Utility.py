DEBUG_MODE = True
import numpy as np


def print_debug(str_in, end="\n"):
    if DEBUG_MODE:
        print(str_in, end=end)


def distance(location_a, location_b):
    import math
    return math.sqrt((location_a[0] - location_b[0]) ** 2 + (location_a[1] - location_b[1]) ** 2)


def random():
    return np.random.random()
