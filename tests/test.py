import pytest

from simulationDriver import SimulationDriver
from environment import Environment
from player import Player
from bracket import Bracket
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def test_1():
    assert 1 + 1 == 2, "Test Passed"


def test_2():
    SimulationDriver.TOTAL_PLAYERS = 10
    x = SimulationDriver()
    x.begin()
    print(x.environment.env["players"])
    print(x.environment.env["occupied"])

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

def test_5():
    test = Bracket(7, 2)
    sum = 0
    print(str(test))
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

    print(str(sum))
