# Abdyrakhman Raiapov
# Nov 3, 2026
# Problem 2 - Uses random.randrange to print an odd integer
# between 0 and 100.

import random

# randrange(start, stop, step): starting at 1 and stepping by 2 only
# produces odd numbers (1, 3, 5, ..., 99), so the result is always odd.
odd_number = random.randrange(1, 100, 2)
print("Random odd integer between 0 and 100:", odd_number)
