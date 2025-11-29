from helpers import prime_gen, is_prime


def trunctable_primes():
    primes = {}
    trunctable_prime_sum = 0

    gen = prime_gen()
    # storing 2,3,5,7
    primes[gen.__next__()] = None
    primes[gen.__next__()] = None
    primes[gen.__next__()] = None
    primes[gen.__next__()] = None

    count = 0
    for prime in gen:
        # store prime
        primes[prime] = None
        # Default value is True
        is_trunctable_prime = True

        prime_str = str(prime)

        for i in range(1, len(prime_str)):
            if is_prime(int(prime_str[i:])) and is_prime(int(prime_str[:-i])):
                pass
            else:
                is_trunctable_prime = False
                break

        if is_trunctable_prime:
            count += 1
            trunctable_prime_sum += prime

        if count == 11:
            break

    return trunctable_prime_sum


if __name__ == "__main__":
    print(trunctable_primes())
    print("incomplete")
