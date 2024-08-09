from base import *
from constants import *
from celestial_body import celestial_body
from solar_system import solar_system


def main():

    print("Initialising Celestial Bodies...")
    sun = celestial_body(name="sun", mass=mass_sun,
                         position=pos_sun, velocity=vel_sun)
    mercury = celestial_body(
        name="mercury", mass=mass_mercury, position=pos_mercury, velocity=vel_mercury)
    venus = celestial_body(name="venus", mass=mass_venus,
                           position=pos_venus, velocity=vel_venus)
    earth = celestial_body(name="earth", mass=mass_earth,
                           position=pos_earth, velocity=vel_earth)
    moon = celestial_body(name="moon", mass=mass_moon,
                          position=pos_moon, velocity=vel_moon)
    mars = celestial_body(name="mars", mass=mass_mars,
                          position=pos_mars, velocity=vel_mars)
    jupiter = celestial_body(
        name="jupiter", mass=mass_jupiter, position=pos_jupiter, velocity=vel_jupiter)
    saturn = celestial_body(name="saturn", mass=mass_saturn,
                            position=pos_saturn, velocity=vel_saturn)
    uranus = celestial_body(name="uranus", mass=mass_uranus,
                            position=pos_uranus, velocity=vel_uranus)
    neptune = celestial_body(
        name="neptune", mass=mass_neptune, position=pos_neptune, velocity=vel_neptune)
    pluto = celestial_body(name="pluto", mass=mass_pluto,
                           position=pos_pluto, velocity=vel_pluto)

    years = 10
    steps = int(365.25 * 24) * years  # 1 year = 365.25 days * 24 hours
    dt = 3600  # 1 hour = 60 * 60 seconds

    print("Simulating Solar System...")
    system = solar_system([sun, mercury, venus, earth,
                          moon, mars, jupiter, saturn, uranus, neptune, pluto])
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
