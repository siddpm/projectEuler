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