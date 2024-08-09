import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib import animation


class dataset:

    def __init__(self, name):
        self.name = name
        self.filename = name + ".csv"
        self.position = np.genfromtxt(self.filename, delimiter=',')


class database:

    def __init__(self, datasets):
        self.datasets = datasets


def animate_system(db):

    fig, ax = plt.subplots()

    # Setting up the plot limits
    ax.set_xlim(-3e12, 3e12)
    ax.set_ylim(-3e12, 3e12)
    ax.set_aspect('equal')

    # Create a plot for each body
    plots = []
    colors = ['y.', 'b.', 'g.', 'g.', 'r.', 'm.', 'k.']
    for i, ds in enumerate(db.datasets):

        plot, = ax.plot([], [], colors[i % len(colors)] if i != 0 else "yo",
                        markersize=5, label=ds.name)
        plots.append(plot)

    # Function to initialise the plot
    def init():
        for plot in plots:
            plot.set_data([], [])
        return plots

    # Function to update the plot
    def update(step):
        for i, ds in enumerate(db.datasets):
            x = ds.position[step][0]
            y = ds.position[step][1]
            plots[i].set_data([x], [y])
        return plots

    # Check if positions are populated
    if any(len(ds.position) == 0 for ds in db.datasets):
        print("Error: Positions are not populated.")
        return

    # Create the animation
    frames = len(db.datasets[0].position)
    ani = animation.FuncAnimation(fig, update, frames=tqdm(
        range(frames)), init_func=init, interval=1, blit=True)

    # Save the animation as a GIF using Pillow
    ani.save('earth_orbit.gif', writer='pillow', fps=30)


def main():

    sun_data = dataset("sun")
    mercury_data = dataset("mercury")
    venus_data = dataset("venus")
    earth_data = dataset("earth")
    moon_data = dataset("moon")
    mars_data = dataset("mars")
    jupiter_data = dataset("jupiter")
    saturn_data = dataset("saturn")
    uranus_data = dataset("uranus")
    neptune_data = dataset("neptune")
    pluto_data = dataset("pluto")

    db = database([sun_data, mercury_data, venus_data, earth_data, moon_data,
                  mars_data, jupiter_data, saturn_data, uranus_data, neptune_data, pluto_data])
    animate_system(db)


if __name__ == "__main__":
    main()
