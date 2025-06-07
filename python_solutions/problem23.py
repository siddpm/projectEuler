'''
Sketch of brute force solution:
    1. Generate all abundant numbers less than 28123
    2. Go through each number from 1 to 28123 and find 
    if it can be expressed as a sum of two abundant numbers.
    3. Sum all non-abundant numbers.
'''
from helpers import prime_factors
from time import time

def proper_divisors(prime_factors_dict):
    '''
    In this function I want to be able to extract all divisors 
    from their prime factors (and their exponents)
    '''
    divisor_set = set()
    for prime,exponent in prime_factors_dict.items():
        temp_lst = set()
        for i in range(exponent + 1):
            temp_lst.add(prime ** i)
        if divisor_set:
            divisor_lst_modify= divisor_set.copy()
            for val in temp_lst:
                for divisor in divisor_lst_modify:
                    divisor_set.add(val*divisor)
            
        divisor_set.update(temp_lst)
    
    # Finally to make it a proper set of divisors, we discard the max value which is n itself
    divisor_set.discard(max(divisor_set))
    
    return divisor_set
                

def abundant_numbers(limit = 13):
    abundant_numbers_lst = []

    for i in range(2,limit+1):
        prime_factors_dict = prime_factors(i)

        # get proper divisors
        proper_divisors_set = proper_divisors(prime_factors_dict)

        if sum(proper_divisors_set) > i:
            abundant_numbers_lst.append(i)
    
    return abundant_numbers_lst


def sum_non_abundant_numbers():
    abundant_nums = abundant_numbers(28123)

    sum_non_abundant_numbers_ = 0

    for i in range(28123):
        print(f"In number: {i}")

        for abundant_num in abundant_nums:
            if abundant_num > i:
                sum_non_abundant_numbers_ += i
                break

            if (i - abundant_num) in abundant_nums:
                break

    return sum_non_abundant_numbers_




# prime_factors_d = prime_factors(2)
# print(proper_divisors(prime_factors_d))
# print(len(abundant_numbers(28123)))
if __name__ == "__main__":
    
    start = time()
    print(sum_non_abundant_numbers())
    print("Total time:", time() - start)






