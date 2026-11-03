# Abdyrakhman Raiapov
# Nov 3, 2026
# Problem 5 - Converts a user input value in radians to degrees.
# Prints my own calculation and the value from math.degrees().
#
# Formula (found online): degrees = radians * 180 / pi
# because a full circle is 2 * pi radians = 360 degrees.

import math

radians = float(input("Enter an angle in radians: "))

my_degrees = radians * 180 / math.pi      # my calculation
math_degrees = math.degrees(radians)      # math module function

print("My calculation:", my_degrees, "degrees")
print("math.degrees():", math_degrees, "degrees")
