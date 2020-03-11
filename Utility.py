import numpy as np
DEBUG_MODE = True


def print_debug(str_in, end="\n"):
    if DEBUG_MODE:
        print(str_in, end=end)


def distance(location_a, location_b):
    import math
    return math.sqrt((location_a[0] - location_b[0]) ** 2 + (location_a[1] - location_b[1]) ** 2)


def random():
    return np.random.random()


def get_random_location_waiting_area(env):
    from simulationDriver import SimulationDriver

    row_min = SimulationDriver.WALL_ROW + 1
    row_max = SimulationDriver.ALL_AREA_ROWS
    col_min = 0
    col_max = SimulationDriver.ALL_AREA_COLS

    random_location_row = np.random.randint(row_min, row_max)
    random_location_col = np.random.randint(col_min, col_max)
    random_location = (random_location_row, random_location_col)

    # if there is something occupied at random_location, generate another one.
    while env.env["occupied"][random_location] == 1:
        random_location_row = np.random.randint(row_min, row_max)
        random_location_col = np.random.randint(col_min, col_max)
        random_location = (random_location_row, random_location_col)

    return random_location
