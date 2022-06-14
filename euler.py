"""Project Euler problems"""

# Problem 1


def problem001(limit: int) -> int:
    """ Solution to problem1"""

    sum_vals = 0
    for val in range(limit):
        if (val % 3 == 0) or (val % 5 == 0):
            sum_vals += val
    return sum_vals


def problem002(limit: int) -> int:
    """ Solution to problem1"""
    sum_vals = 0
    fib1 = 0
    fib2 = 1

    while fib2 < limit:
        nxt_fib2 = fib1 + fib2
        fib1 = fib2
        fib2 = nxt_fib2

        if fib1 % 2 == 0:
            sum_vals += fib1

    return sum_vals

