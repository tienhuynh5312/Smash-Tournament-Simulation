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
        if (p1Wins == numVictory):
            return p1
        if (p2Wins == numVictory):
            return p2

        return -1

    def updateResult(self):
        return

    def getwpath(self):
        return wpath

    def getlpath(self):
        return lpath