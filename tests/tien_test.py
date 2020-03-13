from simulationDriver import SimulationDriver
import numpy as np
import matplotlib.pyplot as plt

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

        data.append(sum_distance/len(driver.players_list))
        del driver
    plt.plot(sim_duration, data)
    plt.xlabel('Simulation running time (s)')
    plt.ylabel('Average walking distance (ft)')
    plt.title('Average walking distance changes over simulation running time.')
    plt.savefig('Average walking distance changes over simulation running time.png')
    plt.show()
