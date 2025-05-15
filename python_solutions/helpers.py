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

def gcd(a: int,b: int) -> int:
    '''
    Using Euclid's method of finding the greatest common divisor (GCD)
    tweaked to use the modulo function instead of simple subtraction
    '''
    max_val = max(a,b)
    min_val = min(a,b)

    while True:
        remainder = max_val % min_val

        # Checks on the remainder
        if remainder == 0:
            return min_val
        
        # We need to continue with gcd, so update max and min respectively
        max_val = min_val
        min_val = remainder

def lcm(a: int,b: int) -> int:
    return a*b // gcd(a,b)
