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
        self.currentMatch = None
        self.currentP1 = None
        self.currentP2 = None
        self.currentConsole = None

    # sets the amount of time that the reporting station is occupied for
    def set_busy_time(self, busy_time=0):
        self.busy_time = busy_time
        print_debug(f"set Reporting Station {self.Stationid} busy for {self.busy_time}")

    # Method that checks whether the reporting station can perform other action
    def is_busy(self, duration=1, env=None):
        self.busy_time = self.busy_time - duration
        if self.isWaiting:
            print_debug(f"Reporting Station{self.Stationid} is waiting for players still")
        elif self.busy_time > 0:
            print_debug(f"Reporting Station{self.Stationid} is talking to someone right now")
        else:
            if env is not None:
                env.set_occupied(self.current_location, "organizers")
            print_debug(f"Player {self.Stationid} is free")
        return self.busy_time > 0

    # Returns the player ids of the match that needs to be played and the console
    # that the match should be played at
    def callPlayers(self):
        # Checks to see if console + match is available
        openConsoles = np.where(self.consoles == True)[0]
        if (not self.bracket.nextMatches.empty()) & (len(openConsoles) > 0):
            self.isWaiting = True
            matchIndex = self.bracket.nextMatches.get()[1]
            matchInfo = self.bracket.getMatch(matchIndex)
            console = openConsoles[0]
            self.consoles[console] = False
            self.currentConsole = console
            self.currentP1 = matchInfo.p1id
            self.currentP2 = matchInfo.p2id
            if (matchInfo.p2id == -1) | (matchInfo.p2id == -1):
                return(True, matchInfo, console)
            else:
                print("Wow match can be played")
                return(False, matchInfo, console)


    # Accepts the result of a match and updates the
    # bracket and the console status
    def updateBracket(self, match, consoleId):
        self.set_busy_time(30)
        winner = match.getWinner()
        loser = match.getLoser()
        wp = match.getwpath()
        lp = match.getlpath()

        # Update the winner of the match
        self.bracket.updatePlayer(wp, winner)

        # Update the loser of the match
        self.bracket.updatePlayer(lp, loser)
        self.consoles[consoleId] = True

    def receivePlayer(self, playerID):
        if self.currentP1 == playerID:
            self.currentP1 = None
        if self.currentP2 == playerID:
            self.currentP2 = None
        if (self.currentP1 is None) & (self.currentP2 is None):
            self.isWaiting = False
        return [self.currentMatch, self.currentConsole]



