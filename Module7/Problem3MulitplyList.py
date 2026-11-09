# Abdyrakhman Raiapov
# Nov 8, 2026
# Problem 3 - A function that multiplies all the numbers in a list.
# Uses the list [5, 2, 7, -1].


def multiplyList(numbers):
    """Returns the product of all numbers in the list."""
    product = 1          # start at 1, because multiplying by 1 changes nothing
    for number in numbers:
        product = product * number
    return product


myList = [5, 2, 7, -1]
print("List:", myList)
print("Product of all the numbers:", multiplyList(myList))   # 5 * 2 * 7 * -1 = -70
