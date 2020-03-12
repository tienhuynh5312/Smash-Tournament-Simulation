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

        self.__tables_array = np.zeros((m, n))

        self.__wall_array = np.ones((m, n))


        # insert array into one env hashtable for easy access
        self.env = {"occupied": self.__occupied_array,
                    "organizers": self.__organizers_array,
                    "consoles": self.__consoles_array,
                    "players": self.__players_array,
                    "tables": self.__tables_array,
                    "wall": self.__wall_array}

        self.__generate_wall()

        #Must do generate table before generate console
        self.__generate_table((4, 5))

        self.__generate_consoles()

        self.update()

    def __generate_wall(self):
        import numpy as np
        from simulationDriver import SimulationDriver
        self.__wall_array[0:SimulationDriver.WALL_ROW, :] = 0
        self.__wall_array[SimulationDriver.WALL_ROW] = 3
        self.__wall_array[SimulationDriver.WALL_ROW+1:, :] = 0

        # TODO: Improve generating door
        for door in SimulationDriver.DOOR_LOCATIONS:
            for i in range(SimulationDriver.DOOR_LENGTH):
                self.__wall_array[door[0], door[1] + i] = 0

    def __generate_consoles(self):
        """This method is migrated to simulationDriver instead."""
        from simulationDriver import SimulationDriver
        import numpy as np

        def draw_console(size_tuple, horizontal=True):
            if horizontal:
                return np.ones(size_tuple)
            else:
                return np.transpose(np.ones(size_tuple))

        data = draw_console(SimulationDriver.CONSOLE_HORIZONTAL_SIZE)
        for console in SimulationDriver.CONSOLE_LOCATIONS["horizontal"]:
            x1 = console[0]
            x2 = x1 + SimulationDriver.CONSOLE_HORIZONTAL_SIZE[0]
            y1 = console[1]
            y2 = y1 + SimulationDriver.CONSOLE_HORIZONTAL_SIZE[1]
            if np.all(self.env["tables"][x1:x2, y1:y2]):
                self.env["consoles"][x1:x2, y1:y2] = 1

        data = draw_console(SimulationDriver.CONSOLE_HORIZONTAL_SIZE, False)
        for console in SimulationDriver.CONSOLE_LOCATIONS["vertical"]:
            x1 = console[0]
            x2 = x1 + SimulationDriver.CONSOLE_HORIZONTAL_SIZE[1]
            y1 = console[1]
            y2 = y1 + SimulationDriver.CONSOLE_HORIZONTAL_SIZE[0]
            if np.all(self.env["tables"][x1:x2, y1:y2]):
                self.env["consoles"][x1:x2, y1:y2] = 1

    # size_tuple = (width, height)
    def __generate_table(self, size_tuple):
        from simulationDriver import SimulationDriver
        import numpy as np

        table = np.ones(size_tuple)

        for tables in SimulationDriver.TABLE_LOCATIONS:
            # self.environment.set_occupied(tables, )
            x1 = tables[0]
            x2 = x1 + size_tuple[0]
            y1 = tables[1]
            y2 = y1 + size_tuple[1]
            self.env["occupied"][x1:x2, y1:y2] = table
            self.env["tables"][x1:x2, y1:y2] = table


    def update(self):
        import numpy as np
        self.__generate_wall()
        self.env['occupied'] = self.__consoles_array + \
                               self.__players_array + \
                               self.__organizers_array + \
                               self.__wall_array + \
                               self.__tables_array

    def set_occupied(self, location_tuple, env_string):
        self.env.get(env_string)[location_tuple] = 1

    def remove_occupied(self, location_tuple, env_string):
        self.env.get(env_string)[location_tuple] = 0

    def move_occupied(self, location_origin_tuple, location_destination_tuple, env_string):
        self.env.get(env_string)[location_origin_tuple] = 0
        self.env.get(env_string)[location_destination_tuple] = 1
