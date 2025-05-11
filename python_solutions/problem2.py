def problem002(limit: int) -> int:
    """ Solution to problem2

    args:
        - limit : the termination limit once a fib value reaches this value

    returns:
        - sum of all even fibs below limit

    """
    sum_vals = 0
    fib1 = 0
    fib2 = 1

    while fib2 < limit:
        nxt_fib2 = fib1 + fib2
        fib1 = fib2
        fib2 = nxt_fib2

        if fib1 % 2 == 0:
            sum_vals += fib1

    return sum_vals