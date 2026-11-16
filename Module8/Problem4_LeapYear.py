# Abdyrakhman Raiapov
# November 15, 2026
# Problem 4 - A function that takes a year and returns True if it is a
# leap year and False otherwise.
#
# Rules: a year divisible by 4 is a leap year, EXCEPT years divisible by
# 100, which are not leap years UNLESS they are also divisible by 400.


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Test each rule: divisible by 4, by 100 (not leap), by 400 (leap), not by 4
for year in [2024, 2026, 1900, 2000, 2100, 1600]:
    print(year, "leap year?", is_leap_year(year))
