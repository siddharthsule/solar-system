from base import *
from celestial_body import celestial_body
from solar_system import solar_system
from plotting import animate_system

def main():
    earth = celestial_body(mass=5.972e24, position=[1.496e11, 0], velocity=[0, 29780])
    sun = celestial_body(mass=1.989e30, position=[0, 0], velocity=[0, 0])

    steps = 5256
    dt = 60

    system = solar_system([earth, sun])
    system.simulate(steps=steps, dt=dt)

    if steps < max_steps:
        system.remove_empty_positions(steps)

    animate_system(system)


if __name__ == "__main__":
    main()