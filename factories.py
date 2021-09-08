from body import System
from body import Body
import math


class TwoBodyWithCenter:

    _center_mass = None
    _mass = 0.0
    _position = None
    _speeds = 0.0
    _angles = None

    def __init__(self, center_mass, mass, position, speeds, angles):
        self._center_mass = center_mass
        self._mass = mass
        self._position = position
        self._speeds = speeds
        self._angles = angles

    def make(self):

        for speed in self.speeds:
            for angle in self.angles:

                yield System(
                    bodies = [
                        Body(
                            mass=self._center_mass,
                            position=[0.0, 0.0, 0.0],
                            velocity=[0.0, 0.0, 0.0]
                        ),
                        Body(
                            mass=self._mass,
                            position=self._position,
                            velocity=[speed * math.cos(angle), speed * math.sin(angle), 0.0]
                        )
                    ]
                )





