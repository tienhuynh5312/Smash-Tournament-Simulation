import pytest

from simulationDriver import SimulationDriver
from environment import Environment
from player import Player
from bracket import Bracket
from reportingStation import ReportingStation
import numpy as np
import sys
from Utility import print_debug

np.set_printoptions(threshold=sys.maxsize)


def test_1():
    assert 1 + 1 == 2, "Test Passed"


def test_2():
    SimulationDriver.TOTAL_PLAYERS = 6
    SimulationDriver.SIM_DURATION = 2000
    x = SimulationDriver()
    visualize = True
    time = x.begin(visualize)

    print(time)


def test_3():
    x = Environment(50, 50)


def test_4():
    Player.reset()
    sim = SimulationDriver()
    x = Player(0)
    # x.set_destination((10, 10))
    # # x.walk(sim.environment)
    # # x.walk(sim.environment)
    # # x.walk(sim.environment)
    # # x.walk(sim.environment)
    # # x.walk(sim.environment)
    # # x.walk(sim.environment)
    y = Player(1)

# Test cases for the bracket Class
def test_5():
    test = Bracket(7, 2)
    sum = 0
    print(str(test))
    assert test.isOver() is False, "Test Passed"
    while (not test.nextMatches.empty()):
        matchId = test.nextMatches.get()[1]
        test.nextMatches
        print(matchId)
        match = test.getMatch(matchId)
        sum = sum + match.matchTime
        print("Match time" + str(match.matchTime))
        winner = match.getWinner()
        loser = match.getLoser()
        wp = match.getwpath()
        lp = match.getlpath()
        test.updatePlayer(wp, winner)
        test.updatePlayer(lp, loser)
    print(test.numAlive)
    assert test.isOver() is True, "Test Passed"

# Test cases for the Reporting Station Class
def test_6():
    testBracket = Bracket(7, 2)
    testOrganizer = ReportingStation(testBracket, 1, [2, 2], 5)
    assert testBracket.isOver() is False, "Test Passed"
    while (not testBracket.nextMatches.empty()):
        matchInfo = testOrganizer.callPlayers()
        isBye = matchInfo[0]
        match = matchInfo[1]
        consoleId = matchInfo[2]
        # Case where the match is a bye (no one should be called)
        testOrganizer.updateBracket(match, consoleId)

    print(testBracket.numAlive)