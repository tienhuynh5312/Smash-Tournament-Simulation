class Player:
    """
    Class to represent the behavior of competitors at smash tournaments
    """
    total_players = 0

    def __init__(self, player_id=0):
        Player.totalPlayers = Player.totalPlayers + 1
        self.player_id = player_id
        self.walking_distance = 0
        self.isWaiting = True
        self.isPlaying = False
        self.isRecentlyEliminated = False

    def play_around(self):
        pass

    def move_random(self):
        pass

    def isRecentlyEliminated(self):
        return self.isRecentlyEliminated

    def isWaiting(self):
        return self.isWaiting

    def isPlaying(self):
        return self.isPlaying
