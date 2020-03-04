class Player:
    """
    Class to represent the behavior of competitors at smash tournaments
    """
    total_players = 0
    total_eliminated_players = 0

    def __init__(self, player_id=0):
        self.play_around_time = 0
        Player.total_players = Player.total_players + 1
        self.player_id = player_id
        self.walking_distance = 0
        self.isWaiting = True
        self.isPlaying = False
        self.isRecentlyEliminated = False
        self.current_location = (0, 0)
        self.destination_location = (0, 0)

    def walk(self):
        # - make the player walk toward the destination location
        pass

    def set_destination(self, location_tuple=(0, 0)):
        self.destination_location = location_tuple

    def eliminated(self):
        Player.total_eliminated_players = Player.total_eliminated_players + 1
        self.isPlaying = False
        self.isWaiting = False
        self.isRecentlyEliminated = True

    def move_random(self):
        pass

    def play_around(self):
        import numpy as N
        if self.isRecentlyEliminated:
            # -  If recently eliminated, give the player random time to stick around
            self.play_around_time = N.random.normal(30, 10)
        else:
            # - now let the player move around for fun.
            pass

    def isWaiting(self):
        return self.isWaiting

    def isPlaying(self):
        return self.isPlaying
