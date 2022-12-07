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


def pi():
    return 3.141


exp_4 = alternate_binom_expansion(4)
print(stringify_binom(exp_4))
