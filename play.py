import numpy as np
from itertools import combinations
from body import Body, System
from matplotlib import pyplot as plt

system = System(bodies=[
    Body(mass=1.0, position=[-1.0, -1.0, 0.0], velocity=[0.0, 5.0, 0.0]),
    Body(mass=100.0, position=[1.0, 1.0, 0.0], velocity=[0.0, 0.0, 0.0])
])

for i in range(1000000):
    if i > 10 and not system.step(0.001):
        break

positions_1 = np.array(system.bodies[0].positions)
positions_2 = np.array(system.bodies[1].positions)

plt.scatter(positions_1[:, 0], positions_1[:, 1])
plt.scatter(positions_2[:, 0], positions_2[:, 1])
plt.show()








