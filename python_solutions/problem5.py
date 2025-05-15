''' Observation 1: 
    We are able to delete some of the numbers from our list [1,2,3...20]
       Note that each of the numbers [1,2..10] is a factor of atleast one of the numbers [11..20]
       For example:
                   2 is a factor of - 12, 14, 16...
                   3 is a factor of - 12,15,18
                   4 is a factor of - 12, 16, 20
                   5 is a factor of - 15, 20
       Similarly for the rest of the numbers in [1..10]
       The importance is that a multiple of say 14, 28 is then also guaranteed to be divisible evenly by 2 and 4.
''' 

from helpers import gcd, lcm

def smallest_multiple_optimised():
    # List of values to consider
    # lst = [11,12...20] 
    lst = [i for i in range(11, 21)] 

    lcm_cumulative = lcm(lst[0], lst[1])

    for number in lst[2:]:
        lcm_cumulative = lcm(lcm_cumulative, number)

    return lcm_cumulative

print(smallest_multiple_optimised())