"""
In this file I will be writing a scrip that uses Newton's method
of calculating Pi to a desired accuracy
"""
import math

"""
The following function will return the binomial expansion of (x + 1)^n

args: n
return : a list of tuples of the form: (coefficient, power of x)
"""


def stringify_binom(lst_binom: list[tuple[int, int]]) -> str:
    return_str = ""
    for coefficient, power in lst_binom:
        return_str += " " + str(coefficient) + "x^" + str(power)
    return return_str


def binomial_expansion(n: int) -> list[tuple[int, int]]:
    return_list = []

    for i in range(n + 1):
        binom_coeff = binom_coefficient(n, i)

        # convert to int
        binom_coeff = int(binom_coeff)

        # getting the power of x
        x_power = n - i
        return_list.append((binom_coeff, x_power))

    return list(reversed(return_list))


def alternate_binom_expansion(n):
    lst = [(1, 0), (n, 1)]

    for i in range(2, n + 1):
        coeff = n
        for j in range(1, i):
            coeff *= n - j
        coeff = int(coeff / math.factorial(i))
        lst.append((coeff, i))
    return lst


def binom_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


# I need a binomial expansion that expands to an infinite series


def binom_infinit(n, x_sign, x_power, stop_iter=10):
    lst = [(1, 0), (x_sign * n, x_power)]

    i = 2

    while True:
        coeff = n
        for j in range(1, i):
            coeff *= n - j
        # coeff = int(coeff / math.factorial(i))
        coeff = coeff / math.factorial(i)
        if (i % 2) != 0:
            coeff *= x_sign

        x_val = i * x_power
        print(coeff, x_val)
        lst.append((coeff, x_val))
        i += 1

        if i == stop_iter:
            break
    return lst


def integrate_expansion(lst_binom):
    result_list = []
    for coeff, power in lst_binom:
        result_list.append((coeff / (power + 1), power + 1))
    return result_list


def pi_old(terms=10):
    binom_series = binom_infinit(0.5, -1, 2, stop_iter=terms)
    series = integrate_expansion(binom_series)
    sum_val = 0
    for coeff, _ in series:
        sum_val += coeff
    sum_val *= 4

    return sum_val


def pi_improved(terms=10):
    binom_series = binom_infinit(0.5, -1, 2, stop_iter=terms)
    series = integrate_expansion(binom_series)
    sum_val = 0
    for coeff, power in series:
        sum_val += coeff * ((0.5) ** power)

    sum_val = sum_val - (math.sqrt(3) / 8)
    sum_val *= 12

    return sum_val


res = pi_improved(100)
print(res)
