
class Console(object):
    def __init__(self, location, orientation):
        self.location = location
        self.chair1 = [location[0] + 1, location[1]]
        self.chari2 = [location[0] - 1, location[1]]
        self.player1 = None
        self.player2 = None

    def isOccupied(self):
        return (self.player1 is not None) and (self.player2 is not None)
