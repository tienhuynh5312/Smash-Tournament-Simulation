"""
Class which drives the simulation of the smash tournament
"""


class Player:
    def __init__(self):
        self.distance = 0
        self.isOut = False
        self.isPlaying = False
        self.isLeft = False
        self.destination = None
        pass

    def walk(self):
        pass

    def wait(self):
        pass

    def play(self):
        pass
