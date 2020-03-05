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
        self.play_around_time = 0
        Player.total_players = Player.total_players + 1
        self.player_id = player_id
        self.walking_distance = 0
        self.is_waiting = True
        self.is_playing = False
        self.is_recently_eliminated = False
        self.current_location = (0, 0)
        self.destination_location = (0, 0)

    def __del__(self):
        Player.total_players = Player.total_players - 1
        Player.total_eliminated_players = Player.total_eliminated_players - 1

    def walk(self, env=None):
        from simulationDriver import SimulationDriver
        import numpy as np

        def get_new_location():
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
            row_location = self.current_location[0]
            col_location = self.current_location[1]
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

            if self.current_location[0] + 1 == self.destination_location[0] or \
                    self.current_location[0] - 1 == self.destination_location[0]:
                row_location = self.destination_location[0]
            elif self.current_location[1] + 1 == self.destination_location[1] or \
                    self.current_location[1] - 1 == self.destination_location[1]:
                col_location = self.destination_location[1]

            return row_location, col_location

        def is_out_of_bound(row, col):

            if row < 0 or row > SimulationDriver.ALL_AREA_ROWS - 1:
                return True

            if col < 0 or col > SimulationDriver.ALL_AREA_COLS - 1:
                return True

            return False

        # - make the player walk toward the destination location
        for i in range(SimulationDriver.TIME_STEP):
            if self.current_location == self.destination_location:
                continue

            new_row_location, new_col_location = get_new_location()
            while is_out_of_bound(new_col_location, new_row_location):
                new_row_location, new_col_location = get_new_location()

            if env is not None:
                env.move_occupied(self.currentLocation, (new_row_location, new_col_location))

            self.current_location = (new_row_location, new_col_location)
            print(self.current_location)
            self.walking_distance = self.walking_distance + 1

    def set_destination(self, location_tuple=(0, 0)):
        self.destination_location = location_tuple

    def eliminated(self):
        Player.total_eliminated_players = Player.total_eliminated_players + 1
        self.is_playing = False
        self.is_waiting = False
        self.is_recently_eliminated = True

    def move_random(self):
        pass

    def play_around(self):
        import numpy as np
        if self.is_recently_eliminated:
            # -  If recently eliminated, give the player random time to stick around
            self.play_around_time = np.random.normal(30, 10)  # - 30 mins * 60 seconds. std 10
        else:
            # - now let the player move around for fun.
            pass
