import pytest

from simulationDriver import SimulationDriver
from environment import Environment
from player import Player
from bracket import Bracket

def test_1():
    assert 1 + 1 == 2, "Test Passed"


def test_2():
    SimulationDriver.TOTAL_PLAYERS = 30
    x = SimulationDriver()
    assert x.time_stamp == 0, "Time stamp = 0"
    x.begin()
    assert x.time_stamp == 4, "Time stamp = 5"
    assert x.total_initial_players == 30, "Initial Players = 30"
    assert x.players_list[0].player_id == 0
    assert x.players_list[15].player_id == 15
    assert x.players_list[29].player_id == 29


def test_3():
    x = Environment(30, 30)
    assert x.env["occupied"].shape == (30,30)
    assert x.env["organizers"].shape == (30, 30)
    assert x.env["consoles"].shape == (30, 30)
    assert x.env["players"].shape == (30, 30)


def test_4():
    Player.reset()
    assert Player.total_eliminated_players == 0
    assert Player.total_players == 0
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
    assert Player.total_players == 32

def test_5():
    pass
    test = Bracket(7, 2)

    # while (test.nextMatches):
    #     matchId = test.nextMatches.get()[1]
    #     print(matchId)
    #     match = test.getMatch(matchId)
    #     print(match)
    #     match.updateResult(1)
    #     winner = match.getWinner()
    #     loser = match.getLoser()
    #     wp = match.getwpath()
    #     lp = match.getlpath()
    #     print(wp)
    #     print(lp)
    #     test.updatePlayer(wp, winner)