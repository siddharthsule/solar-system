from base import *
from celestial_body import celestial_body
from solar_system import solar_system
import argparse


def main():
    parser = argparse.ArgumentParser(description="Simulate the solar system.")
    parser.add_argument('--years', type=int, default=100,
                        help='Number of years to simulate')
    parser.add_argument('--dt', type=int, default=3600,
                        help='Time step in seconds')
    args = parser.parse_args()

    # Load Constants from constants.csv, and create objects for celestial body
    print("Initialising Celestial Bodies...")
    celestial_bodies = []
    with open("constants.csv", "r") as file:

        # ignore the first line
        file.readline()

        # Read the rest of the lines
        for line in file:
            name, mass, posx, posy, velx, vely = line.split(",")
            mass = float(mass)
            position = (float(posx), float(posy))
            velocity = (float(velx), float(vely))
            celestial_bodies.append(celestial_body(
                name, mass, position, velocity))

    # Number of steps to simulate
    years = args.years
    steps = int(365.25 * 24) * years  # 1 year = 365.25 days * 24 hours
    dt = args.dt  # Time step in seconds, default is 1 hour

    print("Simulating Solar System...")
    system = solar_system(celestial_bodies)
    system.simulate(steps=steps, dt=dt)

    print("Saving Data...")
    # Remove empty positions
    if steps < max_steps:
        system.remove_empty_positions(steps)

    # Only store 1000 positions from the whole simulation
    max_positions = 1000
    step = len(system.bodies[0].position) / max_positions
    for body in system.bodies:
        body.position = body.position[::int(step)]

    # For every body in the system, have a name.csv file
    for body in system.bodies:
        filename = body.name + ".csv"
        with open(filename, "w") as file:
            for i in range(max_positions):
                x, y = body.position[i]
                file.write("{}, {}\n".format(x, y))


if __name__ == "__main__":
    main()
