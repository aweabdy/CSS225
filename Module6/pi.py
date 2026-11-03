# Abdyrakhman Raiapov
# Nov 3, 2026
# Problem 4 - Computes an approximation of pi using simple arithmetic
# and prints it next to math.pi from the math module.
#
# Method: the Leibniz series (found online)
#     pi / 4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
# Each term is 1 divided by the next odd number, and the sign
# switches between + and - every time. Adding more terms gets
# closer to the real value of pi.

import math

TERMS = 1000000          # how many terms of the series to add

total = 0.0
sign = 1                 # +1 for the first term, then -1, +1, ...
for k in range(TERMS):
    total = total + sign / (2 * k + 1)    # odd numbers: 1, 3, 5, ...
    sign = -sign                          # flip the sign for the next term

approx_pi = 4 * total    # the series gives pi / 4, so multiply by 4

print("Approximation of pi (Leibniz series,", TERMS, "terms):", approx_pi)
print("Value of math.pi:", math.pi)
print("Difference:", abs(math.pi - approx_pi))
