from base import *

class celestial_body:

    # Constructor
    def __init__(self, mass, position, velocity):

        # Constant Mass
        self.mass = mass

        # Initialise Position and Velocity
        self.position = np.zeros((max_steps, 2))
        self.velocity = np.zeros((max_steps, 2))

        # Initialise Acceleration
        self.acceleration = np.zeros(2)

        # Set Initial Position and Velocity
        self.position[0] = position
        self.velocity[0] = velocity

    # Update Functions
    def update_position(self, step, dt):
        self.position[step] = self.position[step - 1] + self.velocity[step - 1] * dt

    def update_velocity(self, step, dt):
        self.velocity[step] = self.velocity[step - 1] + self.acceleration * dt

    def update_acceleration(self, new_acceleration):
        self.acceleration = new_acceleration

    # Remove Empty Positions
    def remove_empty_positions(self, steps):
        self.position = self.position[:steps]
        self.velocity = self.velocity[:steps]