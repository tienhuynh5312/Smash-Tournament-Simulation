"""
Class representing matches in a smash tournament 
"""

class Match(object):
    def __init__(self, p1, p2, wpath, lpath):
        player1 = p1
        player2 = p2
        p1Wins = 0
        p2Wins = 0
        numVictory = 2


    def getResult(self):
        if (self.p1Wins == self.numVictory):
            return p1
        if (self.p2Wins == self.numVictory):
            return p2

        return -1

    def updateResult(self, winner):
        if winner == 1:
            self.p1Wins = self.p1Wins + 1
        if winner == 2:
            self.p2Wins = self.p2Wins + 1

    def getwpath(self):
        return wpath

    def getlpath(self):
        return lpath