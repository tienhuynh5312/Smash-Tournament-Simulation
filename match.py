"""
Class representing matches in a smash tournament 
"""
import numpy as np

class Match(object):
    def __init__(self,wpath = None, lpath = None, p1 = None, p2 = None, isB05 = False):
        self.p1id = p1
        self.p2id = p2
        self.p1Wins = 0
        self.p2Wins = 0
        self.wpath = wpath
        self.lpath = lpath
        self.numVictory = 2
        if isB05:
            self.numVictory = 3

    # --------------------------Public Methods -----------------------

    # To String method
    def __str__(self):
        return "p1: " + str(self.p1id) + "-" +\
               "p2: " + str(self.p2id) + "-" +\
                "wp: " + str(self.wpath) + "-" +\
                "lp:" + str(self.lpath) + "-"

    # Returns whether or not this match can be run by the reporting station
    def canBeRun(self):
        if (self.p1id is not None) & (self.p2id is not None):
            return True
        return False

    # Returns whether or not the match is complete
    def isComplete(self):
        return self.p1Wins == self.numVictory | self.p2Wins == self.numVictory

    # Adds a player
    def addPlayer(self, player):
        if self.p1id is None:
            self.p1id = player
        elif self.p2id is None:
            self.p2id = player

    # Returns the results of this match
    def getWinner(self):
        if (self.p1Wins == self.numVictory):
            return self.p1id
        if (self.p2Wins == self.numVictory):
            return self.p2id

    # Returns the loser of this match
    def getLoser(self):
        if (self.p1Wins == self.numVictory):
            return self.p2id
        if (self.p2Wins == self.numVictory):
            return self.p1id

    # Returns the indices of the match the winner will be playing next
    def getwpath(self):
        return self.wpath

    # Returns the indices of the match the loser will be playing next
    # Returns -1 if the player is now eliminated
    def getlpath(self):
        return self.lpath

    # TODO: Make time measurements accurate

    # Returns the amount of time the match takes
    def generateTime(self):
        sum = 0
        # Checking for controls
        if np.random.uniform(0, 1) < .5:
            sum += 20
        # Setup Controls
        if np.random.uniform(0, 1) < .5:
            sum += 30
        if np.random.uniform(0, 1) < .5:
            sum += 30
        timeTalking = np.random.binomial(4, .5)
        sum += timeTalking
        # The amount of time playing the games took
        while not self.isComplete():
            sum += self.__playMatch()
        # Packing up controllers
        controllerTime = np.random.binomial(4, .5)
        sum = sum + controllerTime

    # ------------------------ Private Methods ----------------------

    # Plays a single match
    # Updates the result of the match
    # Returns the amount of time the match took
    def __playMatch(self):
        matchTime = np.random.binomial(4, .5)
        if np.random.uniform(0, 1) < .5:
            self.updateResult(1)
        else:
            self.updateResult(2)
        return matchTime

    # Updates the result of this match
    def __updateResult(self, winner):
        if winner == 1:
            self.p1Wins = self.p1Wins + 1
        if winner == 2:
            self.p2Wins = self.p2Wins + 1
