import math
import numpy as np
from matplotlib import pyplot as plt
from body import Body, System
from factories import TwoBodyWithCenter


factory = TwoBodyWithCenter(
    center_mass=1000.0,
    mass = 1.0,
    position=[10.0, 0.0, 0.0],
    speeds=[i * 0.1 + 12.5 for i in range(10)],
    # angles=[i * 2.0 * math.pi / 32.0 for i in range(32)],
    angles=[1.5707963267948966],
    continue_condition=lambda body, force: (
           force > 0.0001 and 10 < len(body.positions) < 20000000
        ) or len(body.positions) <= 10
)

max_steps = 0
max_label = None

for system in factory.make():
    while True:
        if not system.step(0.01):
            break

    if len(system.bodies[1].positions) > max_steps:
        max_steps = len(system.bodies[1].positions)
        max_label = system.label

    print("label: {} - steps {}".format(system.label, len(system.bodies[1].positions)))

print("winner: {} - steps {}".format(max_label, max_steps))

# positions_1 = np.array(system.bodies[0].positions)
# positions_2 = np.array(system.bodies[1].positions)
#
# plt.scatter(positions_1[:, 0], positions_1[:, 1])
# plt.scatter(positions_2[:, 0], positions_2[:, 1])
# plt.show()
