# Abdyrakhman Raiapov
# Nov 3, 2026
# Problem 3 - Uses random.choice to select a day of the week
# from a list and print that day.

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

# random.choice picks one element from the list, each day equally likely
day = random.choice(days)
print("Random day of the week:", day)
