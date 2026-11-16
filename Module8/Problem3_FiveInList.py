# Abdyrakhman Raiapov
# November 15, 2026
# Problem 3 - A function that takes a list and prints whether the value 5
# is in that list.


def check_for_five(numbers):
    # "in" is a Boolean operator: it is True if 5 is one of the items
    if 5 in numbers:
        print(numbers, "-> 5 is in the list")
    else:
        print(numbers, "-> 5 is not in the list")


# Tests: 5 in the middle, 5 missing, an empty list, and 5 at the end
check_for_five([1, 3, 5, 7])
check_for_five([2, 4, 6, 8])
check_for_five([])
check_for_five([10, 20, 5])
