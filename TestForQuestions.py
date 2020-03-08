
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

    # '''This function'''
    # def optimizeSetup(maxConsoles, maxStaff, ):

    # How does whether we use a random walk or calculated distance actually impact runtime?

    # Do bathroom breaks greatly influence the amount of time it takes to run a tournament?

    # Do people showing up to tournaments late greatly influence the amount of time it takes? to run said tournament?

    # How does the length that players stay after getting eliminated influence the tournament runtime?

    # Is it better to have tournament organizers stationary for most of the event or moving around to meet with players?

    # How much faster do single elimination brackets run that double elimination brackets?

    # Does running a tournament stream greatly impact the runtime of the tournament? 

    # How advantageous is it to number setups so that people know where to go?
