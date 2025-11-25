def fibonacci_1000_digit():
    fib_count = 2
    fib1 = 1
    fib2 = 1

    while True:
        fib_count += 1
        tmp_fib = fib2
        fib2 = fib1 + fib2
        fib1 = tmp_fib

        # I need to figure out when 1000th digit has been crossed.
        # Essentialy need to figure out if the new fib number is larger than 1000
        if len(str(fib2)) >= 1000:
            break

    return fib_count, fib2


if __name__ == "__main__":
    print("Fib count and actual fib numbers are: ", fibonacci_1000_digit())
