# Abdyrakhman Raiapov
# November 15, 2026
# Problem 2 - A function that takes two numbers from the user and prints
# whether their sum is greater than 10, less than 10, or equal to 10.


def read_number(prompt):
    """Keeps asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def compare_sum():
    a = read_number("Enter the first number: ")
    b = read_number("Enter the second number: ")
    total = a + b

    # exactly one of the three branches runs
    if total > 10:
        print("The sum", total, "is greater than 10.")
    elif total < 10:
        print("The sum", total, "is less than 10.")
    else:
        print("The sum", total, "is equal to 10.")


compare_sum()
