# - Import modules
from enviornment import *


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

    def __init__(self):
        """
        Initialize the simulation driver for stage 1 in the description.
        """
        self.console_rental_fee_per_hour = 10  # dollars
        self.player_admission_profit = 3  # dollars
        self.time_stamp = 0
        self.__time_step = 5
        self.console_rental_fee = self.get_console_rental_fee()  # $ per hour
        self.tournament_profit = self.get_tournament_profit()

        # - Create environment.
        # - TODO: after creating the environment class.
        self.__generate_environment()

        # - TODO: place consoles
        self.__generate_console_configuration()

        # - TODO: place reporting station(s)
        self.__generate_report_stations()

        # - TODO: place unreachable areas, aka wall, etc
        self.__generate_obstacles()

        # - TODO: place players
        self.__generate_players()
        self.totalInitialPlayers = 0  # TODO: call method from player.py to get total players

    def begin(self):
        self.__start_tournament()
        self.__report_tournament()

    def __start_tournament(self):
        # - TODO: Run the tournament

        while True:
            # - Increase timeStamp by timeStep
            self.time_stamp = self.time_stamp + self.__time_step

            # - Call a pair of player to the reporting station
            # - If they are here:
            # -     Assign player to the consoles by location
            # - else: wait by keep going the execution (waiting time)

            # - for other players not getting called
            # - make them move randomly. player.moveRandom()

            # if player just get eliminated, give them a staying time:
            # - if player.isRecentlyEliminated():
            #       play.playAround()
        pass

    def __report_tournament(self):
        pass

    def get_console_rental_fee(self):

        if self.time_stamp == 0:
            return 0
        else:
            return self.timeStampt / 3600 * self.console_rental_fee_per_hour

    def get_tournament_profit(self):
        total_profit = self.totalInitialPlayers * self.player_admission_profit - self.get_console_rental_fee()
        return total_profit

    def __generate_console_configuration(self):
        return 0

    def __generate_players(self):
        return 0

    def __generate_obstacles(self):
        pass

    def __generate_report_stations(self):
        pass

    def __generate_environment(self):
        pass
