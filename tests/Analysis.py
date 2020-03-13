import bracketUtility
import numpy as np
import matplotlib.pyplot as plt

# Runs brackets with varying number of players and calculates the average amount
# of time each tournament takes with the number of consoles set to 4
def Analysis_1():
    NumConsoles = 4
    numPlayers = np.zeros(125)
    averageTimes = np.zeros(125)
    for i in range(3, 128):
        sum = 0
        print(i)
        for j in range(10):
            time = bracketUtility.runBracket(i, NumConsoles)
            sum = sum + time
        average = (sum / 10)
        numPlayers[i - 3] = i
        averageTimes[i - 3] = average

    plt.plot(numPlayers, averageTimes)
    plt.xlabel("Number of Entrants")
    plt.ylabel("Tournament Runtime (mins)")
    plt.title("Tournament runtime vs numEntrants")
    plt.show()

Analysis_1()