"""
Class representing matches in a smash tournament 
"""

class Match(object):
    def __init__(self, p1 = None, p2 = None, wpath = None, lpath = None):
        self.p1id = p1
        self.p2id = p2
        self.p1Wins = 0
        self.p2Wins = 0
        self.wpath = wpath
        self.lpath = lpath
        self.numVictory = 2

    def __str__(self):
        return "p1: " + str(self.p1id) + "-" +\
               "p2: " + str(self.p2id)

    # Returns whether or not this match can be run by the reporting station
    def canBeRun(self):
        if (self.p1id is not None) & (self.p2id is not None):
            return true
        return false

    # Returns the results of this match
    def getResult(self):
        if (self.p1Wins == self.numVictory):
            return p1
        if (self.p2Wins == self.numVictory):
            return p2

        return -1

    #Updates the result of this match
    def updateResult(self, winner):
        if winner == 1:
            self.p1Wins = self.p1Wins + 1
        if winner == 2:
            self.p2Wins = self.p2Wins + 1

    def getwpath(self):
        return wpath

    def getlpath(self):
        return lpath