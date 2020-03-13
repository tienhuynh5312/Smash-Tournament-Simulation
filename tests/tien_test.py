from simulationDriver import SimulationDriver
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def test_analysis_1():
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
    plt.savefig('Average walking distance changes over simulation running time.png')
    plt.show()


def test_analysis_2():
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
    plt.savefig('Average walking distance changes over number of players in 5000s.png')
    plt.show()


# def test_analysis_3():
#     sim_duration = np.linspace(100, 2000, 10)
#     x = np.arange(0, len(sim_duration))
#     number_players = [20, 24, 30, 50, 64, 80, 90, 100]
#     y = np.arange(0, len(number_players))
#
#     x_line = []
#     y_line = []
#
#     data = []
#     for i in x:
#         SimulationDriver.SIM_DURATION = sim_duration[i]
#         for j in y:
#             SimulationDriver.TOTAL_PLAYERS = number_players[j]
#             driver = SimulationDriver()
#             driver.begin()
#
#             sum_distance = 0
#             for k in range(len(driver.players_list)):
#                 sum_distance = sum_distance + driver.players_list[k].walking_distance
#
#             data.append(sum_distance / len(driver.players_list))
#             x_line.append(sim_duration[i])
#             y_line.append(number_players[j])
#             del driver
#
#     fig = plt.figure()
#     ax = plt.axes(projection='3d')
#     ax.scatter3D(x_line, y_line, data, 'gray')
#     ax.set_xlabel('Running time (s)')
#     ax.set_ylabel('Number of players')
#     ax.set_zlabel('Average walking distance')
#     plt.show()