# CSS-225 – Module 6: An Introduction to Python Modules

**Author:** Abdyrakhman Raiapov
**Course:** CSS-225, National Louis University
**Date:** November 3, 2026

This folder contains my Module 6 Lab Activity programs. Each program shows how to
`import` a module from the Python Standard Library and call its functions with dot
notation (for example `random.choice(days)` or `math.factorial(n)`).

## Programs

| Problem | File | Module | What it does |
|---|---|---|---|
| 1 | `randomrange.py` | `random` | Uses a `for` loop and `random.randrange` to print 10 random integers between 25 and 35. |
| 2 | `randomint.py` | `random` | Uses `random.randrange(1, 100, 2)` to print a random **odd** integer between 0 and 100. |
| 3 | `randomday.py` | `random` | Uses `random.choice` to pick and print a random day of the week from a list. |
| 4 | `pi.py` | `math` | Approximates pi with the Leibniz series (1 − 1/3 + 1/5 − …) and prints it next to `math.pi`. |
| 5 | `degrees.py` | `math` | Converts a user-entered angle from radians to degrees (`radians * 180 / pi`) and compares it with `math.degrees()`. |
| 6 | `factorial.py` | `math` | Calculates the factorial of a user-entered number with a `for` loop and compares it with `math.factorial()`. |

## How to run

Python 3 is required. No extra packages are needed, because `random` and `math`
come with Python.

```
python randomrange.py
python factorial.py
```

Programs 5 and 6 ask for input. For example, entering `5` in `factorial.py` prints
`120` from both the loop and `math.factorial()`.

## Notes

- `random.randrange(start, stop)` never returns `stop`, so Problem 1 uses
  `randrange(25, 36)` to include 35.
- The pi approximation in Problem 4 uses 1,000,000 terms and is within about
  0.000001 of `math.pi`.
- `factorial.py` checks for negative input, because factorial is only defined for
  0 and positive whole numbers.
