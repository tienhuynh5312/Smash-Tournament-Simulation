class Visualize:
    """
    Animates and plots the smash tournament
    """

    @staticmethod
    def plot_3d(data, env):
        import numpy as np
        import matplotlib.pyplot as plt
        from simulationDriver import SimulationDriver
        data_3d = np.zeros((len(data), SimulationDriver.ALL_AREA_ROWS, SimulationDriver.ALL_AREA_COLS))
        time_stamps = []
        for i in range(len(data)):
            data_3d[i] = data[i][1]
            time_stamps.append(data[i][0])

        fig = plt.figure(figsize=(5, 5))
        shape = data_3d.shape
        combine = np.zeros((shape[1], shape[2]))
        combine = env["consoles"]*2 + env["organizers"]*5 + env["wall"]
        data1 = data_3d[0]*4 + combine
        ax = fig.add_axes((0, 0, 1, 1), frameon=False)
        img = ax.imshow(data1, interpolation='none',
                        extent=[0, shape[1], 0, shape[2]],
                        aspect="auto",
                        zorder=0)
        for i in range(len(data_3d)):
            combine = env["consoles"]*2 + env["organizers"]*5 + env["wall"]
            data1 = data_3d[i]*4 + combine
            img.set_data(data1)
            plt.draw()
            plt.pause(0.1)
