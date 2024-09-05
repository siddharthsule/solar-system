import numpy as np
import os
import sys
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib import animation

import matplotlib as mpl
mpl.rc_file("mplstyleerc")

class dataset:

    def __init__(self, name):
        self.name = name
        self.filename = name + ".csv"
        self.position = np.genfromtxt(self.filename, delimiter=',')


class database:

    def __init__(self, datasets):
        self.datasets = datasets


def animate_system(db):

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Setting up the plot limits
    ax[0].set_xlim(-6e12, 6e12)
    ax[0].set_ylim(-6e12, 6e12)
    ax[0].set_aspect('equal')
    ax[0].set_title('Whole Solar System')

    ax[1].set_xlim(-2.5e11, 2.5e11)
    ax[1].set_ylim(-2.5e11, 2.5e11)
    ax[1].set_aspect('equal')
    ax[1].set_title('Nearby Planets')

    # Create a plot for each body on both axes
    plots = []
    # Add more colors if needed
    colors = ['y.', 'b.', 'g.', 'r.', 'm.', 'k.', 'c.']
    for i, ds in enumerate(db.datasets):
        plot0, = ax[0].plot([], [], colors[i % len(colors)],
                            markersize=5, label=ds.name)
        plot1, = ax[1].plot([], [], colors[i % len(colors)],
                            markersize=5, label=ds.name)
        plots.append((plot0, plot1))

    # Function to initialise the plot
    def init():
        for plot0, plot1 in plots:
            plot0.set_data([], [])
            plot1.set_data([], [])
        return [plot for pair in plots for plot in pair]

    # Function to update the plot
    def update(step):
        for i, ds in enumerate(db.datasets):
            x = ds.position[step][0]
            y = ds.position[step][1]
            plots[i][0].set_data([x], [y])
            plots[i][1].set_data([x], [y])
        return [plot for pair in plots for plot in pair]

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

    # Optionally, save the animation as a video if ffmpeg is available
    # ani.save('orbit.mp4', writer='ffmpeg', fps=30)


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
