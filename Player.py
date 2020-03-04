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
        # - make the player walk toward the destination location
        steps = SimulationDriver.TIME_STEP
        direction_vector = (self.destination_location[0] - self.current_location[0],
                            self.destination_location[1] - self.current_location[1])

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
