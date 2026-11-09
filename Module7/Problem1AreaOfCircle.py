# Abdyrakhman Raiapov
# Nov 8, 2026
# Problem 1 - areaOfCircle(r) returns the area of a circle of radius r.
# Uses math.pi from the math module: area = pi * r^2

import math


def areaOfCircle(r):
    """Returns the area of a circle with radius r."""
    return math.pi * r ** 2


# Calling the function with a few sample radii
for radius in [1, 2.5, 10]:
    print("Radius:", radius, "-> area:", round(areaOfCircle(radius), 2))
