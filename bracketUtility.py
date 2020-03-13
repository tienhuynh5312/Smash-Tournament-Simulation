from bracket import Bracket
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

class delayedUpdate:
    def __init__(self, startTime, timeToWait, winner, loser, wp, lp):
        self.startTime = startTime
        self.timeToWait = timeToWait
        self.winner = winner
        self.loser = loser
        self.wp = wp
        self.lp = lp

    def readytoCall(self, currTime):
        return currTime > (self.startTime + self.timeToWait)

    def getWinnerData(self):
        return ([self.wp, self.winner])

    def getLoserData(self):
        return ([self.lp, self.loser])

def runBracket(numPlayers, numConsoles, timeoutMode):
    # Time is measured in seconds
    totalTime = 0
    CurrOpen = numConsoles
    ongoingMatches = []

    # Creates a bracket
    test = Bracket(numPlayers, 2)
    #
    while (not test.isOver()):
        totalTime = totalTime + 1

        if (CurrOpen) > 0 and not (test.nextMatches.empty()):
            matchId = test.nextMatches.get()[1]
            test.nextMatches
            #Marks a setup as taken
            CurrOpen = CurrOpen - 1
            match = test.getMatch(matchId)
            winner = match.getWinner()
            loser = match.getLoser()
            wp = match.getwpath()
            lp = match.getlpath()

            # Deals with byes
            if (winner == -1) or (loser == -1):
                test.updatePlayer(wp, winner)
                test.updatePlayer(lp, loser)
                CurrOpen = CurrOpen + 1

            else:
                currMatch = delayedUpdate(totalTime, match.matchTime, winner, loser, wp, lp)
                if (winner == 1) and (timeoutMode):
                    currMatch = delayedUpdate(totalTime, 3 * 7 * 60 + 5, winner, loser, wp, lp)
                ongoingMatches.append(currMatch)

        for ongoingMatch in ongoingMatches:
            if ongoingMatch.readytoCall(totalTime):
                ongoingMatches.remove(ongoingMatch)
                CurrOpen = CurrOpen + 1
                wData = ongoingMatch.getWinnerData()
                lData = ongoingMatch.getLoserData()
                test.updatePlayer(wData[0], wData[1])
                test.updatePlayer(lData[0], lData[1])

    #print(str(totalTime / 3600) + " hours")
    return (totalTime / 3600)

