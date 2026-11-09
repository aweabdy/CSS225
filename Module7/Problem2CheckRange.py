# Abdyrakhman Raiapov
# Nov 8, 2026
# Problem 2 - A function that checks whether a number is in range(1, 10)
# and prints whether the number is in or not in the range.


def checkRange(number):
    """Prints whether number is in range(1, 10), i.e. 1 through 9.
    range(1, 10) stops before 10, so 10 is NOT in the range."""
    if number in range(1, 10):
        print(number, "is in the range(1, 10)")
    else:
        print(number, "is not in the range(1, 10)")


# Test values: inside, both edges, and outside the range
for value in [5, 1, 9, 10, 0, -3]:
    checkRange(value)
