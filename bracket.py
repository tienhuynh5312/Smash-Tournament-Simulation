"""
Class designed to represent the double elmination format of tournaments 
"""

class Bracket(object):
    # Generate Bracket
    def __init__(self, numPlayers, b05round):
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
        WinnersRounds = []
        LosersRounds = []
        for i in range(self.numRounds + 1):
            WinnersRounds.append([])
            LosersRounds.append([])

        # Create round 0 of matches
        for i in range(self.wExtra):
            match = [numPlayers - i, numPlayers - self.wExtra * 2 + i + 1]
            WinnersRounds[0].append(match)

        for i in range(1, numPlayers - self.wExtra * 2 + 1):
            match = [i, -1]
            WinnersRounds[0].append(match)

        # Create rounds 1 - k of matches
        for i in range(1, self.numRounds + 1):
            for j in range(2 ** (self.numRounds - i)):
                p1 = "w" + str(i - 1) + "-" + str(2 * j)
                p2 = "w" + str(i - 1) + "-" + str(2 * j + 1)
                WinnersRounds[i].append([p1, p2])

        # Create round 0 of matches
        for i in range(self.lExtra):
            p1 = "w" + str(2 * i)
            p2 = "w" + str(2 * i + 1)
            LosersRounds[0].append([p1, p2])

        for i in range(self.lExtra * 2, len(WinnersRounds[0]) // 2 + 1):
            match = ["w" + str(i), -1]
            LosersRounds[0].append(match)

        for i in range(1, self.numRounds + 1):
            for j in range(2 ** (self.numRounds - i)):
                if (i % 2) == 0:
                    p1 = "l" + str(i) + "-" + str(2 * j)
                    p2 = "l" + str(i) + "-" + str(2 * j + 1)
                else:
                    # Winner from previous round
                    p1 = "l" + str(i) + "-" + str(j)
                    # Loser from current round
                    p2 = "w" + str(i) + "-" + str(j)
                LosersRounds[i].append([p1, p2])

        # How do you determine if people should be given a bye?
        # How do you link matches to different indices?
        print(self.numRounds)
        print(self.wExtra)
        print(self.lExtra)
        print(WinnersRounds)
        print(LosersRounds)

    def generateWinnersBracket(self):
        return
    def generateLosersBracket(self):
        return
    def getMatch(self):
        return

    def reportMatch(self):
        return

    def isComplete(self):
        return self.numPlayers == 1

Bracket(16, 2)