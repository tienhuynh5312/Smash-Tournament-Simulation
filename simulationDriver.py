# - Import modules
from environment import Environment
from Player import Player
from visualize import Visualize


class SimulationDriver:
    """
    Class which drives the simulation of the smash tournament
    1. Initialization
    Initialize console configuration, number of players,
    Time is initialized to be 0
    The rental fees are calculated as the number of consoles being used * 3 dollars per hour.
    The Profit of the tournaments is calculated as the number of players * the amount they are being charged - the rental fees.
    Create the environment which will represent the venue
    Place consoles and reporting stations and unreachable areas throughout the environment
    Create a number of players and randomly place them throughout the waiting room.

    2. Start the tournament
    Run the tournament until there are no matches left to be played in the bracket
    Time in the tournament will increment in intervals of 5 second at a time
    If there are available consoles to be played at the reporting desk / staff member will call pairs
    of people to fill those setups until there are either no available matches to be called or there are no empty consoles.
    At each time step if a player has a location that they have been assigned to go towards the will move towards that location.
    If the player has not been assigned a location then they will have a 5% chance of walking in a random unblocked direction.
    When a player is eliminated from the tournament a random amount of time with minimum 10 minutes and maximum 60 minutes
    will be assigned to them. This will be the amount of time they will stay in the simulation before choosing to leave.

    3. Report tournament
    Return the amount of time that the tournament took and the net profit of the tournament.

    """
    TIME_STEP = 4  # second
    SIDE_LENGTH = 1  # ft
    DOOR_LENGTH = 5

    WAITING_AREA_ROWS = 48
    CONSOLE_AREA_ROWS = 24
    WALL_ROW = CONSOLE_AREA_ROWS + 1  # which row we place the wall
    WALL_ROWS = 1
    ALL_AREA_ROWS = WAITING_AREA_ROWS + CONSOLE_AREA_ROWS + WALL_ROWS
    ALL_AREA_COLS = 48
    NUMBER_OF_CONSOLES = 10
    TOTAL_PLAYERS = 30

    # DOOR_LOCATIONS = [(WALL_ROW, 0), (WALL_ROW, 10), (WALL_ROW, 15)]
    DOOR_LOCATIONS = [(WALL_ROW, 0)]
    ORGANIZER_LOCATIONS = [(3, 45)]
    CONSOLE_LOCATIONS = [(0, 1), (0, 5), (0, 23)]
    CONSOLE_LOCATIONS = {"horizontal": [(2, 5), (0, 23), (3,25)],
                         "vertical": [(0, 0), (5, 5), (5,40), (0,40), (10, 40), (17, 40)]}
    CONSOLE_HORIZONTAL_SIZE = (1, 3)  # console size when in horizontal size.

    PLAYER_SHOW_UP_LATE_PERCENT = 0.05
    PLAYER_BATHROOM_PERCENT = 0.01
    BATHROOM_DISTANCE = 101
    SIM_DURATION = 100  # seconds

    def __init__(self):
        """
        Initialize the simulation driver for stage 1 in the description.
        """
        import numpy as np

        self.console_rental_fee_per_hour = 10  # dollars
        self.player_admission_profit = 3  # dollars
        self.time_stamp = 0
        self.__time_step = SimulationDriver.TIME_STEP
        self.console_rental_fee = self.get_console_rental_fee()  # $ per hour
        self.tournament_profit = self.get_tournament_profit()

        # - Create environment.
        # - TODO: after creating the environment class.
        self.environment = None
        self.__generate_environment()
        self.env = self.environment.env

        # - TODO: place consoles
        self.__generate_console_configuration()

        # - TODO: place reporting station(s)
        self.__generate_report_stations()

        # - TODO: place unreachable areas, aka wall, etc
        self.__generate_obstacles()

        # - TODO: place players
        self.__generate_players()

        self.data = np.zeros((int(SimulationDriver.SIM_DURATION / SimulationDriver.TIME_STEP), \
                              SimulationDriver.ALL_AREA_ROWS, SimulationDriver.ALL_AREA_COLS))

    def begin(self):
        """Begin the simulation"""
        self.__start_tournament()
        self.__report_tournament()
        Visualize.plot_3d(self.data, self.environment.env)

    def __start_tournament(self):
        import numpy as np
        # - TODO: Run the tournament
        index_plot = 0
        while True:
            # - Increase timeStamp by timeStep
            self.time_stamp = self.time_stamp + self.__time_step
            for pid in self.players_list.keys():
                player = self.players_list[pid]
                if player.destination_location is None:
                    player.set_destination(SimulationDriver.ORGANIZER_LOCATIONS[0])

                self.environment.update()
                player.walk(self.environment)
            # - Call a pair of player to the reporting station
            # - If they are here:
            # -     Assign player to the consoles by location
            # - else: wait by keep going the execution (waiting time)

            # - for other players not getting called
            # - make them move randomly. player.moveRandom()

            # if player just get eliminated, give them a staying time:
            # - if player.isRecentlyEliminated():
            #       player.playAround()

            self.data[index_plot] = self.environment.env["occupied"]
            index_plot = index_plot + 1
            # - TODO: condition to end the outermost while loop
            if self.time_stamp == SimulationDriver.SIM_DURATION:
                break

    def __report_tournament(self):
        pass

    def get_console_rental_fee(self):
        if self.time_stamp == 0:
            return 0
        else:
            return self.time_stamp / 3600 * self.console_rental_fee_per_hour

    def get_tournament_profit(self):
        total_profit = SimulationDriver.TOTAL_PLAYERS * self.player_admission_profit - self.get_console_rental_fee()
        return total_profit

    def __generate_console_configuration(self):
        def draw_console(size_tuple, horizontal=True):
            import numpy as np
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
            self.environment.env["occupied"][x1:x2, y1:y2] = data
            self.environment.env["consoles"][x1:x2, y1:y2] = data

        data = draw_console(SimulationDriver.CONSOLE_HORIZONTAL_SIZE, False)
        for console in SimulationDriver.CONSOLE_LOCATIONS["vertical"]:
            x1 = console[0]
            x2 = x1 + SimulationDriver.CONSOLE_HORIZONTAL_SIZE[1]
            y1 = console[1]
            y2 = y1 + SimulationDriver.CONSOLE_HORIZONTAL_SIZE[0]
            self.environment.env["occupied"][x1:x2, y1:y2] = data
            self.environment.env["consoles"][x1:x2, y1:y2] = data

    def __generate_players(self):
        import numpy as np
        self.players_list = {}
        # - Set the location of the player randomly
        row_min = SimulationDriver.WALL_ROW + 1
        row_max = SimulationDriver.ALL_AREA_ROWS
        col_min = 0
        col_max = SimulationDriver.ALL_AREA_COLS
        for i in range(SimulationDriver.TOTAL_PLAYERS):
            self.players_list[i] = Player(player_id=i)
            random_location_row = np.random.randint(row_min, row_max)
            random_location_col = np.random.randint(col_min, col_max)
            random_location = (random_location_row, random_location_col)

            # if there is something occupied at random_location, generate another one.
            while self.environment.env["occupied"][random_location] == 1:
                random_location_row = np.random.randint(row_min, row_max)
                random_location_col = np.random.randint(col_min, col_max)
                random_location = (random_location_row, random_location_col)

            self.players_list[i].current_location = random_location
            self.environment.set_occupied(random_location, "players")

    def __generate_obstacles(self):
        pass

    def __generate_report_stations(self):
        for organizer in SimulationDriver.ORGANIZER_LOCATIONS:
            self.environment.set_occupied(organizer, "organizers")

    def __generate_environment(self):
        self.environment = Environment(SimulationDriver.ALL_AREA_ROWS, SimulationDriver.ALL_AREA_COLS)
