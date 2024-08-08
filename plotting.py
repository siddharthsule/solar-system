from base import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm

def animate_system(system):

    print(system.bodies[0].position)
    print(system.bodies[1].position)

    fig, ax = plt.subplots()

    # Setting up the plot limits
    ax.set_xlim(-1.5e11, 1.5e11)
    ax.set_ylim(-1.5e11, 1.5e11)
    ax.set_aspect('equal')

    # The comma unpacks the single element list
    # returned by ax.plot to a single Line2D object
    sun, = ax.plot([], [], 'yo', markersize=10, label='Sun')
    earth, = ax.plot([], [], 'bo', markersize=5, label='Earth')

    # Function to initialise the plot
    def init():
        sun.set_data([], [])
        earth.set_data([], [])
        return sun, earth

    # Function to update the plot
    def update(step):
        sun_x = system.bodies[1].position[step][0]
        sun_y = system.bodies[1].position[step][1]
        earth_x = system.bodies[0].position[step][0]
        earth_y = system.bodies[0].position[step][1]

        # Ensure the data is a sequence
        sun.set_data([sun_x], [sun_y])
        earth.set_data([earth_x], [earth_y])
        return sun, earth

    # Check if positions are populated
    if len(system.bodies[0].position) == 0 or len(system.bodies[1].position) == 0:
        print("Error: Positions are not populated.")
        return

    # Create the animation
    frames = len(system.bodies[0].position)
    ani = animation.FuncAnimation(fig, update, frames=tqdm(range(frames)), init_func=init, interval=1, blit=True)

    # Save the animation as a GIF using Pillow
    ani.save('earth_orbit.gif', writer='pillow', fps=30)

    # Optionally, save the animation as a video if ffmpeg is available
    #ani.save('earth_orbit.mp4', writer='ffmpeg', fps=30)