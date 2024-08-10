from base import *
from celestial_body import celestial_body

class solar_system:

    # Constructor
    def __init__(self, bodies):
        self.bodies = bodies

    # Acceleration Calculation
    def accleration(self, r1, r2, m2):
        rx = r2[0] - r1[0]
        ry = r2[1] - r1[1]
        r_mag = m.sqrt(rx ** 2 + ry ** 2)
        r_hat_x = rx / r_mag
        r_hat_y = ry / r_mag
        factor = G * m2 / (r_mag ** 2)
        return (factor * r_hat_x, factor * r_hat_y)

    # Calculate Acceleration due to all other bodies
    def calculate_accelerations(self, step):
        for body in self.bodies:
            total_acceleration = (0.0, 0.0)
            for other_body in self.bodies:
                if body == other_body:
                    continue
                ax, ay = self.accleration(
                    body.position[step - 1],
                    other_body.position[step - 1],
                    other_body.mass
                )
                total_acceleration = (
                    total_acceleration[0] + ax, total_acceleration[1] + ay)
            body.update_acceleration(total_acceleration)

    # Update Positions
    def update_positions(self, step, dt):
        for body in self.bodies:
            body.update_position(step, dt)

    # Update Velocities
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
            sys.stdout.write("Step: {}/{}\r".format(step, steps))
            sys.stdout.flush()  # Clear Output

        sys.stdout.write("\n")

    # Remove Empty Positions
    def remove_empty_positions(self, steps):
        for body in self.bodies:
            body.remove_empty_positions(steps)
