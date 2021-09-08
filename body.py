import numpy as np
from itertools import combinations

# ---------------------------------------------------------------------------------------------------------------------


class Body:

    _G = 1.0

    mass = 0.0
    position = None
    velocity = None

    positions = None
    velocities = None

    related_bodies = None

    _continue_condition = None

    def __init__(self, mass, position, velocity, continue_condition):
        self.mass = mass
        self.positions = []
        self.velocities = []
        self.related_bodies = []

        self.position = np.array(position, dtype=float)
        self.positions.append(self.position)
        self.velocity = np.array(velocity, dtype=float)
        self.velocities.append(self.velocity)

        self._continue_condition = continue_condition

    def _magnitude(self, body):
        return np.sum((body.position - self.position)**2)

    def _unit_vector(self, body):
        vector = body.position-self.position
        return vector / np.sqrt(np.sum(vector**2))

    def add_related_body(self, body):
        self.related_bodies.append(body)

    def step(self, dt):

        net_force_per_mass = np.array([0.0, 0.0, 0.0], dtype=float)

        for body in self.related_bodies:
            radius_sq = self._magnitude(body)
            force_per_mass = self._G * body.mass / radius_sq
            net_force_per_mass = net_force_per_mass + self._unit_vector(body) * force_per_mass

        self.velocity = net_force_per_mass * dt + self.velocity
        self.velocities.append(self.velocity)

        self.position = self.velocity * dt + self.position
        self.positions.append(self.position)

        net_force = np.sum((net_force_per_mass * self.mass)**2)
        return self._continue_condition(self, net_force)


# ---------------------------------------------------------------------------------------------------------------------


class System:

    label = None
    bodies = []

    def __init__(self, label, bodies):
        combos = list(combinations(range(len(bodies)), 2))
        self.bodies = bodies
        self.label = label

        for combo in combos:
            bodies[combo[0]].add_related_body(bodies[combo[1]])
            bodies[combo[1]].add_related_body(bodies[combo[0]])

    def step(self, dt):

        cont = True

        for body in self.bodies:
            cont = cont and body.step(dt)

        return cont

