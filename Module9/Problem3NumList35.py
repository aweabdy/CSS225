# Abdyrakhman Raiapov
# November 16, 2026
# Problem 3 - Uses a while loop to ask the user for numbers. Each number is
# appended to a list and added to a running total. The loop keeps asking
# until the sum of the numbers is greater than 100.
#
# Input that is not a number is rejected with a message, so a typing mistake
# does not crash the program.

numbers = []
total = 0

while total <= 100:                     # keep going until the sum is > 100
    entry = input("Enter a number: ")
    try:
        value = float(entry)
    except ValueError:
        print('"' + entry + '" is not a number. Please try again.')
        continue                        # ask again without changing the list
    numbers.append(value)
    total += value
    print("Current sum:", total)

print("Numbers entered:", numbers)
print("Final sum:", total, "(greater than 100)")
