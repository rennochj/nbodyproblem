from body import System
from body import Body
import math


class TwoBodyWithCenter:

    _center_mass = None
    _mass = 0.0
    _position = None
    _speeds = 0.0
    _angles = None
    _continue_condition = None

    def __init__(self, center_mass, mass, position, speeds, angles, continue_condition):
        self._center_mass = center_mass
        self._mass = mass
        self._position = position
        self._speeds = speeds
        self._angles = angles
        self._continue_condition = continue_condition

    def make(self):

        for speed in self._speeds:
            for angle in self._angles:

                yield System(
                    label="speed: {}, angle: {}".format(speed, angle),
                    bodies = [
                        Body(
                            mass=self._center_mass,
                            position=[0.0, 0.0, 0.0],
                            velocity=[0.0, 0.0, 0.0],
                            continue_condition=self._continue_condition
                        ),
                        Body(
                            mass=self._mass,
                            position=self._position,
                            velocity=[speed * math.cos(angle), speed * math.sin(angle), 0.0],
                            continue_condition=self._continue_condition
                        )
                    ]
                )





