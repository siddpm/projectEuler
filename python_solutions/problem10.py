"""Project Euler problems"""
from typing import List, Generator

from helpers import prime_gen
import time

def problem010(limit: int, gen: Generator[int, None, None]) -> int:
    sum_primes = 0
    for prime in gen:
        if prime > limit:
            break
        sum_primes += prime
    return sum_primes

if __name__ == "__main__":
    print(problem010(2000000, prime_gen()))