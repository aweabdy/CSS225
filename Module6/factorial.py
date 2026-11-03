# Abdyrakhman Raiapov
# Nov 3, 2026
# Problem 6 - Uses a for statement to calculate the factorial of a
# user input value. Prints my result and the value from math.factorial().
#
# n! = 1 * 2 * 3 * ... * n, and 0! = 1 by definition.

import math

n = int(input("Enter a whole number (0 or more): "))

if n < 0:
    # factorial is not defined for negative numbers
    # (math.factorial would also raise an error)
    print("Factorial is only defined for 0 and positive whole numbers.")
else:
    result = 1                          # start at 1; this also covers 0! = 1
    for number in range(1, n + 1):      # 1, 2, ..., n
        result = result * number

    print("Factorial with a for loop:", result)
    print("math.factorial():", math.factorial(n))
