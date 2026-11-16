# Abdyrakhman Raiapov
# November 16, 2026
# Problem 2 - Uses a while loop to build a list L with the numbers 0 to 10.
# Each pass appends the counter to L and then adds 1 to the counter; the
# loop stops once the counter is greater than 10.

L = []
counter = 0

while counter <= 10:        # stops as soon as counter becomes 11 (> 10)
    L.append(counter)
    counter += 1

print("L =", L)
