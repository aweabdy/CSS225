# Abdyrakhman Raiapov
# Nov 8, 2026
# Problem 5 - Uses the given drawSquare(t, sz) function as a base to draw
# five nested squares (sizes 20, 40, 60, 80, 100), all with the same center.
#
# After each square the turtle lifts its pen and moves 10 steps left and
# 10 steps down, so the next square (20 steps bigger) stays centered.

import turtle


def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

size = 20
for i in range(5):            # five squares
    drawSquare(alex, size)
    size = size + 20          # each square is 20 steps bigger
    alex.penup()              # move without drawing a line
    alex.backward(10)         # 10 steps to the left
    alex.right(90)
    alex.forward(10)          # 10 steps down
    alex.left(90)             # face right (east) again
    alex.pendown()

wn.exitonclick()
