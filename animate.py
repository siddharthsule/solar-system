import numpy as np
import os
import sys
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

    fig, ax = plt.subplots(figsize=(5, 5))

    # Setting up the plot limits
    ax.set_xlim(-3e12, 3e12)
    ax.set_ylim(-3e12, 3e12)
    ax.set_aspect('equal')

    # Create a plot for each body
    plots = []
    for i, ds in enumerate(db.datasets):

        plot, = ax.plot([], [], markersize=5, label=ds.name)
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
    ani.save('orbit.gif', writer='pillow', fps=30)


def main():

    # Find all CSV files and create a dataset for each - except constants.csv
    datasets = []
    csv_files = [f for f in os.listdir(".") if f.endswith(
        ".csv") and f != "constants.csv"]
    for file in csv_files:
        # get the name of the file without the extension
        name = os.path.splitext(file)[0]
        datasets.append(dataset(name))

    db = database(datasets)
    animate_system(db)


if __name__ == "__main__":
    main()
