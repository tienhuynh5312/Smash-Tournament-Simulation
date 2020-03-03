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
        i = 0
        while (2 ^ (i) < numPlayers):
            i = i + 1
        self.numRounds = i

        # Determine the first round of matches
        round1W = []
        for i in range(numPLayers - 2^i):
            match = [numPLayers - i + 1, 2^i]
            round1W.append(match)

        round2W = []
        WinnersMatches = []
        LosersMatches = []
        # How do you determine if people should be given a bye?
        # How do you link matches to different indices?