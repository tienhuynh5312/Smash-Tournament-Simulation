from Utility import *


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
        self.current_location = None
        self.destination_location = None
        self.playTime = 0
        self.match = None
        self.to_organizer = 1
        self.after_match = False
        self.bias = 0

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

    def set_busy_time(self, busy_time):
        self.busy_time = busy_time
        print_debug(f"set player {self.player_id} busy for {self.busy_time}")

    def is_busy(self, duration=1, env=None):
        self.busy_time = self.busy_time - duration
        if self.busy_time > 0:
            print_debug(f"Player {self.player_id} is busy/bathroom/late")
        else:
            if env is not None:
                env.set_occupied(self.current_location, "players")

            # if self.is_playing:
            #     self.after_match = True
            #     self.is_playing = False

            print_debug(f"Player {self.player_id} is free")
        return self.busy_time > 0

    def take_break(self, env=None):
        print_debug(f"Player {self.player_id} needs to take break")
        if self.is_busy(duration=0):
            print_debug(f"  is busy. skip")
        else:
            from simulationDriver import SimulationDriver
            import numpy as np
            print_debug(f"  take the break")
            self.walking_distance = (SimulationDriver.BATHROOM_DISTANCE + distance(self.current_location, (0, 0))) * 2
            self.set_busy_time(np.random.normal(3 * 60, 1 * 60))
            if env is not None:
                env.remove_occupied(self.current_location, "players")

    def is_here(self, radius=1, to_door=False):
        from simulationDriver import SimulationDriver

        if self.destination_location is None:
            print_debug(f"No destination specified. Stay here {self.current_location}")
            return True

        distance_row = self.destination_location[0] - self.current_location[0]
        distance_col = self.destination_location[1] - self.current_location[1]

        # if self.destination_locations[self.destination_index][0] < SimulationDriver.WALL_ROW <= \
        #         self.current_location[0]:
        #     print_debug(f"Switching area. Need to go through door.")
        #     if abs(distance_row) == 0 and abs(distance_col) == 0:
        #         if len(self.destination_locations) - 1 > self.destination_index:
        #             self.destination_index = self.destination_index + 1
        #         return True
        if to_door:
            if abs(distance_row) <= 0 and abs(distance_col) <= 2:
                self.destination_location = None
                return True
        else:
            if abs(distance_row) <= radius and abs(distance_col) <= radius:
                self.destination_location = None
                return True

        return False

    def walk(self, env):
        from simulationDriver import SimulationDriver
        import numpy as np

        def walk2door():
            a = self.current_location[0] - SimulationDriver.WALL_ROW
            b = self.destination_location[0] - SimulationDriver.WALL_ROW
            if a*b < 0:
                print_debug("Switching area. Need to go to door")
                return True
            else:
                return False

        def get_closest_door():
            index = 0
            min_distance = 9999999999
            for loc in range(len(SimulationDriver.DOOR_LOCATIONS)):
                dis = distance(SimulationDriver.DOOR_LOCATIONS[loc], self.current_location)

                if dis < min_distance:
                    index = loc

            return loc

        def get_new_location(bias=(0, 0), to_door=False):
            if to_door:
                which_door = get_closest_door()
                print(f"this door = {which_door}")
                door = SimulationDriver.DOOR_LOCATIONS[which_door]
                direction_vector = (door[0] - self.current_location[0],
                                    door[1] - self.current_location[1])
            else:
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

            # bias walk
            direction_choice = np.random.random()

            row_location = self.current_location[0] + bias[0]
            col_location = self.current_location[1] + bias[1]

            if direction_choice < 0.5 + self.bias:
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

            if row_location < 0:
                row_location = 0
            elif row_location > SimulationDriver.ALL_AREA_ROWS - 1:
                row_location = SimulationDriver.ALL_AREA_ROWS - 1

            if col_location < 0:
                col_location = 0
            elif col_location > SimulationDriver.ALL_AREA_COLS - 1:
                col_location = SimulationDriver.ALL_AREA_COLS - 1

            return row_location, col_location

        def is_out_of_bound(row, col):
            if row < 0 or row > SimulationDriver.ALL_AREA_ROWS - 1:
                return True

            if col < 0 or col > SimulationDriver.ALL_AREA_COLS - 1:
                return True

            return False

        def get_bias(location):
            row_bias = location[0]-self.current_location[0]
            col_bias = location[1]-self.current_location[1]
            if row_bias != 0:
                return -0.25
            elif col_bias != 0:
                return 0.25
            else:
                return 0

        if self.destination_location is None:
            self.move_random()

        if random() < SimulationDriver.PLAYER_BATHROOM_PERCENT:
            self.take_break()

        if self.after_match:
            # walking method after a match
            if self.to_organizer < 0:  # to waiting area
                location = get_random_location_waiting_area(env)
                self.set_destination(location)
            elif self.to_organizer >= 0:  # to organizer
                self.set_destination(SimulationDriver.ORGANIZER_LOCATIONS[self.to_organizer])
            self.after_match = False

        # - make the player walk toward the destination location
        for i in range(SimulationDriver.TIME_STEP):
            if self.is_busy(env=env):
                print_debug(f"Can't walk.")
                continue

            if self.is_here():
                print_debug(f"player id {self.player_id} is here at {self.destination_location}")
                if self.playTime > 0:
                    self.set_busy_time(self.playTime)  # assign play time
                    self.playTime = 0  # reset after assignment.
                break

            try_timeout = 1
            new_row_location, new_col_location = get_new_location(to_door=walk2door())
            while env.env["occupied"][(new_row_location, new_col_location)] > 0:
                try_timeout = try_timeout - 1
                self.bias = get_bias((new_row_location, new_col_location))
                if try_timeout < 0:
                    print_debug(
                        f"Cannot find a way {new_row_location, new_col_location}. Wait here {self.current_location}->{self.destination_location}")
                    break

                new_row_location, new_col_location = get_new_location(to_door=walk2door())

            if try_timeout > -1:
                env.move_occupied(self.current_location, (new_row_location, new_col_location), "players")
                self.current_location = (new_row_location, new_col_location)
                print_debug(self.current_location)
                self.walking_distance = self.walking_distance + 1
                env.update()

    def set_destination(self, location_tuple):
        self.destination_location = location_tuple

    def is_eliminated(self):
        if self.is_recently_eliminated:
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

    # Sets the match location of the
    def set_match(self, match, consoleLocation):
        self.set_destination(consoleLocation)
        self.match = match
        self.playTime = match.matchTime
        self.is_playing = True

    def report_match(self, OrganizerLocation):
        # Walk to the organizer
        self.set_destination(OrganizerLocation)
