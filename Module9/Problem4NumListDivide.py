# Abdyrakhman Raiapov
# November 16, 2026
# Problem 4 - A while loop that starts a counter at 0 and runs until the
# counter reaches 50. Every value divisible by 10 is appended to the list
# called tens, and the list is printed at the end to confirm the result.
#
# The loop includes 50 itself (counter <= 50), because the counter
# "reaches" 50 on the last pass.

tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:               # remainder 0 means divisible by 10
        tens.append(counter)
    counter += 1

print("tens =", tens)
