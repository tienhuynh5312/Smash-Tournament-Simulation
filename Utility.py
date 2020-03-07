DEBUG_MODE = True


def print_debug(str_in, end="\n"):
    if DEBUG_MODE:
        print(str_in, end=end)
