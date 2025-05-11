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
    # A simple proof by contradiction suffices
        # Assume a divisor d > sqrt(n), 
        # and d is a factor of n, such that n/d = r (r is a whole number)
        # From our assumptions, r > sqrt(n) (otherwise, we would've already found it)
        # But then the factor r*d must necessarily be > n. This contradicts our assumption. QED
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
