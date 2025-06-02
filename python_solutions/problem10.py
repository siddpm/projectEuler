"""Project Euler problems"""
from typing import List, Generator

from helpers import prime_gen
from time import time

def problem010(limit: int, gen: Generator[int, None, None]) -> int:
    sum_primes = 0
    for prime in gen:
        if prime > limit:
            break
        sum_primes += prime
    return sum_primes

# This is Lucy_hedgehog's excellent solution,
# found at: https://projecteuler.net/thread=10&page=5

def lucy_hedgehog_solution(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]

# A sieve of erathosthenes approach for comparison - not my implmentation
def sieve_of_erathosthenes(n):
    sieve = [True] * n
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = [False] * len(sieve[i*i:n:i])
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)


if __name__ == "__main__":
    start = time()
    print(problem010(2000000, prime_gen()))
    print("Total time:", time() - start)

    start = time()
    print(lucy_hedgehog_solution(2000000))
    print("Lucy_Hedgehog solution", time() - start)

    start = time()
    print(sieve_of_erathosthenes(2000000))
    print("Total time:", time() - start)

