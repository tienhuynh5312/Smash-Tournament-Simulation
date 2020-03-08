from Utility import print_debug, distance, random


class Player:
    """
    Class to represent the behavior of competitors at smash tournaments
    """
    total_players = 0
    total_eliminated_players = 0

    @staticmethod
    def reset():
        Player.total_players = 0
        Player.total_eliminated_players = 0

    def __init__(self, player_id=0):
        from simulationDriver import SimulationDriver
        self.play_around_time = 0
        Player.total_players = Player.total_players + 1
        self.player_id = player_id
        self.walking_distance = 0
        self.is_waiting = True
        self.is_playing = False
        self.is_recently_eliminated = False
        self.busy_time = 0
        self.set_busy_time(Player.init_showup_late_time(SimulationDriver.PLAYER_SHOW_UP_LATE_PERCENT))  # seconds
        self.current_location = (0, 0)
        self.destination_location = None

    def __del__(self):
        Player.total_players = Player.total_players - 1
        Player.total_eliminated_players = Player.total_eliminated_players - 1

    @staticmethod
    def init_showup_late_time(chance):
        import numpy as np
        is_late = np.random.random()
        if is_late < chance:
            print_debug("A player will show up late")
            return np.random.normal(5 * 60, 2 * 60)
        else:
            return 0

    def set_busy_time(self, busy_time=0):
        self.busy_time = busy_time
        print_debug(f"set player {self.player_id} busy for {self.busy_time}")

    def is_busy(self, duration=1):
        self.busy_time = self.busy_time - duration
        if self.busy_time > 0:
            print_debug(f"Player {self.player_id} is busy/bathroom/late")
        else:
            print_debug(f"Player {self.player_id} is free")
        return self.busy_time > 0

    def take_break(self):
        print_debug(f"Player {self.player_id} needs to take break")
        if self.is_busy(duration=0):
            print_debug(f"  is busy. skip")
        else:
            from simulationDriver import SimulationDriver
            import numpy as np
            print_debug(f"  take the break")
            self.walking_distance = (SimulationDriver.BATHROOM_DISTANCE + distance(self.current_location, (0, 0))) * 2
            self.set_busy_time(np.random.normal(3 * 60, 1 * 60))

    def is_here(self, radius=1):
        distance_row = self.destination_location[0] - self.current_location[0]
        distance_col = self.destination_location[1] - self.current_location[1]
        if abs(distance_row) <= radius and abs(distance_col) <= radius:
            return True

        return False

    def walk(self, env):
        from simulationDriver import SimulationDriver
        import numpy as np

        def get_new_location(bias=(0, 0)):
            direction_vector = (self.destination_location[0] - self.current_location[0],
                                self.destination_location[1] - self.current_location[1])

            if direction_vector[0] > 0:
                go_south = True
            else:
                go_south = False

            if direction_vector[1] > 0:
                go_east = True
            else:
                go_east = False

            # random walk
            direction_choice = np.random.random()
            row_location = self.current_location[0]+bias[0]
            col_location = self.current_location[1]+bias[1]
            if direction_choice < 0.5:
                # go vertical
                if go_south:
                    row_location = row_location + 1
                else:
                    row_location = row_location - 1
            else:
                # go horizontal
                if go_east:
                    col_location = col_location + 1
                else:
                    col_location = col_location - 1

            return row_location, col_location

        def is_out_of_bound(row, col):
            if row < 0 or row > SimulationDriver.ALL_AREA_ROWS - 1:
                return True

            if col < 0 or col > SimulationDriver.ALL_AREA_COLS - 1:
                return True

            return False

        if random() < SimulationDriver.PLAYER_BATHROOM_PERCENT:
            self.take_break()

        # - make the player walk toward the destination location
        for i in range(SimulationDriver.TIME_STEP):
            if self.is_busy():
                print_debug(f"Can't walk.")
                continue

            if self.is_here():
                print_debug(f"player id {self.player_id} is here at {self.destination_location}")
                break

            try_timeout = 4
            new_row_location, new_col_location = get_new_location()
            while is_out_of_bound(new_row_location, new_col_location):
                try_timeout = try_timeout - 1
                if try_timeout == -1:
                    print_debug(f"Cannot find a way {new_row_location, new_col_location}. Wait here {self.current_location}")
                    id= env.env["occupied"][(new_row_location, new_col_location)]
                    print_debug(f"{id}")
                    break
                new_row_location, new_col_location = get_new_location()
                if env.env["occupied"][(new_row_location, new_col_location)] == 1:
                    print_debug("New location is occupied. Try a different one")
                    continue

            if try_timeout > -1:
                env.move_occupied(self.current_location, (new_row_location, new_col_location), "players")

                self.current_location = (new_row_location, new_col_location)
                print_debug(self.current_location)
                self.walking_distance = self.walking_distance + 1

    def set_destination(self, location_tuple=(0, 0)):
        self.destination_location = location_tuple

    def is_eliminated(self):
        if not self.is_playing:
            return True
        else:
            return False

    def eliminated(self):
        Player.total_eliminated_players = Player.total_eliminated_players + 1
        self.is_playing = False
        self.is_waiting = False
        self.is_recently_eliminated = True

    def move_random(self):
        if self.is_busy():
            print_debug(f"Can't move.")
            pass
        pass

    def play_around(self):
        if self.is_busy():
            print_debug(f"Can't hang out.")
            pass

        import numpy as np
        if self.is_recently_eliminated:
            # -  If recently eliminated, give the player random time to stick around
            self.play_around_time = np.random.normal(30 * 60, 10 * 60)  # - 30 mins * 60 seconds. std 10
        else:
            # - now let the player move around for fun.
            pass
