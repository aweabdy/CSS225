# CSS-225 – Module 7: Creating and Using Python Functions

**Author:** Abdyrakhman Raiapov  
**Course:** CSS-225, National Louis University  
**Date:** November 8, 2026

This folder contains my Module 7 Lab Activity programs. Each problem is solved with
a function (`def`) that is defined first and then called, and Problem 6 uses a class.

| Problem | File | What it does |
|---|---|---|
| 1 | `Problem1AreaOfCircle.py` | `areaOfCircle(r)` returns the area of a circle using `math.pi`. |
| 2 | `Problem2CheckRange.py` | `checkRange(n)` prints whether a number is in `range(1, 10)`. |
| 3 | `Problem3MulitplyList.py` | `multiplyList(list)` multiplies all numbers in `[5, 2, 7, -1]` (result: -70). |
| 4 | `Problem4Unique.py` | `uniqueList(list)` returns the unique elements of `[1, 3, 3, 3, 6, 2, 3, 5]` using `append`. |
| 5 | `Problem5Squares.py` | Uses `drawSquare(t, sz)` with turtle to draw five nested, centered squares. |
| 6 | `Problem6ClassCar.py` | The `car` class with new `type` and `manufacturer` attributes, their methods, and an updated `fullspecs()`. |

## Attribute vs. method (Problem 6)

An **attribute** is data stored in an object (for example `self.color`), while a
**method** is a function defined inside the class that works with that data (for
example `get_color()`).

## How to run

```
python Problem1AreaOfCircle.py
```

Python 3 is required; Problem 5 opens a turtle window (click it to close).
