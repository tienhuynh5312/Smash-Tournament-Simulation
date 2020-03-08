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
        self.GrandFinals = self.__generateGrandsBracket()
        self.WinnersRounds = self.__generateWinnersBracket()
        self.LosersRounds = self.__generateLosersBracket()

    # --------------------------Public Methods -----------------------
    def __str__(self):
        string = "Winners Matches:\n"
        for i in range(len(self.WinnersRounds)):
            for j in range(len(self.WinnersRounds[i])):
                string = string + "[" + str(i) + ", " + str(j) + "]" + str(self.WinnersRounds[i][j]) + "\n"
        string = string + "Losers Matches:\n"
        for i in range(len(self.LosersRounds)):
            for j in range(len(self.LosersRounds[i])):
                string = string + "[" + str(i) + ", " + str(j) + "]" + str(self.LosersRounds[i][j]) + "\n"
        string = string + "Finals:\n"
        for i in self.GrandFinals:
             string = string + str(i) + "\n"
        return string

    def getMatch(self, matchInfo):
        type = matchInfo[0]
        round = matchInfo[1]
        matchNumber = matchInfo[2]

        if (type == 0):
            return self.WinnersRounds[round][matchNumber]
        elif (type == 1):
            return self.LosersRounds[round][matchNumber]

    def updatePlayer(self, matchInfo, player):
        if matchInfo == -1:
            self.numAlive = self.numAlive - 1
            self.numEliminated = self.numEliminated + 1
        else:
            type = matchInfo[0]
            round = matchInfo[1]
            matchNumber = matchInfo[2]

            if (type == 0):
                match = self.WinnersRounds[round][matchNumber]
            elif (type == 1):
                match = self.LosersRounds[round][matchNumber]
            elif (type == 2):
                match = self.GrandFinals[matchNumber]
            match.addPlayer(player)
            if(match.canBeRun()):
                self.nextMatches.put((round, matchInfo))


    def isComplete(self):
        return self.numPlayers == 1

    # ------------------------ Private Methods -------------------
    def __generateWinnersBracket(self):
        WinnersRounds = []
        for i in range(self.numRounds + 1):
            WinnersRounds.append([])

        # Create round 0 of matches
        for i in range(self.wExtra):
            p1 = self.numPlayers - i
            p2 = self.numPlayers - self.wExtra * 2 + i + 1
            wp = [0, 1, i // 2]
            lp = [1, 0, i // 2]
            match = Match(wp, lp, p1, p2)
            WinnersRounds[0].append(match)
            self.nextMatches.put((0, [0, 0, i]))

        for i in range(1, self.numPlayers - self.wExtra * 2 + 1):
            p1 = i
            p2 = -1
            wp = [0, 1, (i + self.wExtra) // 2 - 1]
            lp = [1, 0, (i + self.wExtra) // 2 - 1]
            match = Match(wp, lp, p1, p2)
            WinnersRounds[0].append(match)
            self.nextMatches.put((0, [0, 0, self.wExtra - 1 + i]))

        # Create rounds 1 - k of matches
        for i in range(1, self.numRounds + 1):
            for j in range(2 ** (self.numRounds - i)):
                wp = [0, i + 1, j // 2]
                lp = [1, 2 * (i -1) + 1, j]
                if (i == self.numRounds):
                    wp = [2, i + 1, j // 2]
                    lp = [2, i + 1, j // 2]
                match = Match(wp, lp)
                WinnersRounds[i].append(match)
        return WinnersRounds

    def __generateLosersBracket(self):
        LosersRounds = []
        for i in range(self.numRounds + 1):
            LosersRounds.append([])

        # Create round 0 of matches
        for i in range(self.lExtra):
            p1 = "w" + str(2 * i)
            p2 = "w" + str(2 * i + 1)
            wp = [1, 1, i // 2]
            lp = -1
            match = Match(wp, lp)
            LosersRounds[0].append(match)

        for i in range(self.lExtra * 2, len(self.WinnersRounds[0]) // 2 + 1):
            p1 = "w" + str(i)
            p2 = -1
            wp = [1, 1, i // 2]
            lp = -1
            match = Match(wp, lp)
            LosersRounds[0].append(match)

        # Generate the remaining losers matches
        for i in range(1, self.numRounds + 1):
            for j in range(2 ** (self.numRounds - i)):
                wp = [1, i + 1, j // 2]
                lp = -1
                if (i % 2) == 0:
                    p1 = "l" + str(i) + "-" + str(2 * j)
                    p2 = "l" + str(i) + "-" + str(2 * j + 1)
                else:
                    # Winner from previous round
                    p1 = "l" + str(i) + "-" + str(j)
                    # Loser from current round
                    p2 = "w" + str(i) + "-" + str(j)
                match = Match(wp, lp)
                # match = Match(wp, lp)
                LosersRounds[i].append(match)
        return LosersRounds

    def __generateGrandsBracket(self):
        grandsBracket = []
        #Add Grand finals
        match = Match(-1, -1)
        grandsBracket.append(match)
        return grandsBracket

test = Bracket(7, 2)
print(str(test))

