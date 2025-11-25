"""Helper functions for solving Project Euler problems"""

import math
from typing import Generator, Dict, List


def is_prime(n: int, primes: List[int] = []) -> bool:

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

    # Additionally, as all composite numbers can be factored into prime (fundamental theorem of arithmetic)
    # we only need to compare against previous primes below sqrt(n)
    sqrt_n = math.isqrt(n)

    if primes:

        for prime in primes:
            if prime > sqrt_n:
                break
            if n % prime == 0:
                return False
        return True

    else:

        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                return False
        return True


def prime_gen() -> Generator[int, None, None]:

    # keep a list of computed primes for reuse
    primes = [2]

    # Starting candidate by prime definiton
    yield primes[0]

    # We now only look at odd numbers as candidates for primality testing
    candidate = 3

    while True:
        if is_prime(candidate, primes):
            primes.append(candidate)
            yield candidate
        candidate += 2


def gcd(a: int, b: int) -> int:
    """
    Using Euclid's method of finding the greatest common divisor (GCD)
    tweaked to use the modulo function instead of simple subtraction
    """
    max_val = max(a, b)
    min_val = min(a, b)

    while True:
        remainder = max_val % min_val

        # Checks on the remainder
        if remainder == 0:
            return min_val

        # We need to continue with gcd, so update max and min respectively
        max_val = min_val
        min_val = remainder


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def prime_factors(n: int) -> Dict[int, int]:
    """
    General idea is to go through each prime from 2
    If 2 or next prime is a factor, we reduce the original number
    to : n/ prime and we repeat the process.
    This way we get all the exponents of the prime factors as well

    example, if we factor 28

    28 % 2 == 0 -> 2 is a factor, number reduced to 28/2 = 14
    14 % 2 == 0 -> 2 repeats again so we record an exponent of 2 and etc
    """

    # edge case
    if n == 1:
        return {1: 1}

    # store prime factors and their exponents
    prime_factors = {}

    gen = prime_gen()

    candidate = gen.__next__()

    while candidate <= n:

        # If prime candidate is a factor of n
        if n % candidate == 0:

            # Save prime factor
            # Check if prime factor already found previously
            if candidate in prime_factors:
                prime_factors[candidate] += 1
            else:
                prime_factors[candidate] = 1

            # reducing the original number . ex 28 / 2 = 14 and we continue with candidate 2
            n = n // candidate

            # exit condition
            if n == 1:
                break
        else:
            candidate = gen.__next__()

    return prime_factors
