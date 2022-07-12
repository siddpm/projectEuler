"""Project Euler problems"""
from typing import List, Generator
from helpers import *


def problem001(limit: int) -> int:
    """ Solution to problem1"""

    sum_vals = 0
    for val in range(limit):
        if (val % 3 == 0) or (val % 5 == 0):
            sum_vals += val
    return sum_vals


def problem002(limit: int) -> int:
    """ Solution to problem2"""
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


def problem003(num: int, gen: Generator[int, None, None]) -> List[int]:
    """Solution to problem 3"""
    factors = []

    # initialise candidate with first prime
    candidate = gen.__next__()

    while candidate <= num:
        if num % candidate == 0:
            factors.append(candidate)
            num = num / candidate

            if num == 1:
                break
        else:
            candidate = gen.__next__()
    return factors


def problem007(num: int, gen: Generator[int, None, None]) -> int:
    counter = 1
    for prime in gen:
        if counter == num:
            return prime
        counter += 1


print(problem007(10001, prime_gen()))
