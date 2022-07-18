"""Project Euler problems"""
from typing import List, Generator

from helpers import prime_gen
import time


def problem001(limit: int) -> int:
    """ Solution to problem1
    args:
        - limit : the value until which we keep summing multiples of 3 and/or 5

    returns:
        - sum of all multiples of 3 and/or 5 below limit

    """

    sum_vals = 0
    for val in range(limit):
        if (val % 3 == 0) or (val % 5 == 0):
            sum_vals += val
    return sum_vals


def problem002(limit: int) -> int:
    """ Solution to problem2

    args:
        - limit : the termination limit once a fib value reaches this value

    returns:
        - sum of all even fibs below limit

    """
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
    """Solution to problem 3

    args:
        - num : the number to be factorised
        - gen : a prime number generator (see prime_gen in file helpers.py)

    returns:
        - a list of prime factors of num

    """
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


def problem007(n: int, gen: Generator[int, None, None]) -> int:
    """ Solution to problem 7

    args:
        - num : the " n'th " required prime number
                (ex. n = 7 indicates a request for the 7th prime)
        - gen : a prime number generator (see prime_gen in file helpers.py)

    returns:
        - a list of prime factors of num

    """
    counter = 1
    for prime in gen:
        if counter == n:
            return prime
        counter += 1


def problem010(limit: int, gen: Generator[int, None, None]) -> int:
    sum_primes = 0
    for prime in gen:
        if prime > limit:
            break
        sum_primes += prime
    return sum_primes


def problem004() -> int:
    largest_val = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            val = i * j
            str_val = str(val)

            if str_val == str_val[::-1]:
                if val > largest_val:
                    largest_val = val

    return largest_val


# print(problem010(2000000, prime_gen()))
