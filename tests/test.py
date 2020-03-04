import pytest

from simulationDriver import *
from environment import *


def test_1():
    assert 1 + 1 == 2, "Test Passed"


def test_2():
    x = SimulationDriver()
    assert x.time_stamp == 0, "Time stamp = 0"
    x.begin()
    assert x.time_stamp == SimulationDriver.TIME_STEP, "Time stamp = 5"
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
