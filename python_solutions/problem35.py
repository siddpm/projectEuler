from helpers import is_prime, prime_gen


def circular_primes():
    prime_count = 0
    gen = prime_gen()
    prime = gen.__next__()

    while prime <= 1_000_000:

        prime_candidates = rotate_digits(prime)

        if are_primes(prime_candidates):
            # print(prime)
            prime_count += 1

        prime = gen.__next__()

    return prime_count


def are_primes(prime_candidates: list[int]) -> bool:
    # Note: returns True if prime_candidates list is empty.
    #       This is desired behaviour
    for prime_candidate in prime_candidates:
        # print(prime_candidate)
        if not is_prime(prime_candidate):
            return False
    return True


def rotate_digits(num):
    num_str = str(num)
    lst = []

    if len(num_str) >= 2:
        for _ in range(len(num_str) - 1):
            temp_val = num_str[1:] + num_str[0]
            # print(temp_val)
            lst.append(int(temp_val))
            num_str = temp_val

    return lst


if __name__ == "__main__":
    print("The number of circular primes under 1 million are: ", circular_primes())
