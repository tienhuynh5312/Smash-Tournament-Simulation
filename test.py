import pytest

from simulationDriver import SimulationDriver
from environment import Environment
from Player import Player
from bracket import Bracket
from reportingStation import ReportingStation
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


def test_1():
    assert 1 + 1 == 2, "Test Passed"


def test_2():
    SimulationDriver.TOTAL_PLAYERS = 100
    SimulationDriver.SIM_DURATION = 200
    visualize = True
    x = SimulationDriver()
    x.begin(visualize)


def test_3():
    x = Environment(30, 30)


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
        sum = sum + match.generateTime()
        winner = match.getWinner()
        loser = match.getLoser()
        wp = match.getwpath()
        lp = match.getlpath()
        test.updatePlayer(wp, winner)
        test.updatePlayer(lp, loser)
    print(test.numAlive)
    # assert test.isOver() is True, "Test Passed"

# Test cases for the Reporting Station Class
def test_6():
    testBracket = Bracket(7, 2)
    testOrganizer = ReportingStation(testBracket, 1, [2, 2], 5)
    match = testOrganizer.callPlayers()
    time = match[1].generateTime()
    print(time)
    testOrganizer.updateBracket(match[1], match[2])

