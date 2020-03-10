class Visualize:
    """
    Animates and plots the smash tournament
    """

    @staticmethod
    def plot_3d(data_3d, env):
        import numpy as np
        import matplotlib.pyplot as plt
        from simulationDriver import SimulationDriver

        fig = plt.figure(figsize=(5, 5))
        shape = data_3d.shape
        combine = np.zeros((shape[1], shape[2]))
        combine = env["players"]*0.3
        combine[SimulationDriver.WALL_ROW] = env["occupied"][SimulationDriver.WALL_ROW]*10
        data = data_3d[0] + combine
        ax = fig.add_axes((0, 0, 1, 1), frameon=False)
        img = ax.imshow(data, interpolation='none',
                        extent=[0, shape[1], 0, shape[2]],
                        aspect="auto",
                        zorder=0)
        for data in data_3d:
            combine = env["players"]*0.3
            combine[SimulationDriver.WALL_ROW] = env["occupied"][SimulationDriver.WALL_ROW] * 10
            data1 = data + combine
            img.set_data(data1)
            plt.draw()
            plt.pause(0.2)
