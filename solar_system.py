from base import *
from celestial_body import celestial_body


class solar_system:

    # Constructor
    def __init__(self, bodies):
        self.bodies = bodies

    # Calculate Acceleration due to all other bodies

    def calculate_accelerations(self, step):

        for body in self.bodies:

            total_acceleration = np.zeros(2)

            for other_body in self.bodies:

                if body == other_body:
                    continue

                r = self.bodies[1].position[step - 1] - self.bodies[0].position[step - 1]
                r_mag = np.sqrt(r[0] ** 2 + r[1] ** 2)
                r_hat = r / r_mag
                total_acceleration += G * other_body.mass * r_hat / r_mag ** 2

            body.update_acceleration(total_acceleration)

    # Update Functions
    def update_positions(self, step, dt):
        for body in self.bodies:
            body.update_position(step, dt)

    def update_velocities(self, step, dt):
        for body in self.bodies:
            body.update_velocity(step, dt)

    # Update System
    def update(self, step, dt):
        self.calculate_accelerations(step)
        self.update_velocities(step, dt)
        self.update_positions(step, dt)

    # Simulate System
    def simulate(self, steps, dt):

        for step in range(1, steps):

            # Update System
            self.update(step, dt)

            # Print Progress
                # Event Counter for Terminal
            sys.stdout.write("Progress: %d%%   \r" % (step / steps * 100))
            sys.stdout.flush() # Clear Output

    # Remove Empty Positions
    def remove_empty_positions(self, steps):
        for body in self.bodies:
            body.remove_empty_positions(steps)
