"""Project Euler problems"""
from typing import List, Generator

from helpers import prime_gen
import time

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
