import bracketUtility
import numpy as np
import matplotlib.pyplot as plt
from simulationDriver import SimulationDriver

# Runs brackets with varying number of players and calculates the average amount
# of time each tournament takes with the number of consoles set to 4.
# Plots the results.
def Analysis_1():
    NumConsoles = 4
    numPlayers = np.zeros(125)
    averageTimes = np.zeros(125)
    for i in range(3, 128):
        sum = 0
        # print(i)
        for j in range(10):
            time = bracketUtility.runBracket(i, NumConsoles, False)
            sum = sum + time
        average = (sum / 10)
        numPlayers[i - 3] = i
        averageTimes[i - 3] = average

    plt.plot(numPlayers, averageTimes)
    plt.xlabel("Number of Entrants")
    plt.ylabel("Tournament Runtime (hours)")
    plt.title("Tournament runtime vs numEntrants")
    plt.savefig("Analysis1.png")
    plt.clf()

# Runs brackets with the number of players set to 128 and varying
# numbers of consoles from 1 to 64. Runs each set of parameters 10
# times and taking the average as the runtime. Plots the results.
def Analysis_2():
    NumPlayers = 128
    numConsoles = np.zeros(64)
    averageTimes = np.zeros(64)
    for i in range(1, 65):
        sum = 0
        # print(i)
        for j in range(10):
            time = bracketUtility.runBracket(NumPlayers, i, False)
            sum = sum + time
        average = (sum / 10)
        numConsoles[i - 1] = i
        averageTimes[i - 1] = average

    plt.plot(numConsoles, averageTimes)
    plt.xlabel("Number of Consoles")
    plt.ylabel("Tournament Runtime (hours)")
    plt.title("Tournament runtime vs numConsoles")
    plt.savefig("Analysis2.png")
    plt.clf()

# Runs brackets with varying number of players and calculates the average amount
# of time each tournament takes with the number of consoles set to 4. Additionally
# Has one player who is playing extremely slow on purpose. All of this players matches
# Take 21 minutes long. Which is the maximum amount of time a b03 set can take.
# Plots the results.
def Analysis_3():
    NumConsoles = 4
    numPlayers = np.zeros(126)
    averageTimes = np.zeros(126)
    for i in range(3, 129):
        sum = 0
        # print(i)
        for j in range(10):
            time = bracketUtility.runBracket(i, NumConsoles, True)
            sum = sum + time
        average = (sum / 10)
        numPlayers[i - 3] = i
        averageTimes[i - 3] = average

    plt.plot(numPlayers, averageTimes)
    plt.xlabel("Number of Entrants")
    plt.ylabel("Tournament Runtime (hours)")
    plt.title("Tournament runtime vs numEntrants (Timeout Enabled)")
    plt.savefig("Analysis3.png")
    plt.clf()

def Analysis_4():
    sim_duration = np.linspace(100, 50000, 20)
    x = np.arange(0, len(sim_duration))
    data = []
    for i in x:
        SimulationDriver.SIM_DURATION = sim_duration[i]
        driver = SimulationDriver()
        driver.begin()

        sum_distance = 0
        for j in range(len(driver.players_list)):
            sum_distance = sum_distance + driver.players_list[j].walking_distance

        data.append(sum_distance / len(driver.players_list))
        del driver
    plt.plot(sim_duration, data)
    plt.xlabel('Simulation running time (s)')
    plt.ylabel('Average walking distance (ft)')
    plt.title('Average walking distance changes over simulation running time.')
    plt.savefig('Analysis4.png')
    plt.show()


def Analysis_5():
    number_players = [20, 24, 30, 50, 64, 80, 90, 100]
    x = np.arange(0, len(number_players))
    data = []
    SimulationDriver.SIM_DURATION = 5000
    for i in x:
        SimulationDriver.TOTAL_PLAYERS = number_players[i]
        driver = SimulationDriver()
        driver.begin()

        sum_distance = 0
        for j in range(len(driver.players_list)):
            sum_distance = sum_distance + driver.players_list[j].walking_distance

        data.append(sum_distance / len(driver.players_list))
        del driver

    plt.plot(number_players, data)
    plt.xlabel('Number of players')
    plt.ylabel('Average walking distance (ft)')
    plt.title('Average walking distance changes over number of players in 5000s.')
    plt.savefig('Analysis5.png')
    plt.show()

# Runs the test cases
Analysis_1()
Analysis_2()
Analysis_3()
Analysis_4()
Analysis_5()