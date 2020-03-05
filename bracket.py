"""
Class designed to represent the double elmination format of tournaments 
"""

from match import Match
from queue import PriorityQueue

class Bracket(object):
    # Generate Bracket
    def __init__(self, numPlayers, b05round):
        self.numPlayers = numPlayers
        self.numAlive = numPlayers
        self.numEliminated = 0

        # Round B05 starts at
        self.b05round = b05round

        # Calculate number of rounds needed
        k = 0
        while 2**(k + 1) < numPlayers:
            k = k + 1
        self.numRounds = k
        self.wExtra = numPlayers - 2**k
        j = 0
        while 2**(j + 1) < self.wExtra:
            j = j + 1
        self.lExtra = self.wExtra - 2**j
        # Determine the first round of matches
        self.nextMatches = PriorityQueue()
        self.WinnersRounds = self.generateWinnersBracket()
        self.LosersRounds = self.generateLosersBracket()

        print(self.numRounds)
        print(self.wExtra)
        print(self.lExtra)
        print(self.WinnersRounds)
        print(self.LosersRounds)

    def generateWinnersBracket(self):
        WinnersRounds = []
        for i in range(self.numRounds + 1):
            WinnersRounds.append([])

        # Create round 0 of matches
        for i in range(self.wExtra):
            p1 = self.numPlayers - i
            p2 = self.numPlayers - self.wExtra * 2 + i + 1
            wp = [1, i // 2]
            lp = [0, i // 2]
            match = [p1, p2, wp, lp]
            #match = Match(p1, p2)
            WinnersRounds[0].append(match)
            self.nextMatches.put((0, [0, i]))

        for i in range(1, self.numPlayers - self.wExtra * 2 + 1):
            p1 = i
            p2 = -1
            wp = [1, (i + self.wExtra) // 2 - 1]
            lp = [0, (i + self.wExtra) // 2 - 1]
            match = [p1, p2, wp, lp]
            #match = Match(wp, lp)
            WinnersRounds[0].append(match)
            self.nextMatches.put((0, [0, self.wExtra - 1 + i]))

        # Create rounds 1 - k of matches
        for i in range(1, self.numRounds + 1):
            for j in range(2 ** (self.numRounds - i)):
                p1 = "w" + str(i - 1) + "-" + str(2 * j)
                p2 = "w" + str(i - 1) + "-" + str(2 * j + 1)
                wp = [i + 1, j // 2]
                lp = [2 * (i -1) + 1, j]
                match = [wp, lp]
                # match = Match(wp, lp)
                WinnersRounds[i].append(match)
        return WinnersRounds

    def generateLosersBracket(self):
        LosersRounds = []
        for i in range(self.numRounds + 1):
            LosersRounds.append([])

        # Create round 0 of matches
        for i in range(self.lExtra):
            p1 = "w" + str(2 * i)
            p2 = "w" + str(2 * i + 1)
            wp = [1, i // 2]
            lp = -1
            match = [wp, lp]
            LosersRounds[0].append(match)

        for i in range(self.lExtra * 2, len(self.WinnersRounds[0]) // 2 + 1):
            p1 = "w" + str(i)
            p2 = -1
            wp = [1, i // 2]
            lp = -1
            match = [wp, lp]
            LosersRounds[0].append(match)

        for i in range(1, self.numRounds + 1):
            for j in range(2 ** (self.numRounds - i)):
                wp = [i + 1, j // 2]
                lp = -1
                if (i % 2) == 0:
                    p1 = "l" + str(i) + "-" + str(2 * j)
                    p2 = "l" + str(i) + "-" + str(2 * j + 1)
                else:
                    # Winner from previous round
                    p1 = "l" + str(i) + "-" + str(j)
                    # Loser from current round
                    p2 = "w" + str(i) + "-" + str(j)
                match = [wp, lp]
                # match = Match(wp, lp)
                LosersRounds[i].append(match)
        return LosersRounds

    def getMatch(self, type, round, matchNumber):
        return

    def reportMatch(self, type, round, matchNumber):
        return

    def isComplete(self):
        return self.numPlayers == 1
