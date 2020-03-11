
import simulationDriver
import time

class TestForQuestions:

    # How does how early best of 5 start affect the runtime of tournaments of varying number of entrants?

    # How many staff member can we add before there work is negligible based on varying number of entrants? 
    
    '''This function tests the effect of different number of staff members/reporting stations on the amount of time
    the tournament will take. The test will calculate the amount of time it takes to run tournament from 1 to staffNum'''
    #staffNum = how many reportingStations (max, will perform a test at each iteration of staffNum), playerNum = number of entrants
    def testStaff(self, staffNum, playerNum):
        test = simulationDriver.SimulationDriver()
        test.TOTAL_PLAYERS = playerNum
        for reportingStation in range(1, staffNum):
            test.__generate_report_stations()
            start_time = time.time()
            test.begin()
            print("The tournament ran for: " + (time.time() - start_time) + " seconds with " + reportingStation + "staff members.")



    # What is the best setup to optimize for profitability while still staying within time?

    '''This function will only take in consideration for the effect of number of consoles, reporting booths, 
    and hard time limit of 5 hours (aka 18000 secs). 
    Assuming defaults we have:
    - 1 booth volunteer
    - timeLimit = 18000 seconds
    - playerNum = 144 players
    - entryFee = 3 dollars
    - pricePerHour = 10 dollars
    - maxConsoles is going to be 4 for this test.
    Profit is (player entry fee - number of consoles rented * price per hour)
    *Assuming entry fee and ppr stays the same, Max profit is only effected by shorter tournament
    time or fewer rented consoles
    Tables added according to specs, test case:
    - All 4 placed on every table (5)
    - 1 console placed on each table'''
    def optimizeSetup(maxConsoles = 4, booth = 1, playerNum = 144, timeLimit = 18000, entryFee = 3):
        test = simulationDriver.SimulationDriver()
        test.player_admission_profit = entryFee
        test.TOTAL_PLAYERS = playerNum
        test.SIM_DURATION = timeLimit
        test.ORGANIZER_LOCATIONS = [(12, 48)]
        test.__generate_players()
        test.__generate_report_stations()

        #Changing Table Locations and recall again for orientation, could be improved?
        test.TABLE_LOCATIONS = [(18, 0)]
        #Vertical Table size
        size_tuple = (3, 12)
        test.__generate_table(size_tuple)

        #For Horizontal tables
        test.TABLE_LOCATIONS = [(3, 12), (12, 12), (15, 12), (24, 12)]
        size_tuple2 = (24, 3)
        test.__generate_table(size_tuple2)

        test.TABLE_LOCATIONS.insert(0,(18, 0))

        profits_list = []

        for table in test.TABLE_LOCATIONS:
            for console in range(1, maxConsoles):
                profit = 0
                
                # table
                

                if (timeLimit <= 0):
                    profits_list.append
                test.__generate_console_configuration()
        
    # How does whether we use a random walk or calculated distance actually impact runtime?

    # Do bathroom breaks greatly influence the amount of time it takes to run a tournament?

    # Do people showing up to tournaments late greatly influence the amount of time it takes? to run said tournament?

    # How does the length that players stay after getting eliminated influence the tournament runtime?

    # Is it better to have tournament organizers stationary for most of the event or moving around to meet with players?

    # How much faster do single elimination brackets run that double elimination brackets?

    # Does running a tournament stream greatly impact the runtime of the tournament? 

    # How advantageous is it to number setups so that people know where to go?
