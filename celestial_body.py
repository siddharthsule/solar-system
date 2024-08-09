from base import *


class celestial_body:

    # Constructor
    def __init__(self, name, mass, position, velocity):

        # Set Name
        self.name = name

        # Constant Mass
        self.mass = mass

        # Initialise Position and Velocity
        self.position = [(0.0, 0.0)] * max_steps
        self.velocity = [(0.0, 0.0)] * max_steps

        # Initialise Acceleration
        self.acceleration = (0.0, 0.0)

        # Set Initial Position and Velocity
        self.position[0] = position
        self.velocity[0] = velocity

    # Update Functions
    def update_position(self, step, dt):
        x_new = self.position[step - 1][0] + self.velocity[step - 1][0] * dt
        y_new = self.position[step - 1][1] + self.velocity[step - 1][1] * dt
        self.position[step] = (x_new, y_new)

    def update_velocity(self, step, dt):
        vx_new = self.velocity[step - 1][0] + self.acceleration[0] * dt
        vy_new = self.velocity[step - 1][1] + self.acceleration[1] * dt
        self.velocity[step] = (vx_new, vy_new)

    def update_acceleration(self, new_acceleration):
        self.acceleration = new_acceleration

    # Remove Empty Positions
    def remove_empty_positions(self, steps):
        self.position = self.position[:steps]
        self.velocity = self.velocity[:steps]
