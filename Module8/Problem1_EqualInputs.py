# Abdyrakhman Raiapov
# November 15, 2026
# Problem 1 - A function that takes two inputs from the user and prints
# whether they are equal or not.
#
# If both inputs are numbers they are compared as numbers, so "5" and "5.0"
# count as equal; otherwise they are compared as text.


def to_number(text):
    """Returns the input as a float, or None if it is not a number."""
    try:
        return float(text)
    except ValueError:
        return None


def check_equal():
    first = input("Enter the first value: ").strip()
    second = input("Enter the second value: ").strip()

    a, b = to_number(first), to_number(second)
    if a is not None and b is not None:      # both are numbers
        same = (a == b)
    else:                                    # at least one is text
        same = (first == second)

    if same:
        print(first, "and", second, "are equal.")
    else:
        print(first, "and", second, "are not equal.")


check_equal()
