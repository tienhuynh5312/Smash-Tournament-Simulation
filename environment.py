class Environment:
    """
    Class to represent the environment of smash tournaments
    This includes the console play area and areas where the player is waiting
    between matches.
    """

    def __init__(self, m, n):
        import numpy as np
        self.rows = m
        self.cols = n

        self.__occupied_array = np.zeros((m, n))

        self.__organizers_array = np.zeros((m, n))

        self.__consoles_array = np.zeros((m, n))

        self.__players_array = np.zeros((m, n))

        self.__generate_wall()
        self.__generating_consoles()

        # insert array into one env hashtable for easy access
        self.env = {"occupied": self.__occupied_array,
                    "organizers": self.__organizers_array,
                    "consoles": self.__consoles_array,
                    "players": self.__players_array}

    def __generate_wall(self):
        import numpy as np
        from simulationDriver import SimulationDriver

        door = np.zeros(SimulationDriver.DOOR_LENGTH)

        wall = np.ones(self.cols)

        # TODO: Improve generating door
        wall[0:len(door)] = door

        # Mark occupied
        self.__occupied_array[SimulationDriver.WALL_ROW, :] = wall

    def __generating_consoles(self):
        from simulationDriver import SimulationDriver
        # SimulationDriver.NUMBER_OF_CONSOLES

        # - Place console in the console area
        pass

