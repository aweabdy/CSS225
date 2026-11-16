# CSS-225 – Module 9: While Loops

**Author:** Abdyrakhman Raiapov  
**Course:** CSS-225, National Louis University  
**Date:** November 16, 2026

This folder contains my Module 9 Lab Activity programs. Each one repeats work with a
`while` loop: the loop body runs again and again as long as its condition is `True`.

| Problem | File | What it does |
|---|---|---|
| 1 | `Problem1Infinite.py` | An infinite loop (`while True`) that keeps printing `Infinite`. Stop it with **Ctrl+C**. |
| 2 | `Problem2NumList10.py` | Builds the list `L = [0, 1, ..., 10]` with a counter and `while counter <= 10`. |
| 3 | `Problem3NumList35.py` | Asks for numbers, adds them to a list and a running total, and stops once the sum is greater than 100. Non-numbers are rejected. |
| 4 | `Problem4NumListDivide.py` | Counts from 0 to 50 and appends every value divisible by 10, giving `tens = [0, 10, 20, 30, 40, 50]`. |

## Key idea

A `while` loop needs something inside the body that eventually makes the condition
`False` (here, `counter += 1` or the growing sum). Without it, the loop never ends,
which is exactly what Problem 1 shows on purpose.

## How to run

```
python Problem2NumList10.py
```

Python 3 is required.
