""" Helper functions for solving Project Euler problems """

import math
from typing import Generator


def is_prime(n: int) -> bool:

    # Edge case : 2 is prime by definition
    if n == 1:
        return False
    elif n == 2:
        return True

    # Only need to check divisors until sqrt(n)
    sqrt_n = math.isqrt(n)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True


def prime_gen() -> Generator[int, None, None]:

    # Starting candidate by prime definiton
    candidate = 2

    while True:
        if is_prime(candidate):
            yield candidate
        candidate += 1
