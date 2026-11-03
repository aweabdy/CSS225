# Abdyrakhman Raiapov
# Nov 3, 2026
# Problem 1 - Uses a for statement and random.randrange to print
# 10 random integers between 25 and 35.

import random

# randrange(start, stop) never returns "stop" itself,
# so 36 is used to make 35 one of the possible values (25..35).
for count in range(10):
    number = random.randrange(25, 36)
    print(number)
