from typing import List, Generator

from helpers import prime_gen
import time

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

if __name__ == "__main__":
    print(problem003(600851475143, prime_gen()))