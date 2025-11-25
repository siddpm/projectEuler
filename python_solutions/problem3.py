from typing import List, Generator

from helpers import prime_factors
import time


def problem003(num: int) -> List[int]:
    """Solution to problem 3

    args:
        - num : the number to be factorised
        - gen : a prime number generator (see prime_gen in file helpers.py)

    returns:
        - a list of prime factors of num

    """
    prime_factors_dict = prime_factors(num)

    return max(prime_factors_dict)


if __name__ == "__main__":
    print(problem003(600851475143))
