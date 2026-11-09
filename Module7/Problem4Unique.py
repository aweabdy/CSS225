# Abdyrakhman Raiapov
# Nov 8, 2026
# Problem 4 - A function that takes a list of numbers and returns a new
# list with only the unique elements of the first list (no repeats).
# Uses the list [1, 3, 3, 3, 6, 2, 3, 5] and the append function.


def uniqueList(numbers):
    """Returns a new list with each number from numbers only once,
    in the order the numbers first appear."""
    unique = []
    for number in numbers:
        if number not in unique:      # add a number only the first time we see it
            unique.append(number)
    return unique


myList = [1, 3, 3, 3, 6, 2, 3, 5]
print("Original list:", myList)
print("Unique list:  ", uniqueList(myList))    # [1, 3, 6, 2, 5]
