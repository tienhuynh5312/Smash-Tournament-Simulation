"""
Class which represents the reporting station at a tournament
reporting stations have a location which does not change
reporting stations direct players to play there matches
and update the bracket 
"""

from Utility import print_debug, distance, random
import numpy as np

class ReportingStation:
    def __init__(self, bracket, id, location, numConsoles):
        self.bracket = bracket
        self.Stationid = id
        self.current_location = location
        self.consoles = np.ones(numConsoles, dtype = bool)
        self.busy_time = 0
        self.destination_location = None
        self.isWaiting = False
        self.numWaiting = 0

    def set_busy_time(self, busy_time=0):
        self.busy_time = busy_time
        print_debug(f"set Reporting Station {self.Stationid} busy for {self.busy_time}")

    def is_busy(self, duration=1, env=None):
        self.busy_time = self.busy_time - duration
        if self.isWaiting:
            print_debug(f"Reporting Station{self.Stationid} is waiting for players still")
        elif self.busy_time > 0:
            print_debug(f"Reporting Station{self.Stationid} is talking to someone right now")
        else:
            if env is not None:
                env.set_occupied(self.current_location, "players")
            print_debug(f"Player {self.Stationid} is free")
        return self.busy_time > 0

    # Returns the player ids of the match that needs to be played and the console
    # that the match should be played at
    def callPlayers(self):
        # Checks to see if console + match is available
        openConsoles = np.where(self.consoles == True)[0]
        if (not self.bracket.nextMatches.empty()) & (len(openConsoles) > 0):
            matchInfo = self.bracket.getMatch()
            console = openConsoles[0]
            self.consoles[console] = False
            print("Wow match can be played")
            return(matchInfo, console)

    # Accepts the result of a match and updates the
    # bracket and the console status
    def updateBracket(self, matchId, consoleId):
        self.set_busy_time(30)
        matchInfo = self.bracket.getMatch(matchId)
        winner = matchInfo.getWinner()
        loser = matchInfo.getLoser()
        wp = matchInfo.getwpath()
        lp = matchInfo.getlpath()

        # Update the winner of the match
        self.bracket.updatePlayer(wp, winner)

        # Update the loser of the match
        self.bracket.updatePlayer(lp, loser)
        self.consoles[consoleId] = True

    def receivePlayer(self, playerID):
        return 1


